---
week: 2026-W41
period: 2026-10-05 ~ 2026-10-11
collected: 2026-10-11
sources:
  arxiv: 6
  biorxiv: 1
  medrxiv: 0
  pubmed_journal: 0
  total: 7
---

# 2026-W41 수집 논문

수집일: 2026-10-11 / 대상 기간: 2026-10-05 ~ 2026-10-11

소스별 건수: arXiv 6편 · bioRxiv 1편 (핵심 5 + 와이드 2)

> 수집 방법: spaceship/newDailyArxiv GitHub 이슈 #104–#108 (Oct 5–9, 2026), bioRxiv 유전체학 컬렉션 10월 목록, ICLR 2026 virtual listing, 웹 검색. arxiv.org·biorxiv.org·huggingface.co 직접 접근은 에이전트 프록시 차단으로 불가 — 제목·ID는 GitHub 이슈 페이지 직접 추출 및 검색 기반. 초록을 직접 확인한 논문(C1, W1)은 "초록 확인" 표기; 나머지는 "초록 미확인 (제목·ID·게재처 확인)" 표기.

---

## 핵심 (Core)

### [핵심] C1. 단백질-분자 가상 스크리닝을 위한 인과적 개념 정렬 (CausalBind: Causal Modeling and Learning for Protein-Molecule Virtual Screening)

- **저자/소속**: 저자명 미확인 (ICLR 2026 listing 저자 추출 실패)
- **출처**: arXiv · 2026-10-05 · **preprint(미동료심사)** — ICLR 2026 채택 확인 (peer-reviewed 전환)
- **DOI/링크**: https://arxiv.org/abs/2610.07340
- **코드/데이터**: 미확인
- **초록 요약** (초록 확인 — ICLR 2026 listing 기준): 기존 대조 학습 기반 가상 스크리닝 방법은 분자와 단백질 결합 포켓 전체 표현을 정렬하면서 결합과 무관한 특징 및 허위 상관(spurious correlation)이 포함돼 새 표적으로의 일반화가 약해진다는 문제를 지적한다. 교차-어텐션(cross-attention)과 학습 가능한 희소 마스킹으로 인과적으로 결합과 관련된 원자 개념들을 분리·추출하는 플러그인 모듈을 제안한다. BEDROC 및 EF@1% (초기 농축도) 지표에서 기준선 대비 개선을 보이며, LIT-PCBA 벤치마크에서 가장 큰 향상을 기록한다고 보고한다.
- **핵심 수치**: BEDROC 및 EF@1% 개선 (구체 수치는 원문 확인 필요); LIT-PCBA 최대 향상 (출처: ICLR 2026 listing iclr.cc/virtual/2026/10022811)
- **분야 태그**: 신약AI / 단백질
- **사회적 신호**: ICLR 2026 채택 확인; spaceship/newDailyArxiv Issue #108 단백질 분야 목록 수록 (NeurIPS 2026 Oral로도 표기 — 출처 불일치, 확인 필요)
- **선별 사유**: ICLR 2026 채택 + 인과 추론으로 가상 스크리닝 허위 상관 문제를 정면으로 다룬 방법론 — LIT-PCBA 같은 현실적 벤치마크에서의 개선이 의미 있음.

---

### [핵심] C2. 단백질 언어 모델의 선형 피트니스 부분공간을 통한 샘플 효율적 지향 진화 (Linear Fitness Subspace in Protein Language Models Enables Sample-Efficient Directed Evolution)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-06 · **preprint(미동료심사)** — EMNLP 2026 Findings 채택 확인
- **DOI/링크**: https://arxiv.org/abs/2610.07607
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — 제목·ID·게재처 확인): 단백질 언어 모델(PLM) 내부에 피트니스(활성)가 선형 부분공간으로 포착된다는 가설을 바탕으로, 소수의 실험 데이터로 지향 진화(directed evolution)를 가능하게 하는 방법을 제안하는 것으로 보인다 (해석: 제목 기반).
- **핵심 수치**: 미확인 (원문 직접 확인 필요)
- **분야 태그**: 단백질 / LLM-bio / 신약AI
- **사회적 신호**: EMNLP 2026 Findings 채택; spaceship/newDailyArxiv Issue #107–108 단백질 분야 목록 수록
- **선별 사유**: EMNLP 2026 채택 + PLM의 피트니스 지형을 선형화해 샘플 효율을 높인다는 방법론적 기여 — 단백질 공학 실험 데이터가 희소한 환경에 직접 적용 가능.

---

### [핵심] C3. 알츠하이머 신약 개발을 위한 엔트로피 유도 역인과 AI로 상류 병목 유전자 발굴 (Entropy-Guided Reverse-Causal AI to Identify Upstream Bottleneck Genes for Alzheimer's Drug Discovery)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-06 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.08736
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — 제목·ID 확인): 엔트로피 기반 역인과 AI 방법으로 알츠하이머병 신약 개발의 타깃이 되는 상류 병목 유전자(upstream bottleneck genes)를 규명하는 것이 목적인 것으로 보인다 (해석: 제목 기반). 관련 선행 연구(arXiv 2502.03938, AAAI 2025)는 비슷한 역방향 추적 기법을 알츠하이머 인과 유전자 발굴에 적용한 바 있다.
- **핵심 수치**: 미확인
- **분야 태그**: 신약AI / 바이오인포
- **사회적 신호**: spaceship/newDailyArxiv Issue #107–108 약물 분야 목록 수록
- **선별 사유**: 알츠하이머 타깃 발굴에 역인과(reverse-causal) 추론을 접목 — 치매 치료제 개발이라는 높은 임상 파급력과 결합.

