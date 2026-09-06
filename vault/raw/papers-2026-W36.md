---
type: raw-papers
period: 2026-W36
scout-date: 2026-09-06
sources-count:
  arXiv: 6
  Nature: 1
  Nature-Methods: 1
  total: 8
---

> 수집일: 2026-09-06 | 기간: 2026-09-01~2026-09-06 (W36)
> 핵심 5편 · 와이드 3편 | arXiv(q-bio/cs.LG) 6건, Nature 1건, Nature Methods 1건

---

## 핵심 논문 (Core)

### C1. 단일세포 표현 공간에서 개방형 생물학적 발견의 운용화 (Operationalizing open-ended biological discovery across single-cell representations)

- 저자: Ningxuan Zhang, Ziwei Wang, Ning Xie, Na Liu | 소속 미확인
- 소스: arXiv · 2026-09-01
- 상태: preprint(미동료심사)
- DOI/링크: https://arxiv.org/abs/2609.00681
- arXiv ID: arXiv:2609.00681
- 코드: 미확인
- 사회적 신호: 없음
- 요약: 단일세포 연구가 사전 정의된 질문에서 출발하는 관행을 벗어나, 데이터에서 신호를 먼저 추출한 뒤 생물학적 맥락을 부여하는 "개방형 발견(open-ended discovery)" 패러다임을 제안한다. 제안 프레임워크 PROSPECTor는 기존 발현 표현과 다양한 파운데이션 모델 임베딩에 걸쳐 재현 가능한 생물학적 구조를 탐색하고 이를 검증 가능한 가설로 변환한다. 섬유아세포 세포외기질(ECM) 프로그램과 위암 T세포 프로그램에서 독립 코호트·공간 전사체 코호트에 걸친 가설 재현성이 확인되었다고 초록에서 주장한다.
- 핵심 수치: 검증은 독립 마우스 코호트(섬유아세포 ECM) 및 단일세포·벌크·공간 코호트 교차 검증(위암 T세포) 수준; 정량 지표 초록에 명시 없음 — 논문 본문 확인 필요
- 분야 태그: [바이오인포, 단일세포, LLM-bio]
- 선별 사유: 단일세포 데이터에서 파운데이션 모델 임베딩을 포함한 복수 표현을 체계적으로 비교해 가설을 생성하는 프레임워크 — 방법적 신규성이 뚜렷하고, 현재 단일세포 파운데이션 모델 평가 논의와 직접 연결됨

---

### C2. 합성 단백질 어셈블리로부터 바텀업 RNA 전달 비히클 창제 (Creating bottom-up RNA transfer vehicles from synthetic protein assemblies)

- 저자: Schuhmacher M.K. 외 (제1저자), 교신저자 소속 미확인 | Helmholtz Munich · Technische Universität München (TUM)
- 소스: Nature · 2026-09-02
- 상태: peer-reviewed
- DOI/링크: https://doi.org/10.1038/s41586-026-10952-3
- arXiv ID: 없음
- 코드: 미확인
- 사회적 신호: phys.org · news-medical.net · AZoLifeSciences 보도 (2026-09-02~03)
- 요약: 생성형 AI로 설계한 합성 단백질 스캐폴드와 천연 단백질 도메인을 결합해 100종 이상의 합성 전달 비히클(STV, Synthetic Transfer Vehicle)을 구축했다. 다차원 스크리닝으로 선발한 STV-C8은 비자연적 평면 대칭 구조를 가지며, 세포 배양에서 지질나노입자(LNP) 대비 수 자릿수 높은 RNA 전달 효율을 보였다고 보고한다. 계산 설계 펩타이드 바인더를 통한 세포 유형별 표적 프로그래밍과 생체 내(in vivo) 동물 모델 검증도 수행하였다.
- 핵심 수치: STV-C8이 "세포 배양 기준 LNP 대비 수 자릿수(several orders of magnitude) 높은 RNA 전달 효율" — 초록/언론 기준, 정확한 배수는 논문 본문 확인 필요
- 분야 태그: [신약AI, 단백질]
- 선별 사유: AI 설계 단백질 구조물로 RNA 치료제 전달 플랫폼을 새로 구축한 Nature 게재 연구 — mRNA 치료제·유전자 치료의 전달 시스템 병목을 직접 공략하며 산업 함의가 크다

