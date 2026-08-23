---
type: raw
week: 2026-W34
date_range: 2026-08-17 ~ 2026-08-23
scout_date: 2026-08-23
sources: [arXiv, bioRxiv, Nature Medicine, Nature Communications]
---

# Paper Scout Raw — 2026-W34

## 핵심 논문 (Core) — 5편

---

### [C1] arXiv:2608.17381
- **제목**: Leveraging generative hallucination and biophysics-informed modeling for unified biomolecular sequence-structure co-design
- **저자**: Xuefeng Liu, Mingxuan Cao, Xiao Luo, Songhao Jiang, Tobin Sosnick, Jinbo Xu, Louis Maher, Rick Stevens
- **소속**: University of Chicago; Argonne National Laboratory
- **제출일**: 2026-08-18 (arXiv)
- **DOI/링크**: https://arxiv.org/abs/2608.17381
- **코드**: 미공개 (언급 없음)
- **분야**: 신약AI, 단백질, LLM-bio
- **검증 수준**: in silico
- **preprint 여부**: preprint (미동료심사)
- **사회적 신호**: 없음 (검색 기준)
- **요약**:
  - MCTH(Monte Carlo Tree Hallucination) 프레임워크. 동결된 단백질 폴딩/역폴딩 모델에서 hallucination된 디자인 궤적에 대해 MCTS(Monte Carlo Tree Search)로 추론 예산을 할당.
  - 바이오물리 에너지 항(biophysics-informed scoring)을 결합해 단백질-RNA, 단백질-DNA, 단백질-단백질, 단백질-리간드 등 다양한 biomolecular 쌍의 co-design을 단일 프레임워크로 수행.
  - 기존 방법들이 protein-only에 국한되거나 각 modality에 별도 모델이 필요했던 것을 통합.
  - 새로운 추론 예산 배분 전략: hallucination diversity를 활용해 설계 공간 탐색.

---

### [C2] Nature Medicine DOI:10.1038/s41591-026-04524-1
- **제목**: Putting epigenetic aging clocks on trial
- **저자**: Steve Horvath (교신저자)
- **소속**: Altos Labs (Cambridge, UK) — 추정 (원문 확인 필요)
- **제출/출판일**: 2026-08-21 (Nature Medicine online)
- **DOI/링크**: https://doi.org/10.1038/s41591-026-04524-1
- **코드**: 미제공: 별도 언급 없음
- **분야**: 임상ML, 바이오마커, 후성유전체
- **검증 수준**: 후향/전향 multi-study (51개 종단 연구)
- **preprint 여부**: peer-reviewed (Nature Medicine)
- **사회적 신호**: 없음 (검색 기준)
- **요약**:
  - DNA methylation 기반 후성유전체 나이 시계(epigenetic clock) 16종을 51개 종단 연구(longitudinal studies)에 걸쳐 대리 끝점(surrogate endpoint) 행동 여부를 체계적으로 검증.
  - Horvath는 GrimAge, PhenoAge 등 주요 클럭의 창시자이며, 이 논문은 임상시험 대리 끝점으로 사용 가능성을 객관적으로 평가.
  - 일부 클럭은 사망·질병 위험 예측력이 있으나 임상시험 대리 끝점으로 검증된 것은 제한적임을 보임.
  - 노화 개입 임상시험(longevity clinical trial)에서 메틸화 클럭의 실제 효용을 판별하는 기준선 제시.

---

### [C3] Nature Communications DOI:10.1038/s41467-026-76277-x
- **제목**: Deep-learning-enabled multi-omics analyses for prediction of future metastasis in cancer
- **저자**: (구체적 저자 목록 원문 확인 필요)
- **소속**: (원문 확인 필요)
- **출판일**: 2026년 8월 (Nature Communications)
- **DOI/링크**: https://doi.org/10.1038/s41467-026-76277-x
- **코드**: 미제공: 검색 결과에서 확인 안 됨
- **분야**: 멀티오믹스, 임상ML, 신약AI
- **검증 수준**: 후향 (N=7 코호트, 6개 암종)
- **preprint 여부**: peer-reviewed (Nature Communications). 원본 bioRxiv: 2025.05.16.654579
- **사회적 신호**: 없음 (검색 기준)
- **요약**:
  - EmitGCL(Epithelial Metastatic Cell Graph Convolutional Learning) — 딥러닝 기반 멀티오믹스 통합 프레임워크.
  - 6개 암종 7개 코호트에서 미래 전이(future metastasis) 예측. 기존 도구 대비 우월한 민감도·특이도.
  - 림프절 음성(lymph node-negative) 유방암 환자에서 은닉 전이세포(occult metastatic cells)를 탐지 — 기존 영상 검사는 놓쳤으나 이후 전이 확인.
  - HSP90AA1·HSP90AB1을 유방암 미래 전이 바이오마커로 동정. 시험관 내 HSP90 억제로 유방암 세포 이동 감소 검증.

---

