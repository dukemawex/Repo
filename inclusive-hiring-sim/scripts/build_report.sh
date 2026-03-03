#!/usr/bin/env bash
set -euo pipefail
mkdocs build -f report/mkdocs.yml -d site
