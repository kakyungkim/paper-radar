---
week: 2026-W32
date_range: 2026-08-03 ~ 2026-08-09
created: 2026-08-09
scout: paper-scout
---

# 2026-W32 수집 논문

수집일: 2026-08-09 | 주차: 2026-W32 (2026-08-03 ~ 2026-08-09)

| 소스 | 핵심 | 와이드 | 합계 |
|------|------|--------|------|
| arXiv (q-bio / cs.LG / cs.AI / cs.CL) | 5 | 2 | 7 |
| Nature Medicine (저널) | 0 | 1 | 1 |
| **합계** | **5** | **3** | **8** |

중복 제외 확인: W28~W31 arXiv ID 및 DOI 목록 대조 완료. 제외 목록: 2607.* 계열 전체 (W28~W31 수록 논문), DOI:10.64898/2026.07.28.741284 포함.

---

## 핵심 (Core 5)

### 1. 단일세포 생성을 위한 자기회귀 트랜스포머 스케일링 (Scaling an Autoregressive Transformer for Single-Cell Generation)

- **arXiv/DOI**: arXiv:2608.02961
- **원문 URL**: https://arxiv.org/abs/2608.02961
- **저자**: Aleksandr Sharipov, Yusif Mukhtarov, Igor Molybog (교신 저자 미명시) | 소속 기관 미확인
- **출처**: arXiv · 2026-08-03 제출 · **preprint(미동료심사)**
- **분야 태그**: 유전체 / LLM-bio / 단일세포
- **선택 이유**: 단일세포 파운데이션 모델 최초의 양지수 스케일링 법칙(two-exponent scaling law)과 연산 최적 프론티어를 도출한 연구로, 모델 파라미터 수와 학습 데이터 양을 함께 변화시키며 스케일링 행동을 체계적으로 분석했다. 코드·데이터 공개 여부는 미확인이나 방법론적 신규성이 높다.
- **사회적 신호**: 없음
- **핵심 요약**: 세포 유형으로부터 단일세포 유전자 발현 벡터를 추가 생성하는 자기지도 생성 태스크를 연구한다. 모델 구조는 학습된 양자화 VAE 토크나이저와 인과적 트랜스포머(causal transformer)를 결합하고 교차 엔트로피 손실로 학습한다. 생성된 발현 벡터의 생물학적 충실도와 사전 학습 손실의 스케일링 행동을 모두 분석하며, 파라미터 수·학습 데이터 양에 대한 변화를 통해 단일세포 파운데이션 모델 최초의 양지수 스케일링 법칙 및 연산 최적 프론티어(compute-optimal frontier)를 도출한다. 사전 학습 모델을 교란 반응 예측(perturbation response prediction)에 파인튜닝하는 방향도 논의한다. 구체적 성능 수치는 초록 기준 미명시.
- **코드/데이터**: 미확인
- **검증 수준**: in silico

---

### 2. PhenMol: 세포 표현형에서 구조 보존 기반 분자 표현 학습 (Learning Molecular Representations from Cellular Phenotypes with Structure Preservation)

- **arXiv/DOI**: arXiv:2608.02688
- **원문 URL**: https://arxiv.org/abs/2608.02688
- **저자**: Xuan Lin, Jingyu Sheng, Tengfei Ma, Li Sun, Dapeng Xiong (교신: Dapeng Xiong) | Xiangtan University, Hunan University, Beijing University of Posts and Telecommunications, Southeast University
- **출처**: arXiv · 2026-08-03 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / LLM-bio
- **선택 이유**: 기존 다중모달 표현 학습이 교차 모달 정렬 최적화 과정에서 화학 공간의 내재적 구조를 왜곡하는 문제를 명확히 진단하고, 분자 이웃 구조를 보존하면서 세포 표현형 정보를 통합하는 PhenMol 프레임워크를 제안한다. 약 30,400개 분자-세포 형태 쌍 실험에서 270개 생물활성 태스크 전반의 분자 특성 예측 개선을 확인했다.
- **사회적 신호**: 없음
- **핵심 요약**: 표현형 약물 발굴(phenotypic drug discovery)은 분자 구조와 세포 반응 간 기능적 관계를 발견할 수 있으나, 기존 다중모달 정렬 방법은 화학 공간의 본질적 구조를 고려하지 않아 분자 표현을 왜곡하고 구조 정보를 손실한다. PhenMol은 분자 표현과 세포 표현을 공유·비공개 성분(shared/private components)으로 분리해 표현형 유도 정렬을 수행하면서 전담 분자 브랜치로 화학 구조를 보존한다. 약 3.04 × 10^4 분자-세포 형태 쌍에 대한 실험(초록 기준)에서 270개 생물활성 태스크 전반의 분자 특성 예측 성능이 개선됐다. 임상시험 결과 예측 태스크에서도 개선이 보고됐다. 구체 개선 수치는 미명시.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (공개 분자 특성 예측 및 임상시험 결과 예측 벤치마크)

