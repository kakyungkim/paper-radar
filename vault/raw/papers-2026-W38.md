---
type: raw-papers
period: 2026-W38
scout-date: 2026-09-20
sources-count:
  arXiv: 8
  bioRxiv: 0
  저널: 0
  total: 8
---

> 수집일: 2026-09-20 | 기간: 2026-09-14~2026-09-20 (W38)
> 핵심 5편 · 와이드 3편 | arXiv(q-bio.GN/q-bio.QM/cs.LG/stat.ML) 8건
> 중복 제외 기준: vault/_meta/recent-papers.jsonl W31~W37 레코드 전체 (doi·arXiv ID 대조)

---

## 핵심 논문 (Core)

### C1. 면역 월드 모델: 다중 스케일 예측 및 치료 가설 생성 (An immune world model for multiscale forecasting and therapeutic hypothesis generation)

- 저자/소속: Taoyong Cui (제1저자), Xi Wang, Zonghang Li, Jinchao Ding, Lingsen You, Yuzhi Xu, Wanghan Xu, Fang Wu, Kejun Ying, Wanli Ouyang, Pheng Ann Heng, Ling Yang, Zhenfei Yin, Yingcheng Wu | PhAI Labs, Inc. (Palo Alto, CA, USA) / The Chinese University of Hong Kong (CUHK)
- 출처: arXiv · 2026-09-13 제출(2026-09-14 공지) · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.14709
- 코드/데이터: 미확인
- 한 줄 요지: 세포·조직·환자 세 층위에서 면역 상태가 개입(치료)에 따라 어떻게 이동하는지를 학습하는 액션 조건부 월드 모델(Immune World Model)을 구성해, 보지 못한 개입·생물학적 맥락으로 일반화하고 IL-36γ와 SIRPα 억제를 보완 축 치료 가설로 지명했다고 주장한다.
- 핵심 수치: 세포 수준·조직 생태계·환자 반응 예측 개선; IL-36γ+SIRPα 병합 억제 가설 도출 (초록 기준, 구체적 정량 지표 미명시 — 본문 확인 필요)
- 분야 태그: 신약AI / 임상ML / LLM-bio
- 사회적 신호: ArXiv AI 研究日報 2026-09-18 게재
- 선별 사유: 면역 개입의 다중 스케일 영향을 단일 모델로 학습해 치료 가설을 직접 도출한다는 접근이 신약 타깃 발굴의 신규 방법론 패러다임을 제안하며, 면역항암제 개발에 직접적 함의를 가짐

---

### C2. 생물학 지식으로 강화된 단일세포 파운데이션 모델 (Towards a knowledge-enhanced single-cell foundation model)

- 저자/소속: Hanqing Zhang (제1저자), Jie Bao, Mei Ma, Shuai Liu, Jiaying Ma, Jiaguan Liu, Jiaxiao Li, Zhenbo Li, Wenwen Gong, Zhijun Cao | 소속 미확인 (초록 기준)
- 출처: arXiv · 2026-09-14 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.14970
- 코드/데이터: https://github.com/BaoJiee/scKITE (공개)
- 한 줄 요지: 세포 주석(cell annotation)과 유전자 조절 정보를 경량 보조 디코더로 학습에 통합한 단일세포 파운데이션 모델(scKITE)이, 기존 대형 모델이 사용하는 학습 샘플의 0.5% 미만(179,067개)으로도 다양한 다운스트림 과제에서 기존 강력한 scFM을 능가한다고 주장한다.
- 핵심 수치: 학습 샘플 수 179,067개 (기존 scFM 대비 <0.5%); 다양한 다운스트림 과제에서 기존 scFM 초과 성능 (초록 기준)
- 분야 태그: 바이오인포 / 단일세포 / LLM-bio
- 사회적 신호: 없음
- 선별 사유: 단일세포 파운데이션 모델의 데이터 효율성 한계를 생물학 지식 주입으로 돌파한 접근이 재현 가능하고(코드 공개), 데이터 부족 상황의 실험실 연구에 직접 적용 가능성을 가짐

---

### C3. 게놈 서열을 위한 맥락적 쌍곡 표현 학습 (HyCoSeq: Contextual Hyperbolic Representation Learning for Genomic Sequences)

