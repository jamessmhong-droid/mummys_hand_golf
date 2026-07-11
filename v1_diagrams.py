# -*- coding: utf-8 -*-
"""V1 인스타 카드용 다크 패널 다이어그램.

규칙(CLAUDE.md): 다크 패널 표준 / 패널 내 색은 밝은 대비색 명시 / 타깃·볼 진행 오른쪽.
각 논문(pid)마다 하나씩. detail_html()이 커버 다음 슬라이드로 삽입한다.
viewBox는 400x240 기준(카드 폭 ~380px에서 선명).
"""

INK  = "#FCEDF3"; MUT = "#BE99A9"; FAINT = "#8A6675"
LONG = "#FF4DA0"; TEAL = "#1EBBA0"; PUTT = "#8A94F0"; APPR = "#E0A33A"; WARN = "#FF5A4E"
GRID = "#2E1E28"; AXIS = "#5A3F4C"; TRACK = "#241620"; BONE = "#6E5260"

_HEAD = ('<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" '
         'role="img" aria-label="{alt}" style="width:100%;height:auto;display:block">')

def _wrap(body, alt):
    return _HEAD.format(alt=alt) + body + "</svg>"

def _arrowdefs():
    return (f'<defs>'
            f'<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{WARN}"/></marker>'
            f'<marker id="ap" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{LONG}"/></marker>'
            f'<marker id="at" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{TEAL}"/></marker>'
            f'</defs>')

# ── 세로 막대: items=[(label, value, color), ...] · vmax 자동 ──────────────
def vbars(items, unit="", note="", alt=""):
    x0, y0, W, H = 54, 30, 320, 158   # 플롯 영역
    base = y0 + H
    vmax = max(v for _, v, _ in items) * 1.18 or 1
    n = len(items); slot = W / n; bw = min(52, slot * 0.5)
    b = [_arrowdefs()]
    # y 격자 3줄
    for gy in (0, .5, 1):
        yy = base - H * gy
        b.append(f'<line x1="{x0}" y1="{yy:.0f}" x2="{x0+W}" y2="{yy:.0f}" stroke="{GRID}" stroke-width="1"/>')
    for i, (lab, v, col) in enumerate(items):
        cx = x0 + slot * (i + .5)
        bh = H * (v / vmax)
        by = base - bh
        b.append(f'<rect x="{cx-bw/2:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="7" fill="{col}"/>')
        b.append(f'<text x="{cx:.1f}" y="{by-9:.1f}" text-anchor="middle" font-size="17" font-weight="900" fill="{INK}">{v}{unit}</text>')
        for li, line in enumerate(lab.split("\n")):
            b.append(f'<text x="{cx:.1f}" y="{base+20+li*14:.1f}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{MUT}">{line}</text>')
    if note:
        b.append(f'<text x="{x0}" y="18" font-size="12" font-weight="700" fill="{FAINT}">{note}</text>')
    return _wrap("".join(b), alt or note or "막대 그래프")

# ── 가로 막대: items=[(label, value, color)] · 0~vmax ────────────────────
def hbars(items, vmax=None, unit="", note="", alt=""):
    x0, y0, W = 130, 34, 232
    vmax = vmax or max(v for _, v, _ in items) * 1.15 or 1
    n = len(items); rh = 24; gap = (176 - n*rh) / (n+1) if n else 0
    b = []
    if note:
        b.append(f'<text x="20" y="20" font-size="12" font-weight="700" fill="{FAINT}">{note}</text>')
    y = y0
    for lab, v, col in items:
        y += gap
        bw = W * (v / vmax)
        b.append(f'<rect x="{x0}" y="{y:.1f}" width="{W}" height="{rh}" rx="6" fill="{TRACK}"/>')
        b.append(f'<rect x="{x0}" y="{y:.1f}" width="{bw:.1f}" height="{rh}" rx="6" fill="{col}"/>')
        b.append(f'<text x="{x0-10}" y="{y+rh/2+4.5:.1f}" text-anchor="end" font-size="12.5" font-weight="700" fill="{MUT}">{lab}</text>')
        b.append(f'<text x="{x0+bw+8:.1f}" y="{y+rh/2+4.5:.1f}" font-size="13.5" font-weight="900" fill="{INK}">{v}{unit}</text>')
        y += rh
    return _wrap("".join(b), alt or note or "가로 막대")

