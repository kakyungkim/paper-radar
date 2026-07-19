# 2026-W29 논문 수집 (2026-07-14 ~ 2026-07-19)
수집일: 2026-07-19 | 수집자: paper-scout

## 소스별 수집 건수
- Nature Communications (peer-reviewed): 1편
- arXiv (preprint): 5편 (핵심 4 + 와이드 1)
- 모델 릴리스: 1편 (와이드)
- 합계: 핵심 5편 + 와이드 2편 = 7편

---

## 핵심 (Core 5)

### 1. 공간 유전자 지도화를 통한 단일세포 생물학 비전 파운데이션 모델 (A vision foundation model for single-cell biology via spatial gene cartography)
- **저자**: Ridvan Yesiloglu, Sakib Mostafa, James Zou 외 | Stanford University (Adeli, Islam, Alizadeh, Wu, Xing 등)
- **출처**: arXiv (cs.LG / q-bio)
- **날짜**: 2026-07-15
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2607.14163
- **원문 링크**: https://arxiv.org/abs/2607.14163
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: 없음
- **한 줄 요약**: 유전자를 언어 토큰이 아니라 2D 이미지 픽셀로 표현하는 새로운 패러다임으로, 최적전달(optimal transport)로 공발현 유전자를 공간적으로 인접하게 배치한 뒤 비전 트랜스포머(ViT)와 마스크 이미지 모델링으로 7200만 인간 세포를 사전학습하여 6개 보류 연구에서 zero-shot SOTA를 달성한다.
- **핵심 수치**: 6개 독립 보류 연구(held-out study)에서 zero-shot 세포유형 주석 및 유전자 프로그램 발굴 모두 기존 파운데이션 모델·고전 기준선 대비 최고 성능 — 초록 기준, 구체적 수치 미확인
- **선택 이유**: 단일세포 전사체 분석에 비전 트랜스포머를 최초로 파운데이션 모델 규모로 적용한 논문. 언어 모델 방식(유전자 토큰화)의 한계를 이미지 기반 접근으로 극복하며, zero-shot 일반화 성능이 기존 방법을 전방위 앞선다는 주장이 재현 가능성과 함께 주목받는다.
- **분야 태그**: LLM-bio / 유전체 / 단일세포

---

### 2. 인간 유전자 조절의 컨텍스트 인식 서열-기능 모델 (Context-aware sequence-to-function model of human gene regulation)
- **저자**: Ekin Deniz Aksu, Martin Vingron | Max Planck Institute for Molecular Genetics
- **출처**: Nature Communications Vol. 17, Art. 6200
- **날짜**: 2026-07-14
- **상태**: peer-reviewed
- **arXiv ID / DOI**: 10.1038/s41467-026-75527-2
- **원문 링크**: https://www.nature.com/articles/s41467-026-75527-2
- **코드/데이터**: https://github.com/ekinda/corgi
- **사회적 신호**: 없음
- **한 줄 요약**: DNA 서열에 트랜스-조절 인자(trans-regulator) 발현 벡터를 두 번째 입력으로 결합해, 보류된 세포유형에서도 크로마틴 접근성·히스톤 변형·유전자 발현 신호를 예측하는 Corgi를 제시하며, 확장 모델 Corgi+는 RNA-seq만으로 후성유전체 트랙을 대체(imputation)하는 SOTA를 달성한다.
- **핵심 수치**: Corgi+가 RNA-seq 입력만으로 후성유전체 트랙 imputation에서 기존 최고 성능(state-of-the-art) 달성; 보류 세포유형 일반화 확인 — 초록 기준, 구체적 수치 미확인
- **선택 이유**: 기존 서열-기능 모델이 고정 세포유형에 묶인 문제를 트랜스 조절 컨텍스트 통합으로 해결. 코드가 공개되어 RNA-seq 데이터를 가진 연구자가 즉시 후성유전체 신호를 예측·분석할 수 있다. 동료심사 완료(Nature Communications) 논문으로 신뢰도가 높다.
- **분야 태그**: 바이오인포 / 유전체

---

### 3. 멀티모달 공간 오믹스 통합을 위한 그래프 자기지도 학습 (LATTICE: Graph Self-Supervised Learning for Multimodal Spatial Omics Integration)
- **저자**: Jagan Mohan Reddy Dwarampudi, Veena Kochat, Suresh Satpati, Kunal Rai, Tania Banerjee | University of Houston + MD Anderson Cancer Center
- **출처**: arXiv (cs.LG / q-bio)
- **날짜**: 2026-07-15
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2607.14410
- **원문 링크**: https://arxiv.org/abs/2607.14410
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: 없음
- **한 줄 요약**: Visium RNA·scMultiome RNA·scMultiome ATAC·공간 ATAC·공간 CUT&Tag 5가지 모달리티를 단일 스팟 수준에서 동시에 통합하기 위해, 공간 인접 그래프 위에서 TransformerConv 인코더를 마스크 재구성·교차 모달 정렬·공간 평활도 목적함수로 학습하는 LATTICE 프레임워크를 제안한다.
- **핵심 수치**: 구체적 벤치마크 수치 미확인 — 초록 기준
- **선택 이유**: 공간 전사체와 공간 후성유전체를 동시에 통합하는 자기지도 그래프 방법론을 MD Anderson-Houston 협업이 제시. 공간 멀티오믹스 5가지 모달리티를 한 틀 안에 다루는 접근법은 드물어 방법론적 신규성이 있다.
- **분야 태그**: 바이오인포 / 멀티오믹스

---

