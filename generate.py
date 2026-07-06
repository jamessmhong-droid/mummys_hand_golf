# -*- coding: utf-8 -*-
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(OUT, "pages")
os.makedirs(PAGES, exist_ok=True)

# 방문자 카운트(GoatCounter) — 비공개 대시보드: https://mummyshandgolf.goatcounter.com
GC = ('<script data-goatcounter="https://mummyshandgolf.goatcounter.com/count" '
      'async src="//gc.zgo.at/count.js"></script>')

# ---------------------------------------------------------------
# DATA. dup=id -> this card links to that paper's page instead.
# ---------------------------------------------------------------
papers = {
 1:{"part":"PART 01 · 생체역학","title":"비거리·정확성을 극대화하는 생체역학의 역할",
    "authors":"Hume, P., Keogh, J. & Reid, D. (2005)","journal":"Sports Medicine, 35(5), 429–449","cites":"약 400+ 인용",
    "tags":["최다인용 리뷰","스윙·퍼팅 종합","SSC"],
    "summary":"골프 샷의 비거리와 정확성을 결정하는 생체역학 요인을 스윙·퍼팅 전반에 걸쳐 종합한, 이 분야에서 가장 많이 인용되는 대표 <b>종설(review)</b>이다. 자체 실험이 아니라 기존 연구들을 통합했다.",
    "findings":[
      "비거리 극대화에는 큰 <b>지면반력(GRF)</b>이 필요하며, 백스윙엔 뒷발, 다운스윙·가속 구간엔 <b>앞발로 반력이 이동</b>한다.",
      "백스윙에서 고관절·몸통·상지를 빠르게 신전시키고, 다운스윙 초반 <b>X-factor를 극대화</b>하는 것이 '힘의 합산(summation of force)' 원리를 쓰는 방법이다.",
      "구체 지침 — 리드암이 <b>수평보다 약 30° 아래일 때 손목 코킹을 푸는(uncocking)</b> 것이 클럽헤드 스피드에 유리하다.",
      "정확성(칩·퍼팅)은 그립을 낮게, 백스윙을 <b>느리고 짧게</b>, 어깨·손목 움직임을 <b>일관되게</b> 유지할 때 높아진다.",
      "<b>신장-단축 주기(SSC)</b>와 근력·유연성 등 체력 요소가 스윙 역학과 상호작용하며 수행에 영향을 준다."],
    "method":"골프 스윙·퍼팅 생체역학 문헌을 종합한 <b>내러티브 리뷰</b>(자체 표본 없음). 언급된 평가기법: 2D·3D 비디오그래피, 지면반력판(force plate), 근전도(EMG). Sports Medicine 35(5):429–449, PMID 15896091.",
    "significance":"이후 등장한 대부분의 골프 생체역학 연구가 참조하는 개념적 지도. 비거리와 정확성을 하나의 프레임에서 통합해 다뤘다는 점이 핵심이다.",
    "takeaway":"비거리는 지면반력·순차적 힘 전달에서, 정확성은 동작의 일관성에서 나온다."},

 2:{"part":"PART 01 · 생체역학","title":"8주 골프 특화 운동 프로그램의 효과",
    "authors":"Lephart, S.M., Smoliga, J.M., Myers, J.B., Sell, T.C. & Tsai, Y.-S. (2007)","journal":"J. Strength & Conditioning Research, 21(3), 860–869 · Univ. of Pittsburgh","cites":"약 250+ 인용",
    "tags":["중재연구","탄력밴드","홈트레이닝"],
    "summary":"레크리에이션 남성 골퍼 15명(평균 47세, USGA 핸디캡 12.1)을 대상으로, 비시즌 8주 동안 집에서 <b>탄력밴드+폼패드</b>로 수행한 골프 특화 운동이 신체 특성·스윙 역학·비거리를 실제로 바꾸는지 검증한 중재 연구.",
    "findings":[
      "<b>가동범위(ROM) 전 항목 향상</b> — 어깨 신전 +약 20~23%, 고관절 신전 +약 36~38%, 고관절 굴곡 +약 7%.",
      "<b>몸통 회전 근력·고관절 외전 근력</b>이 유의하게 증가(좌우), 균형(자세 흔들림)도 개선.",
      "스윙 역학 변화 — 탑에서 <b>골반이 더 열리고</b>, 다운스윙 가속 구간의 <b>상체 회전 속도·X-factor 속도</b>가 빨라짐.",
      "결과적으로 <b>클럽헤드 스피드·볼 스피드·캐리·총 비거리 모두 유의하게 증가</b>(발사각·백스핀은 변화 없음).",
      "즉 '체력 향상 → 스윙 역학 개선 → 비거리 증가'로 이어지는 <b>인과 사슬</b>을 실증."],
    "method":"동일 집단 전후 비교(pre-post) 설계. 8주 프로그램 전후로 3D 동작분석(Peak Motus, 8카메라), 런치 모니터(Vector/Accusport), Biodex 등속성 근력, ROM·균형을 측정. 비시즌 진행, 참가자는 별도 레슨·연습 금지, 운동 로그로 순응도 확인.",
    "significance":"'골프에 맞춘 트레이닝이 성적을 올린다'를 <b>스윙 역학 분석까지 포함</b>해 실험적으로 뒷받침한 초기 근거. 특별한 장비·헬스장 없이 집에서 하는 밴드 운동만으로도 비거리가 늘 수 있음을 보여, 골프 피트니스 분야에서 널리 인용됨.",
    "takeaway":"집에서 밴드로 3~4회/주, 8주 — 몸·스윙·비거리가 함께 좋아진다.",
    "extra":"""
<section><h2>실제 운동 프로그램</h2>
<div class="box" style="margin-bottom:16px">
<b>구성 원리</b> — 하체는 <b>안정성</b>(균형·고관절 근력·고관절 유연성), 상체는 <b>가동성</b>(몸통 회전·어깨 유연성)을 키우고 <b>몸통 회전 근력</b>을 강화하도록 설계.<br><br>
<b>도구</b> — 1.8m 탄력 저항 밴드(핸들+고정앵커) + 20×25cm 폼 밸런스 패드.<br>
<b>빈도</b> — 주 3~4일, 8주. 첫 측정 후 각 운동의 인쇄물·영상 설명을 받아 <b>집에서 자가 수행</b>.<br>
<b>부하 방식</b> — 스트레칭은 각 30초 유지 / 근력은 밴드로 <b>2초 수축·2초 이완 = 1회</b>, <b>3세트 × 10~15회</b> 좌우. 3세트×15회가 편해지면 앵커에서 더 멀어져 저항 ↑ / 균형은 다리당 30초 <b>2세트</b>.
</div>
<div class="prog">
  <div class="progcol"><h3>스트레칭 (각 30초)</h3><ul>
    <li>누워서 무릎 당기기(고관절 굴곡)</li>
    <li>엎드려 몸통 신전 — 엉덩이 들어 '역V' 자세</li>
    <li>무릎 꿇고 런지(앞다리 90°)</li>
    <li>앉아서 고관절 회전 — 다리 교차해 당기기</li>
    <li>앉아서 몸통 회전</li>
    <li>클럽 들고 앉아서 몸통 회전(목 뒤에 클럽)</li>
    <li>서서 좌우 측면 굽히기(발 넓게)</li>
  </ul></div>
  <div class="progcol"><h3>근력 (3세트 × 10~15회, 2초/2초)</h3><ul>
    <li>고관절 외전 <span class="b">밴드</span></li>
    <li>고관절 내전 <span class="b">밴드</span></li>
    <li>견갑골 후인(scapular retraction) <span class="b">밴드</span></li>
    <li>저항 백스윙 <span class="b">밴드</span></li>
    <li>저항 다운스윙 <span class="b">밴드</span></li>
    <li>저항 스루스윙(팔로스루) <span class="b">밴드</span></li>
    <li>복부 크런치</li>
  </ul></div>
  <div class="progcol"><h3>균형 (다리당 30초 · 2세트)</h3><ul>
    <li>정적 프론트 스쿼트(무릎 45°)</li>
    <li>바닥에서 한 발 서기</li>
    <li>폼 패드 위에서 한 발 서기</li>
  </ul></div>
</div>
<p class="note">* 근력 운동 중 <b>밴드</b> 표시는 탄력 저항 밴드를 사용하는 종목. 스윙 3국면(백/다운/스루)을 밴드 저항으로 그대로 재현하는 것이 이 프로그램의 '골프 특화' 핵심입니다. (출처: Table 4, Lephart et al. 2007)</p>
</section>"""},

 3:{"part":"PART 01 · 생체역학","title":"드라이빙에서 상체·골반 회전의 역할",
    "authors":"Myers, J., Lephart, S., Tsai, Y.-S., Sell, T., Smoliga, J. & Jolly, J. (2008)","journal":"Journal of Sports Sciences, 26(2), 181–188 · PMID 17852693","cites":"약 200+ 인용",
    "tags":["X-factor","N=100","분리각"],
    "summary":"레크리에이션 골퍼 <b>100명</b>(평균 핸디캡 8.1, 45세)을 볼 스피드로 3군으로 나눠, 상체-골반 회전 분리(X-factor)가 볼 스피드에 어떻게 기여하는지 실측한 핵심 실증 연구.",
    "findings":[
      "볼 스피드가 빠른 군일수록 <b>몸통-골반 분리각이 뚜렷하게 컸다</b> — 저속 −44°, 중속 −50°, 고속 −59°(P&lt;0.0001).",
      "최대 <b>상체 회전 속도</b>도 저속 591 → 중속 675 → 고속 767 °/s로 증가(P&lt;0.0001).",
      "볼 스피드와의 상관은 <b>상체 회전 속도 r=0.59~0.61</b>, 분리각 r≈−0.55로 회전 '속도'가 특히 중요.",
      "<b>골반 회전 위치·속도는 볼 스피드와 유의한 상관 없음</b> — 회전량 자체보다 두 분절의 '분리'가 관건.",
      "정점 분리각과 최대 분리각이 비슷하게 상관 → '최대 분리가 정점보다 더 중요'하다는 주장은 지지되지 않음."],
    "method":"3D 동작분석(Peak Motus, 카메라 8대, 200fps) + 런치 모니터(FlightScope). 본인 드라이버로 10스윙, 볼 스피드 상위 5스윙 분석. 일원 ANOVA + Pearson 상관(r≥0.50만 논의).",
    "significance":"'X-factor가 크면 멀리 친다'에 대규모 표본의 정량 근거를 제공. 이후 파워 연구의 기준점이 됐다.",
    "takeaway":"상체를 더 크게·빠르게 돌리고 골반은 덜 돌려 '분리'를 키우면 볼 스피드가 오른다.",
    "extra":"""
<section><h2>볼 스피드 그룹별 회전 데이터</h2>
<table class="dtab"><thead><tr><th>변수</th><th>저속군<br>(n=21)</th><th>중속군<br>(n=65)</th><th>고속군<br>(n=14)</th></tr></thead>
<tbody>
<tr><td>볼 스피드 (m/s)</td><td>55.7</td><td>65.6</td><td>75.4</td></tr>
<tr><td>정점 분리각 (°)</td><td>−44.2</td><td>−49.5</td><td>−59.1</td></tr>
<tr><td>최대 분리각 (°)</td><td>−45.6</td><td>−51.7</td><td>−61.8</td></tr>
<tr><td>최대 상체 회전속도 (°/s)</td><td>591</td><td>675</td><td>767</td></tr>
<tr><td>평균 핸디캡</td><td>15.1</td><td>7.8</td><td>1.8</td></tr>
</tbody></table>
<p class="note">고속군일수록 분리각과 회전 속도가 계단식으로 커진다(모두 P&lt;0.0001). (출처: Myers et al. 2008, Table)</p>
</section>"""},

 4:{"part":"PART 01 · 생체역학","title":"다운스윙에서 X-Factor Stretch의 중요성",
    "authors":"Cheetham, P.J., Martin, P.E., Mottram, R.E. & St. Laurent, B.F. (2001)","journal":"Optimising Performance in Golf (pp.192–199) · Science & Golf 학회 발표(2000)","cites":"약 200+ 인용",
    "tags":["X-factor Stretch","N=19","타이밍"],
    "summary":"고숙련 10명(프로 등)과 저숙련 9명(핸디캡 15+) 총 <b>19명</b>을 비교해, 백스윙 정점이 아니라 다운스윙 '초기'에 X-factor가 순간적으로 더 커지는 현상(<b>X-factor Stretch</b>)을 규명한 연구.",
    "findings":[
      "<b>백스윙 정점의 X-factor 크기는 두 군 간 유의차가 없었다</b>(t=1.02, p=0.33) — 크기만으로 숙련도가 갈리지 않는다.",
      "다운스윙 초반 X-factor 증가율(Stretch)은 <b>고숙련 19% vs 저숙련 13%</b>로 유의하게 달랐다(F=6.90, p=0.02).",
      "사례 — 저숙련은 정점 38.0°→최대 38.5°(스트레치 0.5°)에 그친 반면, 고숙련은 60.1°→73.5°(<b>스트레치 13.4°</b>).",
      "일부 고숙련자는 다운스윙 초반에 X-factor가 <b>최대 15°까지 추가로 증가</b>했다.",
      "백스윙의 목적은 자세 세팅이 아니라, 근육을 <b>동적으로 신장시켜 다운스윙 파워를 준비</b>하는 것이다."],
    "method":"SkillTec 3D-Golf(Polhemus 전자기 추적, 30Hz). 센서를 골반·등(T3)·이마·왼손등에 부착, 전원 5번 아이언 사용. X-factor = 골반과 T3의 회전 위치 차이. 2요인 ANOVA(숙련도×스윙 위치).",
    "significance":"X-factor를 '정적인 각도'가 아니라 '<b>동적 신장 반사</b>'로 재해석하게 만든 연구. 타이밍의 중요성을 부각했다.",
    "takeaway":"X-factor는 얼마나 크냐보다 '다운스윙 초반에 얼마나 더 늘어나느냐(스트레치)'가 관건이다."},

 5:{"part":"PART 01 · 생체역학","title":"핸디캡 10 이하 골퍼의 엉덩이·어깨 회전",
    "authors":"Burden, A.M., Grimshaw, P.N. & Wallace, E.S. (1998)","journal":"Journal of Sports Sciences, 16(2), 165–176 · PMID 9531005","cites":"약 180+ 인용",
    "tags":["회전 운동학","N=8","시퀀스"],
    "summary":"핸디캡 10 이하 숙련 골퍼 <b>8명</b>의 드라이버 스윙을 3D로 분석해, 엉덩이·어깨 회전 패턴과 무게중심 이동이 어떻게 클럽헤드 속도를 만드는지 규명한 기초 운동학 연구.",
    "findings":[
      "숙련 골퍼는 백스윙에서 <b>어깨를 90° 넘게 회전</b>시켜 뚜렷한 분리를 형성한다.",
      "골퍼의 <b>75%</b>에서, 엉덩이가 타깃 쪽으로 되돌아 회전을 시작할 때 <b>어깨는 여전히 반대 방향으로 회전 중</b>이었다.",
      "이 <b>엉덩이 먼저 → 어깨 뒤따름</b>의 순차 패턴이 '속도 합산(summation of speed)' 원리에 부합한다.",
      "임팩트 시 무게중심이 <b>목표 볼 방향으로만</b> 이동하는 것도 드라이브 속도에 기여한다."],
    "method":"티에서의 드라이버 스윙을 비디오 촬영 후 3D 기법으로 분석. 무게중심 이동과 힙·어깨 회전을 국면별로 측정.",
    "significance":"저핸디캡 골퍼의 '정상적' 회전 시퀀스에 대한 초기 기준 데이터. 이후 숙련도 비교 연구의 baseline이 됐다.",
    "takeaway":"좋은 스윙은 '어깨로 90°+ 감고, 엉덩이부터 푸는' 순차 시퀀스를 지킨다."},

 6:{"part":"PART 01 · 생체역학","title":"골프 워밍업과 부상·수행",
    "authors":"Fradkin, A.J., Sherman, C.A. & Finch, C.F. (2004)","journal":"Br. J. Sports Medicine, 38(6), 762–765 (RCT) · PMID 15562177","cites":"약 150+ 인용",
    "tags":["워밍업","RCT","클럽스피드"],
    "summary":"남성 골퍼 <b>20명</b>을 나이·핸디캡으로 매칭해 운동군 10·대조군 10으로 나눈 <b>무작위 대조시험(RCT)</b>. 골프 특화 워밍업을 주 5회·5주간 했을 때 클럽헤드 스피드가 얼마나 오르는지 검증했다.",
    "findings":[
      "워밍업 프로그램 <b>2주차에 클럽헤드 스피드 약 12.8%</b>(3~6 m/s) 향상.",
      "<b>7주차에는 약 24.0%</b>(7~10 m/s)까지 누적 향상 — 꾸준히 할수록 효과가 커진다.",
      "대조군은 거의 변화 없음(0.3~0.8 m/s). 두 군 차이 유의(p=0.029), 시간×군 상호작용 p&lt;0.001.",
      "동일 저자의 <b>동반 연구</b>: 클럽헤드 스피드와 핸디캡의 상관이 <b>r=0.95</b>로 매우 강함 — 스피드는 실력의 타당한 지표.",
      "즉 워밍업은 즉각 효과뿐 아니라 <b>반복 시 누적 효과</b>가 크다."],
    "method":"실험실에서 2D 비디오로 클럽헤드 스피드 측정. 1주차 전원 10스윙 → 운동군만 골프 특화 워밍업 주 5회×5주 → 2·7주차 재측정. 무작위 배정·매칭 설계.",
    "significance":"'워밍업이 수행을 올린다'를 실험(RCT)으로 입증. 부상 예방과 수행 향상을 함께 얻는 실용적 근거.",
    "takeaway":"티오프 전 골프 특화 워밍업을 꾸준히 하면 클럽 스피드가 최대 24%까지 오른다."},

 7:{"part":"PART 01 · 생체역학","title":"골프 스윙의 에너지·파워 분석 (모델링)",
    "authors":"Nesbit, S.M. & Serrano, M. (2005)","journal":"J. Sports Science & Medicine, 4(4), 520–533 · 원제 'Work and Power Analysis of the Golf Swing'","cites":"약 150+ 인용",
    "tags":["모델링","에너지","N=4"],
    "summary":"스킬·체형·스윙 스타일이 다른 아마추어 <b>4명</b>을, 클럽과 전신을 각각 컴퓨터 모델로 만들어 다운스윙의 <b>에너지·파워</b> 관점에서 분석한 모델링 연구.",
    "findings":[
      "에너지 접근법으로 클럽을 가속시키는 <b>힘·토크 성분</b>과 각 신체 분절의 <b>에너지(work) 생성 타이밍</b>을 새롭게 밝혔다.",
      "<b>힘(force)과 가동범위(ROM)가 클럽헤드 속도 생성에 '동등하게' 중요</b>함을 증명 — 어느 하나만으론 부족.",
      "샤프트의 <b>에너지 저장·방출(strain energy)</b>과 스윙 효율(swing efficiency)을 정량화했다.",
      "에너지 기반 분석이 기존 힘/토크 분석보다 다운스윙을 더 포괄적으로 설명한다."],
    "method":"두 컴퓨터 모델 사용 — (1) 클럽 상세 모델로 내부 에너지 전달, (2) 전신 모델로 관절 내부 일(work) 산출. 운동에너지·변형에너지·파워를 표준 역학으로 계산.",
    "significance":"실험으로 못 보는 내부 일·에너지 전달을 계산으로 열어, 장비·기술 최적화 연구의 토대가 됐다.",
    "takeaway":"클럽 스피드는 '힘'과 '가동범위'가 함께 만든다 — 둘 중 하나만으론 부족하다."},

 8:{"part":"PART 01 · 생체역학","title":"생체역학 변수와 드라이빙 수행의 관계",
    "authors":"Chu, Y., Sell, T.C. & Lephart, S.M. (2010)","journal":"Journal of Sports Sciences, 28(11), 1251–1259 · PMID 20845215","cites":"약 120+ 인용",
    "tags":["N=308","회귀분석","X-factor"],
    "summary":"골퍼 <b>308명</b>(남 266·여 42, 평균 핸디캡 8.4)을 대상으로, 어떤 생체역학 변수가 실제 볼 스피드를 결정하는지 단계적 회귀분석으로 규명한 대규모 연구.",
    "findings":[
      "스윙 4개 시점의 회귀모델이 <b>볼 스피드 분산의 43.7~73.5%</b>를 설명 — 임팩트 40ms 전 구간이 73.5%로 가장 높음.",
      "볼 스피드는 핸디캡과 <b>r=−0.71</b>, 클럽헤드 속도와 <b>r=0.94</b>로 강하게 연관.",
      "핵심 예측변수: 가속 시점 <b>상체 회전 속도</b>(β=0.43), <b>X-factor</b>(β=−0.25), 임팩트 시 몸통 전방·측면 기울기, 체중 이동.",
      "상체·골반 각각의 회전보다 <b>둘 사이의 분리(X-factor)</b>가 유의 — 회전량보다 '분리'에 집중해야.",
      "그동안 간과된 <b>전완 근육</b>도 클럽 릴리스 지연·가속에 중요."],
    "method":"8대 고속카메라(240Hz)로 운동학, Kistler 포스플레이트(1200Hz)로 지면반력, FlightScope로 볼 스피드 측정. 10샷 중 상위 5샷 평균에 대해 단계적 다중선형회귀.",
    "significance":"'지면부터 위로'의 운동 연쇄와 X-factor의 중요성을 대규모 표본으로 뒷받침. 코칭·트레이닝에 직접적 함의를 준다.",
    "takeaway":"볼 스피드의 최대 73%는 상체 회전속도·X-factor·몸통 기울기·체중이동으로 설명된다."},

 9:{"part":"PART 01 · 생체역학","title":"골프 스윙의 움직임 변동성 (이론·방법론)",
    "authors":"Glazier, P. (2011)","journal":"Research Quarterly for Exercise and Sport, 82(2), 157–161 · 단독저자 관점논문","cites":"약 100+ 인용",
    "tags":["변동성","동역학계","개념논문"],
    "summary":"스윙의 동작 변동성(반복 간 흔들림)을 <b>동역학계 이론(dynamical systems)</b> 관점에서 다룬 이론·방법론 논문. 실험 표본이 없는 <b>관점(viewpoint) 논문</b>이라는 점에 유의.",
    "findings":[
      "숙련 수행은 '시행 간 변동이 거의 없다'는 통념에 <b>도전</b>한다.",
      "움직임 변동성은 노이즈·결함이 아니라 숙련 운동의 <b>내재적·기능적 요소</b>일 수 있다.",
      "일부 변동성은 <b>부하 분산·환경 적응</b> 등 기능적 역할을 하므로 무조건 줄일 대상이 아니다.",
      "골프 스윙 변동성 연구는 <b>이론·방법론·실무</b> 정비가 필요한 향후 과제로 제시된다."],
    "method":"실증 실험이 아닌 개념적 논의. 동역학계 이론 관점에서 변동성의 의미와 측정 방법을 정리(정량 결과치 없음).",
    "significance":"'일관성=좋음, 변동성=나쁨'이라는 단순 도식을 재검토하게 한 연구. 연습·측정 설계에 관점을 제공.",
    "takeaway":"스윙의 흔들림(변동성)은 무조건 결함이 아니라, 기능적일 수도 있다.",
    "extra":"""
<section><h2>참고 — 실증 연구는 별도</h2>
<div class="box">이 논문은 <b>개념·이론 논문</b>이라 구체 수치가 없습니다. '변동성이 <b>수평 발사각</b>·방향 정확성에 부정적'이라는 실증적 주장은 퍼팅·스윙 변동성을 측정한 <b>별도의 실험 연구들</b>(예: 퍼팅 스트로크 변동성 연구)에서 나온 것으로, 저자·출처가 다릅니다. 카드에는 두 갈래를 구분해 표기했습니다.</div>
</section>"""},

 10:{"part":"PART 01 · 생체역학","title":"퍼팅 생체역학 — 골반·몸통의 기여",
    "authors":"Delphinus, E.M. & Sayers, M.G.L. (2012)","journal":"Sports Biomechanics, 11(2), 212–222 · DOI 10.1080/14763141.2011.638723","cites":"퍼팅 생체역학 대표 실증",
    "tags":["퍼팅","N=10","3D 골반·몸통"],
    "summary":"'퍼팅은 스코어의 핵심인데 생체역학 연구가 거의 없다'는 문제의식에서 출발. 싱글 핸디캡 골퍼 <b>10명</b>의 퍼팅 중 <b>골반·몸통의 3D 움직임과 협응</b>을 정밀 측정해, 잘 넣는 그룹과 못 넣는 그룹의 차이를 규명한 실증 연구.",
    "findings":[
      "성공률 기준으로 <b>숙련군(&gt;79%)</b>과 <b>비숙련군(&lt;79%)</b>으로 나눠 골반·몸통 운동학을 비교.",
      "숙련 퍼터일수록 골반·몸통 움직임이 <b>더 안정적이고 재현성 높은 패턴</b>을 보인다.",
      "퍼팅 <b>정확도의 핵심은 임팩트 시 페이스 각·스트로크 경로</b> — 별도 연구들에서 엘리트는 임팩트 페이스 각이 <b>0°에 더 가깝다</b>.",
      "숙련자는 <b>quiet eye</b>를 백스윙 전 ~1초·스트로크 중 ~1초·임팩트 후 ~0.5초 안정적으로 유지(비숙련자는 스트로크 시작과 함께 시선이 흔들림).",
      "즉 퍼팅은 손목만의 문제가 아니라 <b>몸통·골반의 안정성과 시선 제어</b>가 함께 만드는 결과다."],
    "method":"6대 카메라 모션캡처(100Hz)로 3D 운동학 측정. 실내에서 2m 퍼트 18회 수행, 성공률로 두 그룹으로 분류. 골반·몸통 분절의 위치·협응을 정량 분석.",
    "significance":"스코어 비중이 큰 퍼팅의 <b>골반·몸통 기여</b>를 정면으로 다룬 드문 실증 연구. 이후 퍼팅 생체역학 연구의 참조점이 됐다.",
    "takeaway":"좋은 퍼팅은 손목이 아니라 몸통·골반의 안정성과 시선(quiet eye)에서 나온다.",
    "extra":"""
<section><h2>퍼팅 생체역학, 이런 연구들이 있다</h2>
<div class="prog">
  <div class="progcol"><h3>골반·몸통 협응</h3><ul><li>Delphinus & Sayers (2012)</li><li>싱글 핸디캡 10명, 2m 퍼트 18회</li><li>숙련 vs 비숙련 골반·몸통 3D 비교</li></ul></div>
  <div class="progcol"><h3>임팩트 운동학</h3><ul><li>엘리트 vs 아마추어 체계적 리뷰·메타분석(25편)</li><li>핵심: <b>페이스 각·퍼터 경로·백스윙</b></li><li>엘리트는 임팩트 페이스 각이 <b>0°에 근접</b></li></ul></div>
  <div class="progcol"><h3>Quiet Eye(시선)</h3><ul><li>숙련자는 응시를 길고 안정적으로 유지</li><li>Quiet eye 훈련이 압박 상황 성공률↑</li><li>지각-운동 통제가 퍼팅의 한 축</li></ul></div>
</div>
<p class="note">퍼팅 생체역학은 스윙에 비해 연구가 적지만 분명히 존재하며, ① 몸통·골반 안정성 ② 임팩트 시 페이스 각/경로 ③ quiet eye 시선 제어의 세 축으로 요약된다. (출처: Delphinus & Sayers 2012; 퍼팅 운동학 체계적 리뷰 2022; quiet eye 연구들)</p>
</section>"""},

 11:{"part":"PART 02 · 경기력·데이터","title":"PGA 투어 선수 경기력 평가 (Strokes Gained)",
    "authors":"Broadie, M. (2012)","journal":"Interfaces, 42(2), 146–165 · Columbia Univ. · DOI 10.1287/inte.1120.0626","cites":"고인용 · 골프 분석학 전환점",
    "tags":["Strokes Gained","ShotLink","800만 샷"],
    "summary":"PGA 투어 <b>ShotLink 데이터(2003~2010, 800만 샷+)</b>에 'Strokes Gained' 지표를 적용해, 선수 경기력을 롱게임·숏게임·퍼팅으로 분해한 골프 분석학의 대표 논문.",
    "findings":[
      "<b>Strokes Gained(획득 타수)</b>: 각 샷을 '그 상황의 기대 타수' 대비로 평가하는 지표를 정립(동적계획법 기반).",
      "<b>롱게임(100야드 밖 샷)이 투어 선수 간 스코어 변동의 약 2/3를 설명</b> — '숏게임·퍼팅이 전부'라는 통념 반박.",
      "타이거 우즈는 total strokes gained 1위이며, 그 우위의 <b>약 2/3도 롱게임</b>에서 기인.",
      "전통 통계(퍼팅 수, 페어웨이 안착률 등)의 한계를 데이터로 드러냈다.",
      "이 지표는 2011년 5월 PGA 투어가 퍼팅 측정에 <b>공식 도입</b>."],
    "method":"PGA 투어 ShotLink의 샷 단위 데이터에 기대타수 모델(dynamic programming)을 적용. 스킬 카테고리별 순위화 + 코스 난이도 평가.",
    "significance":"오늘날 투어·방송·코칭의 표준 지표가 된 Strokes Gained의 학술적 토대. 골프 분석학의 전환점이다.",
    "takeaway":"모든 샷을 '기대 타수'로 평가하니, 성적의 약 2/3는 퍼팅이 아니라 롱게임에서 갈렸다.",
    "extra":"""
<section><h2>Strokes Gained 핵심 개념</h2>
<div class="box" style="margin-bottom:14px"><b>정의</b> — 어떤 샷의 '획득 타수' = (샷 <u>전</u> 위치의 기대타수) − (샷 <u>후</u> 위치의 기대타수) − 1. 값이 <b>양수면 필드 평균보다 이득</b>, 음수면 손해.</div>
<div class="prog">
  <div class="progcol"><h3>롱게임</h3><ul><li>티샷·페어웨이 등 100야드 밖 샷</li><li>선수 간 스코어 차의 <b>약 2/3</b> 설명</li></ul></div>
  <div class="progcol"><h3>숏게임</h3><ul><li>100야드 이내 어프로치·칩·벙커</li><li>스코어 기여도 상대적으로 작음</li></ul></div>
  <div class="progcol"><h3>퍼팅</h3><ul><li>그린 위 스트로크</li><li>통념보다 기여도 작음(전부가 아님)</li></ul></div>
</div>
<p class="note">'퍼팅이 우승을 만든다'는 오랜 통념을 데이터로 뒤집은 것이 이 논문의 핵심. (출처: Broadie 2012)</p>
</section>"""},

 12:{"part":"PART 02 · 경기력·데이터","title":"Search for the Perfect Swing",
    "authors":"Cochran, A. & Stobbs, J. (1968)","journal":"단행본(전 35장) · Golf Society of Great Britain 과학연구 (1963 가을~1968.10)","cites":"골프 과학의 초석 · 전 35장",
    "tags":["이중진자","6년 연구","35장"],
    "summary":"영국골프협회(GSGB)가 물리·탄도학·해부학·인간공학·사이버네틱스 과학자들을 모아 <b>약 6년(1963~68)</b>간 진행한 대형 다학제 프로젝트. Alastair Cochran이 연구를 총괄하고 The Observer 골프 기자 John Stobbs가 공저했다. 골프 스윙을 처음으로 물리 과학으로 규명한 <b>기념비적 저서(전 35장)</b>.",
    "findings":[
      "스윙을 최초의 <b>이중 진자(double pendulum) 모델</b>로 정식화 — 어깨·팔(윗 레버)과 클럽(아랫 레버)이 손목에서 경첩처럼 연결되어 <b>하나의 기울어진 평면(스윙 플레인)</b>에서 회전한다.",
      "정상급 선수는 클럽헤드를 <b>시속 100마일+</b>로 휘둘러 볼을 <b>시속 130마일+</b>로 발사함을 계측.",
      "<b>지연 타격(delayed/late hit)</b> — 손목 코킹을 늦게 푸는 것이 클럽헤드 스피드를 높인다는 원리를 역학으로 설명.",
      "'왼팔을 곧게, 머리를 고정, 체중 이동' 같은 <b>전통 레슨 격언을 물리로 번역</b>해 왜 맞는지 근거를 댔다.",
      "잘 맞은 샷뿐 아니라 <b>최악의 미스샷 물리</b>, 볼의 <b>양력·항력 공기역학</b>, 스윙 중 <b>샤프트의 휨</b>, 프로 대회의 <b>통계·전략 분석</b>까지 폭넓게 다뤘다."],
    "method":"수백 장의 왜곡 없는 스트로보스코프(다중섬광) 사진으로 스윙·임팩트·팔로스루를 분석하고, 속도·질량·임팩트의 수학적 모델을 세움. Bernard Hunt·Neil Coles 등 톱 프로 다수가 실험에 참여. 초기 <b>컴퓨터로 탄도를 예측</b>(런치 모니터보다 약 40년 앞섬).",
    "significance":"이후의 골프 생체역학·장비 연구가 거의 예외 없이 참조하는 원류. '게임의 역학·이론·실제를 다룬 역대 최고의 책'으로 평가되며, 훗날 모션캡처로 검증된 스윙 이론들을 수십 년 앞서 제시했다.",
    "takeaway":"현대 골프 과학은 사실상 이 책(이중 진자 모델 + 톱 프로 계측 + 초기 컴퓨터)에서 출발했다.",
    "extra":"""
<section><h2>이중 진자 모델 — 스윙을 '두 개의 레버'로</h2>
<div class="box" style="margin-bottom:16px">이 책이 제시한 핵심 틀. 스윙을 하나의 고정점(hub)을 중심으로 회전하는 <b>두 개의 연결된 진자</b>로 본다. 이후 거의 모든 골프 스윙 모델링의 출발점이 됐다.</div>
<div class="prog">
  <div class="progcol"><h3>윗 레버</h3><ul><li>어깨 + 양팔</li><li>몸통 회전으로 구동</li></ul></div>
  <div class="progcol"><h3>경첩(hinge)</h3><ul><li>손목</li><li>코킹을 <b>늦게 풀수록</b>(지연 타격) 클럽 스피드 ↑</li></ul></div>
  <div class="progcol"><h3>아랫 레버</h3><ul><li>클럽(샤프트+헤드)</li><li>기울어진 <b>단일 스윙 플레인</b>에서 가속</li></ul></div>
</div>
</section>
<section><h2>전 35장이 다룬 범위</h2>
<div class="box">① 스윙의 <b>이중 진자 역학 모델</b> · ② 잘 맞은 샷과 <b>최악의 미스샷</b>의 물리 · ③ 골프공의 <b>양력·항력 공기역학</b>과 비행 궤도 · ④ 스윙 중 <b>샤프트의 휨</b> 거동 · ⑤ 프로 토너먼트의 <b>통계·전략 분석</b>. 여기에 전통 스윙 레슨(왼팔·머리·체중이동)을 물리로 뒷받침했다.</div>
<p class="note">연구 착수 1963년 가을 → 1968년 10월 출간. 참여 과학자 분야: 물리·탄도학·해부학·인체 생체역학·인간공학·사이버네틱스. (공동 연구 총괄: Alastair Cochran)</p>
</section>"""},

 13:{"part":"PART 02 · 경기력·데이터","title":"골프 스윙 중 근활성(EMG)",
    "authors":"McHardy, A. & Pollard, H. (2005)","journal":"British Journal of Sports Medicine, 39(11), 799–804 · PMID 16244187","cites":"약 다수 인용",
    "tags":["EMG","리뷰 9편","근활성"],
    "summary":"1965~2005년 EMG 연구 <b>9편(근육 17종)</b>을 종합해, 골프 스윙 5국면별로 어떤 근육이 활성화되는지 정리한 문헌 리뷰. 대상 골퍼는 대부분 핸디캡 5 이하 숙련자.",
    "findings":[
      "스윙을 <b>백스윙·포워드스윙·가속·초기 팔로스루·후기 팔로스루</b> 5국면으로 나눠 근활성을 정리.",
      "<b>대흉근(pectoralis major)</b>이 양쪽·여러 국면에서 가장 활발 — 스윙을 구동하는 핵심 근육.",
      "<b>이두·삼두·삼각근은 어느 국면에서도 상위 2위 안에 못 듦</b> — 팔의 굵은 근육 의존도는 낮다.",
      "골프 근력 훈련은 팔 근육이 아니라 <b>기능적 움직임과 핵심 근육군(특히 흉부·몸통)</b>에 집중해야.",
      "<b>전완(forearm) 근육</b> EMG 데이터가 부족해 향후 연구가 필요하다."],
    "method":"EMG 기반 골프 스윙 연구를 종합한 리뷰. 근활성을 최대 수의수축(MVC) 대비 %로 비교, 총 17개 근육 검토.",
    "significance":"'어떤 근육을 강화·보호해야 하는가'의 기준을 제시해 부상·컨디셔닝 연구에서 널리 인용된다.",
    "takeaway":"스윙은 팔 근육이 아니라 대흉근·몸통이 주도한다 — 훈련도 거기에 맞춰야."},

 16:{"part":"PART 02 · 경기력·데이터","title":"프로·아마추어 스윙 운동학 비교",
    "authors":"Zheng, N., Barrentine, S.W., Fleisig, G.S. & Andrews, J.R. (2008)","journal":"Int. J. Sports Medicine, 29(6), 487–493","cites":"약 다수 인용",
    "tags":["프로10·아마5","3D 운동학","일관성"],
    "summary":"프로 <b>10명</b>과 아마추어 <b>5명</b>의 스윙을 3D로 비교해, 몸통·골반 회전과 X-factor·S-factor 등이 클럽헤드 스피드와 어떻게 연결되는지 분석한 연구.",
    "findings":[
      "프로가 아마추어보다 <b>백스윙 정점에서 더 큰 몸통 회전</b>을 만든다.",
      "프로 그룹은 핵심 역학 변수의 <b>일관성(변동계수)이 매우 높다</b> — 자유모멘트 6.8%, X-factor 7.4%, S-factor 8.4%.",
      "임팩트 시 클럽헤드 스피드는 몸통 회전·<b>X-factor(상하체 분리)</b>·정규화 자유모멘트와 연관.",
      "숙련도 차이는 단순 힘보다 <b>동작의 재현성(일관성)</b>에서 두드러진다."],
    "method":"프로·아마추어의 스윙을 3D 운동학·운동역학으로 측정. 상체·골반 회전, X-factor, O-factor(골반 경사), S-factor(어깨 경사), 정규화 자유모멘트를 클럽헤드 스피드와 관련지어 분석.",
    "significance":"'무엇이 프로를 프로답게 하는가'를 운동학적으로 보여줘 코칭·평가의 기준점이 됐다.",
    "takeaway":"프로와 아마추어의 진짜 차이는 힘보다 회전 크기와 '일관성'이다."},

 17:{"part":"PART 02 · 경기력·데이터","title":"엘리트 골프: 결과·기술·신체의 관계",
    "authors":"Hellström, J. (2009)","journal":"Sports Medicine, 39(9), 723–741 · PMID 19691363","cites":"종설",
    "tags":["종설","GIR·스크램블","통합"],
    "summary":"엘리트 골프에서 경기 결과·기술·신체 특성이 어떻게 연결되는지를 종합한 리뷰. 어떤 통계가 스코어와 가장 강하게 연관되는지, 무엇이 클럽헤드 스피드를 만드는지를 정리했다.",
    "findings":[
      "평균 스코어와 상관이 가장 강한 3대 지표: <b>GIR(정규 온그린)·스크램블링·퍼트/GIR</b>.",
      "높은 클럽헤드 스피드는 백스윙 정점의 <b>큰 척추 회전+어깨거들 전인</b>, 높은 지면반력·토크와 연관.",
      "다운스윙에서 분절 각속도가 <b>상향식(bottom-up)으로 순차 증가</b>하고 손목이 늦게 풀릴 때 스피드가 난다.",
      "팔·샤프트 길이와 클럽 스피드는 <b>단순 선형보다 2차(quadratic) 관계</b>일 수 있다(관성모멘트 영향).",
      "근력·유연성 등 신체 특성이 기량·클럽 스피드와 연관되며, 훈련 효과는 방법·수준에 따라 다르다."],
    "method":"경기 통계·클럽헤드 역학·X-factor·지면반력·신체 파라미터 관련 선행연구를 종합한 내러티브 리뷰.",
    "significance":"흩어진 요인들을 하나의 그림으로 묶어 엘리트 골프 수행의 결정 요인을 조망했다.",
    "takeaway":"엘리트 성적은 GIR·스크램블·퍼트 지표로 드러나고, 스피드는 회전·지면반력·순차 협응에서 나온다."},

 18:{"part":"PART 02 · 경기력·데이터","title":"고숙련 골퍼의 근력·유연성·균형",
    "authors":"Sell, T.C., Tsai, Y.-S., Smoliga, J.M., Myers, J.B. & Lephart, S.M. (2007)","journal":"J. Strength & Cond. Research, 21(4), 1166–1171 · PMID 18076270","cites":"약 다수 인용",
    "tags":["N=257","핸디캡 3군","근력·유연성"],
    "summary":"남성 골퍼 <b>257명</b>을 핸디캡으로 3군(≤0 / 1–9 / 10–20)으로 나눠, 근력·유연성·균형이 숙련도에 따라 어떻게 다른지 비교한 연구.",
    "findings":[
      "최상급군(핸디캡 ≤0)은 최하위군보다 <b>고관절·몸통·어깨 근력, 유연성, (눈 뜬)균형</b>이 유의하게 우수.",
      "우측 <b>몸통 회전 근력</b>: ≤0군 157 vs 10–20군 123 (%체중, p=0.001).",
      "우측 <b>고관절 외전 근력</b>: ≤0군 154 vs 10–20군 122 (%체중, p=0.001).",
      "자가보고 <b>드라이빙 거리</b>: 281 → 263 → 252야드로 3군 모두 유의차(p=0.001).",
      "핸디캡과 드라이빙 거리 상관 <b>r=−0.48</b> — 핸디캡이 낮을수록 거리가 길다. 이 특성들은 훈련으로 개선 가능."],
    "method":"기술적 코호트. Biodex로 등속성/등척성 근력, 고니오미터로 ROM, Kistler 힘판(100Hz)으로 단일다리 균형(눈 뜨고/감고) 측정.",
    "significance":"'골프를 잘 치려면 어떤 체력이 필요한가'를 대규모 데이터로 제시해 골프 컨디셔닝 프로그램 설계의 근거가 됐다.",
    "takeaway":"코어(고관절·몸통) 근력·유연성·균형이 좋을수록 핸디캡이 낮고 드라이브가 길다.",
    "extra":"""
<section><h2>핸디캡 그룹별 비교</h2>
<table class="dtab"><thead><tr><th>지표</th><th>핸디캡 ≤0<br>(n=45)</th><th>1–9<br>(n=120)</th><th>10–20<br>(n=92)</th></tr></thead>
<tbody>
<tr><td>드라이빙 거리 (yd)</td><td>281</td><td>263</td><td>252</td></tr>
<tr><td>우 몸통회전 근력 (%BW)</td><td>157</td><td>—</td><td>123</td></tr>
<tr><td>우 고관절외전 근력 (%BW)</td><td>154</td><td>—</td><td>122</td></tr>
</tbody></table>
<p class="note">%BW = 체중 대비 최대토크. 핸디캡이 낮은(잘 치는) 군일수록 코어 근력과 거리가 높다(p=0.001). (출처: Sell et al. 2007)</p>
</section>"""},

 19:{"part":"PART 02 · 경기력·데이터","title":"골프 경기력 개발에서 생리학의 역할",
    "authors":"Smith, M. F. (2010)","journal":"Sports Medicine, 40(8), 635–655 · PMID 20632736 · Univ. of Lincoln","cites":"종설",
    "tags":["생리학","컨디셔닝","모니터링"],
    "summary":"골프 경기력의 생리학적 기반(심폐·대사·호르몬·근골격·영양)을 정리한 종설. 골프를 '기술 종목'을 넘어 체력·컨디셔닝의 관점에서 조망한다.",
    "findings":[
      "일관된 고성능에는 코스 요구에 맞춰 <b>설계·모니터링된 체력 컨디셔닝</b>이 필요하다.",
      "<b>골프 특화 평가</b>로 성능에 직접 영향을 주는 신체 속성을 신뢰성 있게 측정해야 한다.",
      "훈련은 <b>전신 기초 체력 + 골프 특화 기능적 근력·유연성</b>에 초점을 둔다.",
      "시즌 내 최적 시점에 최상 컨디션에 도달하도록 <b>지속적 모니터링</b>이 필요하다.",
      "심폐·대사·호르몬·영양 요구가 라운드 내·라운드 간에 함께 작용한다."],
    "method":"골프 생리학 문헌을 종합한 내러티브 리뷰(구체 수치는 미제시).",
    "significance":"'기술 종목'으로만 보던 골프에 체력·생리 관리라는 관점을 체계적으로 정립했다.",
    "takeaway":"골프도 개별화된 체력 컨디셔닝과 지속 모니터링이 뒷받침돼야 끝까지 잘 친다."},

 20:{"part":"PART 02 · 경기력·데이터","title":"트레이닝을 통한 부상 예방·경기력 향상",
    "authors":"Meira, E.P. & Brumitt, J. (2010)","journal":"Sports Health, 2(4), 337–344 · PMID 23015957","cites":"실용 리뷰",
    "tags":["부상예방","요통","트레이닝"],
    "summary":"트레이닝이 골프 부상 예방과 경기력 향상을 동시에 달성할 수 있음을 정리한 임상 지향 리뷰. 부상 원인과 훈련 효과를 함께 다룬다.",
    "findings":[
      "<b>저요통(low back pain)</b>이 아마추어·프로 공통의 주된 골프 관련 질환 — 요추의 압박·전단·회전·측굴 힘이 원인.",
      "부상은 <b>준비운동 부족, 몸통 유연성·근력 저하, 잘못된 스윙, 과사용</b>과 연관.",
      "리뷰가 인용한 중재연구들: 클럽헤드 스피드 <b>+1.5~24%</b>, 드라이빙 거리 <b>+4.3%</b> 향상 사례.",
      "<b>유연성·근력·파워 훈련 + 스윙 역학 교정</b>을 결합한 프로그램이 부상을 줄이고 수행을 높인다.",
      "부상 예방과 수행 향상은 <b>상충하지 않고 함께 간다</b>."],
    "method":"MEDLINE·CINAHL·SPORTDiscus(~2009.11) 검색 기반 문헌 리뷰. 골프 부상·스윙 역학·훈련 루틴·프로그램 설계 연구를 종합(자체 데이터 없음).",
    "significance":"임상가·코치가 바로 적용할 수 있는 '부상 예방 = 수행 향상' 프레임을 제시했다.",
    "takeaway":"코어·유연성 중심 트레이닝 + 스윙 교정은 요통을 막고 비거리도 늘린다."},
}

