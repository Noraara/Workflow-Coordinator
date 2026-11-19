"""Check handoff shape and optional context/result identity."""

import argparse
import json
from pathlib import Path

IDENTITY_FIELDS = ("project_id", "task_id", "scope")
ACCEPTED_SCHEMAS = ("atlas-workflow/v1", "atlas-forge/v1")
CHECK_STATUSES = ("pass", "fail", "unverified", "not-applicable")
LIST_FIELDS = {
    "context": ("constraints", "decisions", "evidence", "unknowns", "acceptance"),
    "result": ("changes", "decisions", "checks", "findings", "unresolved"),
}


def validate(packet):
    if not isinstance(packet, dict):
        return ["packet must be an object"]

    errors = []
    for key in IDENTITY_FIELDS:
        value = packet.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"missing {key}")
    if packet.get("schema") not in ACCEPTED_SCHEMAS:
        errors.append("unsupported schema")

    kind = packet.get("kind")
    if kind not in ("context", "result"):
        return [*errors, "invalid kind"]
    for key in LIST_FIELDS[kind]:
        if not isinstance(packet.get(key), list):
            errors.append(f"{key} must be a list")

    if kind == "result":
        if not isinstance(packet.get("next_action"), str):
            errors.append("missing next_action")
        checks = packet.get("checks")
        if isinstance(checks, list):
            for check in checks:
                if not isinstance(check, dict):
                    errors.append("check must be an object")
                    continue
                name = check.get("name")
                if not isinstance(name, str) or not name.strip():
                    errors.append("check missing name")
                if check.get("status") not in CHECK_STATUSES:
                    errors.append("invalid check status")
                if check.get("status") == "pass":
                    for key in ("evidence", "observed"):
                        value = check.get(key)
                        if not value or isinstance(value, str) and not value.strip():
                            errors.append(f"pass requires {key}")
    return errors


def compare_identity(result, context):
    if result.get("kind") != "result" or context.get("kind") != "context":
        return ["--context compares a result packet with a context packet"]
    return [
        f"result {key} does not match context"
        for key in IDENTITY_FIELDS
        if result[key] != context[key]
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("--context", type=Path)
    args = parser.parse_args()
    try:
        packet = json.loads(args.packet.read_text(encoding="utf-8-sig"))
        errors = validate(packet)
        if args.context is not None:
            context = json.loads(args.context.read_text(encoding="utf-8-sig"))
            context_errors = validate(context)
            if not errors and not context_errors:
                errors.extend(compare_identity(packet, context))
            errors.extend(f"context: {error}" for error in context_errors)
    except (OSError, ValueError) as error:
        errors = [str(error)]
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
