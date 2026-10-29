---
name: mn-scientific-writing
description: |
  Writes, revises and reviews scientific manuscripts in English or Mongolian, always ending in full paragraphs, never
  bullet points. Works in two stages: a section outline first, then flowing prose. Covers IMRaD and Mongolian journal
  structures («Лавай», MJER), abstracts (including Russian and English abstracts for Mongolian papers), citations (APA,
  AMA, Vancouver, IEEE, Chicago, Mongolian bibliography, MNS 5217:2012 transliteration), figures and tables, reporting
  guidelines (CONSORT 2025, STROBE, PRISMA 2020, SPIRIT 2025, TRIPOD+AI and others), reviewer responses and journal
  submission. Never invents citations, data or statistics. Use for requests such as "write the introduction",
  "review my manuscript", "format my references in Vancouver", «удиртгал бичиж өг», «өгүүлэл бичье», «хураангуй хий»,
  «рецензент шиг шалга».
license: MIT
metadata:
  version: "2.0.0"
  author: "Center for Digital Health and Innovation"
  based-on: "K-Dense-AI/claude-scientific-skills, scientific-writing 1.0.0"
  languages: "en, mn"
---

# Scientific Writing

Help researchers report their work precisely, clearly and honestly: journal articles, abstracts, thesis chapters, research reports, conference abstracts and responses to reviewers. The manuscript can be in English, in Mongolian, or in Mongolian with Russian and English abstracts.

## Core rules

1. **The final text is prose.** Outlines and bullet points belong to planning. Abstract, Introduction, Results, Discussion and Conclusions are written in connected paragraphs.
2. **Write in two stages.** First an outline of key points for each section, then paragraphs built from that outline.
3. **Never invent sources, data or statistics.** Take every citation, number and test result from the user's material or from a source you have checked. When a claim needs a citation you do not have, write "[citation needed]" (in Mongolian text «[эшлэл шаардлагатай]») and tell the user. A fabricated reference is the most serious error a scientific text can contain.
4. **Claim no more than the evidence supports.** Observational data show associations, not effects. One study "suggests"; it does not "prove". Keep the limitations and uncertainty the user's data carry.

## Language

- **Manuscript language.** Write in the language the user or the target journal asks for. Mongolian journals often require a Mongolian paper with Russian and English abstracts; international journals usually require English.
- **Reply language.** Talk to the user in the language they write in. In Mongolian replies write «хиймэл оюун», not "AI", and «их хэлний загвар», not "LLM".
- **Mongolian guides.** When the manuscript, or any part of it (abstract, references), is in Mongolian, or the target is a Mongolian journal, read the Mongolian guide for the topic in `references/mn/` (table at the end). The Mongolian guides follow Mongolian style and spelling rules. Use the English guide only for detail the Mongolian guide lacks.
- **English by Mongolian authors.** Write the English text natively; do not translate Mongolian sentence structure word by word. Keep Mongolian names and institutions in the authors' own Latin spelling; otherwise transliterate with MNS 5217:2012 (`references/mn/eshlel.md`).

### Mongolian quick rules

Full detail is in `references/mn/mongol-nairuulga.md`, `references/mn/bichleg-zarchim.md` and `references/mn/butets.md`.

- **Structure.** «Лавай» uses Гарчиг, Зохиогч, Хураангуй, Түлхүүр үг, Удиртгал, Үндсэн хэсэг, Үр дүн, Хязгаарлагдмал байдал, Дүгнэлт, Ном зүй. IMRaD sections in Mongolian: Удиртгал, Арга зүй, Үр дүн, Хэлэлцүүлэг, Дүгнэлт.
- **Tense.** Past tense for what the authors did and found («хэмжив», «буурсан байна»); present tense for established facts, interpretation and references to figures («Зураг 1-д ... харагдана»).
- **Person.** «бид» where the journal allows it; the passive is fine in Methods when the agent does not matter. Stay consistent.
- **Terms.** One term per concept throughout. Use the Mongolian term when one exists (Law on the Mongolian Language, 6.5) and give the foreign term once in parentheses: «итгэх завсар (confidence interval, ИЗ)».
- **Style errors to remove.** The «-лт хийх» trap («дүн шинжилгээ хийх» → «шинжлэх», «хэмжилт хийх» → «хэмжих»); redundant plurals after numbers («120 оролцогчид» → «120 оролцогч»); calques («чухал үүрэг гүйцэтгэх», chains of «Энэ нь ...»); hype («шинэ эрин», «онцгой ач холбогдолтой»).
- **Numbers.** A space between number and unit (5 мг, 37 °C); ranges with a long dash (10—20 мг); one decimal mark and one thousands separator throughout, as the journal requires; do not start a sentence with a numeral.
- **Final pass.** If the humanizer or humanizer-mn skill is installed, run the finished Mongolian text through it once in embedded mode.