# ── 누적 상승 라인: pts=[(label, value)] ────────────────────────────────
def linegain(pts, unit="", note="", alt=""):
    x0, y0, W, H = 50, 30, 326, 158
    base = y0 + H
    vmax = max(v for _, v in pts) * 1.2 or 1
    n = len(pts)
    xs = [x0 + (W)*(i/(n-1)) for i in range(n)]
    ys = [base - H*(v/vmax) for _, v in pts]
    b = [_arrowdefs()]
    for gy in (0, .5, 1):
        yy = base - H*gy
        b.append(f'<line x1="{x0}" y1="{yy:.0f}" x2="{x0+W}" y2="{yy:.0f}" stroke="{GRID}" stroke-width="1"/>')
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in zip(xs, ys))
    b.append(f'<path d="{d}" fill="none" stroke="{LONG}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>')
    for (lab, v), x, y in zip(pts, xs, ys):
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{LONG}" stroke="{INK}" stroke-width="1.5"/>')
        b.append(f'<text x="{x:.1f}" y="{y-11:.1f}" text-anchor="middle" font-size="14" font-weight="900" fill="{INK}">{v}{unit}</text>')
        b.append(f'<text x="{x:.1f}" y="{base+20:.1f}" text-anchor="middle" font-size="12" font-weight="700" fill="{MUT}">{lab}</text>')
    if note:
        b.append(f'<text x="{x0}" y="18" font-size="12" font-weight="700" fill="{FAINT}">{note}</text>')
    return _wrap("".join(b), alt or note or "상승 라인")

# ── 운동 사슬(순차 속도) : 지면→골반→몸통→팔→클럽, 오른쪽으로 ──────────
def sequence(alt="운동 사슬"):
    stages = [("지면", TEAL), ("골반", TEAL), ("몸통", APPR), ("팔", LONG), ("클럽", WARN)]
    b = [_arrowdefs()]
    x = 40; y = 150; step = 78; r = 20
    b.append(f'<text x="200" y="26" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">아래에서 위로 · 속도가 <tspan fill="{INK}">합산</tspan>된다</text>')
    # 상승 곡선(피크가 순차적으로 커짐)
    peaks = [70, 96, 120, 150, 186]
    prev = None
    for i, (lab, col) in enumerate(stages):
        cx = x + step*i
        py = 210 - peaks[i]*0.62
        if prev:
            b.append(f'<line x1="{prev[0]+r}" y1="{prev[1]}" x2="{cx-r}" y2="{py:.0f}" stroke="{AXIS}" stroke-width="2.5" marker-end="url(#at)"/>')
        b.append(f'<circle cx="{cx}" cy="{py:.0f}" r="{r}" fill="{col}"/>')
        b.append(f'<text x="{cx}" y="{py+5:.0f}" text-anchor="middle" font-size="12" font-weight="900" fill="#0E0810">{i+1}</text>')
        b.append(f'<text x="{cx}" y="228" text-anchor="middle" font-size="12" font-weight="700" fill="{MUT}">{lab}</text>')
        prev = (cx, py)
    b.append(f'<text x="360" y="150" text-anchor="end" font-size="11.5" font-weight="700" fill="{FAINT}">타깃 ▶</text>')
    return _wrap("".join(b), alt)

