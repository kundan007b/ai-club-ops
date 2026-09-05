#!/usr/bin/env python3
"""
Build script to compile the unified AI Club Operational Handbook (HANDBOOK.md).
"""

import sys
from pathlib import Path

# Add src to sys.path
pkg_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pkg_dir / "src"))

from ai_club_ops.compiler import compile_handbook

def main():
    out_file = pkg_dir / "HANDBOOK.md"
    print(f"Building {out_file.name}...")
    compile_handbook(out_file)
    print(f"Build complete. Output written to {out_file}")

if __name__ == "__main__":
    main()
