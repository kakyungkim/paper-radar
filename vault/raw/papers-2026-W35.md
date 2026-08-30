---
type: raw
week: 2026-W35
date_range: 2026-08-24 ~ 2026-08-30
scout_date: 2026-08-30
sources: [arXiv (q-bio.QM, q-bio.GN, cs.LG), bioRxiv, Web search (Google, papers.cool, alphaXiv)]
소스별 건수: arXiv 4편, bioRxiv 2편
---

# Paper Scout Raw — 2026-W35

> **Dedup 기준 사전 확인**: `vault/_meta/recent-papers.jsonl` W31-W34 기록 대조 완료.
> 제외 arXiv ID: 2608.17381 · 2608.19304 · 2608.06022 · 2608.19902 (W34 수집본).
> bioRxiv 직접 접근 차단 환경에서 수집 — 일부 DOI는 웹검색 기반 확인이며 "(웹검색 확인)"으로 명시.

---

## 핵심 논문 (Core) — 5편

---

### [C1] arXiv:2608.26208

- **제목**: Learning Interpretable Tumor Microenvironment Representations by Fitting Pan-Cancer Cell State-Niche Correlation (암 종양 미세환경의 세포 상태-니치 상관관계를 이용한 해석 가능한 표현 학습)
- **저자/소속**: Xiao Xiao (Yale University), Jiashu He (University of Pennsylvania), Shiyang Zhang (Yale University), Meiyi Mao (University of Michigan, Ann Arbor)
- **출처**: arXiv (q-bio.QM) · 2026-08-26 제출 · **preprint (미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.26208
- **코드/데이터**: 미공개 (언급 없음 — 원문 확인 시 재검토 권장)
- **한 줄 요지**: GITIII-scale은 공간 전사체와 단일세포 RNA-seq를 통합해 암종 미분류 데이터에서도 세포 상태-니치(cell state-niche) 상관관계를 해석 가능하게 포착하는 팬-암 계층적 그래프 트랜스포머 기반 종양 미세환경(TME) 파운데이션 모델이다.
- **핵심 수치**: 팬-암 데이터베이스(영상 기반 공간 전사체 + scRNA-seq 매칭 데이터셋) 학습; 학습 시 미노출 암종에서 기존 공간 전사체 파운데이션 모델 대비 니치 관련 상태 변화 포착 정확도 우수 (초록 기반, 구체적 수치 원문 확인 필요)
- **분야 태그**: 유전체 / 임상ML / 신약AI (TME-기반 약물 표적 발굴)
- **검증 수준**: in silico — 팬-암 벤치마크 (훈련 외 암종 포함)
- **사회적 신호**: 없음 (검색 기준)
- **선별 사유**: 공간 전사체 파운데이션 모델을 TME 해석에 특화한 최신 시도; 세포-세포 상호작용 기반 약물 표적 발굴에 직접 연결되며, 임상·산업 양면 함의가 뚜렷함

---

### [C2] arXiv:2608.23722

- **제목**: Optimizing RNA yield using deep neural networks coupled to massively parallel screening (대규모 병렬 스크리닝과 결합한 딥러닝 기반 RNA 생산량 최적화)
- **저자/소속**: Dinghai Zheng, Justin Hong, Jun Wang, Adrien Villain, Mickaël Costallat, Fernando Ulloa Montoya, Vikram Agarwal (소속: 원문 확인 필요; mRNA 치료제 분야 산업 연구진 추정)
- **출처**: arXiv · 2026-08-24 제출 · **preprint (미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.23722
- **코드/데이터**: 미공개 (언급 없음)
- **한 줄 요지**: 10만 개 무작위 올리고뉴클레오타이드 서열 라이브러리의 시험관 전사(IVT) RNA 생산량을 NGS로 대규모 측정하고, CNN 기반 딥러닝 모델로 생산량을 예측해 신규 mRNA 서열 설계 후보를 사전 선별할 수 있음을 보인다.
- **핵심 수치**: 보류 테스트 세트에서 예측-실측 Pearson 상관계수 0.94; 서열 라이브러리 규모 10^5개 (초록 기반)
- **분야 태그**: 신약AI / 바이오인포 (mRNA 치료제 제조 최적화)
- **검증 수준**: in silico — 보류(held-out) 테스트 세트 검증
- **사회적 신호**: 없음 (검색 기준)
- **선별 사유**: mRNA 백신·단백질 대체 요법·면역항암제 제조의 핵심 병목인 IVT 수율을 딥러닝으로 해결; 재현성 높은 대규모 스크리닝-딥러닝 파이프라인으로 산업 함의 명확

---

### [C3] bioRxiv 10.64898/2026.08.27.747499

- **제목**: Perturb-seq identifies co-regulated gene programs shaping hematopoietic stem and progenitor cell function (Perturb-seq으로 조혈줄기세포·전구세포 기능을 형성하는 공동 조절 유전자 프로그램 규명)
- **저자/소속**: Joseph S Bowness, Aina Bernal Martinez, Jan Barinka, Jonas Schulte-Schrepping, Simon Renders, Alexander Waclawiczek, Aino-Maija Leppa, Andreas Trumpp, Simon Raffel, Simon Haas, Lars Velten (Centre for Genomic Regulation, Barcelona; 독일·핀란드 기관 포함 다국적 컨소시엄)
- **출처**: bioRxiv · 2026-08-27 제출 · **preprint (미동료심사)**
- **DOI/링크**: https://doi.org/10.64898/2026.08.27.747499 (웹검색 확인)
- **코드/데이터**: 미확인 (원문 접근 불가 환경)
- **한 줄 요지**: 인간 조혈줄기·전구세포(HSPC)에 Perturb-seq을 적용해, 단일 유전자 교란이 복수의 공동 조절 유전자 프로그램을 통해 HSPC 기능에 영향을 미친다는 것을 단일세포 해상도로 규명한다.
- **핵심 수치**: 초록 원문 확인 필요 (bioRxiv 직접 접근 차단 환경)
- **분야 태그**: 유전체 / 단일세포 (조혈줄기세포 기능유전체)
- **검증 수준**: ex vivo (인간 HSPC 실험) + 단일세포 전사체 분석
- **사회적 신호**: 없음 (검색 기준)
- **선별 사유**: Lars Velten 연구실의 기능유전체 연구; Perturb-seq × HSPC 조합은 조혈계 신약 타깃 발굴(혈액암, 유전자 치료)에 직결되며 방법적·임상적 함의가 뚜렷함

---

### [C4] bioRxiv 10.64898/2026.08.26.747213

- **제목**: SALRR: Scalable Analysis of Long-Read RNA-Seq Enables Comprehensive Transcriptome Profiling in Human Brain (장독취 RNA-seq 확장 분석으로 인간 뇌 전사체 전면 프로파일링 가능)
- **저자/소속**: Cedric Kouam, Jackson Mingle, Pilar Alvarez Jerez, Allison Evans, Abraham Moller, Mina Ryten, Fritz Sedlazeck, Luigi Ferrucci 등 다수 (다기관 컨소시엄 — 소속 상세 원문 확인 필요)
- **출처**: bioRxiv · 2026-08-26 제출 · **preprint (미동료심사)**
- **DOI/링크**: https://doi.org/10.64898/2026.08.26.747213 (웹검색 확인; 동일 DOI 문헌 2건 검색됨 — 원문에서 확정 권장)
- **코드/데이터**: 미확인 (원문 접근 불가 환경; SALRR 파이프라인 공개 여부 원문 확인 필요)
- **한 줄 요지**: 인간 뇌 장독취(long-read) RNA-seq 데이터의 대규모 분석을 위한 확장 가능한 파이프라인 SALRR을 개발해, 인간 뇌 전사체의 포괄적인 이소폼(isoform) 프로파일링을 수행했다.
- **핵심 수치**: 원문 확인 필요 (bioRxiv 직접 접근 불가)
- **분야 태그**: 바이오인포 / 유전체 (뇌 전사체)
- **검증 수준**: in silico (대규모 시퀀싱 데이터 분석)
- **사회적 신호**: 없음 (검색 기준)
- **선별 사유**: 뇌 전사체 장독취 시퀀싱의 확장성 문제를 직접 해결하는 파이프라인 논문; 신경질환(파킨슨병 등) 전사체 연구의 기반 도구로 활용 가치 높음. DOI 충돌 가능성 명시.

---

### [C5] arXiv:2608.22642

- **제목**: Mol-JEPA: A Multimodal Joint Embedding Predictive Architecture for Molecules (다중 모달 JEPA 기반 분자 표현 학습)
- **저자/소속**: Florian Rottach, Sebastian Schieferdecker (University of Tübingen; Boehringer Ingelheim), William Rudman (The University of Texas at Austin), Randall Balestriero (Brown University), Carsten Eickhoff (University of Tübingen)
- **출처**: arXiv (cs.LG / q-bio.BM) · 2026-08-23 제출 · **preprint (미동료심사)**
  - *참고: arXiv 제출일 08-23은 W34 마지막 날. W34 수집에 미포함된 논문이므로 W35에 편입.*
- **DOI/링크**: https://arxiv.org/abs/2608.22642
- **코드/데이터**: 미공개 (언급 없음 — papers.cool, alphaXiv 확인)
- **한 줄 요지**: JEPA(Joint Embedding Predictive Architecture) 프레임워크를 분자 표현 학습에 적용해, 분자 구조·세포 표현형·결합 친화도·ADMET 프로파일·양자화학 시뮬레이션 등 다중 모달리티를 모달리티 마스킹(modality masking)으로 통합 학습한다.
- **핵심 수치**: 복수 드러그디스커버리 벤치마크에서 강한 성능 보고 (구체적 수치 원문 확인 필요)
- **분야 태그**: 신약AI / LLM-bio (분자 파운데이션 모델)
- **검증 수준**: in silico (벤치마크 평가)
- **사회적 신호**: alphaXiv 등재 확인; HF Daily Papers 여부 미확인
- **선별 사유**: Boehringer Ingelheim 등 제약산업 기관 참여; JEPA 아키텍처의 분자 도메인 적용은 기존 대비 모달리티 붕괴·화학적 비유효 증강 문제를 해결하려는 신선한 접근

---

## 와이드 논문 (Wide Angle) — 2편

---

### [W1] arXiv:2608.25286

- **제목**: BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks (연구 논문 수준 생물정보학 과제에서 AI 에이전트 성능 평가)
- **저자/소속**: Edison Scientific / FutureHouse 팀 (다수 저자, 소속 원문 확인 필요)
- **출처**: arXiv · 2026-08-26 제출 · **preprint (미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.25286
- **코드/데이터**: https://huggingface.co/datasets/EdisonScientific/BixBench3 (HuggingFace 공개 데이터셋)
- **한 줄 요지**: 17개 분석 유형·9개 과학 도메인에 걸친 20편 실제 출판 논문의 원시 데이터 → 분석 아티팩트 재현 과제로 13개 최전선 LLM의 생물정보학 연구 수준 수행 능력을 평가한다.
- **핵심 수치**: 가장 높은 점수 GPT 5.6 Sol: 0.48 / 최저 Gemini 3.1 Flash Lite: 0.0; 평균 시도당 6.8시간, 약 $43 비용, 1억 토큰 처리 (초록 기반)
- **분야 태그**: AI에이전트 / 바이오인포 (LLM 에이전트 평가)
- **사회적 신호**: FutureHouse 공식 블로그 발표; Bio-IT World 보도
- **선별 사유**: AI 에이전트가 연구 수준 계산생물학 과제를 얼마나 수행할 수 있는지 정량화한 첫 대규모 평가; 연구 자동화·R&D 생산성 논의와 직결

---

### [W2] arXiv:2608.27351

- **제목**: Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO (LLM 추론을 위한 진화전략 이해: GRPO보다 넓은 추론 커버리지)
- **저자/소속**: Yunpeng Ba, Zhi Zheng, Yue Xie, Jiaqing Li, Xialiang Tong, Tao Zhong, Mingxuan Yuan, Zhichao Lu, Xuyang Wu, Zhenkun Wang (다수 산업·학계 기관 — 소속 원문 확인 필요)
- **출처**: arXiv (cs.LG) · 2026-08-24 제출 · **preprint (미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.27351
- **코드/데이터**: 미확인
- **한 줄 요지**: LLM 사후 훈련에서 진화전략(Evolution Strategies)이 현재 주류인 GRPO 대비 더 넓은 추론 커버리지를 제공한다는 이론·실험적 분석을 제시한다.
- **분야 태그**: 방법론 (LLM 사후 훈련) / AI일반
- **사회적 신호**: 없음 (검색 기준)
- **선별 사유**: 생물의학 LLM fine-tuning(단백질·게놈·임상 도메인) 방법론 선택에 직접 닿는 사후 훈련 기법 비교; GRPO 대안 탐색에 관심 있는 독자에게 유용

---

## Dedup 체크 노트

- W31~W34 arXiv·DOI 전체 대조 완료. 금주 수집 5편+2편 모두 dedup 목록 미존재 확인.
- **C5 Mol-JEPA (2608.22642)**: 제출일 2026-08-23은 W34 날짜 경계. W34 수집(scout_date 2026-08-23)에 미포함된 논문이므로 W35에 편입 처리.
- **C4 SALRR DOI 충돌 주의**: 웹검색에서 동일 DOI(10.64898/2026.08.26.747213)를 서로 다른 두 논문(SALRR / MOSurvivor-CpG)에 귀속하는 결과가 1건 포착됨. bioRxiv 직접 접근 불가 환경에서 복수 검색으로 SALRR을 주 귀속 논문으로 판정했으나, 다음 큐레이션 시 원문 확인 권장.
- **Nature Medicine LiON (s41591-026-04589-y)**: 출판일 2026-08-19(W34) — W35 기간 미디어 보도(Xinhua 2026-08-25)가 있었으나, 출판 주 기준 W34에 해당하므로 이번 수집에서 제외. 차주 W34 누락 논문 보강 필요 여부는 knowledge-curator가 판단.
- **arXiv:2608.11475 (Boltz-1 경계 분석)**: 2026-08-11 제출로 W33 해당. W35 미수집 대상.
