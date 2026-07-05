# -*- coding: utf-8 -*-
# Version 2 — expert content, V1 (pink card) design. Reuses golf_data.json.
import os, json, html

OUT = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.join(OUT, "v2")
V2PAGES = os.path.join(V2, "pages")
os.makedirs(V2PAGES, exist_ok=True)

data = json.load(open(os.path.join(OUT, "golf_data.json"), encoding="utf-8"))
papers = {int(k): v for k, v in data["papers"].items()}
dups = {int(k): v for k, v in data["dups"].items()}
partA = data["partA"]
partB = data["partB"]

def esc(s): return html.escape(str(s))

def ref_chips(p):
    """Clickable DOI/PMID/URL anchors for a paper (no wrapper)."""
    out = []
    for r in p.get("refs", []):
        k = r.get("kind")
        if k == "PMID":
            url, label = f"https://pubmed.ncbi.nlm.nih.gov/{r['id']}/", f"PMID {r['id']}"
        elif k == "DOI":
            url, label = f"https://doi.org/{r['id']}", f"DOI {r['id']}"
        else:
            url, label = r["url"], r.get("label", "원문 링크")
        out.append(f"<a class='reflink' href='{esc(url)}' target='_blank' rel='noopener'>"
                   f"{esc(label)} <span class='ext'>↗</span></a>")
    return "".join(out)

def ref_links(p):
    chips = ref_chips(p)
    return f"<div class='reflinks'><span class='reflab'>원문</span>{chips}</div>" if chips else ""

# study-design label + methodological caveat (grounded per paper)
meta = {
 1:("종설 · Narrative review","자체 표본 없음. 체계적 검색 기반이 아니어서 선택적 인용 가능성이 있다."),
 2:("중재 · 전후 비교(N=15)","대조군 없는 8주 pre–post 설계. 학습·계절 효과를 배제하기 어렵고 중년 남성에 한정된다."),
 3:("단면 상관연구(N=100)","상관은 인과가 아니며 r≈0.5–0.6로 설명력은 중간 수준이다."),
 4:("준실험 · 집단 비교(N=19)","소표본·학회 발표 기반. 5번 아이언 한정, 전자기 추적 30 Hz의 시간해상도 한계."),
 5:("기술적 운동학(N=8)","소표본·저핸디캡 남성 한정. 초록 수준 정보로 세부 수치가 제한된다."),
 6:("무작위 대조시험(RCT, N=20)","소표본·남성 한정, 2D 분석·클럽스피드 대리지표. +24%는 5주 반복 후 값이다."),
 7:("역학 모델링/시뮬레이션(N=4)","실측이 아닌 계산값이며 표본 다양성이 낮다."),
 8:("단면 회귀분석(N=308)","설명분산 기반으로 인과가 아니며 볼 스피드를 종속변수로 한다."),
 9:("이론·관점(Viewpoint)","실증 데이터·통계가 없다. 실증적 주장은 별도 연구의 소관이다."),
 10:("3D 운동학 · 집단 비교(N=10)","소표본·2 m 실내 퍼트 한정. 성공률 컷오프(79%)는 표본 의존적이다."),
 11:("관측 데이터 분석(ShotLink)","PGA 엘리트 대상. 투어 프로 집단 특성이라 아마추어로 일반화에 주의."),
 12:("단행본 · 다학제 연구(1968)","당시 장비·표본 기준. 일부 모델은 후속 연구로 정교화되었다."),
 13:("체계적 문헌 리뷰(9편)","전완 근육이 과소대표되며 대부분 저핸디캡·오른손잡이 남성 대상."),
 16:("3D 운동학 · 집단 비교(프로10·아마5)","소표본·집단 크기 불균형. 초록 기반으로 세부가 제한된다."),
 17:("종설 · Review","자체 데이터 없음. 인용 연구 간 이질성이 존재한다."),
 18:("단면 코호트(N=257)","드라이빙 거리 자가보고, 남성·오른손잡이 한정이며 인과가 아니다."),
 19:("종설 · Review","정량 결과 미제시, 개념적 통합 위주."),
 20:("임상 리뷰","자체 데이터 없음. 인용 중재연구들의 표본·설계가 이질적이다."),
}