# duplicate cards: card_id -> target paper id
dups = {14:1, 15:3}

# ---------------------------------------------------------------
# Reference identifiers (real hyperlinks). Merged into `papers`
# so they propagate to golf_data.json and V2 automatically.
#   kind "PMID" -> https://pubmed.ncbi.nlm.nih.gov/<id>/
#   kind "DOI"  -> https://doi.org/<id>
#   kind "URL"  -> explicit url/label (books, non-indexed items)
# ---------------------------------------------------------------
REFS = {
 1:[{"kind":"PMID","id":"15896091"}],
 2:[{"kind":"PMID","id":"17685707"},{"kind":"DOI","id":"10.1519/R-20606.1"}],
 3:[{"kind":"PMID","id":"17852693"}],
 4:[{"kind":"URL","url":"https://scholar.google.com/scholar?q=Cheetham+X-Factor+Stretch+golf+swing+Optimising+Performance","label":"Google Scholar"}],
 5:[{"kind":"PMID","id":"9531005"}],
 6:[{"kind":"PMID","id":"15562177"}],
 7:[{"kind":"PMID","id":"24627666"}],
 8:[{"kind":"PMID","id":"20845215"}],
 9:[{"kind":"PMID","id":"21699094"}],
 10:[{"kind":"DOI","id":"10.1080/14763141.2011.638723"}],
 11:[{"kind":"DOI","id":"10.1287/inte.1120.0626"}],
 12:[{"kind":"URL","url":"https://scholar.google.com/scholar?q=Search+for+the+Perfect+Swing+Cochran+Stobbs","label":"Google Scholar"}],
 13:[{"kind":"PMID","id":"16244187"}],
 16:[{"kind":"PMID","id":"18004680"},{"kind":"DOI","id":"10.1055/s-2007-989229"}],
 17:[{"kind":"PMID","id":"19691363"}],
 18:[{"kind":"PMID","id":"18076270"}],
 19:[{"kind":"PMID","id":"20632736"}],
 20:[{"kind":"PMID","id":"23015957"}],
}
for _pid, _refs in REFS.items():
    if _pid in papers:
        papers[_pid]["refs"] = _refs


