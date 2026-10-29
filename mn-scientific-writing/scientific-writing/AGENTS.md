# Notes for developers and coding agents

How to change this package without breaking it.

## What this repository is

`scientific-writing` is a skill written in Markdown: an assistant reads `SKILL.md` and follows it. It writes, revises and reviews scientific manuscripts in English or Mongolian. The instructions in `SKILL.md` are in English and are based on the K-Dense scientific-writing skill (MIT). The Mongolian guides in `references/mn/` are written in Mongolian, because they teach Mongolian style, structure and citation rules with Mongolian examples.

## Key files

- `SKILL.md`: the single source of truth. Core rules, language handling, Mongolian quick rules, modes, workflow, section guidance, citations, figures, reporting guidelines, reference table.
- `references/*.md`: the English guides from the original skill (IMRaD, writing principles, citations, figures and tables, reporting guidelines).
- `references/mn/*.md`: the Mongolian guides (structure, principles, citations and MNS 5217:2012, figures and tables, reporting guidelines, Mongolian journals, Mongolian scientific style).
- `dist/scientific-writing-buten.md`: everything in one file for chatbots without skill support. Made by `scripts/build-single-file.py`; do not edit by hand.
- `scripts/validate.py`: checks the package.
- `README.md`: install and usage guide for users, in Mongolian.
- `CHANGELOG.md`: release notes, newest first, in Mongolian.
- `.claude-plugin/`, `.cursor-plugin/`, `agents/openai.yaml`: plugin manifests.

## Rules for changes

- **Integrity first.** Never weaken the rule against invented citations, data or statistics.
- **Language split.** `SKILL.md`, the English guides and this file in English; `references/mn/`, `README.md` and `CHANGELOG.md` in Mongolian.
- **Links.** Every reference file must be named in `SKILL.md`, and every `references/...` path inside a file must exist. The validator checks both.
- **Reporting guidelines.** When a guideline is updated, change the table in `SKILL.md`, `references/reporting_guidelines.md` and `references/mn/tailagnah-udirdamj.md` together. The validator fails on CONSORT 2010, SPIRIT 2013 or TRIPOD 2015 as "latest version".
- **Mongolian terms.** In Mongolian text write «хиймэл оюун» (not AI) and «их хэлний загвар» (not LLM). Follow the spelling rules and the 2011 State Language Council resolution (томьёо, харьяа, дараах).
- **Version.** The same version in `SKILL.md` `metadata.version`, the first heading of `CHANGELOG.md`, and both plugin.json files.
- **Description.** Plugin descriptions are the first sentence of the `SKILL.md` description.
- **Single file.** After changing `SKILL.md` or a reference, run `python3 scripts/build-single-file.py`. Add new reference files to its `REFERENCES` list.
- **Length.** The validator caps `SKILL.md` at 5,000 words. Put detail in `references/`.
- **License.** Keep the upstream line «Copyright (c) 2025 K-Dense Inc.» in `LICENSE`.
- **Check before publishing.** `python3 scripts/validate.py`, `npx skills add . --list`, `claude plugin validate .`.