# ---- V1 base CSS (verbatim theme) ----
BASE = """
:root{--bg:#FDEEF3;--bg-soft:#FCE4EC;--hot:#FF1E88;--hot-deep:#E60F73;--ink:#0E0E10;--white:#FFFFFF;--line:#F4C9DC;--muted:#6B5560;}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:'Pretendard','Apple SD Gothic Neo','Segoe UI',system-ui,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased;}
"""

# ---- shared reference-link chips (used on detail cite box + index bibliography) ----
REFLINK_CSS = """
.reflinks{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:13px;padding-top:13px;border-top:1px dashed var(--line)}
.reflinks.bib{margin-top:9px;padding-top:0;border-top:none}
.reflab{font-size:11px;font-weight:800;letter-spacing:.1em;color:var(--muted);text-transform:uppercase}
.reflink{display:inline-flex;align-items:center;gap:5px;font-size:12.5px;font-weight:800;text-decoration:none;background:var(--white);color:var(--hot-deep);border:1.5px solid var(--hot);padding:5px 12px;border-radius:999px;transition:background .15s ease,color .15s ease}
.reflink:hover{background:var(--hot);color:#fff}
.reflink .ext{font-weight:700;opacity:.8}
"""

# ---- detail page (V1 look + expert content) ----
DETAIL_CSS = BASE + REFLINK_CSS + """
.wrap{max-width:760px;margin:0 auto;padding:32px 22px 88px}
.back{display:inline-flex;align-items:center;gap:7px;font-size:14px;font-weight:700;color:var(--hot-deep);text-decoration:none;margin-bottom:26px}
.back:hover{color:var(--ink)}
.part{display:inline-block;background:var(--ink);color:var(--white);font-size:12px;font-weight:800;letter-spacing:.1em;padding:5px 13px;border-radius:999px}
h1{font-size:30px;font-weight:900;letter-spacing:-.02em;line-height:1.3;margin:18px 0 14px}
.cite{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:16px 18px;font-size:14px;color:var(--muted);margin-bottom:14px}
.cite b{color:var(--ink)}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.pill{display:inline-block;background:var(--hot);color:#fff;font-size:12px;font-weight:800;padding:4px 12px;border-radius:999px}
.pill.k{background:var(--ink)}
.badges{display:flex;flex-wrap:wrap;gap:7px;margin:16px 0 30px}
.tag{font-size:12px;font-weight:700;background:var(--bg-soft);color:var(--hot-deep);padding:5px 12px;border-radius:999px;border:1px solid var(--line)}
.lead{font-size:17px;line-height:1.75;background:var(--white);border-left:5px solid var(--hot);border-radius:0 14px 14px 0;padding:18px 22px;margin-bottom:34px}
h2{font-size:15px;font-weight:900;letter-spacing:.02em;color:var(--hot-deep);text-transform:uppercase;margin:0 0 14px;display:flex;align-items:center;gap:9px}
h2::before{content:"";width:10px;height:10px;background:var(--hot);border-radius:3px;display:inline-block}
section{margin-bottom:34px}
.findings{list-style:none;counter-reset:f}
.findings li{counter-increment:f;background:var(--white);border:1px solid var(--line);border-radius:14px;padding:15px 16px 15px 52px;margin-bottom:11px;font-size:15px;position:relative}
.findings li::before{content:counter(f);position:absolute;left:14px;top:14px;width:26px;height:26px;background:var(--hot);color:#fff;font-weight:900;font-size:13px;border-radius:8px;display:flex;align-items:center;justify-content:center}
.findings b{color:var(--hot-deep)}
.box{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:16px 18px;font-size:15px}
.take{background:var(--ink);color:#fff;border-radius:16px;padding:20px 22px;font-size:16px;font-weight:700;line-height:1.6}
.take span{color:var(--hot);display:block;font-size:12px;letter-spacing:.14em;margin-bottom:8px;font-weight:800}
.limit{background:var(--white);border:1px solid var(--line);border-left:5px solid var(--ink);border-radius:0 14px 14px 0;padding:16px 18px;font-size:15px;line-height:1.7}
.limit .lab{display:block;font-size:12px;font-weight:800;letter-spacing:.1em;color:var(--ink);text-transform:uppercase;margin-bottom:7px}
h3{font-size:14px;font-weight:900;color:var(--ink);margin:0 0 10px;padding-bottom:8px;border-bottom:2px solid var(--hot)}
.prog{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.progcol{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:16px 16px}
.progcol ul{list-style:none;margin:0;padding:0}
.progcol li{font-size:13.5px;padding:7px 0;border-bottom:1px dashed var(--line);line-height:1.45}
.progcol li:last-child{border-bottom:none}
.progcol .b{display:inline-block;font-size:10px;font-weight:800;background:var(--hot);color:#fff;padding:1px 7px;border-radius:999px;margin-left:4px;vertical-align:middle}
.note{font-size:12.5px;color:var(--muted);margin-top:14px;line-height:1.6}
.note b{color:var(--ink)}
.dtab{width:100%;border-collapse:collapse;background:var(--white);border-radius:14px;overflow:hidden;border:1px solid var(--line);font-size:13.5px}
.dtab th{background:var(--ink);color:#fff;padding:11px 10px;text-align:center;font-weight:800;font-size:12.5px;line-height:1.3}
.dtab td{padding:10px 10px;text-align:center;border-bottom:1px solid var(--line)}
.dtab td:first-child{text-align:left;font-weight:700}
.dtab tbody tr:last-child td{border-bottom:none}
.dtab tbody tr:nth-child(even){background:var(--bg-soft)}
.foot{margin-top:40px;text-align:center}
.foot a{color:var(--hot-deep);font-weight:700;text-decoration:none;font-size:14px}
@media(max-width:640px){.prog{grid-template-columns:1fr}.dtab{font-size:12px}.dtab th,.dtab td{padding:8px 6px}}
@media(max-width:520px){h1{font-size:24px}.wrap{padding:24px 15px 64px}}
"""

