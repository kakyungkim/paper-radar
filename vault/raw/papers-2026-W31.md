---
week: 2026-W31
date_range: 2026-07-27 ~ 2026-08-02
created: 2026-08-02
scout: paper-scout
---

# 2026-W31 수집 논문

수집일: 2026-08-02 | 주차: 2026-W31 (2026-07-27 ~ 2026-08-02)

| 소스 | 핵심 | 와이드 | 합계 |
|------|------|--------|------|
| arXiv (q-bio / cs.LG / cs.AI) | 4 | 3 | 7 |
| bioRxiv | 1 | 0 | 1 |
| **합계** | **5** | **3** | **8** |

중복 제외 확인: W26~W30 arXiv ID 및 DOI 목록 대조 완료. 제외 목록: arXiv:2607.17227, 2607.17601, 2607.18144, 2607.20582, 2607.21453, 2607.21561 및 DOI:10.64898/2026.07.23.739930 (W30 수록 논문 전체).

---

## 핵심 (Core 5)

### 1. CENO: 진화적 서열 해석과 프로그래밍 가능한 조절 서열 설계를 위한 게놈 스케일 세계 모델 (CENO: A Genome-Scale World Model for Evolutionary Sequence Interpretation and Programmable Regulatory Design)

- **arXiv/DOI**: DOI:10.64898/2026.07.28.741284
- **원문 URL**: https://www.biorxiv.org/content/10.64898/2026.07.28.741284
- **저자**: Mingqian Ma, Yucheng Wu, Xin Chen, Feifei Jiang, Peijun Lin, Dongxin Ye, Yidi Sun, Yijing Zhang, Tianqiong Shi, Yu Zhao, Wanli Ouyang, Bowen Zhou, Lei Bai, Yuchen Ren (교신: Yuchen Ren) | Shanghai Artificial Intelligence Laboratory
- **출처**: bioRxiv · 2026-07-28 게재 · **preprint(미동료심사)**
- **분야 태그**: 유전체 / LLM-bio
- **선택 이유**: Mamba·Attention·MoE를 결합한 하이브리드 아키텍처에 다중 종(multi-species) MSA 후처리를 더해, 긴 DNA 서열 이해·변이 효과 점수(VEP)·조절 서열 신규 설계를 단일 자기회귀 모델로 수행하는 게놈 스케일 세계 모델을 제안한다. 코드·모델이 완전 공개(오픈소스)된 점이 재현 가능성 측면에서 즉각 활용 가능하다.
- **사회적 신호**: 없음
- **핵심 요약**: CENO는 Mamba/Attention/MoE 하이브리드 백본을 기반으로, 다중 종 정렬(MSA) 사후 훈련(post-training)을 통해 긴 DNA 서열을 통합적으로 이해하는 게놈 스케일 자기회귀 모델이다. 하나의 통합 모델로 (1) 긴 DNA 맥락 이해, (2) 변이 효과 점수(Variant Effect Prediction, VEP) 계산, (3) 새로운 조절 서열(regulatory sequence) 생성 세 가지 다운스트림 태스크를 수행한다. GitHub(CladeTeam/CENO)를 통해 HuggingFace trust_remote_code 지원 패키지, TraitGym 예시를 포함한 VEP 파이프라인, vLLM 오프라인 추론 데모를 공개한다. 초록 기준 구체적 성능 수치는 확인되지 않아 "미명시"로 기재한다.
- **코드/데이터**: https://github.com/CladeTeam/CENO (오픈소스 공개)
- **검증 수준**: in silico

---

### 2. Vilya-2: 화학적으로 다양한 분자 계면의 정확한 구조 모델링 (Accurate structural modeling of chemically diverse molecular interfaces with Vilya-2)