### [C4] arXiv:2608.19304
- **제목**: Quantum Kernel Estimation for the Discovery of Early Lung Cancer Detection
- **저자**: Hamed Javidi, Alex Zajichek, Hakan Doga, Laxmi Parida, Filippo Utro, Peter J. Mazzone
- **소속**: IBM Research; Cleveland Clinic
- **제출일**: 2026-08-19 (arXiv)
- **DOI/링크**: https://arxiv.org/abs/2608.19304
- **코드**: 미공개 (언급 없음)
- **분야**: 임상ML, 유전체, 액체생검
- **검증 수준**: in silico
- **preprint 여부**: preprint (CIBB 2026 accepted)
- **사회적 신호**: 없음 (검색 기준)
- **요약**:
  - DNA fragmentomics + DNA methylation 데이터를 각도/밀집-각도(angle/dense-angle) 특징 맵으로 변환, fidelity 기반 양자 커널(quantum kernel) 적용.
  - 폐암 조기 발견을 위한 액체생검(liquid biopsy) 분류 모델 구축.
  - CIBB 2026(국제 바이오인포매틱스 및 바이오통계 심포지엄) 채택.
  - IBM과 Cleveland Clinic 협업 — 임상 데이터와 양자 컴퓨팅 방법론 연계 시도.

---

### [C5] arXiv:2608.06022
- **제목**: EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?
- **저자**: Zirui Wang et al. (구체적 저자 목록 원문 확인 필요)
- **소속**: (원문 확인 필요)
- **제출일**: 2026년 8월 초-중순 (arXiv, 정확한 날짜 확인 필요)
- **DOI/링크**: https://arxiv.org/abs/2608.06022
- **코드**: 미제공: 언급 없음
- **분야**: 신약AI, LLM-bio, 항체
- **검증 수준**: in silico (benchmark evaluation)
- **preprint 여부**: preprint (미동료심사)
- **사회적 신호**: 없음 (검색 기준)
- **요약**:
  - EpiBench — LLM의 에피토프(epitope) 추론 능력을 평가하는 폐쇄형·서열 기반·자동 채점 가능 벤치마크.
  - 1,609개 샘플: 구조적 항체-항원 접촉, 기능적 B세포 분석, 딥 돌연변이 스캐닝(deep mutational scanning) escape 측정 데이터 기반.
  - 5가지 과제: 표적 영역 발견, 항체-조건부 에피토프 동정, 에피토프 빈닝(binning), 기능적 에피토프 평가, 항체 탈출(escape) 평가.
  - 9개 범용 LLM 평가 결과: 에피토프 관련 신호를 부분적으로 포착하나, 항체 특이적 서열 접지(sequence grounding)·장-맥락 잔기 지역화·생물학적 추론에서 제한적.

---

## 와이드 논문 (Wide Angle) — 2편

---

### [W1] arXiv:2608.19902
- **제목**: Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis
- **저자**: Zijiao Chen, Nicholas Lu, Xinhui Li et al.
- **소속**: (원문 확인 필요)
- **제출일**: 2026-08-19 (arXiv)
- **DOI/링크**: https://arxiv.org/abs/2608.19902
- **코드**: 미제공: 언급 없음
- **분야**: LLM-bio, 바이오인포, 뇌영상
- **검증 수준**: in silico (platform evaluation)
- **preprint 여부**: preprint (NCTA 2026 / IJCCI 2026 accepted)
- **사회적 신호**: 없음 (검색 기준)
- **요약**:
  - Brain Researcher — 신경영상(neuroimaging) 데이터 분석에 분석적 엄밀성(analytic rigor)을 더한 에이전트 AI 플랫폼.
  - 도구 선택 정확도 23.3% → 93.6% (+70.2pp) 달성.
  - NCTA 2026 및 IJCCI 2026 학회 채택.
  - 범용 AI 에이전트 프레임워크를 과학 도메인에 특화 적용한 사례.

---

### [W2] Nature d41586-026-02551-z
- **제목**: Staggering 90% of biomedical papers now show signs of AI help
- **저자**: (Nature News 기사 — 기자/에디터 작성)
- **소속**: Nature Editorial
- **출판일**: 2026년 8월 (Nature)
- **링크**: https://www.nature.com/articles/d41586-026-02551-z
- **분야**: 과학정책, AI 활용
- **검증 수준**: 해당 없음 (뉴스 기사)
- **preprint 여부**: 해당 없음 (peer-reviewed 뉴스)
- **사회적 신호**: Nature 메인 피처
- **요약**:
  - PubMed Central 아카이브 분석 결과 2025년 출판 논문의 77%(또는 90%)가 LLM 사용 흔적 보임.
  - 과학 글쓰기에서 AI 활용 급증 현황·논쟁·함의 정리.
  - 광범위한 AI 도입이 재현성·신뢰성에 미치는 영향 논의.
  - 주의: 뉴스 기사(2차 출처). 원저 연구 있으면 추적 필요.

---

## Dedup 체크 노트
- W33 논문들(scKanFormer, IMPROVE DRP, RetFold/DRR, SVPLEX, LEN-Seek)과 겹침 없음 확인.
- EmitGCL(s41467-026-76277-x)의 정확한 출판일 불확실 — 원문 접근 시 재확인 권장.
- arXiv:2608.06022(EpiBench) 제출일 August 초-중순 추정, W33/W34 경계 가능성 있음.
