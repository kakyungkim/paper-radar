---
week: 2026-W33
date_range: 2026-08-10 ~ 2026-08-16
created: 2026-08-16
scout: paper-scout
---

# 2026-W33 수집 논문

수집일: 2026-08-16 | 주차: 2026-W33 (2026-08-10 ~ 2026-08-16)

| 소스 | 핵심 | 와이드 | 합계 |
|------|------|--------|------|
| arXiv (q-bio / cs.LG / cs.AI) | 3 | 2 | 5 |
| PLOS Computational Biology (저널) | 1 | 0 | 1 |
| bioRxiv | 1 | 0 | 1 |
| **합계** | **5** | **2** | **7** |

중복 제외 확인: W29~W32 arXiv ID 및 DOI 목록 대조 완료. W32 기수집 ID (2608.02961, 2608.04046, 2608.06022, 2608.01964, 2608.05329) 및 JSONL 수록 전체 ID 제외. 2608.08xxx 이하 논문은 W32 날짜 범위(Aug 3~9)로 판단해 포함 제외.

---

## 핵심 (Core 5)

### 1. [핵심] scKanFormer: 대규모 단일세포 RNA 시퀀싱 세포 유형 주석을 위한 Transformer-KAN 프레임워크 (scKanFormer: A Transformer-KAN framework with biologically informed attention for cell type annotation in large-scale scRNA-seq data)

- **저자/소속**: Yuan L, Cao J, Sun S, Wang S, Ye L, Huang D-S (교신: Huang De-Shuang) | 소속 기관 미확인
- **출처**: PLOS Computational Biology 22(8): e1014607 · 2026-08-14 게재 · **peer-reviewed**
- **DOI/링크**: https://doi.org/10.1371/journal.pcbi.1014607
- **코드/데이터**: 미확인
- **한 줄 요지**: Kolmogorov-Arnold Networks(KAN)와 생물학적 경로 정보를 내포한 어텐션 메커니즘을 Transformer에 결합해 대규모 scRNA-seq 데이터에서 세포 유형 주석의 정확도·해석 가능성·배치 효과 강건성을 높인다.
- **핵심 수치**: 9개 최신 방법 대비 비교 평가에서 정확도 및 배치 효과 분리 성능 개선 보고(초록 기준, 구체 수치 미명시)
- **분야 태그**: 바이오인포 / 단일세포
- **사회적 신호**: PLOS Computational Biology 동료심사 게재
- **선별 사유**: KAN 기반 단일세포 주석 방법 중 처음으로 Transformer와 결합하고 경로 수준 생물학 사전지식을 어텐션 마스크로 통합했다. 동료심사 논문으로 재현 신뢰도가 높다.

---

### 2. [핵심] 대규모 항암 약물 반응 모델링을 위한 AI 준비 데이터 (Large-scale AI-Ready Data for Anti-Cancer Drug Response Modeling)