### 4. Evo 2 프로브를 이용한 메타게노믹 데이터의 생물안전 특성 스크리닝 (Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes)
- **저자**: Guntoro 외 | AIxBio Hackathon 2026 참가팀
- **출처**: arXiv (q-bio / cs.LG)
- **날짜**: 2026-07-15
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2607.14070
- **원문 링크**: https://arxiv.org/abs/2607.14070
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: 없음
- **한 줄 요약**: 게놈 파운데이션 모델 Evo 2의 26번째 레이어 활성화를 동결(frozen)한 채 선형 프로브와 어텐션 프로브로 항생제 내성(AMR) 및 독성 인자를 탐지하고, AMR 어텐션 프로브 ROC-AUC 0.977, 독성 인자 탐지 ROC-AUC 0.833을 보고한다.
- **핵심 수치**: AMR 선형 프로브 ROC-AUC 0.888 / AMR 어텐션 프로브 ROC-AUC 0.977 / 독성 인자 탐지 ROC-AUC 0.833 — 초록 기준
- **선택 이유**: Evo 2 파운데이션 모델을 생물안전 스크리닝 문제에 직접 적용한 첫 사례로, 파인튜닝 없이 프로빙만으로 높은 탐지 성능을 보인다는 점이 주목할 만하다. 메타게노믹 파이프라인에 Evo 2 임베딩을 활용하려는 연구자에게 실용적 레퍼런스.
- **분야 태그**: 유전체 / LLM-bio

---

### 5. 인간 세포의 방사선 반응 메커니즘에 대한 인과 발견 (Causal Discovery of Radiation Response Mechanisms in Human Cells)
- **저자**: Ashka Shah, Rick Stevens | University of Chicago
- **출처**: arXiv (q-bio / cs.LG)
- **날짜**: 2026-07-15
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2607.13994
- **원문 링크**: https://arxiv.org/abs/2607.13994
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: 없음
- **한 줄 요약**: 방사선 조사와 유전자 발현 데이터를 결합해 인과 발견 알고리즘을 적용함으로써, 방향성 유전자 조절 네트워크를 복원하고 알려진 방사선 반응 경로(pathway)가 네트워크에서 유의하게 농축됨을 보인다.
- **핵심 수치**: 방사선 반응 관련 알려진 경로의 네트워크 농축(enrichment) 확인 — 초록 기준, 정량 수치 미확인
- **선택 이유**: 방사선 반응의 인과 구조를 관찰 유전자 발현에서 복원하는 시도로, 단순 상관 분석을 넘어 방향성 있는 조절망을 제시. Rick Stevens(Argonne/UChicago, 계산과학 분야 저명 연구자) 공저로 방법론적 신뢰도가 있다.
- **분야 태그**: 유전체 / 바이오인포

---

## 와이드 (Wide 2)

### W1. Inkling: 오픈웨이트 975B 멀티모달 MoE 모델 릴리스
- **저자/소속**: Thinking Machines Lab (창업자: Mira Murati 전 OpenAI CTO)
- **출처**: 모델 릴리스 (기술 블로그 + 모델 카드)
- **날짜**: 2026-07-15
- **상태**: 모델 릴리스 (동료심사 없음)
- **arXiv ID / DOI**: 해당 없음
- **원문 링크**: https://thinkingmachines.ai/news/introducing-inkling/ | 모델 카드: https://thinkingmachines.ai/model-card/inkling/
- **코드/데이터**: 가중치 공개 — https://huggingface.co/thinkingmachines (Apache 2.0)
- **사회적 신호**: gHacks, Unite.AI, MarkTechPost, WaveSpeed 등 다수 언론 보도
- **한 줄 요약**: 66층 디코더-온리 트랜스포머, 총 975B 파라미터(활성 41B), 256 전문가(토큰당 6개 라우팅 + 공유 2개), 1M 토큰 컨텍스트, 텍스트·이미지·오디오 멀티모달, 45조 토큰으로 사전학습한 오픈웨이트 MoE 모델.
- **선택 이유**: 이 주에 공개된 가장 큰 오픈웨이트 멀티모달 MoE 모델. Apache 2.0 라이선스로 생물학 도메인 파인튜닝이 가능하며, 대형 오픈웨이트 모델의 생물의학 적용 기준선으로 주목할 만하다.

---

### W2. SEED: 에이전트 강화학습을 위한 자기 진화 온-폴리시 증류 (SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning)
- **저자**: Jinyang Wu, Shuo Yang, Zhengxi Lu, Fan Zhang, Yuhao Shen, Lang Feng, Haoran Luo, Zheng Lian, Shuai Zhang, Zhengqi Wen, Jianhua Tao | Tsinghua University, Zhejiang University, CUHK, NTU, Tongji University
- **출처**: arXiv (cs.LG / cs.AI)
- **날짜**: 2026-07-16
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2607.14777
- **원문 링크**: https://arxiv.org/abs/2607.14777
- **코드/데이터**: https://github.com/jinyangwu/SEED
- **사회적 신호**: 없음
- **한 줄 요약**: LLM 에이전트가 완료된 온-폴리시 궤적에서 재사용 가능한 '힌드사이트 스킬'을 자동 추출·내재화하는 자기 진화 루프를 구성해, 결과 전용 RL 대비 ALFWorld 매크로 성공률을 14.9에서 45.9pp로 끌어올린다.
- **선택 이유**: LLM 에이전트의 자기 개선 훈련 방법론. CellVoyager(W25) 같은 생물학 AI 에이전트에 직접 적용 가능한 일반 프레임워크로, 코드가 공개되어 추적·실험이 용이하다.