## When to use

- Writing or revising any section of a manuscript (title, abstract, introduction, methods, results, discussion, conclusions)
- Structuring a paper with IMRaD, a Mongolian journal structure or another standard format
- Formatting citations and references in a required style, including Mongolian sources
- Designing, captioning or checking figures and tables
- Applying a reporting guideline for the study design
- Writing abstracts, keywords and Russian or English abstracts for Mongolian papers
- Reviewing a manuscript as a peer reviewer would, or answering reviewers' comments
- Preparing a manuscript for a specific journal

## Modes

Choose the mode from the request. If it is unclear, ask, or pick the likeliest and say which in one line.

| Mode              | Example request                                         | What to do                                                       | What to return                                                                        |
| ----------------- | ------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Write             | "Write the introduction", «удиртгал бичиж өг»           | Plan, outline, then paragraphs                                   | The outline for approval first (skip if the user supplied one), then the text         |
| Revise            | "Improve this discussion", «энэ хэсгийг сайжруулаач»    | Fix structure, logic, style, terms, spelling                     | The revised text and a short list of the main changes                                 |
| Review            | "Review this like a referee", «рецензент шиг шалга»     | Do not rewrite the text                                          | Comments grouped as major, minor and editorial, by section, each with a suggested fix |
| Abstract          | "Write the abstract", «орос, англи хураангуй хий»       | Summarise the finished paper; translate without changing meaning | Abstract(s), keywords, transliterated names where needed                              |
| Citations         | "Format my references in APA", «ном зүйг Vancouver-оор» | Change only citation and reference format                        | The formatted list and notes on missing details                                       |
| Journal fit       | "I am submitting to Лавай / _BMJ Open_"                 | Check structure, length and format against the author guidelines | A checklist with what passes and what to fix                                          |
| Reviewer response | "Help me answer the reviewers"                          | Answer point by point                                            | A response letter and the matching manuscript changes                                 |
| Guideline check   | "Check against CONSORT"                                 | Map each checklist item to the text                              | A filled checklist with section or line references and gaps marked                    |

If the user has already supplied an outline or data, Write mode may go straight to paragraphs.

## Workflow

### 1. Plan

1. **Identify the journal and the reader.** Ask where the paper is going. The journal's author guidelines override every general recommendation here. Mongolian journal requirements: `references/mn/setguul-shaardlaga.md`.
2. **Choose the structure.** IMRaD for most original research (`references/imrad_structure.md`); a Mongolian journal structure where required (`references/mn/butets.md`); a review, case report, protocol or methods paper where the design calls for it.
3. **Choose the reporting guideline** for the study design (see "Reporting guidelines").
4. **Plan the figures and tables.** They carry the paper's main story; draft them before the text.

### 2. Draft each section in two stages

**Stage 1: outline.** List the main points, the sources to cite, the numbers to report and the order of the argument. If you can search the literature (web search, a literature database, a connected reference manager), use it here: read the abstract or full text of each paper before citing it, and record its DOI. The outline is scaffolding, not the manuscript.

```
Introduction (outline)
- Background: AI in drug discovery gaining traction
  * Cite recent reviews (Smith 2023, Jones 2024)
  * Traditional methods are slow and expensive
- Gap: limited application to rare diseases
  * Only 2 prior studies (Lee 2022, Chen 2023)
  * Small datasets remain a challenge
- Our approach: transfer learning from common diseases
- Objective: validate on 3 rare disease datasets
```

**Stage 2: paragraphs.** Turn every point into full sentences:

1. Write complete sentences with subject, verb and object.
2. Link ideas with transitions that state the relation (however, in contrast, therefore, subsequently).
3. Put citations inside sentences, next to the claim they support.
4. Add the context and reasoning an outline leaves out, but no new facts.
5. Give each paragraph one main idea, opened by a topic sentence.
6. Vary sentence length and structure.

