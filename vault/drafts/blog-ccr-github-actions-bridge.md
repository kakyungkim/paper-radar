---
type: draft
status: ready-to-publish
created: 2026-06-16
tags: [기술블로그, CCR, GitHub Actions, 텔레그램, AI에이전트]
---

# 클라우드 AI 에이전트가 외부 API를 못 부를 때 — GitHub Actions 연동 패턴

Claude Code의 클라우드 루틴(CCR)으로 자동화를 구성하다 보면 벽 하나에 부딪힌다. 텔레그램, Slack 같은 외부 API를 직접 호출할 수가 없다. 클라우드 샌드박스 환경이 아웃바운드 HTTPS를 막고 있기 때문이다.

처음엔 단순한 설정 실수인 줄 알았다. 토큰이 맞는지 몇 번을 확인하고, curl로 직접 때려보기도 했다. 연결 자체가 안 됐다. CCR이 실행되는 Anthropic 클라우드 환경은 `api.telegram.org:443`으로 나가는 트래픽이 차단돼 있다. 토큰 문제가 아니었다.

## 해결 아이디어: git push를 이벤트 브리지로

에이전트가 외부 API를 직접 부르지 못한다면, 인터넷 제한이 없는 곳에서 대신 부르면 된다. GitHub Actions가 딱 그 역할이다.

흐름은 이렇다.

```
CCR (클라우드 에이전트)
  → 산출물 파일을 vault/push/*.md 에 생성
  → git push origin main

GitHub Actions (인터넷 제한 없음)
  → vault/push/*.md 변경 감지
  → 텔레그램 API 호출 → 채널 발송
```

에이전트는 파일을 쓰고 push만 한다. 텔레그램 발송은 Actions가 맡는다. 파일 하나를 중간 계층으로 쓰는 셈이다.

## 구현

### 1. send_push.py 작성

push용 마크다운 파일을 읽어 텔레그램으로 보내는 간단한 스크립트.

```python
import os, sys, requests

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID   = os.environ.get("TELEGRAM_CHAT_ID", "")

if not BOT_TOKEN or not CHAT_ID:
    print("[ERROR] 환경변수 미설정")
    sys.exit(1)

week = sys.argv[1]
push_file = f"vault/push/{week}.md"
text = open(push_file).read()

resp = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
)
print(resp.json())
```

환경변수에서만 토큰·채팅ID를 읽는다. 하드코딩하면 레포에 노출된다.

### 2. GitHub Actions 워크플로

```yaml
on:
  push:
    branches: [main]
    paths:
      - 'vault/push/*.md'

jobs:
  send:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0   # 전체 히스토리 필요 (아래 참고)

      - name: 날짜 감지
        id: detect
        run: |
          BEFORE="${{ github.event.before }}"
          if [ "$BEFORE" = "0000000000000000000000000000000000000000" ]; then
            BEFORE="HEAD~1"
          fi
          DATE=$(git diff --name-only "$BEFORE" HEAD \
            | grep -E '^vault/push/[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$' \
            | sed 's|vault/push/||; s|\.md||' \
            | sort -r | head -1)
          echo "date=$DATE" >> "$GITHUB_OUTPUT"

      - name: 텔레그램 발송
        if: steps.detect.outputs.date != ''
        env:
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: python3 scripts/send_push.py ${{ steps.detect.outputs.date }}
```

`vault/push/` 아래 파일이 push됐을 때만 실행된다. 다른 커밋엔 반응하지 않는다.

### ⚠️ 함정: `HEAD~1 HEAD` 대신 `before..HEAD`를 써야 하는 이유

처음엔 감지 로직을 `HEAD~1 HEAD`로 짰다. 며칠은 잘 됐다. 그러다 어느 날 텔레그램 알림이 안 왔다.

원인은 이랬다. CCR이 한 번의 `git push`에 커밋을 여러 개 묶어서 보냈다.

```
b38e97f  econ-radar: 2026-06-16 자동 생성  ← vault/push/2026-06-16.md 여기
8834dde  topics MOC 갱신
027155e  반도체 topics MOC 갱신
4520dc9  topics MOC 최종 정합              ← HEAD
```

`HEAD~1 HEAD`는 `4520dc9`와 `027155e`만 비교한다. `vault/push/` 변경은 `b38e97f`에 있었으니 감지에서 빠진다. 워크플로는 "성공"으로 끝나지만(스텝 자체가 skip됐으니) 텔레그램엔 아무것도 안 간다.

`github.event.before..HEAD`로 바꾸면 해당 push에 포함된 모든 커밋을 통째로 비교한다. `before`는 이 push 직전 커밋 SHA라서, 커밋이 몇 개 묶여 오든 전부 커버된다. `fetch-depth: 0`은 이 전체 범위 diff가 가능하도록 전체 히스토리를 내려받는 설정이다.

### 3. GitHub Secrets 등록

레포 Settings → Secrets → `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` 등록. Actions 실행 환경에서만 참조된다.

### 4. CCR 프롬프트 수정

기존에 텔레그램 직접 호출하던 단계를 빼고 이렇게 바꾼다.

```
산출물을 vault/push/YYYY-MM-DD.md에 저장하고 git push origin main.
텔레그램 발송은 GitHub Actions가 자동으로 처리한다.
```

## 채널 chat_id 찾는 법 — 한 줄 팁

새 채널의 chat_id를 찾을 때 `getUpdates`를 쓰면 채널 메시지가 나오지 않는 경우가 많다. 대신 이걸 쓴다.

```
https://api.telegram.org/bot{BOT_TOKEN}/getChat?chat_id=@채널명
```

`result.id` 필드가 chat_id다. 채널은 음수(-100으로 시작)가 나온다.

## 채널이 여럿이라면

채널마다 `TELEGRAM_CHAT_ID_XXXX` 식으로 Secret 이름을 분리하고, 워크플로에서 `${{ secrets.TELEGRAM_CHAT_ID_XXXX }}`로 주입한다. 봇 토큰은 하나로 공유해도 된다. 봇을 각 채널의 관리자로 추가해 두어야 발송된다.

## 이 패턴의 범위

텔레그램에만 쓰는 패턴이 아니다. CCR에서 직접 부를 수 없는 외부 서비스라면 어디든 같은 구조가 된다.

- Slack 알림 → `vault/push/slack-YYYY-MM-DD.md` + Actions에서 `slackapi/slack-github-action`
- Discord, Line, Notion, 사내 API — 모두 동일 패턴

파일 하나를 사이에 두고 "에이전트가 쓰면 Actions가 읽는다"는 구조를 만들면 된다.

## 정리

CCR(클라우드 에이전트)이 외부 API를 직접 못 부르는 건 설계상 제약이다. 우회 방법은 간단하다. git push를 이벤트 브리지로 쓰고, 실제 외부 호출은 인터넷이 열린 GitHub Actions에 위임한다. 에이전트는 파일만 쓰면 되고, 배포·알림 로직은 Actions YAML에 담아 버전 관리된다.