---

### C3. 전사체·단백질 구조·국소화 정보를 활용한 세포소기관 해상도 단일세포 임베딩 학습 (Subcellularly Resolved Single-Cell Embedding Learning with Transcriptomic data, Protein Structure and Localization Information)

- 저자: Zhen Zhou, Jiachen Li, Yuan Liu, Xiaoyong Pan | 교신저자 Hong-Bin Shen | 소속 미확인
- 소스: arXiv · 2026-09-02
- 상태: preprint(미동료심사)
- DOI/링크: https://arxiv.org/abs/2609.02344
- arXiv ID: arXiv:2609.02344
- 코드: 미확인
- 사회적 신호: 없음
- 요약: RNA 발현 프로파일, 단백질 서열 표현, 단백질 3D 구조 정보를 교차 어텐션(cross-attention) 아키텍처로 통합해 세포소기관 해상도의 단일세포 임베딩을 학습하는 멀티모달 프레임워크를 제안한다. 각 세포를 세포내 구획별 미세 조직으로 표현함으로써 분자 발현 패턴과 관련 단백질의 기능적 특성을 동시에 포착하는 것이 목표다.
- 핵심 수치: 초록에 정량 지표 미명시 — 논문 본문 확인 필요; 20쪽 분량, 4개 그림, 1개 표
- 분야 태그: [바이오인포, 단일세포, 단백질]
- 선별 사유: 단일세포 임베딩에 단백질 구조 정보를 세포소기관 해상도로 통합하는 시도 — 기존 전사체 중심 표현의 한계를 확장하는 방법론으로 바이오인포매틱스 연구자에게 직접 활용 가능성이 있음

---

### C4. 약물-표적 상호작용 예측을 위한 탐침 기반 다중 척도 생화학적 패턴 매칭 (ProbeMatchDTI: Probe-Driven Multi-Scale Biochemical Pattern Matching for Drug-Target Interaction Prediction)

- 저자: Quan Hao, Mengyue Fan, Zifan Dong, Youru Li, Jianduo Zhao, Lechuan Xu, Hao Zhang, Fei Xia, Jigang Wang, Chong Qiu, Liguo Zhang | 소속 미확인
- 소스: arXiv · 2026-09-02
- 상태: preprint(미동료심사)
- DOI/링크: https://arxiv.org/abs/2609.02549
- arXiv ID: arXiv:2609.02549
- 코드: https://github.com/developer-hq/ProbeMatchDTI
- 사회적 신호: 없음
- 요약: 기존 DTI(drug-target interaction) 예측 모델의 수동적 특징 집계가 지배적 분자 패턴을 선호하고 결합 관련 약한 신호(기능기·잔기 맥락 패턴)를 억제하는 문제를 제기하며, 학습 가능한 탐침(learnable probe) 기반 프레임워크 ProbeMatchDTI를 제안한다. IterProbe와 BindingProbe 두 모듈로 구성되며, 다중 척도 생화학적 대응(기능기-국소 모티프-분자 스캐폴드)을 강화해 약한 결합 신호도 보존한다.
- 핵심 수치: BindingDB에서 AUC-ROC +2.0%, DrugBank에서 AUC-ROC +0.5% 향상 — 초록 기준
- 분야 태그: [신약AI]
- 선별 사유: DTI 예측에서 약한 생화학적 신호 억제 문제를 명시적으로 다루며 코드도 공개 — 신약 발굴 스크리닝 파이프라인에 즉시 적용 검토 가능

---

### C5. 바이오메디컬 파운데이션 모델 벤치마킹 (Benchmarking biomedical foundation models)

