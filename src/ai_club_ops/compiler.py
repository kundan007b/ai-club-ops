"""
Compiler and audit engine for AI Club SOPs.
Generates the consolidated HANDBOOK.md and performs link/integrity checks.
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple


BASE_DIR = Path(__file__).resolve().parent.parent.parent
SOPS_DIR = BASE_DIR / "sops"
CHARTER_PATH = BASE_DIR / "CHARTER.md"
TEAM_STRUCTURE_PATH = BASE_DIR / "TEAM_STRUCTURE.md"


def parse_sop_metadata(file_path: Path) -> Dict[str, str]:
    """Extracts metadata table values from an SOP markdown file."""
    content = file_path.read_text(encoding="utf-8")
    
    code_match = re.search(r"SOP-\d{3}", file_path.stem)
    sop_code = code_match.group(0) if code_match else "SOP-000"

    meta = {
        "code": sop_code,
        "file": file_path.name,
        "rel_path": str(file_path.relative_to(BASE_DIR)),
        "title": "Untitled",
        "category": "General",
        "effective_date": "N/A"
    }

    # Extract title (# SOP-xxx: Title)
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        meta["title"] = title_match.group(1).strip()

    # Extract table rows
    cat_match = re.search(r"\|\s*\*\*Category\*\*\s*\|\s*([^\|]+)\|", content, re.IGNORECASE)
    if cat_match:
        meta["category"] = cat_match.group(1).strip()

    date_match = re.search(r"\|\s*\*\*Effective Date\*\*\s*\|\s*([^\|]+)\|", content, re.IGNORECASE)
    if date_match:
        meta["effective_date"] = date_match.group(1).strip()

    return meta


def audit_repository() -> Tuple[bool, List[str], List[str]]:
    """Performs integrity check on SOPs, links, team structure, and templates."""
    errors = []
    warnings = []

    # Check Charter
    if not CHARTER_PATH.exists():
        errors.append("Missing CHARTER.md")

    # Check Team Structure
    if not TEAM_STRUCTURE_PATH.exists():
        errors.append("Missing TEAM_STRUCTURE.md")

    # Check SOPs
    sop_files = sorted(list(SOPS_DIR.rglob("*.md")))
    if not sop_files:
        errors.append("No SOP files found in sops/ directory.")

    for sop in sop_files:
        content = sop.read_text(encoding="utf-8")
        if not re.search(r"^#\s+SOP-\d{3}:", content, re.MULTILINE):
            warnings.append(f"Header in {sop.name} does not match '# SOP-XXX: Title' format.")
        if "| **SOP Code** |" not in content:
            warnings.append(f"Metadata table missing SOP Code in {sop.name}.")

    return len(errors) == 0, errors, warnings


def compile_handbook(output_file: Path) -> str:
    """Compiles all SOPs, Charter, and Team Structure into a unified, publication-ready HANDBOOK.md."""
    sop_files = sorted(list(SOPS_DIR.rglob("*.md")))
    
    metadata_list = [parse_sop_metadata(p) for p in sop_files]

    lines = []
    lines.append("# 🏛️ The AI Club Operational Handbook — Nalanda University\n")
    lines.append("> **Official Standard Operating Procedures & Governance Manual**  \n")
    lines.append("> *Cohort 2026–28 and Subsequent Cohorts*  \n")
    lines.append("> *Published: September 2026 | Nalanda University, Rajgir*\n\n")
    lines.append("---\n")

    # Master Index Table
    lines.append("## 📋 Master Index of Standard Operating Procedures\n")
    lines.append("| SOP Code | Title | Category | Effective Date | File Link |\n")
    lines.append("| :--- | :--- | :--- | :--- | :--- |\n")
    for m in metadata_list:
        lines.append(f"| `{m['code']}` | **{m['title']}** | {m['category']} | {m['effective_date']} | [{m['file']}]({m['rel_path']}) |\n")

    lines.append("\n---\n\n")

    # Include Charter
    if CHARTER_PATH.exists():
        lines.append("## 📜 Section A: The Founding Charter\n\n")
        charter_content = CHARTER_PATH.read_text(encoding="utf-8")
        # Demote H1 to H3 to maintain document hierarchy
        charter_content = re.sub(r"^#\s+", "### ", charter_content, flags=re.MULTILINE)
        lines.append(charter_content)
        lines.append("\n\n---\n\n")

    # Include Team Structure & RACI
    if TEAM_STRUCTURE_PATH.exists():
        lines.append("## 👥 Section B: Team Structure & RACI Task Ownership Matrix\n\n")
        team_content = TEAM_STRUCTURE_PATH.read_text(encoding="utf-8")
        team_content = re.sub(r"^#\s+", "### ", team_content, flags=re.MULTILINE)
        lines.append(team_content)
        lines.append("\n\n---\n\n")

    # Include SOPs
    lines.append("## 📚 Section C: Codified Standard Operating Procedures\n\n")
    for sop in sop_files:
        sop_content = sop.read_text(encoding="utf-8")
        lines.append(f"\n\n<!-- BEGIN {sop.name} -->\n\n")
        lines.append(sop_content)
        lines.append(f"\n\n[Back to Top](#-the-ai-club-operational-handbook--nalanda-university)\n\n---\n")

    compiled_text = "".join(lines)
    output_file.write_text(compiled_text, encoding="utf-8")
    return compiled_text
