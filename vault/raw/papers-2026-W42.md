---
week: 2026-W42
period: 2026-10-12 ~ 2026-10-18
collected: 2026-10-18
sources:
  arxiv: 7
  biorxiv: 0
  medrxiv: 0
  pubmed_journal: 0
  total: 7
---

# 2026-W42 수집 논문

수집일: 2026-10-18 / 대상 기간: 2026-10-12 ~ 2026-10-18

소스별 건수: arXiv 7편 (핵심 5 + 와이드 2)

> 수집 방법: arXiv q-bio(GN·QM·BM) 최근 목록 웹 검색 스니펫, arXiv cs.LG/cs.AI 크로스리스트, HuggingFace Daily Papers 및 NeurIPS 2026 포스터 목록 참조. arxiv.org·biorxiv.org·huggingface.co 직접 접근은 에이전트 프록시 차단(403)으로 불가 — 제목·ID는 Google/Bing 캐시 스니펫 및 q-bio 주간 목록 기반 추출. 초록을 직접 확인하지 못한 논문은 "초록 미확인 (제목·ID 확인)" 표기.

---

## 핵심 (Core)

### [핵심] C1. 계통 감독 신경 역최적운송을 이용한 클론 특이적 섭동 반응 예측 (CloneOT: predicting clone-specific perturbation responses with lineage-supervised neural inverse optimal transport)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-13 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.16093
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — q-bio.GN/QM 목록 제목 확인): CRISPR 기반 계통 추적(lineage tracing) 데이터를 감독 신호로 결합한 신경 역최적운송(neural inverse optimal transport) 프레임워크 CloneOT를 제안. 기존 CellOT(NeurIPS 2021 / Nature Methods 2023) 계열은 섭동 전후 세포를 집단 수준에서 매핑하는 반면, CloneOT는 클론 계통 정보를 레이블로 활용해 동일 클론 내 세포의 섭동 반응을 직접 예측하는 것으로 보인다.
- **핵심 수치**: 미확인 (원문 직접 확인 필요)
- **분야 태그**: 유전체 / 바이오인포 / 단일세포
- **사회적 신호**: 없음
- **선별 사유**: 계통 해상도 섭동 예측은 클론별 약물 반응 이질성 이해의 핵심 — 단일세포 신약 반응 모델링(예: CRISPR 화학-유전학 스크리닝)에서 재현·적용 가능성이 높음.

---

### [핵심] C2. 인터페이스 품질을 위한 AlphaFold 신뢰도 점수 보정 (Calibrating AlphaFold confidence scores for interface quality)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-14 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.17108
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — q-bio.BM 목록 제목 확인): AlphaFold(AF2/AF3)가 제공하는 인터페이스 신뢰도 점수(ipLDDT, ipTM, PAE 기반 점수 등)가 단백질-단백질 인터페이스의 실제 품질(native contact 회수율 등)과 어느 정도 일치하는지 체계적으로 분석하고, 보정(calibration) 방법을 제안하는 것으로 보인다. 선행 연구(actifpTM, C2Qscore, Pinc)에서 ipTM 등이 유연한 영역에 의해 왜곡됨이 지적된 바 있다.
- **핵심 수치**: 미확인
- **분야 태그**: 단백질 / 신약AI / 바이오인포
- **사회적 신호**: 없음
- **선별 사유**: 구조 기반 신약 개발(SBDD)에서 AlphaFold 인터페이스 점수를 필터로 사용할 때 보정 없는 점수가 얼마나 신뢰 가능한지는 실무 핵심 질문 — 신뢰도 점수 보정 방법은 즉시 파이프라인에 통합 가능한 실용적 기여.

---

### [핵심] C3. 동결 단백질 인코더 진단 벤치마크 (A Diagnostic Benchmark of Frozen Protein Encoders)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-14 ~ 15 · **preprint(미동료심사)** (cs.LG 크로스리스트)
- **DOI/링크**: https://arxiv.org/abs/2610.18879
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — q-bio/cs.LG 목록 제목 확인): ESM-2, ProtTrans, ESM-C 등 대규모 사전훈련 단백질 언어 모델(pLM)의 동결(frozen) 표현이 다양한 다운스트림 태스크(기능 예측·구조 특성·상호작용 등)에서 얼마나 유용한지 진단하는 포괄적 벤치마크를 제시하는 것으로 보인다. 인접 논문 esm-bind(ICML 2026)도 유사한 동결 인코더 탐침(probing) 방식을 다룬다.
- **핵심 수치**: 미확인
- **분야 태그**: 단백질 / LLM-bio / 방법론
- **사회적 신호**: 없음
- **선별 사유**: pLM 동결 표현의 '진단' 이라는 틀 — 어떤 생물학적 정보가 frozen representation에 인코딩되어 있고 어떤 것이 빠져 있는지를 정량화하면 fine-tuning 전략 수립과 신약 설계 파이프라인 선택에 직접 참고 가능.

---

