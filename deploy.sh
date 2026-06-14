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
if git diff --cached --quiet; then echo "변경 없음 — 종료"; exit 0; fi
git commit -q -m "paper-radar: $WEEK 발행"
echo "✅ 커밋 완료"

if [ "$CONFIRM" = "1" ]; then
  read -r -p "지금 push 해서 공개할까요? [y/N] " yn
  case "$yn" in
    [yY]*) git push origin main && echo "🚀 공개 완료 (1~2분 뒤 라이브)";;
    *)     echo "⏸  push 보류 — 나중에:  (cd \"$BLOG\" && git push)";;
  esac
else
  git push origin main && echo "🚀 공개 완료 (1~2분 뒤 라이브)"
fi
