---
type: moc
tags: [임상ML]
---
# 🗂 임상ML — 주제 지도(MOC)

## 핵심 흐름
(2026-W26 기준) 범용 LLM이 의료 벤치마크에서 임상 특화 AI를 앞지른다는 동료심사 결과(Nature Medicine)가 나왔다. 전문 임상 AI 시스템의 존재 이유를 근본적으로 묻는 결과로, "특화 모델이 항상 범용보다 낫다"는 통념에 반례가 쌓이고 있다. 동시에 DeepBD는 에이전트 워크플로우(agentic workflow)를 변이 우선순위 결정과 희귀질환 진단에 적용해 임상 LLM의 새로운 사용 패턴을 보여준다. W25에서 드러난 EHR 다단계 추론 실패와 W26의 벤치마크 역전을 함께 보면, 임상 AI 평가 지표 자체의 재설계 필요성이 커지고 있다. W24 ctDNA·W25 공정성 지표에 이어 W26에서는 "어떤 AI 모델 유형을 언제 써야 하나"라는 선택 기준 논의가 중심으로 이동한다.

## 타임라인
### 2026-W26
- **범용 LLM vs 임상 특화 AI(Vishwanath 외, NYU)** — GPT-4o 등 범용 LLM이 다수 의료 벤치마크에서 임상 특화 AI 도구 전반을 능가. Nature Medicine 동료심사 게재. 코드 공개. 출처: [[digest/2026-W26]] | DOI:10.1038/s41591-026-04431-5
- **DeepBD: 선천성 유전 결함 변이 진단 에이전트(Li 외)** — 그라운딩된 에이전트 워크플로우로 변이 우선순위 결정 및 희귀질환 진단 자동화. 미동료심사(preprint). 출처: [[digest/2026-W26]] | arXiv:2606.24779

### 2026-W25
- **EHR 추론 실패 실증(Basu, UCSF)** — MedAlign 313개 질의에서 Claude Sonnet hop=1 정확도 30.6% → hop=4 17.6% 단조 감소. GPT-4o·GPT-5 동일 패턴 확인. 임상 LLM 안전성 벤치마크로 즉시 활용 가능. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.16890
- **xCI: 그룹 조건부 C-지수(Wang 외)** — Harrell C-지수 그룹 조건부 확장. Framingham·MESA·ARIC·Truveta EHR에서 심혈관 위험 모델 집단 편향 감지. 공정성 규제 심사 직결. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.16872
- **Tabular FM 생존 분석 적응(Pham 외)** — TabPFN·TabDPT·TabICL + MTLR 헤드. MIMIC-IV C-지수 0.856(DeepSurv +1.4%), eICU 0.797. AIiH 2026 게재 확정. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.12006
- **멀티모달 암 FM 벤치마킹(Hu 외)** — WSI+전사체 8개 분류 과제. 실제 상업 코호트(IH-BC, IH-NSCLC)에서 분포 이동 하 일반화·신뢰성 평가. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.17115

### 2026-W24
- **Span ctDNA 변화점 검출기** — 비검출 ctDNA를 censored 관측으로 처리하는 베이지안 잠재 성장 모델. 합성 시나리오 조기 검출률 2배 향상(25% vs 11%). 코드 공개(github.com/span-ai-labs/span-detector). 출처: [[digest/2026-W24]]
- **병리 파운데이션 모델 재고** — Nature Biomedical Engineering 논평. 자연 이미지 기반 모델의 조직 형태 부적합성 주장, 병리 전용 아키텍처 필요성 제기. 출처: [[digest/2026-W24]]