---

### 3. THBKG: 임상 진전 예측을 위한 시간 인식 의생명 지식 그래프 (THBKG: A Temporal Biomedical Knowledge Graph for Decision-Aligned Clinical Advancement Prediction)

- **arXiv/DOI**: arXiv:2608.05982
- **원문 URL**: https://arxiv.org/abs/2608.05982
- **저자**: Pui Chung Siu (1저자), Claudia Cabrera, Mani Mudaliar, Arkaitz Zubiaga (교신) | Queen Mary University of London, Recursion Pharmaceuticals
- **출처**: arXiv · 2026-08-06 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / 임상ML
- **선택 이유**: 임상시험 Phase II→III 진전 예측 문제를 과거 어느 시점의 증거 프로파일도 재구성할 수 있는 시간 인식 이종 지식 그래프로 접근한 연구다. Recursion Pharmaceuticals 공동 저자 참여로 산업 연관성이 높고, Phase II 진입 시점 기준 직접 타깃-질환 증거가 없는 72.8% 쌍에서 그래프 전파가 가장 큰 성능 향상을 보인 점이 실용적이다.
- **사회적 신호**: 없음
- **핵심 요약**: 타깃-질환 연결의 불충분한 증거가 Phase II 효능 실패의 40~50%를 설명하는 것으로 알려져 있으나, 과거 특정 시점의 증거 프로파일을 재구성할 수 있는 의생명 지식 그래프는 기존에 없었다. THBKG(Temporal Heterogeneous Biomedical Knowledge Graph)는 19가지 관계 유형, 110,396개 엔티티, 1,110만 개 엣지로 구성되며 각 엣지에는 증거가 변경된 연도가 부여된다. 의사결정 정렬 벤치마크는 특정 타깃-질환 쌍의 Phase II 진입 여부와, 해당 결정 이전 증거를 근거로 Phase III 진전 여부를 예측한다. THBKG 기반 그래프 전파는 모든 직접 증거 참조 방법을 능가하며, 치료 영역별 상위 10 쌍 기준 상대 성공률 4.3~4.5를 달성한다(초록 기준). Phase II 진입 시점 직접 타깃-질환 증거가 없는 72.8% 쌍에서 성능 향상이 집중됐다.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (후향 임상시험 데이터 기반 벤치마크)

---

### 4. 생존 결과 이진화의 비용: 임상 예후 모델링에서의 대가 (The Cost of Binarizing Survival Outcomes in Clinical Prognostic Modeling)

- **arXiv/DOI**: arXiv:2608.04046
- **원문 URL**: https://arxiv.org/abs/2608.04046
- **저자**: Shashank Yadav, David M. Routman, Andrew Y.K. Foong (교신: Andrew Y.K. Foong) | Mayo Clinic, Department of Radiation Oncology, Rochester MN
- **출처**: arXiv · 2026-08-04 제출 · **preprint(미동료심사)** (Machine Learning for Healthcare Conference 2026 채택)
- **분야 태그**: 임상ML
- **선택 이유**: 임상 ML 연구에서 광범위하게 통용되는 생존 결과 이진화 관행의 통계적 비용을 Bayesian network 기반 특징 선택과 두 임상 코호트를 통해 실증적으로 정량화한 연구다. MLHC 2026에 채택된 연구로 임상 예후 모델 설계 방법론에 직접적 함의가 있다.
- **사회적 신호**: Machine Learning for Healthcare (MLHC) Conference 2026 채택
- **핵심 요약**: 생존 분석(survival analysis)은 사건 발생 시간 데이터를 다루는 정립된 프레임워크이나, 많은 임상 ML 연구는 모델 학습 이전에 결과를 이진화한다. 이진화는 중도절단(censored) 환자를 제외하고, 시간 정보를 단일 임계값으로 붕괴시키며, 예후적으로 관련된 특징 선택에 영향을 줄 수 있다. 저자들은 이진화 비용을 Bayesian network 특징 선택 맥락에서 분석한다. 두 가지 사례 연구: (1) 두경부암(head-and-neck cancer) 코호트에 BN 기반 특징 선택 적용, (2) 생존 결과를 이진화한 수술 코호트 연구. 표본 수 및 구체적 성능 수치는 초록 기준 미명시.
- **코드/데이터**: 미확인
- **검증 수준**: 후향 (두경부암 코호트, 수술 코호트 — 기존 데이터셋 재분석)

