# 2026-W25 주간 논문 수집 (2026-06-16 ~ 2026-06-22)

**수집일**: 2026-06-21
**수집 주차**: 2026-W25
**중복 확인**: `vault/_meta/recent-papers.jsonl` 확인 완료 — W24 5편(2606.12219, 2606.12838, 2606.11876, 2606.11382, 2606.11508) 제외

## 소스별 건수 요약

| 소스 | 건수 |
|------|------|
| arXiv (q-bio / cs.LG / cs.AI) | 6편 |
| Nature Methods (peer-reviewed) | 1편 |
| **합계** | **7편 (핵심 5 + 와이드 2)** |

---

## 핵심 논문 (5편)

### [핵심] scGTN: 단일세포 RNA 시퀀싱 클러스터링을 위한 샴 그래프 트랜스포머 네트워크 (scGTN: Deep Siamese Graph Transformer Network for Single-cell RNA Sequencing Clustering)
- 저자/소속: Jinke Wu, Yifan Wang, Siyu Yi, Caiyang Yu, Ziyue Qiao, Nan Yin, Jiancheng Lv, Wei Ju | Sichuan University, University of International Business and Economics, Great Bay University, The Education University of Hong Kong
- 출처: arXiv (q-bio.GN, cs.LG) · 2026-06-17 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.18672
- 코드/데이터: 미확인 (논문 내 코드 URL 명시 예고, 접근 미확인)
- 사회적 신호: 없음
- 한 줄 요지: scRNA-seq 데이터의 희소성·잡음과 세포 간 구조 정보를 동시에 통합하는 샴 그래프 트랜스포머 네트워크(scGTN)로 세포 유형 클러스터링을 수행한다.
- 핵심 수치: 미기재 (초록 기준 구체적 수치 없음; 논문 본문 접근 미확인)
- 분야 태그: 유전체 / 단일세포 / LLM-bio
- 선별 사유: W25 기간 제출(6월 17일) 단일세포 클러스터링 신규 방법론. 세포 간 그래프 구조를 명시적으로 통합한 트랜스포머 아키텍처로 멀티오믹스 세포 유형 분류 파이프라인에 적용 가능

---

### [핵심] 멀티모달 암 분석을 위한 파운데이션 모델 표현의 체계적 평가 (Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis)
- 저자/소속: Jingyu Hu, Giuseppe Tripodi, Reed Naidoo, Sarah F. McGough, Tapabrata Chakraborti | 소속 미명기
- 출처: arXiv (cs.CV, cs.LG) · 2026-06-15 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.17115
- 코드/데이터: 공개 안 됨/미확인
- 사회적 신호: 없음
- 한 줄 요지: 실세계 상업 종양 코호트(유방암 IH-BC, 비소세포폐암 IH-NSCLC)에서 전체 슬라이드 이미지(WSI)와 전사체 프로파일을 활용해 파운데이션 모델 표현의 일반화·융합·신뢰성을 8개 하위 분류 과제에서 체계적으로 벤치마킹한다.
- 핵심 수치: 8개 하위 분류 과제에서 평가; 세 가지 이미지-오믹스 융합 전략 비교 (구체적 AUC/정확도 수치는 초록 기준 미기재)
- 분야 태그: 임상ML / 신약AI / 유전체 / LLM-bio
- 선별 사유: 분포 이동 하 파운데이션 모델 일반화라는 핵심 임상 배포 문제를 실제 상업 코호트로 검증. 병리+전사체 멀티모달 암 분석의 현실적 한계 파악에 직결

---

### [핵심] 공정한 예후 예측을 위한 그룹 조건부 C-지수 (Towards Fair Predictions: Group Conditional Concordance Index to Quantify Fairness in Time-to-Event Prognostication)
- 저자/소속: Haoyuan Wang 외 5인 | 소속 미명기
- 출처: arXiv (stat.ML, cs.LG) · 2026-06-15 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.16872
- 코드/데이터: 공개 안 됨/미확인
- 사회적 신호: 없음
- 한 줄 요지: Harrell C-지수를 그룹 조건부로 확장한 xCI를 제안하고, Framingham·MESA·ARIC 코호트 및 Truveta 대규모 EHR 데이터베이스에서 심혈관 질환 위험 예측 모델의 인구통계 집단 간 공정성 편향을 감지한다.
- 핵심 수치: Framingham Offspring, MESA, ARIC 조화 데이터 및 Truveta EHR 두 케이스 스터디; xCI가 기존 C-지수로 놓친 그룹 간 편향 식별 (구체적 수치는 초록 기준 미기재)
- 분야 태그: 임상ML / 공정성 / 바이오마커
- 선별 사유: 생존 분석 공정성을 계량화하는 새 지표 제안. 임상 ML 모델의 규제 심사 및 의료 형평성 연구에 직접 활용 가능

---