def ref_links(p):
    """Render clickable DOI/PMID/URL chips for a paper's cite box."""
    refs = p.get("refs", [])
    if not refs:
        return ""
    out = []
    for r in refs:
        kind = r.get("kind")
        if kind == "PMID":
            url, label = f"https://pubmed.ncbi.nlm.nih.gov/{r['id']}/", f"PMID {r['id']}"
        elif kind == "DOI":
            url, label = f"https://doi.org/{r['id']}", f"DOI {r['id']}"
        else:
            url, label = r["url"], r.get("label", "원문 링크")
        out.append(f'<a class="reflink" href="{html.escape(url)}" target="_blank" rel="noopener">'
                   f'{html.escape(label)} <span class="ext">↗</span></a>')
    return '<div class="reflinks"><span class="reflab">원문</span>' + "".join(out) + '</div>'

# order of cards in index
partA = [1,2,3,4,5,6,7,8,9,10]
partB = [11,12,13,14,15,16,17,18,19,20]
# 14·15 are duplicates of 1·3, so there are 18 unique papers ("18선").
# Keep file names / pids stable; only the DISPLAYED badge is renumbered 1..18.
order = [i for i in (partA + partB) if i not in dups]
DISP = {pid: n + 1 for n, pid in enumerate(order)}

CSS = """
:root{--bg:#FDEEF3;--bg-soft:#FCE4EC;--hot:#FF1E88;--hot-deep:#E60F73;--ink:#0E0E10;--white:#FFFFFF;--line:#F4C9DC;--muted:#6B5560;}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:'Pretendard','Apple SD Gothic Neo','Segoe UI',system-ui,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased;}
"""


