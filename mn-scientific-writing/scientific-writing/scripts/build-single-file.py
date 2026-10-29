#!/usr/bin/env python3
"""Joins SKILL.md and every reference file into one file.

For chatbots without skill support (ChatGPT, Gemini, and others), which take one
attached file. Output: dist/scientific-writing-buten.md

Usage:
    python3 scripts/build-single-file.py           # write the file
    python3 scripts/build-single-file.py --check   # fail if the file is out of date
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "scientific-writing-buten.md"
REFERENCES = [
    "references/imrad_structure.md",
    "references/writing_principles.md",
    "references/citation_styles.md",
    "references/figures_tables.md",
    "references/reporting_guidelines.md",
    "references/mn/butets.md",
    "references/mn/bichleg-zarchim.md",
    "references/mn/eshlel.md",
    "references/mn/zurag-husnegt.md",
    "references/mn/tailagnah-udirdamj.md",
    "references/mn/setguul-shaardlaga.md",
    "references/mn/mongol-nairuulga.md",
]


def demote(text: str) -> str:
    """Push every heading down one level so the file keeps one top-level outline."""
    return re.sub(r"(?m)^(#{1,5}) ", r"#\1 ", text)


def build() -> str:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    meta = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    body = skill[meta.end():] if meta else skill
    version = re.search(r'version:\s*"([^"]+)"', meta.group(1)).group(1) if meta else "?"

    parts = [
        f"<!-- Made by scripts/build-single-file.py. Do not edit by hand. scientific-writing {version}. -->\n\n",
        "# Scientific Writing: complete version (one file)\n\n",
        "You are an assistant that writes, revises and reviews scientific manuscripts in English or Mongolian. "
        "Whenever the user asks for scientific writing, follow the Instructions part of this file. "
        "Every file the instructions cite as `references/...` is in the Reference part of this file under the same name. "
        "Reply in the language the user writes in.\n\n",
        "## Contents\n\n- Instructions (SKILL.md)\n",
        *(f"- Reference: {r}\n" for r in REFERENCES),
        "\n---\n\n# Instructions (SKILL.md)\n\n",
        demote(body).strip() + "\n",
    ]
    for ref in REFERENCES:
        text = demote((ROOT / ref).read_text(encoding="utf-8")).strip()
        parts.append(f"\n---\n\n# Reference: {ref}\n\n{text}\n")
    return "".join(parts)


def main() -> None:
    content = build()
    if "--check" in sys.argv:
        if not OUT.is_file() or OUT.read_text(encoding="utf-8") != content:
            raise SystemExit("dist/scientific-writing-buten.md is out of date: run python3 scripts/build-single-file.py")
        print("dist/scientific-writing-buten.md is up to date")
        return
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(content.split()):,} words")


if __name__ == "__main__":
    main()