# ── 이중 진자 : 허브 → 윗레버(팔) → 경첩(손목) → 아랫레버(클럽) ──────────
def pendulum(alt="이중 진자"):
    b = [_arrowdefs()]
    hx, hy = 150, 46          # 허브(어깨)
    wx, wy = 120, 150         # 손목(경첩)
    cx, cy = 250, 205         # 클럽헤드
    b.append(f'<text x="200" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">스윙 = <tspan fill="{INK}">두 개의 레버</tspan></text>')
    b.append(f'<circle cx="{hx}" cy="{hy}" r="8" fill="{INK}"/>')
    b.append(f'<text x="{hx+14}" y="{hy+4}" font-size="12" font-weight="700" fill="{MUT}">허브(어깨)</text>')
    b.append(f'<line x1="{hx}" y1="{hy}" x2="{wx}" y2="{wy}" stroke="{LONG}" stroke-width="7" stroke-linecap="round"/>')
    b.append(f'<text x="{hx-70}" y="105" font-size="12" font-weight="800" fill="{LONG}">윗 레버</text>')
    b.append(f'<text x="{hx-70}" y="120" font-size="10.5" font-weight="600" fill="{FAINT}">팔</text>')
    b.append(f'<circle cx="{wx}" cy="{wy}" r="7" fill="{APPR}"/>')
    b.append(f'<text x="{wx-14}" y="{wy+3}" text-anchor="end" font-size="12" font-weight="800" fill="{APPR}">경첩</text>')
    b.append(f'<text x="{wx-14}" y="{wy+17}" text-anchor="end" font-size="10" font-weight="600" fill="{FAINT}">손목</text>')
    b.append(f'<line x1="{wx}" y1="{wy}" x2="{cx}" y2="{cy}" stroke="{TEAL}" stroke-width="7" stroke-linecap="round"/>')
    b.append(f'<text x="205" y="168" font-size="12" font-weight="800" fill="{TEAL}">아랫 레버</text>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{WARN}"/>')
    b.append(f'<text x="{cx+14}" y="{cy+4}" font-size="11.5" font-weight="700" fill="{MUT}">클럽헤드</text>')
    b.append(f'<text x="360" y="60" text-anchor="end" font-size="11" font-weight="700" fill="{FAINT}">코킹을 늦게 풀수록 ↑</text>')
    return _wrap("".join(b), alt)

# ── X-factor : 위에서 본 상체·골반 회전 분리(분리각 표시) ────────────────
def xfactor(sep, alt="X팩터 분리"):
    b = [_arrowdefs()]
    cx, cy = 200, 132
    b.append(f'<text x="200" y="26" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">상체–골반 <tspan fill="{INK}">분리각</tspan> = X팩터</text>')
    # 골반(작게 덜 돌아감) / 상체(크게 돌아감)
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="86" ry="30" fill="none" stroke="{AXIS}" stroke-width="2" stroke-dasharray="4 5"/>')
    # 골반 화살표(약간 오른쪽)
    b.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+70}" y2="{cy-12}" stroke="{TEAL}" stroke-width="5" marker-end="url(#at)"/>')
    b.append(f'<text x="{cx+74}" y="{cy-14}" font-size="12" font-weight="800" fill="{TEAL}">골반(덜)</text>')
    # 상체 화살표(크게 뒤로)
    b.append(f'<line x1="{cx}" y1="{cy}" x2="{cx-74}" y2="{cy-40}" stroke="{LONG}" stroke-width="5" marker-end="url(#ap)"/>')
    b.append(f'<text x="{cx-78}" y="{cy-44}" text-anchor="end" font-size="12" font-weight="800" fill="{LONG}">상체(더)</text>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{INK}"/>')
    b.append(f'<text x="200" y="212" text-anchor="middle" font-size="26" font-weight="900" fill="{INK}">{sep}</text>')
    b.append(f'<text x="200" y="230" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUT}">분리가 클수록 볼 스피드 ↑</text>')
    return _wrap("".join(b), alt)

# ── 지면반력 체중 이동 : 뒷발→앞발, 타깃 오른쪽 ─────────────────────────
def grf(alt="지면반력 체중이동"):
    b = [_arrowdefs()]
    b.append(f'<text x="200" y="26" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">체중(지면반력) <tspan fill="{INK}">뒷발→앞발</tspan></text>')
    ground = 190
    b.append(f'<line x1="30" y1="{ground}" x2="370" y2="{ground}" stroke="{AXIS}" stroke-width="2.5"/>')
    # 뒷발(왼쪽), 앞발(오른쪽=타깃쪽)
    b.append(f'<rect x="96" y="{ground-16}" width="46" height="16" rx="4" fill="{BONE}"/>')
    b.append(f'<text x="119" y="{ground+18}" text-anchor="middle" font-size="12" font-weight="700" fill="{MUT}">뒷발</text>')
    b.append(f'<rect x="258" y="{ground-16}" width="46" height="16" rx="4" fill="{BONE}"/>')
    b.append(f'<text x="281" y="{ground+18}" text-anchor="middle" font-size="12" font-weight="700" fill="{MUT}">앞발</text>')
    # 반력 화살표(위로) — 앞발이 더 큼
    b.append(f'<line x1="119" y1="{ground}" x2="119" y2="{ground-48}" stroke="{TEAL}" stroke-width="6" marker-end="url(#at)"/>')
    b.append(f'<line x1="281" y1="{ground}" x2="281" y2="{ground-92}" stroke="{LONG}" stroke-width="8" marker-end="url(#ap)"/>')
    # 이동 화살표(뒷→앞)
    b.append(f'<line x1="150" y1="{ground-118}" x2="250" y2="{ground-118}" stroke="{WARN}" stroke-width="3.5" marker-end="url(#ah)"/>')
    b.append(f'<text x="356" y="{ground+18}" text-anchor="end" font-size="11" font-weight="700" fill="{FAINT}">타깃 ▶</text>')
    return _wrap("".join(b), alt)

# ── 도넛 비율 : frac(0~1) 강조 ──────────────────────────────────────────
def donut(frac, big, small, title="", alt="비율"):
    import math
    b = []
    cx, cy, r = 130, 128, 66; sw = 30
    C = 2*math.pi*r
    if title:
        b.append(f'<text x="200" y="26" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">{title}</text>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{TRACK}" stroke-width="{sw}"/>')
    dash = C*frac
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LONG}" stroke-width="{sw}" '
             f'stroke-dasharray="{dash:.1f} {C-dash:.1f}" stroke-dashoffset="{C*0.25:.1f}" stroke-linecap="round" transform="rotate(-90 {cx} {cy})"/>')
    b.append(f'<text x="{cx}" y="{cy-2}" text-anchor="middle" font-size="30" font-weight="900" fill="{INK}">{int(frac*100)}%</text>')
    b.append(f'<text x="{cx}" y="{cy+20}" text-anchor="middle" font-size="12" font-weight="700" fill="{LONG}">{big}</text>')
    # 범례
    lx = 236
    b.append(f'<rect x="{lx}" y="108" width="15" height="15" rx="4" fill="{LONG}"/>')
    b.append(f'<text x="{lx+22}" y="120" font-size="13" font-weight="800" fill="{INK}">{big}</text>')
    b.append(f'<rect x="{lx}" y="136" width="15" height="15" rx="4" fill="{TRACK}" stroke="{AXIS}"/>')
    b.append(f'<text x="{lx+22}" y="148" font-size="13" font-weight="700" fill="{MUT}">{small}</text>')
    return _wrap("".join(b), alt)

