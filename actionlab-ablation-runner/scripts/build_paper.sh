#!/usr/bin/env bash
set -euo pipefail
if command -v typst >/dev/null 2>&1; then
  typst compile paper/paper.typ paper/paper.pdf
else
  echo "typst missing; creating placeholder PDF not possible in pure shell" >&2
  exit 1
fi