# ---------------------------------------------------------------
# Branding: mascot favicon, Instagram footer, card corner watermark
# ---------------------------------------------------------------
IG_URL = "https://www.instagram.com/mummys_hand_golf/"
IG_HANDLE = "@mummys_hand_golf"

BRAND_CSS = """
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

def brand_footer(prefix):
    return (f'<div class="brand"><img src="{prefix}assets/mascot.png" alt="마미손 골프 마스코트">'
            f'<a class="brand-ig" href="{IG_URL}" target="_blank" rel="noopener">'
            f'{_IG_SVG}{IG_HANDLE}</a></div>')

def card_watermark(prefix):
    return (f'<a class="cardwm" href="{IG_URL}" target="_blank" rel="noopener" '
            f'aria-label="Instagram {IG_HANDLE}"><img src="{prefix}assets/wm.png" alt="">'
            f'<span>{IG_HANDLE}</span></a>')

PIG = ('<a class="pig" href="https://www.instagram.com/mummys_hand_golf/" target="_blank" '
       'rel="noopener"><img src="../assets/wm.png" alt="">@mummys_hand_golf</a>')
CIRC = "①②③④⑤⑥⑦⑧"

# Scroll-stopping hooks for each card's cover (curiosity opener, distinct from the takeaway).
HOOKS = {
 1: "장타는 '힘'으로만 치는 게 아니다?",
 2: "집에서 밴드 하나로 비거리가 는다면?",
 3: "골반을 '덜' 돌려야 볼 스피드가 오른다?",
 4: "X팩터, 크기보다 중요한 게 따로 있다.",
 5: "싱글의 스윙엔 '순서'가 있다.",
 6: "티오프 전 5분이 클럽 스피드를 바꾼다.",
 7: "힘만 키우면 장타? 절반만 맞다.",
 8: "볼 스피드의 73%는 이 4가지로 정해진다.",
 9: "스윙이 매번 흔들리는 게 나쁜 걸까?",
 10: "퍼팅은 손목이 아니다.",
 11: "'퍼팅이 우승을 만든다'는 거짓말?",
 12: "현대 골프 과학은 이 책에서 시작됐다.",
 13: "스윙의 주인공은 팔이 아니었다.",
 16: "프로와 아마의 차이는 '힘'이 아니다.",
 17: "잘 치는 선수는 대체 뭐가 다를까?",
 18: "핸디캡을 낮추는 건 스윙이 아니라 몸?",
 19: "라운드 후반에 무너지는 진짜 이유.",
 20: "요통 없이 비거리까지 늘리는 법.",
}

# Site-wide top nav (home / V1 / V2 / V3). prefix reaches the site root from the page.
NAV_CSS = (
 ".sitenav{display:flex;flex-wrap:wrap;justify-content:center;gap:5px;margin:0 auto 16px;padding:0 12px}"
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

def detail_html(pid, p):
    # V1 = Instagram carousel. One idea per 4:5 slide: cover, each finding, takeaway.
    finds = p["findings"][:8]
    v2href = f"../v2/pages/paper-{pid:02d}.html"
    total = len(finds) + 2
    hook = HOOKS.get(pid, p["takeaway"])
    S = []
    # 1) cover — leads with a scroll-stopping hook
    S.append(f"""<div class="slide cover" id="s1">
  <div class="stop"><span class="pno">{DISP[pid]:02d}</span><span class="ppart">{html.escape(p['part'])}</span><img class="smasc" src="../assets/mascot.png" alt="마미손 골프 마스코트"></div>
  <div class="chook">{html.escape(hook)}</div>
  <div class="csub"><span class="clab">논문</span>{html.escape(p['title'])}</div>
  <div class="ccite"><b>{html.escape(p['authors'])}</b> · {html.escape(p['journal'])}<div class="cpill">{html.escape(p['cites'])}</div></div>
  <div class="sfoot">{PIG}<span class="swipe">밀어서 다음 <b>→</b></span></div>
