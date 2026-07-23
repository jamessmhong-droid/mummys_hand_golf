#!/usr/bin/env python3
"""Validate the static GitHub Pages artifact without third-party packages."""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


EXTERNAL_SCHEMES = {
    "data",
    "http",
    "https",
    "javascript",
    "mailto",
    "sms",
    "tel",
}
PARITY_TREES = ("v3", "v4", "v5")
PARITY_FILES = ("practice-guide.html", "series.html")


class PageParser(HTMLParser):
    def __init__(self, source: str) -> None:
        super().__init__(convert_charrefs=True)
        self.source = source
        self.line_offsets = [0]
        for line in source.splitlines(keepends=True):
            self.line_offsets.append(self.line_offsets[-1] + len(line))
        self.html_lang: str | None = None
        self.in_title = False
        self.title_parts: list[str] = []
        self.has_viewport = False
        self.description: str | None = None
        self.targets: list[tuple[str, str]] = []
        self.images_without_alt = 0
        self.document_markers: dict[str, list[int]] = {
            "doctype": [],
            "html_open": [],
            "head_open": [],
            "head_close": [],
            "body_open": [],
            "body_close": [],
            "html_close": [],
        }
        self.html_close_ends: list[int] = []

    def source_offset(self) -> int:
        line, column = self.getpos()
        return self.line_offsets[line - 1] + column

    def handle_decl(self, decl: str) -> None:
        if decl.strip().lower().startswith("doctype"):
            self.document_markers["doctype"].append(self.source_offset())

    def handle_starttag(
        self, tag: str, attrs_list: list[tuple[str, str | None]]
    ) -> None:
        tag = tag.lower()
        attrs = {key.lower(): value for key, value in attrs_list}
        marker = f"{tag}_open"
        if marker in self.document_markers:
            self.document_markers[marker].append(self.source_offset())
        if tag == "html" and self.html_lang is None:
            self.html_lang = attrs.get("lang")
        elif tag == "title":
            self.in_title = True
        elif tag == "meta":
            name = (attrs.get("name") or "").strip().lower()
            if name == "viewport":
                self.has_viewport = True
            elif name == "description":
                self.description = attrs.get("content")
        elif tag == "img" and "alt" not in attrs:
            self.images_without_alt += 1

        for attribute in ("href", "src"):
            value = attrs.get(attribute)
            if value:
                self.targets.append((attribute, value.strip()))

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        marker = f"{tag}_close"
        if marker in self.document_markers:
            position = self.source_offset()
            self.document_markers[marker].append(position)
            if tag == "html":
                closing_bracket = self.source.find(">", position)
                self.html_close_ends.append(
                    len(self.source) if closing_bracket < 0 else closing_bracket + 1
                )
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def local_target(site: Path, page: Path, raw: str) -> Path | None:
    if not raw or raw.startswith(("#", "//")):
        return None

    parsed = urlsplit(raw)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
        return None
    if parsed.scheme:
        return None

    path = unquote(parsed.path)
    if not path:
        return None
    if path.startswith("/"):
        target = site / path.lstrip("/")
    else:
        target = page.parent / path
    return target.resolve()


def validate_page(site: Path, page: Path) -> list[str]:
    errors: list[str] = []
    relative = page.relative_to(site).as_posix()
    try:
        source = page.read_text(encoding="utf-8")
        parser = PageParser(source)
        parser.feed(source)
    except (OSError, UnicodeError) as exc:
        return [f"{relative}: cannot read as UTF-8 ({exc})"]

    marker_names = (
        "doctype",
        "html_open",
        "head_open",
        "head_close",
        "body_open",
        "body_close",
        "html_close",
    )
    counts = {
        name: len(parser.document_markers[name])
        for name in marker_names
    }
    if any(count != 1 for count in counts.values()):
        summary = ", ".join(
            f"{name.replace('_', ' ')}={counts[name]}"
            for name in marker_names
            if counts[name] != 1
        )
        errors.append(f"{relative}: document structure requires exactly one tag ({summary})")
    else:
        positions = [parser.document_markers[name][0] for name in marker_names]
        if positions != sorted(positions) or len(set(positions)) != len(positions):
            errors.append(
                f"{relative}: invalid document order; expected doctype < html < head "
                "< /head < body < /body < /html"
            )
        html_end = parser.html_close_ends[0]
        if source[html_end:].strip():
            errors.append(f"{relative}: non-whitespace content after </html>")

    if parser.html_lang != "ko":
        errors.append(f"{relative}: <html> must have lang=\"ko\"")
    if not "".join(parser.title_parts).strip():
        errors.append(f"{relative}: missing or empty <title>")
    if not parser.has_viewport:
        errors.append(f"{relative}: missing viewport meta tag")
    if not (parser.description or "").strip():
        errors.append(f"{relative}: missing or empty meta description")
    if parser.images_without_alt:
        errors.append(
            f"{relative}: {parser.images_without_alt} <img> tag(s) missing alt"
        )

    for attribute, raw in parser.targets:
        target = local_target(site, page, raw)
        if target is None:
            continue
        try:
            target.relative_to(site.resolve())
        except ValueError:
            errors.append(f"{relative}: {attribute} escapes site root: {raw}")
            continue
        exists = target.exists()
        if target.is_dir():
            exists = (target / "index.html").is_file()
        if not exists:
            errors.append(f"{relative}: missing {attribute} target: {raw}")
    return errors


def compare_pair(root: Path, left: Path, right: Path, label: str) -> list[str]:
    if not left.is_file():
        return [f"parity {label}: missing {left.relative_to(root).as_posix()}"]
    if not right.is_file():
        return [f"parity {label}: missing {right.relative_to(root).as_posix()}"]
    if left.read_bytes() != right.read_bytes():
        return [f"parity {label}: files differ"]
    return []


def validate_parity(root: Path, site: Path) -> list[str]:
    errors: list[str] = []
    for tree_name in PARITY_TREES:
        source = root / tree_name
        deployed = site / tree_name
        source_files = {
            path.relative_to(source).as_posix()
            for path in source.rglob("*")
            if path.is_file()
        }
        deployed_files = {
            path.relative_to(deployed).as_posix()
            for path in deployed.rglob("*")
            if path.is_file()
        }
        for relative in sorted(source_files | deployed_files):
            errors.extend(
                compare_pair(
                    root,
                    source / relative,
                    deployed / relative,
                    f"{tree_name}/{relative}",
                )
            )

    for relative in PARITY_FILES:
        errors.extend(
            compare_pair(
                root,
                root / relative,
                site / relative,
                relative,
            )
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (default: inferred from script location)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    site = root / "site"
    if not site.is_dir():
        print(f"ERROR: site directory not found: {site}", file=sys.stderr)
        return 2

    pages = sorted(site.rglob("*.html"))
    errors = [
        error
        for page in pages
        for error in validate_page(site, page)
    ]
    errors.extend(validate_parity(root, site))

    if errors:
        print(f"Site validation failed: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Site validation passed: {len(pages)} HTML page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