# ── 두 요인 → 결과 : A × B = C ──────────────────────────────────────────
def twofactor(a, b_, c, alt="두 요인"):
    b = []
    y = 130
    b.append(f'<rect x="24" y="{y-42}" width="112" height="84" rx="14" fill="{TRACK}" stroke="{LONG}" stroke-width="2"/>')
    b.append(f'<text x="80" y="{y-4}" text-anchor="middle" font-size="15" font-weight="900" fill="{LONG}">{a}</text>')
    b.append(f'<text x="152" y="{y+8}" text-anchor="middle" font-size="30" font-weight="900" fill="{INK}">×</text>')
    b.append(f'<rect x="168" y="{y-42}" width="112" height="84" rx="14" fill="{TRACK}" stroke="{TEAL}" stroke-width="2"/>')
    b.append(f'<text x="224" y="{y-4}" text-anchor="middle" font-size="15" font-weight="900" fill="{TEAL}">{b_}</text>')
    b.append(f'<text x="298" y="{y+8}" text-anchor="middle" font-size="26" font-weight="900" fill="{INK}">=</text>')
    b.append(f'<rect x="316" y="{y-42}" width="66" height="84" rx="14" fill="{WARN}"/>')
    _cl = c.split("\n")
    for li, line in enumerate(_cl):
        b.append(f'<text x="349" y="{y-6+li*15 - (len(_cl)-1)*7:.0f}" text-anchor="middle" font-size="12.5" font-weight="900" fill="#1B0F16">{line}</text>')
    b.append(f'<text x="200" y="40" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">둘 중 <tspan fill="{INK}">하나만으론 부족</tspan></text>')
    b.append(f'<text x="80" y="{y+62}" text-anchor="middle" font-size="11" font-weight="600" fill="{FAINT}">한 축</text>')
    b.append(f'<text x="224" y="{y+62}" text-anchor="middle" font-size="11" font-weight="600" fill="{FAINT}">다른 축</text>')
    return _wrap("".join(b), alt)

