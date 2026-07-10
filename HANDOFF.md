# HANDOFF — 골프 경기력 핵심 연구 20선 (정적 사이트)

Claude Code에서 이 프로젝트를 이어서 작업하기 위한 인수인계 문서.

## 1. 프로젝트 개요
골프 경기력(생체역학·퍼포먼스·트레이닝) 관련 영향력 있는 논문 **20편**(고유 18편 + 중복 2편)을
정적 HTML 사이트로 정리. 네 가지 버전 + 연재/가이드 허브를 제공한다.

- **V1 — 카드용 요약**: 인스타그램 카드 업로드용 간결판. 핑크 카드 디자인. (생성기 `generate.py`)
- **V2 — 전문가용 근거 자료집**: V1과 **동일 디자인**에 연구 설계 라벨·통계·**한계(Limitations)**·참고문헌 추가. (생성기 `generate_v2.py`)
- **V3 — 롱폼 딥다이브**: 논문 18편 전편 + 운동사슬 테마 1편(완간). 손으로 관리하는 정적 페이지(`v3/`).
- **V4 — 최신 연구 트랙**: 2013년 이후 연구를 잇는 사이드 트랙(현재 9편, 계속 추가). 정적 페이지(`v4/`).
- **연재 허브(`series.html`)**: 매주 저녁 8시(KST) 한 편씩 공개하는 날짜 잠금 리더. `generate_series.py`가
  공개된 회차만 iframe으로 심는다(GitHub Action이 매일 재빌드).
- **연습 가이드(`practice-guide.html`)**: 핸디캡별 연습시간 배분(Strokes Gained 근거).
- **접속 게이트**: 홈·V1~V4에 소프트 접속코드 게이트(`<!--MHG_GATE-->`)를 주입. 연재는 공개.

V1·V2는 같은 콘텐츠 데이터(`golf_data.json`)를 공유하며 서로 상호 링크된다.

## 2. 파일 구조
```
generate.py              # V1 생성기 + 콘텐츠 원본(papers 딕셔너리 = 단일 진실원본)
generate_v2.py           # V2 생성기 (golf_data.json을 읽음)
golf_data.json           # generate.py의 papers/dups/partA/partB 스냅샷 (V2 입력)

# 빌드 산출물 (V1)
golf-research-summary.html
pages/paper-01.html ... paper-20.html   # 고유 18개 (14,15 없음: 1,3과 중복)

# 빌드 산출물 (V2)
v2/golf-research-v2.html
v2/pages/paper-01.html ...

# 업로드 패키지
site/                    # index.html(랜딩) + V1 + V2 + README + .nojekyll
golf-research-site.zip   # site/ 압축본 (GitHub Pages 업로드용)
```

## 3. 콘텐츠 데이터 흐름 & 재생성
**단일 진실원본은 `generate.py` 안의 `papers` 딕셔너리.** 각 논문 항목 필드:
`part, title, authors, journal, cites, tags[], summary, findings[], method, significance, takeaway, extra(선택 HTML)`
- `dups = {14:1, 15:3}` — 14·15번 카드는 1·3번 페이지로 연결(중복).
- V2 전용 필드는 `generate_v2.py`의 `meta` 딕셔너리: `{pid: (연구설계 라벨, 한계 문구)}`.

콘텐츠 수정 후 **전체 재생성 순서**:
```bash
python3 generate.py                       # V1 재생성 + papers 갱신
python3 -c "import importlib.util,json; \
 s=importlib.util.spec_from_file_location('g','generate.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); \
 json.dump({'papers':{str(k):v for k,v in m.papers.items()},'dups':{str(k):v for k,v in m.dups.items()},'partA':m.partA,'partB':m.partB}, open('golf_data.json','w'), ensure_ascii=False, indent=1)"
python3 generate_v2.py                     # V2 재생성
# site/ 로 산출물 복사 (덮어쓰기만 — 절대 rm -rf 하지 말 것)
cp golf-research-summary.html site/ && cp -f pages/*.html site/pages/
cp v2/golf-research-v2.html site/v2/ && cp -f v2/pages/*.html site/v2/pages/
python3 generate_series.py                 # 연재 페이지(site/series.html)를 직접 생성
cp site/series.html series.html            # 루트 사본 동기화
```
> ⚠️ **`rm -rf site` 금지.** 랜딩(`site/index.html`)·연재·`.nojekyll`·README 등 생성기가 만들지
> 않는 파일이 site/에만 있어, 통째로 지우면 복구가 불가능하다(루트에 사본 없음). 반드시 개별 덮어쓰기로만 재조립할 것.
> V3(`v3/`)·V4(`v4/`)는 손으로 관리하는 정적 페이지이며 재생성 대상이 아니다 — 수정 시 루트와 `site/` **양쪽**을 직접 편집한다.

