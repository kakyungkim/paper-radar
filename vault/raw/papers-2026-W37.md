---
type: raw-papers
period: 2026-W37
scout-date: 2026-09-13
sources-count:
  arXiv: 5
  bioRxiv: 2
  Nature: 1
  total: 8
---

> 수집일: 2026-09-13 | 기간: 2026-09-07~2026-09-13 (W37)
> 핵심 5편 · 와이드 3편 | arXiv(q-bio/cs.LG/cs.CV) 5건, bioRxiv 2건, Nature 1건
> 중복 제외 기준: vault/_meta/recent-papers.jsonl W31~W36 레코드 전체 (doi·arXiv ID 대조)

---

## 핵심 논문 (Core)

### C1. 교란 프로테오믹스 기반 운용 가능한 가상세포 모델 (An operational perturbation proteomics-based virtual cell model)

- 저자/소속: Rui Sun (제1저자), Liujia Qian, Yongge Li 외 다수 | Westlake University / Westlake Omics Inc. / DP Technology Co., Ltd.
- 출처: Nature · 2026년 9월 · **peer-reviewed**
- DOI/링크: https://doi.org/10.1038/s41586-026-11001-9
- 코드/데이터: 미확인 (Westlake 연구팀 관련 공개 리포지터리 존재 확인; 본 논문 전용 링크 미확인)
- 한 줄 요지: 유방암 세포주를 63종 FDA 승인 항암제 및 59종 2제 병용으로 교란하며 측정한 3,800만 건의 시간별 단백질 발현량 데이터를 신경 상미분방정식(Neural ODE) 기반 파운데이션 모델(ProteinTalks)로 학습해, 약물 효능·시너지 예측, 신규 병용 발굴, 약물 내성 관련 단백질 탐색 작업에 운용 가능한 가상세포 모델을 구축했다고 주장한다.
- 핵심 수치: 3,800만 건 시간별 단백질 측정값, 63종 FDA 승인 항암제, 59종 2제 병용, 측정 시점 = 투여 전·6h·24h·48h (Nature 논문 본문 및 Nature 뉴스 기준)
- 분야 태그: 신약AI / 단백질 / 멀티오믹스
- 사회적 신호: Nature 뉴스 피처 게재 (doi:10.1038/d41586-026-02845-2); MedicalXpress 보도 (2026-09)
- 선별 사유: 대규모 동적 프로테오믹스로 학습한 가상세포 모델을 Nature에 발표한 peer-reviewed 논문으로, 신약 개발 AI에 직접적인 방법론 함의를 지님

---

### C2. PROTAC 분해 활성의 E3 리가제 간 소수샷 예측 (ProMeta: Few-shot PROTAC-targeted degradation prediction across E3 ligases)

- 저자/소속: Yuansheng Liu (제1저자), Yufei Ye, Tao Tang, Jiawei Luo, Wen Tao, Xiao Luo | 소속 미확인 (초록 기준)
- 출처: arXiv · 2026-09-09 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.09891
- 코드/데이터: 공개 예정 또는 공개됨 (GitHub 링크 미확인 — 초록에 가용성 명시 여부 미확인)
- 한 줄 요지: PROTACs(단백질 분해 유도 키메라)의 분해 활성 예측이 특정 E3 리가제(CRBN, VHL 등)에 집중된 데이터 편향으로 인해 일반화에 실패하는 문제를, 분자 그래프 인코딩과 표적 단백질·E3 리가제 서열 임베딩을 결합한 프로토타입 기반 그래프 신경망(ProMeta)을 에피소딕 메타러닝으로 훈련해 해결했다고 주장한다.
- 핵심 수치: 소수샷(few-shot) 조건 및 교차-리가제 일반화 정량 지표는 초록에 구체적 수치 미명시 — 논문 본문 확인 필요
- 분야 태그: 신약AI / 단백질
- 사회적 신호: 없음
- 선별 사유: 타깃 분해(Targeted Protein Degradation) 분야에서 '언드러거블' 표적으로 설계 공간을 확장하는 계산 도구로, 메타러닝 기반 교차-E3 일반화 방법론이 신규임

---

### C3. CRISPR 스크린에서 생물학-인-더-루프 방식의 상각화된 히트 발굴 (Biology-in-the-loop: Amortized Adaptive Hit Discovery in CRISPR Screens)

