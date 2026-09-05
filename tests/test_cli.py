"""
Tests for ai-ops CLI commands and operations.
"""

import unittest
import tempfile
from pathlib import Path
from ai_club_ops.cli import main

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"


class TestCli(unittest.TestCase):

    def test_cli_validate_success(self):
        res = main(["validate", str(TEMPLATES_DIR / "compute-allocation-request.yml")])
        self.assertEqual(res, 0)

    def test_cli_scaffold_rfc(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            res = main(["scaffold", "--type", "rfc", "--title", "Test Proposal", "--dir", str(tmp_path)])
            self.assertEqual(res, 0)
            scaffolded_files = list(tmp_path.glob("RFC-*.md"))
            self.assertEqual(len(scaffolded_files), 1)
            content = scaffolded_files[0].read_text(encoding="utf-8")
            self.assertIn("Test Proposal", content)
            self.assertIn("72-Hour Consent Deadline", content)

    def test_cli_scaffold_project(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            res = main(["scaffold", "--type", "project", "--title", "Bihar Groundwater AI", "--dir", str(tmp_path)])
            self.assertEqual(res, 0)
            scaffolded_files = list(tmp_path.glob("proposal-*.md"))
            self.assertEqual(len(scaffolded_files), 1)
            content = scaffolded_files[0].read_text(encoding="utf-8")
            self.assertIn("Bihar Groundwater AI", content)
            self.assertIn("technical_lead", content)
            self.assertIn("domain_lead", content)

    def test_cli_audit(self):
        res = main(["audit"])
        self.assertEqual(res, 0)

    def test_cli_compile(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_handbook = Path(tmp_dir) / "TEST_HANDBOOK.md"
            res = main(["compile", "--output", str(out_handbook)])
            self.assertEqual(res, 0)
            self.assertTrue(out_handbook.exists())
            content = out_handbook.read_text(encoding="utf-8")
            self.assertIn("The AI Club Operational Handbook", content)
            self.assertIn("Master Index of Standard Operating Procedures", content)
            self.assertIn("SOP-010", content)
            self.assertIn("SOP-061", content)


if __name__ == "__main__":
    unittest.main()