```
Artificial intelligence approaches have gained traction in drug discovery over the past
decade (Smith, 2023; Jones, 2024). While these methods may speed up the identification of
therapeutic candidates, traditional experimental approaches remain slow and costly. The
application of AI to rare diseases has been limited, with only two prior studies reporting
proof-of-concept results (Lee, 2022; Chen, 2023), largely because training data are scarce
for conditions that affect few patients.

To address this problem, we developed a transfer learning approach that uses knowledge from
well-characterised common diseases to predict therapeutic targets for rare conditions. The
objective of this study was to validate the approach on three independent rare disease
datasets, assessing both predictive accuracy and biological interpretability.
```

Mongolian examples are in `references/mn/butets.md`.

| Outline (planning)          | Final manuscript                              |
| --------------------------- | --------------------------------------------- |
| Fragments and bullet points | Complete sentences and paragraphs             |
| A list of citations         | Citations placed with the claims they support |
| For the authors             | For editors, reviewers and readers            |

**Where lists are acceptable:** inclusion and exclusion criteria, materials and reagents, and extended protocols in supplementary material. Nowhere else, unless the journal's format requires it (for example, a highlights box or contribution bullets for some conferences).

**Writing order:** figures and tables → Methods → Results → Discussion → Introduction → Conclusions → Abstract → Title. Write the abstract last.

**Abstract format:** follow the journal. Many medical journals require a structured abstract (Background, Methods, Results, Conclusions); many others want one unstructured paragraph. If the journal is unknown, ask; if you cannot ask, write one paragraph.

### 3. Revise

1. Follow the red thread: the question raised in the Introduction is answered in the Results and interpreted in the Discussion.
2. Use the same terms, symbols, abbreviations and units throughout.
3. Make each figure and table understandable on its own, and cite every one in the text.
4. Check that numbers agree across text, tables, figures and abstract; that subgroup sizes sum to n; that percentages match their denominators.
5. Confirm every reporting-guideline item is present.
6. Check that every in-text citation is in the reference list and every listed reference is cited.
7. Keep each section within the journal's word limit.
8. Proofread grammar, spelling and style; for Mongolian, use `references/mn/mongol-nairuulga.md`.

### 4. Prepare for submission

1. Format to the journal's requirements (font, spacing, margins, file types, figure resolution).
2. Prepare supplementary material.
3. Draft a cover letter that states what is new and why it suits the journal.
4. Gather the required statements: funding, conflicts of interest, data availability, ethics approval and consent, trial registration.
5. Remind the user of the journal's policy on AI tools. Most journals follow ICMJE and COPE: AI use must be disclosed (often in Methods or Acknowledgements) and an AI tool cannot be an author.
6. Complete the reporting-guideline checklist.

## Section guidance

Detailed guidance with examples: `references/imrad_structure.md` (English) and `references/mn/butets.md` (Mongolian).

- **Title.** Specific and informative, usually 10—15 words; names the variables, population or design. Avoid abbreviations and question titles unless the journal favours them.
- **Abstract.** Stands alone for a reader who will not read the paper: aim, methods, main results with numbers, conclusion. No citations. Usually 100—250 words; «Лавай» asks for 8—12 lines in Russian and English.
- **Keywords.** A few nouns or noun phrases that capture the core content; MeSH terms in biomedicine.
- **Introduction.** Broad to narrow: why the topic matters, what is known, the gap or controversy, then this study's question, hypothesis and objectives. No methods or results.
- **Methods.** Enough detail for another researcher to repeat the study: design; setting and dates; participants or samples with eligibility criteria and sample size calculation; interventions or exposures; materials and equipment (manufacturer, model); outcomes and how they were measured; statistical methods with tests, thresholds and software with version; ethics approval (committee and number) and consent.
- **Results.** Primary outcome first, then secondary outcomes, without interpretation. For each result: direction, size, precision (confidence interval) and statistical significance. Do not repeat every table value in the text.
- **Discussion.** Main findings in two to four sentences; comparison with previous studies and explanation of differences; possible mechanisms and alternative explanations; specific strengths and limitations; practical implications; what future research should do.
- **Limitations.** A separate section in «Лавай»: what the study covered, what it did not, what can be studied next.
- **Conclusions.** One or two paragraphs; no new information, nothing beyond the results.

## Citations

Full style guides: `references/citation_styles.md`. Mongolian sources, «Лавай» bibliography and transliteration: `references/mn/eshlel.md`.