- 저자/소속: Chenhao Zeng (제1저자), Zhibin Pu, Shufei Ge | 소속 미확인
- 출처: arXiv · 2026-09-15 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.16925
- 코드/데이터: 미확인
- 한 줄 요지: 기존 쌍곡 게놈 모델의 잔차 경로가 완전한 Lorentz 표현을 직접 집계하지 않는 한계를 보완하기 위해, 가중 Lorentzian 잔차 집계를 다중 곡률 Lorentz 인코딩에 통합하고 양방향 LSTM으로 위치 간 맥락을 학습하는 HyCoSeq를 제안해, 기존 쌍곡 기준선을 능가하고 대규모 사전학습 없이 대형 DNA 언어 모델과 경쟁적 성능을 달성했다고 주장한다.
- 핵심 수치: 기존 쌍곡 기준선 대비 성능 개선; 대규모 사전학습 없이 대형 DNA LM과 경쟁적 성능 달성 (초록 기준, 구체적 수치 미명시 — 본문 확인 필요)
- 분야 태그: 유전체 / 바이오인포
- 사회적 신호: 없음
- 선별 사유: 유전체 서열 표현 학습에 쌍곡 기하학을 효과적으로 통합한 경량 접근으로, 사전학습 비용 없이 대형 모델 수준 성능을 주장한다는 점에서 방법론 파급력이 있음

---

### C4. 소비자용 하드웨어에서의 임상 종양 전장유전체 분석 민주화 (Democratizing Clinical Tumor Whole Genome Sequencing: 18-hour End-to-end Analysis via Trillion-parameter Large Language Models Locally Deployed on Consumer-grade Hardware)

- 저자/소속: Rui Xiao (제1저자), Yili Xu | 소속 미확인 (교신저자 이메일: 22465225@qq.com; 중국 기관 추정)
- 출처: arXiv · ~2026-09-17 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.17620
- 코드/데이터: 미확인
- 한 줄 요지: 조 단위 파라미터 바이오의학 LLM을 소비자용 RTX 4060 노트북(32GB RAM, 8GB VRAM)과 일반 병원 임상 워크스테이션에 완전히 로컬 배포하고, 표준 30X 깊이 종양-정상 WGS 분석을 원시 FASTQ 입력부터 임상 등급 변이 보고서까지 18시간 내에 완료하며 A100 클러스터 파이프라인과 >99.9% 일치율을 달성했다고 주장한다.
- 핵심 수치: 18시간 이내 단일 종양-정상 쌍 WGS 분석; 체세포 변이 검출 F1 99.62%; A100 클러스터 대비 >99.9% 일치율 (초록 기준)
- 분야 태그: 임상ML / 유전체 / LLM-bio
- 사회적 신호: 없음
- 선별 사유: 임상 WGS 분석을 수백만 달러 GPU 클러스터 없이 일반 병원 하드웨어에서 가능하게 만드는 기술적 전환점을 주장하며, 저자원 환경 정밀종양학 접근성과 직접적 임상 함의를 가짐

---

### C5. 약물 재창출 후보 실용적 스크리닝을 위한 사전학습 의료 표현 (Pretrained Medical Representations for the Practical Screening of Drug Repositioning Candidates)

- 저자/소속: Yuhei Fujioka (제1저자), Daitaro Misawa, Shingo Fukuma | 소속 미확인 (초록 기준)
- 출처: arXiv · 2026-09-17 · **preprint(미동료심사)** (ICML 2026 AI for Science Workshop 채택)
- DOI/링크: https://arxiv.org/abs/2609.19865
- 코드/데이터: 미확인
- 한 줄 요지: 전자건강기록(EHR)의 의료 코드 시퀀스에서 계층적 서브토큰 집계, 부분 마스킹, 교차 참조 메커니즘을 통합한 새로운 단일 사전학습 프레임워크를 제안해, 기존 BERT 기반 모델이 포착하지 못했던 의료 코드의 계층 구조와 진단-치료 간 복잡한 상호작용을 학습하여 약물 재창출 가설 발굴에 적용했다고 주장한다.
- 핵심 수치: 약물 재창출 후보 스크리닝 성능 정량 지표 미확인 — 본문 확인 필요 (ICML 2026 AI for Science Workshop 채택)
- 분야 태그: 신약AI / 임상ML / LLM-bio
- 사회적 신호: 없음
- 선별 사유: EHR 기반 표현 학습을 약물 재창출이라는 구체적 신약 개발 과제로 연결한 접근으로, 임상 데이터에서 과학적 가설을 추출하는 방법론의 범위를 확장함