- **arXiv/DOI**: arXiv:2607.25156
- **원문 URL**: https://arxiv.org/abs/2607.25156
- **저자**: Pascal Sturmfels, Naozumi Hiranuma, Milad Salem, Benjamin D. Sellers, Stephen Rettie, CJ San Felipe, Chase A. P. Wood, Jeffrey K. Holden, Adam P. Moyer, Patrick J. Salveson, Ivan Anishchanka | Vilya Research
- **출처**: arXiv · 2026-07-28 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / 단백질
- **선택 이유**: 비정규 잔기·거대고리화(macrocyclization)·복잡한 위상을 가진 펩타이드 치료제를 표적 단백질과의 계면 수준까지 전원자(all-atom) 표현으로 정확히 모델링하는 확산 트랜스포머를 제안하며, 펩타이드 모달리티의 구조 예측 한계를 처음 체계적으로 극복한 모델이다. 59.1% sub-2Å 회복률이라는 정량적 성과와 공개 벤치마크(Riptides)가 즉각 활용 가능하다.
- **사회적 신호**: 없음 (Vilya Research, C&EN 기사 내 언급)
- **핵심 요약**: 공진화 통계(co-evolutionary statistics) 기반 구조 예측 네트워크는 단백질에서는 성과를 거뒀지만 비정규 잔기·거대고리화·복잡한 위상을 특징으로 하는 펩타이드 치료제에서는 정확도가 확장되지 않는다. Vilya-2는 Vilya-1의 전원자 표현을 개별 분자 모델링에서 단백질 표적과의 상호작용 모델링으로 확장한 확산 트랜스포머(diffusion transformer)다. 초록 기준 — 펩타이드 계면의 59.1%를 backbone RMSD 2Å 미만으로 회복하며, 결합 수용체를 템플릿으로 제공해도 대표적 공동-폴딩(co-folding) 모델의 성능을 크게 상회한다. 소형 분자 도킹에서도 최고 수준이며, 훈련 시 보지 못한 분자보다 수 배 큰 거대고리 및 이황화 결합 스테이플 미니단백질(disulfide-stapled miniprotein)까지 일반화된다.
- **코드/데이터**: Riptides 벤치마크 공개: https://github.com/VilyaPublic/Riptides (모델 추론 코드 미확인)
- **검증 수준**: in silico (Riptides 벤치마크 및 내부 데이터셋 기준)

---

### 3. PMRD: 세포 반응에서 약리학적 도메인으로 — 다중모달 제로샷 약물 표현 학습 (From Cellular Responses to Pharmacological Domains: Multimodal Zero-Shot Drug Representation Learning)

- **arXiv/DOI**: arXiv:2607.25322
- **원문 URL**: https://arxiv.org/abs/2607.25322
- **저자**: Jintao Huang, Lu Leng, Ziyuan Yang | 소속 기관 미확인
- **출처**: arXiv · 2026-07-28 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / LLM-bio
- **선택 이유**: 화학 구조 너머로 유전자 발현(gene expression)·세포 형태(cell morphology) 등 세포 반응 모달리티를 통합해 제로샷 약물 특성을 예측하는 PMRD 프레임워크를 제안하며, 기존 직접 융합·인스턴스 수준 대조 정렬이 기전 신호와 모달리티 노이즈를 혼동하는 문제를 도메인 분리로 해결한다. KDD 2026에 채택된 연구다.
- **사회적 신호**: KDD 2026 (ACM SIGKDD, 8월 9~13일) 발표 채택
- **핵심 요약**: 직접 융합이나 인스턴스 수준 대조 정렬(contrastive alignment)은 기전 관련 신호를 모달리티별 노이즈와 분리하지 못해, 구조적으로 다르지만 생물학적으로 유사한 화합물을 잘못 분리할 수 있다. PMRD(Pharmacological Response Domain-guided framework)는 화학 구조·유전자 발현·세포 형태 세 가지 모달리티에 걸쳐 메커니즘 일치 인자(mechanism-consistent factors)를 모달리티별 정보와 분리하고 합의 반응 도메인(consensus response domain)을 구축한다. 메커니즘 후보 증강(mechanism candidate augmentation)이 국소적으로 안정적인 인자를 식별하고, 검색-기하 귀인(retrieval-geometry attribution)이 정렬·증강 목표의 업데이트 가중치를 동적으로 조정한다. 공개 데이터셋 실험에서 개선된 제로샷 특성 예측 성능 및 생물학적으로 더 일관된 약물 이웃 구조를 달성했다(초록 기준; 구체 수치 미명시).
- **코드/데이터**: 미확인
- **검증 수준**: in silico (공개 약물 특성 예측 벤치마크)

---

### 4. SCTA: 단일세포 RNA 시퀀싱에서 안정적이고 해석 가능한 표적 유전자 발굴을 위한 에이전트 프레임워크 (SCTA: An Agentic Framework for Stable and Interpretable Target Gene Discovery from Single-Cell RNA Sequencing)