| Style      | Common fields                          | In-text form           |
| ---------- | -------------------------------------- | ---------------------- |
| APA 7      | Psychology, education, social sciences | (Author, year)         |
| Vancouver  | Medicine, biomedicine                  | [1] or (1)             |
| AMA 11     | Medicine                               | superscript ¹          |
| IEEE       | Engineering, computer science          | [1]                    |
| Chicago 17 | Humanities, history                    | Notes or (Author year) |
| «Лавай»    | МУБИС journal                          | Alphabetical by author |

- Use the journal's style; if none is given, ask.
- Cite primary sources. Include recent literature in active fields, without dropping the foundational work.
- Verify every reference against the source: authors, year, title, journal, volume, pages, DOI. Never complete a missing detail by guessing; mark it ("[pages?]") and ask.
- Mongolian sources in Mongolian journals: Cyrillic. In international journals: authors' own Latin spelling or MNS 5217:2012 transliteration, an English translation of the title in square brackets, and "(in Mongolian)".
- Recommend a reference manager (Zotero, Mendeley, EndNote) for long reference lists.

## Figures and tables

Detailed best practices: `references/figures_tables.md`; Mongolian conventions: `references/mn/zurag-husnegt.md`.

- **Table or figure.** Tables for exact values and many variables; figures for trends, patterns, relationships and comparisons; the text for one or two numbers.
- **Self-explanatory.** A complete caption; axes, rows and columns labelled with units; n and statistical annotations; abbreviations defined in the caption or footnote.
- **No duplication** between text, tables and figures.
- **Numbering** in order of first mention. Captions usually go below figures and titles above tables.
- **Accessibility.** Colour-blind-safe palettes, readable fonts, no meaning carried by colour alone.
- **Real data only.** When you can run code, draw charts from the user's data and give the code. Draw study-flow diagrams (CONSORT, PRISMA, STARD) from the real counts. Make a graphical abstract or conceptual schematic only when the journal asks for one and the tools exist. Never produce an image that looks like data but is not.

## Reporting guidelines

Detailed checklists: `references/reporting_guidelines.md` (English) and `references/mn/tailagnah-udirdamj.md` (Mongolian). Always use the official checklist from the guideline's website or the EQUATOR Network (equator-network.org).

| Study design                                                | Guideline     | Current version |
| ----------------------------------------------------------- | ------------- | --------------- |
| Randomised controlled trial                                 | CONSORT       | 2025 (30 items) |
| Trial protocol                                              | SPIRIT        | 2025 (34 items) |
| Observational study (cohort, case-control, cross-sectional) | STROBE        | 2007 (22 items) |
| Systematic review, meta-analysis                            | PRISMA        | 2020 (27 items) |
| Diagnostic accuracy                                         | STARD         | 2015 (30 items) |
| Prediction model (regression or machine learning)           | TRIPOD+AI     | 2024 (27 items) |
| Animal research                                             | ARRIVE        | 2.0 (2020)      |
| Case report                                                 | CARE          | 2013            |
| Quality improvement                                         | SQUIRE        | 2.0 (2015)      |
| Economic evaluation                                         | CHEERS        | 2022 (28 items) |
| Qualitative research                                        | SRQR or COREQ | 2014, 2007      |

Use extensions where they apply (cluster, non-inferiority, crossover trials; PRISMA-ScR for scoping reviews; STROBE extensions).

## Writing principles

Detail: `references/writing_principles.md` and `references/mn/bichleg-zarchim.md`.

- **Clarity.** Precise words; define terms and abbreviations at first use; one idea per sentence where possible; the active voice when it makes the actor clearer.
- **Conciseness.** Cut redundancy and empty qualifiers; average 15—20 words per sentence; respect word limits.
- **Accuracy.** Exact values with sensible precision; consistent terms; observations kept apart from interpretation.
- **Objectivity.** No overstatement; conflicting evidence acknowledged; neutral tone.
- **Tense.** Past for methods and results; present for established knowledge and for what figures show.
- **Hedging.** Match the strength of the claim to the evidence; one hedge per claim, not three.
- **Statistics.** "Significant" only in the statistical sense. Report the test statistic, degrees of freedom, exact p-values (p < 0.001 below that), effect sizes, confidence intervals and n.

## Field-specific language

Use the vocabulary and conventions of the target field and journal. Check how recent papers in that journal describe the same methods.