### [핵심] C4. 딥러닝 가상 섭동이 밝힌 노화에 따른 유전자 조절 반응 이질성 증가 (Deep learning-based virtual perturbation reveals increasing heterogeneity of gene regulatory responses with aging)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-14 · **preprint(미동료심사)** (q-bio.MN, q-bio.GN 크로스리스트)
- **DOI/링크**: https://arxiv.org/abs/2610.19029
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — arXiv q-bio.GN 10월 15일 목록 및 검색 스니펫 기반): 단일세포 전사체 데이터에서 딥러닝 모델을 이용해 유전자 가상 섭동(virtual perturbation)을 수행, 노화가 진행될수록 세포 간 유전자 조절 반응의 이질성이 증가한다는 것을 발견. q-bio.MN(분자 네트워크) 분야 주제어로 등록된 것으로 보아 유전자 조절 네트워크(GRN) 모델링과 노화 생물학을 접목한 연구로 보인다.
- **핵심 수치**: 미확인
- **분야 태그**: 유전체 / 바이오인포
- **사회적 신호**: arXiv q-bio.GN 2026-10-14 목록 수록
- **선별 사유**: 노화를 GRN 이질성 증가로 정량화한다는 새로운 프레임 — 항노화 신약 타깃 발굴(개인화된 노화 모듈 역전)에 직접적 기초 연구 함의.

---

### [핵심] C5. OmicsBench: 연구 규모 바이오인포매틱스를 위한 장기간 다회전 AI 에이전트 벤치마크 (OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics)

- **저자/소속**: 저자명 미확인
- **출처**: arXiv · 2026-10-16 (추정) · **preprint(미동료심사)** (cs.AI, q-bio.GN)
- **DOI/링크**: https://arxiv.org/abs/2610.21074
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — 검색 스니펫 기반): 실제 연구 규모 바이오인포매틱스 워크플로우를 모방한 97개 태스크를 방향 비순환 그래프(DAG) 구조로 연결하고, 이를 662개 서브태스크로 분해하여 AI 에이전트의 다회전(multi-turn) 장기간(long-horizon) 실행 능력을 평가하는 OmicsBench를 소개. cs.AI 및 q-bio.GN에 등록된 것으로 보아 실제 오믹스 분석 파이프라인(RNA-seq, 변이 호출, 다중오믹스 통합 등)을 태스크로 포함하는 것으로 추정된다.
- **핵심 수치**: 97 태스크 (DAG 구조), 662 서브태스크 (출처: 검색 스니펫 — 원문 확인 권장)
- **분야 태그**: 바이오인포 / LLM-bio
- **사회적 신호**: 검색 스니펫에서 확인; BixBench3·scBench-Long·BioAgent Bench(ICML 2026) 대비 더 큰 규모·다회전 설계로 소개됨
- **선별 사유**: BixBench(17% 정답률), BioAgent Bench(ICML 2026) 이후 바이오인포 에이전트 평가의 복잡도를 한 단계 높인 벤치마크 — LLM 기반 자동 분석 파이프라인의 실용화 수준을 가늠하는 기준선으로 활용 가능.

---

## 🔭 와이드 (Wide)

### [와이드] W1. 인간과 7개 모델 생물에 걸친 게놈 단위 기능 요소 구성의 균질성과 이질성 (Homogeneity and heterogeneity of functional element composition of genome units across human and seven model organisms)

- **arXiv/DOI**: https://arxiv.org/abs/2610.15182
- **저자**: 저자명 미확인
- **날짜**: 2026-10-13
- **상태**: preprint(미동료심사) (q-bio.GN)
- **한 줄 요약** (초록 미확인 — q-bio.GN 목록 제목 확인): 인간, 마우스, 제브라피시 등 7개 모델 생물의 게놈 단위(유전자 좌위·염색체 구간 등) 안에서 프로모터·인핸서·코딩 서열 등 기능적 요소의 구성 비율이 어느 정도 균질(homogeneous)하거나 이질적(heterogeneous)인지 비교 분석.
- **와이드 선택 사유**: 종간 기능 요소 보존/분기 패턴은 범종 게놈 파운데이션 모델(BacLM, Nucleotide Transformer 등) 설계와 전이 학습 가능성을 이해하는 배경 지식으로 유용.

---

### [와이드] W2. 보지 못한 과학적 상호작용 예측을 위한 조건부 플로우 모델 (Conditional flow models for predicting unseen scientific interactions)

- **arXiv/DOI**: https://arxiv.org/abs/2610.20288
- **저자**: 저자명 미확인
- **날짜**: 2026-10-14
- **상태**: preprint(미동료심사) (cs.LG 크로스리스트, q-bio.GN)
- **한 줄 요약** (초록 미확인 — q-bio.GN 2026-10-14 목록 스니펫 기반): 훈련 중 보지 못한(unseen) 과학적 상호작용(약물-유전자, 단백질-리간드 등으로 추정)을 조건부 플로우 매칭(conditional flow matching)으로 예측하는 방법론을 제안하는 것으로 보인다. cs.LG에서 q-bio.GN으로 크로스리스트된 것으로 보아 단일세포 또는 게놈 맥락에서의 out-of-distribution 상호작용 예측이 응용 타깃인 것으로 추정.
- **와이드 선택 사유**: 분포 외(OOD) 상호작용 예측은 신약 개발(새로운 약물-표적 조합 탐색)과 단일세포 섭동 연구(미측정 처리 조합 예측) 모두에 중요한 방법론적 도전 과제.