---

### 5. EpiBench: LLM은 항체 신약 개발을 위한 에피토프를 이해할 수 있는가? (EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?)

- **arXiv/DOI**: arXiv:2608.06022
- **원문 URL**: https://arxiv.org/abs/2608.06022
- **저자**: Zirui Wang, Jiaqi Wang, Qinghan Wang, Yuzhi Xu, Gang Du, Tingjun Hou, Odin Zhang (교신: Tingjun Hou, Odin Zhang) | 소속 기관 미확인
- **출처**: arXiv · 2026-08-06 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / LLM-bio
- **선택 이유**: 에피토프(epitope)는 항체 결합 위치와 치료적 특성(기능 차단·내성 회피)을 결정하는 핵심 요소임에도, LLM이 서열 정보만으로 에피토프를 추론할 수 있는지에 대한 체계적 평가가 없었다. 구조적 항체-항원 접촉, 기능적 B세포 분석, 심층 돌연변이 스캐닝(DMS) 데이터를 기반으로 한 1,609개 샘플 벤치마크가 이 공백을 처음 채운다.
- **사회적 신호**: 없음
- **핵심 요약**: 에피토프는 항체가 항원에 결합하는 위치를 결정하며 기능 차단·내성 회피 같은 치료적 특성을 형성해 항체 신약 개발의 핵심 요소다. LLM은 강력한 생의학 추론 능력을 보여왔으나 항원·항체 서열에서 직접 에피토프 정보를 추론할 수 있는지는 불분명하다. EpiBench는 (1) 구조적 항체-항원 접촉 데이터, (2) 선별된 기능적 B세포 분석, (3) 심층 돌연변이 스캐닝(deep mutational scanning) 내성 측정치를 기반으로 큐레이션된 1,609개 샘플로 구성된 폐쇄형(closed-book)·서열 기반·자동 채점 가능 벤치마크다. LLM의 에피토프 추론 능력을 체계적으로 평가할 표준 지표가 없던 항체 발굴 분야에 처음으로 정량적 기준선을 제공한다. 개별 모델 결과 수치는 초록 기준 미명시.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (구조 데이터베이스 및 DMS 공개 데이터셋 기반)

---

## 와이드 (Wide 3편)

### W1. LongHorizon-Harness: 실세계 장기 과제를 위한 에이전트 하네스 (LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks)

- **arXiv/DOI**: arXiv:2608.01964
- **원문 URL**: https://arxiv.org/abs/2608.01964
- **저자**: Ziyu Ma, Hailang Huang, Shun Zou, Yong Wang, Shidong Yang, Yiming Hu, Fei Wei, XiangXiang Chu | DreamX Team, Alibaba Group
- **출처**: arXiv · 2026-08-03 제출 · **preprint(미동료심사)**
- **분야 태그**: 에이전트 / LLM
- **선택 이유**: 장기 복합 태스크에서 LLM 에이전트의 자기 평가 오류 누적 문제를 관리-실행-감사(MEA) 루프로 해결하는 하네스를 제안하며, 여러 모델·벤치마크에서 일관된 성능 향상을 보인 이 주 HF Daily Papers 주간 1위 논문이다.
- **사회적 신호**: HuggingFace Daily Papers 주간 랭킹 1위 (2026-08-06 기준). GitHub 코드 공개.
- **핵심 요약**: LLM 에이전트가 여러 단계의 추론·도구 사용·수정을 거치는 장기 태스크에서, 기존 하네스는 실행·태스크 상태·완료 평가를 확장되는 컨텍스트 안에서 유지해 오류 자기 평가가 이후 결정에 누적된다. LongHorizon-Harness는 태스크 상태를 실행 외부에서 명시적으로 관리하고, 환경에서 독립적으로 검증된 사실로만 갱신한다. 관리자(manager)가 태스크 상태를 유지·다음 하위 태스크 결정, 새 컨텍스트 실행자(fresh-context executor)가 수행, 읽기 전용 감사자(read-only auditor)가 환경 상태를 검증하는 MEA 루프 구조다. Qwen 3.7-Plus 기준: WeaveBench 51.8%→80.7%, Terminal-Bench 2.1 69.7%→77.2%, OSWorld 2.0 2.8%→8.3% 향상. Claude Opus 4.7의 OSWorld 2.0 하위집합에서도 20.0%→34.3% 향상(초록 기준).
- **코드/데이터**: https://github.com/AMAP-ML/LongHorizon-Harness (오픈소스 공개)
- **검증 수준**: in silico (WeaveBench, Terminal-Bench 2.1, OSWorld 2.0 벤치마크)