</div>""")
    # 2) one finding per slide
    for i, f in enumerate(finds):
        S.append(f"""<div class="slide" id="s{i+2}">
  <div class="stop"><span class="slabel">핵심 발견 {CIRC[i]}</span><img class="smasc" src="../assets/mascot.png" alt=""></div>
  <div class="sbody"><p class="ftext">{f}</p></div>
  <div class="sfoot">{PIG}<span class="swipe">밀어서 다음 <b>→</b></span></div>
</div>""")
    # 3) takeaway
    S.append(f"""<div class="slide take" id="s{total}">
  <div class="stop"><span class="slabel">ONE-LINE 결론</span><img class="smasc" src="../assets/mascot.png" alt=""></div>
  <div class="sbody"><p class="ttext">{p['takeaway']}</p></div>
  <div class="sfoot">{PIG}<a class="more" href="{v2href}">근거 자세히 → V2</a></div>
</div>""")
    # 4) CTA — save/follow/like/comment + weekly full-version notice
    S.append(f"""<div class="slide cta" id="s{total+1}">
  <div class="stop"><span class="slabel">SAVE · FOLLOW</span><img class="smasc" src="../assets/mascot.png" alt=""></div>
  <div class="sbody" style="flex-direction:column;align-items:stretch;justify-content:center">
    <div class="cta-h">이 시리즈,<br><b>매주</b> 이어집니다</div>
    <div class="cta-open"><b>🌐 풀버전 딥다이브</b><span>매주 월요일 저녁 8시 · 웹사이트 오픈</span></div>
    <div class="cta-list">
      <div class="cta-item"><span class="cta-emoji">🔖</span><span class="cta-txt">저장<span>연습 전에 다시 꺼내 보기</span></span></div>
      <div class="cta-item"><span class="cta-emoji">➕</span><span class="cta-txt">팔로우<span>매주 새 편 놓치지 않기</span></span></div>
      <div class="cta-item"><span class="cta-emoji">❤️</span><span class="cta-txt">좋아요 · 댓글 💬<span>궁금한 점·다음에 볼 주제 남기기</span></span></div>
    </div>
  </div>
  <div class="sfoot">{PIG}<span class="hint">EP.{DISP[pid]} / 18</span></div>
