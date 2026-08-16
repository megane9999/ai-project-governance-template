#!/usr/bin/env python3
"""Validate the project-governance repository without third-party packages."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "START_HERE.md",
    "AGENTS.md",
    ".github/copilot-instructions.md",
    "project.toml",
    "PROJECT.md",
    "docs/ARCHITECTURE.md",
    "docs/CHARTER.md",
    "docs/STRATEGY.md",
    "docs/OPERATIONS.md",
    "docs/GOVERNANCE.md",
    "docs/INFORMATION_POLICY.md",
    "initiatives/README.md",
    "research/README.md",
    "experiments/README.md",
    "decisions/README.md",
    "metrics/README.md",
    "risks/README.md",
    "budget/ledger.csv",
    "archive/README.md",
)

RECORDS = {
    "initiatives": {
        "prefix": "WRK",
        "statuses": {"Inbox", "Researching", "Planned", "Active", "Blocked", "Parked", "Completed", "Cancelled"},
        "sections": ("Conclusion", "Intended outcome", "Completion and exit"),
    },
    "research": {
        "prefix": "RES",
        "statuses": {"Draft", "Current", "Stale", "Superseded"},
        "sections": ("Conclusion", "Question and scope", "Claims and evidence", "Freshness"),
    },
    "experiments": {
        "prefix": "EXP",
        "statuses": {"Draft", "Ready", "Running", "Completed", "Cancelled"},
        "sections": ("Pre-registration", "Change log", "Result", "Decision", "Lessons"),
    },
    "decisions": {
        "prefix": "DEC",
        "statuses": {"Proposed", "Approved", "Rejected", "Superseded"},
        "sections": ("Decision", "Reason", "Evidence", "Alternatives", "Risks and limits", "Revisit condition", "Outcome addenda"),
    },
    "risks": {
        "prefix": "RSK",
        "statuses": {"Open", "Mitigating", "Accepted", "Closed"},
        "sections": ("Risk statement", "Assessment", "Signals", "Response", "Residual risk", "History"),
    },
}

IGNORED_DIRS = {".git", "__pycache__", ".venv", "venv", "tmp", "dist", "build", "local", "private"}
TEXT_SUFFIXES = {".md", ".txt", ".toml", ".yml", ".yaml", ".csv", ".py"}
PLACEHOLDER = re.compile(r"<<[^<>\n]+>>")
INSTANCE_FILES = {
    "project.toml",
    "PROJECT.md",
    "docs/CHARTER.md",
    "docs/STRATEGY.md",
    "docs/GOVERNANCE.md",
    "docs/INFORMATION_POLICY.md",
    "docs/SELF_REVIEW.md",
    "initiatives/README.md",
    "research/README.md",
    "experiments/README.md",
    "decisions/README.md",
    "metrics/README.md",
    "risks/README.md",
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
LOCAL_PATHS = (
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.IGNORECASE),
    re.compile(r"/(?:Users|home)/[^/\s]+"),
)
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "generic sk token": re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORED_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line[:1].isspace():
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def load_config(errors: list[str]) -> dict:
    try:
        text = (ROOT / "project.toml").read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"invalid project.toml: {exc}")
        return {}
    config: dict[str, object] = {}
    schema_match = re.search(r"^schema_version\s*=\s*(\d+)\s*$", text, flags=re.MULTILINE)
    mode_match = re.search(r'^mode\s*=\s*"([^"]+)"\s*$', text, flags=re.MULTILINE)
    config["schema_version"] = int(schema_match.group(1)) if schema_match else None
    config["mode"] = mode_match.group(1) if mode_match else None
    if config.get("schema_version") != 1:
        errors.append("project.toml schema_version must be 1")
    if config.get("mode") not in {"template", "active"}:
        errors.append('project.toml mode must be "template" or "active"')
    return config


def check_markdown_links(errors: list[str]) -> None:
    for path in iter_files(ROOT):
        if path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        if text is None:
            continue
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>").split()[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target or "<<" in target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"broken link: {path.relative_to(ROOT)} -> {raw_target}")


def check_records(errors: list[str]) -> None:
    seen: dict[str, Path] = {}
    for directory_name, rule in RECORDS.items():
        directory = ROOT / directory_name
        registry = read_text(directory / "README.md") or ""
        prefix = rule["prefix"]
        for path in directory.glob(f"{prefix}-*.md"):
            text = read_text(path) or ""
            meta = parse_front_matter(text)
            record_id = meta.get("id", "")
            expected = re.match(rf"({prefix}-\d{{4,}})-", path.name)
            expected_id = expected.group(1) if expected else ""
            if not expected_id:
                errors.append(f"invalid record filename: {path.relative_to(ROOT)}")
            if record_id != expected_id:
                errors.append(f"record id mismatch: {path.relative_to(ROOT)} has id={record_id!r}")
            if record_id in seen:
                errors.append(f"duplicate id {record_id}: {seen[record_id].relative_to(ROOT)} and {path.relative_to(ROOT)}")
            elif record_id:
                seen[record_id] = path
            status = meta.get("status", "")
            if status not in rule["statuses"]:
                errors.append(f"invalid status {status!r}: {path.relative_to(ROOT)}")
            for section in rule["sections"]:
                if not re.search(rf"^## {re.escape(section)}\s*$", text, flags=re.MULTILINE | re.IGNORECASE):
                    errors.append(f"missing section {section!r}: {path.relative_to(ROOT)}")
            if record_id and record_id not in registry:
                errors.append(f"record missing from {directory_name}/README.md: {record_id}")


def check_budget(errors: list[str]) -> None:
    path = ROOT / "budget" / "ledger.csv"
    text = read_text(path)
    if text is None:
        return
    expected = "entry_id,date,related_id,category,description,currency,planned_amount,actual_amount,status,approved_by_role,approval_decision,external_system_ref,notes"
    first_line = text.splitlines()[0] if text.splitlines() else ""
    if first_line != expected:
        errors.append("budget/ledger.csv header does not match the documented schema")


def check_placeholders(config: dict, errors: list[str]) -> None:
    if config.get("mode") != "active":
        return
    for relative_name in sorted(INSTANCE_FILES):
        path = ROOT / relative_name
        if not path.is_file():
            continue
        text = read_text(path)
        if text is None:
            continue
        for match in PLACEHOLDER.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"unresolved placeholder: {relative_name}:{line} {match.group(0)}")


def check_sensitive_patterns(errors: list[str]) -> None:
    for path in iter_files(ROOT):
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore", ".python-version"}:
            continue
        text = read_text(path)
        if text is None:
            continue
        relative = path.relative_to(ROOT)
        for label, pattern in SECRET_PATTERNS.items():
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"possible {label}: {relative}:{line}")
        for pattern in LOCAL_PATHS:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"local absolute path: {relative}:{line}")


def load_denylist(path: Path | None, errors: list[str]) -> list[str]:
    if path is None:
        default = ROOT / "privacy-denylist.txt"
        path = default if default.exists() else None
    if path is None:
        return []
    try:
        terms = [line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines()]
    except OSError as exc:
        errors.append(f"cannot read denylist: {exc}")
        return []
    return [term for term in terms if term and not term.startswith("#")]


def check_denylist(terms: list[str], errors: list[str]) -> None:
    if not terms:
        return
    lowered_terms = [(term, term.casefold()) for term in terms]
    for path in iter_files(ROOT):
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore", ".python-version"}:
            continue
        text = read_text(path)
        if text is None:
            continue
        folded = text.casefold()
        relative = path.relative_to(ROOT)
        for original, needle in lowered_terms:
            index = folded.find(needle)
            if index >= 0:
                line = text.count("\n", 0, index) + 1
                errors.append(f"denylist match {original!r}: {relative}:{line}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Treat all validation findings as errors")
    parser.add_argument("--denylist", type=Path, help="Private one-term-per-line release denylist")
    args = parser.parse_args()

    errors: list[str] = []
    check_required(errors)
    config = load_config(errors)
    check_markdown_links(errors)
    check_records(errors)
    check_budget(errors)
    check_placeholders(config, errors)
    check_sensitive_patterns(errors)
    terms = load_denylist(args.denylist, errors)
    check_denylist(terms, errors)

    if errors:
        print(f"FAIL: {len(errors)} finding(s)")
        for finding in sorted(set(errors)):
            print(f"- {finding}")
        return 1 if args.strict else 0

    print(f"PASS: repository structure is valid (mode={config.get('mode', 'unknown')})")
    if terms:
        print(f"PASS: denylist scan completed with {len(terms)} term(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
