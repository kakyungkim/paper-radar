# paper-radar vault

옵시디언 vault. 이 폴더를 옵시디언에서 그대로 열면 된다(변환 불필요).

## 폴더 지도
| 폴더 | 무엇 | 누가 씀 |
| --- | --- | --- |
| `raw/` | 주간 수집 논문 1차 선별 | paper-scout |
| `analysis/` | 방법·임상·산업 3렌즈 분석 | method/clinical/industry-analyst |
| `digest/` | 주간 다이제스트(통합·검수·검증본) | digest-editor → style-critic → claim-checker |
| `html/` | 브라우저용 HTML 다이제스트 | digest-renderer(`scripts/render_html.py`) |
| `push/` | 텔레그램용 짧은 요약 | digest-renderer |
| `topics/` | 주제 MOC(유전체·임상ML·신약개발AI 등) | knowledge-curator |
| `briefs/` | 스터디 발제 자료 | study-brief-writer |
| `reports/` | 월간·분기 동향 리포트 | trend-synthesizer |
| `_meta/` | 기준선(lens-guide·benchmarks·문체·dedup·개선기록) | 전원 참조 |
| `assets/` | 로고·이미지 | — |

## 흐름
paper-scout → method ∥ clinical ∥ industry → digest-editor → style-critic → claim-checker → digest-renderer ∥ knowledge-curator → (선택) study-brief-writer

## 규칙
- 모든 논문에 DOI/원문 링크 + 검증 수준 + preprint 여부.
- dedup 기준: `_meta/recent-papers.md`(DOI/arXiv ID, 최근 3주).
- 자세한 설계는 루트 `CLAUDE.md` 참조.