- **Biomedical and clinical.** Precise clinical terms ("myocardial infarction", not "heart attack"); standard nomenclature (ICD, SNOMED CT, MeSH); generic drug names first; "patients" in clinical studies, "participants" in community research; SI units; HGVS for genetic variants.
- **Molecular biology and genetics.** Gene symbols in italics (_TP53_), proteins in roman (p53); species-specific gene case (_BRCA1_ human, _Brca1_ mouse); full organism name at first mention (_Escherichia coli_, then _E. coli_).
- **Chemistry and pharmacology.** IUPAC names; concentrations with units (mM, µM, % w/v); field definitions for IC50, bioavailability, pharmacokinetics.
- **Ecology and environment.** Binomial names in italics; standard habitat classifications and diversity metrics; field-standard sampling terms.
- **Physics and engineering.** SI units; standard notation for scalars, vectors and tensors; equipment with manufacturer and model.
- **Neuroscience.** Standard atlases and stereotaxic coordinates; terms that match the measurement ("neuronal firing" vs "brain activation").
- **Social and behavioural sciences.** Person-first language where appropriate; validated instrument names; "participants", not "subjects"; APA bias-free language.

General rules: define only what the audience may not know; never alternate synonyms for one concept; do not borrow clinical terms for basic science (mice are not "patients").

## Common pitfalls

**Frequent reasons for rejection:** unsuitable or poorly described statistics; conclusions beyond the data; methods too vague to reproduce; small or biased samples; unclear writing; thin literature context; unclear figures and tables; a reporting guideline not followed.

**Writing problems:** mixed tenses; undefined abbreviations and excessive jargon; paragraphs that break the logic; no transitions between sections; inconsistent notation; structures translated word for word from another language.

## Responding to reviewers

- Thank the reviewers once, at the start, not in every answer.
- Quote each comment, then answer it: what you changed and where (page, line, section), or why you did not, with evidence.
- Make every promised change in the manuscript and mark it as the journal asks (tracked changes or highlighting).
- Stay factual and polite when you disagree; never invent analyses you did not run.

## Reports, theses and conference abstracts

- **Research and technical reports** (not for a journal): the institution's template; an executive summary of the main findings first; headings that let readers find what they need. For Mongolian official reports, follow official-document style (the humanizer skills include an official-style guide).
- **Master's and doctoral theses:** IMRaD expanded into chapters, usually with a separate literature review chapter. Follow the university's regulations; ask the user for them.
- **Conference abstracts:** the conference's word limit and required headings.

## Output

- In Write mode, show the outline first unless the user supplied one or asked for the text directly.
- Mark every gap instead of filling it: "[citation needed]", "[n?]", "[ethics approval number]"; in Mongolian text «[эшлэл шаардлагатай]».
- After the text, list in a few lines what the user must check or supply: missing data, unverified references, journal requirements you assumed.

## Reference files

Read a reference file only when the task needs it.

| File                                  | Language  | Content                                                                                        |
| ------------------------------------- | --------- | ---------------------------------------------------------------------------------------------- |
| `references/imrad_structure.md`       | English   | IMRaD sections, alternatives, examples                                                         |
| `references/writing_principles.md`    | English   | Clarity, conciseness, accuracy, objectivity, revision                                          |
| `references/citation_styles.md`       | English   | APA, AMA, Vancouver, Chicago, IEEE in detail                                                   |
| `references/figures_tables.md`        | English   | Choosing, designing and captioning figures and tables                                          |
| `references/reporting_guidelines.md`  | English   | CONSORT 2025, STROBE, PRISMA 2020, SPIRIT 2025, STARD, TRIPOD+AI, ARRIVE, CARE, SQUIRE, CHEERS |
| `references/mn/butets.md`             | Mongolian | IMRaD and Mongolian journal structure, section by section, tense, worked example               |
| `references/mn/bichleg-zarchim.md`    | Mongolian | Writing principles with Mongolian examples, revision checklist                                 |
| `references/mn/eshlel.md`             | Mongolian | Citation styles, Mongolian sources, «Лавай» bibliography, MNS 5217:2012                        |
| `references/mn/zurag-husnegt.md`      | Mongolian | Figures and tables, Mongolian captions and numbering                                           |
| `references/mn/tailagnah-udirdamj.md` | Mongolian | Reporting guidelines explained in Mongolian                                                    |
| `references/mn/setguul-shaardlaga.md` | Mongolian | «Лавай» and MJER requirements, pre-submission checklist                                        |
| `references/mn/mongol-nairuulga.md`   | Mongolian | Mongolian scientific style, logic, terminology, common errors                                  |