- 저자/소속: Carl Edwards (제1저자), Edward De Brouwer, Xiner Li, Namkyeong Lee, Ehsan Hajiramezanali, Anne Biton, Sara Mostafavi, Gabriele Scalia (교신) | Genentech 및 공동 기관
- 출처: arXiv · 2026-09-10 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.11877
- 코드/데이터: https://github.com/Genentech/AssayBench
- 한 줄 요지: 1,389개 공개 CRISPR 스크린을 5개 표현형 카테고리로 구성한 대규모 벤치마크(AssayBench-Loop)를 구축하고, 과거 스크린으로 사전학습된 트랜스포머 기반 상각 획득 정책(AssayFormer)과 LLM 파생 생물학 사전(prior)을 결합한 순차적 실험 설계 프레임워크(AssayLoop)가 기존 적응형 설계 방법 및 단독 LLM보다 CRISPR 히트 발굴 효율을 높인다고 주장한다.
- 핵심 수치: 후보 라이브러리의 5% 스크리닝 후 히트의 27.7% 회수; 랜덤 선택 대비 5.67배 enrichment (초록 기준)
- 분야 태그: 바이오인포 / 유전체 / 신약AI
- 사회적 신호: 없음
- 선별 사유: 실험 예산 제약 하의 CRISPR 스크린 설계를 자동화하는 방법으로, 기능 유전체학과 신약 타깃 발굴 사이의 실용적 연결고리를 제공함

---

### C4. 관상동맥 조영술 해석을 위한 공간 근거 기반 감사 가능 추론 (CARDEA: Auditable Reasoning Grounded in Spatial Evidence for End-to-End Coronary Angiography Interpretation)

