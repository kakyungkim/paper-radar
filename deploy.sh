#!/usr/bin/env bash
# paper-radar 발행 배포 스크립트
# 렌더된 주간 HTML을 블로그(GitHub Pages)로 복사 → index 갱신 → commit → push.
#
# 사용법:
#   ./deploy.sh                        # 이번 주차 발행본 배포
#   ./deploy.sh 2026-W24               # 특정 주차
#   ./deploy.sh 2026-W24 "헤드라인"     # 목록에 보일 제목 지정
#   CONFIRM=0 ./deploy.sh              # 확인 없이 바로 push
#   BLOG=~/work/kakyungkim.github.io ./deploy.sh
set -euo pipefail

# 현재 ISO 주차
WEEK="${1:-$(TZ=Asia/Seoul date '+%G-W%V')}"
TITLE="${2:-paper-radar $WEEK 주간 다이제스트}"
CONFIRM="${CONFIRM:-1}"

PAPER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG="${BLOG:-$HOME/kakyungkim.github.io}"
SRC="$PAPER/vault/html/$WEEK.html"
DST="$BLOG/paper-radar/$WEEK.html"
IDX="$BLOG/paper-radar/index.html"

[ -f "$SRC" ] || { echo "❌ 렌더 파일이 없습니다: $SRC"; exit 1; }
[ -d "$BLOG/paper-radar" ] || { echo "❌ 블로그 paper-radar 폴더 없음: $BLOG/paper-radar"; exit 1; }

# ── 발행 전 검증 게이트 (2026-W27 블로그 한글 깨짐 사고 재발 방지) ──
# 배포할 HTML이 소스에서 즉석 재렌더한 결과와 바이트 동일한지 대조한다.
# 손편집·깨진 중간본·오래된 렌더본이 그대로 나가는 것을 막는다.
DIGEST="$PAPER/vault/digest/$WEEK.md"
if [ -f "$DIGEST" ]; then
  python3 "$PAPER/scripts/render_html.py" "$WEEK" --out-suffix .verify >/dev/null 2>&1 || {
    echo "❌ 검증용 재렌더 실패 — 배포 중단"; exit 1; }
  VERIFY="$PAPER/vault/html/$WEEK.verify.html"
  if ! diff -q "$SRC" "$VERIFY" >/dev/null; then
    echo "❌ 배포 대상 HTML이 소스 재렌더본과 다릅니다 — 손편집/깨짐/구본 의심. 배포 중단."
    echo "   확인:  diff \"$SRC\" \"$VERIFY\""
    exit 1
  fi
  rm -f "$VERIFY" "$PAPER/vault/push/$WEEK.verify.md" "$PAPER/vault/push/$WEEK.verify-deepdive.md" 2>/dev/null || true
  echo "✅ 검증: 배포본 == 소스 재렌더본 (깨짐·손편집 없음)"
else
  echo "⚠️  소스 digest 없음($DIGEST) — 재렌더 대조 건너뜀. SRC를 그대로 신뢰함."
fi

cp "$SRC" "$DST"
echo "✅ 복사: paper-radar/$WEEK.html"

if grep -q "$WEEK.html" "$IDX"; then
  echo "ℹ️  index에 $WEEK 이미 있음 — 목록 추가 건너뜀"
else
  ENTRY="        <a href=\"$WEEK.html\" class=\"block bg-white border border-gray-200 rounded-xl p-5 shadow-sm hover:shadow-md hover:border-indigo-200 transition\"><p class=\"text-xs text-gray-400 mb-1\">$WEEK</p><p class=\"font-bold text-gray-900 text-[16px] leading-snug\">$TITLE</p></a>"
  awk -v e="$ENTRY" '{print} /<!-- ENTRIES:INSERT_AFTER -->/{print e}' "$IDX" > "$IDX.tmp" && mv "$IDX.tmp" "$IDX"
  echo "✅ index 목록에 $WEEK 추가"
fi

cd "$BLOG"
git add "paper-radar/$WEEK.html" "paper-radar/index.html"
if git diff --cached --quiet; then
  echo "ℹ️  로컬 변경 없음 — 원격 반영 여부만 확인"   # 앞선 실행이 커밋만 하고 push를 못 했을 수 있다
else
  git commit -q -m "paper-radar: $WEEK 발행"
  echo "✅ 커밋 완료"
fi

# HEAD:main 으로 민다. `git push origin main`은 detached HEAD(클라우드 세션의 기본 상태)에서
# 새 커밋이 아닌 옛 main을 밀어 "Everything up-to-date"로 성공 종료했다(2026-W40~W42, W44 블로그 누락).
# push 뒤에는 원격 main에 이 주차 파일이 로컬과 같은 내용으로 있는지 확인하고, 없으면 실패로 끝낸다.
publish() {
  git push origin HEAD:main
  git fetch -q origin main
  if [ "$(git rev-parse "FETCH_HEAD:paper-radar/$WEEK.html" 2>/dev/null)" != "$(git rev-parse "HEAD:paper-radar/$WEEK.html")" ]; then
    echo "❌ push 뒤 원격 main에 paper-radar/$WEEK.html 이 없거나 다릅니다. 공개되지 않았습니다." >&2
    exit 1
  fi
  echo "🚀 공개 완료 — 원격 main 반영 확인 (페이지는 1~2분 뒤 라이브)"
}

if [ "$CONFIRM" = "1" ]; then
  read -r -p "지금 push 해서 공개할까요? [y/N] " yn
  case "$yn" in
    [yY]*) publish;;
    *)     echo "⏸  push 보류 — 나중에:  (cd \"$BLOG\" && git push origin HEAD:main)";;
  esac
else
  publish
fi
