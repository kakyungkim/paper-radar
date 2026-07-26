---
week: 2026-W30
date_range: 2026-07-20 ~ 2026-07-26
created: 2026-07-26
scout: paper-scout
---

# 2026-W30 수집 논문

수집일: 2026-07-26 | 주차: 2026-W30 (2026-07-20 ~ 2026-07-26)

| 소스 | 핵심 | 와이드 | 합계 |
|------|------|--------|------|
| arXiv (q-bio / cs.LG / cs.AI) | 4 | 2 | 6 |
| bioRxiv | 1 | 0 | 1 |
| **합계** | **5** | **2** | **7** |

중복 제외 확인: W26~W29 arXiv ID 및 DOI 목록 대조 완료. 이번 주 신규 논문만 수록.

---

## 핵심 (Core 5)

### 1. 단일세포·공간 전사체 파운데이션 모델 조화 벤치마크: 맥락 의존적 일반화 (Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation)

- **arXiv/DOI**: arXiv:2607.17227
- **원문 URL**: https://arxiv.org/abs/2607.17227
- **저자**: Sally Chen, Roxana Zahedi, Lucy Chhuo, Ricky Nguyen, Marjan BaghGolshani, Amin Beheshti, Mark Grosser, Min Yang, Nona Farbehi, Nigel Lovell, Ahmadreza Argha, Fatemeh Vafaee, Youqiong Ye, Hamid Alinejad-Rokny | University of New South Wales · University of Technology Sydney (교신: Hamid Alinejad-Rokny)
- **출처**: arXiv · 2026-07-19 제출 (arXiv 공개 2026-07-21) · **preprint(미동료심사)**
- **분야 태그**: 바이오인포 / 단일세포 / LLM-bio
- **선택 이유**: scRNA-seq, 공간 전사체, Perturb-seq를 아우르는 통일 프레임워크로 6종 파운데이션 모델을 처음 체계 비교한 벤치마크; 모델 선택에 직접적 실용 가이드를 제공한다
- **사회적 신호**: 없음(확인된 HF Daily Papers 순위·X 언급 없음)
- **핵심 요약**: Nicheformer, CellPLM, scGPT-spatial, GenePT, scELMo, Novae 등 6종 단일세포·공간 파운데이션 모델을 동일 프레임워크로 평가했다. 평가 범위는 제로샷 및 지속학습(continually pretrained) 클러스터링, 지도 어노테이션, 마커 유전자 일치도, 교란(perturbation) 반응 예측이며, 어떤 단일 모델도 전 과제에서 우위를 보이지 않았다. 성능 순위는 모달리티·전처리·토크나이저·생물학적 사전·도메인 이동·지표 선택에 따라 크게 달라졌다.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (표준 벤치마크)

---

### 2. 신뢰 가능한 단백질-리간드 결합 친화도 예측: 신뢰도 인식 다중엔진 융합 (Trustworthy Protein-Ligand Binding Affinity Prediction via Reliability-Aware Multi-Engine Fusion)

- **arXiv/DOI**: arXiv:2607.17601
- **원문 URL**: https://arxiv.org/abs/2607.17601
- **저자**: 미확인 (초록 페이지 접근 차단으로 저자명 확인 불가)
- **출처**: arXiv · 2026-07-20 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / 단백질 / 바이오인포
- **선택 이유**: 기존 도킹 엔진 합의 스코어링의 한계를 불확실성 정량화로 극복한 방법; 신뢰 가능한 계산 약물 발견에 대한 실질적 진전
- **사회적 신호**: 없음
- **핵심 요약**: 기존 도킹 엔진들이 서로 다른 결합 친화도 예측을 제시할 때 어느 것을 신뢰해야 하는지 알 수 없다는 문제를 해결하기 위해 RELIABLE-BA를 제안했다. 각 도킹 엔진을 Normal-Inverse-Gamma 분포 기반 증거 전문가(evidential expert)로 모델링하고, 분자 맥락에서 학습한 신뢰도로 인식론적 불확실성을 조정한 뒤 폐쇄형(closed-form) 집계로 융합한다. PDBBind·BDB2020+ 벤치마크에서 경쟁적 점 예측을 유지하면서 불확실성 보정이 실질적으로 개선됐으며, SARS-CoV-2 Mpro·5HT2A 수용체에서도 적용 가능성을 확인했다.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (PDBBind, BDB2020+, SARS-CoV-2 Mpro, 5HT2A 수용체 벤치마크)