- 저자/소속: Jia-Jen Lee (제1저자), Shih-Yen Hou, Kee Koon Ng, Wei-Chun Wang, Shih-Sheng Chang (교신) | 소속 미확인 (초록 기준)
- 출처: arXiv · 2026-09-07 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.06931
- 코드/데이터: 모델 가중치 및 추론 코드 공개 (HuggingFace 페이지: https://huggingface.co/papers/2609.06931; GitHub 링크 미확인)
- 한 줄 요지: 관상동맥 조영술(CAG) 해석의 관찰자 간 변동성 문제를 해결하기 위해, 공개 데이터셋으로만 훈련한 대형 시각-언어 모델(CARDEA)을 시각 정렬 → 자기-증류 Chain-of-Box(CoB) 콜드스타트 → 검증 가능 보상 기반 강화학습(RLVR) 3단계로 학습해, 원시 다시점 CAG 영상에서 키프레임 선택 및 연구 수준 진단까지 감사 가능한 공간 근거를 제공하는 end-to-end 파이프라인을 구축했다고 주장한다.
- 핵심 수치: 2개 연구 수준 진단 과제(우관동맥 우세도 분류, 복잡도 평가) 평가; 검증 데이터셋 규모·성능 수치 초록에 미명시 — 논문 본문 확인 필요
- 분야 태그: 임상ML / 의료영상
- 사회적 신호: HuggingFace Daily Papers 등재 (2026-W37 내)
- 선별 사유: 심장내과 영역의 AI 진단 신뢰성 문제를 RLVR + 공간 근거 노출로 다룬 점이 임상 채택 가능성 측면에서 주목할 만함

---

### C5. 표현형 변화와 연관된 유전자 조절 네트워크 변화 탐지 (CIDER: detecting changes in gene regulatory networks that are associated with changes in phenotype)

- 저자/소속: Wooseok J Jung (제1저자), Mingyue Ding, Shu Liao, Zolboo Erdenebaatar, Michael Brent (교신) | Washington University in St. Louis 추정 (Brent 연구팀 기준; 소속 직접 확인 필요)
- 출처: bioRxiv · 2026-09-08 · **preprint(미동료심사)**
- DOI/링크: https://doi.org/10.64898/2026.09.08.750185
- 코드/데이터: 미확인
- 한 줄 요지: 두 생물학적 조건(예: 질환 대 정상) 사이에서 유전자 조절 네트워크(GRN)의 어떤 연결이 달라지는지를 탐지하는 CIDER 방법을 제안하고, 이 변화가 표현형 전환과 연관됨을 보였다고 주장한다.
- 핵심 수치: 구체적 수치 미확인 — 초록 상세 내용 직접 확인 필요
- 분야 태그: 바이오인포 / 유전체
- 사회적 신호: 없음
- 선별 사유: GRN 추론 도구가 다수 존재하지만 조건 간 GRN 변화(차등 GRN)를 직접 탐지하는 방법은 상대적으로 부족하며, 질환 메커니즘 이해에 실용적 함의를 가짐

---

## 와이드 논문 (Wide)

> 그 주 화제가 된 핵심 축 밖(또는 주변부) 논문 — 가볍게 한 눈에

---

### W1. 드 노보 신약 설계를 위한 분자 생성 모델 체계적 평가 (A Systematic Evaluation of Molecule Generation Models for De Novo Drug Design: From Benchmarks to Practical Insights)

- 저자/소속: Xinrui Xu, Xueer Wang, Dan Luo, Sisu Yuan, Xuan Lin | 소속 미확인
- 출처: arXiv · 2026-09-09 · **peer-reviewed** (Journal of Chemical Information and Modeling 게재 확정)
- DOI/링크: https://arxiv.org/abs/2609.10099
- 코드/데이터: 공개 안 됨 (리뷰/서베이 논문)
- 한 줄 요지: 분자 생성 모델 82종을 RNN·트랜스포머·VAE·GAN·플로우·확산(diffusion) 5개 프레임워크로 분류하고 표준 벤치마크 및 평가 지표 기준으로 체계적으로 비교 분석한 서베이다.
- 핵심 수치: 82개 방법, 5개 생성 프레임워크 분류 (초록 기준)
- 분야 태그: 신약AI / 분자생성
- 사회적 신호: 없음
- 선별 사유: 분자 생성 분야의 현 주소를 가장 넓게 조감할 수 있는 최신 실용 지도로, 분야 진입 연구자 및 방법 선택 시 기준선으로 활용 가능

---

### W2. 이질성과 동질성을 계층적으로 통합한 통합 의료 영상 복원 모델 (UniH³: Unifying Hierarchical Homogeneity and Heterogeneity for All-in-One Medical Image Restoration)

- 저자/소속: Zhiwen Yang (제1저자), Jiayin Li, Chengyu Liu, Hui Zhang, Bingzheng Wei, Yan Xu (교신) | Beihang University (북항항공항천대), Tsinghua University
- 출처: arXiv · 2026-09-10 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.11156
- 코드/데이터: GitHub 리포지터리 Yaziwel/UniH3; 데이터셋 HuggingFace 공개 예정 (GitHub Issue #1 기준)
- 한 줄 요지: 의료 영상 복원에서 과제 간 이질성(heterogeneity)과 과제 내 동질성(homogeneity)을 계층적으로 모두 활용하는 통합 모델(UniH³)을 제안해 모달리티·열화 유형에 무관하게 단일 모델로 SOTA를 달성했다고 주장한다.
- 핵심 수치: MedIR-2D-500K 및 MedIR-3D-3K 2개 대규모 벤치마크에서 all-in-one 및 단일 과제 복원 SOTA (초록 기준; 구체적 지표 초록에 미명시)
- 분야 태그: 임상ML / 의료영상
- 사회적 신호: HuggingFace Daily Papers 등재 (2026-W37 내)
- 선별 사유: 단일 모델로 MRI·CT·내시경 등 다양한 의료 영상 복원을 커버하는 실용 인프라로, 임상 데이터 전처리 파이프라인에 직접 활용 가능성이 있음

---

### W3. 두경부 편평세포암 내 순환 단핵구 동력학의 단일세포 프로테오믹스 매핑 (Single-cell proteomics maps circulating monocyte dynamics in advanced head and neck squamous cell carcinoma)

- 저자/소속: Prado HM de A. (제1저자), Miyamoto JG, Busso-Lopes AF, Coimbra NAR, de Figueiredo D, Domingues RR, Pauletti BA, Mores AL, Medina TS, Ramos RN, Brandao TB, Prado-Ribeiro AC, Kowalski LP, Paes Leme A (교신) | 브라질 국립암연구소 및 공동 기관
- 출처: bioRxiv · 2026-09-10 · **preprint(미동료심사)**
- DOI/링크: https://doi.org/10.64898/2026.09.09.750366
- 코드/데이터: 미확인
- 한 줄 요지: 진행성 두경부 편평세포암(HNSCC) 환자에서 순환 단핵구의 프로테옴을 단일세포 수준으로 측정해, 종양 미세환경과 단핵구 서브타입 간의 동적 연관성을 제시한다고 주장한다.
- 핵심 수치: 미확인 (초록 구체적 수치 직접 확인 필요)
- 분야 태그: 임상ML / 바이오마커 / 단일세포
- 사회적 신호: 없음
- 선별 사유: 액체 생검(liquid biopsy) 대안으로서 순환 면역세포의 단일세포 프로테오믹스를 임상 암 연구에 적용한 사례로, 비침습적 바이오마커 발굴 방향과 맞닿아 있음