- **arXiv/DOI**: arXiv:2607.23821
- **원문 URL**: https://arxiv.org/abs/2607.23821
- **저자**: Shuyu Chen, Chen Zhu, Ye Zhang, Yang Li, Qiqi Xie, Haohan Wang | 소속 기관 미확인 (BioKDD 2026 워크숍 채택)
- **출처**: arXiv · 2026-07-26 제출 · **preprint(미동료심사)** (BioKDD 2026 워크숍 채택)
- **분야 태그**: 유전체 / 신약AI
- **선택 이유**: scRNA-seq 표적 발굴이 전처리·세포집단 선택·차등 발현 분석 등 분석 선택에 고도로 민감한 문제를 에이전트 구조로 최초로 명시적 해결한 연구다. "단일 실행 타당성"이 아닌 "교차 실행 안정성"을 평가 기준으로 전환한 방법론적 시도가 신규하다.
- **사회적 신호**: BioKDD 2026 (ACM SIGKDD 워크숍) 채택
- **핵심 요약**: scRNA-seq는 이질적인 세포 상태와 희귀 하위집단을 포착하지만 이 이질성이 표적 발굴을 분석 선택에 크게 좌우되게 만들어 재현성이 낮다. SCTA(Single-Cell Target Agent)는 단일 범용 추론이 아닌, 파이프라인 핵심 결정점에 전문화된 에이전트를 배치(cell-type triage·candidate filtering·evidence aggregation)하고 후속 추론을 구조화된 생물학적 증거로 제약하는 의사결정 중심 다중 에이전트 프레임워크다. 표적 우선순위를 교차 실행 안정성으로 평가함으로써 재현 가능한 표적 발굴이 가능해진다. 유전성 만성 췌장염(hereditary chronic pancreatitis) 절제 연구에서 전체 증거 통합 시 독립 실행 간 가장 안정적인 표적 선택을 달성하면서도 선행 연구에서 검증된 생물학적으로 일관성 있는 기전을 회복했다(초록 기준; 표본 수 미명시).
- **코드/데이터**: 미확인
- **검증 수준**: in silico (scRNA-seq 공개 데이터셋, 워크숍 논문 수준)

---

### 5. 다중모달 입력을 갖춘 자기회귀 EHR 파운데이션 모델 (Autoregressive EHR Foundation Models with Multimodal Inputs)

- **arXiv/DOI**: arXiv:2607.22264
- **원문 URL**: https://arxiv.org/abs/2607.22264
- **저자**: Yuxuan Liu, Joshua Placidi, Jinpei Han, Alfred John Balston, Marek Rei, A. Aldo Faisal | Imperial College London
- **출처**: arXiv · 2026-07-24 제출 · **preprint(미동료심사)** (ICML 2026 Structured Data for Health 워크숍 발표)
- **분야 태그**: 임상ML
- **선택 이유**: 구조화 EHR 이벤트 코드만 다루던 자기회귀 EHR 파운데이션 모델에 ECG 파형·흉부 X선·임상 노트 등 실제 임상 데이터를 시간 정렬(temporal alignment) 방식으로 통합하는 최초 체계적 비교 연구다. MIMIC-IV 기준 제로샷 임상 예측으로 검증한 점이 실용적이다.
- **사회적 신호**: ICML 2026 Structured Data for Health 워크숍 발표
- **핵심 요약**: 자기회귀 EHR 파운데이션 모델은 토크나이즈된 전자건강기록(Electronic Health Record, EHR)으로 훈련해 제로샷 임상 예측을 지원할 수 있으나, 대부분 구조화 이벤트 코드만 사용하고 다중 모달리티를 원칙적으로 통합하지 못한다. 저자들은 ECG 파형·흉부 X선·임상 노트를 모달리티별 잠재 압축(latent compression) 및 게이트 교차 어텐션(gated cross-attention)으로 시간 정렬해 조건화하는 프레임워크를 제안한다. 두 가지 핵심 설계 선택지 — (1) 긴 모달리티별 시퀀스의 압축 방법, (2) 각 모달리티의 사전 훈련 인코더 선택 — 를 체계적으로 분석한다. MIMIC-IV 데이터셋 제어 절제 실험(controlled ablation)에서 최적 잠재 압축 구성이 비압축 교차 어텐션과 평균 풀링 모두를 상회하는 성능을 보인다(초록 기준; 구체 AUC/AUROC 수치 미명시).
- **코드/데이터**: 미확인
- **검증 수준**: 후향 (MIMIC-IV 임상 데이터베이스)

---

## 와이드 (Wide 3편)

### W1. Q-Steer: 분자 정책 최적화를 위한 행동-가치 유도 (Q-Steer: Action-Value Guidance for Molecular Policy Optimization)

