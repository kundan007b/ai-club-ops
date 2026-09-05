"""
Tests for JSON schemas and policy validation rules (e.g. '2-in-a-Pod', compute quotas).
"""

import unittest
from pathlib import Path
from ai_club_ops.validator import (
    validate_project_proposal,
    validate_compute_request,
    validate_file
)

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"


class TestSchemasAndPolicies(unittest.TestCase):

    def test_valid_project_proposal_template(self):
        proposal_file = TEMPLATES_DIR / "project-proposal-template.md"
        ok, doc_type, errors = validate_file(proposal_file)
        self.assertTrue(ok, f"Default project proposal template failed validation: {errors}")
        self.assertEqual(doc_type, "Project Incubation Proposal")

    def test_2_in_a_pod_rule_enforcement(self):
        # Only technical leads, missing domain lead
        invalid_data = {
            "title": "Toy Transformer",
            "authors": [
                {
                    "name": "Dev One",
                    "email": "dev1@nalandauniv.edu.in",
                    "role": "technical_lead",
                    "background": "Computer Science"
                },
                {
                    "name": "Dev Two",
                    "email": "dev2@nalandauniv.edu.in",
                    "role": "technical_lead",
                    "background": "IT"
                }
            ],
            "target_stage": "SPARK",
            "primary_discipline": "Machine Learning",
            "requested_tier": "Tier-1",
            "estimated_duration_weeks": 4
        }
        ok, errors = validate_project_proposal(invalid_data)
        self.assertFalse(ok)
        self.assertTrue(any("2-IN-A-POD" in err for err in errors))

    def test_valid_compute_request_template(self):
        compute_file = TEMPLATES_DIR / "compute-allocation-request.yml"
        ok, doc_type, errors = validate_file(compute_file)
        self.assertTrue(ok, f"Default compute request template failed validation: {errors}")
        self.assertEqual(doc_type, "Compute Allocation Request")

    def test_compute_quota_limits(self):
        # Tier-2 cost exceeding ₹3,000 threshold
        over_budget = {
            "version": "1.0",
            "project": {
                "codename": "heavy-llm",
                "github_repo": "https://github.com/nalanda-ai-club/heavy",
                "lead_name": "Lead",
                "lead_email": "lead@nalandauniv.edu.in",
                "pod_members": ["lead@nalandauniv.edu.in", "domain@nalandauniv.edu.in"]
            },
            "allocation_details": {
                "tier": "Tier-2",
                "provider": "RunPod",
                "hardware_type": "4x H100",
                "estimated_gpu_hours": 100,
                "estimated_cost_inr": 8500,  # Exceeds 3000
                "start_date": "2026-10-01",
                "end_date": "2026-10-15"
            },
            "workload_specification": {
                "framework": "PyTorch",
                "dataset_size_gb": 10,
                "batch_size": 32,
                "max_runtime_per_job_hours": 12,
                "idle_auto_shutdown_minutes": 20
            },
            "safety_and_hygiene": {
                "keys_vault_confirmed": True,
                "public_loss_curves_agreement": True,
                "open_source_commitment": True
            }
        }
        ok, errors = validate_compute_request(over_budget)
        self.assertFalse(ok)
        self.assertTrue(any("cannot exceed ₹3,000" in err for err in errors))

    def test_auto_shutdown_enforcement(self):
        # Idle shutdown > 30 mins
        long_idle = {
            "version": "1.0",
            "project": {
                "codename": "idle-test",
                "github_repo": "https://github.com/nalanda-ai-club/idle",
                "lead_name": "Lead",
                "lead_email": "lead@nalandauniv.edu.in",
                "pod_members": ["lead@nalandauniv.edu.in", "domain@nalandauniv.edu.in"]
            },
            "allocation_details": {
                "tier": "Tier-2",
                "provider": "RunPod",
                "hardware_type": "1x RTX 4090",
                "estimated_gpu_hours": 10,
                "estimated_cost_inr": 1500,
                "start_date": "2026-10-01",
                "end_date": "2026-10-15"
            },
            "workload_specification": {
                "framework": "PyTorch",
                "dataset_size_gb": 2,
                "batch_size": 16,
                "max_runtime_per_job_hours": 4,
                "idle_auto_shutdown_minutes": 60  # Violates max 30 mins
            },
            "safety_and_hygiene": {
                "keys_vault_confirmed": True,
                "public_loss_curves_agreement": True,
                "open_source_commitment": True
            }
        }
        ok, errors = validate_compute_request(long_idle)
        self.assertFalse(ok)
        self.assertTrue(any("idle_auto_shutdown_minutes cannot exceed 30" in err for err in errors))


if __name__ == "__main__":
    unittest.main()
