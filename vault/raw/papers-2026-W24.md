# 2026-W24 주간 논문 수집 (2026-06-09 ~ 2026-06-15)

**수집일**: 2026-06-14
**수집 주차**: 2026-W24
**중복 확인**: `vault/_meta/recent-papers.jsonl` 확인 완료 — 기존 기록 없음 (첫 실행)

## 소스별 건수 요약

| 소스 | 건수 |
|------|------|
| arXiv (q-bio / cs.LG / cs.AI) | 7편 |
| bioRxiv | 1편 |
| Nature Biomedical Engineering (peer-reviewed) | 1편 |
| **합계** | **9편 (핵심 5 + 와이드 4)** |

---

## 핵심 논문 (5편)

### [핵심] m6A-FORM: N6-메틸아데노신 생물학 해독 파운데이션 모델 (m6A-FORM: A Foundation Model for Decoding N6-methyladenosine Biology)
- 저자/소속: Tinghe Zhang, Sumin Jo, Shou-Jiang Gao, Yufei Huang / 소속 미확인
- 출처: arXiv (q-bio.GN, q-bio.MN) · 2026-06-10 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.12219
- 코드/데이터: 공개 안 됨/미확인
- 한 줄 요지: MeRIP-seq 피크를 선행 지식으로 삼아 약 2,200만 서열(143개 연구)을 사전학습한 m6A RNA 변형 예측 파운데이션 모델로, 단일 뉴클레오타이드 수준의 m6A 사이트를 예측한다.
- 핵심 수치: PR-AUC 0.635, ROC-AUC 0.988 (기존 최고 대비 PR-AUC +0.14 이상); 24개 인간 조직에서 보존된 사이트 19,631개 식별; 연관 조절인자 19종 예측
- 분야 태그: 유전체 / LLM-bio / 후성유전체
- 선별 사유: RNA 메틸화(m6A) 특화 파운데이션 모델로 기존 예측기 대비 PR-AUC 대폭 개선, 다중 조직 전사체 응용 가능성 제시

---

### [핵심] OCOO-T: 전사 교란 반응 예측을 위한 단순·확장 가능한 가상 세포 모델 (OCOO-T: A Simple and Scalable Virtual Cell Model for Transcriptional Perturbation Response Prediction)
- 저자/소속: Danning Jiang, Zheming An, Yalong Zhao, Lipeng Lai / 소속 미확인
- 출처: arXiv (q-bio.QM, cs.AI, q-bio.GN) · 2026-06-11 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.12838
- 코드/데이터: 공개 안 됨/미확인
- 한 줄 요지: 흐름 매칭(flow matching) 기반 트랜스포머가 유전적·화학적·사이토카인 교란에 대한 단일 세포 전사 반응을 예측하며, 적응형 정규화와 컨텍스트 토큰으로 세포 유형 특이성을 반영한다.
- 핵심 수치: Tahoe100M, Replogle, PBMC 세 벤치마크에서 경쟁력 있는 성능 보고 (구체적 수치 초록에 미기재)
- 분야 태그: 단일세포 / 가상세포 / 유전체 / LLM-bio
- 선별 사유: 가상 세포(Virtual Cell) 모델의 단순·확장 가능한 구현체로, 약물·유전자 편집 반응 예측 파이프라인 직결 응용 가능

---

### [핵심] Span 검출기: 전이성 유방암 ctDNA 직렬 검사에서 검출 한계 아래 약물 내성 징후 조기 포착 (Seeing Below the Limit of Detection: A Censored-Poisson Bayesian Latent-Growth Change-Point Detector for Serial ctDNA in HR+/HER2- Metastatic Breast Cancer)
- 저자/소속: Aarchi Singh Thakur, Abhijoy Sarkar / 소속 미확인
- 출처: arXiv (q-bio.QM, cs.LG, stat.ME) · 2026-06-10 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.11876
- 코드/데이터: https://github.com/span-ai-labs/span-detector (공개)
- 한 줄 요지: 비검출 ctDNA 측정값을 결측이 아닌 구간 중도절단(censored) 관측으로 처리하는 베이지안 잠재 성장 변화점 모델로, 임상적으로 보이지 않는 단계에서 내성 서브클론 출현을 감지한다.
- 핵심 수치: 합성 시나리오에서 조기 검출률 2배 향상(25% vs 11%, 허위 경보율 10% 동일); GBSG-2 코호트(n=686) C-index 0.67 vs 0.68 기저치; PBC2 코호트(n=312) 검증
- 분야 태그: 임상ML / ctDNA / 액체생검 / 바이오마커
- 선별 사유: 검출 한계 아래 데이터를 정보로 전환하는 통계 설계가 액체생검 기반 조기 내성 감시에 직접 적용 가능