# ---- Branding: mascot favicon, Instagram footer, card corner watermark ----
IG_URL = "https://www.instagram.com/mummys_hand_golf/"
IG_HANDLE = "@mummys_hand_golf"

BRAND_CSS = """
.wrap{position:relative}
.brand{margin-top:56px;padding-top:26px;border-top:1px solid var(--line);display:flex;flex-direction:column;align-items:center;gap:11px;text-align:center}
.brand>img{width:48px;height:48px;filter:drop-shadow(0 6px 12px rgba(230,15,115,.35))}
.brand-ig{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:800;color:var(--hot-deep);text-decoration:none}
.brand-ig:hover{color:var(--ink)}
.cardwm{position:absolute;top:16px;right:16px;z-index:5;display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.74);-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);border:1px solid var(--line);border-radius:999px;padding:5px 12px 5px 6px;text-decoration:none;box-shadow:0 4px 14px -6px rgba(230,15,115,.45)}
.cardwm img{width:26px;height:26px}
.cardwm span{font-size:12px;font-weight:800;color:var(--hot-deep);letter-spacing:.01em}
"""

def favicon_links(prefix):
    return (f'<link rel="icon" type="image/png" href="{prefix}assets/favicon.png">'
            f'<link rel="apple-touch-icon" href="{prefix}assets/mascot.png">')

_IG_SVG = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
           '<rect x="2" y="2" width="20" height="20" rx="5.5"/><circle cx="12" cy="12" r="4"/>'
           '<circle cx="17.6" cy="6.4" r="1.1" fill="currentColor" stroke="none"/></svg>')

NAV_CSS = (
 ".sitenav{display:flex;flex-wrap:wrap;justify-content:center;gap:5px;margin:0 auto 18px;padding:0 12px}"
 ".sitenav a{font-size:12.5px;font-weight:800;color:var(--muted);text-decoration:none;padding:7px 13px;"
 "border-radius:999px}"
 ".sitenav a:hover{color:var(--hot-deep);background:var(--bg-soft)}"
 ".sitenav a.cur{color:#fff;background:var(--hot)}"
)

def nav(prefix, cur):
    items = [("index.html", "🏠 홈", "home"),
             ("golf-research-summary.html", "V1 카드", "v1"),
             ("v2/golf-research-v2.html", "V2 근거", "v2"),
             ("v3/index.html", "V3 딥다이브", "v3")]
    out = []
    for href, label, key in items:
        c = ' class="cur"' if key == cur else ''
        out.append(f'<a href="{prefix}{href}"{c}>{label}</a>')
    return '<nav class="sitenav">' + "".join(out) + '</nav>'