---

## 와이드 논문 (Wide)

> 그 주 화제가 된 핵심 축 밖(또는 주변부) 논문 — 가볍게 한 눈에

---

### W1. 자폐 스펙트럼 장애 근거 기반 스크리닝을 위한 멀티모달 LLM (A multimodal large language model for evidence-based autism spectrum disorder screening)

- 저자/소속: Jun Chen (제1저자), Qi Zhao, Yunliang Jiang 외 | 소속 미확인
- 출처: arXiv · 2026-09-15 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.16464
- 코드/데이터: 미확인
- 한 줄 요지: 영상·음성·대화를 입력받는 이중 분기(결정 분기 + 근거 분기) 구조의 멀티모달 LLM(ASDchat)으로 ADOS-2 임상 기준에 정렬된 타임스탬프 행동 근거 체인과 함께 ASD 스크리닝 확률을 출력한다고 주장한다.
- 핵심 수치: 미확인 (초록 기준, 구체적 성능 수치 확인 필요)
- 분야 태그: 임상ML / 신경발달장애
- 사회적 신호: 없음
- 선별 사유: ASD 진단 병목(전문가 부족, 주관적 도구)을 다중모달 AI로 해결하고 설명 가능성을 강조한 임상 AI 설계 사례로, 핵심 축 밖 임상 진단 AI의 동향으로 주목

---

### W2. 단백질 상호작용 네트워크의 문헌 중심 시각화 도구 v2 (ProLiVis 2.0: Literature-Centric Visualization of Protein-Protein Interaction Networks, with a Citation-Trust Model for Interaction Evidence)

- 저자/소속: Melih Sözdinler (제1저자), Yalçın Doksanbir, Gökhan Akpınar, Ege Aktan | 소속 미확인
- 출처: arXiv · 2026-09-14 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.15236
- 코드/데이터: https://github.com/melihsozdinler/CenterLayout (공개); 브라우저 내 실행, 별도 설치 불필요
- 한 줄 요지: 인용 건수·독립 실험실 수 기반 인용-신뢰 모델(citation-trust model)로 PPI 증거의 신뢰도를 점수화하고, 결정론적 센터 레이아웃 알고리즘으로 단백질 상호작용 네트워크를 웹 브라우저에서 바로 탐색할 수 있게 한 시각화 도구를 제시한다.
- 핵심 수치: 8쪽, 그림 6개 (논문 메타데이터 기준)
- 분야 태그: 바이오인포 / 단백질
- 사회적 신호: 없음
- 선별 사유: PPI 데이터베이스 접근성과 증거 신뢰도 평가를 실용적으로 개선한 도구로, 설치 없이 바로 연구에 활용 가능한 재현성 친화적 인프라

---

### W3. 다양한 세계를 아우르는 예측 모델 학습 프레임워크 (JEPA-Anything: Learning Predictive Models across Different Worlds)

- 저자/소속: Taoyong Cui (제1저자) 외 | PhAI Labs, Inc. / CUHK
- 출처: arXiv · 2026-09-17 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2609.20800
- 코드/데이터: GitHub 공개 (링크 미확인)
- 한 줄 요지: 직교 예측 분해(Orthogonal Predictive Factorization)를 기반으로 시각·생물학·임상 궤적·제어·분자 동역학·물리장·기상 등 7개 도메인에 걸쳐 단일 공통 학습 원리로 월드 모델을 학습하는 JEPA-Anything 프레임워크를 제안한다.
- 핵심 수치: 7개 도메인, 10개 매칭 동역학 과제, 1,000개 이상 임상 사건 예측, 분자 동역학 100스텝 롤아웃 (초록 기준)
- 분야 태그: 방법론 / LLM
- 사회적 신호: HuggingFace Daily Papers 등재 (2026-09-17 기준); AkihikoWatanabe paper_notes 기록
- 선별 사유: 단일 모델로 생물학·임상·분자 동역학 도메인을 포괄하는 범용 월드 모델 접근법으로, 향후 생물학 파운데이션 모델 설계에 영향을 줄 수 있는 방법론적 화제작