- 저자: Saez-Rodriguez J., Schäfer P.S.L., Kalavros N. 외 | 소속 미확인(주저자 소속 추정 불가)
- 소스: Nature Methods · 2026년 9월 (vol. 23, pp. 1724–1733)
- 상태: peer-reviewed
- DOI/링크: https://doi.org/10.1038/s41592-026-03182-y
- arXiv ID: 없음
- 코드: 미확인
- 사회적 신호: 없음
- 요약: 파운데이션 모델이 다양한 생물학 분야에서 급속히 확산되고 있으나 이를 엄밀하게 평가하는 방법이 아직 미성숙하다는 점을 지적하는 퍼스펙티브(Perspective) 논문이다. 현재 벤치마킹의 한계와 도전 과제를 정리하고, 단순한 환자 예후 예측을 넘어 파운데이션 모델을 평가할 때 요구되는 투명성·재현성·일반화 기준을 위한 지침을 제안한다.
- 핵심 수치: 정량 지표 없음(퍼스펙티브 논문)
- 분야 태그: [LLM-bio, 바이오인포]
- 선별 사유: 분야 전반의 파운데이션 모델 평가 방법론을 체계화한 Nature Methods Perspective — 현재 단일세포·유전체 파운데이션 모델 선택 기준 논의에 레퍼런스로 직접 활용 가능

---

## 와이드 논문 (Wide)

### W1. 단백질 서열·구조 공동 설계를 위한 단순 결합 모델 (SimpleDesign: A Joint Model for Protein Sequence and Structure Codesign)

- 저자: Jiarui Lu, Yuyang Wang, Yizhe Zhang, Jiatao Gu, Navdeep Jaitly, Joshua M. Susskind, Miguel Ángel Bautista | Apple Research
- 소스: arXiv · 2026-09 / Transactions on Machine Learning Research (TMLR) 게재
- 상태: peer-reviewed (TMLR)
- DOI/링크: https://arxiv.org/abs/2609.03377
- arXiv ID: arXiv:2609.03377
- 코드: 미확인
- 사회적 신호: 없음
- 요약: 단백질 기능이 서열과 3D 구조의 복잡한 상호작용에 의해 결정됨을 출발점으로, 기존 다단계(자동인코더 + 생성 모델) 학습 파이프라인 없이 데이터 공간에서 직접 엔드-투-엔드로 훈련하는 단일 단계 단백질 설계 모델을 제안한다. 서열에는 이산 교차 엔트로피 목적함수, 구조에는 회귀 목적함수를 결합한다.
- 분야 태그: [신약AI, 단백질]
- 선별 사유: 단백질 서열-구조 공동 설계를 단순한 단일 단계로 다룬다는 아이디어 — 기존 복잡한 파이프라인에 대한 방법론적 반론이자 Apple Research 발 단백질 설계 모델이라는 점에서 산업 동향으로도 주목

---

### W2. 약물 재창출에 응용된 결합 텐서-텐서 완성 방법 (Coupled Tensor-Tensor Completion Method with Applications in Drug Repurposing)

- 저자: Maryam Bagherian, Albert Hung, Ivo Dinov, Joshua Welch | University of Michigan
- 소스: arXiv · 2026-09-02
- 상태: preprint(미동료심사)
- DOI/링크: https://arxiv.org/abs/2609.03190
- arXiv ID: arXiv:2609.03190
- 코드: 미확인
- 사회적 신호: 없음
- 요약: 많은 바이오메디컬 문제를 텐서 완성(tensor completion)으로 정식화할 수 있으나, 기존 방법은 사이드 정보를 행렬 형태로만 수용한다. 이 논문은 사이드 정보 자체도 텐서로 표현하는 결합 텐서-텐서 완성(CTTC) 프레임워크를 제안하며, 거리 계량 학습과 군론(group theory)에 기반한 이론적 수렴 증명과 함께 약물 재창출에 적용 결과를 보인다.
- 분야 태그: [신약AI, 바이오인포]
- 선별 사유: 약물 재창출을 위한 다모달 텐서 수학 기반 방법론 — 이론적 근거가 명시된 드문 시도이며, 유전체·약물·표적 데이터 통합에 관심 있는 연구자에게 방법론적 선택지를 제공