## 4. 디자인 테마 토큰 (V1·V2 공통)
```
--bg:#FDEEF3   (흰색에 가까운 핑크, 배경)
--bg-soft:#FCE4EC
--hot:#FF1E88   (핫핑크 포인트)
--hot-deep:#E60F73
--ink:#0E0E10   (검정)
--white:#FFFFFF
--line:#F4C9DC
--muted:#6B5560
```
폰트: Pretendard / Apple SD Gothic Neo / system-ui.

## 5. 완료 / 보류
**완료**
- 20편 전편 원문 조사 기반 내용 보강(표본·장비·통계 수치 포함).
- 데이터 표: paper-03(볼스피드 3군), paper-18(핸디캡 3군). 개념 박스: paper-02(운동 프로그램), paper-11(Strokes Gained), paper-09/10(주석).
- V2 전편에 연구설계 라벨 + 한계(Limitations) 섹션.
- GitHub Pages 업로드 패키지(zip).

**보류 / 다음 작업 후보**
- V1 상단 `이미지 자리`(.imgspot)에 누끼 이미지 삽입 — 이미지 준비되면 교체.
- 각 논문 페이지에 실제 **DOI/PMID 하이퍼링크** 추가(현재는 텍스트).
- V2에 참고문헌(References) 섹션 추가.
- (선택) V2 색인 표를 정렬·필터 가능하게.

## 6. 주의점
- 고유 페이지는 18개(14·15 파일 없음). 링크는 상대경로 → 폴더 구조 유지 필수.
- 통계 부호 렌더링: 본문에 `<`가 숫자 앞에 오면 `&lt;`로 이스케이프(예: `P&lt;0.0001`). `>`도 필요시 `&gt;`.
- **paper-09 (Glazier 2011)**: 실증이 아닌 이론·관점 논문. 정량 결과 없음(내용에 명시).
- **paper-10 (Delphinus & Sayers 2012)**: 원 목록의 "Smith/Roberts/Wallace 퍼팅 리뷰"는 특정 불가하여, 검증된 퍼팅 생체역학 실증 논문으로 대체함.
- `generate.py`는 한글·이모지 많은 대형 파일. 에디터/도구에 따라 대량 편집 시 말미가 잘릴 수 있으니, 편집 후 반드시 `python3 -c "import ast; ast.parse(open('generate.py').read())"`로 구문 확인.

## 7. GitHub Pages 배포
`site/`의 내용을 저장소 루트에 올리고 Settings → Pages → Deploy from a branch(main / root).
공개 URL: `https://<사용자명>.github.io/<저장소명>/`

---

## Claude Code 시작 프롬프트 (복사해서 사용)
> 이 저장소는 "골프 경기력 핵심 연구 20선" 정적 사이트입니다. HANDOFF.md를 먼저 읽어 구조를 파악하세요.
> 콘텐츠 원본은 generate.py의 papers 딕셔너리이고, V2는 golf_data.json을 읽는 generate_v2.py로 생성됩니다.
> 디자인 테마(핑크 #FDEEF3 배경 / 핫핑크 #FF1E88 포인트 / 검정 텍스트)는 유지하세요.
> 다음 작업을 해줘: (1) 각 논문 페이지에 DOI/PMID 실제 하이퍼링크 추가, (2) V2에 References 섹션 추가,
> (3) 준비되면 V1 상단 이미지 자리에 이미지 삽입. 수정 후 generate.py → golf_data.json 재추출 → generate_v2.py →
> site/ 재조립 순으로 재생성하고, 편집마다 python3 ast로 구문을 검증하세요.