### [핵심] 임상 EHR 질의응답에서 트랜스포머의 합성 추론 한계 실증 (Compositional Reasoning Depth Predicts Clinical AI Failure: Empirical Evidence Consistent with Transformer Compositionality Limits in Electronic Health Record Question Answering)
- 저자/소속: Sanjay Basu | UCSF Department of Medicine
- 출처: arXiv (cs.AI, cs.CL) · 2026-06-15 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.16890
- 코드/데이터: 공개 안 됨/미확인
- 사회적 신호: 없음
- 한 줄 요지: 임상 EHR 질의에서 추론 단계 수(hop count)가 많을수록 대형 언어 모델 정확도가 단조 감소함을 실증하며, Claude Sonnet·GPT-4o·GPT-5 세 모델에서 모두 재현된다.
- 핵심 수치: 313개 MedAlign EHR 질의응답 쌍; hop=1에서 Claude Sonnet 정확도 30.6%, hop=4에서 17.6%로 단조 감소; GPT 모델 두 세대에서도 동일 패턴 확인
- 분야 태그: 임상ML / LLM-bio
- 선별 사유: 임상 LLM의 구조적 실패 원인을 multi-hop 추론 한계로 정량화한 최초 실증. 임상 AI 도입 시 안전성 평가 지표로 즉시 활용 가능

---

### [핵심] 임상 생존 분석을 위한 테이블 파운데이션 모델의 생존 적응 (Tabular Foundation Models for Clinical Survival Analysis via Survival-Aware Adaptation)
- 저자/소속: Minh-Khoi Pham 외 | 소속 미명기
- 출처: arXiv (cs.LG, stat.ML) · 2026-06-10 · **preprint(미동료심사)** | AIiH 2026 게재 승인
- DOI/링크: https://arxiv.org/abs/2606.12006
- 코드/데이터: 공개 안 됨/미확인
- 사회적 신호: 없음
- 한 줄 요지: TabPFN·TabDPT·TabICL 등 범용 테이블 파운데이션 모델에 다중과제 로지스틱 회귀(MTLR) 헤드를 결합해 임상 생존 분석에 적용하고, MIMIC-IV·eICU 두 대규모 ICU 코호트에서 검증한다.
- 핵심 수치: MIMIC-IV에서 TabDPT-FT-MTLR C-지수 0.856 (DeepSurv 대비 +1.4%); eICU에서 TabICL-FT-MTLR C-지수 0.797
- 분야 태그: 임상ML / LLM-bio
- 선별 사유: 범용 테이블 FM을 임상 생존 분석에 이식하는 경량 적응 레시피 제시. W24 미수집 논문으로 AIiH 2026 게재 확정이며 MIMIC-IV·eICU 대규모 검증 포함

---

## 와이드 논문 (2편)

### [와이드] CellVoyager: AI 계산생물학 에이전트의 자율적 단일세포 데이터 분석 (CellVoyager: AI CompBio Agent Generates New Insights by Autonomously Analyzing Biological Data)
- 저자/소속: Alber, S., Chen, B., Sun, E. 외 | 소속 미명기
- 출처: Nature Methods · 2026 (vol. 23, pp. 749-759) · **peer-reviewed**
- DOI/링크: https://doi.org/10.1038/s41592-026-03029-6
- 코드/데이터: 미확인 (Nature Methods 출판, 원문 접근 필요)
- 사회적 신호: Nature Methods 게재; RNA-Seq Blog 외 다수 언론 보도
- 한 줄 요지: LLM 기반 AI 에이전트가 scRNA-seq 데이터셋을 자율 탐색하며 수행 이력을 참조해 새 분석 파이프라인을 생성·실행하고, 코로나19·세포 간 소통·노화 주제에서 전문가 평가 기준 창의적·과학적으로 타당한 신규 발견을 생성한다.
- 핵심 수치: GPT-4o 및 o3-mini 대비 논문 저자가 실제로 수행한 분석 예측 정확도 최대 +23%; 3개 케이스 스터디에서 전문가가 '창의적·과학적 타당' 평가
- 분야 태그: LLM-bio / 단일세포 / 유전체
- 선별 사유: AI 에이전트가 자율적으로 생물학적 가설을 생성·검증하는 첫 Nature Methods 동료심사 사례. 컴퓨터 생물학 연구 자동화의 실용적 이정표

---

### [와이드] BioHarness: 문헌·지식베이스·생물학 아틀라스를 아우르는 기질 인식 생의학 질의응답 (BioHarness: Substrate-Aware Evidence Assembly for Biomedical Question Answering across Literature, Knowledge Bases, and Biological Atlases)
- 저자/소속: Meng Xiao 외 | 교신저자: Yuanchun Zhou, Hengshu Zhu
- 출처: arXiv (cs.CL, cs.AI) · 2026-06-17 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.19396
- 코드/데이터: 공개 안 됨/미확인
- 사회적 신호: 없음
- 한 줄 요지: 문헌 검색이 불충분할 때 생의학 지식 도구 호출·아틀라스 기반 구조화 증거 조립으로 단계적 에스컬레이션하는 LLM 하네스로, 예/아니오·다지선다·사실·목록·요약·발현 6개 질문 유형을 통합 지원한다.
- 핵심 수치: 미기재 (초록 기준 구체적 벤치마크 수치 없음)
- 분야 태그: LLM-bio / 임상ML
- 선별 사유: 생의학 RAG(검색 증강 생성)에서 지식베이스·아틀라스 기반 증거를 계층적으로 조립하는 새 아키텍처. 유전체·오믹스 데이터 기반 임상 의사결정 지원 시스템 설계와 직결
