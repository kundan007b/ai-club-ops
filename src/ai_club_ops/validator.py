"""
Validator engine for AI Club proposals and compute requests.
Enforces the '2-in-a-Pod' multidisciplinary rule and schema compliance.
Supports both jsonschema library and a self-contained schema validator fallback.
"""

import os
import re
import json
import yaml
from pathlib import Path
from typing import Dict, Any, Tuple, List, Optional

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


SCHEMAS_DIR = Path(__file__).resolve().parent.parent.parent / "schemas"


def load_schema(schema_name: str) -> Dict[str, Any]:
    schema_path = SCHEMAS_DIR / schema_name
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found at {schema_path}")
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _simple_validate(data: Any, schema: Dict[str, Any], path: str = "") -> List[str]:
    """Lightweight self-contained schema validator fallback when jsonschema is not installed."""
    errors = []
    expected_type = schema.get("type")

    # Type checking
    if expected_type == "object":
        if not isinstance(data, dict):
            return [f"Expected object at '{path or 'root'}', got {type(data).__name__}"]
        
        # Check required
        for req in schema.get("required", []):
            if req not in data:
                errors.append(f"Missing required property '{req}' at '{path or 'root'}'")
        
        # Check properties
        props = schema.get("properties", {})
        for k, prop_schema in props.items():
            if k in data:
                sub_path = f"{path}.{k}" if path else k
                errors.extend(_simple_validate(data[k], prop_schema, sub_path))

    elif expected_type == "array":
        if not isinstance(data, list):
            return [f"Expected array at '{path or 'root'}', got {type(data).__name__}"]
        
        min_items = schema.get("minItems")
        if min_items is not None and len(data) < min_items:
            errors.append(f"Array at '{path}' requires at least {min_items} items, got {len(data)}")

        item_schema = schema.get("items")
        if item_schema:
            for idx, item in enumerate(data):
                errors.extend(_simple_validate(item, item_schema, f"{path}[{idx}]"))

    elif expected_type == "string":
        if not isinstance(data, str):
            errors.append(f"Expected string at '{path}', got {type(data).__name__}")
        else:
            min_len = schema.get("minLength")
            if min_len is not None and len(data) < min_len:
                errors.append(f"String at '{path}' must be at least {min_len} characters long")
            max_len = schema.get("maxLength")
            if max_len is not None and len(data) > max_len:
                errors.append(f"String at '{path}' cannot exceed {max_len} characters")

    elif expected_type in ["number", "integer"]:
        if expected_type == "integer" and not (isinstance(data, int) and not isinstance(data, bool)):
            errors.append(f"Expected integer at '{path}', got {type(data).__name__}")
        elif expected_type == "number" and not isinstance(data, (int, float)):
            errors.append(f"Expected number at '{path}', got {type(data).__name__}")
        else:
            minimum = schema.get("minimum")
            if minimum is not None and data < minimum:
                errors.append(f"Value at '{path}' must be >= {minimum}, got {data}")
            maximum = schema.get("maximum")
            if maximum is not None and data > maximum:
                errors.append(f"Value at '{path}' must be <= {maximum}, got {data}")

    elif expected_type == "boolean":
        if not isinstance(data, bool):
            errors.append(f"Expected boolean at '{path}', got {type(data).__name__}")

    # Enums
    if "enum" in schema and data not in schema["enum"]:
        errors.append(f"Value '{data}' at '{path}' is not one of allowed values: {schema['enum']}")

    # Const
    if "const" in schema and data != schema["const"]:
        errors.append(f"Value '{data}' at '{path}' must equal const '{schema['const']}'")

    return errors


def validate_against_schema(data: Any, schema: Dict[str, Any]) -> List[str]:
    """Validates using jsonschema if available, otherwise uses built-in validator."""
    if HAS_JSONSCHEMA:
        validator = jsonschema.Draft202012Validator(schema)
        errors = []
        for err in validator.iter_errors(data):
            errors.append(f"Schema error at '{'.'.join([str(p) for p in err.path])}': {err.message}")
        return errors
    else:
        return _simple_validate(data, schema)


def extract_yaml_from_markdown(content: str) -> Optional[Dict[str, Any]]:
    """Extracts first yaml codeblock from markdown if present."""
    match = re.search(r"```ya?ml\s*\n(.*?)\n```", content, re.DOTALL | re.IGNORECASE)
    if match:
        return yaml.safe_load(match.group(1))
    return None


def validate_compute_request(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validates compute request against compute_request.schema.json and operational quotas."""
    schema = load_schema("compute_request.schema.json")
    errors = validate_against_schema(data, schema)

    if errors:
        return False, errors

    # Business rule: Tier-2 maximum budget check
    alloc = data.get("allocation_details", {})
    tier = alloc.get("tier")
    cost = alloc.get("estimated_cost_inr", 0)

    if tier == "Tier-1" and cost > 0:
        errors.append("Tier-1 compute must be free/self-service (estimated_cost_inr must be 0).")
    elif tier == "Tier-2" and cost > 3000:
        errors.append(f"Tier-2 micro-quota cannot exceed ₹3,000 (requested: ₹{cost}). Request Tier-3 via RFC.")

    # Business rule: Auto-shutdown
    workload = data.get("workload_specification", {})
    shutdown = workload.get("idle_auto_shutdown_minutes", 0)
    if shutdown > 30:
        errors.append("idle_auto_shutdown_minutes cannot exceed 30 minutes to prevent cloud bill waste.")

    return len(errors) == 0, errors


def validate_project_proposal(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validates project proposal against project_proposal.schema.json and the 2-in-a-Pod rule."""
    schema = load_schema("project_proposal.schema.json")
    errors = validate_against_schema(data, schema)

    if errors:
        return False, errors

    # Enforce '2-in-a-Pod' Law
    authors = data.get("authors", [])
    has_tech = any(a.get("role") == "technical_lead" for a in authors)
    has_domain = any(a.get("role") == "domain_lead" for a in authors)

    if not (has_tech and has_domain):
        errors.append(
            "VIOLATION OF THE '2-IN-A-POD' RULE (SOP-021): "
            "A project must have at least one 'technical_lead' and at least one 'domain_lead' "
            "to bridge technical methods with authentic domain inquiries."
        )

    return len(errors) == 0, errors


def validate_file(file_path: Path) -> Tuple[bool, str, List[str]]:
    """Inspects file type, parses YAML, and validates."""
    if not file_path.exists():
        return False, "File Not Found", [f"File {file_path} does not exist."]

    text = file_path.read_text(encoding="utf-8")
    data = None

    if file_path.suffix.lower() in [".yml", ".yaml"]:
        try:
            data = yaml.safe_load(text)
        except Exception as e:
            return False, "YAML Parse Error", [str(e)]
        if not isinstance(data, dict):
            return False, "Format Error", ["YAML root must be a dictionary."]
        
        # Determine schema by keys
        if "allocation_details" in data:
            success, errs = validate_compute_request(data)
            return success, "Compute Allocation Request", errs
        else:
            return False, "Unknown YAML Schema", ["Unrecognized YAML structure."]

    elif file_path.suffix.lower() in [".md", ".markdown"]:
        data = extract_yaml_from_markdown(text)
        if not data:
            return False, "Missing Metadata", ["No YAML metadata code block (```yaml ... ```) found in Markdown file."]
        
        if "target_stage" in data:
            success, errs = validate_project_proposal(data)
            return success, "Project Incubation Proposal", errs
        else:
            return False, "Unknown Markdown Schema", ["YAML block does not match project proposal format."]

    return False, "Unsupported File Type", [f"Unsupported extension: {file_path.suffix}"]