---

### 3. LLM은 결합 분자를 꿈꾸는가? 공간적 제약 하의 LLM 벤치마크 (Do Language Models Dream of Binding Molecules? Benchmarking LLMs under Spatial Constraints)

- **arXiv/DOI**: arXiv:2607.18144
- **원문 URL**: https://arxiv.org/abs/2607.18144
- **저자**: Thomas MacDougall, Maksim Kuznetsov, Roman Schutski, Rim Shayakhmetov, Maxim Malkov, Vladimir Aladinskiy, Alex Aliper, Alex Zhavoronkov | Insilico Medicine 외
- **출처**: arXiv · 2026-07-20 제출 · **preprint(미동료심사)**
- **분야 태그**: 신약AI / LLM-bio
- **선택 이유**: 확산 모델 위주였던 구조 기반 약물 설계(SBDD) 생성 분야에서 범용 LLM이 얼마나 근접했는지 처음으로 체계 비교; Insilico Medicine 팀의 벤치마크로 산업 시사가 크다
- **사회적 신호**: 없음
- **핵심 요약**: 3D 단백질 포켓 구조를 조건으로 결합 분자를 생성하는 구조 기반 약물 설계(SBDD)에서 범용 LLM이 기존 확산 모델 특화 기준선과 어떻게 비교되는지 체계적으로 분석했다. 포켓 조건부 분자 생성 외에 앵커 단편(anchor fragments), 파마코포어 포인트, 필수 포켓-리간드 상호작용 등 추가적 3D 공간 제약 조건 세 종류를 포함해 평가했다. 현재 범용 LLM은 복잡한 3D 물리적 공간 추론에서 확산 기반 특화 모델에 크게 미치지 못함을 보였다.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (벤치마크)

---

### 4. GatorPrism: 공간 멀티오믹스 통합을 위한 연합 그래프 전문가의 프로토타입 조건부 라우팅 (GatorPrism: Prototype-Conditioned Routing across Coalition Graph Experts for Spatial Multi-Omics Integration)

- **arXiv/DOI**: 10.64898/2026.07.23.739930
- **원문 URL**: https://www.biorxiv.org/content/10.64898/2026.07.23.739930
- **저자**: Zhang Z., Zhang Y., Li X., Bian J., Shen J., Liu Y. | 기관 미확인
- **출처**: bioRxiv · 2026-07-24 게재 · **preprint(미동료심사)**
- **분야 태그**: 바이오인포 / 공간전사체 / 멀티오믹스
- **선택 이유**: 공간 멀티오믹스 통합에 혼합 전문가(MoE) 방식을 적용한 새로운 접근; 공간 해상도를 유지하면서 멀티오믹스 데이터를 통합하는 미해결 문제에 대응한다
- **사회적 신호**: 없음
- **핵심 요약**: 공간 멀티오믹스 데이터 통합을 위해 프로토타입 조건부 라우팅(prototype-conditioned routing)과 연합 그래프 전문가(coalition graph experts) 구조를 활용한 GatorPrism을 제안했다. 추정: 서로 다른 오믹스 모달리티를 공간 정보를 보존하면서 통합하는 그래프 기반 프레임워크로 보임. 세부 방법론 및 성능 수치는 bioRxiv 초록 직접 확인 필요.
- **코드/데이터**: 미확인
- **검증 수준**: in silico (추정)

---

### 5. 베이즈 불확실성 추정이 의료 AI 에이전트의 임상 의사결정을 개선한다 (Bayesian uncertainty estimation improves clinical decision making in medical AI agents)

