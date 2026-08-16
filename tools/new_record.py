#!/usr/bin/env python3
"""Create the next governance record from a repository template."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date
from pathlib import Path


CONFIG = {
    "initiative": ("initiatives", "WRK", "initiative.md"),
    "research": ("research", "RES", "research.md"),
    "experiment": ("experiments", "EXP", "experiment.md"),
    "decision": ("decisions", "DEC", "decision.md"),
    "risk": ("risks", "RSK", "risk.md"),
}


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    return slug[:60] or "record"


def next_id(directory: Path, prefix: str) -> str:
    pattern = re.compile(rf"^{re.escape(prefix)}-(\d{{3,}})(?:-|\.md)")
    numbers = []
    for path in directory.glob(f"{prefix}-*.md"):
        match = pattern.match(path.name)
        if match:
            numbers.append(int(match.group(1)))
    return f"{prefix}-{max(numbers, default=0) + 1:04d}"


def render(template: str, record_id: str, title: str) -> str:
    prefix = record_id.split("-", 1)[0]
    rendered = template.replace(f"{prefix}-NNN", record_id)
    rendered = re.sub(
        r'^title: ""$',
        f"title: {json.dumps(title, ensure_ascii=False)}",
        rendered,
        count=1,
        flags=re.MULTILINE,
    )
    today = date.today().isoformat()
    for field in ("created", "updated", "date"):
        rendered = re.sub(
            rf"^({field}: )YYYY-MM-DD$",
            rf"\g<1>{today}",
            rendered,
            count=1,
            flags=re.MULTILINE,
        )
    rendered = re.sub(
        rf"^# {re.escape(record_id)}: .*$",
        f"# {record_id}: {title}",
        rendered,
        count=1,
        flags=re.MULTILINE,
    )
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record_type", choices=sorted(CONFIG))
    parser.add_argument("title")
    parser.add_argument("--slug", help="ASCII filename slug; generated from title by default")
    parser.add_argument("--root", type=Path, help="Repository root; auto-detected by default")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = (args.root or Path(__file__).resolve().parents[1]).resolve()
    directory_name, prefix, template_name = CONFIG[args.record_type]
    target_directory = root / directory_name
    template_path = root / "templates" / template_name
    if not template_path.is_file() or not target_directory.is_dir():
        parser.error(f"Repository structure is incomplete under {root}")

    record_id = next_id(target_directory, prefix)
    slug = args.slug or slugify(args.title)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        parser.error("--slug must contain lowercase ASCII letters, digits, and hyphens only")

    target = target_directory / f"{record_id}-{slug}.md"
    if target.exists():
        parser.error(f"Target already exists: {target}")

    content = render(template_path.read_text(encoding="utf-8"), record_id, args.title)
    if not args.dry_run:
        target.write_text(content, encoding="utf-8", newline="\n")

    relative = target.relative_to(root)
    action = "Would create" if args.dry_run else "Created"
    print(f"{action}: {relative}")
    print(f"Next: complete the record and add {record_id} to {directory_name}/README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