---

### [핵심] GLACIER: 분자 특성 예측을 위한 멀티모달 학생-교사 파운데이션 모델 (GLACIER: A Multimodal Student-Teacher Foundation Model for Molecular Property Prediction)
- 저자/소속: Emily Nguyen, Yongchan Hong, Harsh Toshniwal, Yan Liu, Andreas Luttens / 소속 미확인
- 출처: arXiv (cs.LG, q-bio.BM) · 2026-06-09 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.11382
- 코드/데이터: https://github.com/eemokey/glacier (공개)
- 한 줄 요지: 분자 그래프·SMILES·물리화학 기술자를 학생-교사 지식 증류 구조로 통합해 10만 개 약물 유사 분자로 사전학습한 분자 특성 예측 파운데이션 모델.
- 핵심 수치: Biogen 벤치마크 기저치(KERMT) 대비 +7.6%, ExpansionRX +9.9%, ChEMBL-MT +9.5%
- 분야 태그: 신약AI / 분자특성 / LLM-bio
- 선별 사유: ADME/독성 등 약물 개발 핵심 특성 예측 성능 개선, 멀티모달 분자 표현 학습의 실용적 구현 사례

---

### [핵심] ADME 다중과제 예측을 위한 확률론적 대조 사전학습 (Probabilistic Contrastive Pretraining for Multi-task ADME Property Prediction)
- 저자/소속: Yifan Xue, Srimukh Prasad Veccham, Saee Paliwal, Tyler Shimko, Micha Livne / 소속 미확인
- 출처: arXiv (cs.LG, q-bio.QM) · 2026-06-09 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.11508
- 코드/데이터: 공개 안 됨/미확인
- 한 줄 요지: 재건·대조 판별·화학 작업을 단일 확률론적 잠재 변수 목적함수로 통합한 분자 그래프-트랜스포머로 흡수·분포·대사·배설 특성을 다중과제로 예측한다.
- 핵심 수치: Biogen 데이터셋 +7.6%, ExpansionRX +9.9%, ChEMBL-MT +9.5% (기저치 KERMT 대비)
- 분야 태그: 신약AI / ADME / 분자특성
- 선별 사유: 후보물질 초기 스크리닝 단계 핵심인 ADME 예측 품질 향상, 음전이(negative transfer) 완화 설계 포함

---

## 와이드 논문 (4편)

### [와이드] 가상 바이오텍: 치료제 발견·개발을 위한 다중에이전트 AI 프레임워크 (The Virtual Biotech: A Multi-Agent AI Framework for Therapeutic Discovery and Development)
- 저자/소속: Harrison G. Zhang, Peter Eckmann, Jiacheng Miao, Andrew B. Mahon, James Zou / (Stanford 계열 추정, 소속 미명기)
- 출처: bioRxiv · 2026-02-23 · **preprint(미동료심사)**
- DOI/링크: https://doi.org/10.64898/2026.02.23.707551
- 코드/데이터: 미확인 (라이선스 제약으로 PMC 아카이빙 불가)
- 한 줄 요지: 가상 CSO 에이전트가 통계유전학·기능유전체·화학정보학·임상데이터 전문 AI 과학자 에이전트들을 조율해 치료 표적 발굴·임상 실패 원인 분석·바이오마커 전략 수립을 자율 수행하는 멀티에이전트 시스템.
- 핵심 수치: 5만 5,984개 임상시험 자율 분석; 세포 유형 특이 유전자 표적 약물이 Ph I→II 전환율 40% 높음, 시장 출시 확률 48% 높음, 부작용 발생률 32% 낮음
- 분야 태그: 신약AI / 임상ML / 멀티에이전트
- 선별 사유: W24 기준 가장 파급력 큰 신약 AI 아키텍처 논문 중 하나; CSO-에이전트 조직 구조가 제약 R&D 자동화 방향을 구체적으로 제시