# ── 근활성(EMG) 몸통 : 대흉근·몸통 高 / 팔 低 ───────────────────────────
def musclebody(alt="근활성"):
    b = []
    b.append(f'<text x="200" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">스윙 주도 = <tspan fill="{INK}">가슴·몸통</tspan> (팔 아님)</text>')
    # 몸통
    b.append(f'<path d="M170 60 Q200 52 230 60 L242 168 Q200 182 158 168 Z" fill="{BONE}" opacity=".55"/>')
    # 머리
    b.append(f'<circle cx="200" cy="46" r="15" fill="{BONE}" opacity=".55"/>')
    # 대흉근(핫) 하이라이트
    b.append(f'<ellipse cx="184" cy="90" rx="22" ry="15" fill="{LONG}"/>')
    b.append(f'<ellipse cx="216" cy="90" rx="22" ry="15" fill="{LONG}"/>')
    b.append(f'<text x="200" y="94" text-anchor="middle" font-size="10.5" font-weight="900" fill="#1B0F16">대흉근</text>')
    # 코어
    b.append(f'<rect x="182" y="112" width="36" height="46" rx="8" fill="{APPR}"/>')
    b.append(f'<text x="200" y="140" text-anchor="middle" font-size="10.5" font-weight="900" fill="#1B0F16">몸통</text>')
    # 팔(낮음) - 회색 얇게
    b.append(f'<line x1="168" y1="66" x2="120" y2="150" stroke="{AXIS}" stroke-width="9" stroke-linecap="round"/>')
    b.append(f'<line x1="232" y1="66" x2="280" y2="150" stroke="{AXIS}" stroke-width="9" stroke-linecap="round"/>')
    b.append(f'<text x="108" y="168" text-anchor="middle" font-size="11" font-weight="700" fill="{FAINT}">팔 低</text>')
    b.append(f'<text x="292" y="168" text-anchor="middle" font-size="11" font-weight="700" fill="{FAINT}">팔 低</text>')
    # 범례
    b.append(f'<rect x="150" y="204" width="14" height="14" rx="4" fill="{LONG}"/><text x="170" y="215" font-size="11.5" font-weight="700" fill="{MUT}">활성 高</text>')
    b.append(f'<rect x="238" y="204" width="14" height="14" rx="4" fill="{AXIS}"/><text x="258" y="215" font-size="11.5" font-weight="700" fill="{MUT}">활성 低</text>')
    return _wrap("".join(b), alt)

# ── 퍼팅 : quiet eye 시선 + 페이스각 0°, 타깃(홀) 오른쪽 ─────────────────
def quieteye(alt="퍼팅 시선·페이스각"):
    b = [_arrowdefs()]
    b.append(f'<text x="200" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">시선 고정 + <tspan fill="{INK}">페이스 0°</tspan></text>')
    # 눈
    b.append(f'<circle cx="70" cy="70" r="16" fill="{TRACK}" stroke="{PUTT}" stroke-width="2.5"/>')
    b.append(f'<circle cx="70" cy="70" r="6" fill="{PUTT}"/>')
    b.append(f'<text x="70" y="104" text-anchor="middle" font-size="11" font-weight="700" fill="{MUT}">응시</text>')
    # 시선 → 볼
    b.append(f'<line x1="88" y1="78" x2="150" y2="150" stroke="{PUTT}" stroke-width="2.5" stroke-dasharray="5 5"/>')
    # 볼
    b.append(f'<circle cx="160" cy="162" r="13" fill="{INK}"/>')
    # 퍼터 페이스(볼 뒤, 0°=수직)
    b.append(f'<line x1="140" y1="140" x2="140" y2="186" stroke="{TEAL}" stroke-width="5" stroke-linecap="round"/>')
    b.append(f'<text x="130" y="130" text-anchor="end" font-size="11" font-weight="800" fill="{TEAL}">페이스 0°</text>')
    # 경로 → 홀(오른쪽)
    b.append(f'<line x1="176" y1="162" x2="330" y2="162" stroke="{WARN}" stroke-width="3" stroke-dasharray="2 6" marker-end="url(#ah)"/>')
    b.append(f'<circle cx="348" cy="162" r="12" fill="none" stroke="{APPR}" stroke-width="3"/>')
    b.append(f'<text x="348" y="192" text-anchor="middle" font-size="11.5" font-weight="700" fill="{APPR}">홀 ▶</text>')
    return _wrap("".join(b), alt)