---

### W2. NeuroVFM: 보건 시스템 학습으로 구현된 범용 신경영상 모델 (Health system learning enables generalist neuroimaging models)

- **arXiv/DOI**: DOI:10.1038/s41591-026-04497-1
- **원문 URL**: https://www.nature.com/articles/s41591-026-04497-1
- **저자**: Kondepudi et al. (교신 저자 미확인) | 소속 기관 미확인
- **출처**: Nature Medicine · 2026년 8월 게재 · **peer-reviewed**
- **분야 태그**: 임상ML / 의료영상
- **선택 이유**: 임상 현장에서 일상적으로 생성되는 비큐레이션 CT·MRI 데이터 524만 건을 직접 학습에 사용해 진단·보고 생성·우선순위 분류(triage)를 지원하는 범용 신경영상 파운데이션 모델을 구현했다. 이번 주 Nature Medicine 게재 중 임상 AI 독자에게 직접적 관심이 높다.
- **사회적 신호**: Nature Medicine (IF 최상위) 게재
- **핵심 요약**: NeuroVFM은 보건 시스템 내 일상 임상 진료에서 생성된 비큐레이션 CT·MRI 524만 건을 확장 가능한 3D 체적 예측 아키텍처로 학습해 신경해부학·질환의 공유 표현을 습득한 시각 파운데이션 모델이다. 공개 인터넷 및 의학 데이터로 학습한 기존 파운데이션 모델과 달리, 보건 시스템 데이터를 직접 활용함으로써 최고 수준의 진단 성능을 달성했으며 실제 보건 시스템 내 예비 보고 생성 및 트리아지(triage)를 지원할 수 있음을 보였다. 식별 가능한 안면 특징 포함으로 공개 영역에서 신경영상이 과소 대표되는 문제를 직접 학습으로 극복했다. 구체적 성능 수치는 초록 기준 미명시.
- **코드/데이터**: 미확인
- **검증 수준**: 후향·외부 검증 포함 (실제 보건 시스템 데이터 기반, 세부 코호트 정보 미확인)

---

### W3. 동결하되 항상 접근 가능하지는 않다: 유전체 언어 모델의 표현 분석 (Frozen but Not Always Accessible: A Representation Analysis of Genomic Language Models)

- **arXiv/DOI**: arXiv:2608.05329
- **원문 URL**: https://arxiv.org/abs/2608.05329
- **저자**: Nirjhor Datta, Swakkhar Shatabda, M. Sohel Rahman (교신: M. Sohel Rahman) | Bangladesh University of Engineering and Technology, BRAC University
- **출처**: arXiv · 2026-08-05 제출 · **preprint(미동료심사)**
- **분야 태그**: 바이오인포 / 유전체 / LLM-bio
- **선택 이유**: 유전체 파운데이션 모델을 동결 특징 추출기로 재사용할 때 어느 태스크에서 파인튜닝 없이 생물학적 정보에 접근 가능한지를 처음 통일된 프로빙 프로토콜로 분석한다. "동결 vs. 파인튜닝"의 실용적 판단 기준을 태스크별로 제공하는 연구다.
- **사회적 신호**: 없음
- **핵심 요약**: 유전체 파운데이션 모델은 하위 서열 예측 태스크의 연산 효율적 대안으로 동결 특징 추출기(frozen feature extractor)로 재사용되는 경우가 늘고 있으나, 어떤 생물학적 정보가 태스크 특화 적응 없이 접근 가능한지는 불분명하다. 본 연구는 DNABERT-2, Nucleotide Transformer, HyenaDNA, GENERATOR-v2, Omni-DNA 다섯 모델에 대해 조절·후성유전학·프로모터·스플라이스 부위·변이 효과 예측 태스크에 걸쳐 통일된 동결 프로빙 프로토콜 하에 표현 접근성을 분석한다. 진단 판독(readout)과 검증-선택 분석을 분리함으로써 편향을 최소화한다. 태스크 의존적 일관된 패턴 발견: 동결 프로브는 프로모터 태스크에서 파인튜닝 성능의 95~100%를 회복하나, 평균 스플라이스 부위(splice-site) 회복률은 60~88%에 그친다.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (5개 유전체 언어 모델, 공개 서열 예측 벤치마크)
