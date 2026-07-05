---
type: raw
period: 2026-W27
date_collected: 2026-07-05
sources:
  arxiv_qbio: 2편
  arxiv_csLG: 3편
  wide_arxiv: 2편
total_core: 5
total_wide: 2
---

# 2026-W27 논문 수집 (2026-07-05)

수집 범위: 2026-06-29 ~ 2026-07-05
소스: arXiv(q-bio.GN, cs.LG, cs.AI), 웹 검색(arXiv 직접 조회)
중복 제외: W24 5편, W25 7편, W26 5편 (recent-papers.jsonl 기준, arXiv ID 2606.12219 외 16건)

---

# 핵심 논문 (Top 5)

## 1. 게놈 규모 메커니즘 유전자 주석: 발표 문헌으로부터 (Affinage: genome-scale mechanistic gene annotation from the published literature)

- **저자**: Matteo Di Bernardo, Iain M. Cheeseman | Whitehead Institute for Biomedical Research & MIT Department of Biology, Cambridge MA
- **출처**: arXiv:2607.02217 · 2026-07-02 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2607.02217
- **코드**: 데이터 공개 (초록 내 URL 명시 — 19,293개 유전자 주석 레코드 오픈 배포)
- **태그**: [유전체, LLM-bio, 바이오인포]
- **사회적 신호**: 없음
- **선택 이유**: 인간 단백질 코딩 유전자 19,293개 전체에 대해 LLM이 1차 문헌에서 직접 메커니즘 근거를 추출·합성한 구조화 주석을 생성하고, 결과물을 오픈 배포한 것이 방법론적·자원 측면에서 즉시 활용 가능한 임팩트를 지님.
- **초록 요약**: Affinage는 유전자당 한 번씩 1차 문헌만을 대상으로 검색·메커니즘 추론을 수행하고 재사용 가능한 구조화 주석으로 저장하는 LLM 파이프라인이다. 생물학자가 설계한 "읽기 패스(reading pass)"는 직접 실험 증거만 추출하고, "합성 패스(synthesis pass)"는 그 증거만으로 추론한다. 게놈 전체에 적용해 19,293개 인간 단백질 코딩 유전자를 주석했다. UniProt 기능 항목이 비어 있거나 부실한 수천 개 유전자에 메커니즘 기술을 제공하며, 크로스-패밀리 LLM 판사 기준 head-to-head 비교에서 큐레이션 참조 자료(UniProt) 대비 99.1%에서 우위를 기록했다고 보고한다. (초록 기준 수치)

---

## 2. DNA 메틸화 기반 중추신경계 종양 91클래스 분류 (A Novel Machine Learning Approach for Central Nervous System Tumor Classification from DNA Methylation)

- **저자**: Paulo R. Ferreira Jr., Lucas Coutinho Freitas, Laís dos Santos Gonçalves, William Borges Domingues, Lucas Petitemberte de Souza, Mariana B. Michalowski, Vinicius F. Campos | Universidade Federal de Pelotas & Hospital de Clínicas de Porto Alegre (Brazil)
- **출처**: arXiv:2607.01307 · 2026-07-01 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2607.01307
- **코드**: 미확인
- **태그**: [임상ML, 유전체, 암진단]
- **사회적 신호**: 없음
- **선택 이유**: 독립 임상 평가 코호트(1,104건) 포함 91클래스 CNS 종양 분류에서 기존 참조 시스템(Capper 2018 기준) 대비 클래스·패밀리 수준 모두 4~5 퍼센트포인트 개선을 보여, 신경병리 진단에 실질적 함의가 있다.
- **초록 요약**: DNA 메틸화 프로파일링 기반 CNS 종양 분류에서 코호트 간 전이 가능성, 방법론적 엄밀성, 강건한 다중클래스 평가라는 과제를 다룬다. 드문 랜덤 투영(Sparse Random Projection)으로 차원을 축소하고 다항 로지스틱 회귀로 분류하는 방법론을 제안한다. 2,801건 참조 코호트에서 층화 3-fold 교차검증 평균 정확도 96%를 기록했으며, 독립 임상 평가 코호트(1,104건)에서 91클래스 수준 86%, 메틸화 클래스 패밀리 수준 93%를 달성했다. 이는 기존 상태-of-the-art 참조 수치 대비 각각 4 퍼센트포인트, 5 퍼센트포인트 절대 개선에 해당한다. (초록 기준 수치)

---

## 3. LLM 기반 분자 최적화를 위한 능동적 모방-자기발견 강화학습 (Active-GRPO: Adaptive Imitation and Self-Improving Reasoning for Molecular Optimization)

- **저자**: Xuefeng Liu, Mingxuan Cao, Qinan Huang, Thomas Brettin, Rick Stevens, Le Cong | Stanford University School of Medicine; University of Chicago (Data Science Institute & Pritzker School of Molecular Engineering); Argonne National Laboratory
- **출처**: arXiv:2607.00531 · 2026-07-01 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2607.00531
- **코드**: 미확인
- **태그**: [신약AI, LLM-bio, 분자최적화]
- **사회적 신호**: 없음
- **선택 이유**: 지시 기반 분자 최적화에서 LLM이 인스턴스별로 참조 모방과 자체 발견 강화를 동적으로 선택하는 Active Reasoning 패러다임을 제안해, TOMG-Bench MOLOPT에서 RePO 대비 의미 있는 성능 개선을 달성했다.
- **초록 요약**: 답만 제공하는 지도학습(SFT)은 다단계 추론을 붕괴시키고, 검증 가능한 보상의 강화학습(RLVR)은 희소 피드백으로 어려움을 겪는 지시 기반 분자 최적화 문제를 다룬다. 기존 Reference-guided Policy Optimization(RePO)은 참조 품질에 성능 상한이 묶이는 문제가 있었다. Active-GRPO는 정책(policy)이 인스턴스별로 참조를 모방할지 자체 발견을 강화할지 능동적으로 결정하면서 모방 대상도 지속 갱신하는 active reasoning 패러다임을 제안한다. TOMG-Bench MOLOPT에서 평균 SRxSim이 GRPO 0.0959, RePO 0.1665에서 Active-GRPO 0.1773으로 향상되었으며, LogP·MR·QED에서 통계적으로 유의한 개선을 보였다고 보고한다. (초록 기준 수치)

