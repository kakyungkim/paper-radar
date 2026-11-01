---
week: 2026-W44
period: 2026-10-26 ~ 2026-11-01
collected: 2026-11-01
sources:
  arxiv: 5
  biorxiv: 0
  medrxiv: 1
  neurips_2026: 1
  total: 7
---

# 2026-W44 수집 논문

수집일: 2026-11-01 / 대상 기간: 2026-10-26 ~ 2026-11-01

소스별 건수: arXiv 5편 + medRxiv 1편 + NeurIPS 2026 1편 (핵심 5 + 와이드 2)

> 수집 방법: GitHub 일별 arXiv 다이제스트(spacenship/newDailyArxiv issues #118–#122), NeurIPS 2026 포스터 목록(neurips.cc), arXiv 카테고리 스니펫(q-bio.GN·cs.AI·cs.LG·q-bio.QM 최신 리스팅), medRxiv 최신 리스팅, 웹 검색 스니펫 기반 추출. arxiv.org·biorxiv.org·medrxiv.org·huggingface.co 직접 접근은 에이전트 프록시 차단으로 불가 — 제목·ID·초록은 검색 스니펫·NeurIPS 공식 포스터 초록·2차 미러(papers.cool 스니펫 포함) 기반. 저자명 미확인 논문은 "저자명 미확인" 표기. 초록 직접 확인 불가 논문은 "초록 미확인 (제목·ID 확인)" 표기.
>
> arXiv 논문의 제출일과 공개일 차이: 금요일(Oct 23) 제출 논문은 월요일(Oct 27)에 공개 발표됨. 이번 주에 처음 arXiv에 공개 발표된 논문(제출일 기준 Oct 21~28)을 W44로 수집함.

---

## 핵심 (Core)

### [핵심] C1. 임상 유전체 분석을 위한 스킬 중심 에이전트 (Advancing Clinical Genomic Analysis with a Skill-Centred Agent)

- **저자/소속**: 저자명 미확인 (arXiv q-bio.GN + cs.AI 교차 등재; 다중 의료기관 소속 저자로 명기됨 — 원문 접근 불가)
- **출처**: arXiv · 2026-10-29 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.40556
- **코드/데이터**: 미확인
- **초록 요약** (arXiv 리스팅 스니펫 및 관련 검색 결과 기반): 임상 유전체 분석을 위해 105개의 원자적(atomic) 스킬을 큐레이션한 에이전트 시스템을 제안. 희귀 유전 질환 해석, 분자 종양학 의사결정 두 임상 영역에서 평가. 11개 의료기관 소속 임상 유전체 전문가 11명이 한 달간 실제 업무에 시스템을 사용하며 96건의 완료된 분석에 대해 피드백 제공. 기준 판단(criterion-level) 변이 분석 일치율과 유전체 해석 일치율이 모두 향상됐으며, 모든 시나리오에서 해석 소요 시간이 단축됨.
- **핵심 수치**: 105개 원자적 스킬 / 11개 의료기관 전문가 11명 참여 / 96건 완료 분석 / 모든 평가 시나리오에서 해석 시간 단축 (출처: arXiv 리스팅 스니펫)
- **분야 태그**: 임상ML / LLM-bio / 유전체
- **사회적 신호**: arXiv q-bio.GN + cs.AI 교차 등재 (Oct 29 q-bio 최신 리스팅 상위 노출)
- **선별 사유**: 실제 임상 환경에서 여러 의료기관 전문가를 대상으로 prospective하게 검증된 임상 유전체 LLM 에이전트 — in silico 벤치마크를 넘어 실제 해석 시간 단축과 일치율 개선을 동시에 달성했다는 점에서 임상 적용 가능성이 가장 높은 이번 주 논문.

---

### [핵심] C2. 바이오뱅크 규모 조건부 합성 게놈 생성 (HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching)

- **저자/소속**: Ahmad Abdel-Azim, Xihong Lin · Harvard T.H. Chan School of Public Health
- **출처**: arXiv · 2026-10-28 · **peer-reviewed** (NeurIPS 2026 포스터 채택)
- **DOI/링크**: https://arxiv.org/abs/2610.36361 (NeurIPS 포스터: https://neurips.cc/virtual/2026/poster/150881)
- **코드/데이터**: 미확인 (NeurIPS 2026 포스터 목록에 코드 링크 미기재)
- **초록 요약** (NeurIPS 2026 공식 포스터 초록 기반): 하플로타입 위상 분리(haplotype phasing) 없이 SNP 수준의 게놈 전장 데이터를 생성하는 잠재 플로우 매칭(latent flow matching) 프레임워크 HELICS를 제안. 염색체 단위 데이터를 컨볼루션 오토인코더로 잠재 토큰으로 압축하고, 트랜스포머 기반 조건부 플로우 매칭 모델로 생성. UK Biobank 약 428K 게놈으로 학습. 조상 정보(ancestry)와 유전적 부담(genetic liability) 요약 통계를 조건으로 사용해 다양한 위험 프로파일에서 타겟 생성 가능. 보류된 실제 게놈 대비 대립 유전자 빈도(allele frequency) 검증 R² = 0.992 달성, 기존 하플로타입 기반 및 유전자형 기반 시뮬레이터를 상회.
- **핵심 수치**: 훈련 데이터 ~428K UK Biobank 게놈 / 알릴 빈도 검증 R² = 0.992 / 기존 시뮬레이터 대비 우위 (출처: NeurIPS 2026 공식 포스터 초록)
- **분야 태그**: 유전체 / 바이오인포
- **사회적 신호**: NeurIPS 2026 포스터 채택 (poster #150881)
- **선별 사유**: 거대 바이오뱅크 규모의 합성 게놈 생성이 가능해지면 희귀 유전자형 증강, 개인정보 보호 데이터 공유, 임상 유전체 모델 훈련에 직접 활용 가능 — 하플로타입 위상 분리 없이도 높은 충실도 달성이 방법론적 진보.

---

### [핵심] C3. 단백질 서열·구조·언어를 통합한 확산 언어 모델 (Trion-1: Unifying Language, Protein Sequence, and Structure with Diffusion Language Models)

- **저자/소속**: 저자명 미확인 (arXiv 2026-10-22 제출, Oct 26–27 공개 발표 — 원문 접근 불가)
- **출처**: arXiv · 2026-10-22 (제출) / 2026-10-26 (공개) · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.31215
- **코드/데이터**: 미확인
- **초록 요약** (papers.cool 스니펫 기반): 단백질 서열·구조·자연어를 단일 이산 토큰 공간으로 통합한 최초의 네이티브 다중모달 확산 언어 모델(dLLM) Trion-1을 제안. 엄격한 상동성 관리(strict homology control) 조건에서 단일 샘플로 TM-score 0.8 초과 달성 — 기존 삼중모달 모델이 200 샘플을 요구하던 성능 수준. 서열 이해 태스크에서 최상위 LLM과 동등 수준 보고. 폴딩·역폴딩·서열 이해·구조 이해·서열 설계·구조 설계 6개 태스크를 단일 모델로 처리.
- **핵심 수치**: 폴딩 TM-score >0.8 (단일 샘플, 엄격한 상동성 관리) / 기존 삼중모달 모델의 200 샘플 성능 달성 / 서열 이해 62.37%(최상위 LLM 동등 수준) (출처: papers.cool 스니펫 — 원문 확인 권장)
- **분야 태그**: 단백질 / LLM-bio
- **사회적 신호**: 없음
- **선별 사유**: 단백질 폴딩·설계를 위한 별도 특화 모델 없이 자연어·서열·구조를 단일 확산 LM으로 처리하는 접근 — 멀티태스크 단백질 파이프라인 단순화에 직접적 함의. 샘플 효율(1 vs 200)이 특히 주목할 만함.

---

### [핵심] C4. 종단 AI 모델로 암 이상반응 예측 (Longitudinal AI Models Predict Cancer Adverse Events)

- **저자/소속**: 저자명 미확인 (medRxiv 검색 스니펫 기반; 소속 다기관 — 원문 접근 불가)
- **출처**: medRxiv · 2026-10-26 (게시) · **preprint(미동료심사)**
- **DOI/링크**: https://www.medrxiv.org/content/10.64898/2026.10.22.26364879v1
- **코드/데이터**: 미확인
- **초록 요약** (medRxiv 검색 결과 스니펫 기반): 암 환자 약 224,000명으로부터 수집된 약 1억 200만 건의 측정값으로 모델을 사전 훈련 및 미세조정. 보류 코호트·전향적 코호트·외부 검증 코호트 전반에 걸쳐 암 관련 이상반응(adverse events) 예측에서 최신 성능 달성. 단일 기관 미세조정보다 여러 기관 데이터 풀링이 일반화 성능을 더 크게 향상시킴.
- **핵심 수치**: 224,000명 암 환자 / 102,000,000건 측정값 / 다기관 풀링 > 단기관 미세조정 (일반화 성능) / 보류·전향적·외부 검증 코호트 전반 최신 성능 (출처: medRxiv 검색 스니펫 — 원문 확인 권장)
- **분야 태그**: 임상ML
- **사회적 신호**: 없음
- **선별 사유**: 실제 임상 환경의 이상반응 조기 탐지는 항암 치료 안전성의 핵심 과제 — 대규모 측정값 기반 종단 사전훈련 모델이 다기관 전향적·외부 검증에서 SoTA를 달성한 점이 임상 배포 신뢰성을 높임.

---

### [핵심] C5. 머신러닝 원자간 포텐셜로 유도하는 구조 기반 신약 설계 확산 모델 (MLIPDiff: Guiding Denoising Diffusion Models for Structure-Based Drug Design via Machine-Learned Interatomic Potentials)

- **저자/소속**: 저자명 미확인 (GitHub arXiv 다이제스트 제목 확인; 원문 접근 불가)
- **출처**: arXiv · 2026-10-23 (제출) / 2026-10-27 (공개) · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.33315
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — GitHub 다이제스트 제목 및 관련 문헌 맥락 기반 추정): 구조 기반 신약 설계(SBDD) 확산 모델(denoising diffusion)의 디노이징 단계에 머신러닝 원자간 포텐셜(MLIP)을 유도 신호로 통합하여, 단백질 결합 포켓 내에서 생성되는 리간드의 물리화학적 타당성을 향상시키는 방법론을 제안하는 것으로 추정. MLIP는 DFT 수준의 에너지·힘 정보를 빠르게 계산 가능하게 해 기존 확산 모델의 구조적 오류를 보정하는 역할로 알려짐.
- **핵심 수치**: 미확인 (원문 직접 확인 필요)
- **분야 태그**: 신약AI
- **사회적 신호**: 없음
- **선별 사유**: MLIP를 SBDD 확산 모델에 결합하는 아이디어는 생성 분자의 양자화학적 타당성 문제를 직접 해결하는 방향으로, 기존 DiffSBDD·DiffBP 계열 모델의 실용 한계를 극복할 가능성이 있음 — 제목 확인 수준이므로 분석가가 원문 초록·결과 확인 후 세부 평가 권장.

---

## 🔭 와이드 (Wide)

### [와이드] W1. 다단계 역합성 장기 추론을 위한 에이전트 (Solvent: Long-Horizon Reasoning for Multi-Step Retrosynthesis)

- **arXiv/DOI**: https://arxiv.org/abs/2610.32308
- **저자**: 저자명 미확인 (GitHub arXiv 다이제스트 Oct 26, 2026 기재; 코드·HuggingFace 링크 함께 공개)
- **날짜**: 2026-10-23 (제출) / 2026-10-27 (공개)
- **상태**: preprint(미동료심사)
- **코드**: GitHub + HuggingFace 공개 (링크 미확인 — 다이제스트에 공개 명시)
- **한 줄 요약**: 다단계 역합성 계획(retrosynthesis planning)을 장기 추론(long-horizon reasoning) 문제로 재구성하고, 체인 오브 씽킹(CoT) 기반 에이전트로 합성 경로를 탐색한다고 주장.
- **와이드 선택 사유**: 신약개발 R&D에서 합성 가능성(synthesizability)은 후보 물질 선정의 핵심 관문 — 장기 추론 LLM이 다단계 역합성에 진입하는 트렌드를 포착하며, 신약AI 분야의 파이프라인 자동화 방향성 모니터링에 유용.

---

### [와이드] W2. GLP-1 경험 탐색을 위한 지식 그래프 LLM 에이전트 (AskGLP1: A Knowledge Graph LLM Agent for Exploring GLP-1 Experience from Online Patient Narratives)

- **arXiv/DOI**: https://arxiv.org/abs/2610.34987
- **저자**: 저자명 미확인 (GitHub arXiv 다이제스트 Oct 27, 2026 "Graph" 섹션 기재; 원문 접근 불가)
- **날짜**: 2026-10-26
- **상태**: preprint(미동료심사)
- **한 줄 요약**: 온라인 환자 내러티브(예: Reddit, 포럼)로부터 GLP-1 수용체 작용제(세마글루타이드·티르제파타이드 등) 사용 경험 정보를 지식 그래프와 LLM 에이전트로 구조화해 탐색한다고 주장.
- **와이드 선택 사유**: GLP-1 계열 약물은 2024~2026년 최대 규모 블록버스터 — 실환자 경험 데이터의 체계적 마이닝은 임상시험에서 포착되지 않는 부작용·사용 패턴 신호 탐지에 산업적 함의가 있어 약물감시(pharmacovigilance) 관점에서 모니터링 가치가 있음.

---

## 수집 메모

- **검색 쿼리**: "arxiv October 28 29 30 31 2026 drug discovery protein genomics clinical", "GitHub spacenship/newDailyArxiv issues 118–122 직접 열람", "HELICS biobank synthetic genome NeurIPS 2026", "ClinGeX clinical genomics agent skill arxiv 2610", "Longitudinal AI cancer adverse events medRxiv 2026" 외 다수
- **유효 중복 제외**: W43 수집 논문 전량(2610.26747·2610.26009·2610.24124·2610.26787·2610.28943) 및 W41–W42 목록 제외. 이번 주 후보 중 2610.28943(W43 수집)보다 높은 ID 보유 논문만 포함.
- **W44 기간 논문 판단 기준**: arXiv 제출일 Oct 21–28 → 공개 발표일 Oct 26–Nov 1 범위 논문을 W44로 처리. medRxiv·NeurIPS 포스터는 게시/채택 날짜 기준.
- **정보 신뢰도 주의**: C1(2610.40556)·C2(HELICS)는 arXiv 리스팅 스니펫 및 NeurIPS 공식 포스터 초록으로 내용 확인. C3(Trion-1)은 papers.cool 스니펫. C4(medRxiv 암 이상반응)은 medRxiv 검색 결과 스니펫. C5(MLIPDiff)는 GitHub 다이제스트 제목만 확인 — 분석가 단계에서 원문 재확인 권장. W1(Solvent)·W2(AskGLP1)는 다이제스트 제목·코드 공개 여부 확인; 초록 미확인.
- **분야 분포**: 임상ML(C1·C4) 2편, 유전체/바이오인포(C2) 1편, 단백질/LLM-bio(C3) 1편, 신약AI(C5) 1편, 화학AI 와이드(W1) 1편, 건강정보학 와이드(W2) 1편.