- **arXiv/DOI**: arXiv:2607.20582
- **원문 URL**: https://arxiv.org/abs/2607.20582
- **저자**: Frederik Hauke, Patrick Wienholt, Christiane Kuhl, Dyke Ferber, Jakob Nikolas Kather, Sven Nebelung, Daniel Truhn | RWTH Aachen University 외
- **출처**: arXiv · 2026-07-22 제출 · **preprint(미동료심사)**
- **분야 태그**: 임상ML
- **선택 이유**: 의료 AI의 불확실성 정량화가 임상 의사결정 에이전트에서 실제 오진 감소로 이어진다는 정량적 증거를 제시; AI 신뢰성 문제에 실험적으로 답한다
- **사회적 신호**: 없음
- **핵심 요약**: 흉부 X선 8종 소견을 분류하는 다중 과제 모델(훈련 이미지 137,593장)에 몬테카를로 드롭아웃(MC dropout)을 적용해 인식론적 불확실성을 추출했다. 이 불확실성 신호를 추가했을 때 오류 탐지 AUROC가 0.74에서 0.77로 향상됐다(초록 기준). 2×2 요인설계 통제 실험에서, 불확실성을 원시 점수가 아닌 이진 오류-위험 플래그로 제공했을 때만 임상 의사결정 지원 AI 에이전트가 이를 실제 활용해 신뢰성 낮은 소견에서 자신감 있는 오진율을 8.5%에서 2.7%로 낮췄다(초록 기준).
- **코드/데이터**: 미확인
- **검증 수준**: in silico / 통제 실험 (흉부 X선 데이터, 단기관 추정)

---

## 와이드 (Wide 2)

### W1. 오류 국소화를 통한 추론 시간 스케일링 (Test-Time Scaling via Error Localization)

- **arXiv/DOI**: arXiv:2607.21453
- **원문 URL**: https://arxiv.org/abs/2607.21453
- **저자**: Rajiv Shailesh Chitale, Rahul Madhavan, Taneesh Gupta, Deepanway Ghosal, Aravindan Raghuveer
- **출처**: arXiv · 2026-07-23 제출 · **preprint(미동료심사)**
- **분야 태그**: LLM / 추론 (핵심 축 외)
- **선택 이유**: 추론 시간 스케일링의 실용적 진보; 바이오 에이전트 및 임상 의사결정 AI에도 잠재적 적용 가능
- **핵심 요약**: 추론 경로에서 오류가 발생한 토큰 위치를 조건부 확률 비교로 국소화하고, 유효한 전위(prefix)를 최대한 재사용하면서 새 경로를 분기하는 TTEL 알고리즘을 제안했다. 별도 학습 없이 고정 또는 환경 피드백을 활용하는 추론 시간(inference-time) 접근이다.

---

### W2. 사이클릭 펩타이드 앙상블의 그래프 학습: 분자 앙상블 모델링 탐구 (Graph Learning on Ensembles of Cyclic Peptides: An Investigation of Molecular Ensemble Modeling)

- **arXiv/DOI**: arXiv:2607.21561
- **원문 URL**: https://arxiv.org/abs/2607.21561
- **저자**: Aaron Feller, Kris Deibler, Maxim Secor
- **출처**: arXiv · 2026-07-23 제출 · **preprint(미동료심사)** (ICML 2026 Graph Foundation Models 워크숍 채택)
- **분야 태그**: 분자ML / 신약AI 인접 (핵심 축 경계)
- **선택 이유**: 단일 구조가 아닌 형태 앙상블(conformational ensemble) 전체를 학습 입력으로 삼는 새로운 패러다임; 사이클릭 펩타이드 신약 분야에서 점점 중요해지는 방향
- **핵심 요약**: 용액 내 분자는 단일 구조가 아닌 형태 앙상블로 존재함에도 기존 모델은 대표 구조 하나만 사용하는 한계를 지적했다. EnsembleEGNN은 각 구조를 공유 EGNN으로 인코딩한 뒤 Set Attention Block으로 풀링하는 앙상블 인코더를 도입했다. CREMP 사이클릭 펩타이드 앙상블 데이터셋으로 사전학습(마스크 토큰 복원·좌표 재구성·쌍 거리 재구성)했으며, CREMP-CycPeptMPDB에서 스크래치 학습(R²=0.005) 대비 사전학습 모델(R²=0.477, Pearson r=0.699)이 크게 앞서며 서열 전용 BERT 기준(R²=0.439)도 능가했다(초록 기준).