---

## 4. 생물학적 경로 구조 통합 Gaussian Process를 이용한 고차원·소표본 오믹스 분류 (Structured Gaussian Processes for Uncertainty-Aware Classification of High-Dimensional, Small-Sampled Omics Data)

- **저자**: Yue Zhang, Nandini Amit Gadhia, Georgios Karagiannis, Michalis Smyrnakis | Durham University (Mathematical Sciences); STFC Hartree Centre, University of Liverpool & Daresbury Laboratory
- **출처**: arXiv:2607.02103 · 2026-07-02 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2607.02103
- **코드**: 미확인
- **태그**: [유전체, 임상ML, 마이크로바이옴]
- **사회적 신호**: 없음
- **선택 이유**: 고차원-소표본 오믹스 분류라는 임상 연구의 고질적 문제를 해결하기 위해 알려진 생물학적 상호작용 네트워크를 커널(kernel)에 직접 내장한 구조화 GP를 제안하며, 불확실성 정량화를 포함한 점이 임상 적용 가능성을 높인다.
- **초록 요약**: 비선형 상호작용이 지배하고 클래스 불균형이 소수 표현형 예측을 어렵게 하는 고차원·소표본 오믹스 분류 문제를 다룬다. 알려진 생물학적 경로를 그래프로 인코딩하고 이를 GP 커널 구성에 직접 통합하는 구조화 GP 분류 프레임워크를 제안한다. 알려진 상호작용 네트워크를 따라 정보를 전파하고 풍부도(abundance) 파생 특성과 결합함으로써 정량적 측정값과 위상적 맥락을 모두 포착한다. 3개의 공개 장·대변 마이크로바이옴 데이터셋에서 벤치마킹 결과를 보고한다. (초록 기준)

---

## 5. 수용해도 예측을 위한 화학·구조 기여 분리 MLP-GNN 프레임워크 (An Additive MLP-GNN Framework for Characterizing Chemical and Structural Contributions to Aqueous Solubility)

- **저자**: Sampreeti Bhattacharya, Arkaprava Roy | University of North Carolina (졸업생), University of Florida
- **출처**: arXiv:2607.02212 · 2026-07-02 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2607.02212
- **코드**: 미확인
- **태그**: [신약AI, ADME, 분자특성]
- **사회적 신호**: 없음
- **선택 이유**: 약물 초기 스크리닝 핵심 지표인 수용해도 예측에서 물리화학적 기술자(MLP)와 그래프 위상(GNN)을 분리 학습해 기여도를 분해하는 해석 가능한 구조를 제안하며, AqSolDB 사전학습 + BigSolDB2 파인튜닝으로 정확도와 재현성을 개선했다.
- **초록 요약**: 수용해도 예측 모델 대부분이 물리화학적 기술자와 분자 그래프 정보를 단일 표현으로 병합해 예측이 전역 화학에 의한 것인지 분자 구조에 의한 것인지 불분명한 문제를 다룬다. 물리화학적 기술자는 다층 퍼셉트론(화학 브랜치)으로, 분자 그래프 위상은 그래프 신경망(구조 브랜치)으로 각각 학습하고 예측 단계에서만 덧셈 결합하는 프레임워크를 제안한다. 선택적 곱셈 상호작용(multiplicative interaction) 항을 허용해 화학·구조 기여도를 훈련 후 분리 검토할 수 있다. 대규모 AqSolDB로 사전학습하고 소규모 BigSolDB2로 파인튜닝하면 정확도와 반복 안정성이 실질적으로 개선된다고 보고한다. (초록 기준)

---

# 와이드 (Wide Angle)

## W1. 반복적 메타-반추를 통한 자율 과학 발견 시스템 DiscoPER (Autonomous Scientific Discovery via Iterative Meta-Reflection)

- **출처**: arXiv:2607.01131 · 2026-07-01 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2607.01131
- **태그**: [AI에이전트, 자율과학]
- **사회적 신호**: 없음
- **한줄 요약**: DiscoPER는 사전 정의된 연구 목표 없이 데이터셋을 동적으로 탐색하는 자율 LLM 과학발견 프레임워크로, 모든 발견에 통계 검증을 요구하고 주기적 '메타-반추(meta-reflection)'로 누적 발견을 2차 합성해 복잡한 상호 연결 현상을 포착한다고 보고한다.

---

## W2. 교환대수 학습 기반 단백질 유연성 분석 (Commutative Algebra Learning for Protein Flexibility Analysis)

- **출처**: arXiv:2607.00879 · 2026-07-01 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2607.00879
- **태그**: [단백질, 구조생물학]
- **사회적 신호**: 없음
- **한줄 요약**: CAL(Commutative Algebra Learning)은 교환대수 이론으로 다중 공간 스케일의 국소 대수 기술자를 구성해 단백질 B-팩터(유연성)를 예측하며, 364개 단백질 벤치마크에서 고전적 가우시안 네트워크 모델(GNM) 대비 34.5% 예측 정확도 향상을 보고한다.
