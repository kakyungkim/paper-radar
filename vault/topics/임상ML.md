---
type: moc
tags: [임상ML]
---
# 🗂 임상ML — 주제 지도(MOC)

## 핵심 흐름
(2026-W25 기준) 임상 LLM의 구조적 한계가 수치로 드러나기 시작했다. 다단계 추론(multi-hop reasoning)이 필요한 EHR 질의에서 주요 모델 모두 hop 수에 비례해 정확도가 하락하며, 이는 안전성 평가 지표로 즉시 전용 가능한 발견이다. 생존 분석 쪽에서는 테이블 파운데이션 모델(TabPFN, TabDPT, TabICL)에 MTLR 헤드를 결합한 경량 어댑터가 MIMIC-IV·eICU에서 DeepSurv를 웃도는 C-지수를 기록해 범용 FM의 임상 이식 가능성을 넓혔다. 예후 공정성 평가 분야에서는 C-지수의 그룹 조건부 확장(xCI)이 Framingham·MESA·ARIC·Truveta 대규모 코호트에서 기존 지표가 놓친 집단 간 편향을 포착했다. 멀티모달 암 파운데이션 모델 벤치마킹 연구는 분포 이동 하 일반화 실패를 실제 상업 코호트로 재확인하며 배포 안전성 논의를 촉진한다.

## 타임라인
### 2026-W25
- **EHR 추론 실패 실증(Basu, UCSF)** — MedAlign 313개 질의에서 Claude Sonnet hop=1 정확도 30.6% → hop=4 17.6% 단조 감소. GPT-4o·GPT-5 동일 패턴 확인. 임상 LLM 안전성 벤치마크로 즉시 활용 가능. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.16890
- **xCI: 그룹 조건부 C-지수(Wang 외)** — Harrell C-지수 그룹 조건부 확장. Framingham·MESA·ARIC·Truveta EHR에서 심혈관 위험 모델 집단 편향 감지. 공정성 규제 심사 직결. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.16872
- **Tabular FM 생존 분석 적응(Pham 외)** — TabPFN·TabDPT·TabICL + MTLR 헤드. MIMIC-IV C-지수 0.856(DeepSurv +1.4%), eICU 0.797. AIiH 2026 게재 확정. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.12006
- **멀티모달 암 FM 벤치마킹(Hu 외)** — WSI+전사체 8개 분류 과제. 실제 상업 코호트(IH-BC, IH-NSCLC)에서 분포 이동 하 일반화·신뢰성 평가. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.17115

### 2026-W24
- **Span ctDNA 변화점 검출기** — 비검출 ctDNA를 censored 관측으로 처리하는 베이지안 잠재 성장 모델. 합성 시나리오 조기 검출률 2배 향상(25% vs 11%). 코드 공개(github.com/span-ai-labs/span-detector). 출처: [[digest/2026-W24]]
- **병리 파운데이션 모델 재고** — Nature Biomedical Engineering 논평. 자연 이미지 기반 모델의 조직 형태 부적합성 주장, 병리 전용 아키텍처 필요성 제기. 출처: [[digest/2026-W24]]