</div>""")
    slides = "\n".join(S)
    return f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(p['title'])} — 카드</title>
{favicon_links("../")}
<style>{CSS}{NAV_CSS}
body{{display:flex;flex-direction:column;align-items:center;min-height:100vh;padding:22px 0 40px}}
.carousel{{display:flex;flex-direction:column;align-items:center;gap:20px;width:100%;padding:4px 16px}}
.slide{{position:relative;width:min(92vw,440px);aspect-ratio:4/5;background:linear-gradient(165deg,#fff 0%,#FFF2F7 100%);border:1px solid var(--line);border-radius:26px;box-shadow:0 22px 56px -30px rgba(230,15,115,.55);padding:30px 30px 24px;display:flex;flex-direction:column;overflow:hidden}}
.stop{{display:flex;align-items:center;gap:12px;margin-bottom:16px}}
.pno{{font-size:30px;font-weight:900;color:#fff;background:var(--hot);min-width:56px;height:56px;padding:0 6px;border-radius:15px;display:flex;align-items:center;justify-content:center;letter-spacing:-.02em}}
.smasc{{width:46px;height:46px;margin-left:auto;filter:drop-shadow(0 5px 10px rgba(230,15,115,.3))}}
.slabel{{font-size:13px;font-weight:800;letter-spacing:.02em;color:#fff;background:var(--hot);padding:7px 15px;border-radius:999px}}
.ppart{{font-size:12px;font-weight:800;letter-spacing:.09em;color:var(--muted);text-transform:uppercase;margin-bottom:6px}}
.chook{{font-size:33px;font-weight:900;letter-spacing:-.02em;line-height:1.28;color:var(--ink);margin:6px 0 16px;padding-left:14px;border-left:5px solid var(--hot)}}
.csub{{font-size:17.5px;font-weight:800;line-height:1.45;color:var(--muted)}}
.clab{{display:inline-block;font-size:10px;font-weight:800;letter-spacing:.08em;color:#fff;background:var(--ink);padding:3px 9px;border-radius:999px;margin-right:8px;vertical-align:middle}}
.ppart{{flex:1}}
.ccite{{font-size:14px;line-height:1.6;color:var(--muted);font-weight:600;margin-top:auto}}
.ccite b{{color:var(--ink);font-weight:800}}
.cpill{{display:inline-block;margin-top:9px;background:var(--hot);color:#fff;font-size:12px;font-weight:800;padding:4px 13px;border-radius:999px}}
.sbody{{flex:1;display:flex;align-items:center;padding:6px 0}}
.ftext{{font-size:27px;font-weight:750;line-height:1.5;color:var(--ink)}}
.ftext b{{color:var(--hot-deep)}}
.slide.take{{background:var(--ink);border-color:var(--ink)}}
.slide.take .slabel{{background:var(--hot)}}
.ttext{{font-size:31px;font-weight:800;line-height:1.45;color:#fff}}
.ttext b{{color:var(--hot)}}
.sfoot{{display:flex;align-items:center;justify-content:space-between;gap:10px;border-top:1px solid var(--line);padding-top:13px;margin-top:12px}}
.slide.take .sfoot{{border-top-color:rgba(255,255,255,.18)}}
.pig{{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:800;color:var(--hot-deep);text-decoration:none;white-space:nowrap}}
.pig img{{width:22px;height:22px}}
.slide.take .pig{{color:#fff}}
.hint,.sidx{{font-size:12px;font-weight:800;color:var(--muted)}}
.more{{font-size:12.5px;font-weight:800;color:var(--hot);text-decoration:none;white-space:nowrap}}
.swipe{{display:inline-flex;align-items:center;gap:8px;background:var(--hot);color:#fff;font-size:14px;font-weight:900;letter-spacing:.01em;padding:9px 17px;border-radius:999px;box-shadow:0 8px 18px -8px rgba(230,15,115,.75)}}
.swipe b{{font-size:18px;line-height:1;animation:nudge 1s ease-in-out infinite}}
@keyframes nudge{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(5px)}}}}
.swipehint{{margin-top:14px;font-size:13px;color:var(--muted);font-weight:700;text-align:center}}
.controls{{width:min(92vw,460px);display:flex;justify-content:space-between;gap:10px;margin:6px auto 0}}
.controls a{{font-size:13px;font-weight:800;color:var(--hot-deep);text-decoration:none;background:var(--white);border:1px solid var(--line);padding:9px 16px;border-radius:999px}}
.controls a:hover{{background:var(--hot);color:#fff;border-color:var(--hot)}}
.slide.cta{{background:linear-gradient(165deg,#fff 0%,#FFF2F7 100%);border-color:var(--line)}}
.cta-h{{font-size:28px;font-weight:900;line-height:1.26;color:var(--ink);margin:2px 0 12px}}
.cta-h b{{color:var(--hot-deep)}}
.cta-open{{background:linear-gradient(120deg,var(--hot) 0%,var(--hot-deep) 100%);border-radius:14px;padding:12px 16px;margin-bottom:14px;box-shadow:0 12px 22px -12px rgba(230,15,115,.55)}}
.cta-open b{{display:block;font-size:16.5px;font-weight:900;color:#fff;line-height:1.3}}
.cta-open span{{display:block;font-size:13px;font-weight:700;color:rgba(255,255,255,.95);margin-top:3px}}
.cta-list{{display:flex;flex-direction:column;gap:9px;width:100%}}
.cta-item{{display:flex;align-items:center;gap:13px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:11px 15px}}
.cta-emoji{{font-size:21px;line-height:1;flex-shrink:0}}
.cta-txt{{font-size:15.5px;font-weight:800;color:var(--ink);line-height:1.25}}
.cta-txt span{{display:block;font-size:12px;font-weight:600;color:var(--muted);margin-top:2px}}
</style></head>
<body>
{nav("../","v1")}
<div class="carousel">
{slides}
</div>
<p class="swipehint">아래로 스크롤 · 총 {total+1}장 (표지 · 발견 {len(finds)} · 결론 · 팔로우) · 인스타 캐러셀 순서 그대로</p>
<div class="controls"><a href="../golf-research-summary.html">← 목록</a><a href="{v2href}">근거 자세히 보기 →</a></div>
{GC}
</body></html>"""

