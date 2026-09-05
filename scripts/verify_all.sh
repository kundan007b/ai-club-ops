#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

echo "=== 1. Checking Python Environment ==="
PYTHON_BIN="python3"
if [ -f "$DIR/../../.venv/bin/python" ]; then
    PYTHON_BIN="$DIR/../../.venv/bin/python"
elif [ -f "$DIR/../.venv/bin/python" ]; then
    PYTHON_BIN="$DIR/../.venv/bin/python"
fi
echo "Using Python: $PYTHON_BIN"

echo "=== 2. Running Repository Integrity Audit ==="
PYTHONPATH="src" $PYTHON_BIN -m ai_club_ops.cli audit

echo "=== 3. Compiling Unified Operational Handbook ==="
PYTHONPATH="src" $PYTHON_BIN scripts/build_docs.py

echo "=== 4. Validating Default Proposal and Compute Templates ==="
PYTHONPATH="src" $PYTHON_BIN -m ai_club_ops.cli validate templates/project-proposal-template.md
PYTHONPATH="src" $PYTHON_BIN -m ai_club_ops.cli validate templates/compute-allocation-request.yml

echo "=== 5. Running Test Suite (unittest) ==="
PYTHONPATH="src" $PYTHON_BIN -m unittest discover -s tests -p "test_*.py" -v

echo "=== ALL VERIFICATIONS PASSED SUCCESSFULLY! ==="