def brand_footer(prefix):
    return (f'<div class="brand"><img src="{prefix}assets/mascot.png" alt="마미손 골프 마스코트">'
            f'<a class="brand-ig" href="{IG_URL}" target="_blank" rel="noopener">'
            f'{_IG_SVG}{IG_HANDLE}</a></div>')

def card_watermark(prefix):
    return (f'<a class="cardwm" href="{IG_URL}" target="_blank" rel="noopener" '
            f'aria-label="Instagram {IG_HANDLE}"><img src="{prefix}assets/wm.png" alt="">'
            f'<span>{IG_HANDLE}</span></a>')

def detail(pid, p):
    st, caveat = meta.get(pid, ("연구",""))
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in p["tags"])
    findings = "".join(f"<li>{f}</li>" for f in p["findings"])
    extra = p.get("extra", "")
    h = []
    h.append("<!DOCTYPE html><html lang='ko'><head><meta charset='UTF-8'>")
    h.append("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
    h.append(f"<title>{esc(p['title'])} — 전문가용 (V2)</title>")
    h.append(favicon_links("../../"))
    h.append(f"<style>{DETAIL_CSS}{BRAND_CSS}{NAV_CSS}</style></head><body><div class='wrap'>")
    h.append(card_watermark("../../"))
    h.append(nav("../../", "v2"))
    h.append("<a class='back' href='../golf-research-v2.html'>← 근거 자료집(V2)으로 돌아가기</a>")
    h.append(f"<div><span class='part'>{esc(p['part'])} · No.{pid:02d}</span></div>")
    h.append(f"<h1>{esc(p['title'])}</h1>")
    h.append(f"<div class='cite'><b>{esc(p['authors'])}</b><br>{esc(p['journal'])}"
             f"<div class='pills'><span class='pill k'>{esc(st)}</span>"
             f"<span class='pill'>{esc(p['cites'])}</span></div>{ref_links(p)}</div>")
    h.append(f"<div class='badges'>{tags}</div>")
    h.append(f"<p class='lead'>{p['summary']}</p>")
    h.append(f"<section><h2>핵심 결과 · Findings</h2><ol class='findings'>{findings}</ol></section>")
    h.append(f"<section><h2>연구 설계·방법 · Methods</h2><div class='box'>{p['method']}</div></section>")
    if extra:
        h.append(extra)
    h.append(f"<section><h2>해석과 함의 · Interpretation</h2><div class='box'>{p['significance']}</div></section>")
    h.append(f"<section><div class='limit'><span class='lab'>한계·유의 · Limitations</span>{esc(caveat)}</div></section>")
    h.append(f"<div class='take'><span>BOTTOM LINE</span>{esc(p['takeaway'])}</div>")
    h.append("<div class='foot'><a href='../golf-research-v2.html'>← 목록으로</a></div>")
    h.append(brand_footer("../../"))
    h.append("</div></body></html>")
    return "".join(h)

for pid, p in papers.items():
    with open(os.path.join(V2PAGES, f"paper-{pid:02d}.html"), "w", encoding="utf-8") as f:
        f.write(detail(pid, p))

# ---- index (V1 card look + expert framing) ----
INDEX_CSS = BASE + REFLINK_CSS + """
.wrap{max-width:920px;margin:0 auto;padding:56px 24px 96px}
.hero{text-align:center;padding:40px 0 40px;border-bottom:3px solid var(--hot)}
.kicker{display:inline-block;background:var(--ink);color:#fff;font-size:13px;font-weight:800;letter-spacing:.14em;padding:7px 16px;border-radius:999px;margin-bottom:22px}
.hero h1{font-size:38px;font-weight:900;letter-spacing:-.02em;line-height:1.22}
.hero h1 span{color:var(--hot)}
.hero p{margin-top:16px;color:var(--muted);font-size:16px;max-width:660px;margin-left:auto;margin-right:auto}
.switch{display:inline-block;margin-top:18px;font-size:13px;font-weight:800;color:var(--hot-deep);border:1px solid var(--line);background:var(--white);border-radius:999px;padding:8px 16px;text-decoration:none}
.switch:hover{background:var(--bg-soft)}
.sec{margin-top:64px}
.sec-head{display:flex;align-items:baseline;gap:14px;margin-bottom:8px}
.sec-num{font-size:15px;font-weight:900;color:#fff;background:var(--ink);padding:4px 12px;border-radius:8px;letter-spacing:.05em}
.sec-head h2{font-size:26px;font-weight:900;letter-spacing:-.01em}
.sec-sub{color:var(--muted);font-size:14px;margin-bottom:28px;padding-left:2px}
.card{display:block;text-decoration:none;color:inherit;background:var(--white);border-radius:18px;padding:24px 26px;margin-bottom:18px;border:1px solid var(--line);box-shadow:0 6px 22px -14px rgba(230,15,115,.35);position:relative;transition:transform .15s ease,box-shadow .15s ease}
.card:hover{transform:translateY(-3px);box-shadow:0 14px 30px -14px rgba(230,15,115,.55)}
.card::before{content:"";position:absolute;left:0;top:22px;bottom:22px;width:5px;background:var(--hot);border-radius:0 6px 6px 0}
.card-top{display:flex;align-items:flex-start;gap:16px;margin-bottom:12px}
.no{flex:0 0 auto;width:42px;height:42px;border-radius:12px;background:var(--hot);color:#fff;font-size:19px;font-weight:900;display:flex;align-items:center;justify-content:center}
.meta{flex:1}
.title{font-size:18px;font-weight:800;letter-spacing:-.01em;line-height:1.4}
.cite{font-size:13px;color:var(--muted);margin-top:4px}
.badges{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}
.tag{font-size:11px;font-weight:700;letter-spacing:.03em;background:var(--bg-soft);color:var(--hot-deep);padding:4px 10px;border-radius:999px;border:1px solid var(--line)}
.tag.design{background:var(--ink);color:#fff;border-color:var(--ink)}
.tag.dup{background:var(--hot-deep);color:#fff;border-color:var(--hot-deep)}
.finding{font-size:14.5px;color:var(--ink);padding-left:2px}
.more{display:inline-block;margin-top:12px;font-size:13px;font-weight:800;color:var(--hot-deep);letter-spacing:.02em}
.card:hover .more{color:var(--ink)}
.footnote{margin-top:64px;padding:22px 24px;background:var(--white);border-radius:16px;border:1px dashed var(--line);font-size:13px;color:var(--muted);line-height:1.7}
.footnote b{color:var(--ink)}
.refsec{margin-top:72px}
.refsec .sec-head{margin-bottom:8px}
.refsec-sub{color:var(--muted);font-size:14px;margin-bottom:24px}
.reflist{list-style:none;margin:0;padding:0}
.reflist li{display:flex;gap:14px;background:var(--white);border:1px solid var(--line);border-radius:14px;padding:15px 17px;margin-bottom:11px}
.rnum{flex:0 0 auto;width:30px;height:30px;border-radius:9px;background:var(--ink);color:#fff;font-weight:900;font-size:13px;display:flex;align-items:center;justify-content:center}
.rtxt{font-size:13.5px;line-height:1.6}
.rtxt .rt-title{font-weight:800;color:var(--ink)}
.rtxt .rt-src{color:var(--muted);display:block;margin-top:2px}
@media(max-width:560px){.hero h1{font-size:28px}.card{padding:20px 18px}.wrap{padding:36px 16px 72px}}
"""

def card(cid):
    target = dups.get(cid, cid)
    p = papers[target]
    st = meta.get(target, ("연구",""))[0]
    href = f"pages/paper-{target:02d}.html"
    tag0 = esc(p["tags"][0]) if p["tags"] else ""
    dup = f'<span class="tag dup">중복 · {target}번과 동일</span>' if cid in dups else ""
    suffix = ' <span style="color:var(--hot-deep)">(중복)</span>' if cid in dups else ""
    return (f"<a class='card' href='{href}'>"
            f"<div class='card-top'><div class='no'>{cid}</div><div class='meta'>"
            f"<div class='title'>{esc(p['title'])}{suffix}</div>"
            f"<div class='cite'>{esc(p['authors'])} · {esc(p['journal'])} · {esc(p['cites'])}</div>"
            f"<div class='badges'><span class='tag design'>{esc(st)}</span>"
            f"<span class='tag'>{tag0}</span>{dup}</div>"
            f"</div></div>"
            f"<p class='finding'>{p['summary']}</p>"
            f"<span class='more'>전문가용 상세 →</span></a>")

cardsA = "".join(card(i) for i in partA)
cardsB = "".join(card(i) for i in partB)

def ref_bibliography():
    """Full References list on the V2 index (unique papers, with live DOI/PMID links)."""
    order = [i for i in (partA + partB) if i not in dups]
    items = []
    for pid in order:
        p = papers[pid]
        chips = ref_chips(p)
        chiprow = f"<div class='reflinks bib'>{chips}</div>" if chips else ""
        items.append(
            f"<li id='ref-{pid:02d}'><span class='rnum'>{pid:02d}</span>"
            f"<div class='rtxt'><span class='rt-title'>{esc(p['title'])}</span>"
            f"<span class='rt-src'>{esc(p['authors'])} · {esc(p['journal'])}</span>"
            f"{chiprow}</div></li>")
    return ("<section class='refsec'><div class='sec-head'>"
            "<span class='sec-num'>REF</span><h2>참고문헌 · References</h2></div>"
            "<p class='refsec-sub'>고유 논문 18편 · 각 항목의 DOI·PMID를 누르면 원문(또는 학술 검색)으로 이동합니다. "
            "14·15번은 1·3번과 동일 논문이라 생략했습니다.</p>"
            "<ol class='reflist'>" + "".join(items) + "</ol></section>")

ix = []
ix.append("<!DOCTYPE html><html lang='ko'><head><meta charset='UTF-8'>")
ix.append("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
ix.append("<title>골프 경기력 핵심 연구 20선 — 전문가용 근거 자료집 (V2)</title>")
ix.append(favicon_links("../"))
ix.append(f"<style>{INDEX_CSS}{BRAND_CSS}{NAV_CSS}</style></head><body><div class='wrap'>")
ix.append(nav("../", "v2"))
ix.append("<header class='hero'><span class='kicker'>EVIDENCE DOSSIER · 전문가용</span>"
          "<h1>골프 경기력 핵심 연구 20선<br><span>— 근거 자료집</span></h1>"
          "<p>V1(카드용 요약)과 동일한 20편을, <b>연구 설계·표본·핵심 통계·한계</b>까지 담아 전문가용으로 재정리했습니다. "
          "각 카드에 연구 설계 라벨을 달았고, 상세 페이지에는 '한계·유의' 항목을 포함합니다.</p>"
          "<a class='switch' href='../golf-research-summary.html'>V1 (카드용 요약) 보기 →</a></header>")
ix.append("<section class='sec'><div class='sec-head'><span class='sec-num'>PART 01</span>"
          "<h2>생체역학 · 스윙 메커니즘 10선</h2></div>"
          "<p class='sec-sub'>연구 설계 라벨 · 인용 영향력 기준 대략 순위</p>" + cardsA + "</section>")
ix.append("<section class='sec'><div class='sec-head'><span class='sec-num'>PART 02</span>"
          "<h2>경기력 · 데이터 · 종합 10선</h2></div>"
          "<p class='sec-sub'>연구 설계 라벨 · 인용 영향력 기준 대략 순위</p>" + cardsB + "</section>")
ix.append(ref_bibliography())
ix.append("<div class='footnote'><b>해석 유의 —</b> 리뷰/종설은 자체 표본이 없고, 단면·상관 연구는 인과를 함의하지 않으며, "
          "소표본·자가보고·특정 성별/숙련도 한정 연구는 일반화에 주의가 필요합니다. 각 상세 페이지의 '한계·유의'를 함께 참고하세요. "
          "인용 수는 데이터베이스·시점에 따라 달라집니다. 14·15번은 1·3번과 동일 논문(중복)입니다.</div>")
ix.append(brand_footer("../"))
ix.append("</div></body></html>")

with open(os.path.join(V2, "golf-research-v2.html"), "w", encoding="utf-8") as f:
    f.write("".join(ix))

print("v2 detail pages:", len(os.listdir(V2PAGES)))
print("v2 index written")