for pid, p in papers.items():
    with open(os.path.join(PAGES, f"paper-{pid:02d}.html"), "w", encoding="utf-8") as f:
        f.write(detail_html(pid, p))

def card(card_id):
    p = papers[card_id]
    href = f"pages/paper-{card_id:02d}.html"
    tags = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in p["tags"][:2])
    return f"""    <a class="card" href="{href}">
      <div class="card-top">
        <div class="no">{DISP[card_id]}</div>
        <div class="meta">
          <div class="title">{html.escape(p['title'])}</div>
          <div class="cite">{html.escape(p['authors'])} · {html.escape(p['journal'])} · {html.escape(p['cites'])}</div>
          <div class="badges">{tags}</div>
        </div>
      </div>
      <p class="finding">{p['summary']}</p>
      <span class="more">자세히 보기 →</span>
    </a>"""

cardsA = "\n".join(card(i) for i in partA if i not in dups)
cardsB = "\n".join(card(i) for i in partB if i not in dups)

# Hero image: drop a file at assets/hero.<ext> and it replaces the placeholder.
import glob as _glob
_hero = sorted(_glob.glob(os.path.join(OUT, "assets", "hero.*")))
_herorel = "assets/" + os.path.basename(_hero[0]) if _hero else "assets/hero.jpg"
# Always emit the <img>; if the file is missing at view time, onerror falls
# back to the dashed placeholder — so simply dropping assets/hero.jpg later works.
imgspot = (
    f'<div class="imgspot has-img"><img src="{_herorel}" '
    f'alt="핑크 스키마스크를 쓴 골프공 마스코트" '
    f"onerror=\"var p=this.parentNode;p.classList.remove('has-img');"
    f"p.innerHTML='이미지 자리<br>(assets/hero.jpg 추가 시 자동 표시)'\"></div>")

