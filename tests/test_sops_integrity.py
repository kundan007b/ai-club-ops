"""
Tests verifying integrity, headers, and metadata across all codified SOPs, Charter, and Team Structure.
"""

import unittest
from pathlib import Path
from ai_club_ops.compiler import parse_sop_metadata, audit_repository

BASE_DIR = Path(__file__).resolve().parent.parent
SOPS_DIR = BASE_DIR / "sops"
CHARTER_PATH = BASE_DIR / "CHARTER.md"
TEAM_STRUCTURE_PATH = BASE_DIR / "TEAM_STRUCTURE.md"


class TestSopsIntegrity(unittest.TestCase):

    def test_charter_exists_and_articles_complete(self):
        self.assertTrue(CHARTER_PATH.exists())
        charter_text = CHARTER_PATH.read_text(encoding="utf-8")
        self.assertIn("Founding Charter of the AI Club — Nalanda University", charter_text)
        self.assertIn("https://aiclub.nalandalibrary.com", charter_text)
        self.assertIn("Article I: Name and Identity", charter_text)
        self.assertIn("Article II: Foundational Premise", charter_text)
        self.assertIn("Article III: Core Principles of Governance", charter_text)
        self.assertIn("Article IV: Intellectual Property & Public Good", charter_text)
        self.assertIn("Article V: Responsible AI & Civilizational Ethics", charter_text)
        self.assertIn("Article VI: Amendments", charter_text)
        self.assertIn("80%", charter_text)
        self.assertIn("exclusive, non-transferable private property of the Founder", charter_text)

    def test_domain_non_transferable_in_succession_docs(self):
        sop11_path = SOPS_DIR / "01_GOVERNANCE_AND_SUCCESSION" / "SOP-011-annual-succession-and-asset-handoff.md"
        sop11_text = sop11_path.read_text(encoding="utf-8")
        self.assertIn("NON-TRANSFERABLE", sop11_text)
        self.assertIn("Sole property of Founder", sop11_text)

        checklist_path = BASE_DIR / "templates" / "succession-handoff-checklist.md"
        checklist_text = checklist_path.read_text(encoding="utf-8")
        self.assertIn("NON-TRANSFERABLE", checklist_text)
        self.assertIn("Founder", checklist_text)

    def test_team_structure_and_task_ownership(self):
        self.assertTrue(TEAM_STRUCTURE_PATH.exists())
        team_text = TEAM_STRUCTURE_PATH.read_text(encoding="utf-8")
        self.assertIn("Master Team Topology", team_text)
        self.assertIn("Master Task Ownership & RACI Matrix", team_text)
        self.assertIn("Directly Responsible Individual (DRI)", team_text)
        self.assertIn("80% Supermajority", team_text)
        self.assertIn("SOP-014", team_text)

    def test_all_categories_populated(self):
        expected_categories = [
            "01_GOVERNANCE_AND_SUCCESSION",
            "02_MEMBER_LIFECYCLE_AND_COMMUNITY",
            "03_PROJECT_INCUBATION_AND_INNOVATION",
            "04_EVENTS_AND_KNOWLEDGE_SHARING",
            "05_FINANCE_GRANTS_AND_TRANSPARENCY",
            "06_AI_ETHICS_DATA_AND_SAFETY"
        ]
        for cat in expected_categories:
            cat_dir = SOPS_DIR / cat
            self.assertTrue(cat_dir.exists(), f"Category directory {cat} does not exist")
            files = list(cat_dir.glob("*.md"))
            self.assertGreaterEqual(len(files), 2, f"Category {cat} has fewer than 2 SOPs: {files}")

    def test_sop_metadata_structure(self):
        sop_files = list(SOPS_DIR.rglob("*.md"))
        self.assertGreaterEqual(len(sop_files), 19, f"Expected at least 19 SOPs, found {len(sop_files)}")

        for sop in sop_files:
            meta = parse_sop_metadata(sop)
            self.assertTrue(meta["code"].startswith("SOP-"), f"Invalid code in {sop.name}: {meta['code']}")
            self.assertNotEqual(meta["title"], "Untitled", f"Missing title in {sop.name}")
            self.assertNotEqual(meta["category"], "General", f"Missing category in {sop.name}")
            self.assertNotEqual(meta["effective_date"], "N/A", f"Missing effective date in {sop.name}")

    def test_audit_passes_clean(self):
        ok, errors, warnings = audit_repository()
        self.assertTrue(ok, f"Audit failed with errors: {errors}")
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(warnings), 0, f"Audit generated unexpected warnings: {warnings}")


if __name__ == "__main__":
    unittest.main()