- **저자/소속**: Vincent Lavelle, Yitan Zhu, Kaitlyn Marlor, Thomas Brettin, Rick Stevens | Argonne National Laboratory
- **출처**: arXiv · 2026-08-11 제출 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.11444
- **코드/데이터**: IMPROVE 프레임워크(https://github.com/JDACS4C-IMPROVE) 기반 공개 — PharmacoDB 연동 데이터 공개 여부 확인 필요
- **한 줄 요지**: 약물 반응 예측(DRP) 모델의 성능이 데이터 규모 부족과 불일치한 벤치마크 관행에 의해 제약된다는 진단 하에, IMPROVE 표준 스키마를 통해 PharmacoDB를 중심으로 한 대규모 약물유전체 데이터를 통합·제공한다.
- **핵심 수치**: 기존 IMPROVE 벤치마크 대비 대폭 확장된 pharmacogenomic 데이터 통합(구체 규모 수치 초록 기준 미명시)
- **분야 태그**: 신약AI / 유전체
- **사회적 신호**: 없음
- **선별 사유**: 약물 반응 예측 ML 연구의 고질적 문제인 데이터 불균질성·벤치마크 비교 불가 문제를 국립연구소 수준의 표준화 작업으로 직접 공략한다. 코드·데이터 공개 지향 연구로 재현 가능성이 높다.

---

### 3. [핵심] 검색만으로 충분한가? 단백질 구조 생성의 신규성 평가와 창발 (Is Retrieval All You Need? Assessment and Emergence of Novelty in Protein Structure Generation)

- **저자/소속**: Tongyue Xu, Yijie Zhang, Mutian He, Lingdong Shen, Zhihong Liu, Tianlei Ying, Cheng Tan (교신: Cheng Tan) | Zhejiang University 외
- **출처**: arXiv · 2026-08-11 제출 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.10598
- **코드/데이터**: 미확인
- **한 줄 요지**: 단백질 백본 생성 모델이 "신규 폴드를 생성한다"고 평가받는 기준인 전체 체인 유사도 지표가 기존 도메인 조합에 불과한 것과 진정한 신규 폴드를 구별하지 못한다는 한계를 지적하고, 도메인 검색률(DRR) 지표와 훈련 없는 RetFold 베이스라인을 제안한다.
- **핵심 수치**: 확산·흐름 매칭 계열 8개 백본 생성 모델 분석 결과, 대부분 출력물에서 CATH S40 데이터베이스 내 기존 도메인과 지역 정렬 가능한 구조 발견; RetFold는 재훈련 없이 해당 모델들과 경쟁적 성능(초록 기준)
- **분야 태그**: 신약AI / 단백질
- **사회적 신호**: kiin.bio 뉴스레터 소개 (Memorial Sloan Kettering, Zhejiang University 연구 언급)
- **선별 사유**: 단백질 구조 생성 평가의 근본적 허점을 새 지표(DRR)로 정량화하고, 훈련 없는 검색 기반 베이스라인이 학습 기반 모델과 경쟁할 수 있음을 보였다. 신약개발 관점에서 생성 모델 선택 기준을 재고하게 하는 방법론 논문이다.

---

### 4. [핵심] SVPLEX: 코호트 수준 구조적 변이 검출을 위한 Nextflow 파이프라인 (SVPLEX: A Nextflow Pipeline for Cohort-level Structural Variant Calling)

- **저자/소속**: Jacob E. Munro, Mark F. Bennett, Melanie Bahlo (교신: Melanie Bahlo) | Walter and Eliza Hall Institute of Medical Research(WEHI), 호주
- **출처**: arXiv · 2026-08-12 제출 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.11621
- **코드/데이터**: 공개 (Nextflow 파이프라인 — GitHub 링크 논문 내 포함, 정확 URL 미확인)
- **한 줄 요지**: 단편 읽기(short-read) 전장유전체 시퀀싱(WGS) 데이터에서 6종의 구조적 변이(SV) 검출기를 통합해 코호트 단위 합의 콜셋을 생성하고, 희귀질환 변이 우선순위화 워크플로에 바로 연결 가능한 재현·확장성 있는 파이프라인을 제공한다.
- **핵심 수치**: 6개 SV 검출기 통합, 합의 기반 필터링, 결실·중복 콜에 대한 읽기 깊이 변화 확인 추가 적용 (수치 성능 지표 초록 기준 미명시)
- **분야 태그**: 바이오인포 / 유전체
- **사회적 신호**: 없음
- **선별 사유**: WEHI에서 개발한 코호트 규모 SV 검출 파이프라인으로, Nextflow 기반 재현성과 로컬·HPC·클라우드 이식성이 보장된다. 희귀질환 유전체 연구에 직접 연결되는 실용성 높은 오픈소스 도구다.

---

### 5. [핵심] LEN-Seek: SE(3)-불변 그래프 VAE의 잠재 공간에서 빠르고 확장 가능한 리간드 결합 부위 유사도 검색 (LEN-Seek: Fast and scalable ligand binding-site similarity search in the latent space of an SE(3)-invariant graph VAE)

- **저자/소속**: Kyunghwan Yeo, Dongwoo Kim, Jaemin Sim, Juyong Lee (교신: Juyong Lee) | 소속 기관 미확인
- **출처**: bioRxiv · 2026-08-14 게시 · **preprint(미동료심사)**
- **DOI/링크**: https://doi.org/10.64898/2026.08.14.744759
- **코드/데이터**: 미확인
- **한 줄 요지**: SE(3)-불변 그래프 변분 오토인코더(VAE)가 생성하는 잠재 공간에서 리간드 결합 부위 간 유사도를 빠르게 검색하는 LEN-Seek 방법을 제안한다.
- **핵심 수치**: 초록 기준 속도·확장성 수치 미명시; 3D 회전·이동 불변 표현을 잠재 벡터로 압축해 검색 효율화
- **분야 태그**: 신약AI
- **사회적 신호**: 없음
- **선별 사유**: 리간드 결합 부위 유사도 검색은 신약 재창출(drug repurposing) 및 표적 식별에 핵심인 작업이다. SE(3) 불변 그래프 VAE 기반 잠재 공간 검색은 기존 구조 정렬 기반 방법보다 계산 비용을 대폭 낮출 잠재력이 있다.

---

## 와이드 (Wide 2편)

### W1. [와이드] 다중 현미경 데이터셋에서 강건한 백혈병 세포 분류를 위한 검색 증강 비전 파운데이션 모델 (Retrieval-Augmented Vision Foundation Models for Robust Leukemia Cell Classification across Multiple Microscopy Datasets)

- **저자/소속**: (저자 미확인) | 소속 기관 미확인
- **출처**: arXiv · 2026-08-11 제출 · **preprint(미동료심사)** (SPIE Optics + Photonics 2026 구두 발표 채택)
- **DOI/링크**: https://arxiv.org/abs/2608.10657
- **코드/데이터**: 미확인
- **한 줄 요지**: 사이트·장비별 도메인 시프트가 큰 현미경 이미지 환경에서 백혈병(ALL/AML) 분류를 위해 비전 파운데이션 모델에 검색 증강(retrieval augmentation)을 결합한 2단계 분류 파이프라인을 제안한다.
- **핵심 수치**: Stage 1(이진 분류) 학습 이미지 122,167장, Stage 2(ALL/AML 아형 분류) 69,400장; 23쪽 논문, 12개 그림, 9개 표
- **분야 태그**: 임상ML / 의료영상
- **사회적 신호**: SPIE Optics + Photonics 2026 구두 발표 채택
- **선별 사유**: 단일 데이터셋 훈련 모델의 임상 일반화 문제를 검색 증강으로 해결하는 접근법이 이 주 화제. 백혈병 혈액 현미경 이미지 분야에서 실제 배포 문제를 직접 다룬다.

---

### W2. [와이드] Spark-to-Paper: 조합 가능한 스킬로서의 엔드투엔드 연구 논문 생성 (Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill)

- **저자/소속**: (저자 미확인) | 소속 기관 미확인
- **출처**: arXiv · 2026-08-12 제출 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2608.11924
- **코드/데이터**: 미확인
- **한 줄 요지**: 기존 코딩 어시스턴트 안에서 13개의 조합 가능한 스킬로 구현된 엔드투엔드 연구 논문 생성 시스템으로, 별도 에이전트 플랫폼 없이 문헌 검색·실험 설계·결과 기반 주장 수정·출판 준비 수준 그림 생성을 수행한다.
- **핵심 수치**: 8개 통제 연구 주제에서 인용 유효성 99.5%, 그림 편집 가능성 96.4%; 논문당 평균 11.9M 토큰, $8.1, 3.2시간 소요 (초록 기준)
- **분야 태그**: AI에이전트 / LLM
- **사회적 신호**: HuggingFace Daily Papers 상위 트렌딩 (2026-08-12~16 기간)
- **선별 사유**: 이 주 HuggingFace에서 화제가 된 논문. 연구 자동화 에이전트 분야의 현재 수준을 정량적으로 보여준다. 바이오인포 분야 연구 워크플로 자동화에도 직접 연결되는 트렌드다.