---

### [핵심] C4. 드문 스플라이싱 이벤트에 유전체 모델 파인튜닝으로 TDP-43 병리 신규 바이오마커 발굴 (Fine-tuning genomic models on rare splicing events identifies a novel biomarker of TDP-43 pathology)

- **저자/소속**: 저자명 미확인
- **출처**: bioRxiv · 2026-10-07 · **preprint(미동료심사)**
- **DOI/링크**: https://doi.org/10.64898/2026.10.07.757366
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — bioRxiv 유전체학 컬렉션 2026-10-07 목록에서 제목 확인): 유전체 파운데이션 모델을 드문(rare) 스플라이싱 이벤트에 파인튜닝하여 TDP-43 단백질병증(proteinopathy)의 신규 RNA 기반 바이오마커를 발굴하는 연구로 보인다 (해석: 제목 기반). TDP-43은 ALS(근위축성 측삭경화증)·FTD(전두측두엽치매)의 핵심 병인 단백질이다.
- **핵심 수치**: 미확인
- **분야 태그**: 유전체 / LLM-bio / 임상ML
- **사회적 신호**: bioRxiv 유전체학 컬렉션 2026-10-07 목록 수록
- **선별 사유**: 유전체 파운데이션 모델을 드문 스플라이싱 이벤트에 파인튜닝한다는 방법론 + ALS/FTD 진단용 바이오마커 발굴이라는 임상 파급력 결합.

---

### [핵심] C5. 마우스-인간 신경 역학 정렬로 임상 약효를 추적하는 교차 종 표현 학습 (Cross-species representation learning aligns mouse and human neural dynamics and tracks clinical drug efficacy)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-08 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.11222
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — 제목·ID 확인): 마우스와 인간의 신경 역학(neural dynamics)을 공동 표현 공간으로 정렬하는 교차 종 표현 학습(cross-species representation learning)을 통해 전임상(preclinical) 데이터로부터 임상 약효(clinical drug efficacy)를 추적하는 것이 핵심 내용으로 보인다 (해석: 제목 기반). 전임상-임상 번역 문제에 신경 표현 학습을 적용한 신규 방향.
- **핵심 수치**: 미확인
- **분야 태그**: 임상ML / 신약AI
- **사회적 신호**: spaceship/newDailyArxiv Issue #108 약물 분야 목록 수록
- **선별 사유**: 마우스 전임상 신호에서 인간 임상 약효를 예측하는 연결 고리를 표현 학습으로 구축한다는 방향 — 신약 개발 번역 실패(translational failure) 문제에 직접 닿는 방법론.

---

## 🔭 와이드 (Wide)

### [와이드] W1. 변환기(Transformer)는 여섯 공변량보다 못하다: 아동기 에세이에서 우울 증상 장기 예측 (No Transformer Beats Six Covariates: Long-Horizon Prediction of Depressive Symptoms from Childhood Essays)

- **arXiv/DOI**: https://arxiv.org/abs/2610.07764
- **저자**: Daniel Kua, Emrul Hasan, John-Jose Nunez, Frances Chen | 소속 미확인
- **날짜**: 2026-10-06
- **상태**: preprint(미동료심사)
- **한 줄 요약** (초록 확인 — 제3자 집계 기반): 영국 전국 아동 발달 연구(NCDS) 코호트에서 11세 에세이만 사용하는 텍스트 전용 모델 7종(파인튜닝 트랜스포머)과 제로샷 LLM 4종 모두가 아동기 6개 구조화 공변량에 대한 로지스틱 회귀보다 23세 우울 증상 예측에서 뒤처진다는 것을 보였다 (출처: opentrain.ai 집계 페이지 — 원문 직접 확인 권장).
- **와이드 선택 사유**: "구조화 공변량 > 복잡한 텍스트 모델"이라는 결과가 임상 예측 연구 설계 및 모델 선택에 주는 반례 — 특히 종적 임상 데이터에서 과잉 복잡성의 위험을 되짚게 한다.

---

### [와이드] W2. 회로 질환 타깃 발굴을 위한 시스템 신경과학 지식 그래프 기반 에이전틱 추론 (CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies)

- **arXiv/DOI**: https://arxiv.org/abs/2610.09643
- **저자**: 저자명 미확인
- **날짜**: 2026-10-07
- **상태**: preprint(미동료심사)
- **한 줄 요약** (초록 미확인 — 제목·ID 확인): 시스템 신경과학 지식 그래프 위에서 LLM 에이전틱 추론을 수행해 회로병증(circuitopathies — 뇌 회로 이상 관련 신경질환)의 신약 타깃을 발굴하는 프레임워크로 보인다 (해석: 제목 기반).
- **와이드 선택 사유**: LLM 에이전트와 신경과학 지식 그래프를 결합한 신약 타깃 발굴 시스템 — 뇌 회로 질환(우울증·조현병·파킨슨병 등)에 대한 타깃 중심 신약 개발 관점에서 관심 가치가 있는 접근법.