---

### [와이드] 병리학의 파운데이션 모델 재고 (Rethinking Foundation Models in Pathology)
- 저자/소속: Hamid R. Tizhoosh / 소속 미확인
- 출처: Nature Biomedical Engineering · 2026 · **peer-reviewed**
- DOI/링크: https://doi.org/10.1038/s41551-026-01696-6
- 코드/데이터: 해당 없음 (논평/관점 논문)
- 한 줄 요지: 자연 이미지 기반 범용 파운데이션 모델이 조직 형태의 조합적 복잡성과 근본적으로 맞지 않음을 주장하며, 병리 이미지 전용 아키텍처 필요성을 제기한다.
- 핵심 수치: 정량 수치 없음 (논평 형식)
- 분야 태그: 임상ML / 병리AI / 파운데이션모델
- 선별 사유: Nature Biomedical Engineering 동료심사 논평으로, 병리 AI 표준화 논의의 기준점이 될 peer-reviewed 관점 제시

---

### [와이드] OmniBioTwin: 건강 디지털 트윈을 위한 계층 쌍둥이 시스템 프레임워크 (OmniBioTwin: A System-of-Twinned-Systems Framework for Health Digital Twins)
- 저자/소속: Zhaohui Wang, Yu Huang, Jiang Bian / 소속 미확인
- 출처: arXiv (q-bio.QM, cs.AI) · 2026-06-09 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.11264
- 코드/데이터: 공개 안 됨/미확인
- 한 줄 요지: 분자·세포·기관 수준 계산 모델을 7개 레이어의 명시적 상호작용 연산자로 연결한 모듈식 건강 디지털 트윈 프레임워크로, GLP-1 신호 경로·알츠하이머 모델에 적용을 시연했다.
- 핵심 수치: 7개 조율 레이어 구조; GLP-1 신호 경로-알츠하이머 다중 스케일 시범 모델
- 분야 태그: 임상ML / 디지털트윈 / 정밀의료
- 선별 사유: 멀티스케일 생물 디지털 트윈 아키텍처의 체계적 설계 프레임워크로, 개인 맞춤 임상 시뮬레이션 방향 제시

---

### [와이드] 유전체 기반 개인화 생리 해석을 위한 베이지안 추론 프레임워크 (Is It You or Your Environment? A Bayesian Inference Framework for Genomically-Anchored Personalized Physiological Interpretation)
- 저자/소속: Aruna Dey, Suraj Biswas / 소속 미확인
- 출처: arXiv (cs.AI, q-bio.BM, q-bio.GN) · 2026-06-11 · **preprint(미동료심사)**
- DOI/링크: https://arxiv.org/abs/2606.13556
- 코드/데이터: 공개 안 됨/미확인
- 한 줄 요지: 유전체 프로파일을 외생적 유전적 기준점(anchor)으로 삼아 생리 측정값의 유전 대 환경 기여를 분리하는 베이지안 추론 프레임워크로, 행동 데이터 축적 전 초기 해석을 가능하게 한다.
- 핵심 수치: 6개 생리 도메인에서 프레임워크 적용; FTO·FADS1/2·FKBP5 3개 유전자 검증 앵커 사용; HRV 55 ms 독해 예시에서 유전형별 해석 역전 시연
- 분야 태그: 임상ML / 정밀의료 / 유전체 / 웨어러블
- 선별 사유: 유전체-표현형 연결 기반 개인화 건강 AI의 새로운 프레이밍 — 소비자 건강 앱과 디지털 치료제 영역 연결 가능성
