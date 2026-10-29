# Notes for developers and coding agents

How to change this package without breaking it.

## What this repository is

Humanizer is a skill written in Markdown: an assistant reads `SKILL.md` and follows it. It edits **Mongolian** text, but its instructions are in **English**. English instructions take fewer tokens, so the assistant loads them faster; the Mongolian examples, watch lists, and word tables stay in Mongolian because they are the data the assistant matches against. It is the English-instruction variant of Humanizer-MN (Mongolian instructions). The skill name is `humanizer`, the same as the English upstream skill, so users should not install both. Both cover the same 30 patterns and the same rules. Keep the skill portable: do not write instructions that depend on one or two assistants' tools.

There is no build step except the single-file version made by a script.

## Key files

- `SKILL.md`: the single source of truth. YAML front matter, why AI text sounds the way it does, work modes, the workflow, and 30 numbered patterns in seven sections, ordered by strength and frequency.
- `references/`: files the assistant reads only when needed. The five styles (`1-` … `5-`), essays, spelling rules, and common style errors.
- `dist/humanizer-buten.md`: `SKILL.md` and all references in one file, for chatbots without skill support. Made by `scripts/build-single-file.py`; do not edit by hand.
- `scripts/mn_tells.py`: points out suspect spots. Changes nothing.
- `scripts/validate-package.py`: checks files, shared values, terminology, and the single-file version.
- `README.md`: install and usage guide for users, in Mongolian.
- `CHANGELOG.md`: release notes, newest first.
- `.claude-plugin/`, `.cursor-plugin/`, `agents/openai.yaml`: plugin manifests.

## Rules for changes

- **Language split.** Instructions, explanations, and table headers in English. Everything the assistant must match or produce stays in Mongolian: Before/After examples, watch lists, fixed formulas, word tables, quotations, and legal citations. Pattern headings are `### n. English name (Mongolian name)`; section headings keep their Cyrillic letters (`## А. ...`).
- **Reply language.** The skill tells the assistant to reply in Mongolian, use «хиймэл оюун» and «их хэлний загвар» in Mongolian replies, and use the section labels «Найруулгын төрөл», «Ноорог», «Үлдсэн шинж», «Эцсийн хувилбар». Keep that rule.
- **Patterns.** Number them from 1 with no gaps, strongest and most frequent first. If a new tell fits an existing pattern, add it there instead of making a new one. After adding, removing, or renumbering, update the README table, the README headings, and every § reference.
- **The § sign.** In `SKILL.md` and the references, § means only a pattern number. Write spelling rules as "rule 61".
- **Mongolian terms.** In Mongolian text write «хиймэл оюун» (not AI), «их хэлний загвар» (not LLM), «ур чадвар» (skill), «өргөтгөл» (plugin), «заавар» (prompt). The validator flags «AI» and «LLM» inside Mongolian sentences; English sentences may use the English words.
- **Version.** The same version in `SKILL.md` `metadata.version`, the first heading of `CHANGELOG.md`, and both plugin.json files.
- **Description.** The plugin description is the first sentence of the `SKILL.md` description.
- **Single file.** After changing `SKILL.md` or a reference, run `python3 scripts/build-single-file.py`. If you add a reference file, add it to the script's `REFERENCES` list.
- **Length.** The assistant reads every word of `SKILL.md` each time it is used. The validator caps it at 7,000 words. Put long lists in `references/`.
- **Spelling.** All Mongolian text follows the spelling rules and the 2011 resolution (томьёо, харьяа, дараах, идэвх). Replace «ѐ» (U+0450), which comes in when copying from PDFs, with «ё»; the validator catches it.
- **Keep the two variants in step.** A rule or example changed here should also change in Humanizer-MN, and the reverse.
- **License.** Keep the upstream line «Copyright (c) 2025 Siqi Chen» in `LICENSE`.
- **Check before publishing.** `python3 scripts/validate-package.py`, `python3 scripts/mn_tells.py tests/ai-sample.md`, `npx skills add . --list`, `claude plugin validate .`.

## Writing style

Write instructions, docs, comments, and validator messages in plain language:

- Lead with the point.
- Use common words and the active voice.
- Keep sentences and paragraphs short.
- Name each thing with one term.
- Keep quoted wrong phrasings, citations, and code exactly as they are.
- Do not let this skill's patterns into your own writing: «-лт хийх», «олон хүмүүс», chains of «Энэ нь...».