# ── 변동성 : 여러 시행 궤적 + 평균, 일부 변동은 기능적 ───────────────────
def variability(alt="움직임 변동성"):
    b = []
    b.append(f'<text x="200" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">시행마다 <tspan fill="{INK}">조금씩 다른 궤적</tspan></text>')
    x0, base = 40, 200
    import math
    # 여러 흐린 궤적
    faint_paths = [
        "M40 150 C120 60,200 120,360 70",
        "M40 158 C120 78,200 108,360 82",
        "M40 146 C120 52,200 132,360 62",
        "M40 162 C120 88,200 100,360 92",
    ]
    for p in faint_paths:
        b.append(f'<path d="{p}" fill="none" stroke="{PUTT}" stroke-width="2" opacity=".38"/>')
    # 평균(굵게)
    b.append(f'<path d="M40 154 C120 70,200 115,360 76" fill="none" stroke="{LONG}" stroke-width="3.5" stroke-linecap="round"/>')
    b.append(f'<text x="360" y="70" text-anchor="end" font-size="11.5" font-weight="800" fill="{LONG}">평균</text>')
    b.append(f'<text x="200" y="224" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUT}">변동 = 결함이 아니라 <tspan fill="{INK}">적응</tspan>일 수 있다</text>')
    return _wrap("".join(b), alt)