---

### W3. 만성 신장 질환 조기 선별을 위한 LLM 활용 (LLM4CKD: Large Language Models for Early Stage Chronic Kidney Disease Screening)

- 저자: Muhammad Ashad Kabir, Sirajam Munira | 소속 미확인
- 소스: arXiv · 2026-09 / ICDM 2026 채택
- 상태: preprint(미동료심사, ICDM 2026 채택)
- DOI/링크: https://arxiv.org/abs/2609.04013
- arXiv ID: arXiv:2609.04013
- 코드: 미확인
- 사회적 신호: 없음
- 요약: LLM을 CKD(만성 신장 질환) 조기 선별에 제로샷(zero-shot)·퓨샷(few-shot) 인컨텍스트 학습으로 적용하는 프레임워크를 평가한다. 임상적으로 선별된 표 형식 특징과 구조화된 프롬프트 템플릿으로 태스크별 학습 없이 LLM 기반 추론을 수행하며, 적은 예시로도 전통적 접근법에 필적하거나 능가하는 성능을 저데이터 설정에서 달성한다고 주장한다.
- 분야 태그: [임상ML, LLM-bio]
- 선별 사유: LLM의 임상 표 데이터 적용을 EHR 기반 신장 질환 선별로 구체화한 사례 — 저자원 임상 환경에서의 LLM 활용 가능성을 묻는 임상ML 연구자들에게 참고 사례

---

## 수집 메모

### 제외 논문
- 특별히 제외된 DOI/ID: 없음
- 검색에서 발견되었으나 제외 이유: 2025년 9월 이전 게시 논문(arXiv 2509.* 시리즈 일부)은 2025년 9월 제출이므로 W36 대상 아님

### 중복 회피
recent-papers.jsonl 대조 결과 W36 신규 수집 논문과 기존 수록 논문 간 DOI·arXiv ID 중복 없음 확인. 기존 수록 논문(W31~W35) 목록은 파일에 명시됨.

### 소스별 검색 URL 및 결과
- arXiv cs.LG September 2026: https://arxiv.org/list/cs.LG/current (프록시 차단으로 직접 접근 불가 — 검색 엔진 우회)
- arXiv q-bio.GN September 2026: https://arxiv.org/list/q-bio.GN/2026-09 (프록시 차단으로 직접 접근 불가)
- bioRxiv bioinformatics collection: https://www.biorxiv.org/collection/bioinformatics (프록시 차단)
- HuggingFace Daily Papers: https://huggingface.co/papers (프록시 차단)
- 검색 엔진 쿼리로 수집:
  - "site:arxiv.org 2609 September 2026 bioinformatics genomics cancer single-cell drug"
  - "arxiv 2609 September 2026 cancer treatment prediction drug molecular design new paper"
  - "Creating bottom-up RNA transfer vehicles" Nature 2026
  - "Benchmarking biomedical foundation models" Nature Methods 2026
  - "ProbeMatchDTI" arxiv 2609
  - "SimpleDesign" protein codesign arxiv 2609
  - "Coupled Tensor-Tensor Completion" drug repurposing arxiv 2609
  - "LLM4CKD" chronic kidney disease arxiv 2609

### 참고사항
- C5 (Benchmarking biomedical foundation models, Nature Methods s41592-026-03182-y)는 검색 결과에서 "September 2026" 게재로 언급되었으나 정확한 온라인 게재일을 Nature Methods 직접 접근 불가로 확인하지 못함. 분석가 렌즈 작업 전 날짜 재확인 권장.
- arXiv 2609.* 논문들은 2026년 9월 1~6일 제출 확인.
- 프록시 차단으로 bioRxiv, arXiv, HuggingFace 직접 접근 불가 — 검색 엔진 스니펫 기반 수집이므로 초록 수치는 논문 본문에서 재확인 필요.
