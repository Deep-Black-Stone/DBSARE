#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
echo "[DBSARE] Linux foundation installer"
python3 --version
python3 -m pip install --user -e .
echo "[DBSARE] installed. Run: dbsare status"
