#!/usr/bin/env python3
"""Checks the Humanizer package files with no third-party libraries."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NAME = "humanizer"
WORD_LIMIT = 7000


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


def require(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


SKILL_PATH = ROOT / "SKILL.md"
SKILL = read(SKILL_PATH)
README = read(ROOT / "README.md")
CHANGELOG = read(ROOT / "CHANGELOG.md")
PLUGIN = load_json(ROOT / ".claude-plugin" / "plugin.json")
CURSOR_PLUGIN = load_json(ROOT / ".cursor-plugin" / "plugin.json")
MARKETPLACE = load_json(ROOT / ".claude-plugin" / "marketplace.json")

yaml_metadata = require(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must start with YAML front matter",
).group(1)

for unsupported in ("version:", "compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported)}", yaml_metadata):
        raise SystemExit(f"Remove the unsupported YAML field: {unsupported[:-1]}")

if not re.search(rf"(?m)^name: {re.escape(NAME)}$", yaml_metadata):
    raise SystemExit(f"SKILL.md name must be {NAME}")

skill_version = require(
    re.search(r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', yaml_metadata),
    "Add metadata.version to SKILL.md as a three-part version",
).group(1)
changelog_version = require(
    re.search(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9]+)$", CHANGELOG),
    "Add a version heading to CHANGELOG.md",
).group(1)
versions = {skill_version, changelog_version, str(PLUGIN.get("version", "")), str(CURSOR_PLUGIN.get("version", ""))}
if len(versions) != 1:
    raise SystemExit(f"Use one version in every file: {sorted(versions)}")

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Keep exactly one regular SKILL.md, at the root")
if PLUGIN.get("name") != NAME or CURSOR_PLUGIN.get("name") != NAME:
    raise SystemExit(f"Set the plugin name to {NAME}")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("Point the Claude plugin skills loader at the root folder")
if "skills" in CURSOR_PLUGIN:
    raise SystemExit("Remove skills from the Cursor plugin so it loads the root SKILL.md")

skill_description = " ".join(
    require(
        re.search(r"(?m)^description: \|\n((?:  .*\n)+)", yaml_metadata + "\n"),
        "Write the SKILL.md description as an indented block",
    ).group(1).split()
)
if len(skill_description) > 1024:
    raise SystemExit(f"The SKILL.md description must be 1024 characters or fewer; now {len(skill_description)}")
descriptions = {
    str(PLUGIN.get("description", "")),
    str(CURSOR_PLUGIN.get("description", "")),
    *(str(p.get("description", "")) for p in MARKETPLACE.get("plugins", [])),
}
if len(descriptions) != 1 or not skill_description.startswith(next(iter(descriptions))):
    raise SystemExit(
        "Use the first sentence of the SKILL.md description in every plugin description: "
        f"{sorted(descriptions)}"
    )

# Pattern headings are "### n. English name (Mongolian name)"; README uses the Mongolian name
skill_headings = {int(n): name for n, name in re.findall(r"(?m)^### ([0-9]+)\. (.+)$", SKILL)}
skill_patterns = {}
for n, heading in skill_headings.items():
    mongolian = re.search(r" \(([^()]+)\)$", heading)
    if mongolian is None:
        raise SystemExit(f"SKILL.md pattern {n}: end the heading with the Mongolian name in parentheses: {heading!r}")
    skill_patterns[n] = mongolian.group(1)
numbers = list(skill_patterns)
count = len(numbers)
if count == 0 or numbers != list(range(1, count + 1)):
    raise SystemExit(f"Number the SKILL.md patterns from 1 with no gaps: {numbers}")

readme_patterns = {int(n): name for n, name in re.findall(r"(?m)^\| ([0-9]+) \| \*\*(.+?)\*\*", README)}
if sorted(readme_patterns) != numbers:
    raise SystemExit(f"List patterns 1 to {count} once each in the README tables: {sorted(readme_patterns)}")
renamed = [
    f"{n}: {readme_patterns[n]!r} → {name!r}"
    for n, name in skill_patterns.items()
    if readme_patterns[n] != name
]
if renamed:
    raise SystemExit("Match the README pattern names to the Mongolian names in SKILL.md: " + "; ".join(renamed))
if f"## {count} хэв маяг" not in README:
    raise SystemExit(f"Name the README pattern section '## {count} хэв маяг'")

references = sorted({int(n) for n in re.findall(r"§([0-9]+)", SKILL)})
missing = [n for n in references if not 1 <= n <= count]
if missing:
    raise SystemExit(f"Every § in SKILL.md must point to patterns 1–{count} (write spelling rules as 'rule 61'): {missing}")

linked = set(re.findall(r"((?:references|scripts)/[\w.-]+\.(?:md|py))", SKILL))
absent = sorted(p for p in linked if not (ROOT / p).is_file())
if absent:
    raise SystemExit(f"Files named in SKILL.md are missing: {absent}")
orphans = sorted(
    str(p.relative_to(ROOT)) for p in (ROOT / "references").glob("*.md")
    if str(p.relative_to(ROOT)) not in linked and str(p.relative_to(ROOT)) not in README
)
if orphans:
    raise SystemExit(f"Reference files no file points to: {orphans}")

# Copying from PDFs can turn «ё» into «ѐ» (U+0450)
for path in [SKILL_PATH, ROOT / "README.md", *(ROOT / "references").glob("*.md")]:
    if "ѐ" in read(path):
        raise SystemExit(f"{path.relative_to(ROOT)}: replace «ѐ» (U+0450) with «ё»")

# In Mongolian text use «хиймэл оюун», «их хэлний загвар», not «AI», «LLM».
# English sentences may say AI and LLM, so only flag them next to Cyrillic words.
term_files = [SKILL_PATH, ROOT / "README.md", ROOT / "AGENTS.md", *(ROOT / "references").glob("*.md")]
for path in term_files:
    for number, line in enumerate(read(path).splitlines(), 1):
        # Words inside «...» and (...) are treated as talking about the term
        line = re.sub(r"«[^»]*»|\([^)]*\)", " ", line)
        if re.search(r"\b(?:AI|LLM)[-‑]?[а-яөүёА-ЯӨҮЁ]|\b(?:AI|LLM)\s+[а-яөүё]|[а-яөүё]\s+(?:AI|LLM)\b", line):
            raise SystemExit(
                f"{path.relative_to(ROOT)}:{number}: in Mongolian text write «хиймэл оюун» for «AI» "
                "and «их хэлний загвар» for «LLM»"
            )

# The single-file version for chatbots without skill support must be up to date
import subprocess, sys  # noqa: E401
builder = ROOT / "scripts" / "build-single-file.py"
builder_text = read(builder)
missing_refs = sorted(
    str(p.relative_to(ROOT)) for p in (ROOT / "references").glob("*.md")
    if str(p.relative_to(ROOT)) not in builder_text
)
if missing_refs:
    raise SystemExit(f"Add to REFERENCES in build-single-file.py: {missing_refs}")
check = subprocess.run([sys.executable, str(builder), "--check"], capture_output=True, text=True)
if check.returncode != 0:
    raise SystemExit(check.stderr.strip() or check.stdout.strip())

words = len(SKILL.split())
if words > WORD_LIMIT:
    raise SystemExit(f"Keep SKILL.md at {WORD_LIMIT:,} words or fewer; now {words:,}")

if not re.search(r"(?m)^\s+instructions-language:\s*[\"']?en[\"']?\s*$", yaml_metadata):
    raise SystemExit("Set metadata.instructions-language to \"en\" in SKILL.md")
if "Reply in Mongolian" not in SKILL:
    raise SystemExit("Keep the reply-language rule (\"Reply in Mongolian ...\") in SKILL.md")

print(f"Humanizer v{skill_version} package OK: {count} patterns, {len(linked)} linked files, SKILL.md {words:,} words")