- **arXiv/DOI**: arXiv:2607.26391
- **원문 URL**: https://arxiv.org/abs/2607.26391
- **저자**: Xinyu Wang, Jinbo Bi (University of Connecticut); Minghu Song (Institute of Health and Medicine, Hefei Comprehensive National Science Center)
- **출처**: arXiv · 2026-07-29 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / 분자생성
- **선택 이유**: 분자 언어 모델(LM)이 SMILES 토큰을 생성하는 과정에서 어떤 중간 토큰이 좋은 분자를 만들었는지 알 수 없는 지연 피드백(delayed-feedback) 병목을 오프라인 Q-함수로 롤아웃 시점에 직접 해결하는 방법론이 새롭다.
- **사회적 신호**: 없음
- **핵심 요약**: SMILES 기반 분자 최적화는 완성된 분자에만 보상이 주어져 중간 토큰 기여를 알 수 없는 구조적 근시안성(myopia)이 있다. Q-Steer는 오프라인 훈련된 고정 접두어-행동 가치 채점기(PAVS-Q)로 부분 SMILES 접두어 아래 다음 토큰의 하류 보상을 추정하고, 정규화된 가치 보너스를 샘플링 로짓에 더하는 롤아웃-시점 조향(rollout-time steering) 방식을 취한다. 추가 파인튜닝 없이 기존 분자 LM에 래핑해 사용 가능하다.
- **코드/데이터**: 미확인
- **검증 수준**: in silico

---

### W2. 딥 표현 학습은 언제 단일세포 클러스터링에 도움이 되는가? 감도 인식 진단 벤치마크 (When Does Deep Representation Learning Help Single-Cell Clustering? A Sensitivity-Aware Diagnostic Benchmark for Biomedical AI Pipelines)

- **arXiv/DOI**: arXiv:2607.25288
- **원문 URL**: https://arxiv.org/abs/2607.25288
- **저자**: Nguyen Thanh Phong, Truong Viet Vu, Nguyen Ha Thu, Tran An Ky, Tran Hoang Thong, Le Pham Thuy Hien, Nguyen Thai Anh | 소속 기관 미확인 (ISRSD 2026 채택)
- **출처**: arXiv · 2026-07-28 제출 · **preprint(미동료심사)** (ISRSD 2026 채택)
- **분야 태그**: 바이오인포 / 단일세포
- **선택 이유**: "딥러닝 vs. PCA — 어느 쪽이 실제로 더 나은가?"라는 단일세포 분석의 실용적 의문을 Sobol 전체차수 민감도 분석과 엄밀한 통계 검정 조합으로 처음 정량화한 진단 벤치마크다.
- **사회적 신호**: 없음
- **핵심 요약**: 10개 실제 데이터셋(세포 수 90~5,685개, 유전자 수 19,046~41,480개, 세포 유형 4~11종)에서 9개 클러스터링 파이프라인을 비교했으며, Optuna 하이퍼파라미터 탐색·반복 실행 강건성·Friedman/Wilcoxon-Holm/TOST 검정·Sobol 전체차수 민감도 분석을 통합한 프로토콜로 딥 표현 학습이 PCA 기반 파이프라인을 유의미하게 상회하는 조건을 진단한다.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (10개 공개 실제 데이터셋 벤치마크)

---

### W3. FEV 프레임워크: 기능·증거·검증을 통한 에이전트 바이오인포매틱스 평가 (Evaluating Agentic Bioinformatics through Function, Evidence, and Validation)

- **arXiv/DOI**: arXiv:2607.27556
- **원문 URL**: https://arxiv.org/abs/2607.27556
- **저자**: Phuc Pham, Truong-Son Hy | 소속 기관 미확인
- **출처**: arXiv · 2026-07-30 제출 · **preprint(미동료심사)**
- **분야 태그**: LLM-bio / 바이오인포
- **선택 이유**: 에이전트 바이오인포매틱스 109개 시스템·28개 벤치마크를 포괄하는 이번 주 주목할 리뷰로, LLM 에이전트가 생물학 분석에서 과학적 신뢰성을 갖추기 위한 조건을 FEV 프레임워크로 처음 체계화했다.
- **사회적 신호**: 없음
- **핵심 요약**: LLM 에이전트가 생물학 분석을 유창하게 수행해도 과학적 신뢰성은 자동으로 보장되지 않는다. FEV(Function·Evidence·Validation) 프레임워크는 워크플로 아키텍처나 최종 출력이 아닌 검사 가능한 워크플로 궤적을 분석 단위로 삼아, 유전체·단일세포·공간 오믹스·단백질 과학·신약 발굴·계산 병리 등 6개 분야에 걸쳐 109개 에이전트/에이전트 인접 시스템과 28개 벤치마크·평가 자료를 분류한다.
- **코드/데이터**: 미확인
- **검증 수준**: 해당 없음 (리뷰·프레임워크 논문)
