---
type: raw
period: 2026-W40
date_collected: 2026-10-04
sources:
  arxiv: 8
  biorxiv: 0
  medrxiv: 0
  pubmed_journal: 0
  total: 8
---

# 2026-W40 수집 논문
수집일: 2026-10-04 / 대상 기간: 2026-09-28 ~ 2026-10-04

소스별 건수: arXiv 8편 (핵심 5 + 와이드 3)

> 수집 방법: GitHub DailyArXiv 트래커(junjianli106/DailyArXiv 이슈 #1059·#1064·#1066, spaceship/newDailyArxiv 이슈 #99·#100·#102) 및 웹 검색. arxiv.org/biorxiv.org/huggingface.co 직접 접근은 에이전트 프록시 차단으로 불가. 제목·ID는 GitHub 이슈 페이지 직접 추출 기준.

---

## 핵심 (Core)

### C1. 화학·단백질 언어 모델의 위계적 교차 어텐션을 통한 약물-표적 상호작용 예측 (Drug-Target Interaction Prediction via Hierarchical Sequential Cross-Attention over Chemical and Protein Language Models)

- **원제**: Drug-Target Interaction Prediction via Hierarchical Sequential Cross-Attention over Chemical and Protein Language Models
- **저자**: 저자·소속 미확인 (초록 기준 정보 없음 — 원문 직접 확인 필요)
- **출처**: arXiv · 2026-09-28 · **[preprint, 미동료심사]**
- **DOI/링크**: https://arxiv.org/abs/2609.34921
- **코드**: 미공개/미확인
- **초록 요약** (2~3줄, 한국어): 화학 언어 모델(SMILES 기반)과 단백질 언어 모델을 결합해 위계적 순차 교차 어텐션(hierarchical sequential cross-attention)으로 약물-표적 상호작용을 예측하는 방법을 제안한다. 분자 수준과 단백질 서열 수준에서 표현을 계층적으로 융합함으로써 DTI 예측 정확도를 높이는 것이 핵심 주장이다. 구체적 수치는 초록 직접 확인 필요.
- **선택 이유**: 화학 LM과 단백질 LM을 교차 어텐션으로 이어 붙인 신약 AI DTI 방법론. spaceship/newDailyArxiv W40 약물 분야 신착 최상위 목록 수록.
- **사회적 신호**: spaceship/newDailyArxiv 약물 분야 목록 수록 (순위 미확인); HF Daily Papers 확인 불가 (접근 차단)
- **검증 수준**: in silico
- **tags**: [신약AI, DTI, LLM-bio]

---

### C2. 진화 정보 기반 토크나이저로 효율적인 단백질 언어 모델 구축 — LEMON-ZEST (LEMON-ZEST: Evolution-Informed Tokenization for Efficient Protein Language Modeling)

- **원제**: LEMON-ZEST: Evolution-Informed Tokenization for Efficient Protein Language Modeling
- **저자**: Team-LEMON (저자 명단 미확인, 익명 제출 이력 있음)
- **출처**: arXiv · 2026-09-29 · **[preprint → NeurIPS 2026 accepted, 동료심사 완료]**
- **DOI/링크**: https://arxiv.org/abs/2609.37675
- **코드**: https://huggingface.co/Team-LEMON/lemon (HuggingFace 모델 허브)
- **초록 요약** (2~3줄, 한국어): ZEST(Zoned Encoding of Sequence Traits) 토크나이저를 도입해 생화학적으로 치환 가능한 아미노산 n-gram 클러스터를 기반으로 32K 어휘를 구축했다. LEMON 모델은 24-레이어 트랜스포머(768-d, 헤드 12개, 총 203.72M 파라미터)로, 이 토크나이저를 통해 단백질 패밀리·폴드 유사도 검색 성능을 높이는 것을 목표로 한다. 구체적 벤치마크 수치는 원문 확인 필요.
- **선택 이유**: 단백질 언어 모델의 토크나이징 방식을 진화적 보존 정보로 개선한 NeurIPS 2026 채택 논문. HuggingFace에 모델 공개로 재현 가능성 높음.
- **사회적 신호**: NeurIPS 2026 채택; HuggingFace 모델 공개 확인
- **검증 수준**: in silico
- **tags**: [단백질, LLM-bio, 방법론]

---

### C3. 단백질 지향 진화를 위한 구조 인식 강화학습 (Structure-aware Reinforcement Learning for Protein Directed Evolution)

- **원제**: Structure-aware Reinforcement Learning for Protein Directed Evolution
- **저자**: 저자·소속 미확인 (초록 기준 정보 없음 — 원문 직접 확인 필요)
- **출처**: arXiv · 2026-09-30 · **[preprint, 미동료심사]**
- **DOI/링크**: https://arxiv.org/abs/2609.39048
- **코드**: 미공개/미확인
- **초록 요약** (2~3줄, 한국어): 단백질 지향 진화(directed evolution)에 강화학습을 적용하되 단백질 3차 구조 정보를 함께 인코딩하는 구조 인식 RL 프레임워크를 제안한다. 서열 공간 탐색에서 구조적 제약을 반영함으로써 기능 향상 돌연변이를 더 효율적으로 탐색하는 것이 핵심 주장이다. 구체적 수치는 원문 직접 확인 필요.
- **선택 이유**: RL 기반 단백질 공학에 구조 정보를 접목한 신규 방법론. 신약 타깃용 단백질 최적화에 직접 연결.
- **사회적 신호**: spaceship/newDailyArxiv 단백질 분야 신착 목록 수록; HF Daily Papers 확인 불가
- **검증 수준**: in silico
- **tags**: [신약AI, 단백질, 방법론]

---

### C4. 형태-공간 거시 상태와 저-계수 분자 프로그램을 통한 조직병리에서 유전자 발현 예측 — MoSPR (MoSPR: Histology-to-Gene Expression Prediction with Morpho-Spatial Macrostates and Low-Rank Molecular Programs)

- **원제**: MoSPR: Histology-to-Gene Expression Prediction with Morpho-Spatial Macrostates and Low-Rank Molecular Programs
- **저자**: 저자·소속 미확인 (원문 직접 확인 필요)
- **출처**: arXiv · 2026-09-28 · **[preprint, 미동료심사]**
- **DOI/링크**: https://arxiv.org/abs/2609.34280
- **코드**: 미공개/미확인
- **초록 요약** (2~3줄, 한국어): H&E 염색 조직 이미지(histology)에서 공간 전사체(spatial transcriptomics) 유전자 발현을 예측하는 MoSPR 모델을 제안한다. 형태-공간 거시 상태(morpho-spatial macrostates)를 추출하고 저-계수 분자 프로그램(low-rank molecular programs)으로 전사 패턴을 압축해 예측하는 구조다. 상세 수치는 원문 직접 확인 필요.
- **선택 이유**: 값비싼 공간 전사체 실험 없이 H&E 이미지만으로 유전자 발현을 추론하는 접근. 유전체·바이오인포 연구에 직접 활용 가능성 있음.
- **사회적 신호**: junjianli106/DailyArXiv 이슈 #1059 수록; HF Daily Papers 확인 불가
- **검증 수준**: in silico
- **tags**: [바이오인포, 공간전사체, LLM-bio]

---

### C5. 전자 건강 기록에서 연속적 환자 궤적 학습 — EHRFlow (Learning Continuous Patient Trajectories from Electronic Health Records)

- **원제**: Learning Continuous Patient Trajectories from Electronic Health Records
- **저자**: 저자·소속 미확인 (ML4H 2026 제출본; 원문 직접 확인 필요)
- **출처**: arXiv · 2026-09-28 · **[preprint, 미동료심사; ML4H 2026 Proceedings Track 제출]**
- **DOI/링크**: https://arxiv.org/abs/2609.36144
- **코드**: 미공개/미확인
- **초록 요약** (2~3줄, 한국어): EHRFlow는 다중-마진 플로우 매칭(multi-marginal flow matching) 프레임워크로, 인코딩된 환자 과거 기록을 조건으로 미래 임상 궤적 역학을 모델링한다. 불규칙 관측 시간을 처리하고 임의 시점에서 예측을 지원하며, 100만 명 이상 환자 실제 임상 데이터셋에서 임상 코드 예측과 잠재 상태 복원 성능을 개선했다고 주장한다. 구체적 수치는 원문 직접 확인 필요.
- **선택 이유**: EHR 기반 임상 ML에서 연속 시계열 모델링에 플로우 매칭을 처음 도입한 것으로 보이며, ML4H 2026 제출로 임상 커뮤니티에서 검토 중.
- **사회적 신호**: ML4H 2026 Proceedings Track 제출 확인; HF Daily Papers 확인 불가
- **검증 수준**: 후향적 (실제 임상 데이터, 규모 100만 명+ 환자)
- **tags**: [임상ML, LLM-bio]

---

## 와이드 (Wide)

### W1. CAGenMol-2: 마스크드 분자 추론으로 재정의한 약물 설계 (One Sequence, Many Decodings: CAGenMol-2 Recasts Drug Design as Masked Molecular Inference)

- **원제**: One Sequence, Many Decodings: CAGenMol-2 Recasts Drug Design as Masked Molecular Inference
- **저자**: 저자·소속 미확인 (원문 직접 확인 필요)
- **출처**: arXiv · 2026-09-28 · **[preprint, 미동료심사]**
- **DOI/링크**: https://arxiv.org/abs/2609.34301
- **코드**: 미공개/미확인
- **초록 요약** (2~3줄, 한국어): 하나의 분자 서열로부터 다양한 유효 분자를 생성하는 마스크드 분자 추론(masked molecular inference) 패러다임을 제안한다. 약물 설계 문제를 조건부 마스크 언마스킹 과정으로 재정의해 구조·성질 동시 최적화를 노린다.
- **선택 이유**: 분자 생성의 새로운 추론 패러다임; 핵심 축(신약AI)에 근접하나 다른 접근법 다양성 확보를 위해 와이드에 배치.
- **사회적 신호**: spaceship/newDailyArxiv 약물 분야 W40 목록 수록

---

### W2. 전체 슬라이드 이미지를 동적 종양 미세환경 장(場)으로 모델링 (Modeling Whole-Slide Images as Dynamic Tumor Microenvironment Fields)

- **원제**: Modeling Whole-Slide Images as Dynamic Tumor Microenvironment Fields
- **저자**: 저자·소속 미확인 (원문 직접 확인 필요)
- **출처**: arXiv · 2026-09-28 · **[preprint → NeurIPS 2026 accepted, 동료심사 완료]**
- **DOI/링크**: https://arxiv.org/abs/2609.34451
- **코드**: 미공개/미확인
- **초록 요약** (2~3줄, 한국어): 병리 전체 슬라이드 이미지(WSI)를 연속적 장(field)으로 모델링해 종양 미세환경(TME)의 공간적 역학을 포착하는 새로운 프레임워크를 제안한다. NeurIPS 2026 채택. 구체적 방법과 수치는 원문 직접 확인 필요.
- **선택 이유**: 종양 미세환경 분석은 신약 타깃 발굴과 면역항암제 연구에 직결. 와이드 선택; 임상 병리 영역에서 이 주 가장 주목받은 논문 중 하나.
- **사회적 신호**: NeurIPS 2026 채택

---

### W3. AI 보조 유사분열상 계수로 복수 종양 유형에서 재현성·효율 향상 (AI-assisted mitotic counting improves reproducibility and efficiency across multiple tumour types)

- **원제**: AI-assisted mitotic counting improves reproducibility and efficiency across multiple tumour types
- **저자**: 저자·소속 미확인 (원문 직접 확인 필요)
- **출처**: arXiv · 2026-10-02 · **[preprint, 미동료심사]**
- **DOI/링크**: https://arxiv.org/abs/2610.01813
- **코드**: 미공개/미확인
- **초록 요약** (2~3줄, 한국어): 다양한 종양 유형에 걸쳐 AI를 활용한 유사분열상(mitotic figure) 계수의 재현성과 효율을 병리의사와 비교 평가한 연구다. 임상 병리 워크플로우에서 AI 보조 계수의 실용성과 한계를 조사하는 것이 핵심 주장이다.
- **선택 이유**: 병리 AI의 실용화 사례. 와이드 선택; 이번 주 임상 AI 분야에서 화제 논문.
- **사회적 신호**: junjianli106/DailyArXiv 이슈 #1066 수록