# ── 노드 4개(시스템) : 생리학 종합 ──────────────────────────────────────
def systems(nodes, center, alt="시스템"):
    import math
    b = []
    cx, cy, r = 200, 128, 70
    cols = [TEAL, APPR, PUTT, LONG]
    b.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="{WARN}"/>')
    for i, w in enumerate(center.split()):
        b.append(f'<text x="{cx}" y="{cy-2+i*15:.0f}" text-anchor="middle" font-size="12.5" font-weight="900" fill="#1B0F16">{w}</text>')
    for i, lab in enumerate(nodes):
        ang = -math.pi/2 + i*(2*math.pi/len(nodes))
        nx = cx + math.cos(ang)*r*1.55
        ny = cy + math.sin(ang)*r*1.0
        col = cols[i % 4]
        b.append(f'<line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="{AXIS}" stroke-width="2"/>')
        b.append(f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="26" fill="{TRACK}" stroke="{col}" stroke-width="2.5"/>')
        b.append(f'<text x="{nx:.0f}" y="{ny+4:.0f}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{col}">{lab}</text>')
    return _wrap("".join(b), alt)

# ── 요통·부상예방=수행향상 : 요추 + 양방향 ──────────────────────────────
def backdual(alt="부상예방=수행향상"):
    b = [_arrowdefs()]
    b.append(f'<text x="200" y="26" text-anchor="middle" font-size="13" font-weight="800" fill="{MUT}">골프 최다 = <tspan fill="{WARN}">요통</tspan></text>')
    # 척추 + 요추 강조
    b.append(f'<path d="M120 60 C110 100,110 140,124 176" fill="none" stroke="{BONE}" stroke-width="12" stroke-linecap="round"/>')
    b.append(f'<circle cx="118" cy="150" r="17" fill="none" stroke="{WARN}" stroke-width="3.5"/>')
    b.append(f'<text x="118" y="200" text-anchor="middle" font-size="11.5" font-weight="800" fill="{WARN}">요추</text>')
    # 양방향: 부상예방 <-> 수행향상
    b.append(f'<rect x="196" y="78" width="176" height="40" rx="12" fill="{TRACK}" stroke="{TEAL}" stroke-width="2"/>')
    b.append(f'<text x="284" y="103" text-anchor="middle" font-size="14" font-weight="900" fill="{TEAL}">부상 예방</text>')
    b.append(f'<rect x="196" y="150" width="176" height="40" rx="12" fill="{TRACK}" stroke="{LONG}" stroke-width="2"/>')
    b.append(f'<text x="284" y="175" text-anchor="middle" font-size="14" font-weight="900" fill="{LONG}">수행 향상</text>')
    b.append(f'<line x1="284" y1="120" x2="284" y2="148" stroke="{INK}" stroke-width="2.5" marker-end="url(#ap)" marker-start="url(#at)"/>')
    b.append(f'<text x="284" y="212" text-anchor="middle" font-size="11" font-weight="700" fill="{MUT}">함께 간다</text>')
    return _wrap("".join(b), alt)

# ── 일관성(변동계수 낮을수록 좋음) : 프로 vs 아마 ───────────────────────
def consistency(alt="일관성"):
    return hbars([("프로", 7, LONG), ("아마추어", 22, AXIS)], vmax=26, unit="%",
                 note="핵심 변수 변동계수(CV%) · 낮을수록 일관", alt=alt)


# ── pid → (다이어그램 SVG, 캡션) ────────────────────────────────────────
def build():
    D = {}
    D[1]  = (grf(), "지면반력: 뒷발 → 앞발로 이동")
    D[2]  = (vbars([("클럽\n스피드", 5, TEAL), ("볼\n스피드", 5, APPR), ("캐리", 6, LONG), ("총\n비거리", 7, WARN)],
                   unit="%↑", note="8주 프로그램 후 향상(개략)", alt="8주 후 향상"),
             "8주 운동 → 스피드·비거리 모두 ↑")
    D[3]  = (vbars([("저속군", 44, TEAL), ("중속군", 50, APPR), ("고속군", 59, LONG)],
                   unit="°", note="볼 스피드 그룹별 분리각(X팩터)", alt="분리각"),
             "빠를수록 상체–골반 분리각이 크다")
    D[4]  = (vbars([("저숙련", 0.5, AXIS), ("고숙련", 13.4, LONG)],
                   unit="°", note="다운스윙 초반 X팩터 '스트레치'", alt="X팩터 스트레치"),
             "핵심은 크기보다 '다운스윙 스트레치'")
    D[5]  = (sequence(), "어깨 90°+ 감고, 엉덩이부터 순차로 푼다")
    D[6]  = (linegain([("시작", 0), ("2주", 12.8), ("7주", 24.0)],
                      unit="%", note="워밍업 누적 → 클럽 스피드 향상", alt="워밍업 누적 효과"),
             "꾸준할수록 클럽 스피드 누적 상승")
    D[7]  = (twofactor("힘", "가동범위", "클럽\n스피드", alt="힘×가동범위"),
             "힘과 가동범위가 함께 스피드를 만든다")
    D[8]  = (donut(0.735, "설명됨", "나머지", title='4요인이 <tspan fill="'+INK+'">볼 스피드</tspan> 설명', alt="볼 스피드 설명력"),
             "볼 스피드의 최대 73%를 4요인이 설명")
    D[9]  = (variability(), "변동성은 무조건 결함이 아니다")
    D[10] = (quieteye(), "퍼팅 = 시선 고정 + 페이스 0°")
    D[11] = (donut(0.67, "롱게임", "숏·퍼팅", title='성적 차이의 <tspan fill="'+INK+'">대부분</tspan>', alt="스트로크 게인드"),
             "성적 차이의 약 2/3는 롱게임")
    D[12] = (pendulum(), "이중 진자 = 두 개의 레버 + 경첩")
    D[13] = (musclebody(), "스윙은 대흉근·몸통이 주도한다")
    D[16] = (consistency(), "프로의 차이는 힘보다 '일관성'")
    D[17] = (hbars([("GIR(온그린)", 88, TEAL), ("스크램블링", 80, APPR), ("퍼트/GIR", 76, PUTT)],
                   vmax=100, note="스코어와 가장 강하게 연관된 3대 지표", alt="엘리트 지표"),
             "GIR·스크램블·퍼트가 성적을 가른다")
    D[18] = (vbars([("핸디 ≤0", 281, LONG), ("1–9", 263, APPR), ("10–20", 252, TEAL)],
                   unit="yd", note="핸디캡 그룹별 드라이빙 거리", alt="핸디캡별 거리"),
             "코어 근력·유연성 ↑ → 핸디 ↓, 거리 ↑")
    D[19] = (systems(["심폐", "대사", "근골격", "영양"], "지속 모니터링", alt="생리학 종합"),
             "체력·컨디셔닝을 개별화해 모니터링")
    D[20] = (backdual(), "부상 예방과 수행 향상은 함께 간다")
    return D

DIAGRAMS = build()
