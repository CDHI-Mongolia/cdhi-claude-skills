#!/usr/bin/env python3
"""Joins SKILL.md and every reference file into one file.

For chatbots without skill support (ChatGPT, Gemini, and others), which take one
attached file. Output: dist/humanizer-buten.md

Usage:
    python3 scripts/build-single-file.py           # write the file
    python3 scripts/build-single-file.py --check   # fail if the file is out of date
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "humanizer-buten.md"
REFERENCES = [
    "references/1-uran-zohiol.md",
    "references/2-alban-bichig.md",
    "references/3-niitelgee.md",
    "references/4-shinjleh-uhaan.md",
    "references/5-hayag-temdeglegee.md",
    "references/esse.md",
    "references/nairuulgyn-aldaa.md",
    "references/zov-bichih-durem.md",
]


def build() -> str:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    meta = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    body = skill[meta.end():] if meta else skill
    version = re.search(r'version:\s*"([^"]+)"', meta.group(1)).group(1) if meta else "?"

    parts = [
        f"<!-- Made by scripts/build-single-file.py. Do not edit by hand. Humanizer {version}. -->\n\n",
        "# Humanizer: complete version (one file)\n\n",
        "You are an assistant that edits, rewrites, writes, and checks Mongolian text. "
        "Whenever the user asks for anything involving Mongolian text, follow the Instructions part of this file. "
        "Every file the instructions cite as `references/...` is in the Reference part of this file under the same name. "
        "If you cannot run `scripts/mn_tells.py`, skip that step. "
        "Reply in Mongolian unless the user asks otherwise.\n\n",
        "## Contents\n\n- Instructions (SKILL.md)\n",
        *(f"- Reference: {r}\n" for r in REFERENCES),
        "\n---\n\n# Instructions (SKILL.md)\n\n",
        re.sub(r"(?m)^(#{1,5}) ", r"#\1 ", body).strip() + "\n",
    ]
    for ref in REFERENCES:
        text = (ROOT / ref).read_text(encoding="utf-8")
        text = re.sub(r"(?m)^(#{1,5}) ", r"#\1 ", text).strip()
        parts.append(f"\n---\n\n# Reference: {ref}\n\n{text}\n")
    return "".join(parts)


def main() -> None:
    content = build()
    if "--check" in sys.argv:
        if not OUT.is_file() or OUT.read_text(encoding="utf-8") != content:
            raise SystemExit("dist/humanizer-buten.md is out of date: run python3 scripts/build-single-file.py")
        print("dist/humanizer-buten.md is up to date")
        return
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(content.split()):,} words")


if __name__ == "__main__":
    main()
