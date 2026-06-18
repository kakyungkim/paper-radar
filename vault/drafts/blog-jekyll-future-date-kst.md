---
type: draft
status: ready-to-publish
created: 2026-06-19
tags: [기술블로그, Jekyll, GitHub Pages, timezone, KST]
---

# Jekyll GitHub Pages에서 KST 당일 포스트가 404 나는 이유

## 증상

포스트를 올렸는데 빌드는 success인데 URL에서 404가 난다.

```yaml
date: 2026-06-19 09:00:00 +0900   # KST 오전 9시
```

로컬에서 `jekyll build --verbose`를 돌리면 이게 보인다.

```
Skipping: _posts/kr/2026-06-19-my-post.md has a future date
```

## 원인

GitHub Pages 빌드 서버는 UTC로 동작한다. `+0900`으로 지정된 `2026-06-19 09:00`은 UTC로 `2026-06-19T00:00Z`다.

한국 시간 오전에 포스트를 올리면, UTC 기준으로는 그 날짜가 아직 오지 않았다. Jekyll은 미래 날짜 포스트를 기본적으로 skip한다.

빌드 로그에서 확인할 수 있는 타임스탬프:
- GitHub Actions 빌드: `2026-06-18T15:43Z` (UTC)
- 포스트 날짜: `2026-06-19T00:00Z` (UTC 환산)
- → 빌드 시점보다 약 8시간 미래 → skip

## 해결

`_config.yml`에 한 줄 추가.

```yaml
future: true   # KST 기준 당일 포스트가 UTC 빌드에서 미래로 skip되는 것 방지
```

이후 KST 당일 포스트도 빌드 즉시 발행된다.

## 왜 `future: true`가 안전한가

"미래 포스트를 발행하지 않는다"는 기능은 예약 발행 목적이다. 파일을 올려놓고 날짜가 되면 자동 발행되길 기대하는 워크플로에서 쓴다. 그런데 GitHub Pages는 push할 때만 빌드한다. 시간이 되면 알아서 재빌드하지 않는다. 어차피 예약 발행이 작동하지 않으니, `future: false`를 유지할 이유가 없다.

## 진단 방법

404가 나면 먼저 로컬에서 확인한다.

```bash
bundle exec jekyll build --verbose 2>&1 | grep -i "skip\|future"
```

`has a future date`가 보이면 이 문제다.
