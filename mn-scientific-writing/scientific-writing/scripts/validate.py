#!/usr/bin/env python3
"""Checks the scientific-writing package files with no third-party libraries."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "scientific-writing"
WORD_LIMIT = 5000


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"Could not read {path.relative_to(ROOT)}: {error}")


def load_json(path: Path) -> dict:
    try:
        return json.loads(read(path))
    except json.JSONDecodeError as error:
        raise SystemExit(f"Fix the JSON in {path.relative_to(ROOT)}: {error}")


skill = read(ROOT / "SKILL.md")
meta = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
if not meta:
    raise SystemExit("SKILL.md must start with YAML front matter")
yaml = meta.group(1)
if not re.search(rf"(?m)^name: {NAME}$", yaml):
    raise SystemExit(f"SKILL.md name must be {NAME}")
for field in ("version:", "allowed-tools:", "compatibility:"):
    if re.search(rf"(?m)^{field}", yaml):
        raise SystemExit(f"Remove the unsupported YAML field: {field[:-1]}")
block = re.search(r"(?m)^description: \|\n((?:  .*\n)+)", yaml + "\n")
if not block:
    raise SystemExit("Write the SKILL.md description as an indented block")
description = " ".join(block.group(1).split())
if len(description) > 1024:
    raise SystemExit(f"The SKILL.md description must be 1024 characters or fewer; now {len(description)}")
version = re.search(r'(?m)^\s+version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"', yaml).group(1)

plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
cursor = load_json(ROOT / ".cursor-plugin" / "plugin.json")
market = load_json(ROOT / ".claude-plugin" / "marketplace.json")
changelog = re.search(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9]+)$", read(ROOT / "CHANGELOG.md")).group(1)
versions = {version, changelog, plugin.get("version"), cursor.get("version")}
if len(versions) != 1:
    raise SystemExit(f"Use one version in every file: {sorted(map(str, versions))}")
if {plugin.get("name"), cursor.get("name"), *(p.get("name") for p in market.get("plugins", []))} != {NAME}:
    raise SystemExit(f"Set every plugin name to {NAME}")
if plugin.get("skills") != ["./"]:
    raise SystemExit("Point the Claude plugin skills loader at the root folder")
first_sentence = description.split(". ")[0].rstrip(".") + "."
for d in [plugin.get("description"), cursor.get("description"), *(p.get("description") for p in market.get("plugins", []))]:
    if d != first_sentence:
        raise SystemExit(f"Plugin descriptions must equal the first sentence of the SKILL.md description: {d!r}")

# Every file SKILL.md names must exist, and every reference file must be named in SKILL.md
linked = set(re.findall(r"references/[\w/-]+\.md", skill))
missing = sorted(p for p in linked if not (ROOT / p).is_file())
if missing:
    raise SystemExit(f"Files named in SKILL.md are missing: {missing}")
refs = {str(p.relative_to(ROOT)) for p in (ROOT / "references").rglob("*.md")}
orphans = sorted(refs - linked)
if orphans:
    raise SystemExit(f"Reference files SKILL.md does not name: {orphans}")
for path in (ROOT / "references").rglob("*.md"):
    for target in re.findall(r"references/[\w/-]+\.md", read(path)):
        if not (ROOT / target).is_file():
            raise SystemExit(f"{path.relative_to(ROOT)} points to a missing file: {target}")

# Reporting guideline versions must stay current in the English guide
guide = read(ROOT / "references" / "reporting_guidelines.md")
for stale in ("**Latest version:** CONSORT 2010", "**Latest version:** SPIRIT 2013", "**Latest version:** TRIPOD 2015"):
    if stale in guide:
        raise SystemExit(f"references/reporting_guidelines.md is out of date: {stale}")

# Copying from PDFs can turn «ё» into «ѐ» (U+0450)
mongolian_files = [ROOT / "README.md", *(ROOT / "references" / "mn").glob("*.md")]
for path in [ROOT / "SKILL.md", *mongolian_files]:
    if "ѐ" in read(path):
        raise SystemExit(f"{path.relative_to(ROOT)}: replace «ѐ» (U+0450) with «ё»")

# In Mongolian text use «хиймэл оюун», «их хэлний загвар», not «AI», «LLM»
for path in mongolian_files:
    for number, line in enumerate(read(path).splitlines(), 1):
        line = re.sub(r"«[^»]*»|\([^)]*\)|`[^`]*`", " ", line)
        if re.search(r"\b(?:AI|LLM)[-‑]?[а-яөүёА-ЯӨҮЁ]|\b(?:AI|LLM)\s+[а-яөүё]|[а-яөүё]\s+(?:AI|LLM)\b", line):
            raise SystemExit(
                f"{path.relative_to(ROOT)}:{number}: in Mongolian text write «хиймэл оюун» for «AI» "
                "and «их хэлний загвар» for «LLM»"
            )

builder = ROOT / "scripts" / "build-single-file.py"
not_built = sorted(r for r in refs if r not in read(builder))
if not_built:
    raise SystemExit(f"Add to REFERENCES in build-single-file.py: {not_built}")
check = subprocess.run([sys.executable, str(builder), "--check"], capture_output=True, text=True)
if check.returncode != 0:
    raise SystemExit(check.stderr.strip() or check.stdout.strip())

words = len(skill.split())
if words > WORD_LIMIT:
    raise SystemExit(f"Keep SKILL.md at {WORD_LIMIT:,} words or fewer; now {words:,}")

print(f"scientific-writing v{version} package OK: {len(refs)} reference files, SKILL.md {words:,} words")
