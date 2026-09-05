"""
CLI Interface for AI Club Operations (ai-ops).
Provides commands for validation, scaffolding, handbook compilation, and repository auditing.
"""

import sys
import argparse
from pathlib import Path
from typing import Optional

from ai_club_ops.validator import validate_file
from ai_club_ops.scaffolder import scaffold_rfc, scaffold_project, scaffold_compute, scaffold_event
from ai_club_ops.compiler import audit_repository, compile_handbook, BASE_DIR


def cmd_validate(args: argparse.Namespace) -> int:
    path = Path(args.file)
    print(f"🔍 Validating {path.name}...")
    success, doc_type, errors = validate_file(path)
    
    print(f"📄 Detected Type: {doc_type}")
    if success:
        print(f"✅ PASSED: Document satisfies all schemas and policy rules (e.g. '2-in-a-Pod').")
        return 0
    else:
        print(f"❌ FAILED with {len(errors)} violation(s):")
        for idx, err in enumerate(errors, 1):
            print(f"   {idx}. {err}")
        return 1


def cmd_scaffold(args: argparse.Namespace) -> int:
    out_dir = Path(args.dir) if args.dir else Path.cwd()
    t_type = args.type.lower()
    title = args.title

    if t_type == "rfc":
        res = scaffold_rfc(title, out_dir)
    elif t_type == "project":
        res = scaffold_project(title, out_dir)
    elif t_type == "compute":
        res = scaffold_compute(title, out_dir)
    elif t_type == "event":
        res = scaffold_event(title, out_dir)
    else:
        print(f"❌ Unknown type: {args.type}. Supported: rfc, project, compute, event")
        return 1

    print(f"✨ Successfully scaffolded {t_type.upper()}: {res.relative_to(Path.cwd()) if res.is_relative_to(Path.cwd()) else res}")
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    print("🔎 Auditing AI Club Operations repository...")
    ok, errors, warnings = audit_repository()
    
    if warnings:
        print(f"⚠️  {len(warnings)} Warning(s):")
        for w in warnings:
            print(f"   - {w}")

    if not ok:
        print(f"❌ {len(errors)} Error(s) encountered:")
        for e in errors:
            print(f"   - {e}")
        return 1

    print("✅ Repository audit clean! All SOP headers and Charter verified.")
    return 0


def cmd_compile(args: argparse.Namespace) -> int:
    out_path = Path(args.output) if args.output else (BASE_DIR / "HANDBOOK.md")
    print(f"📚 Compiling unified handbook into {out_path.name}...")
    compile_handbook(out_path)
    print(f"✅ Handbook successfully compiled! ({out_path.stat().st_size} bytes)")
    return 0


def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ai-ops",
        description="AI Club Nalanda University Operations & Governance CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # validate
    p_val = subparsers.add_parser("validate", help="Validate a project proposal or compute request")
    p_val.add_argument("file", help="Path to markdown proposal or YAML compute request")
    p_val.set_defaults(func=cmd_validate)

    # scaffold
    p_scaf = subparsers.add_parser("scaffold", help="Scaffold a new RFC, project proposal, or runbook")
    p_scaf.add_argument("--type", choices=["rfc", "project", "compute", "event"], required=True, help="Artifact type to scaffold")
    p_scaf.add_argument("--title", required=True, help="Title or codename")
    p_scaf.add_argument("--dir", default=None, help="Target output directory")
    p_scaf.set_defaults(func=cmd_scaffold)

    # audit
    p_audit = subparsers.add_parser("audit", help="Audit SOP repository integrity and formatting")
    p_audit.set_defaults(func=cmd_audit)

    # compile
    p_comp = subparsers.add_parser("compile", help="Compile all SOPs into a unified HANDBOOK.md")
    p_comp.add_argument("--output", default=None, help="Output file path (default: HANDBOOK.md)")
    p_comp.set_defaults(func=cmd_compile)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
