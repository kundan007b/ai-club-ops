"""
Scaffolding generator for AI Club operational templates.
Quickly scaffolds RFCs, project incubation briefs, and compute requests.
"""

import re
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional


TEMPLATES_DIR = Path(__file__).resolve().parent.parent.parent / "templates"


def sanitize_filename(title: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", title.lower())
    return re.sub(r"[-\s]+", "-", cleaned).strip("-")


def scaffold_rfc(title: str, output_dir: Path, author_name: str = "Member Name", author_email: str = "member@nalandauniv.edu.in") -> Path:
    template_path = TEMPLATES_DIR / "rfc-template.md"
    content = template_path.read_text(encoding="utf-8")
    
    today = datetime.now().strftime("%Y-%m-%d")
    deadline = (datetime.now() + timedelta(hours=72)).strftime("%Y-%m-%d %H:%M IST")
    slug = sanitize_filename(title)
    
    # Calculate next RFC number if directory exists
    existing = list(output_dir.glob("RFC-*.md"))
    next_num = len(existing) + 1
    rfc_num_str = f"{next_num:03d}"

    content = content.replace("[NUMBER]", rfc_num_str)
    content = content.replace("[PROPOSAL TITLE]", title)
    content = content.replace("[Name(s), Email(s)]", f"{author_name} ({author_email})")
    content = content.replace("YYYY-MM-DD", today)
    content = content.replace("YYYY-MM-DD 23:59 IST", deadline)

    target_file = output_dir / f"RFC-{rfc_num_str}-{slug}.md"
    output_dir.mkdir(parents=True, exist_ok=True)
    target_file.write_text(content, encoding="utf-8")
    return target_file


def scaffold_project(title: str, output_dir: Path, computational_lead: str = "Lead Dev", domain_lead: str = "Domain Researcher") -> Path:
    template_path = TEMPLATES_DIR / "project-proposal-template.md"
    content = template_path.read_text(encoding="utf-8")
    
    slug = sanitize_filename(title)
    content = content.replace("Project Codename", title)
    content = content.replace("Computational Lead Name", computational_lead)
    content = content.replace("Domain Specialist Name", domain_lead)

    target_file = output_dir / f"proposal-{slug}.md"
    output_dir.mkdir(parents=True, exist_ok=True)
    target_file.write_text(content, encoding="utf-8")
    return target_file


def scaffold_compute(title: str, output_dir: Path) -> Path:
    template_path = TEMPLATES_DIR / "compute-allocation-request.yml"
    content = template_path.read_text(encoding="utf-8")
    
    slug = sanitize_filename(title)
    today = datetime.now().strftime("%Y-%m-%d")
    end = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

    content = content.replace("pali-ocr-transformer", slug)
    content = content.replace("2026-10-01", today)
    content = content.replace("2026-10-15", end)

    target_file = output_dir / f"compute-request-{slug}.yml"
    output_dir.mkdir(parents=True, exist_ok=True)
    target_file.write_text(content, encoding="utf-8")
    return target_file


def scaffold_event(title: str, output_dir: Path) -> Path:
    template_path = TEMPLATES_DIR / "event-runbook-template.md"
    content = template_path.read_text(encoding="utf-8")
    
    slug = sanitize_filename(title)
    today = datetime.now().strftime("%Y-%m-%d")
    content = content.replace("[Event Title]", title)
    content = content.replace("YYYY-MM-DD", today)

    target_file = output_dir / f"runbook-{slug}.md"
    output_dir.mkdir(parents=True, exist_ok=True)
    target_file.write_text(content, encoding="utf-8")
    return target_file