index = f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>골프 경기력 핵심 연구 18선 — 요약</title>
{favicon_links("")}
<style>{CSS}{BRAND_CSS}{NAV_CSS}
.wrap{{max-width:920px;margin:0 auto;padding:56px 24px 96px}}
.sitenav{{margin-top:8px;margin-bottom:0}}
.hero{{text-align:center;padding:40px 0 48px;border-bottom:3px solid var(--hot)}}
.kicker{{display:inline-block;background:var(--hot);color:#fff;font-size:13px;font-weight:800;letter-spacing:.14em;padding:7px 16px;border-radius:999px;margin-bottom:22px}}
.hero h1{{font-size:40px;font-weight:900;letter-spacing:-.02em;line-height:1.22}}
.hero h1 span{{color:var(--hot)}}
.hero p{{margin-top:16px;color:var(--muted);font-size:16px;max-width:620px;margin-left:auto;margin-right:auto}}
.imgspot{{margin:36px auto 0;max-width:360px;aspect-ratio:3/4;background:repeating-linear-gradient(135deg,var(--bg-soft) 0 14px,var(--white) 14px 28px);border:2px dashed var(--hot);border-radius:20px;display:flex;align-items:center;justify-content:center;color:var(--hot-deep);font-weight:700;font-size:14px;text-align:center;padding:20px}}
.imgspot.has-img{{background:none;border:none;padding:0;overflow:hidden;box-shadow:0 16px 38px -18px rgba(230,15,115,.55)}}
.imgspot.has-img img{{width:100%;height:100%;object-fit:cover;display:block}}
.sec{{margin-top:72px}}
.sec-head{{display:flex;align-items:baseline;gap:14px;margin-bottom:8px}}
.sec-num{{font-size:15px;font-weight:900;color:#fff;background:var(--ink);padding:4px 12px;border-radius:8px;letter-spacing:.05em}}
.sec-head h2{{font-size:26px;font-weight:900;letter-spacing:-.01em}}
.sec-sub{{color:var(--muted);font-size:14px;margin-bottom:28px;padding-left:2px}}
.card{{display:block;text-decoration:none;color:inherit;background:var(--white);border-radius:18px;padding:26px 28px;margin-bottom:18px;border:1px solid var(--line);box-shadow:0 6px 22px -14px rgba(230,15,115,.35);position:relative;transition:transform .15s ease,box-shadow .15s ease}}
.card:hover{{transform:translateY(-3px);box-shadow:0 14px 30px -14px rgba(230,15,115,.55)}}
.card::before{{content:"";position:absolute;left:0;top:22px;bottom:22px;width:5px;background:var(--hot);border-radius:0 6px 6px 0}}
.card-top{{display:flex;align-items:flex-start;gap:16px;margin-bottom:14px}}
.no{{flex:0 0 auto;width:42px;height:42px;border-radius:12px;background:var(--hot);color:#fff;font-size:19px;font-weight:900;display:flex;align-items:center;justify-content:center}}
.meta{{flex:1}}
.title{{font-size:18px;font-weight:800;letter-spacing:-.01em;line-height:1.4}}
.cite{{font-size:13px;color:var(--muted);margin-top:4px}}
.badges{{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}}
.tag{{font-size:11px;font-weight:700;letter-spacing:.03em;background:var(--bg-soft);color:var(--hot-deep);padding:4px 10px;border-radius:999px;border:1px solid var(--line)}}
.tag.dup{{background:var(--ink);color:#fff;border-color:var(--ink)}}
.finding{{font-size:15px;color:var(--ink);padding-left:2px}}
.more{{display:inline-block;margin-top:14px;font-size:13px;font-weight:800;color:var(--hot-deep);letter-spacing:.02em}}
.card:hover .more{{color:var(--ink)}}
.footnote{{margin-top:64px;padding:22px 24px;background:var(--white);border-radius:16px;border:1px dashed var(--line);font-size:13px;color:var(--muted);line-height:1.7}}
.footnote b{{color:var(--ink)}}
@media(max-width:560px){{.hero h1{{font-size:30px}}.card{{padding:22px 20px}}.wrap{{padding:36px 16px 72px}}}}
</style></head>
<body><div class="wrap">
  {nav("","v1")}
  <header class="hero">
    <span class="kicker">GOLF PERFORMANCE · RESEARCH</span>
    <h1>골프 경기력을 만든<br><span>핵심 연구 18선</span></h1>
    <p>비거리·정확성·퍼팅·부상예방까지 — 영향력 있는 논문 18편을 <b>인스타그램 카드</b>로 정리했습니다. 카드를 누르면 <b>스와이프 카드 세트</b>(표지·발견·결론)가 열려요. 더 깊은 근거는 전문가용(V2)에서.</p>
    {imgspot}
  </header>
  <section class="sec">
    <div class="sec-head"><span class="sec-num">PART 01</span><h2>생체역학 · 스윙 메커니즘</h2></div>
    <p class="sec-sub">인용 영향력 기준 대략 순위 · 수치는 추정치</p>
{cardsA}
  </section>
  <section class="sec">
    <div class="sec-head"><span class="sec-num">PART 02</span><h2>경기력 · 데이터 · 종합</h2></div>
    <p class="sec-sub">인용 영향력 기준 대략 순위 · 수치는 명시하지 않거나 추정</p>
{cardsB}
  </section>
  <div class="footnote">
    <b>참고 —</b> 인용 횟수는 Google Scholar 등 검색엔진·데이터베이스와 시점에 따라 달라지므로, 위 순서는 <b>인용 영향력 기준 대략적 순위</b>이며 수치는 추정치입니다. 원자료에서 중복된 2편을 제외한 <b>18편</b>입니다.
  </div>
  {brand_footer("")}
{GC}</div></body></html>"""

with open(os.path.join(OUT, "golf-research-summary.html"), "w", encoding="utf-8") as f:
    f.write(index)

print("detail pages:", len(papers))
print("files:", len(os.listdir(PAGES)))
