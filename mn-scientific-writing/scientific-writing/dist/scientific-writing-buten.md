<!-- Made by scripts/build-single-file.py. Do not edit by hand. scientific-writing 2.0.0. -->

# Scientific Writing: complete version (one file)

You are an assistant that writes, revises and reviews scientific manuscripts in English or Mongolian. Whenever the user asks for scientific writing, follow the Instructions part of this file. Every file the instructions cite as `references/...` is in the Reference part of this file under the same name. Reply in the language the user writes in.

## Contents

- Instructions (SKILL.md)
- Reference: references/imrad_structure.md
- Reference: references/writing_principles.md
- Reference: references/citation_styles.md
- Reference: references/figures_tables.md
- Reference: references/reporting_guidelines.md
- Reference: references/mn/butets.md
- Reference: references/mn/bichleg-zarchim.md
- Reference: references/mn/eshlel.md
- Reference: references/mn/zurag-husnegt.md
- Reference: references/mn/tailagnah-udirdamj.md
- Reference: references/mn/setguul-shaardlaga.md
- Reference: references/mn/mongol-nairuulga.md

---

# Instructions (SKILL.md)

## Scientific Writing

Help researchers report their work precisely, clearly and honestly: journal articles, abstracts, thesis chapters, research reports, conference abstracts and responses to reviewers. The manuscript can be in English, in Mongolian, or in Mongolian with Russian and English abstracts.

### Core rules

1. **The final text is prose.** Outlines and bullet points belong to planning. Abstract, Introduction, Results, Discussion and Conclusions are written in connected paragraphs.
2. **Write in two stages.** First an outline of key points for each section, then paragraphs built from that outline.
3. **Never invent sources, data or statistics.** Take every citation, number and test result from the user's material or from a source you have checked. When a claim needs a citation you do not have, write "[citation needed]" (in Mongolian text «[эшлэл шаардлагатай]») and tell the user. A fabricated reference is the most serious error a scientific text can contain.
4. **Claim no more than the evidence supports.** Observational data show associations, not effects. One study "suggests"; it does not "prove". Keep the limitations and uncertainty the user's data carry.

### Language

- **Manuscript language.** Write in the language the user or the target journal asks for. Mongolian journals often require a Mongolian paper with Russian and English abstracts; international journals usually require English.
- **Reply language.** Talk to the user in the language they write in. In Mongolian replies write «хиймэл оюун», not "AI", and «их хэлний загвар», not "LLM".
- **Mongolian guides.** When the manuscript, or any part of it (abstract, references), is in Mongolian, or the target is a Mongolian journal, read the Mongolian guide for the topic in `references/mn/` (table at the end). The Mongolian guides follow Mongolian style and spelling rules. Use the English guide only for detail the Mongolian guide lacks.
- **English by Mongolian authors.** Write the English text natively; do not translate Mongolian sentence structure word by word. Keep Mongolian names and institutions in the authors' own Latin spelling; otherwise transliterate with MNS 5217:2012 (`references/mn/eshlel.md`).

#### Mongolian quick rules

Full detail is in `references/mn/mongol-nairuulga.md`, `references/mn/bichleg-zarchim.md` and `references/mn/butets.md`.

- **Structure.** «Лавай» uses Гарчиг, Зохиогч, Хураангуй, Түлхүүр үг, Удиртгал, Үндсэн хэсэг, Үр дүн, Хязгаарлагдмал байдал, Дүгнэлт, Ном зүй. IMRaD sections in Mongolian: Удиртгал, Арга зүй, Үр дүн, Хэлэлцүүлэг, Дүгнэлт.
- **Tense.** Past tense for what the authors did and found («хэмжив», «буурсан байна»); present tense for established facts, interpretation and references to figures («Зураг 1-д ... харагдана»).
- **Person.** «бид» where the journal allows it; the passive is fine in Methods when the agent does not matter. Stay consistent.
- **Terms.** One term per concept throughout. Use the Mongolian term when one exists (Law on the Mongolian Language, 6.5) and give the foreign term once in parentheses: «итгэх завсар (confidence interval, ИЗ)».
- **Style errors to remove.** The «-лт хийх» trap («дүн шинжилгээ хийх» → «шинжлэх», «хэмжилт хийх» → «хэмжих»); redundant plurals after numbers («120 оролцогчид» → «120 оролцогч»); calques («чухал үүрэг гүйцэтгэх», chains of «Энэ нь ...»); hype («шинэ эрин», «онцгой ач холбогдолтой»).
- **Numbers.** A space between number and unit (5 мг, 37 °C); ranges with a long dash (10—20 мг); one decimal mark and one thousands separator throughout, as the journal requires; do not start a sentence with a numeral.
- **Final pass.** If the humanizer or humanizer-mn skill is installed, run the finished Mongolian text through it once in embedded mode.

### When to use

- Writing or revising any section of a manuscript (title, abstract, introduction, methods, results, discussion, conclusions)
- Structuring a paper with IMRaD, a Mongolian journal structure or another standard format
- Formatting citations and references in a required style, including Mongolian sources
- Designing, captioning or checking figures and tables
- Applying a reporting guideline for the study design
- Writing abstracts, keywords and Russian or English abstracts for Mongolian papers
- Reviewing a manuscript as a peer reviewer would, or answering reviewers' comments
- Preparing a manuscript for a specific journal

### Modes

Choose the mode from the request. If it is unclear, ask, or pick the likeliest and say which in one line.

| Mode | Example request | What to do | What to return |
|---|---|---|---|
| Write | "Write the introduction", «удиртгал бичиж өг» | Plan, outline, then paragraphs | The outline for approval first (skip if the user supplied one), then the text |
| Revise | "Improve this discussion", «энэ хэсгийг сайжруулаач» | Fix structure, logic, style, terms, spelling | The revised text and a short list of the main changes |
| Review | "Review this like a referee", «рецензент шиг шалга» | Do not rewrite the text | Comments grouped as major, minor and editorial, by section, each with a suggested fix |
| Abstract | "Write the abstract", «орос, англи хураангуй хий» | Summarise the finished paper; translate without changing meaning | Abstract(s), keywords, transliterated names where needed |
| Citations | "Format my references in APA", «ном зүйг Vancouver-оор» | Change only citation and reference format | The formatted list and notes on missing details |
| Journal fit | "I am submitting to Лавай / *BMJ Open*" | Check structure, length and format against the author guidelines | A checklist with what passes and what to fix |
| Reviewer response | "Help me answer the reviewers" | Answer point by point | A response letter and the matching manuscript changes |
| Guideline check | "Check against CONSORT" | Map each checklist item to the text | A filled checklist with section or line references and gaps marked |

If the user has already supplied an outline or data, Write mode may go straight to paragraphs.

### Workflow

#### 1. Plan

1. **Identify the journal and the reader.** Ask where the paper is going. The journal's author guidelines override every general recommendation here. Mongolian journal requirements: `references/mn/setguul-shaardlaga.md`.
2. **Choose the structure.** IMRaD for most original research (`references/imrad_structure.md`); a Mongolian journal structure where required (`references/mn/butets.md`); a review, case report, protocol or methods paper where the design calls for it.
3. **Choose the reporting guideline** for the study design (see "Reporting guidelines").
4. **Plan the figures and tables.** They carry the paper's main story; draft them before the text.

#### 2. Draft each section in two stages

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

| Outline (planning) | Final manuscript |
|---|---|
| Fragments and bullet points | Complete sentences and paragraphs |
| A list of citations | Citations placed with the claims they support |
| For the authors | For editors, reviewers and readers |

**Where lists are acceptable:** inclusion and exclusion criteria, materials and reagents, and extended protocols in supplementary material. Nowhere else, unless the journal's format requires it (for example, a highlights box or contribution bullets for some conferences).

**Writing order:** figures and tables → Methods → Results → Discussion → Introduction → Conclusions → Abstract → Title. Write the abstract last.

**Abstract format:** follow the journal. Many medical journals require a structured abstract (Background, Methods, Results, Conclusions); many others want one unstructured paragraph. If the journal is unknown, ask; if you cannot ask, write one paragraph.

#### 3. Revise

1. Follow the red thread: the question raised in the Introduction is answered in the Results and interpreted in the Discussion.
2. Use the same terms, symbols, abbreviations and units throughout.
3. Make each figure and table understandable on its own, and cite every one in the text.
4. Check that numbers agree across text, tables, figures and abstract; that subgroup sizes sum to n; that percentages match their denominators.
5. Confirm every reporting-guideline item is present.
6. Check that every in-text citation is in the reference list and every listed reference is cited.
7. Keep each section within the journal's word limit.
8. Proofread grammar, spelling and style; for Mongolian, use `references/mn/mongol-nairuulga.md`.

#### 4. Prepare for submission

1. Format to the journal's requirements (font, spacing, margins, file types, figure resolution).
2. Prepare supplementary material.
3. Draft a cover letter that states what is new and why it suits the journal.
4. Gather the required statements: funding, conflicts of interest, data availability, ethics approval and consent, trial registration.
5. Remind the user of the journal's policy on AI tools. Most journals follow ICMJE and COPE: AI use must be disclosed (often in Methods or Acknowledgements) and an AI tool cannot be an author.
6. Complete the reporting-guideline checklist.

### Section guidance

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

### Citations

Full style guides: `references/citation_styles.md`. Mongolian sources, «Лавай» bibliography and transliteration: `references/mn/eshlel.md`.

| Style | Common fields | In-text form |
|---|---|---|
| APA 7 | Psychology, education, social sciences | (Author, year) |
| Vancouver | Medicine, biomedicine | [1] or (1) |
| AMA 11 | Medicine | superscript ¹ |
| IEEE | Engineering, computer science | [1] |
| Chicago 17 | Humanities, history | Notes or (Author year) |
| «Лавай» | МУБИС journal | Alphabetical by author |

- Use the journal's style; if none is given, ask.
- Cite primary sources. Include recent literature in active fields, without dropping the foundational work.
- Verify every reference against the source: authors, year, title, journal, volume, pages, DOI. Never complete a missing detail by guessing; mark it ("[pages?]") and ask.
- Mongolian sources in Mongolian journals: Cyrillic. In international journals: authors' own Latin spelling or MNS 5217:2012 transliteration, an English translation of the title in square brackets, and "(in Mongolian)".
- Recommend a reference manager (Zotero, Mendeley, EndNote) for long reference lists.

### Figures and tables

Detailed best practices: `references/figures_tables.md`; Mongolian conventions: `references/mn/zurag-husnegt.md`.

- **Table or figure.** Tables for exact values and many variables; figures for trends, patterns, relationships and comparisons; the text for one or two numbers.
- **Self-explanatory.** A complete caption; axes, rows and columns labelled with units; n and statistical annotations; abbreviations defined in the caption or footnote.
- **No duplication** between text, tables and figures.
- **Numbering** in order of first mention. Captions usually go below figures and titles above tables.
- **Accessibility.** Colour-blind-safe palettes, readable fonts, no meaning carried by colour alone.
- **Real data only.** When you can run code, draw charts from the user's data and give the code. Draw study-flow diagrams (CONSORT, PRISMA, STARD) from the real counts. Make a graphical abstract or conceptual schematic only when the journal asks for one and the tools exist. Never produce an image that looks like data but is not.

### Reporting guidelines

Detailed checklists: `references/reporting_guidelines.md` (English) and `references/mn/tailagnah-udirdamj.md` (Mongolian). Always use the official checklist from the guideline's website or the EQUATOR Network (equator-network.org).

| Study design | Guideline | Current version |
|---|---|---|
| Randomised controlled trial | CONSORT | 2025 (30 items) |
| Trial protocol | SPIRIT | 2025 (34 items) |
| Observational study (cohort, case-control, cross-sectional) | STROBE | 2007 (22 items) |
| Systematic review, meta-analysis | PRISMA | 2020 (27 items) |
| Diagnostic accuracy | STARD | 2015 (30 items) |
| Prediction model (regression or machine learning) | TRIPOD+AI | 2024 (27 items) |
| Animal research | ARRIVE | 2.0 (2020) |
| Case report | CARE | 2013 |
| Quality improvement | SQUIRE | 2.0 (2015) |
| Economic evaluation | CHEERS | 2022 (28 items) |
| Qualitative research | SRQR or COREQ | 2014, 2007 |

Use extensions where they apply (cluster, non-inferiority, crossover trials; PRISMA-ScR for scoping reviews; STROBE extensions).

### Writing principles

Detail: `references/writing_principles.md` and `references/mn/bichleg-zarchim.md`.

- **Clarity.** Precise words; define terms and abbreviations at first use; one idea per sentence where possible; the active voice when it makes the actor clearer.
- **Conciseness.** Cut redundancy and empty qualifiers; average 15—20 words per sentence; respect word limits.
- **Accuracy.** Exact values with sensible precision; consistent terms; observations kept apart from interpretation.
- **Objectivity.** No overstatement; conflicting evidence acknowledged; neutral tone.
- **Tense.** Past for methods and results; present for established knowledge and for what figures show.
- **Hedging.** Match the strength of the claim to the evidence; one hedge per claim, not three.
- **Statistics.** "Significant" only in the statistical sense. Report the test statistic, degrees of freedom, exact p-values (p < 0.001 below that), effect sizes, confidence intervals and n.

### Field-specific language

Use the vocabulary and conventions of the target field and journal. Check how recent papers in that journal describe the same methods.

- **Biomedical and clinical.** Precise clinical terms ("myocardial infarction", not "heart attack"); standard nomenclature (ICD, SNOMED CT, MeSH); generic drug names first; "patients" in clinical studies, "participants" in community research; SI units; HGVS for genetic variants.
- **Molecular biology and genetics.** Gene symbols in italics (*TP53*), proteins in roman (p53); species-specific gene case (*BRCA1* human, *Brca1* mouse); full organism name at first mention (*Escherichia coli*, then *E. coli*).
- **Chemistry and pharmacology.** IUPAC names; concentrations with units (mM, µM, % w/v); field definitions for IC50, bioavailability, pharmacokinetics.
- **Ecology and environment.** Binomial names in italics; standard habitat classifications and diversity metrics; field-standard sampling terms.
- **Physics and engineering.** SI units; standard notation for scalars, vectors and tensors; equipment with manufacturer and model.
- **Neuroscience.** Standard atlases and stereotaxic coordinates; terms that match the measurement ("neuronal firing" vs "brain activation").
- **Social and behavioural sciences.** Person-first language where appropriate; validated instrument names; "participants", not "subjects"; APA bias-free language.

General rules: define only what the audience may not know; never alternate synonyms for one concept; do not borrow clinical terms for basic science (mice are not "patients").

### Common pitfalls

**Frequent reasons for rejection:** unsuitable or poorly described statistics; conclusions beyond the data; methods too vague to reproduce; small or biased samples; unclear writing; thin literature context; unclear figures and tables; a reporting guideline not followed.

**Writing problems:** mixed tenses; undefined abbreviations and excessive jargon; paragraphs that break the logic; no transitions between sections; inconsistent notation; structures translated word for word from another language.

### Responding to reviewers

- Thank the reviewers once, at the start, not in every answer.
- Quote each comment, then answer it: what you changed and where (page, line, section), or why you did not, with evidence.
- Make every promised change in the manuscript and mark it as the journal asks (tracked changes or highlighting).
- Stay factual and polite when you disagree; never invent analyses you did not run.

### Reports, theses and conference abstracts

- **Research and technical reports** (not for a journal): the institution's template; an executive summary of the main findings first; headings that let readers find what they need. For Mongolian official reports, follow official-document style (the humanizer skills include an official-style guide).
- **Master's and doctoral theses:** IMRaD expanded into chapters, usually with a separate literature review chapter. Follow the university's regulations; ask the user for them.
- **Conference abstracts:** the conference's word limit and required headings.

### Output

- In Write mode, show the outline first unless the user supplied one or asked for the text directly.
- Mark every gap instead of filling it: "[citation needed]", "[n?]", "[ethics approval number]"; in Mongolian text «[эшлэл шаардлагатай]».
- After the text, list in a few lines what the user must check or supply: missing data, unverified references, journal requirements you assumed.

### Reference files

Read a reference file only when the task needs it.

| File | Language | Content |
|---|---|---|
| `references/imrad_structure.md` | English | IMRaD sections, alternatives, examples |
| `references/writing_principles.md` | English | Clarity, conciseness, accuracy, objectivity, revision |
| `references/citation_styles.md` | English | APA, AMA, Vancouver, Chicago, IEEE in detail |
| `references/figures_tables.md` | English | Choosing, designing and captioning figures and tables |
| `references/reporting_guidelines.md` | English | CONSORT 2025, STROBE, PRISMA 2020, SPIRIT 2025, STARD, TRIPOD+AI, ARRIVE, CARE, SQUIRE, CHEERS |
| `references/mn/butets.md` | Mongolian | IMRaD and Mongolian journal structure, section by section, tense, worked example |
| `references/mn/bichleg-zarchim.md` | Mongolian | Writing principles with Mongolian examples, revision checklist |
| `references/mn/eshlel.md` | Mongolian | Citation styles, Mongolian sources, «Лавай» bibliography, MNS 5217:2012 |
| `references/mn/zurag-husnegt.md` | Mongolian | Figures and tables, Mongolian captions and numbering |
| `references/mn/tailagnah-udirdamj.md` | Mongolian | Reporting guidelines explained in Mongolian |
| `references/mn/setguul-shaardlaga.md` | Mongolian | «Лавай» and MJER requirements, pre-submission checklist |
| `references/mn/mongol-nairuulga.md` | Mongolian | Mongolian scientific style, logic, terminology, common errors |

---

# Reference: references/imrad_structure.md

## IMRAD Structure Guide

### Overview

IMRAD (Introduction, Methods, Results, And Discussion) is the predominant organizational structure for scientific journal articles of original research. Adopted as the majority format since the 1970s, it is now the standard in medical, health, biological, chemical, engineering, and computer sciences.

### Why IMRAD?

The IMRAD structure mirrors the scientific method:
- **Introduction**: What question did you ask?
- **Methods**: How did you study it?
- **Results**: What did you find?
- **Discussion**: What does it mean?

This logical flow makes scientific papers easier to write, read, and evaluate.

### Complete Manuscript Components

A full scientific manuscript typically includes these sections in order:

1. **Title**
2. **Abstract**
3. **Introduction**
4. **Methods** (also called Materials and Methods, Methodology)
5. **Results**
6. **Discussion** (sometimes combined with Results)
7. **Conclusion** (sometimes part of Discussion)
8. **Acknowledgments**
9. **References**
10. **Supplementary Materials** (if applicable)

### Title

#### Purpose
Attract readers and accurately represent the paper's content.

#### Guidelines
- Be concise yet descriptive (typically 10-15 words)
- Include key variables and the relationship studied
- Avoid abbreviations, jargon, and question formats (unless the journal allows)
- Make it specific enough to distinguish from other studies
- Include key search terms for discoverability

#### Examples
- Good: "Effects of High-Intensity Interval Training on Cardiovascular Function in Older Adults"
- Too vague: "Exercise and Health"
- Too detailed: "A Randomized Controlled Trial Examining the Effects of High-Intensity Interval Training Compared to Moderate Continuous Training on Cardiovascular Function Measured by VO2 Max in Adults Aged 60-75 Years"

### Abstract

#### Purpose
Provide a complete, standalone summary enabling readers to decide if the full paper is relevant to them.

#### Structure
Most journals now require **structured abstracts** with labeled sections:

**Background/Objective**: Why was the study needed? What was the aim?
- 1-2 sentences
- State the research problem and objective

**Methods**: How was it done?
- 2-4 sentences
- Study design, participants, key procedures, analysis methods

**Results**: What was found?
- 3-5 sentences
- Main findings with key statistics
- Present the most important numerical data

**Conclusions**: What does it mean?
- 1-2 sentences
- Interpretation and implications
- Avoid overstating or adding new information

#### Length
- Typically 100-250 words (check journal requirements)
- Some journals allow up to 300 words

#### Key Rules
- Write the abstract **last** (after completing all other sections)
- Make it fully understandable without reading the paper
- Do not cite references in the abstract
- Avoid abbreviations or define them at first use
- Use past tense for methods and results, present tense for conclusions
- Include key quantitative results with statistical measures

#### Example Structure
```
Background: Hospital-acquired infections remain a major cause of morbidity. This study
evaluated the effectiveness of a new disinfection protocol in reducing infection rates.

Methods: We conducted a 12-month before-after study in a 500-bed teaching hospital.
Environmental surfaces were cultured monthly, and infection rates were tracked via
surveillance data. The intervention involved UV-C disinfection added to standard cleaning.

Results: Post-intervention, surface contamination decreased by 47% (95% CI: 38-56%,
p<0.001), and catheter-associated urinary tract infections declined from 3.2 to 1.8
per 1000 catheter-days (RR=0.56, 95% CI: 0.38-0.83, p=0.004). No adverse effects were
observed.

Conclusions: UV-C disinfection significantly reduced environmental contamination and
infection rates. This intervention may be a valuable addition to hospital infection
control programs.
```

### Introduction

#### Purpose
Convince readers that the research addresses an important question using an appropriate approach.

#### Structure and Content

**Paragraph 1: The Big Picture**
- Establish the broad research area
- Explain why this topic matters
- Use present tense for established facts
- Keep it accessible to non-specialists

**Paragraphs 2-3: Narrowing Down**
- Review relevant prior research
- Show what is already known
- Identify controversies or limitations in existing work
- Create a logical progression toward the gap

**Paragraph 4: The Gap**
- Explicitly identify what remains unknown
- Explain why this knowledge gap is problematic
- Connect the gap to the big picture importance

**Final Paragraph: This Study**
- State the specific research question or hypothesis
- Describe the overall approach briefly
- Explain how this study addresses the gap
- Optional: Preview key findings (some journals discourage this)

#### Length
- Typically 1.5-2 pages (depending on journal)
- Usually 4-5 paragraphs
- Shorter for letters/brief communications

#### Verb Tense
- **Present tense**: Established facts ("Exercise improves cardiovascular health")
- **Past tense**: Previous studies and their findings ("Smith et al. found that...")
- **Present/past tense**: Your study aims ("This study investigates..." or "This study investigated...")

#### Common Mistakes to Avoid
- Starting too broad (e.g., "Since the beginning of time...")
- Exhaustive literature review (save for review articles)
- Citing irrelevant or outdated references
- Failing to identify a clear gap
- Weak justification for the study
- Not stating a clear research question or hypothesis
- Including methods or results (these belong in later sections)

#### Key Questions to Answer
1. What do we know about this topic?
2. What don't we know? (the gap)
3. Why does this gap matter?
4. What did this study aim to find out?

### Methods

#### Purpose
Provide sufficient detail for others to replicate the study and evaluate its validity.

#### Key Principle
Another expert in the field should be able to repeat your experiment exactly as you performed it.

#### Standard Subsections

##### Study Design
- State the overall design (e.g., randomized controlled trial, cohort study, cross-sectional survey)
- Justify the design choice if not obvious
- Mention blinding, randomization, or controls if applicable

##### Participants/Subjects/Sample
- Define the population of interest
- Describe inclusion and exclusion criteria precisely
- Report sample size and how it was determined (power analysis)
- Explain recruitment methods and setting
- For animals: specify species, strain, age, sex, housing conditions

##### Materials and Equipment
- List all materials, reagents, and equipment used
- Include manufacturer names and locations (in parentheses)
- Specify catalog numbers for specialized items
- Report software names and versions

##### Procedures
- Describe what was done in chronological order
- Include sufficient detail for replication
- Use subheadings to organize complex procedures
- Specify timing (e.g., "incubated for 2 hours at 37°C")
- For surveys/interviews: describe instruments, validation, administration

##### Measurements and Outcomes
- Define all variables measured
- Specify primary and secondary outcomes
- Describe measurement instruments and their validity
- Include units of measurement

##### Statistical Analysis
- Name all statistical tests used
- Justify test selection
- State significance level (typically α = 0.05)
- Report power analysis for sample size
- Name statistical software with version
- Describe handling of missing data
- Mention adjustments for multiple comparisons if applicable

##### Ethical Considerations
- State IRB/ethics committee approval (with approval number)
- Mention informed consent procedures
- For human studies: state adherence to Helsinki Declaration
- For animal studies: state adherence to relevant guidelines (e.g., ARRIVE)

#### Length
- Typically 2-4 pages
- Proportional to study complexity

#### Verb Tense
- **Past tense** for actions you performed ("We measured...", "Participants completed...")
- **Present tense** for established procedures ("PCR amplifies...", "The questionnaire contains...")

#### Common Mistakes
- Insufficient detail for replication
- Methods appearing for the first time in Results
- Including results or discussion
- Missing statistical tests
- Undefined abbreviations
- Lack of ethical approval statement

### Results

#### Purpose
Present the findings objectively without interpretation.

#### Key Principle
Show, don't interpret. Save interpretation for the Discussion.

#### Structure and Content

**Opening Paragraph**
- Describe the participants/sample characteristics
- Report recruitment flow (e.g., screened, enrolled, completed)
- Consider including a CONSORT-style flow diagram

**Subsequent Paragraphs**
- Present results in logical order (usually primary outcome first)
- Follow the order of objectives stated in Introduction
- Organize by theme or by chronology, depending on what's clearest
- Reference figures and tables by number

**Each Finding Should Include:**
- The observed result
- The direction of the effect
- The magnitude of the effect
- The statistical significance
- The confidence interval

**Example**: "Mean systolic blood pressure decreased by 12 mmHg in the intervention group compared to 3 mmHg in controls (difference: 9 mmHg, 95% CI: 4-14 mmHg, p=0.002)."

#### Integration with Figures and Tables

**When to Use:**
- **Figures**: Trends, patterns, distributions, comparisons, relationships
- **Tables**: Precise values, demographic data, multiple variables

**How to Reference:**
- "Figure 1 shows the distribution of..." (not "Figure 1 below")
- "Table 2 presents baseline characteristics..."
- Don't repeat all table data in text; highlight key findings
- Each figure/table should be referenced in text

#### Figures and Tables Guidelines
- Number consecutively in order of mention
- Include complete, standalone captions
- Define all abbreviations in caption or footnote
- Report sample sizes (n)
- Indicate statistical significance (*, p-values)
- Use consistent formatting

#### Statistical Reporting

**Required Elements:**
- Test statistic (t, F, χ², etc.)
- Degrees of freedom
- p-value (exact if p > 0.001, otherwise report as "p < 0.001")
- Effect size and confidence interval
- Sample sizes

**Example**: "Groups differed significantly on test performance (t(48) = 3.21, p = 0.002, Cohen's d = 0.87, 95% CI: 0.34-1.40)."

#### Length
- Typically 2-4 pages
- Roughly equivalent to Methods length

#### Verb Tense
- **Past tense** for your findings ("The mean was...", "Participants showed...")

#### Common Mistakes
- Interpreting results (save for Discussion)
- Repeating all table/figure data in text
- Presenting new methods
- Insufficient statistical detail
- Inconsistent units or notation
- Not addressing negative or unexpected findings
- Selective reporting (all tested hypotheses should be reported)

#### Organization Strategies

**By Objective:**
```
Effect of intervention on primary outcome
Effect of intervention on secondary outcome A
Effect of intervention on secondary outcome B
```

**By Analysis Type:**
```
Descriptive statistics
Univariate analyses
Multivariate analyses
```

**Chronological:**
```
Baseline characteristics
Short-term outcomes (1 month)
Long-term outcomes (6 months)
```

### Discussion

#### Purpose
Interpret findings, relate them to existing knowledge, acknowledge limitations, and propose future directions.

#### Structure and Content

**Paragraph 1: Summary of Main Findings**
- Restate the primary objective or hypothesis
- Summarize the principal findings in 2-4 sentences
- Avoid repeating details from Results
- State clearly whether the hypothesis was supported

**Paragraphs 2-4: Interpretation in Context**
- Compare your findings with previous research
- Explain agreements and disagreements with prior work
- Propose mechanisms or explanations for findings
- Discuss unexpected results
- Consider alternative explanations
- Address whether findings support or refute existing theories

**Paragraph 5: Strengths and Limitations**
- Acknowledge study limitations honestly
- Explain how limitations might affect interpretation
- Mention study strengths (design, sample, methods)
- Avoid generic limitations ("larger sample needed")—be specific

**Paragraph 6: Implications**
- Clinical implications (for medical research)
- Practical applications
- Policy implications
- Theoretical contributions

**Final Paragraph: Conclusions and Future Directions**
- Summarize the take-home message
- Suggest specific future research to address gaps or limitations
- End with a strong concluding statement

#### Length
- Typically 3-5 pages
- Usually the longest section

#### Verb Tense
- **Past tense**: Your study findings ("We found that...", "The results showed...")
- **Present tense**: Established facts and your interpretations ("This suggests that...", "These findings indicate...")
- **Future tense**: Implications and future research ("Future studies should investigate...")

#### Discussion Strategies

**Comparing to Prior Work:**
```
"Our finding of a 30% reduction in symptoms aligns with Smith et al. (2023), who
reported a 28% reduction using a similar intervention. However, Jones et al. (2022)
found no significant effect, possibly due to their use of a less intensive protocol."
```

**Proposing Mechanisms:**
```
"The observed improvement in cognitive function may result from increased cerebral
blood flow, as evidenced by the concurrent increase in functional MRI signals in the
prefrontal cortex. This interpretation is consistent with the vascular hypothesis of
cognitive enhancement."
```

**Acknowledging Limitations:**
```
"The cross-sectional design prevents causal inference. Additionally, the convenience
sample from a single academic medical center may limit generalizability to community
settings. Self-reported measures may introduce recall bias, though we attempted to
minimize this through structured interviews."
```

#### Common Mistakes
- Simply repeating results without interpretation
- Over-interpreting findings or claiming causation without warrant
- Ignoring inconsistent or negative findings
- Failing to compare with existing literature
- Introducing new data or methods
- Generic or superficial discussion of limitations
- Overgeneralization beyond the study population
- Missing the "so what?"—failing to explain significance

#### Key Questions to Answer
1. What do these findings mean?
2. How do they compare to prior research?
3. Why might differences exist?
4. What are alternative explanations?
5. What are the limitations?
6. What are the practical implications?
7. What should future research investigate?

### Conclusion

#### Purpose
Provide a concise summary of key findings and their significance.

#### Placement
- May be a separate section or the final paragraph of Discussion (check journal requirements)

#### Content
- 1-2 paragraphs maximum
- Restate the main finding(s)
- Emphasize the significance or implications
- End with a strong, memorable statement
- Do NOT introduce new information

#### Example
```
This randomized trial demonstrates that a 12-week mindfulness intervention significantly
reduces anxiety symptoms in college students, with effects persisting at 6-month follow-up.
These findings support the integration of mindfulness-based programs into university mental
health services. Given the scalability and cost-effectiveness of group-based mindfulness
training, this approach offers a promising strategy to address the growing mental health
crisis in higher education.
```

### Additional Sections

#### Acknowledgments
- Thank funding sources (with grant numbers)
- Acknowledge substantial contributions not qualifying for authorship
- Thank those who provided materials, equipment, or assistance
- Declare any conflicts of interest

#### References
- Format according to journal style (see `citation_styles.md`)
- Verify all citations are accurate
- Ensure all citations appear in text and vice versa
- Typical range: 20-50 references for original research

#### Supplementary Materials
- Additional figures, tables, or data sets
- Detailed protocols or questionnaires
- Video or audio files
- Large datasets or code repositories

### Tense Usage Summary

| Section | Verb Tense |
|---------|-----------|
| Abstract - Background | Present (established facts) or past (prior studies) |
| Abstract - Methods | Past |
| Abstract - Results | Past |
| Abstract - Conclusions | Present |
| Introduction - General background | Present |
| Introduction - Prior studies | Past |
| Introduction - Your objectives | Present or past |
| Methods | Past (your actions), present (general procedures) |
| Results | Past |
| Discussion - Your findings | Past |
| Discussion - Interpretations | Present |
| Discussion - Prior work | Present or past |
| Conclusion | Present |

### IMRAD Variations

#### Combined Results and Discussion
- Some journals allow or require this format
- Interweaves presentation and interpretation
- Each result is presented then immediately discussed
- Useful for complex studies with multiple experiments

#### IMRaD without separate Conclusion
- Conclusion integrated into final Discussion paragraph
- Common in many journals

#### Extended IMRAD (ILMRaD)
- Adds "Literature Review" as separate section
- More common in theses and dissertations

### Adapting IMRAD to Different Study Types

#### Clinical Trials
- Add CONSORT flow diagram in Results
- Include trial registration number in Methods
- Report adverse events in Results

#### Systematic Reviews/Meta-Analyses
- Methods describes search strategy and inclusion criteria
- Results includes PRISMA flow diagram and synthesis
- May have additional sections (risk of bias assessment)

#### Case Reports
- Introduction: background on the condition
- Case Presentation: replaces Methods and Results
- Discussion: relates case to literature

#### Observational Studies
- Follow STROBE guidelines
- Careful attention to potential confounders in Methods
- Discussion addresses causality limitations

### Venue-Specific Structure Expectations

#### Journal vs. Conference Formats

| Venue Type | Length | Structure | Methods Placement | Key Focus |
|-----------|--------|-----------|-------------------|-----------|
| **Nature/Science** | 2,000-4,500 words | Modified IMRAD | Supplement | Broad significance |
| **Medical** | 2,700-3,500 words | Strict IMRAD | Main text | Clinical outcomes |
| **Field journals** | 3,000-6,000 words | Standard IMRAD | Main text | Technical depth |
| **ML conferences** | 8-9 pages (~6,000 words) | Intro-Method-Experiments-Conclusion | Main text (concise) | Novel contribution |

#### ML Conference Structure (NeurIPS/ICML/ICLR)

**Typical 8-page structure:**
1. **Abstract** (150-200 words): Problem, method, key results
2. **Introduction** (1 page): Motivation, contribution summary, related work overview
3. **Method** (2-3 pages): Technical approach, architecture, algorithms
4. **Experiments** (2-3 pages): Setup, datasets, baselines, results, ablations
5. **Related Work** (0.5-1 page, often in appendix): Detailed literature comparison
6. **Conclusion** (0.25-0.5 pages): Summary, limitations, future work
7. **References** (within page limit or separate depending on conference)
8. **Appendix/Supplement** (unlimited): Additional experiments, proofs, details

**Key differences from journals:**
- **Contribution bullets**: Often numbered list in intro (e.g., "Our contributions are: (1)... (2)... (3)...")
- **No separate Results/Discussion**: Integrated in Experiments section
- **Ablation studies**: Critical component showing what matters
- **Computational requirements**: Often required (training time, GPUs, memory)
- **Code availability**: Increasingly expected

#### Section Length Proportions

| Venue | Intro | Methods | Results/Experiments | Discussion/Conclusion |
|-------|-------|---------|---------------------|----------------------|
| **Nature/Science** | 10% | 15%* | 40% | 35% |
| **Medical (NEJM/JAMA)** | 10% | 25% | 30% | 35% |
| **Field journals** | 20% | 25% | 30% | 25% |
| **ML conferences** | 12-15% | 30-35% | 40-45% | 5-8% |

*Methods often in supplement for Nature/Science

**Key medical journal features:**
- NEJM/Lancet/JAMA: Strict IMRAD; clinical focus; structured Discussion; CONSORT/STROBE compliance
- Clear primary/secondary outcomes; statistical pre-specification

**Key ML conference features:**
- Numbered contribution list in intro
- Method details with pseudocode/equations
- Extensive experiments: main results, ablations, analysis
- Brief conclusion (limitations noted)
- Related work often in appendix

#### Writing Style by Venue

| Venue | Audience | Intro Focus | Methods Detail | Results/Experiments | Discussion/Conclusion |
|-------|----------|-------------|----------------|---------------------|----------------------|
| **Nature/Science** | Non-specialists | Broad significance | Brief, supplement | Story-driven | Broad implications |
| **Medical** | Clinicians | Clinical problem | Comprehensive | Primary outcome first | Clinical relevance |
| **Specialized** | Experts | Field context | Full technical | By experiment | Mechanistic depth |
| **ML conferences** | ML researchers | Novel contribution | Reproducible | Baselines, ablations | Brief, limitations |

**ML conference emphasis:**
- **Introduction**: Clear problem statement; numbered contributions; positioning vs. prior work
- **Method**: Mathematical notation; pseudocode; architecture diagrams; complexity analysis
- **Experiments**: Datasets described; multiple baselines; ablation studies; error analysis
- **Conclusion**: Summary; acknowledged limitations; broader impact (if required)

#### Evaluation Across Venues

**What gets checked:**
- **Fit**: Appropriate for venue scope and audience
- **Length**: Within limits (strict for conferences)
- **Clarity**: Writing quality sufficient; claims supported
- **Reproducibility**: Methods enable replication
- **Completeness**: All outcomes reported; limitations acknowledged

**Common rejection reasons:**
- Insufficient significance for venue
- Methods lack detail for reproduction
- Results don't support claims
- Discussion overstates findings
- Page/word limits exceeded (conferences strict)

**ML conference specific evaluation:**
- Clear problem formulation and motivation
- Novelty and contribution well-articulated
- Baselines comprehensive and fair
- Ablation studies demonstrate what works
- Code/data availability (increasingly required)
- Reproducibility information (seeds, hyperparameters)

#### Quick Adaptation Guide

**Journal → ML conference:**
- Condense intro; add numbered contributions
- Methods: keep concise, add pseudocode
- Combine Results+Discussion → Experiments section
- Add extensive ablations and baseline comparisons
- Brief conclusion with limitations

**ML conference → Journal:**
- Expand introduction with more background
- Separate Methods section with full details
- Split Experiments into Results and Discussion
- Remove contribution numbering
- Expand limitations discussion

**Specialist → Broad journal:**
- Simplify intro; emphasize broad significance
- Move technical methods to supplement
- Story-driven results organization
- Lead discussion with implications

**Broad → Specialist:**
- Add detailed literature review
- Full methods in main text
- Organize results by experiment
- Add mechanistic discussion depth

#### Pre-Submission Structure Checklist

**All venues:**
- [ ] Word/page count within limits
- [ ] Section proportions appropriate
- [ ] Writing style matches venue
- [ ] Methods enable reproducibility
- [ ] Limitations acknowledged

**ML conferences add:**
- [ ] Contributions clearly listed
- [ ] Ablation studies included
- [ ] Baselines comprehensive
- [ ] Hyperparameters/seeds reported
- [ ] Code availability statement

---

# Reference: references/writing_principles.md

## Scientific Writing Principles

### Overview

Effective scientific writing requires mastering fundamental principles that ensure clarity, precision, and impact. Unlike creative or narrative writing, scientific writing prioritizes accuracy, conciseness, and objectivity. This guide covers the core principles that distinguish good scientific writing from poor writing and provides practical strategies for improvement.

### The Three Pillars of Scientific Writing

#### 1. Clarity

**Definition:** Writing that is immediately understandable to the intended audience without ambiguity or confusion.

**Why it matters:** Science is complex enough without unclear writing adding confusion. Readers should focus on understanding the science, not deciphering the prose.

##### Strategies for Clarity

**Use precise, unambiguous language:**
```
Poor: "The drug seemed to help quite a few patients."
Better: "The drug reduced symptoms in 68% (32/47) of patients."
```

**Define technical terms at first use:**
```
"We measured brain-derived neurotrophic factor (BDNF), a protein involved in
neuronal survival and plasticity."
```

**Maintain logical flow within and between paragraphs:**
- Each paragraph should have one main idea
- Topic sentence introduces the paragraph's focus
- Supporting sentences develop that focus
- Transition sentences connect paragraphs

**Use active voice when it improves clarity:**
```
Passive (less clear): "The samples were analyzed by the researchers."
Active (clearer): "Researchers analyzed the samples."
```

However, passive voice is acceptable and often preferred in Methods when the action is more important than the actor:
```
"Blood samples were collected at baseline and after 6 weeks."
```

**Break up long, complex sentences:**
```
Poor: "The results of our study, which involved 200 participants recruited from
three hospitals and followed for 12 months with assessments every 4 weeks using
validated questionnaires, showed significant improvements in the intervention
group."

Better: "Our study involved 200 participants recruited from three hospitals.
Participants were followed for 12 months with assessments every 4 weeks using
validated questionnaires. The intervention group showed significant improvements."
```

**Use specific verbs:**
```
Weak: "The study looked at depression in adolescents."
Stronger: "The study examined factors contributing to depression in adolescents."
```

##### Common Clarity Problems

**Ambiguous pronouns:**
```
Poor: "Group A received the drug and Group B received placebo. They showed
improvement."
(Who is "they"?)

Better: "Group A received the drug and Group B received placebo. The drug-treated
group showed improvement."
```

**Misplaced modifiers:**
```
Poor: "We measured blood pressure in patients using an automated monitor."
(Are the patients using the monitor, or are we?)

Better: "Using an automated monitor, we measured blood pressure in patients."
```

**Unclear referents:**
```
Poor: "The increase in expression was accompanied by decreased proliferation, which
was unexpected."
(What was unexpected—the decrease, the accompaniment, or both?)

Better: "The increase in expression was accompanied by decreased proliferation.
This inverse relationship was unexpected."
```

#### 2. Conciseness

**Definition:** Expressing ideas in the fewest words necessary without sacrificing clarity or completeness.

**Why it matters:** Concise writing respects readers' time. Every unnecessary word is a missed opportunity for clarity and impact. As the principle states: "We value concise writing because we value time."

##### Strategies for Conciseness

**Eliminate redundant words and phrases:**

| Wordy | Concise |
|-------|---------|
| "due to the fact that" | "because" |
| "in order to" | "to" |
| "it is important to note that" | [delete] |
| "a total of 50 participants" | "50 participants" |
| "completely eliminate" | "eliminate" |
| "has been shown to be" | "is" |
| "in the event that" | "if" |
| "at the present time" | "now" or "currently" |
| "conduct an investigation into" | "investigate" |
| "give consideration to" | "consider" |

**Avoid throat-clearing phrases:**
```
Wordy: "It is interesting to note that the results of our study demonstrate that..."
Concise: "Our results demonstrate that..." or "The results show that..."
```

**Use strong verbs instead of noun+verb combinations:**

| Wordy | Concise |
|-------|---------|
| "make a decision" | "decide" |
| "perform an analysis" | "analyze" |
| "conduct a study" | "study" or "studied" |
| "make an assessment" | "assess" |
| "provide information about" | "inform" |

**Eliminate unnecessary intensifiers:**
```
Wordy: "The results were very significant."
Concise: "The results were significant." (p-value conveys the degree)
```

**Avoid repeating information unnecessarily:**
```
Redundant: "The results showed that participants in the intervention group, who
received the treatment intervention, had better outcomes."
Concise: "The intervention group had better outcomes."
```

**Favor shorter constructions:**
```
Wordy: "In spite of the fact that the sample size was small..."
Concise: "Although the sample size was small..."
```

##### Acceptable Length vs. Unnecessary Length

**Not all long sentences are bad:**
```
This detailed sentence is fine: "We analyzed blood samples using liquid
chromatography-tandem mass spectrometry (LC-MS/MS) with a Waters Acquity UPLC
system coupled to a Xevo TQ-S mass spectrometer (Waters Corporation, Milford, MA)."

Why? Because each element is necessary information.
```

**The key question:** Can any word be removed without losing meaning or precision? If yes, remove it.

#### 3. Accuracy

**Definition:** Precise, correct representation of data, methods, and interpretations.

**Why it matters:** Scientific credibility depends on accuracy. Inaccurate reporting undermines the entire scientific enterprise.

##### Strategies for Accuracy

**Report exact values with appropriate precision:**
```
Poor: "The mean was about 25."
Better: "The mean was 24.7 ± 3.2 (SD)."
```

**Match precision to measurement capability:**
```
Inappropriate: "Mean age was 45.237 years" (implies false precision)
Appropriate: "Mean age was 45.2 years"
```

**Use consistent terminology throughout:**
```
Inconsistent: Introduction calls it "cognitive function," Methods call it "mental
performance," Results call it "intellectual ability."

Consistent: Use "cognitive function" throughout, or define explicitly: "cognitive
function (also termed mental performance)"
```

**Distinguish observations from interpretations:**
```
Observation: "Mean blood pressure decreased from 145 to 132 mmHg (p=0.003)."
Interpretation: "This suggests the intervention effectively lowers blood pressure."
```

**Be specific about uncertainty:**
```
Vague: "There may be some error in these measurements."
Specific: "Measurements have a standard error of ±2.5 mmHg based on instrument
specifications."
```

**Use correct statistical language:**
```
Incorrect: "The correlation was highly significant (p=0.03)."
Correct: "The correlation was statistically significant (p=0.03)."
(p=0.03 is not "highly" significant; that's reserved for p<0.001)
```

**Verify all numbers:**
- Check that numbers in text match tables/figures
- Verify that n values sum correctly
- Confirm percentages are correctly calculated
- Double-check all statistics

##### Common Accuracy Problems

**Overgeneralization:**
```
Poor: "Exercise prevents depression."
Better: "In our sample, participants randomized to the exercise intervention showed
fewer depressive symptoms than controls (mean difference 3.2 points on the BDI-II,
95% CI: 1.5-4.9, p<0.001)."
```

**Unwarranted causal claims:**
```
Poor (from observational study): "Vitamin D supplementation reduces cancer risk."
Better: "Vitamin D levels were inversely associated with cancer incidence in this
cohort (HR=0.82, 95% CI: 0.71-0.95)."
```

**Imprecise numerical descriptions:**
```
Vague: "Many participants dropped out."
Precise: "15/50 (30%) participants withdrew before study completion."
```

### Additional Key Principles

#### 4. Objectivity

**Definition:** Presenting information impartially without bias, exaggeration, or unsupported opinion.

**Strategies:**

**Present results without bias:**
```
Biased: "As expected, our superior method performed better."
Objective: "Method A showed higher accuracy than Method B (87% vs. 76%, p=0.02)."
```

**Acknowledge conflicting evidence:**
```
"Our findings contrast with Smith et al. (2022), who reported no significant effect.
This discrepancy may result from differences in intervention intensity or population
characteristics."
```

**Avoid emotional or evaluative language:**
```
Subjective: "The results were disappointing and concerning."
Objective: "The intervention did not significantly reduce symptoms (p=0.42)."
```

**Distinguish fact from speculation:**
```
"The observed decrease in cell viability was accompanied by increased caspase-3
activity, suggesting that apoptosis may be the primary mechanism of cell death."
(Uses "suggesting" and "may be" to indicate interpretation)
```

#### 5. Consistency

**Maintain consistency throughout the manuscript:**

**Terminology:**
- Use the same term for the same concept (not synonyms for variety)
- Define abbreviations at first use and use consistently thereafter
- Use standard nomenclature for genes, proteins, chemicals

**Notation:**
- Statistical notation (p-value format, CI presentation)
- Units of measurement
- Number formatting (decimal places)

**Tense:**
- Past tense for your specific study actions
- Present tense for established facts
- See detailed tense guide in IMRAD structure reference

**Style:**
- Follow journal guidelines consistently
- Citation format
- Heading capitalization
- Number vs. word for numerals

#### 6. Logical Organization

**Create a clear "red thread" through the manuscript:**

**Paragraph structure:**
1. Topic sentence (main idea)
2. Supporting sentences (evidence, explanation)
3. Concluding/transition sentence (link to next idea)

**Section flow:**
- Each section builds logically on the previous
- Questions raised in Introduction are answered in Results
- Findings presented in Results are interpreted in Discussion

**Signposting:**
```
"First, we examined..."
"Next, we investigated..."
"Finally, we assessed..."
```

**Parallelism:**
```
Not parallel: "Aims were to (1) measure blood pressure, (2) assessment of
cognitive function, and (3) we wanted to evaluate mood."

Parallel: "Aims were to (1) measure blood pressure, (2) assess cognitive
function, and (3) evaluate mood."
```

### Verb Tense in Scientific Writing

#### General Guidelines

**Present tense** for:
- Established facts and general truths
  - "DNA is composed of nucleotides."
- Conclusions you are drawing
  - "These findings suggest that..."
- Referring to figures and tables
  - "Figure 1 shows the distribution..."

**Past tense** for:
- Specific findings from completed research (yours and others')
  - "Smith et al. (2022) found that..."
  - "We observed a significant decrease..."
- Methods you performed
  - "Participants completed questionnaires at baseline."

**Present perfect** for:
- Recent developments with current relevance
  - "Recent studies have demonstrated..."
- Research area background
  - "Several approaches have been proposed..."

#### Section-Specific Tense

| Section | Primary Tense | Examples |
|---------|---------------|----------|
| **Abstract - Background** | Present or present perfect | "Depression affects millions" / "Research has shown..." |
| **Abstract - Methods** | Past | "We recruited 100 participants" |
| **Abstract - Results** | Past | "The intervention reduced symptoms" |
| **Abstract - Conclusions** | Present | "These findings suggest..." |
| **Introduction - Background** | Present (facts), present perfect (research) | "Exercise is beneficial" / "Studies have shown..." |
| **Introduction - Gap** | Present or present perfect | "However, little is known..." |
| **Introduction - This study** | Past or present | "We investigated..." / "This study investigates..." |
| **Methods** | Past | "We collected samples..." |
| **Results** | Past | "Mean age was 45 years" |
| **Discussion - Your findings** | Past | "We found that..." |
| **Discussion - Interpretation** | Present | "This suggests..." |
| **Discussion - Prior work** | Past or present | "Smith found..." / "Previous work demonstrates..." |

### Common Writing Pitfalls

#### 1. Jargon Overload

**Problem:** Excessive use of technical terms without definition

**Example:**
```
Poor: "We utilized qRT-PCR to quantify mRNA expression via SYBR-Green-based
fluorescence detection following cDNA synthesis from total RNA using oligo-dT primers."

Better: "We quantified mRNA expression using quantitative reverse transcription PCR
(qRT-PCR). Total RNA was reverse transcribed to complementary DNA (cDNA) using
oligo-dT primers, then amplified with SYBR Green fluorescent detection."
```

#### 2. Nominalization

**Problem:** Turning verbs into nouns, making writing heavy and indirect

**Examples:**

| Nominalized | Direct |
|-------------|--------|
| "give consideration to" | "consider" |
| "make an assumption" | "assume" |
| "perform an investigation" | "investigate" |
| "conduct an examination" | "examine" |
| "achieve a reduction" | "reduce" |

#### 3. Hedging Excessively or Insufficiently

**Excessive hedging** (sounds uncertain):
```
"It could perhaps be possible that the intervention might possibly have some effect
on symptoms under certain conditions."
```

**Insufficient hedging** (overstates conclusions):
```
"The intervention cures depression."
```

**Appropriate hedging:**
```
"The intervention significantly reduced depressive symptoms in this sample,
suggesting it may be effective for treating mild to moderate depression."
```

**Hedging words to use appropriately:**
- Suggests, indicates, implies (not proves, demonstrates for correlational data)
- May, might, could (possibilities)
- Appears to, seems to (observations needing confirmation)
- Likely, probably, possibly (degrees of certainty)

#### 4. Anthropomorphism

**Problem:** Attributing human characteristics to non-human entities

**Examples:**

| Anthropomorphic | Scientific |
|----------------|-----------|
| "The study wanted to examine..." | "We aimed to examine..." or "The study examined..." |
| "The data suggest they want..." | "The data suggest that..." |
| "This paper will prove..." | "This paper demonstrates..." |
| "Table 1 tells us..." | "Table 1 shows..." |

#### 5. Abbreviation Abuse

**Problems:**
- Too many abbreviations burden the reader
- Abbreviating terms used only once or twice
- Not defining abbreviations at first use

**Guidelines:**
- Only abbreviate terms used ≥3-4 times
- Define at first use in abstract (if used in abstract)
- Define at first use in main text
- Don't abbreviate in title
- Limit to 3-4 new abbreviations per paper when possible
- Use standard abbreviations (DNA, RNA, HIV, etc.) without definition

**Example:**
```
Poor: "We measured Brain-Derived Neurotrophic Factor (BDNF) at baseline. BDNF
levels were elevated."
(Only used twice, abbreviation unnecessary)

Better: "We measured brain-derived neurotrophic factor at baseline. Levels were
elevated."
```

### Specific Sentence-Level Issues

#### Dangling Modifiers

**Problem:**
```
"After incubating for 2 hours, we measured absorbance."
(The sentence suggests "we" were incubated)

Better: "After incubating samples for 2 hours, we measured absorbance."
Or: "After 2-hour incubation, we measured absorbance."
```

#### Misplaced Commas

**Common errors:**

**Between subject and verb:**
```
Wrong: "The participants in the intervention group, showed improvement."
Right: "The participants in the intervention group showed improvement."
```

**In compound predicates:**
```
Wrong: "We measured blood pressure, and recorded symptoms."
Right: "We measured blood pressure and recorded symptoms."
(No comma before "and" when it doesn't join independent clauses)
```

#### Pronoun Agreement

```
Wrong: "Each participant completed their questionnaire."
Right: "Each participant completed his or her questionnaire."
Or better: "Participants completed their questionnaires."
```

#### Subject-Verb Agreement

```
Wrong: "The group of participants were heterogeneous."
Right: "The group of participants was heterogeneous."
(Subject is "group" [singular], not "participants")

But: "The participants were heterogeneous." (Plural subject)
```

### Word Choice

#### Commonly Confused Words in Scientific Writing

| Often Misused | Correct Usage |
|---------------|---------------|
| **affect / effect** | Affect (verb): influence; Effect (noun): result; Effect (verb): bring about |
| **among / between** | Among: three or more; Between: two |
| **continual / continuous** | Continual: repeated; Continuous: uninterrupted |
| **data is / data are** | Data are (plural); datum is (singular) |
| **fewer / less** | Fewer: countable items; Less: continuous quantities |
| **i.e. / e.g.** | i.e. (that is): restatement; e.g. (for example): examples |
| **imply / infer** | Imply: suggest; Infer: deduce |
| **parameter / variable** | Parameter: population value; Variable: measured characteristic |
| **principal / principle** | Principal: main; Principle: rule or concept |
| **significant** | Reserve for statistical significance, not importance |
| **that / which** | That: restrictive clause; Which: nonrestrictive clause |

#### Words to Avoid or Use Carefully

**Avoid informal language:**
- "a lot of" → "many" or "substantial"
- "got" → "obtained" or "became"
- "showed up" → "appeared" or "was evident"

**Avoid vague quantifiers:**
- "some" → specify how many
- "often" → specify frequency
- "recently" → specify timeframe

**Avoid unnecessary modifiers:**
- "very significant" → "significant" (p-value shows degree)
- "quite large" → "large" or specify size
- "rather interesting" → delete or explain why

### Numbers and Units

#### When to Use Numerals vs. Words

**Use numerals for:**
- All numbers ≥10
- Numbers with units (5 mg, 3 mL)
- Statistical values (p=0.03, t=2.14)
- Ages, dates, times
- Scores and scales
- Percentages (15%)

**Use words for:**
- Numbers <10 when not connected to units (five participants)
- Numbers beginning a sentence (spell out or restructure)

**Examples:**
```
"Five participants withdrew" OR "There were 5 withdrawals"
(NOT: "5 participants withdrew")

"We tested 15 samples at 3 time points"
"Mean age was 45 years"
```

#### Units and Formatting

**Guidelines:**
- Space between number and unit (5 mg, not 5mg)
- No period after units (mg not mg.)
- Use SI units unless field convention differs
- Be consistent in decimal places
- Use commas for thousands in text (12,500 not 12500)

**Ranges:**
- Use en-dash (–) for ranges: 15–20 mg
- Include unit only after second number: 15–20 mg (not 15 mg–20 mg)

### Paragraph Structure

#### Ideal Paragraph Length

**Guidelines:**
- 3-7 sentences typically
- One main idea per paragraph
- Too short (<2 sentences): may indicate idea needs development or combining
- Too long (>10 sentences): may need splitting

#### Paragraph Coherence

**Techniques:**

**1. Topic sentence:**
```
"Exercise training improves cardiovascular function through multiple mechanisms.
[Following sentences explain these mechanisms]"
```

**2. Transitional phrases:**
- First, second, third, finally
- Furthermore, moreover, in addition
- However, nevertheless, conversely
- Therefore, thus, consequently
- For example, specifically, particularly

**3. Repetition of key terms:**
```
"...this mechanism of action. This mechanism may explain..."
(Not: "...this mechanism. This process may explain...")
```

**4. Parallel structure:**
```
"Group A received the drug. Group B received placebo. Group C received no treatment."
(Not: "Group A received the drug. Placebo was given to Group B. No treatment was
provided to the third group.")
```

### Revision Checklist

#### Content Level

- [ ] Does every sentence add value?
- [ ] Are claims supported by data?
- [ ] Is the logic clear and sound?
- [ ] Are interpretations warranted by results?

#### Paragraph Level

- [ ] Does each paragraph have one main idea?
- [ ] Are paragraphs in logical order?
- [ ] Are transitions smooth?
- [ ] Is there a clear "red thread"?

#### Sentence Level

- [ ] Are sentences clear and concise?
- [ ] Is sentence structure varied?
- [ ] Are there no dangling modifiers?
- [ ] Do subjects and verbs agree?

#### Word Level

- [ ] Is word choice precise?
- [ ] Are technical terms defined?
- [ ] Is terminology consistent?
- [ ] Are abbreviations necessary and defined?
- [ ] Are numbers formatted correctly?

#### Grammar and Mechanics

- [ ] Is verb tense correct and consistent?
- [ ] Are commas used correctly?
- [ ] Do pronouns agree with antecedents?
- [ ] Is punctuation correct?
- [ ] Is spelling correct (including technical terms)?

### Tools for Improving Writing

#### Grammar and Style Checkers

- **Grammarly**: Grammar, style, clarity
- **ProWritingAid**: In-depth writing analysis
- **Hemingway Editor**: Readability, simplification
- **LanguageTool**: Open-source grammar checker

**Caution:** These tools don't understand scientific writing conventions. Use them as a starting point, not final arbiter.

#### Readability Metrics

**Flesch Reading Ease:**
- 60-70: acceptable for scientific papers
- <60: may be too complex

**Caution:** Don't sacrifice precision for readability scores designed for general audiences.

#### Peer Review

**Most valuable tool:**
- Ask colleagues to read and provide feedback
- Identify unclear passages
- Check logical flow
- Verify interpretations are warranted

### Additional Resources

#### Books on Scientific Writing

- *The Elements of Style* by Strunk & White (classic on clear writing)
- *On Writing Well* by William Zinsser
- *Scientific Writing: A Reader and Writer's Guide* by Jean-Luc Lebrun
- *How to Write a Scientific Paper* by George M. Whitesides
- *Style: Lessons in Clarity and Grace* by Joseph Williams

#### Online Resources

- **Academic Phrasebank** (University of Manchester): Common academic phrases
- **Purdue OWL**: Grammar, punctuation, style
- **Nature Masterclasses**: Scientific writing courses
- **WritingCenters**: Many universities provide free online resources

#### University Writing Centers

Most research universities offer:
- Individual consultations
- Workshops on scientific writing
- Online resources and handouts
- Support for non-native English speakers

### Venue-Specific Writing Styles

#### Four Major Writing Style Categories

1. **Broad-audience accessible** (Nature, Science, PNAS)
2. **Clinical-professional** (NEJM, Lancet, JAMA)
3. **Technical-specialist** (field-specific journals)
4. **ML conference** (NeurIPS, ICML, ICLR, CVPR)

#### Writing Style Comparison

| Aspect | Nature/Science | Medical | Specialized | ML Conference |
|--------|---------------|---------|-------------|---------------|
| **Sentence length** | 15-20 words | 12-18 words | 18-25 words | 12-20 words |
| **Vocabulary** | Minimal jargon | Clinical terms | Field-specific | Technical + math |
| **Tone** | Engaging, significant | Conservative | Formal | Direct, contribution-focused |
| **Key phrases** | "Here we show" | "We conducted" | "To elucidate" | "We propose", "Our contributions" |

**ML Conference Style:**

**Characteristics:**
- Direct, technical language with mathematical notation
- Contribution-focused (numbered lists common)
- Assumes ML expertise (CNNs, transformers, SGD, etc.)
- Emphasizes novelty and performance gains
- Pseudocode and equations expected

**Example opening (NeurIPS style):**
```
Vision transformers have achieved state-of-the-art performance on image classification,
but their quadratic complexity limits applicability to high-resolution images. We propose
Efficient-ViT, which reduces complexity to O(n log n) while maintaining accuracy. Our
contributions are: (1) a novel sparse attention mechanism, (2) theoretical analysis
showing preserved expressive power, and (3) empirical validation on ImageNet showing
15% speedup with comparable accuracy.
```
- Problem stated with technical context
- Solution previewed
- Numbered contributions
- Quantitative claims

#### Key Writing Differences

| Aspect | Nature/Science | Medical | Specialized | ML Conference |
|--------|---------------|---------|-------------|---------------|
| **Paragraph length** | 3-5 sentences | 5-7 sentences | 6-10 sentences | 4-6 sentences |
| **Math/equations** | Minimize | Rare | Moderate | Essential |
| **Active voice** | Preferred | Mixed | Passive OK | Preferred |
| **Hedging** | Moderate | Conservative | Detailed | Minimal (claim gains) |
| **Figure integration** | Tight | Systematic | Detailed | Dense, in-page |

#### Evaluation Focus by Venue

| Venue | Key Evaluation Criteria |
|-------|------------------------|
| **Nature/Science** | Accessible to non-specialists? Broad significance clear? Compelling story? |
| **Medical** | Clinical relevance apparent? Professional tone? Methods adequate? |
| **Specialized** | Technical precision? Field expertise shown? Methods detailed? |
| **ML conferences** | Clear contributions? Claims supported by experiments? Reproducible? |

**Common rejection reasons:**
- Poor writing quality/unclear prose
- Inappropriate style for venue
- Overstated claims
- Methods insufficient for reproduction
- Missing key details (baselines, ablations for ML; statistics for journals)

#### Quick Style Adaptation Guide

| From → To | Key Changes |
|-----------|-------------|
| **Journal → ML conference** | Add numbered contributions; include equations/pseudocode; emphasize quantitative gains; condense prose |
| **ML conference → Journal** | Remove contribution numbering; expand motivation; separate Results/Discussion; reduce equations in main text |
| **Specialist → Broad** | Simplify language; emphasize broad implications; explain technical concepts; add context for non-experts |
| **Broad → Specialist** | Add technical detail; use field terminology freely; expand mechanistic discussion; cite field literature |
| **Basic science → Clinical** | Add patient/clinical context; use clinical language; emphasize outcomes/implications; cite clinical evidence |

#### Pre-Submission Style Checklist

**All venues:**
- [ ] Writing style matches 3-5 recent papers from venue
- [ ] Sentence length appropriate
- [ ] Technical vocabulary level correct
- [ ] Tone consistent with venue
- [ ] No overstated claims

**ML conferences add:**
- [ ] Contributions clearly numbered in intro
- [ ] Mathematical notation correct and consistent
- [ ] Pseudocode/algorithms included where appropriate
- [ ] Claims quantified (e.g., "15% faster", "2.3% accuracy gain")
- [ ] Limitations acknowledged

### Final Thoughts

Effective scientific writing is a skill developed through practice. Key principles:

1. **Clarity** trumps complexity
2. **Conciseness** respects readers' time
3. **Accuracy** builds credibility
4. **Objectivity** maintains scientific integrity
5. **Consistency** aids comprehension
6. **Logical organization** guides readers
7. **Journal-specific adaptation** maximizes publication success

**Remember:** The goal is not to impress readers with vocabulary or complexity, but to communicate your science clearly and precisely so readers can understand, evaluate, and build upon your work. Adapt your writing style to match your target journal's expectations and audience.

---

# Reference: references/citation_styles.md

## Citation Styles Guide

### Overview

Citation styles provide standardized formats for acknowledging sources in scientific writing. Different disciplines prefer different styles, and journals typically specify which style to use. The five most common citation styles in science are AMA, Vancouver, APA, Chicago, and IEEE.

### Choosing the Right Style

| Style | Primary Disciplines | In-Text Format |
|-------|-------------------|----------------|
| AMA | Medicine, health sciences | Superscript numbers¹ |
| Vancouver | Biomedical sciences | Numbers in brackets [1] |
| APA | Psychology, social sciences, education | Author-date (Smith, 2023) |
| Chicago | Humanities, history, some sciences | Notes-bibliography or author-date |
| IEEE | Engineering, computer science | Numbers in brackets [1] |
| ACS | Chemistry | Superscript numbers¹ or (1) |
| NLM | Life sciences, PubMed | Numbers in brackets [1] |

**Default recommendation**: When in doubt, check the journal's author guidelines. Most biomedical journals use Vancouver or AMA style.

### AMA Style (American Medical Association)

#### Overview
- Used primarily in medical research
- Based on the *AMA Manual of Style* (11th edition, 2020)
- Numbered citations appearing as superscripts
- References listed numerically in order of appearance

#### In-Text Citations

**Basic format**: Superscript numerals outside periods and commas, inside semicolons and colons.

**Examples:**
```
Several studies have demonstrated this effect.¹

The results were inconclusive,² although Smith et al³ reported otherwise.

These findings³⁻⁵ suggest a correlation.

One meta-analysis⁶ found significant heterogeneity; however, the pooled effect was significant.⁷
```

**Multiple citations**: Use commas or hyphens for ranges
```
Multiple studies¹,³,⁵⁻⁷ have confirmed this.
```

**Same source cited multiple times**: Use the same number throughout

#### Reference List Format

**Journal Articles:**
```
1. Author AA, Author BB, Author CC. Title of article. Journal Name. Year;Volume(Issue):Page range. doi:xx.xxxx
```

**Example:**
```
1. Smith JD, Johnson AB, Williams CD. Effectiveness of cognitive behavioral therapy for anxiety disorders. JAMA Psychiatry. 2023;80(5):456-464. doi:10.1001/jamapsychiatry.2023.0123
```

**Books:**
```
2. Author AA. Book Title. Edition. Publisher; Year.
```

**Book Chapters:**
```
3. Chapter Author AA. Chapter title. In: Editor AA, Editor BB, eds. Book Title. Edition. Publisher; Year:Page range.
```

**Online Resources:**
```
4. Organization Name. Page title. Website name. Published date. Updated date. Accessed date. URL
```

#### Special Cases

**More than 6 authors**: List first 3, then "et al"
```
Smith JD, Jones AB, Williams CD, et al.
```

**No author**: Begin with title

**Advance online publication**:
```
Published online Month Day, Year. doi:xx.xxxx
```

### Vancouver Style

#### Overview
- Developed by the International Committee of Medical Journal Editors (ICMJE)
- Described in *Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals*
- Also called "author-number style"
- Numbered citations in square brackets
- References listed numerically

#### In-Text Citations

**Basic format**: Numbers in square brackets after the relevant text, before periods and commas.

**Examples:**
```
Several studies have shown this effect [1].

The results were inconclusive [2], although Smith et al [3] reported otherwise.

These findings [3-5] suggest a correlation.

Multiple studies [1,3,5-7] have confirmed this.
```

#### Reference List Format

**Journal Articles:**
```
1. Author AA, Author BB, Author CC. Title of article. Journal Name. Year;Volume(Issue):Page range.
```

**Example:**
```
1. Smith JD, Johnson AB, Williams CD. Effectiveness of cognitive behavioral therapy for anxiety disorders. JAMA Psychiatry. 2023;80(5):456-464.
```

**Books:**
```
2. Author AA, Author BB. Book title. Edition. Place of publication: Publisher; Year.
```

**Book Chapters:**
```
3. Chapter Author AA, Chapter Author BB. Chapter title. In: Editor AA, Editor BB, editors. Book title. Edition. Place: Publisher; Year. p. Page range.
```

**Electronic Sources:**
```
4. Author AA. Title of page [Internet]. Place: Publisher; Date of publication [cited Date of citation]. Available from: URL
```

#### Special Cases

**More than 6 authors**: List first 6, then "et al."

**Journal title abbreviations**: Use PubMed/Index Medicus abbreviations
- *The Journal of the American Medical Association* → *JAMA*
- *Nature Medicine* → *Nat Med*

**No volume or issue**: Use year and page numbers only

**Article in press**: Use "[Epub ahead of print]" notation

### APA Style (American Psychological Association)

#### Overview
- Widely used in psychology, education, and social sciences
- Based on the *Publication Manual of the APA* (7th edition, 2020)
- Author-date format for in-text citations
- References listed alphabetically by author surname

#### In-Text Citations

**Basic format**: (Author, Year)

**Examples:**
```
One study found significant effects (Smith, 2023).

Smith (2023) found significant effects.

Multiple studies (Jones, 2020; Smith, 2023; Williams, 2024) support this conclusion.
```

**Two authors**: Use "&" in parentheses, "and" in narrative
```
(Smith & Jones, 2023)
Smith and Jones (2023) demonstrated...
```

**Three or more authors**: Use "et al." after first author
```
(Smith et al., 2023)
Smith et al. (2023) reported...
```

**Multiple works by same author(s) in same year**: Add letters
```
(Smith, 2023a, 2023b)
```

**Direct quotations**: Include page numbers
```
(Smith, 2023, p. 45)
"Quote text" (Smith, 2023, p. 45).
Smith (2023) stated, "Quote text" (p. 45).
```

#### Reference List Format

**Journal Articles:**
```
Author, A. A., Author, B. B., & Author, C. C. (Year). Title of article. Journal Name, Volume(Issue), page range. https://doi.org/xx.xxxx
```

**Example:**
```
Smith, J. D., Johnson, A. B., & Williams, C. D. (2023). Effectiveness of cognitive behavioral therapy for anxiety disorders. JAMA Psychiatry, 80(5), 456-464. https://doi.org/10.1001/jamapsychiatry.2023.0123
```

**Books:**
```
Author, A. A. (Year). Book title: Subtitle (Edition). Publisher. https://doi.org/xx.xxxx
```

**Book Chapters:**
```
Chapter Author, A. A., & Chapter Author, B. B. (Year). Chapter title. In E. E. Editor & F. F. Editor (Eds.), Book title (pp. page range). Publisher.
```

**Websites:**
```
Author, A. A. (Year, Month Day). Page title. Website Name. URL
```

#### Capitalization Rules
- Sentence case for article and book titles (capitalize only first word and proper nouns)
- Title case for journal names (capitalize all major words)

**Example:**
```
Smith, J. D. (2023). Effects of stress on cognitive performance: A meta-analysis. Journal of Experimental Psychology: General, 152(3), 456-478.
```

#### Special Cases

**No author**: Move title to author position
```
Title of work. (Year). Journal Name...
```

**No date**: Use (n.d.)
```
Smith, J. D. (n.d.). Title...
```

**Up to 20 authors**: List all authors with "&" before last
**21 or more authors**: List first 19, then "...", then final author

### Chicago Style

#### Overview
- Based on *The Chicago Manual of Style* (17th edition, 2017)
- Two systems: Notes-Bibliography and Author-Date
- Notes-Bibliography common in humanities
- Author-Date common in sciences

#### Notes-Bibliography System

**In-Text**: Superscript numbers for footnotes or endnotes
```
One study demonstrated this effect.¹
```

**Note format:**
```
1. John D. Smith, Alice B. Johnson, and Carol D. Williams, "Effectiveness of Cognitive Behavioral Therapy for Anxiety Disorders," JAMA Psychiatry 80, no. 5 (2023): 456-64.
```

**Bibliography format:**
```
Smith, John D., Alice B. Johnson, and Carol D. Williams. "Effectiveness of Cognitive Behavioral Therapy for Anxiety Disorders." JAMA Psychiatry 80, no. 5 (2023): 456-64.
```

#### Author-Date System

**In-Text**: Similar to APA
```
(Smith, Johnson, and Williams 2023)
Smith, Johnson, and Williams (2023) found...
```

**Reference list**: Similar to APA but with different punctuation
```
Smith, John D., Alice B. Johnson, and Carol D. Williams. 2023. "Effectiveness of Cognitive Behavioral Therapy for Anxiety Disorders." JAMA Psychiatry 80 (5): 456-64.
```

#### Special Features
- Full names in bibliography (not just initials)
- Uses "and" not "&"
- Different punctuation from APA

### IEEE Style

#### Overview
- Used in engineering, computer science, and technology
- Published by the Institute of Electrical and Electronics Engineers
- Numbered citations in square brackets
- References listed numerically

#### In-Text Citations

**Format**: Numbers in square brackets

**Examples:**
```
Several studies have demonstrated this effect [1].

The algorithm was described by Smith [2] and later improved [3], [4].

Multiple implementations [1]-[4] have been proposed.
```

#### Reference List Format

**Journal Articles:**
```
[1] A. A. Author, B. B. Author, and C. C. Author, "Title of article," Journal Name, vol. X, no. X, pp. XX-XX, Month Year.
```

**Example:**
```
[1] J. D. Smith, A. B. Johnson, and C. D. Williams, "Effectiveness of cognitive behavioral therapy for anxiety disorders," JAMA Psychiatry, vol. 80, no. 5, pp. 456-464, May 2023.
```

**Books:**
```
[2] A. A. Author, Book Title, Edition. City, State: Publisher, Year.
```

**Conference Papers:**
```
[3] A. A. Author, "Paper title," in Proc. Conference Name, City, State, Year, pp. XX-XX.
```

**Online Sources:**
```
[4] A. A. Author. "Title." Website. URL (accessed Mon. Day, Year).
```

#### Special Features
- Abbreviated first and middle names
- Uses "and" before last author (not comma)
- Month abbreviations (Jan., Feb., etc.)
- "vol." and "no." before volume and issue
- "pp." before page range

### Additional Styles

#### ACS Style (American Chemical Society)

**In-Text**: Superscript numbers or numbers in parentheses
```
This reaction has been well studied.¹
This reaction has been well studied (1).
```

**Reference format:**
```
(1) Smith, J. D.; Johnson, A. B.; Williams, C. D. Title of Article. J. Am. Chem. Soc. 2023, 145, 1234-1245.
```

**Features:**
- Semicolons between authors
- Abbreviated journal names
- Year in bold
- No issue numbers

#### NLM Style (National Library of Medicine)

**Very similar to Vancouver**, used by PubMed/MEDLINE

**Key differences:**
- Uses PubMed journal abbreviations
- Specific format for electronic publications
- PMID or PMCID can be included

**Example:**
```
Smith JD, Johnson AB, Williams CD. Effectiveness of cognitive behavioral therapy for anxiety disorders. JAMA Psychiatry. 2023 May;80(5):456-64. doi: 10.1001/jamapsychiatry.2023.0123. PMID: 12345678.
```

### General Citation Best Practices

#### Across All Styles

**When to cite:**
- Direct quotations
- Paraphrased ideas from others
- Statistics, data, or figures from other sources
- Theories, models, or frameworks developed by others
- Information that is not common knowledge

**Citation density:**
- Introduction: Cite liberally to establish context
- Methods: Cite when referencing established protocols or instruments
- Results: Rarely cite (focus on your own findings)
- Discussion: Cite frequently when comparing to prior work

**Source quality:**
- Prefer peer-reviewed journal articles
- Cite original sources when possible (not secondary citations)
- Use recent sources (within 5-10 years for active fields)
- Ensure sources are reputable and relevant

**Common mistakes to avoid:**
- Inconsistent formatting
- Missing required elements (DOI, page numbers, etc.)
- Citing sources not actually read (citation chaining)
- Over-reliance on review articles instead of primary sources
- Including uncited references or missing cited references
- Incorrect author names or initials
- Wrong year of publication
- Truncated titles

#### Managing Citations

**Reference Management Software:**
- **Zotero**: Free, open-source, browser integration
- **Mendeley**: Free, PDF annotation, social features
- **EndNote**: Commercial, powerful, institutional support
- **RefWorks**: Web-based, institutional subscriptions

**Software benefits:**
- Automatic formatting in multiple styles
- In-text citation insertion
- Reference list generation
- PDF organization
- Sharing capabilities

#### Verifying Citations

**Before submission, check:**
1. Every in-text citation has a corresponding reference
2. Every reference is cited in text
3. Formatting is consistent throughout
4. Author names and initials are correct
5. Titles are accurate
6. Journal names match required abbreviations
7. Volume, issue, and page numbers are correct
8. DOIs are included (when required)
9. URLs are functional (for web sources)
10. Citations appear in correct order (numerical styles)

### DOI (Digital Object Identifier)

#### What is a DOI?
A unique alphanumeric string identifying digital content permanently.

**Format:**
```
doi:10.1001/jamapsychiatry.2023.0123
or
https://doi.org/10.1001/jamapsychiatry.2023.0123
```

#### When to include:
- Required by most journals for recent publications
- Preferred over URLs because DOIs don't change
- Look up DOIs at https://www.crossref.org/ if not provided

#### Style-specific formatting:
- **AMA**: `doi:10.xxxx/xxxxx`
- **APA**: `https://doi.org/10.xxxx/xxxxx`
- **Vancouver**: Often omitted or added at journal's discretion
- **Chicago**: `https://doi.org/10.xxxx/xxxxx`

### Quick Reference: Journal Article Format

| Style | Format |
|-------|--------|
| **AMA** | Author AA, Author BB. Title of article. *Journal*. Year;Vol(Iss):pp. doi:xx |
| **Vancouver** | Author AA, Author BB. Title of article. Journal. Year;Vol(Iss):pp. |
| **APA** | Author, A. A., & Author, B. B. (Year). Title of article. *Journal*, Vol(Iss), pp. https://doi.org/xx |
| **Chicago A-D** | Author, A. A., and B. B. Author. Year. "Title." *Journal* Vol (Iss): pp. |
| **IEEE** | A. A. Author and B. B. Author, "Title," *Journal*, vol. X, no. X, pp. XX-XX, Mon. Year. |

### Common Abbreviations

#### Journal Abbreviations
Follow the journal's specified system (usually Index Medicus or ISO):
- *The Journal of Biological Chemistry* → *J Biol Chem*
- *Proceedings of the National Academy of Sciences* → *Proc Natl Acad Sci USA*
- *Nature Medicine* → *Nat Med*

#### Month Abbreviations
- Jan., Feb., Mar., Apr., May, June, July, Aug., Sept., Oct., Nov., Dec.
- Some styles use three-letter abbreviations without periods

#### Edition Abbreviations
- 1st ed., 2nd ed., 3rd ed., etc.
- Or: 1st edition, 2nd edition

### Special Publication Types

#### Preprints
```
APA: Author, A. A. (Year). Title [Preprint]. Repository Name. https://doi.org/xx.xxxx
```

#### Theses and Dissertations
```
APA: Author, A. A. (Year). Title [Doctoral dissertation, University Name]. Repository Name. URL
```

#### Conference Proceedings
```
IEEE: A. A. Author, "Title," in Proc. Conf. Name, City, Year, pp. XX-XX.
```

#### Software/Code
```
APA: Author, A. A. (Year). Title (Version X.X) [Computer software]. Publisher. URL
```

#### Datasets
```
APA: Author, A. A. (Year). Title of dataset (Version X) [Data set]. Repository. https://doi.org/xx.xxxx
```

### Transitioning Between Styles

When converting between citation styles:

1. **Use reference management software** for automatic conversion
2. **Check these elements** that vary by style:
   - In-text citation format (numbered vs. author-date)
   - Author name format (initials vs. full names)
   - Title capitalization (sentence case vs. title case)
   - Journal name formatting (abbreviated vs. full)
   - Punctuation (periods, commas, semicolons)
   - Use of italics and bold
   - Order of elements
3. **Manually verify** after automatic conversion
4. **Check journal guidelines** for specific requirements

### Journal-Specific Citation Styles and Requirements

#### How to Identify a Journal's Citation Style

**Step 1: Check Author Guidelines**
- Every journal provides author instructions (usually "Instructions for Authors" or "Author Guidelines")
- Citation style is typically specified in "References" or "Citations" section
- Look for example references formatted in the journal's style

**Step 2: Review Recent Publications**
- Examine 3-5 recent articles from your target journal
- Note the in-text citation format (numbered vs. author-date)
- Compare reference list formatting
- Check for journal-specific variations

**Step 3: Verify Journal-Specific Variations**
Some journals use modified versions of standard styles:
- Abbreviated vs. full journal names
- DOI inclusion requirements
- Article titles in title case vs. sentence case
- Maximum number of authors before "et al."

#### Common Journals and Their Citation Styles

| Journal | Citation Style | Key Features |
|---------|---------------|--------------|
| **JAMA, JAMA Network journals** | AMA | Superscript numbers, abbreviated journal names, no issue numbers |
| **New England Journal of Medicine** | Modified Vancouver | Numbered brackets, abbreviated journals, limited authors (3 then et al) |
| **The Lancet** | Vancouver | Numbered brackets, PubMed abbreviations |
| **BMJ** | Vancouver | Numbered in-text, DOIs required when available |
| **Nature, Nature journals** | Nature style (numbered) | Numbered superscripts, abbreviated journals, no article titles in some journals |
| **Science** | Science style (numbered) | Numbered in-text, abbreviated format |
| **Cell, Cell Press journals** | Cell style (author-year) | Author-date, specific formatting for multiple citations |
| **PLOS journals** | Vancouver | Numbered brackets, full journal names in some PLOS journals |
| **Journal of Biological Chemistry** | JBC style (numbered) | Numbered in-text, specific abbreviation rules |
| **Psychological journals** | APA | Author-date, DOIs required |
| **IEEE journals** | IEEE | Numbered brackets, specific format for conference papers |
| **ACS journals** | ACS | Superscript or numbered, semicolons between authors |

#### Journal Family Consistency

**Journals from the same publisher often share citation styles:**

**Elsevier journals:**
- Vary widely; check specific journal
- Many use numbered Vancouver-style
- Some allow author-date

**Springer Nature journals:**
- Nature journals: Nature style (numbered, abbreviated)
- Springer journals: Often numbered or author-date depending on field
- BMC journals: Vancouver with full journal names

**Wiley journals:**
- Varies by field
- Many biomedical journals use Vancouver
- Psychology/social science journals often use APA

**American Chemical Society (ACS):**
- All ACS journals use ACS style
- Consistent across Journal of American Chemical Society, Analytical Chemistry, etc.

#### High-Impact Journal and Conference Preferences

| Venue | Field | Citation Preference | Key Features |
|-------|-------|-------------------|--------------|
| **Nature/Science** | Multidisciplinary | Numbered, abbreviated | Space-saving, broad readability |
| **Cell family** | Life sciences | Author-date or numbered | Attribution visibility |
| **NEJM/Lancet/JAMA** | Medicine | Vancouver/AMA numbered | Medical standard |
| **NeurIPS/ICML/ICLR** | Machine Learning | Numbered [1] or (Author, Year) | Varies by conference, check template |
| **CVPR/ICCV/ECCV** | Computer Vision | Numbered [1], IEEE-like | Compact format |
| **ACL/EMNLP** | NLP | Author-year (ACL style) | Attribution-focused |

#### Adapting Citations for Different Target Journals

**When switching journals after desk rejection or withdrawal:**

**Use reference management software:**
1. Import references into Zotero, Mendeley, or EndNote
2. Select target journal's citation style from software library
3. Regenerate citations and reference list automatically
4. Manually verify formatting matches journal examples

**Key elements to check when converting:**
- In-text format (switch numbered ↔ author-date)
- Journal name abbreviation style
- Article title capitalization
- Author name format (initials vs. full names)
- DOI format and inclusion
- Issue number inclusion/exclusion
- Page number format

**Manual verification essential for:**
- Preprints and non-standard sources
- Software/datasets citations
- Conference proceedings
- Dissertations and theses

#### Venue-Specific Evaluation Criteria

**Content expectations:**
- **High-impact journals**: >50% citations from last 5 years; primary sources preferred
- **Medical journals**: Recent clinical evidence; systematic reviews valued
- **ML conferences**: Recent papers (last 2-3 years); preprints (arXiv) acceptable
- **Self-citation**: Keep <20% across all venues

**Format compliance (often automated):**
- Match venue citation style exactly
- All in-text citations have corresponding references
- Include DOIs when required (journals) or arXiv IDs (ML conferences)
- Use correct abbreviations (PubMed for medical, standard for ML)

**ML conference specifics:**
- **NeurIPS/ICML/ICLR**: ArXiv preprints widely cited; recent work heavily valued
- **Page limits strict**: Citation formatting affects space
- **Supplementary material**: Can include extended bibliography
- **Double-blind review**: Avoid obvious self-citation patterns during review

#### Citation Density by Venue Type

| Venue Type | Expected Citations | Key Notes |
|-----------|-------------------|-----------|
| **Nature/Science research** | 30-50 | Selective, high-impact citations |
| **Medical journals (RCT)** | 25-40 | Recent clinical evidence |
| **Field-specific journals** | 30-60 | Comprehensive field coverage |
| **ML conferences (8-page)** | 20-40 | Space-limited, recent work |
| **Review articles** | 100-300+ | Comprehensive coverage |

**ML conference citation practices:**
- **NeurIPS/ICML**: 25-40 references typical for 8-page papers
- **Workshop papers**: 15-25 references
- **ArXiv preprints**: Widely accepted and cited
- **Related work**: Concise but comprehensive; often moved to appendix
- **Recency critical**: Cite work from last 1-2 years when relevant

#### Pre-Submission Citation Checklist

**Content:**
- [ ] ≥50% citations from last 5-10 years (or 2-3 years for ML conferences)
- [ ] <20% self-citations; balanced perspectives
- [ ] Primary sources cited (not citation chains)
- [ ] All claims supported by appropriate citations

**Format:**
- [ ] Style matches venue exactly (check template)
- [ ] All in-text citations in reference list and vice versa
- [ ] DOIs/arXiv IDs included as required
- [ ] Abbreviations match venue style

**ML conferences additional:**
- [ ] ArXiv preprints properly formatted
- [ ] Self-citations anonymized if double-blind review
- [ ] References fit within page limits

### Resources for Citation Styles

#### Official Manuals
- AMA: https://www.amamanualofstyle.com/
- Vancouver/ICMJE: http://www.icmje.org/
- APA: https://apastyle.apa.org/
- Chicago: https://www.chicagomanualofstyle.org/
- IEEE: https://ieeeauthorcenter.ieee.org/

#### Journal-Specific Style Guides
- Nature: https://www.nature.com/nature/for-authors/formatting-guide
- Science: https://www.science.org/content/page/instructions-authors
- Cell: https://www.cell.com/cell/authors
- JAMA: https://jamanetwork.com/journals/jama/pages/instructions-for-authors

#### Quick Reference Guides
- Purdue OWL: https://owl.purdue.edu/
- Citation Machine: https://www.citationmachine.net/
- EasyBib: https://www.easybib.com/

#### Reference Management
- Zotero: https://www.zotero.org/
- Mendeley: https://www.mendeley.com/
- EndNote: https://endnote.com/

#### Journal Citation Style Databases
- Journal Citation Reports (Clarivate): Lists journal citation styles
- EndNote style repository: >7000 journal-specific styles
- Zotero Style Repository: https://www.zotero.org/styles

---

# Reference: references/figures_tables.md

## Figures and Tables Best Practices

### Overview

Figures and tables are essential components of scientific papers, serving to display data patterns, summarize results, and provide evidence for conclusions. Effective visual displays enhance comprehension and can sustain reader interest while illustrating trends, patterns, and relationships not easily conveyed through text alone.

A recent Nature Cell Biology checklist (2025) emphasizes that creating clear and engaging scientific figures is crucial for communicating complex data with clarity, accessibility, and design excellence.

### When to Use Tables vs. Figures

#### Use Tables When:
- Presenting precise numerical values that readers need to reference
- Comparing exact measurements across multiple variables
- Showing detailed statistical outputs
- Data cannot be adequately summarized in 1-2 sentences
- Readers need access to specific data points
- Displaying demographic or baseline characteristics
- Presenting multiple related statistical tests

**Example use cases:**
- Baseline participant characteristics (age, sex, diagnosis, etc.)
- Detailed statistical model outputs (coefficients, p-values, confidence intervals)
- Dose-response data with exact values
- Gene expression levels for specific genes
- Chemical compositions or concentrations

#### Use Figures When:
- Showing trends over time
- Displaying relationships or correlations
- Comparing groups visually
- Illustrating distributions
- Demonstrating patterns not easily seen in numbers
- Showing images (microscopy, radiography, etc.)
- Displaying workflows, diagrams, or schematics

**Example use cases:**
- Growth curves or time series
- Dose-response curves
- Scatter plots showing correlations
- Bar graphs comparing treatment groups
- Histograms showing distributions
- Heatmaps displaying patterns across conditions
- Microscopy images or Western blots

#### General Decision Rule

**Can the information be conveyed in 1-2 sentences of text?**
- Yes → Use text only
- No, and precise values are needed → Use a table
- No, and patterns/trends are most important → Use a figure

### Core Design Principles

#### 1. Self-Explanatory Display Items

**Each figure or table must stand alone without requiring the main text.**

**Essential elements:**
- Complete, descriptive caption
- All abbreviations defined (in caption or footnote)
- Units of measurement clearly indicated
- Sample sizes (n) reported
- Statistical significance annotations explained
- Legend included (for figures with multiple data series)

**Example of self-explanatory caption:**
```
Figure 1. Mean systolic blood pressure (SBP) over 12 weeks in intervention and control groups.
Error bars represent standard error of the mean (SEM). Asterisks indicate significant
differences between groups at each time point (*p < 0.05, **p < 0.01, ***p < 0.001,
two-tailed t-tests). n = 48 per group. BP = blood pressure; SEM = standard error of mean.
```

#### 2. Avoid Redundancy

**Do not duplicate information between text, tables, and figures.**

**Bad practice:**
```
"Mean age was 45.2 years in Group A and 47.8 years in Group B. Mean BMI was 26.3 in
Group A and 28.1 in Group B. Mean systolic blood pressure was 132 mmHg in Group A..."
[Also shown in Table 1]
```

**Good practice:**
```
"Baseline characteristics were similar between groups (Table 1), with no significant
differences in age, BMI, or blood pressure (all p > 0.15)."
[Details in Table 1]
```

**Key principle:** Text should highlight key findings from tables/figures, not repeat all data.

#### 3. Consistency

**Maintain uniform formatting across all display items:**
- Font types and sizes
- Color schemes
- Terminology and abbreviations
- Axis labels and units
- Statistical annotation methods
- Figure styles (all line graphs should look similar)

**Example of inconsistency to avoid:**
- Figure 1 uses "standard error" while Figure 2 uses "SE"
- Figure 1 has blue/red color scheme while Figure 2 uses green/yellow
- Table 1 reports p-values as "p = 0.023" while Table 2 uses "p-value = .023"

#### 4. Optimal Quantity

**Follow the "one display item per 1000 words" guideline.**

**Typical manuscript:**
- 3000-4000 words → 3-4 tables/figures total
- 5000-6000 words → 5-6 tables/figures total

**Quality over quantity:** A few well-designed, information-rich displays are better than many redundant or poorly designed ones.

#### 5. Clarity and Simplicity

**Avoid cluttered or overly complex displays:**
- Don't include too many variables in one figure
- Use clear, readable fonts (minimum 8-10 pt in final size)
- Provide adequate spacing between elements
- Use high contrast (especially for color-blind accessibility)
- Remove unnecessary grid lines, borders, or decoration
- Maximize data-ink ratio (Tufte principle: minimize non-data ink)

### Figure Types and When to Use Them

#### Bar Graphs

**Best for:**
- Comparing discrete categories or groups
- Showing counts or frequencies
- Displaying mean values with error bars

**Design guidelines:**
- Start y-axis at zero (unless showing small differences in large values)
- Order bars logically (by size, alphabetically, or temporally)
- Use error bars (SD, SEM, or CI) consistently
- Include sample sizes
- Avoid 3D effects (they distort perception)

**Common mistakes:**
- Not starting at zero (can exaggerate differences)
- Too many categories (consider table instead)
- Missing error bars

**Example applications:**
- Mean gene expression across tissue types
- Treatment group comparisons
- Frequency of adverse events

#### Line Graphs

**Best for:**
- Showing trends over continuous variables (usually time)
- Displaying multiple groups on same axes
- Illustrating dose-response relationships

**Design guidelines:**
- Use different line styles or colors for groups
- Include data point markers for sparse data
- Show error bars or shaded confidence intervals
- Label axes clearly with units
- Use consistent intervals on x-axis

**Common mistakes:**
- Connecting discrete data points that shouldn't be connected
- Too many lines making graph unreadable
- Inconsistent time intervals without indication

**Example applications:**
- Growth curves
- Time course experiments
- Survival curves (Kaplan-Meier plots)
- Pharmacokinetic profiles

#### Scatter Plots

**Best for:**
- Showing relationships between two continuous variables
- Displaying correlations
- Identifying outliers

**Design guidelines:**
- Include trend line or regression line with equation and R²
- Report correlation coefficient and p-value
- Use semi-transparent points if data overlap
- Consider logarithmic scales for wide ranges
- Mark outliers if relevant

**Common mistakes:**
- Not showing individual data points
- Using scatter plots for categorical data
- Missing correlation statistics

**Example applications:**
- Correlation between biomarkers
- Relationship between dose and response
- Method comparison (Bland-Altman plots)

#### Box Plots (Box-and-Whisker Plots)

**Best for:**
- Showing distributions and spread
- Comparing distributions across groups
- Identifying outliers

**Design guidelines:**
- Clearly define box elements (median, quartiles, whiskers)
- Show or note outliers explicitly
- Consider violin plots for small sample sizes
- Overlay individual data points when n < 20

**Common mistakes:**
- Not defining what whiskers represent
- Using for very small samples without showing raw data
- Not marking outliers

**Example applications:**
- Comparing distributions across treatment groups
- Showing variability in measurements
- Quality control data

#### Heatmaps

**Best for:**
- Displaying matrices of data
- Showing patterns across many conditions
- Representing clustering or grouping

**Design guidelines:**
- Use color scales that are perceptually uniform
- Include color scale bar with units
- Consider hierarchical clustering for rows/columns
- Use appropriate color scheme (diverging vs. sequential)
- Make axes labels readable

**Common mistakes:**
- Poor color choice (rainbow scales are often misleading)
- Too many rows/columns making labels unreadable
- No color scale bar

**Example applications:**
- Gene expression across samples
- Correlation matrices
- Time-series data across multiple variables

#### Images (Microscopy, Gels, Blots)

**Best for:**
- Showing representative examples
- Demonstrating morphology or localization
- Presenting gel electrophoresis or Western blots

**Design guidelines:**
- Include scale bars (not magnification in caption)
- Show representative images with quantification in separate panel
- Label important features with arrows or labels
- Ensure adequate resolution (usually 300+ dpi)
- Show full, unmanipulated images with cropping noted
- Include all relevant controls

**Common mistakes:**
- No scale bar
- Over-processed or manipulated images
- Cherry-picking best images without quantification
- Insufficient resolution

**Example applications:**
- Histological sections
- Immunofluorescence
- Western blots
- Gel electrophoresis

#### Forest Plots

**Best for:**
- Displaying meta-analysis results
- Showing effect sizes with confidence intervals
- Comparing multiple studies or subgroups

**Design guidelines:**
- Include point estimates and CI for each study
- Show overall pooled estimate clearly
- Include line of no effect (typically at 1.0 or 0)
- List study details or weights

**Example applications:**
- Meta-analyses
- Systematic reviews
- Subgroup analyses

#### Flow Diagrams

**Best for:**
- Study participant flow (CONSORT diagrams)
- Systematic review search process (PRISMA diagrams)
- Experimental workflows

**Design guidelines:**
- Follow reporting guideline templates (CONSORT, PRISMA)
- Use consistent shapes and connectors
- Include numbers at each stage
- Clearly show inclusions and exclusions

### Table Design Guidelines

#### Structure

**Basic anatomy:**
1. **Table number and title** (above table)
2. **Column headers** (with units)
3. **Row labels**
4. **Data cells** (with appropriate precision)
5. **Footnotes** (below table for abbreviations, statistics, notes)

#### Formatting Best Practices

**Column headers:**
- Use clear, concise labels
- Include units in parentheses
- Use abbreviations sparingly (define in footnote)

**Data presentation:**
- Align decimal points in columns
- Use consistent decimal places (usually 1-2 for means)
- Report same precision across rows/columns
- Use en-dash (–) for "not applicable"
- Use appropriate precision (don't over-report)

**Statistical annotations:**
- Use superscript letters (ᵃ, ᵇ, ᶜ) or symbols (*, †, ‡) for footnotes
- Define p-value thresholds clearly
- Report exact p-values when possible (p = 0.032, not p < 0.05)

**Footnotes:**
- Define all abbreviations
- Explain statistical tests used
- Note any missing data
- Indicate data source if not original

#### Example Table Format

```
Table 1. Baseline Characteristics of Study Participants

Characteristic          Intervention (n=50)   Control (n=48)    p-value
─────────────────────────────────────────────────────────────────────────
Age, years               45.3 ± 8.2           47.1 ± 9.1        0.28
Male sex, n (%)          28 (56)              25 (52)           0.71
BMI, kg/m²               26.3 ± 3.8           27.1 ± 4.2        0.32
Current smoker, n (%)    12 (24)              15 (31)           0.42
Systolic BP, mmHg        132 ± 15             134 ± 18          0.54
─────────────────────────────────────────────────────────────────────────

Data presented as mean ± SD or n (%). p-values from independent t-tests for
continuous variables and χ² tests for categorical variables. BMI = body mass
index; BP = blood pressure; SD = standard deviation.
```

#### Common Table Mistakes

1. **Excessive complexity** (too many rows/columns)
2. **Insufficient context** (missing units, unclear abbreviations)
3. **Over-precision** (reporting 5 decimal places for p-values)
4. **Missing sample sizes**
5. **No statistical comparisons when appropriate**
6. **Inconsistent formatting** across multiple tables
7. **Duplicate information** with figures or text

### Statistical Presentation in Figures and Tables

#### Reporting Requirements

**For each comparison, report:**
1. **Point estimate** (mean, median, proportion)
2. **Measure of variability** (SD, SEM, CI)
3. **Sample size** (n)
4. **Test statistic** (t, F, χ², etc.)
5. **p-value** (exact when p > 0.001)
6. **Effect size** (when appropriate)

#### Error Bars

**Choose the appropriate measure:**

| Measure | Meaning | When to Use |
|---------|---------|-------------|
| **SD (Standard Deviation)** | Variability in the data | Showing data spread |
| **SEM (Standard Error of Mean)** | Precision of mean estimate | Showing measurement precision |
| **95% CI (Confidence Interval)** | Range likely to contain true mean | Showing statistical significance |

**Key rule:** Always state which measure is shown.

**Example caption:**
```
"Error bars represent 95% confidence intervals."
NOT: "Error bars represent standard error."
```

**Recommendation:** 95% CI preferred because non-overlapping CIs indicate significant differences.

#### Significance Indicators

**Common notation:**
```
* p < 0.05
** p < 0.01
*** p < 0.001
n.s. or NS = not significant
```

**Alternative:** Show exact p-values in table or caption

**Best practice:** Define significance indicators in every figure caption or table footnote.

### Accessibility Considerations

#### Color-Blind Friendly Design

**Recommendations:**
- Use color palettes designed for color-blind accessibility
- Don't rely on color alone (add patterns, shapes, or labels)
- Test figures in grayscale
- Avoid red-green combinations

**Color-blind safe palettes:**
- Blue-Orange
- Purple-Yellow
- Colorbrewer2.org palettes
- Viridis, Plasma, Inferno (for heatmaps)

#### High Contrast

**Ensure readability:**
- Dark text on light background (or vice versa)
- Avoid low-contrast color combinations (gray on gray)
- Use thick enough lines (minimum 0.5-1 pt)
- Large enough text (minimum 8-10 pt after scaling)

#### Screen and Print Compatibility

**Design for both media:**
- Use vector formats when possible (PDF, EPS, SVG)
- Minimum 300 dpi for raster images (TIFF, PNG)
- Test appearance at final print size
- Ensure color figures work in grayscale if printed

### Technical Requirements

#### File Formats

**Vector formats** (preferred for graphs and diagrams):
- **PDF**: Universal, preserves quality
- **EPS**: Encapsulated PostScript, publishing standard
- **SVG**: Scalable vector graphics, web-friendly

**Raster formats** (for photos and images):
- **TIFF**: Uncompressed, high quality, large files
- **PNG**: Lossless compression, good for screen
- **JPEG**: Lossy compression, avoid for data figures

**Avoid:**
- Low-resolution screenshots
- Figures copied from presentations (usually too low resolution)
- Heavily compressed JPEGs (artifacts)

#### Resolution Requirements

**Minimum standards:**
- **Line art** (graphs, diagrams): 300-600 dpi
- **Halftones** (photos, grayscale): 300 dpi
- **Combination** (images with labels): 300-600 dpi

**Best practice:** Create figures at final size and resolution.

#### Dimensions

**Check journal requirements:**
- **Single column**: typically 8-9 cm (3-3.5 inches) wide
- **Double column**: typically 17-18 cm (6.5-7 inches) wide
- **Full page**: varies by journal

**Recommendation:** Design figures to fit single column when possible.

#### Image Manipulation

**Allowed:**
- Brightness/contrast adjustment applied to entire image
- Color balance adjustment
- Cropping (with notation)
- Rotation

**NOT allowed:**
- Selective editing (e.g., enhancing bands in gels)
- Removing background artifacts
- Splicing images without clear indication
- Any manipulation that obscures, eliminates, or misrepresents data

**Ethical requirement:** Report all image adjustments in Methods section.

### Figure and Table Numbering

#### Numbering System

**Figures:**
- Number consecutively in order of first mention in text
- Use Arabic numerals: Figure 1, Figure 2, Figure 3...
- Supplementary figures: Figure S1, Figure S2...

**Tables:**
- Number separately from figures
- Use Arabic numerals: Table 1, Table 2, Table 3...
- Supplementary tables: Table S1, Table S2...

#### In-Text References

**Format:**
```
"Results are shown in Figure 1."
"Participant characteristics are presented in Table 2."
"Multiple analyses confirmed this finding (Figures 3-5)."
```

**NOT:**
```
"Figure 1 below shows..." (avoid "above" or "below" - pagination may change)
"The figure shows..." (always use specific number)
```

### Captions

#### Caption Structure

**For figures:**
```
Figure 1. [One-sentence title]. [Additional description sentences providing context,
defining abbreviations, explaining panels, describing statistical tests, and noting
sample sizes].
```

**For tables:**
```
Table 1. [Descriptive Title]
[Table contents]
[Footnotes defining abbreviations, statistical methods, and providing additional context]
```

#### Caption Content

**Essential information:**
1. What is being shown (brief title)
2. Detailed description of content
3. Definition of all abbreviations and symbols
4. Sample sizes
5. Statistical tests used
6. Meaning of error bars or annotations
7. Panel labels explained (if multiple panels)

**Example comprehensive caption:**
```
Figure 3. Cognitive performance improves with treatment over 12 weeks. (A) Mean Mini-Mental
State Examination (MMSE) scores at baseline, 6 weeks, and 12 weeks for treatment (blue) and
placebo (gray) groups. (B) Individual participant trajectories for treatment group. Error bars
represent 95% confidence intervals. Asterisks indicate significant between-group differences
(*p < 0.05, **p < 0.01, ***p < 0.001; repeated measures ANOVA with Bonferroni correction).
n = 42 treatment, n = 40 placebo. MMSE scores range from 0-30, with higher scores indicating
better cognitive function.
```

### Journal-Specific Requirements

#### Before Creating Figures/Tables

**Check journal guidelines for:**
- Preferred file formats
- Resolution requirements
- Color specifications (RGB vs. CMYK)
- Maximum number of display items
- Dimension requirements
- Font restrictions
- Whether to embed figures in manuscript or submit separately

#### During Submission

**Prepare checklist:**
- [ ] All figures/tables numbered correctly
- [ ] All cited in text in order
- [ ] Captions complete and self-explanatory
- [ ] Abbreviations defined
- [ ] Correct file format and resolution
- [ ] Appropriate size/dimensions
- [ ] High enough quality for print
- [ ] Color-blind friendly (if using color)
- [ ] Permissions obtained (if adapting from others' work)

### Common Pitfalls to Avoid

#### Content Issues
1. **Duplication** between text, tables, and figures
2. **Insufficient context** (unclear what is shown)
3. **Too much information** in one display
4. **Missing key information** (sample sizes, units, statistics)
5. **Cherry-picking** data without showing full picture

#### Design Issues
6. **Poor color choices** (not color-blind friendly)
7. **Inconsistent formatting** across displays
8. **Cluttered or busy designs**
9. **Too small text** at final size
10. **Misleading visualizations** (truncated axes, 3D distortions)

#### Technical Issues
11. **Insufficient resolution** (pixelated when printed)
12. **Wrong file format** (lossy compression, non-vector graphs)
13. **Improper image manipulation** (undeclared editing)
14. **Missing scale bars** on images
15. **Figures that don't work in grayscale** (if journal prints in B&W)

### Tools for Creating Figures

#### Graphing Software
- **R (ggplot2)**: Highly customizable, publication-quality, reproducible
- **Python (matplotlib, seaborn)**: Flexible, programmable, widely used
- **GraphPad Prism**: User-friendly, statistics integrated, common in life sciences
- **Origin**: Advanced graphing, popular in physics/engineering
- **Excel**: Basic graphs, widely available, limited customization
- **MATLAB**: Technical computing, good for complex visualizations

#### Image Processing
- **ImageJ/Fiji**: Free, powerful, widely used in microscopy
- **Adobe Photoshop**: Professional standard, extensive tools
- **GIMP**: Free alternative to Photoshop
- **Adobe Illustrator**: Vector graphics, figure assembly
- **Inkscape**: Free vector graphics editor

#### Best Practices for Software Choice
- Use tools that produce vector output for graphs
- Learn one tool well rather than many superficially
- Script your figure generation for reproducibility
- Save original data files separately from figure files

### Journal-Specific Figure and Table Requirements

#### Understanding Journal Expectations

**Different journals have vastly different requirements for figures and tables.** Before creating display items, always consult your target journal's author guidelines for specific requirements.

#### Common Journal-Specific Variations

| Aspect | Variation by Journal | Example Journals |
|--------|---------------------|------------------|
| **Number allowed** | 4-10 display items for research articles | Nature (4-6), PLOS ONE (unlimited), Science (4-5) |
| **File format** | TIFF, EPS, PDF, AI, or specific formats | Nature (EPS/PDF for line art), Cell (TIFF preferred) |
| **Resolution** | 300-1000 dpi depending on type | JAMA (300-600 dpi), Nature (300+ dpi) |
| **Color** | RGB vs. CMYK | Print journals: CMYK; Online: RGB |
| **Dimensions** | Single vs. double column widths | Nature (89mm or 183mm), Science (specific templates) |
| **Figure legends** | Length limits, specific format | Some journals: 150 word max per legend |
| **Table format** | Editable vs. image | Most prefer editable tables, not images |

#### Venue-Specific Requirements Summary

| Venue Type | Display Limit | Format | Resolution | Key Features |
|-----------|--------------|--------|------------|--------------|
| **Nature/Science** | 4-6 main | EPS/PDF/TIFF | 300+ dpi | Extended data allowed; multi-panel figures |
| **Medical journals** | 3-5 | TIFF/EPS | 300-600 dpi | CONSORT diagrams; conservative design |
| **PLOS ONE** | Unlimited | TIFF/EPS/PDF | 300+ dpi | Must work in grayscale |
| **ML conferences** | 4-6 in 8-page limit | PDF (vector preferred) | Print quality | Compact design; info-dense figures |

**ML Conference Figure Requirements:**

**NeurIPS/ICML/ICLR:**
- Figures count toward page limit (typically 8 pages including references)
- Vector graphics (PDF) preferred for plots
- High information density expected
- Supplementary material for additional figures
- LaTeX template provided (use neurips_2024.sty or equivalent)
- Figures must be legible when printed in grayscale

**Computer Vision (CVPR/ICCV/ECCV):**
- Qualitative results figures critical
- Side-by-side comparisons standard
- Must show failure cases
- Supplementary material for videos/additional examples
- Often 6-8 main figures in 8-page papers

**Key ML conference figure practices:**
- **Ablation studies**: Compact tables/plots showing component contributions
- **Architecture diagrams**: Clear, professional block diagrams
- **Performance plots**: Include error bars/confidence intervals
- **Qualitative examples**: Show diverse, representative samples
- **Comparison tables**: Concise, bold best results

#### Evaluation Criteria Across Venues

**What reviewers check:**
- **Necessity**: Each figure/table supports conclusions
- **Quality**: Professional appearance, sufficient resolution
- **Clarity**: Self-explanatory with captions; proper labeling
- **Statistics**: Error bars, sample sizes, significance indicators
- **Consistency**: Formatting uniform across display items

**Common rejection reasons:**
- Poor resolution or image quality
- Missing error bars or sample sizes
- Unclear or missing labels
- Too many figures (exceeds venue limits)
- Figures duplicate text information

**ML conference specific evaluation:**
- **Ablation studies**: Must demonstrate component contributions
- **Baselines**: Comparison with relevant prior work required
- **Error bars**: Confidence intervals/std dev expected
- **Architecture diagrams**: Must be clear and informative
- **Space efficiency**: Information density valued (page limits strict)

#### Caption/Legend Styles by Venue

| Venue Type | Style | Example Features |
|-----------|-------|------------------|
| **Nature/Science** | Concise | Brief; *P<0.05; minimal methods |
| **Medical** | Formal | Title case; 95% CIs; statistical tests spelled out |
| **PLOS/BMC** | Detailed | Complete sentences; all abbreviations defined |
| **ML conferences** | Technical | Architecture details; hyperparameters; dataset info |

**ML conference caption example:**
```
Figure 1. Architecture of proposed model. (a) Encoder with 12 transformer layers.
(b) Attention visualization. (c) Performance vs. baseline on ImageNet (error bars:
95% CI over 3 runs).
```
- Technical precision
- Hyperparameters when relevant
- Dataset/experimental setup details
- Compact to save space

#### Quick Adaptation Guide

**When changing venues:**
- **Journal → ML conference**: Compress figures; increase information density; add hyperparameters to captions
- **ML conference → journal**: Expand captions; separate dense figures; add more methodological detail
- **Specialist → broad journal**: Simplify; add explanatory panels; define terms in captions
- **Broad → specialist journal**: Add technical detail; use field-standard plot types

#### Pre-Submission Figure/Table Checklist

**Technical (all venues):**
- [ ] Meets format requirements (PDF/EPS/TIFF)
- [ ] Sufficient resolution (300+ dpi) 
- [ ] Fits venue dimensions/page limits
- [ ] Self-explanatory captions
- [ ] All symbols/abbreviations defined
- [ ] Error bars defined; sample sizes noted

**ML conferences additional:**
- [ ] Figures fit in page limit (8-9 pages typical)
- [ ] Comparison with baselines shown
- [ ] Ablation studies included
- [ ] Architecture diagram clear
- [ ] Legible in grayscale

### Checklist for Final Review

#### Before Submission

**For every figure:**
- [ ] High enough resolution (300+ dpi)?
- [ ] Correct file format per journal requirements?
- [ ] Correct dimensions for journal (single/double column)?
- [ ] Meets journal's RGB/CMYK requirements?
- [ ] Self-explanatory caption with all abbreviations defined?
- [ ] Caption length within journal limits?
- [ ] All symbols/colors explained in caption or legend?
- [ ] Error bars included and defined?
- [ ] Sample sizes noted?
- [ ] Statistical tests described?
- [ ] Axes labeled with units?
- [ ] Readable text at final print size?
- [ ] Works in grayscale or color-blind friendly?
- [ ] Referenced in text in correct order?
- [ ] Style matches target journal's published figures?

**For every table:**
- [ ] Clear, descriptive title?
- [ ] Title capitalization matches journal style?
- [ ] Column headers include units?
- [ ] Appropriate numerical precision?
- [ ] Abbreviations defined in footnotes?
- [ ] Statistical methods explained?
- [ ] Sample sizes included?
- [ ] Consistent formatting with other tables?
- [ ] Editable format (not image)?
- [ ] Referenced in text in correct order?
- [ ] Formatting matches target journal's tables?

**Overall:**
- [ ] Number of display items within journal limits?
- [ ] Appropriate number of display items (~1 per 1000 words)?
- [ ] No duplication between text, figures, and tables?
- [ ] Consistent formatting across all display items?
- [ ] All display items necessary (each tells important part of story)?
- [ ] Visual style matches target journal?
- [ ] Quality comparable to published examples in journal?

---

# Reference: references/reporting_guidelines.md

## Reporting Guidelines for Scientific Studies

### Overview

Reporting guidelines are evidence-based recommendations for what information should be included when reporting specific types of research studies. They provide checklists and flow diagrams to ensure complete, accurate, and transparent reporting, which is essential for readers to assess study validity and for other researchers to replicate the work.

The EQUATOR Network (Enhancing the QUAlity and Transparency Of health Research) maintains a comprehensive library of reporting guidelines. Using appropriate reporting guidelines improves manuscript quality and increases the likelihood of publication acceptance.

### Why Use Reporting Guidelines?

#### Benefits

**For authors:**
- Ensures nothing important is forgotten
- Increases acceptance rates
- Improves manuscript organization
- Reduces reviewer requests for additional information

**For readers and reviewers:**
- Enables critical appraisal of study validity
- Facilitates systematic reviews and meta-analyses
- Improves understanding of what was actually done

**For science:**
- Enhances reproducibility
- Reduces research waste
- Improves transparency
- Enables better evidence synthesis

#### When to Use

- **During study design**: Many guidelines include protocol versions (e.g., SPIRIT for trial protocols)
- **During manuscript drafting**: Use checklist to ensure all items are covered
- **Before submission**: Verify adherence and often submit checklist with manuscript
- **Many journals require**: Reporting guideline checklists as part of submission

### Major Reporting Guidelines by Study Type

#### CONSORT - Randomized Controlled Trials

**Full name:** Consolidated Standards of Reporting Trials

**When to use:** Any randomized controlled trial (RCT), including pilot and feasibility trials

**Latest version:** CONSORT 2025 (Hopewell et al., published April 2025 in several journals, e.g. *PLoS Medicine* 22(4):e1004587, doi:10.1371/journal.pmed.1004587). It replaces CONSORT 2010.

**Key components:**
- **Checklist**: 30 essential items. Compared with CONSORT 2010 it adds 7 items, revises 3 and deletes 1, and adds a new open science section.
- **Flow diagram**: Participant flow through enrollment, allocation, follow-up, and analysis

**New or expanded in CONSORT 2025:**
- Open science section: trial registration; where the protocol and statistical analysis plan can be accessed; data sharing; funding and conflicts of interest
- Patient and public involvement in design, conduct and reporting
- Criteria for selecting trial sites and the people delivering the interventions
- How harms were defined and assessed
- Analysis population and how missing data were handled
- Intervention delivery, adherence and concomitant care

**Core items carried over from CONSORT 2010 (abridged; use the official 30-item checklist when reporting):**
1. Title identifies study as randomized trial
2. Structured abstract
3. Scientific background and rationale
4. Specific objectives and hypotheses
5. Trial design description (parallel, crossover, factorial, etc.)
6. Eligibility criteria for participants
7. Settings and locations of data collection
8. Interventions described in sufficient detail for replication
9. Primary and secondary outcomes defined
10. Sample size determination and power calculation
11. Randomization sequence generation
12. Allocation concealment mechanism
13. Blinding implementation
14. Statistical methods
15. Participant flow with reasons for dropouts
16. Recruitment dates and follow-up dates
17. Baseline characteristics table
18. Analysis results for each outcome
19. Harms and adverse events
20. Trial limitations
21. Generalizability
22. Interpretation consistent with results
23. Trial registration number
24. Full protocol access
25. Funding sources

**Extensions for specific designs:**
- CONSORT for cluster randomized trials
- CONSORT for non-inferiority and equivalence trials
- CONSORT for pragmatic trials
- CONSORT for crossover trials
- CONSORT for N-of-1 trials
- CONSORT for stepped wedge designs

**Where to access:** http://www.consort-statement.org/

#### STROBE - Observational Studies

**Full name:** Strengthening the Reporting of Observational Studies in Epidemiology

**When to use:** Cohort studies, case-control studies, and cross-sectional studies

**Latest version:** STROBE 2007 (widely adopted standard)

**Key study designs covered:**
- **Cohort**: Follow exposed and unexposed groups forward in time
- **Case-control**: Compare exposure history between cases and controls
- **Cross-sectional**: Measure exposure and outcome simultaneously

**Main checklist items (22 items):**
1. Title and abstract indicate study design
2. Background and rationale
3. Objectives
4. Study design with rationale
5. Setting, locations, and dates
6. Eligibility criteria and selection methods
7. Variables clearly defined (outcomes, exposures, confounders)
8. Data sources and measurement methods
9. Bias management strategies
10. Study size justification
11. Handling of quantitative variables
12. Statistical methods including confounding and interactions
13. Sensitivity analyses
14. Participant flow with reasons for non-participation
15. Descriptive data including follow-up time
16. Outcome data
17. Main results with unadjusted and adjusted estimates
18. Other analyses (subgroups, sensitivity analyses)
19. Key results summary
20. Limitations with potential bias discussion
21. Interpretation and generalizability
22. Funding sources and role

**Extensions:**
- STROBE-ME (Molecular Epidemiology)
- RECORD (Routinely collected health data)
- STROBE-RDS (Respondent-driven sampling)

**Where to access:** https://www.strobe-statement.org/

#### PRISMA - Systematic Reviews and Meta-Analyses

**Full name:** Preferred Reporting Items for Systematic Reviews and Meta-Analyses

**When to use:** Systematic reviews with or without meta-analysis

**Latest version:** PRISMA 2020 (significant update)

**Key components:**
- **Checklist**: 27 items covering all sections
- **Flow diagram**: Study selection process

**Main sections:**
1. **Title**: Identify as systematic review/meta-analysis
2. **Abstract**: Structured summary
3. **Introduction**: Rationale and objectives
4. **Methods**:
   - Eligibility criteria
   - Information sources (databases, dates)
   - Search strategy (full strategy for at least one database)
   - Selection process
   - Data collection process
   - Data items extracted
   - Risk of bias assessment
   - Effect measures
   - Synthesis methods
   - Reporting bias assessment
   - Certainty assessment (e.g., GRADE)
5. **Results**:
   - Study selection flow diagram
   - Study characteristics
   - Risk of bias assessment results
   - Synthesis results (meta-analysis if applicable)
   - Reporting biases
   - Certainty of evidence
6. **Discussion**:
   - Limitations
   - Interpretation
   - Implications

**Extensions:**
- PRISMA for Abstracts
- PRISMA for Protocols (PRISMA-P)
- PRISMA for Network Meta-Analyses
- PRISMA for Scoping Reviews (PRISMA-ScR)
- PRISMA for Individual Patient Data
- PRISMA for Diagnostic Test Accuracy
- PRISMA for Equity-focused reviews

**Where to access:** http://www.prisma-statement.org/

#### SPIRIT - Study Protocols for Clinical Trials

**Full name:** Standard Protocol Items: Recommendations for Interventional Trials

**When to use:** Protocols for randomized trials and other planned intervention studies

**Latest version:** SPIRIT 2025 (Chan, Hopewell et al., published April 2025 alongside CONSORT 2025). It replaces SPIRIT 2013.

**Purpose:** Ensure trial protocols contain complete descriptions before trial begins

**Checklist:** 34 minimum items. Compared with SPIRIT 2013 it adds 2 items, revises 5 and deletes or merges 5, and adds an open science section aligned with CONSORT 2025.

**Main content areas (abridged; use the official SPIRIT 2025 checklist):**
- Administrative information (title, trial registration, funding)
- Introduction (background, rationale, objectives)
- Methods: Trial design
  - Study setting
  - Eligibility criteria
  - Interventions in detail
  - Outcomes (primary and secondary)
  - Participant timeline
  - Sample size calculation
  - Recruitment strategy
  - Allocation and randomization
  - Blinding
  - Data collection methods
  - Data management
  - Statistical methods
  - Monitoring (data monitoring committee)
  - Harms reporting
  - Auditing
- Ethics and dissemination
  - Ethics approval
  - Consent procedures
  - Confidentiality
  - Dissemination plans

**Where to access:** https://www.spirit-statement.org/

#### STARD - Diagnostic Accuracy Studies

**Full name:** Standards for Reporting of Diagnostic Accuracy Studies

**When to use:** Studies evaluating diagnostic test accuracy

**Latest version:** STARD 2015

**Main checklist items (30 items):**
1. Study design identification
2. Background information and objectives
3. Study design description
4. Participant selection criteria and recruitment
5. Data collection methods
6. Index test description and execution
7. Reference standard description
8. Rationale for choosing reference standard
9. Test result definition and cutoffs
10. Flow of participants with timing
11. Baseline demographic and clinical characteristics
12. Cross-tabulation of index test results by reference standard
13. Estimates of diagnostic accuracy with confidence intervals
14. Handling of indeterminate results
15. Adverse events from testing

**Flow diagram:** Shows participant flow and test results

**Where to access:** https://www.equator-network.org/reporting-guidelines/stard/

#### TRIPOD - Prediction Model Studies

**Full name:** Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis

**When to use:** Studies developing, validating, or updating prediction models

**Latest version:** TRIPOD+AI (Collins et al., *BMJ* 2024;385:e078378). It covers models built with regression or machine learning and supersedes TRIPOD 2015, which should no longer be used. The checklist has 27 items (52 subitems). Related: TRIPOD-LLM for studies that use large language models.

**Types of studies:**
- Model development only
- Model development with validation
- External validation of existing model
- Model update

**Core items (abridged from TRIPOD 2015; use the official TRIPOD+AI checklist, which adds fairness items throughout, an open science section (protocol, registration, data and code sharing) and an item on patient and public involvement):**
1. Title identifies study as prediction model study
2. Abstract summarizes key elements
3. Background and objectives
4. Data source and participants
5. Outcome definition
6. Predictors (candidate and selected)
7. Sample size justification
8. Missing data handling
9. Model building procedure
10. Model specification (equation or algorithm)
11. Model performance measures
12. Risk groups if used
13. Participant flow diagram
14. Model development results
15. Model performance
16. Model updating if applicable

**Where to access:** https://www.tripod-statement.org/

#### ARRIVE - Animal Research

**Full name:** Animal Research: Reporting of In Vivo Experiments

**When to use:** All in vivo animal studies

**Latest version:** ARRIVE 2.0 (2020 update)

**Two sets of items:**

**ARRIVE Essential 10** (minimum requirements):
1. Study design
2. Sample size calculation
3. Inclusion and exclusion criteria
4. Randomization
5. Blinding
6. Outcome measures
7. Statistical methods
8. Experimental animals (species, strain, sex, age)
9. Experimental procedures
10. Results and interpretation

**ARRIVE Recommended Set** (additional items for full reporting):
- Abstract, background, objectives
- Ethics statement
- Housing and husbandry
- Animal care and monitoring
- Interpretation and generalizability
- Protocol registration
- Data access

**Where to access:** https://arriveguidelines.org/

#### CARE - Case Reports

**Full name:** CAse REport Guidelines

**When to use:** Case reports and case series

**Latest version:** CARE 2013

**Main checklist items (13 items):**
1. Title with "case report"
2. Abstract summarizing case
3. Introduction with case background
4. Patient information (demographics, primary concern)
5. Clinical findings
6. Timeline of events
7. Diagnostic assessment
8. Therapeutic intervention
9. Follow-up and outcomes
10. Discussion with strengths and limitations
11. Patient perspective
12. Informed consent

**Where to access:** https://www.care-statement.org/

#### SQUIRE - Quality Improvement Studies

**Full name:** Standards for QUality Improvement Reporting Excellence

**When to use:** Healthcare quality improvement reports

**Latest version:** SQUIRE 2.0 (2015)

**Main sections (18 items):**
1. Title and abstract
2. Introduction (problem description, available knowledge, rationale, objectives)
3. Methods (context, intervention, study design, measures, analysis, ethical review)
4. Results (intervention, outcomes)
5. Discussion (summary, interpretation, limitations, conclusions)
6. Other information (funding)

**Where to access:** http://www.squire-statement.org/

#### CHEERS - Economic Evaluations

**Full name:** Consolidated Health Economic Evaluation Reporting Standards

**When to use:** Health economic evaluations

**Latest version:** CHEERS 2022 (major update from 2013)

**Main checklist items (28 items):**
1. Title identification as economic evaluation
2. Abstract
3. Background and objectives
4. Target population and subgroups
5. Setting and location
6. Study perspective
7. Comparators
8. Time horizon
9. Discount rate
10. Selection of outcomes
11. Measurement of effectiveness
12. Measurement and valuation of costs
13. Currency and price adjustments
14. Choice of model
15. Assumptions
16. Analytical methods

**Where to access:** https://www.equator-network.org/reporting-guidelines/cheers/

#### SRQR - Qualitative Research

**Full name:** Standards for Reporting Qualitative Research

**When to use:** Qualitative and mixed methods research

**Latest version:** SRQR 2014

**Main sections:**
- Title and abstract
- Introduction (problem formulation, purpose)
- Methods (qualitative approach, researcher characteristics, context, sampling strategy, ethical issues, data collection, data analysis, trustworthiness)
- Results (synthesis and interpretation, links to empirical data)
- Discussion (limitations, implications)

**Alternative:** COREQ (Consolidated criteria for reporting qualitative research) for interviews and focus groups

**Where to access:** https://www.equator-network.org/reporting-guidelines/srqr/

### How to Use Reporting Guidelines

#### During Study Planning

1. **Identify relevant guideline** based on study design
2. **Review checklist items** that require planning (e.g., randomization, blinding)
3. **Design study** to ensure all required elements will be captured
4. **Consider protocol guidelines** (e.g., SPIRIT for trials)

#### During Manuscript Drafting

1. **Download checklist** from guideline website
2. **Work through each item** systematically
3. **Note where each item is addressed** in manuscript (page/line numbers)
4. **Revise manuscript** to include missing items
5. **Use flow diagrams** as appropriate

#### Before Submission

1. **Complete formal checklist** with page numbers
2. **Review all items** are adequately addressed
3. **Include checklist** with submission if journal requires
4. **Note guideline adherence** in cover letter or methods

#### Example Checklist Entry

```
Item 7: Eligibility criteria for participants, and the settings and locations where the data were collected
Page 6, lines 112-125: "Participants were community-dwelling adults aged 60-85 years with mild cognitive impairment (MCI) as defined by Petersen criteria. Exclusion criteria included dementia diagnosis, major psychiatric disorders, or unstable medical conditions. Recruitment occurred from three memory clinics in Boston, MA, between January 2022 and December 2023."
```

### Finding the Right Guideline

#### EQUATOR Network Search

**Website:** https://www.equator-network.org/

**How to use:**
1. Select your study design from the wizard
2. Browse by health research category
3. Search for specific keywords
4. Filter by guideline status (development stage)

#### By Study Design

| If your study is a... | Use this guideline |
|----------------------|-------------------|
| Randomized controlled trial | CONSORT |
| Cohort, case-control, or cross-sectional study | STROBE |
| Systematic review or meta-analysis | PRISMA |
| Protocol for a trial | SPIRIT |
| Diagnostic accuracy study | STARD |
| Prediction model study | TRIPOD |
| Animal study | ARRIVE |
| Case report | CARE |
| Quality improvement study | SQUIRE |
| Economic evaluation | CHEERS |
| Qualitative research | SRQR or COREQ |

#### Multiple Guidelines

**Some studies may require multiple guidelines:**

**Example 1:** Pilot RCT with qualitative component
- CONSORT for quantitative arm
- SRQR for qualitative component

**Example 2:** Systematic review of diagnostic tests
- PRISMA for review methods
- STARD considerations for included studies

### Extensions and Adaptations

Many reporting guidelines have extensions for specific contexts:

#### CONSORT Extensions (examples)

- **CONSORT for Abstracts**: Structured abstracts for RCT reports
- **CONSORT for Harms**: Reporting adverse events
- **CONSORT-EHEALTH**: eHealth interventions
- **CONSORT-SPI**: Social and psychological interventions

#### PRISMA Extensions (examples)

- **PRISMA-P**: Protocols for systematic reviews
- **PRISMA for Abstracts**: Conference abstracts
- **PRISMA-NMA**: Network meta-analyses
- **PRISMA-IPD**: Individual patient data reviews
- **PRISMA-S**: Search strategies
- **PRISMA-DTA**: Diagnostic test accuracy reviews

#### STROBE Extensions (examples)

- **STROBE-ME**: Molecular epidemiology
- **RECORD**: Routinely collected health data

### Creating Flow Diagrams

#### CONSORT Flow Diagram

**Four stages:**
1. **Enrollment**: Assessed for eligibility
2. **Allocation**: Randomly assigned to groups
3. **Follow-up**: Received intervention, lost to follow-up
4. **Analysis**: Included in analysis

**Example:**
```
Assessed for eligibility (n=250)
    ↓
Excluded (n=50)
  • Did not meet criteria (n=30)
  • Declined to participate (n=15)
  • Other reasons (n=5)
    ↓
Randomized (n=200)
    ├─────────────────┬─────────────────┐
    ↓                 ↓                 ↓
Allocated to       Allocated to      Allocated to
Intervention A     Intervention B     Control
(n=67)            (n=66)            (n=67)
    ↓                 ↓                 ↓
Lost to follow-up  Lost to follow-up  Lost to follow-up
(n=3)             (n=5)             (n=2)
    ↓                 ↓                 ↓
Analyzed          Analyzed          Analyzed
(n=64)            (n=61)            (n=65)
```

#### PRISMA Flow Diagram

**Stages:**
1. **Identification**: Records from databases and registers
2. **Screening**: Records screened, excluded
3. **Included**: Studies included in review and synthesis

**New features in PRISMA 2020:**
- Separate tracking for database and register searches
- Tracking of duplicate removal
- Clear distinction between reports and studies

### Common Mistakes and How to Avoid Them

#### Mistake 1: Not Using Guidelines at All

**Impact:** Missing critical information, lower chance of acceptance

**Solution:** Identify and use appropriate guideline from study planning stage

#### Mistake 2: Using Guidelines Only After Manuscript is Complete

**Impact:** May realize key data were not collected or documented

**Solution:** Review guidelines during study design and data collection

#### Mistake 3: Incomplete Checklist Completion

**Impact:** Missed items remain unreported

**Solution:** Systematically address every single checklist item

#### Mistake 4: Using Outdated Guidelines

**Impact:** Missing recent improvements in reporting standards

**Solution:** Always check for latest version on official guideline website

#### Mistake 5: Using Wrong Guideline for Study Design

**Impact:** Important design-specific elements not reported

**Solution:** Carefully match study design to appropriate guideline

#### Mistake 6: Not Submitting Checklist When Required

**Impact:** Editorial desk rejection or delays

**Solution:** Check journal submission guidelines and include checklist

#### Mistake 7: Generic Reporting Without Specificity

**Impact:** Insufficient detail for replication or appraisal

**Solution:** Provide specific, detailed information for each item

### Journal Requirements

#### Many Journals Now Require:

1. **Statement of adherence** to reporting guidelines in Methods
2. **Completed checklist** uploaded as supplementary file
3. **Page/line numbers** on checklist indicating where items are addressed
4. **Flow diagrams** as figures in manuscript

#### Example Methods Statement:

```
"This study is reported in accordance with the Strengthening the Reporting of
Observational Studies in Epidemiology (STROBE) statement. A completed STROBE
checklist is provided as Supplementary File 1."
```

#### Journals with Strong Requirements:

- PLOS journals (require checklists for specific designs)
- BMJ (requires CONSORT, PRISMA, and others)
- The Lancet (requires adherence statements)
- JAMA and JAMA Network journals (require checklists)
- Nature portfolio journals (encourage guidelines)

### Resources

#### Official Guideline Websites

- **EQUATOR Network**: https://www.equator-network.org/
- **CONSORT**: http://www.consort-statement.org/
- **STROBE**: https://www.strobe-statement.org/
- **PRISMA**: http://www.prisma-statement.org/
- **SPIRIT**: https://www.spirit-statement.org/
- **ARRIVE**: https://arriveguidelines.org/
- **CARE**: https://www.care-statement.org/

#### Training Materials

- EQUATOR Network provides webinars and training resources
- Many guidelines have explanatory papers published in medical journals
- Universities often provide workshops on reporting guidelines

#### Software Tools

- **Some reference managers** can insert reporting guideline citations
- **Covidence, RevMan** for systematic review reporting
- **PRISMA flow diagram generator**: http://prisma.thetacollaborative.ca/

### Checklist: Using Reporting Guidelines

**Before starting your study:**
- [ ] Identified appropriate reporting guideline(s)
- [ ] Reviewed checklist items requiring prospective planning
- [ ] Designed study to capture all required elements
- [ ] Registered protocol if applicable

**During manuscript drafting:**
- [ ] Downloaded latest version of guideline checklist
- [ ] Systematically addressed each checklist item
- [ ] Created required flow diagram
- [ ] Noted where each item is addressed (page/line)

**Before submission:**
- [ ] Completed formal checklist with page numbers
- [ ] Verified all items adequately addressed
- [ ] Included adherence statement in Methods
- [ ] Prepared checklist as supplementary file if required
- [ ] Checked journal-specific requirements
- [ ] Mentioned guideline adherence in cover letter

### Venue-Specific Reporting Requirements

#### Reporting Standards by Venue Type

| Venue Type | Guideline Use | Transparency Requirements |
|-----------|--------------|---------------------------|
| **Medical journals** | Mandatory (CONSORT, STROBE, etc.) | Checklist required at submission |
| **PLOS/BMC** | Mandatory for study types | Checklist uploaded as supplement |
| **Nature/Science** | Recommended | Methods completeness emphasized |
| **ML conferences** | No formal guidelines | Reproducibility details required |

#### ML Conference Reporting Standards

**NeurIPS/ICML/ICLR reproducibility requirements:**
- **Datasets**: Names, versions, access methods, preprocessing
- **Code**: Availability statement; GitHub common
- **Hyperparameters**: All settings reported (learning rate, batch size, etc.)
- **Seeds**: Random seeds for reproducibility
- **Computational resources**: GPUs used, training time
- **Statistical significance**: Error bars, confidence intervals, multiple runs
- **Broader Impact** statement (NeurIPS): Societal implications

**What to include (typically in appendix):**
- Complete hyperparameter settings
- Training details and convergence criteria
- Hardware specifications
- Software versions (PyTorch 2.0, etc.)
- Dataset splits and any preprocessing
- Evaluation metrics and protocols

#### Enforcement and Evaluation

**What gets checked:**
- **Medical journals**: Checklist uploaded; adherence statement in Methods; systematic completeness
- **PLOS/BMC**: Mandatory checklists for certain designs; reproducibility emphasized
- **High-impact**: Methods sufficiency for replication (checklist often not required)
- **ML conferences**: Reproducibility checklist (NeurIPS); code availability increasingly expected

**Common issues leading to rejection:**
- Missing required checklists (medical journals)
- Insufficient methods detail for reproduction
- Missing key information (randomization, blinding, power calculation)
- No data/code availability statement when required

**Methods statement examples:**

**Journal (STROBE):**
```
This study followed STROBE reporting guidelines. Checklist provided in Supplement 1.
```

**ML conference (reproducibility):**
```
Code available at github.com/user/project. All hyperparameters in Appendix A.
Training used 4×A100 GPUs (~20 hours). Seeds: {42, 123, 456}.
```

#### Pre-Submission Reporting Checklist

**For clinical trials (medical journals):**
- [ ] CONSORT checklist complete with page numbers
- [ ] Trial registration number in abstract and methods
- [ ] CONSORT flow diagram included
- [ ] Statistical analysis plan described
- [ ] Adherence statement in Methods

**For observational studies (medical/epidemiology):**
- [ ] STROBE checklist complete
- [ ] Study design clearly stated
- [ ] Statistical methods detailed
- [ ] Confounders addressed
- [ ] Adherence statement in Methods

**For systematic reviews:**
- [ ] PRISMA checklist complete
- [ ] PRISMA flow diagram included
- [ ] Protocol registered (PROSPERO)
- [ ] Search strategy documented
- [ ] Risk of bias assessment included

**For ML conference papers:**
- [ ] All datasets named with versions
- [ ] Code availability stated (GitHub link if available)
- [ ] Hyperparameters listed (appendix acceptable)
- [ ] Random seeds reported
- [ ] Computational resources specified
- [ ] Error bars/confidence intervals shown
- [ ] Broader Impact statement (if required)

---

# Reference: references/mn/butets.md

## Өгүүллийн бүтэц: IMRaD ба монгол сэтгүүлийн загвар

Эх сурвалж: K-Dense «IMRAD Structure Guide» (references/imrad_structure.md)-ийн монгол буулгалт; МУБИС-ийн «Лавай» эрдэм шинжилгээний бичгийн зөвлөмж; Монголын эдийн засгийн тойм (MJER) сэтгүүлийн зохиогчид өгөх заавар.

### Хоёр загвар

IMRaD (Introduction, Methods, Results, and Discussion: удиртгал, арга зүй, үр дүн, хэлэлцүүлэг) бол анхдагч судалгааны өгүүллийн олон улсын үндсэн бүтэц. Шинжлэх ухааны аргатай давхцдаг тул бичих, унших, үнэлэхэд хялбар:

- Удиртгал: ямар асуулт тавьсан бэ?
- Арга зүй: хэрхэн судалсан бэ?
- Үр дүн: юу олсон бэ?
- Хэлэлцүүлэг: энэ юуг илэрхийлж байна вэ?

Монгол сэтгүүлүүд IMRaD-ыг өөрийн нэрлэлт, нэмэлт хэсэгтэй хэрэглэдэг. «Лавай»-н бүтэц, IMRaD-ын харьцаа:

| «Лавай» | IMRaD | Тайлбар |
|---|---|---|
| Сэдэв буюу гарчиг | Title | Бүгдийг том үсгээр, үндсэн бичвэрээс өөр фонтоор |
| Зохиогчийн хаяг | Authors, affiliations | Ажил, албан тушаал, цол зэрэг, овог нэр; хэвлэлийн шаардлага хангасан зураг |
| Хураангуй | Abstract | Орос, англи хэлээр 8—12 мөр |
| Түлхүүр үг | Keywords | Цөм утгыг илэрхийлэх цөөн нэр үг, холбоо үг |
| Удиртгал | Introduction + Methods | Арга, зорилго, зорилт, хэрэгцээ, асуудал, таамаглал, туршилт, материалын хэмжээ, боловсруулалтын арга |
| Үндсэн хэсэг | Results + Discussion | Өөрийн үр дүнг бусад судалгаа, онолтой харьцуулж, таамаглалаа баталсан, үгүйсгэснийг эшлэл, баримт, нотолгоотой; тоон үзүүлэлтэд заавал математик боловсруулалт |
| Судалгааны үр дүн | Results (нэгтгэл) | Үр дүнг баталгаатай, логик дараалалтай, эмх цэгцтэй |
| Судалгааны хязгаарлагдмал байдал | Limitations | Аль асуудлыг аль талаас хөндсөн, цаашид юуг судлах боломжтой |
| Дүгнэлт | Conclusion | Логик дараалалтай, оновчтой, тодорхой |
| Иш татсан бүтээл, ашигласан материал | References | Зөвхөн иш татсан, ашигласан бүтээл |

Анхаар: «Лавай»-д арга зүйг удиртгалд багтаадаг. Арга зүй урт, нарийн бол «Удиртгал» дотор «Судалгааны арга зүй» дэд гарчиг гарга, эсвэл редакцаас тусдаа хэсэг болгох эсэхийг тодруул.

MJER-ийн бүтэц IMRaD-тай бараг ижил: Гарчиг, Зохиогч, Хураангуй, түлхүүр үг (англи, монгол), Удиртгал (бичвэрийн 5 орчим хувь), Арга зүй, Үр дүн, Хэлэлцүүлэг ба дүгнэлт, Ном зүй, Хавсралт. Гарчгийг ром тоогоор дугаарлана.

### Бүрэн өгүүллийн бүрэлдэхүүн

1. Гарчиг
2. Хураангуй, түлхүүр үг
3. Удиртгал
4. Арга зүй (материал ба арга)
5. Үр дүн
6. Хэлэлцүүлэг (заримдаа үр дүнтэй нэгтгэнэ)
7. Дүгнэлт (заримдаа хэлэлцүүлгийн сүүлийн догол мөр)
8. Талархал
9. Ном зүй
10. Хавсралт (шаардлагатай бол)

### Гарчиг

**Зорилго:** уншигчийг татаж, агуулгыг үнэн зөв илэрхийлэх.

- Товч боловч тодорхой (ихэвчлэн 10—15 үг).
- Судалсан гол хувьсагч, хамаарлыг нэрлэ.
- Товчлол, мэргэжлийн хэллэг, асуулт хэлбэрээс зайлсхий (сэтгүүл зөвшөөрөөгүй бол).
- Бусад судалгаанаас ялгарахуйц нарийвчлалтай; хайлтад олдох түлхүүр үгтэй.
- Орон нутгийн судалгаанд улс, бүс нутгийг нэрлэ (MJER-ийн шаардлага).

| Үнэлгээ | Жишээ |
|---|---|
| Сайн | «Өндөр эрчимтэй интервал дасгалын ахмад настны зүрх судасны үйл ажиллагаанд үзүүлэх нөлөө» |
| Хэт ерөнхий | «Дасгал ба эрүүл мэнд» |
| Хэт нарийн | «60—75 насны хүмүүсийн VO2 max-аар хэмжсэн зүрх судасны үйл ажиллагаанд өндөр эрчимтэй интервал дасгал, дунд эрчимтэй тасралтгүй дасгалын нөлөөг харьцуулсан санамсаргүй хяналттай туршилт» |

### Хураангуй

**Зорилго:** өгүүллийг бүтнээр нь уншихгүйгээр түүний ач холбогдлыг шийдэх боломж олгох бие даасан хураангуй.

**Бүтэцлэгдсэн хураангуй** (сэтгүүл шаардсан бол):

- Үндэслэл, зорилго: 1—2 өгүүлбэр. Асуудал ба зорилго.
- Арга: 2—4 өгүүлбэр. Загвар, оролцогч, гол явц, шинжилгээний арга.
- Үр дүн: 3—5 өгүүлбэр. Гол үр дүн, статистик үзүүлэлттэй.
- Дүгнэлт: 1—2 өгүүлбэр. Тайлбар, ач холбогдол; шинэ мэдээлэл, хэтрүүлэлгүй.

Сэтгүүл бүтэцлэгдсэн хэлбэр шаардаагүй бол дээрх дарааллаар нэг үргэлжилсэн догол мөр бич.

**Хэмжээ:** ихэвчлэн 100—250 үг (сэтгүүлийн шаардлагыг шалга). «Лавай»: орос, англиар 8—12 мөр. MJER: англи, монголоор 10—15 мөр.

**Дүрэм:**

- Хураангуйг хамгийн сүүлд бич.
- Өгүүллийг уншаагүй хүнд ойлгогдохуйц бүрэн байлга.
- Эшлэл оруулахгүй.
- Товчлолгүй, эсвэл анх дурдахдаа задал.
- Арга, үр дүнд өнгөрсөн цаг, дүгнэлтэд одоо цаг.
- Гол тоон үр дүнг статистик үзүүлэлттэй нь оруул.

**Жишээ (бүтэцлэгдсэн):**

```
Үндэслэл: Эмнэлгийн дотоод халдвар өвчлөл, нас баралтын томоохон шалтгаан хэвээр байна.
Судалгаагаар халдваргүйжүүлэх шинэ аргын үр дүнг үнэлэв.

Арга: 500 ортой сургалтын эмнэлэгт 12 сарын өмнө-дараах судалгаа хийв. Гадаргуугаас сар бүр
арчдас авч, халдварын давтамжийг тандалтын өгөгдлөөр хянав. Энгийн цэвэрлэгээн дээр хэт ягаан
туяаны (UV-C) халдваргүйжүүлэлт нэмсэн.

Үр дүн: Арга нэвтрүүлсний дараа гадаргуугийн бохирдол 47 хувиар буурсан (95% ИЗ: 38—56,
p < 0.001). Шээсний катетертай холбоотой халдвар 1000 катетер-өдөрт 3.2-оос 1.8 болж буурсан
(RR = 0.56, 95% ИЗ: 0.38—0.83, p = 0.004). Гаж нөлөө ажиглагдаагүй.

Дүгнэлт: UV-C халдваргүйжүүлэлт гадаргуугийн бохирдол, халдварын давтамжийг бууруулсан.
Энэ аргыг эмнэлгийн халдвар хяналтын хөтөлбөрт нэмж болно.
```

Энэ жишээ эх англи заавраас орчуулсан бөгөөд тоо нь зөвхөн хэлбэрийг харуулна.

### Удиртгал

**Зорилго:** судалгаа чухал асуултыг зохих аргаар хөндсөн гэдэгт уншигчийг итгүүлэх.

**Бүтэц (4—5 догол мөр):**

1. **Ерөнхий дүр зураг:** судалгааны салбар, сэдвийн ач холбогдол. Батлагдсан баримтад одоо цаг. Мэргэжлийн бус уншигчид ч ойлгогдохуйц.
2. **Нарийсгах (2—3 догол мөр):** холбогдох өмнөх судалгаа; юу мэдэгдэж байгаа; маргаантай асуудал, хязгаарлалт; цоорхой руу хөтлөх логик дараалал.
3. **Цоорхой:** юу тодорхойгүй хэвээр байгаа, энэ нь яагаад асуудал болохыг тодорхой хэл.
4. **Энэ судалгаа:** асуулт, таамаглал; ерөнхий арга; цоорхойг хэрхэн нөхөх. Сэтгүүл зөвшөөрвөл гол үр дүнг товч дурдаж болно.

**Хэмжээ:** ихэвчлэн 1.5—2 хуудас, 4—5 догол мөр. MJER: бичвэрийн 5 орчим хувь.

**Цаг:** батлагдсан баримтад одоо цаг («Дасгал зүрх судасны эрүүл мэндийг сайжруулдаг»); өмнөх судалгааны үр дүнд өнгөрсөн цаг («Бат нар ... болохыг тогтоосон [3]»); өөрийн зорилгод одоо эсвэл өнгөрсөн цаг.

**Алдаа:** хэт ерөнхий эхлэл («Эрт дээр үеэс хүн төрөлхтөн...»); тойм өгүүлэл мэт бүрэн уншлагын тойм; хамааралгүй, хуучирсан эшлэл; цоорхойг тодорхой заагаагүй; үндэслэл сул; асуулт, таамаглалгүй; арга, үр дүнг удиртгалд оруулах.

**Хариулах асуулт:** энэ сэдвийн талаар юу мэдэгдэж байна вэ? Юу мэдэгдэхгүй байна вэ? Энэ цоорхой яагаад чухал бэ? Судалгаа юуг тогтоохыг зорьсон бэ?

### Арга зүй

**Зорилго:** өөр судлаач судалгааг давтан хийж, найдвартай эсэхийг үнэлэх боломж олгох.

**Дэд хэсэг:**

- **Судалгааны загвар:** санамсаргүй хяналттай туршилт, когорт, хөндлөн огтлолын судалгаа г.м.; сонголтын үндэслэл; далдлалт, санамсаргүй хуваарилалт, хяналтын бүлэг.
- **Оролцогч, түүвэр:** судалгааны хүн ам; хамруулах, хасах шалгуур (энд жагсаалт болно); түүврийн хэмжээ, түүнийг хэрхэн тооцсон (чадлын шинжилгээ); элсүүлсэн арга, газар. Амьтан бол зүйл, омог, нас, хүйс, тэжээх нөхцөл.
- **Материал, багаж:** бүх материал, урвалж, багаж; үйлдвэрлэгч, улс (хаалтад); тусгай бүтээгдэхүүний каталогийн дугаар; программ хангамжийн нэр, хувилбар.
- **Явц:** цаг хугацааны дарааллаар, давтан хийхэд хангалттай нарийн; хугацаа, нөхцөл («37 °C-д 2 цаг»); асуулгын хэрэгсэл, түүний баталгаажуулалт.
- **Хэмжсэн хувьсагч:** бүх хувьсагч, гол ба туслах үр дагавар, хэмжих хэрэгсэл, хэмжих нэгж.
- **Статистик шинжилгээ:** бүх тест, сонголтын үндэслэл; ач холбогдлын түвшин (ихэвчлэн α = 0.05); чадлын шинжилгээ; программ хангамж, хувилбар; дутуу өгөгдлийг хэрхэн боловсруулсан; олон харьцуулалтын засвар.
- **Ёс зүй:** ёс зүйн хорооны зөвшөөрөл (хорооны нэр, огноо, дугаар); мэдээлэл өгсний үндсэн дээрх зөвшөөрөл; Хельсинкийн тунхаглал; амьтны судалгаанд ARRIVE.

**Цаг:** өөрийн хийсэн үйлд өнгөрсөн цаг («Бид ... хэмжив», «Оролцогчид асуулга бөглөсөн»); тогтсон аргын тайлбарт одоо цаг («PCR нь ДНХ-ийг олшруулдаг»).

**Алдаа:** давтан хийхэд хүрэлцэхгүй мэдээлэл; аргыг анх удаа үр дүнд дурдах; үр дүн, хэлэлцүүлгийг арга зүйд оруулах; статистик тест дутуу; тайлбаргүй товчлол; ёс зүйн мэдэгдэлгүй.

### Үр дүн

**Зорилго:** үр дүнг тайлбаргүйгээр бодитойгоор харуулах. Тайлбарыг хэлэлцүүлэгт үлдээ.

**Бүтэц:**

- Эхний догол мөр: оролцогч, түүврийн шинж; элсүүлэлтийн урсгал (шалгасан, хамруулсан, дуусгасан); шаардлагатай бол CONSORT маягийн урсгалын бүдүүвч.
- Дараагийн догол мөрүүд: гол үр дагавраас эхлэн, удиртгалд заасан зорилгын дарааллаар; сэдэв эсвэл цаг хугацаагаар; зураг, хүснэгтийг дугаараар нь дурдах.

**Үр дүн бүрт:** ажиглагдсан үр дүн; нөлөөний чиглэл; нөлөөний хэмжээ; статистик ач холбогдол; итгэх завсар.

Жишээ: «Систолын даралт оролцох бүлэгт 12 мм м.у.б-аар, хяналтын бүлэгт 3 мм м.у.б-аар буурсан (зөрүү 9 мм м.у.б, 95% ИЗ: 4—14, p = 0.002).»

**Статистик тайлагнал:** тестийн статистик (t, F, χ²); чөлөөний зэрэг; p-утга (0.001-ээс их бол яг утга, бага бол «p < 0.001»); нөлөөний хэмжээ, итгэх завсар; түүврийн хэмжээ.

Жишээ: «Бүлгүүдийн шалгалтын гүйцэтгэл ялгаатай байв (t(48) = 3.21, p = 0.002, Cohen-ийн d = 0.87, 95% ИЗ: 0.34—1.40).»

**Цаг:** өнгөрсөн цаг («Дундаж нас 45 байв», «Оролцогчдын ... буурсан»).

**Алдаа:** үр дүнг тайлбарлах; хүснэгт, зургийн бүх тоог бичвэрт давтах; шинэ арга танилцуулах; статистикийн мэдээлэл дутуу; нэгж, тэмдэглэгээ тогтворгүй; сөрөг, хүлээгээгүй үр дүнг орхих; сонгомол тайлагнал (шалгасан бүх таамаглалыг тайлагнана).

**Зохион байгуулах арга:** зорилгоор (гол үр дагавар → туслах үр дагавар А → Б); шинжилгээний төрлөөр (дүрслэх статистик → нэг хүчин зүйлийн → олон хүчин зүйлийн шинжилгээ); цаг хугацаагаар (суурь үзүүлэлт → 1 сар → 6 сар).

### Хэлэлцүүлэг

**Зорилго:** үр дүнг тайлбарлаж, одоо байгаа мэдлэгтэй холбох, хязгаарлалтаа хүлээн зөвшөөрөх, цаашдын чиглэлийг санал болгох.

**Бүтэц:**

1. **Гол үр дүнгийн хураангуй:** зорилгоо сануулж, гол үр дүнг 2—4 өгүүлбэрээр; таамаглал батлагдсан эсэх.
2. **Тайлбар (2—4 догол мөр):** өмнөх судалгаатай харьцуулах; тохирол, зөрүүг тайлбарлах; механизм, тайлбар; хүлээгээгүй үр дүн; өөр тайлбар; онолыг дэмжиж, няцааж байгаа эсэх.
3. **Давуу тал, хязгаарлалт:** хязгаарлалтыг тодорхой нэрлэж, тайлбарт хэрхэн нөлөөлөхийг хэл. «Илүү том түүвэр хэрэгтэй» мэт ерөнхий хязгаарлалтаас зайлсхий.
4. **Ач холбогдол:** эмнэлзүйн, практик, бодлогын, онолын.
5. **Дүгнэлт ба цаашдын судалгаа:** гол санаа; цоорхой, хязгаарлалтыг нөхөх тодорхой судалгаа.

**Хэмжээ:** ихэвчлэн 3—5 хуудас, хамгийн урт хэсэг.

**Цаг:** өөрийн үр дүнд өнгөрсөн цаг; тайлбарт одоо цаг («Энэ нь ... байж болохыг харуулж байна»); цаашдын судалгаанд ирээдүй цаг.

**Жишээ:**

```
Шинж тэмдэг 30 хувиар буурсан бидний үр дүн ижил төстэй арга хэрэглэсэн өмнөх судалгааны
28 хувийн бууралттай ойролцоо [12]. Харин өөр нэг судалгаагаар ач холбогдолтой нөлөө
илрээгүй [13] нь тэдний хэрэглэсэн аргын эрчим бага байсантай холбоотой байж магадгүй.
```

```
Хөндлөн огтлолын загвар учир шалтгааныг тогтоох боломж олгохгүй. Мөн нэг эмнэлгээс
хүртээмжээр сонгосон түүвэр тул үр дүнг орон нутгийн хүн амд шууд хамааруулахад хязгаартай.
Өөрөө үнэлсэн хэмжүүр санах хазайлт үүсгэж болох тул бид бүтэцлэгдсэн ярилцлага хэрэглэсэн.
```

**Алдаа:** үр дүнг тайлбаргүй давтах; хэт тайлбарлах, үндэслэлгүй учир шалтгаан; зөрүүтэй, сөрөг үр дүнг орхих; өмнөх судалгаатай харьцуулаагүй; шинэ өгөгдөл, арга оруулах; ерөнхий хязгаарлалт; судалгааны хүн амаас хэт өргөн нийтлэг дүгнэлт; ач холбогдлыг тайлбарлаагүй.

### Дүгнэлт

- Тусдаа хэсэг эсвэл хэлэлцүүлгийн сүүлийн догол мөр (сэтгүүлийн шаардлагаар).
- 1—2 догол мөр: гол үр дүн, ач холбогдол; шинэ мэдээлэлгүй.
- «Лавай»-д: үр дүнд гаргасан дүгнэлтүүдийг логик дараалалтай, оновчтой, тодорхой.

### Нэмэлт хэсэг

- **Талархал:** санхүүжүүлэгч (гэрээний дугаартай); зохиогчийн шалгуур хангаагүй ч их хувь нэмэр оруулсан хүмүүс; материал, багаж өгсөн хүмүүс; ашиг сонирхлын зөрчлийн мэдэгдэл.
- **Ном зүй:** сэтгүүлийн стандартаар (references/mn/eshlel.md); эшлэл бүр бичвэрт, бичвэрийн эшлэл бүр жагсаалтад. Анхдагч судалгааны өгүүлэлд ихэвчлэн 20—50 бүтээл.
- **Хавсралт:** нэмэлт зураг, хүснэгт, өгөгдөл; дэлгэрэнгүй протокол, асуулга; кодын сан.

### Хэсэг бүрийн цаг

| Хэсэг | Цаг |
|---|---|
| Хураангуй: үндэслэл | Одоо (батлагдсан баримт), өнгөрсөн (өмнөх судалгаа) |
| Хураангуй: арга, үр дүн | Өнгөрсөн |
| Хураангуй: дүгнэлт | Одоо |
| Удиртгал: ерөнхий суурь | Одоо |
| Удиртгал: өмнөх судалгаа | Өнгөрсөн |
| Удиртгал: зорилго | Одоо эсвэл өнгөрсөн |
| Арга зүй | Өнгөрсөн (өөрийн үйл), одоо (тогтсон арга) |
| Үр дүн | Өнгөрсөн |
| Хэлэлцүүлэг: өөрийн үр дүн | Өнгөрсөн |
| Хэлэлцүүлэг: тайлбар | Одоо |
| Дүгнэлт | Одоо |

Монгол хэлний жишээ: өнгөрсөн цаг «-в», «-сан», «-лаа», «-жээ» (судалгааны бичвэрт «-в», «-сан» түгээмэл); одоо цаг «-даг», «-на», «... байна».

### IMRaD-ын хувилбар

- **Үр дүн, хэлэлцүүлэг нэгтгэсэн:** үр дүн бүрийг танилцуулаад шууд хэлэлцэнэ; олон туршилттай судалгаанд тохиромжтой.
- **Тусдаа дүгнэлтгүй:** дүгнэлт хэлэлцүүлгийн сүүлд.
- **Онолын тойм тусдаа бүлэгтэй (ILMRaD):** диссертацид түгээмэл.

### Судалгааны төрөлд тааруулах

- **Эмнэлзүйн туршилт:** үр дүнд CONSORT урсгалын бүдүүвч; арга зүйд туршилтын бүртгэлийн дугаар; үр дүнд гаж нөлөө.
- **Системчилсэн тойм, мета-шинжилгээ:** арга зүйд хайлтын стратеги, хамруулах шалгуур; үр дүнд PRISMA урсгалын бүдүүвч, нэгтгэл; хазайлтын эрсдэлийн үнэлгээ.
- **Тохиолдлын тайлан:** удиртгал (эмгэгийн суурь мэдээлэл) → тохиолдлын тайлбар (арга, үр дүнгийн оронд) → хэлэлцүүлэг.
- **Ажиглалтын судалгаа:** STROBE; арга зүйд төөрөгдүүлэгч хүчин зүйл; хэлэлцүүлэгт учир шалтгааны хязгаарлалт.

### Сэтгүүлийн төрлөөр ялгаатай байдал

| Төрөл | Хэмжээ | Бүтэц | Гол анхаарал |
|---|---|---|---|
| Nature, Science | 2000—4500 үг | Өөрчилсөн IMRaD, арга нь хавсралтад | Өргөн ач холбогдол |
| Анагаахын сэтгүүл (NEJM, Lancet, JAMA) | 2700—3500 үг | Хатуу IMRaD | Эмнэлзүйн үр дагавар |
| Салбарын сэтгүүл | 3000—6000 үг | Стандарт IMRaD | Техникийн гүнзгий мэдээлэл |
| Машин сургалтын хурал (NeurIPS, ICML) | 8—9 хуудас | Удиртгал, арга, туршилт, дүгнэлт | Шинэ хувь нэмэр, туршилтын харьцуулалт |
| Монгол сэтгүүл («Лавай», MJER) | Сэтгүүлийн заавраар (MJER: A4 10 хуудас хүртэл) | IMRaD-д суурилсан монгол бүтэц | Сэтгүүлийн зааврыг үз |

Сэтгүүлийн төрлийн дэлгэрэнгүй ялгааг (хэсгийн хувь хэмжээ, хуралд зориулсан бүтэц) references/imrad_structure.md-ээс үз.

### Илгээхийн өмнөх бүтцийн шалгах хуудас

- [ ] Үг, хуудасны тоо хязгаарт багтсан
- [ ] Хэсгийн харьцаа зохистой
- [ ] Бичлэгийн хэв маяг сэтгүүлд тохирсон
- [ ] Арга зүй давтан хийх боломж олгох
- [ ] Хязгаарлалтыг хүлээн зөвшөөрсөн
- [ ] Хураангуй, түлхүүр үг сэтгүүлийн шаардсан хэлээр

---

# Reference: references/mn/bichleg-zarchim.md

## Шинжлэх ухааны бичлэгийн зарчим

Эх сурвалж: K-Dense «Scientific Writing Principles» (references/writing_principles.md)-ийн монгол буулгалт. Жишээг монгол хэлэнд тохируулж дахин бичив.

Шинжлэх ухааны бичлэг уран зохиол, нийтлэлээс үнэн зөв, товч, бодитой байдлаараа ялгарна. Зорилго нь уншигчийг үгийн баялаг, нарийн бүтцээр гайхшруулах биш, судалгааг ойлгож, үнэлж, цааш нь хөгжүүлэх боломж олгох.

### 1. Тодорхой

Зорилтот уншигчид шууд, ганц утгаар ойлгогдох бичвэр.

**Тодорхой, нэг утгатай үг хэрэглэ:**

| Бүрхэг | Тодорхой |
|---|---|
| «Эм нэлээд олон өвчтөнд тус болсон бололтой.» | «Эм өвчтөнүүдийн 68 хувьд (32/47) шинж тэмдгийг бууруулсан.» |

**Мэргэжлийн нэр томьёог анх дурдахдаа тайлбарла:** «Бид тархины нейротрофик хүчин зүйл (BDNF) буюу мэдрэлийн эсийн амьдрах чадвар, уян хатан байдалд оролцдог уургийг хэмжив.»

**Догол мөрийн логик урсгал:** догол мөр бүр нэг гол санаатай; түлхүүр өгүүлбэр санааг танилцуулна; дэмжих өгүүлбэр түүнийг хөгжүүлнэ; шилжүүлэх өгүүлбэр дараагийн догол мөртэй холбоно.

**Идэвхтэй хэв тодорхой болгож байвал хэрэглэ:**

| Үйлдэгдэх (бүрхэг) | Идэвхтэй (тодорхой) |
|---|---|
| «Дээжүүд судлаачдаар шинжлэгдсэн.» | «Судлаачид дээжийг шинжлэв.» |

Үйлдэгч чухал биш арга зүйн өгүүлбэрт үйлдэгдэх хэв зохимжтой: «Цусны дээжийг судалгааны эхэнд, 6 долоо хоногийн дараа авсан.» Монгол хэлэнд эзэнгүй өгүүлбэр («... авсан») ихэвчлэн «-гд-» хэвээс илүү уншигдана.

**Урт, нийлмэл өгүүлбэрийг хуваа:**

```
Муу: Гурван эмнэлгээс элсүүлсэн, 12 сарын турш 4 долоо хоног тутам баталгаажсан асуулгаар
үнэлсэн 200 оролцогчийг хамарсан бидний судалгааны үр дүн оролцох бүлэгт мэдэгдэхүйц
сайжрал байгааг харуулсан.

Сайн: Судалгаанд гурван эмнэлгээс 200 оролцогч элсүүлэв. Оролцогчдыг 12 сарын турш 4 долоо
хоног тутам баталгаажсан асуулгаар үнэлсэн. Оролцох бүлэгт ач холбогдолтой сайжрал ажиглагдав.
```

**Тодорхой үйл үг хэрэглэ:** «Судалгаагаар өсвөр насныхны сэтгэл гутралыг харсан» → «Судалгаагаар өсвөр насныхны сэтгэл гутралд нөлөөлөх хүчин зүйлийг судлав».

#### Түгээмэл бүрхэг байдал

- **Төлөөний үгийн давхар утга:** «А бүлэг эм, Б бүлэг хуурмаг эм хэрэглэв. Тэд сайжирсан.» (Хэн?) → «Эм хэрэглэсэн бүлэг сайжирсан.»
- **Байрлал буруу тодотгол:** «Бид өвчтөнүүдийн даралтыг автомат аппаратаар хэмжив» гэвэл хэн аппарат хэрэглэснийг тодорхой бич: «Бид автомат аппаратаар өвчтөнүүдийн даралтыг хэмжив.»
- **Бүрхэг заалт:** «Илрэл нэмэгдэхэд эсийн өсөлт буурсан нь хүлээгээгүй үр дүн.» (Аль нь?) → «Илрэл нэмэгдэхэд эсийн өсөлт буурсан. Энэ урвуу хамаарал хүлээгдээгүй байв.»
- **Харьяалахын тийн ялгалын давхар утга:** «Хулгайн мод тээвэрлэгчид» (хулгайн мод уу, хулгайгаар тээвэрлэгч үү?) → «Модыг хулгайгаар тээвэрлэгчид».

### 2. Товч

Санааг тодорхой, бүрэн байдлыг алдалгүйгээр цөөн үгээр илэрхийл.

**Илүүц үг, хэллэгийг хас:**

| Нуршуу | Товч |
|---|---|
| «...-аас шалтгаалан» | «...-аас болж», «тул» |
| «...-ыг хийх зорилгоор» | «...-хын тулд» |
| «Дурдах нь зүйтэй зүйл бол ...» | [хас] |
| «нийт 50 оролцогч» | «50 оролцогч» |
| «бүрэн арилгах» | «арилгах» |
| «... болох нь харагдсан» | «... байна» |
| «одоогийн байдлаар» | «одоо» |
| «судалгаа явуулах» | «судлах» |
| «анхаарал хандуулах» | «анхаарах» |

**Оршил хэллэгээс зайлсхий:** «Сонирхолтой нь, бидний судалгааны үр дүн ... болохыг харуулж байна» → «Үр дүнгээс ... харагдана.»

**«-лт» нэр + хоосон үйл үгийн оронд үйл үг** (англи хэлний nominalization-ын монгол хэлбэр):

| Нуршуу | Товч |
|---|---|
| «шийдвэр гаргалт хийх» | «шийдэх» |
| «дүн шинжилгээ хийх» | «шинжлэх» |
| «судалгаа хийх» | «судлах» |
| «үнэлгээ хийх» | «үнэлэх» |
| «мэдээлэл өгөх» | «мэдэгдэх» |
| «бууралт үзүүлэх» | «буурах» |

**Шаардлагагүй эрчимжүүлэгч үг:** «Үр дүн маш ач холбогдолтой байв» → «Үр дүн ач холбогдолтой байв» (зэргийг p-утга илэрхийлнэ).

**Давталт:** «Эмчилгээ хийлгэсэн оролцох бүлгийн оролцогчдын үр дүн илүү сайн байв» → «Оролцох бүлгийн үр дүн илүү сайн байв.»

**Урт өгүүлбэр бүхэн муу биш:** «Цусны дээжийг Waters Acquity UPLC системтэй холбосон Xevo TQ-S масс-спектрометрээр (Waters Corporation, АНУ) шингэн хроматографи-давхар масс-спектрометрийн (LC-MS/MS) аргаар шинжлэв.» Үг бүр шаардлагатай мэдээлэл агуулж байгаа тул зөв.

**Гол асуулт:** утга, нарийвчлалаа алдалгүйгээр аль нэг үгийг хасаж болох уу? Болох бол хас.

### 3. Үнэн зөв

Өгөгдөл, арга, тайлбарыг нарийн, зөв илэрхийлэх.

- **Яг утгыг зохих нарийвчлалтай:** «Дундаж 25 орчим байв» → «Дундаж 24.7 ± 3.2 (стандарт хазайлт) байв.»
- **Хэмжилтийн чадвартай тохирох нарийвчлал:** «Дундаж нас 45.237» (хуурмаг нарийвчлал) → «45.2».
- **Нэр томьёо тууштай:** удиртгалд «танин мэдэхүйн үйл ажиллагаа», арга зүйд «оюуны гүйцэтгэл», үр дүнд «сэтгэхүйн чадвар» гэж бүү солбин бич. Нэгийг сонго, эсвэл тодорхойл: «танин мэдэхүйн үйл ажиллагаа (оюуны гүйцэтгэл гэж бас нэрлэдэг)».
- **Ажиглалт, тайлбарыг ялга:** «Дундаж даралт 145-аас 132 мм м.у.б болж буурсан (p = 0.003).» (ажиглалт) / «Энэ нь арга даралтыг бууруулдаг байж болохыг харуулж байна.» (тайлбар)
- **Тодорхойгүй байдлыг тодорхой хэл:** «Хэмжилтэд зарим алдаа байж магадгүй» → «Аппаратын үзүүлэлтээр хэмжилтийн стандарт алдаа ±2.5 мм м.у.б.»
- **Статистикийн зөв хэллэг:** «Хамаарал маш ач холбогдолтой (p = 0.03)» буруу → «Хамаарал статистикийн хувьд ач холбогдолтой (p = 0.03).»
- **Бүх тоог шалга:** бичвэрийн тоо хүснэгт, зурагтай таарах; n-ийн нийлбэр зөв; хувь зөв тооцоологдсон.

**Түгээмэл алдаа:**

- Хэт ерөнхийлөх: «Дасгал сэтгэл гутралаас хамгаална» → «Манай түүвэрт дасгалын бүлэгт санамсаргүйгээр хуваарилагдсан оролцогчдын сэтгэл гутралын шинж тэмдэг хяналтынхаас бага байв (BDI-II-ын онооны зөрүү 3.2, 95% ИЗ: 1.5—4.9, p < 0.001).»
- Үндэслэлгүй учир шалтгаан (ажиглалтын судалгаанаас): «D аминдэм хорт хавдрын эрсдэлийг бууруулдаг» → «Энэ когортод D аминдэмийн түвшин хорт хавдрын давтамжтай урвуу хамааралтай байв (HR = 0.82, 95% ИЗ: 0.71—0.95).»
- Бүрхэг тоо: «Олон оролцогч судалгаанаас гарсан» → «50 оролцогчийн 15 нь (30 хувь) судалгааг дуусгалгүй гарсан.»

### 4. Бодитой

- **Хэвшмэл үнэлгээгүй:** «Хүлээж байсанчлан бидний давуу арга илүү сайн ажилласан» → «А арга Б аргаас өндөр нарийвчлалтай байв (87 ба 76 хувь, p = 0.02).»
- **Зөрүүтэй нотолгоог хүлээн зөвшөөр:** «Бидний үр дүн ач холбогдолтой нөлөө илрээгүй өмнөх судалгаатай [8] зөрж байна. Энэ нь аргын эрчим, хүн амын онцлогийн ялгаатай холбоотой байж болно.»
- **Сэтгэл хөдлөлийн үг хэрэглэхгүй:** «Үр дүн сэтгэл дундуур, түгшүүртэй байлаа» → «Арга шинж тэмдгийг ач холбогдолтой бууруулаагүй (p = 0.42).»
- **Баримт, таамаглалыг ялга:** «Эсийн амьдрах чадвар буурахад каспаза-3-ын идэвх нэмэгдсэн нь апоптоз эсийн үхлийн гол механизм байж болохыг харуулж байна.»

### 5. Тууштай

- **Нэр томьёо:** нэг ойлголтод нэг нэр томьёо; товчлолыг анх тайлбарлаад тууштай хэрэглэ; ген, уураг, химийн бодисын стандарт нэршил.
- **Тэмдэглэгээ:** p-утга, итгэх завсрын хэлбэр; хэмжих нэгж; аравтын оронгийн тоо.
- **Цаг:** өөрийн үйлд өнгөрсөн, батлагдсан баримтад одоо цаг (references/mn/butets.md).
- **Хэлбэр:** сэтгүүлийн заавар; эшлэлийн хэлбэр; гарчгийн том үсэг (монголд зөвхөн эхний үг, оноосон нэр); тоог цифр эсвэл үгээр бичих дүрэм.

### 6. Логик зохион байгуулалт

Өгүүллийн «улаан утас»: удиртгалын асуулт үр дүнд хариулт авч, үр дүн хэлэлцүүлэгт тайлбарлагдана.

- **Догол мөр:** түлхүүр өгүүлбэр → дэмжих өгүүлбэр (нотолгоо, тайлбар) → дүгнэх, шилжүүлэх өгүүлбэр.
- **Дохио үг:** «Эхлээд бид ...-ыг шинжлэв. Дараа нь ... судлав. Эцэст нь ... үнэлэв.» Дохио үгийг логик дараалал байгаа үед л хэрэглэ; догол мөр бүрийг механикаар «Нэгдүгээрт», «Цаашлаад»-аар эхлүүлэхгүй.
- **Зэрэгцээ бүтэц:** «Зорилго нь (1) даралтыг хэмжих, (2) танин мэдэхүйн үнэлгээ хийх, (3) бид сэтгэл санааг үнэлэхийг хүссэн» → «Зорилго нь (1) даралтыг хэмжих, (2) танин мэдэхүйг үнэлэх, (3) сэтгэл санааг үнэлэх.»

### Болгоомжлол: хэт их, хэт бага

| Төрөл | Жишээ |
|---|---|
| Хэт их | «Арга тодорхой нөхцөлд шинж тэмдэгт зарим талаараа нөлөөлж болох магадлалтай байж болох юм.» |
| Хэт бага | «Арга сэтгэл гутралыг эдгээдэг.» |
| Зохистой | «Арга энэ түүвэрт сэтгэл гутралын шинж тэмдгийг ач холбогдолтой бууруулсан нь хөнгөн, дунд зэргийн сэтгэл гутралд үр дүнтэй байж болохыг харуулж байна.» |

Болгоомжлолын үг: «харуулж байна», «илэрхийлж байна» (хамааралд «баталж байна» биш); «байж магадгүй», «байж болно» (боломж); «бололтой» (баталгаажуулах шаардлагатай ажиглалт); «магадлалтай», «байх магадлал өндөр» (итгэлийн зэрэг).

### Хүнлэгжүүлэх (антропоморфизм)

| Буруу | Зөв |
|---|---|
| «Судалгаа ...-ыг судлахыг хүссэн.» | «Бид ...-ыг судлахыг зорьсон.» / «Судалгаагаар ...-ыг судлав.» |
| «Энэ өгүүлэл ...-ыг батлах болно.» | «Энэ өгүүлэлд ...-ыг харуулна.» |
| «Хүснэгт 1 бидэнд хэлж байна.» | «Хүснэгт 1-д ... харагдана.» |

### Товчлол

- 3—4-өөс цөөн удаа гарах нэрийг товчлохгүй.
- Хураангуйд хэрэглэсэн бол хураангуйд, үндсэн бичвэрт дахин анх дурдахдаа задал.
- Гарчигт товчлохгүй.
- Нэг өгүүлэлд 3—4-өөс олон шинэ товчлол оруулахгүйг хичээ.
- Нийтлэг олон улсын товчлолыг (ДНХ/DNA, ХДХВ/HIV) тайлбаргүй хэрэглэж болно; монгол, олон улсын хувилбарын аль нэгийг сонгож тууштай хэрэглэ.

### Тоо, нэгж

- **Цифрээр:** 10-аас дээш тоо; нэгжтэй тоо (5 мг, 3 мл); статистик утга (p = 0.03, t = 2.14); нас, огноо, цаг; оноо; хувь.
- **Үгээр:** нэгжгүй 10-аас доош тоо (таван оролцогч); өгүүлбэрийн эхэнд (эсвэл өгүүлбэрийг өөрчил). MJER-д 1—10 хүртэлх тоог үгээр бичнэ.
- **Нэгж:** тоо, нэгжийн хооронд зай (5 мг); нэгжийн ард цэггүй; SI нэгж; аравтын оронгийн тоо тууштай.
- **Хязгаар:** урт зураасаар, нэгжийг сүүлийн тооны ард: «15—20 мг» (зөв бичих дүрмийн 61-р зүйл).
- **Аравтын тэмдэг, мянгатын тусгаарлагч:** сэтгүүлийн шаардлагаар (цэг эсвэл таслал), нэг бичвэрт нэг хэлбэр. Олон улсын сэтгүүлд цэг.

### Засварын шалгах хуудас

**Агуулга:**
- [ ] Өгүүлбэр бүр утга нэмж байна уу?
- [ ] Мэдэгдэл бүр өгөгдлөөр нотлогдсон уу?
- [ ] Логик тодорхой, зөв үү?
- [ ] Тайлбар үр дүнгээс давсан уу?

**Догол мөр:**
- [ ] Догол мөр бүр нэг гол санаатай юу?
- [ ] Логик дарааллаар уу?
- [ ] Шилжилт жигд үү?
- [ ] «Улаан утас» тодорхой юу?

**Өгүүлбэр:**
- [ ] Тодорхой, товч уу?
- [ ] Бүтэц нь олон янз уу?
- [ ] Эзэн, өгүүлэхүүн зохицсон уу?
- [ ] Гадаад хэлний бүтэц хуулсан өгүүлбэр байна уу?

**Үг:**
- [ ] Үгийн сонголт нарийн уу?
- [ ] Нэр томьёо тайлбарлагдсан, тууштай юу?
- [ ] Товчлол шаардлагатай, тайлбарлагдсан уу?
- [ ] Тоо зөв хэлбэрээр бичигдсэн үү?

**Хэл зүй, зөв бичиг:**
- [ ] Цаг зөв, тууштай юу?
- [ ] Таслал, цэг тэмдэг зөв үү?
- [ ] Зөв бичгийн алдаагүй юу (references/mn/mongol-nairuulga.md)?

### Хэрэгсэл

- **Хамт ажиллагчийн хянан үзэлт:** хамгийн үнэ цэнэтэй хэрэгсэл. Ойлгомжгүй хэсэг, логик урсгал, тайлбар үндэслэлтэй эсэхийг шалгуул.
- **Зөв бичгийн шалгалт:** Humanizer (эсвэл Humanizer-MN) ур чадварын `scripts/mn_tells.py` монгол бичвэрийн түгээмэл алдааг заана.
- Англи хэлний хэрэгсэл (Grammarly, LanguageTool), уншигдах байдлын хэмжүүр монгол бичвэрт тохирохгүй.

---

# Reference: references/mn/eshlel.md

## Эшлэл, ном зүй

Эх сурвалж: K-Dense «Citation Styles Guide» (references/citation_styles.md)-ийн монгол буулгалт; МУБИС-ийн «Лавай» эрдэм шинжилгээний бичгийн зөвлөмж; MNS 5217:2012 «Монгол кирилл үсгийг латин үсгээр галиглах» стандарт; Монгол хэлний зөв бичих дүрэм (1983), 48-р зүйл.

Жишээн дэх зохиогч, сэтгүүлийн нэр нь зөвхөн хэлбэрийг харуулах загвар. Бодит эшлэлд эдгээрийг бүү хуул.

### Эшлэл зохиохгүй байх журам

1. Эшлэл бүр хэрэглэгчийн өгсөн эх сурвалж эсвэл тухайн ярианд шалгасан эх сурвалжаас ирнэ.
2. Эх сурвалж хайх хэрэгсэл (вэб хайлт, PubMed, Google Scholar, номын сангийн сан) байгаа бол хайж, хураангуй, мэдээллийг нь уншаад хамааралтай эсэхийг шалга.
3. Хэрэгсэлгүй, эсвэл олдоогүй бол «[эшлэл шаардлагатай: юуны тухай]» гэж тэмдэглэ. Санаж байгаа мэт зохиогч, он, сэтгүүлийн нэр бүү бич.
4. Мэдээлэл дутуу бол (он, боть, хуудас, хэвлэлийн газар, DOI) зохиохгүй: «[он?]», «[хуудас?]» гэж үлдээгээд хэрэглэгчээс асуу.
5. Эшилсэн санаа эх сурвалжид үнэхээр байгаа эсэхийг шалга. Хураангуйгаас өөр зүйл эшлэх бол бүтэн бичвэрийг унш.

### Стандарт сонгох

| Стандарт | Голлон хэрэглэдэг салбар | Бичвэр доторх хэлбэр | Ном зүйн дараалал |
|---|---|---|---|
| APA 7 | Сэтгэл зүй, боловсрол, нийгмийн ухаан | (Зохиогч, он) | Зохиогчийн нэрийн цагаан толгойгоор |
| Vancouver | Анагаах, биоанагаах | [1] | Эшилсэн дарааллаар |
| AMA 11 | Анагаах | ¹ дээд индекс | Эшилсэн дарааллаар |
| IEEE | Инженер, мэдээлэл технологи | [1] | Эшилсэн дарааллаар |
| Chicago 17 | Хүмүүнлэг, түүх | Зүүлт эсвэл (Зохиогч он) | Цагаан толгойгоор |
| ACS | Хими | ¹ эсвэл (1) | Эшилсэн дарааллаар |
| «Лавай» (МУБИС) | Боловсрол, хүмүүнлэг | Редакцын жишээгээр | Зохиогчийн нэрийн цагаан толгойгоор |

Сэтгүүлийн зохиогчид өгөх зааварт заасан стандарт бүх зөвлөмжөөс давуу. Сэтгүүлийн заавар өөртөө зөрчилтэй бол (жишээ нь MJER-ийн заавар APA 7 гэж заасан ч жишээ нь Vancouver маягтай) редакцаас тодруул.

### APA 7

**Бичвэр дотор:**

- Нэг зохиогч: (Бат, 2023) эсвэл Бат (2023) ...-ыг тогтоосон.
- Хоёр зохиогч: (Бат ба Дорж, 2023); англи бичвэрт (Bat & Dorj, 2023).
- Гурав ба түүнээс дээш: (Бат нар, 2023); англи бичвэрт (Bat et al., 2023).
- Олон бүтээл: (Бат, 2020; Дорж, 2023) цагаан толгойн дарааллаар.
- Шууд эшлэл: хуудастай (Бат, 2023, х. 45); англиар (Bat, 2023, p. 45).

**Ном зүй:**

```
Сэтгүүлийн өгүүлэл:
Зохиогч, А. А., Зохиогч, Б. Б., & Зохиогч, В. В. (Он). Өгүүллийн нэр. Сэтгүүлийн нэр, Боть(Дугаар), хуудас. https://doi.org/xx.xxxx

Ном:
Зохиогч, А. А. (Он). Номын нэр: Дэд гарчиг (Хэвлэл). Хэвлэлийн газар.

Номын бүлэг:
Зохиогч, А. А. (Он). Бүлгийн нэр. In Э. Эмхэтгэгч (Ed.), Номын нэр (pp. хуудас). Хэвлэлийн газар.

Вэб хуудас:
Зохиогч, А. А. (Он, Сар Өдөр). Хуудасны нэр. Сайтын нэр. URL
```

- Өгүүлэл, номын нэрийг өгүүлбэрийн том үсгээр (зөвхөн эхний үг, оноосон нэр).
- 20 хүртэлх зохиогчийг бүгдийг; 21 ба түүнээс дээш бол эхний 19, «...», сүүлийн зохиогч.
- Огноогүй бол (n.d.); монгол бичвэрт (о.з.) гэж бичих эсэхийг сэтгүүлээс асуу.

### Vancouver

**Бичвэр дотор:** дөрвөлжин хаалтад, цэг, таслалын өмнө: «... нөлөө илэрсэн [1].», «... [3—5]», «... [1, 3, 5—7]».

**Ном зүй:**

```
Сэтгүүлийн өгүүлэл:
1. Зохиогч АА, Зохиогч ББ, Зохиогч ВВ. Өгүүллийн нэр. Сэтгүүлийн товчилсон нэр. Он;Боть(Дугаар):хуудас.

Ном:
2. Зохиогч АА. Номын нэр. Хэвлэл. Хэвлэсэн газар: Хэвлэлийн газар; Он.

Цахим эх сурвалж:
3. Зохиогч АА. Хуудасны нэр [Internet]. Газар: Нийтлэгч; Он [cited Огноо]. Available from: URL
```

- 6-аас олон зохиогч бол эхний 6, дараа нь «et al.» (монгол бичвэрт «нар» эсвэл «бусад»; сэтгүүлийн жишээг мөрд).
- Сэтгүүлийн нэрийг PubMed-ийн товчлолоор.

### AMA 11

**Бичвэр дотор:** дээд индекс тоо цэг, таслалын ард: «... нөлөө илэрсэн.¹», «... ³⁻⁵».

**Ном зүй:**

```
1. Зохиогч АА, Зохиогч ББ, Зохиогч ВВ. Өгүүллийн нэр. Сэтгүүлийн нэр. Он;Боть(Дугаар):хуудас. doi:xx.xxxx
```

6-аас олон зохиогч бол эхний 3, дараа нь «et al».

### IEEE

**Бичвэр дотор:** [1], [2]; олон бол [1]—[3] эсвэл [1], [4].

**Ном зүй:**

```
[1] А. А. Зохиогч, Б. Б. Зохиогч, "Өгүүллийн нэр," Сэтгүүлийн товчилсон нэр, vol. X, no. X, pp. XX—XX, Сар Он, doi: xx.xxxx.
```

### Chicago 17

- **Зүүлт, ном зүйн систем** (хүмүүнлэг): бичвэрт зүүлтийн дугаар, хуудасны доор бүтэн мэдээлэл, төгсгөлд цагаан толгойн ном зүй.
- **Зохиогч-он систем** (шинжлэх ухаан): (Бат 2023, 45), ном зүй APA-тай төстэй.

### «Лавай» (МУБИС)

Редакцын шаардлага:

- Зөвхөн өгүүлэлд иш татсан, ашигласан бүтээлийг оруулна.
- Зохиогчдын нэрийг цагаан толгойн дарааллаар.
- Эшлэл, зүүлтийн журмыг баримтална.

Редакцын жишээ (яг хэлбэрээр нь):

```
Эрдэнэбат. Ш., Хөгжмийн онолын сурах бичиг, Уб., 1971. 4-р тал.
```

Бүтэц: Нэр Овгийн үсэг., Бүтээлийн нэр, Хэвлэсэн газар (товчилсон)., Он. Хуудас.

Цэг, таслалыг редакцын жишээгээр мөрд. Бичвэр доторх эшлэлийн хэлбэрийг (зүүлт, хаалт) зөвлөмжид заагаагүй тул редакцаас тодруул.

### Монгол эх сурвалжийг эшлэх

#### Монгол хэлний сэтгүүлд

- Кирилл үсгээр, эх хэлбэрээр нь.
- Зохиогчийн нэрийг ном зүйд «Нэр О.» (Эрдэнэбат Ш.) эсвэл сэтгүүлийн заасан хэлбэрээр. Бичвэрт «Ш.Эрдэнэбат» эсвэл «Эрдэнэбат (1971)»: овгийн хураасан үсгийн ард цэг тавина (зөв бичих дүрмийн 48-р зүйл).
- Гадаад эх сурвалжийг эх хэлээр нь (латин үсгээр).
- Ном зүйд монгол, гадаад эх сурвалжийг тусад нь жагсаах эсэхийг сэтгүүлээс шалга.

#### Олон улсын сэтгүүлд

APA 7, Vancouver, AMA зэрэг стандарт латин бус бичгийн эх сурвалжийг галиглаж, нэрийн англи орчуулгыг дөрвөлжин хаалтад өгөхийг шаарддаг.

```
APA 7:
Erdenebat, Sh. (1971). Khögjmiin onolyn surakh bichig [Music theory textbook]. Ulaanbaatar.

Vancouver / NLM:
Erdenebat Sh. [Music theory textbook]. Ulaanbaatar; 1971. Mongolian.
```

- **Зохиогчийн нэр:** зохиогч өөрийн латин нэрээ тогтмол хэрэглэдэг бол (ORCID, өмнөх нийтлэл) түүнийг ав. Үгүй бол MNS 5217:2012-оор галигла.
- **Нэрийн дараалал:** монгол хүнийг олон улсын ном зүйд ихэвчлэн өөрийн нэрээр нь (Erdenebat Sh.) эрэмбэлдэг. Нэг өгүүлэлд тууштай байлга.
- **Хэлийг заах:** Vancouver, NLM-д төгсгөлд «Mongolian.», APA-д орчуулгыг [ ] хаалтад.
- Монгол бичгээр (үндэсний бичиг) бичигдсэн эх сурвалжийг кирилл галиг эсвэл латин галигаар өгөх эсэхийг сэтгүүлээс асуу.

### MNS 5217:2012 галиг

Монгол кирилл үсгийг латин үсгээр галиглах Монгол Улсын үндэсний стандарт.

| Кирилл | Латин | Кирилл | Латин | Кирилл | Латин |
|---|---|---|---|---|---|
| а | a | л | l | ф | f |
| б | b | м | m | х | kh |
| в | v | н | n | ц | ts |
| г | g | о | o | ч | ch |
| д | d | ө | ö | ш | sh |
| е | ye | п | p | щ | sh |
| ё | yo | р | r | ъ | i |
| ж | j | с | s | ы | y |
| з | z | т | t | ь | i |
| и | i | у | u | э | e |
| й | i | ү | ü | ю | yu |
| к | k |  |  | я | ya |

Жишээ: Эрдэнэбат → Erdenebat; Хөгжмийн онолын сурах бичиг → Khögjmiin onolyn surakh bichig; Улаанбаатар → Ulaanbaatar.

Анхаар: ö, ü тэмдэгтийг зарим систем дэмжихгүй; сэтгүүл, мэдээллийн сан (Scopus, Web of Science)-д бүртгэлтэй хэлбэрийг давуу үз.

### DOI

- Өгүүлэлд олгосон байнгын танигч (жишээ нь 10.1000/xyz123).
- Байгаа бол үргэлж оруул; хэлбэр нь стандартаас хамаарна: APA-д https://doi.org/..., AMA-д doi:..., Vancouver-д сонголтоор.
- DOI зохиохгүй; мэдэхгүй бол орхи.

### Нийтлэг дүрэм

- Анхдагч эх сурвалжийг эшил; хоёрдогч эх сурвалжаар дамжсан бол «(... -аас эшилсэн)».
- Идэвхтэй хөгжиж буй салбарт сүүлийн 5—10 жилийн судалгааг оруул.
- Эшлэлийг удиртгал, хэлэлцүүлэгт тэнцвэртэй байрлуул.
- Эшлэл бүрийг эх бүтээлтэй нь тулга: зохиогчийн нэрийн бичлэг, он, боть, хуудас.
- Ном зүй удирдах программ (Zotero, Mendeley, EndNote) хэрэглэвэл монгол нэрийн бичлэгийг гараар шалга.
- Хэвлэгдээгүй бүтээл, хувийн яриаг ном зүйд биш, зөвхөн бичвэрт дурд (MJER-ийн шаардлага).

### Тусгай төрөл

- **Препринт:** препринтийн сервер, DOI, «препринт» гэсэн тэмдэглэл.
- **Диссертаци:** зохиогч, он, нэр, зэрэг (докторын, магистрын), сургууль, хот.
- **Хурлын илтгэл:** зохиогч, нэр, хурлын нэр, газар, огноо, хуудас.
- **Программ хангамж, код:** нэр, хувилбар, хөгжүүлэгч, он, URL эсвэл DOI.
- **Өгөгдлийн сан:** зохиогч, он, нэр, хувилбар, сан, DOI.
- **Хууль тогтоомж:** хуулийн нэр, батлагдсан он, legalinfo.mn-ийн холбоос; зүйл, заалтыг бичвэрт.

### Стандарт хооронд шилжүүлэх

1. Бичвэр доторх хэлбэрийг солих (тоо ↔ зохиогч-он).
2. Ном зүйг дахин эрэмбэлэх (эшилсэн дараалал ↔ цагаан толгой).
3. Зохиогчийн нэр, нэрийн том үсэг, сэтгүүлийн нэрийн товчлол, DOI-ийн хэлбэрийг солих.
4. Монгол эх сурвалжийн хэлбэрийг (кирилл ↔ галиг + орчуулга) шилжүүлэх.

### Илгээхийн өмнөх шалгах хуудас

- [ ] Бичвэрийн эшлэл бүр ном зүйд, ном зүйн бүтээл бүр бичвэрт байгаа
- [ ] Стандарт сэтгүүлийн шаардлагатай таарсан
- [ ] Зохиогчийн нэр, он, боть, хуудас эх бүтээлтэй таарсан
- [ ] Монгол эх сурвалжийн хэлбэр нэг загвартай (кирилл эсвэл галиг)
- [ ] DOI байгаа газар оруулсан, зохиосон DOI байхгүй
- [ ] «[эшлэл шаардлагатай]», «[он?]» тэмдэглэгээ үлдээгүй

---

# Reference: references/mn/zurag-husnegt.md

## Зураг, хүснэгт

Эх сурвалж: K-Dense «Figures and Tables Best Practices» (references/figures_tables.md)-ийн монгол буулгалт; Монголын эдийн засгийн тойм (MJER) сэтгүүлийн зохиогчид өгөх заавар.

### Зураг уу, хүснэгт үү, бичвэр үү

**Мэдээллийг 1—2 өгүүлбэрээр хэлж болох уу?**

- Болно → зөвхөн бичвэр.
- Болохгүй, яг утга хэрэгтэй → хүснэгт.
- Болохгүй, хандлага, хамаарал чухал → зураг.

| Хүснэгт | Зураг |
|---|---|
| Уншигч лавлах яг тоон утга | Цаг хугацааны хандлага |
| Олон хувьсагчийн нарийн харьцуулалт | Хамаарал, корреляци |
| Статистик загварын дэлгэрэнгүй гаралт (коэффициент, p-утга, итгэх завсар) | Бүлгүүдийн нүдэнд харагдах харьцуулалт |
| Оролцогчдын суурь шинж (нас, хүйс, онош) | Тархалт |
| Тун-хариу урвалын яг утга | Зураг (микроскоп, рентген), урсгалын бүдүүвч |

### Үндсэн зарчим

1. **Дангаараа ойлгогдох.** Зураг, хүснэгт бүр үндсэн бичвэргүйгээр ойлгогдоно: бүрэн тайлбар; бүх товчлолыг тайлбарт эсвэл зүүлтэд задалсан; хэмжих нэгж; түүврийн хэмжээ (n); статистик тэмдэглэгээний тайлбар; олон цуваатай зурагт тайлбар (legend).
2. **Давхардуулахгүй.** Бичвэр хүснэгтийн гол үр дүнг онцолно, бүх тоог давтахгүй.

   ```
   Муу: «А бүлгийн дундаж нас 45.2, Б бүлгийнх 47.8 байв. А бүлгийн БЖИ 26.3, Б бүлгийнх 28.1...»
   (Хүснэгт 1-д мөн байгаа)

   Сайн: «Бүлгүүдийн суурь шинж ижил төстэй байв (Хүснэгт 1); нас, БЖИ, даралтын хувьд
   ач холбогдолтой ялгаа илрээгүй (бүгд p > 0.15).»
   ```

3. **Тууштай.** Бүх зураг, хүснэгтэд ижил фонт, өнгө, нэр томьёо, товчлол, тэнхлэгийн нэр, нэгж, статистик тэмдэглэгээ. Нэг зурагт «стандарт алдаа», нөгөөд «SE» гэж бичихгүй.
4. **Зохистой тоо.** 1000 үг тутамд нэг зураг эсвэл хүснэгт орчим: 3000—4000 үгтэй өгүүлэлд 3—4. MJER-д нийт 8-аас хэтрэхгүй.
5. **Энгийн.** Нэг зурагт хэт олон хувьсагч бүү оруул; эцсийн хэмжээнд 8—10 пунктаас багагүй фонт; илүүдэл тор, хүрээ, чимэглэлгүй.

### Зургийн төрөл

| Төрөл | Хэзээ |
|---|---|
| Баганан график | Тусдаа ангиллыг харьцуулах |
| Шугаман график | Цаг хугацааны хандлага |
| Цэгэн график | Хоёр тоон хувьсагчийн хамаарал |
| Хайрцган график | Тархалт, хэт утга |
| Дулааны зураг (heatmap) | Матриц, нөхцөл бүрийн хэв шинж |
| Ой модны график (forest plot) | Мета-шинжилгээ, олон бүлгийн нөлөөний хэмжээ |
| Урсгалын бүдүүвч | CONSORT, PRISMA, судалгааны явц |
| Зураг (микроскоп, гель) | Хэмжүүрийн шугам (scale bar) заавал |

### Хүснэгтийн бүтэц

1. **Дугаар, нэр** (хүснэгтийн дээр)
2. **Баганын толгой** (нэгжийг хаалтад)
3. **Мөрийн нэр**
4. **Өгөгдлийн нүд** (зохих нарийвчлалтай)
5. **Зүүлт** (доор нь: товчлол, статистик, тэмдэглэл)

Аравтын бутархайг баганад тэгшил; дундажид ихэвчлэн 1—2 орон; «хамаарахгүй» бол урт зураас (—); боломжтой бол яг p-утга (p = 0.032).

**Жишээ:**

```
Хүснэгт 1. Оролцогчдын суурь шинж

Шинж                    Оролцох бүлэг (n = 50)   Хяналтын бүлэг (n = 48)   p
──────────────────────────────────────────────────────────────────────────────
Нас, жил                 45.3 ± 8.2               47.1 ± 9.1                0.28
Эрэгтэй, n (%)           28 (56)                  25 (52)                   0.71
БЖИ, кг/м²               26.3 ± 3.8               27.1 ± 4.2                0.32
Тамхи татдаг, n (%)      12 (24)                  15 (31)                   0.42
Систолын даралт, мм м.у.б 132 ± 15                134 ± 18                  0.54
──────────────────────────────────────────────────────────────────────────────
Өгөгдлийг дундаж ± стандарт хазайлт эсвэл n (%)-иар үзүүлэв. Тасралтгүй хувьсагчид
бие даасан t тест, ангиллын хувьсагчид χ² тест хэрэглэв. БЖИ = биеийн жингийн индекс.
```

Тоо нь зөвхөн хэлбэрийг харуулна.

**Түгээмэл алдаа:** хэт олон мөр, багана; нэгж, товчлолын тайлбаргүй; хэт нарийвчлал (p-утгад 5 орон); түүврийн хэмжээгүй; шаардлагатай харьцуулалтгүй; хүснэгт хоорондын хэлбэр зөрүүтэй; зураг, бичвэртэй давхардсан.

### Статистик үзүүлэх

Харьцуулалт бүрт: цэгэн үнэлгээ (дундаж, медиан, хувь); хэлбэлзлийн хэмжүүр (стандарт хазайлт, стандарт алдаа, итгэх завсар); түүврийн хэмжээ (n); тестийн статистик (t, F, χ²); p-утга; шаардлагатай бол нөлөөний хэмжээ.

| Алдааны шугам | Утга | Хэзээ |
|---|---|---|
| Стандарт хазайлт (СХ, SD) | Өгөгдлийн тархалт | Тархалтыг харуулах |
| Дунджийн стандарт алдаа (SEM) | Дунджийн үнэлгээний нарийвчлал | Хэмжилтийн нарийвчлал |
| 95% итгэх завсар (ИЗ, CI) | Жинхэнэ дунджийг агуулах магадлалтай муж | Статистик ач холбогдол |

Аль хэмжүүрийг харуулснаа тайлбарт заавал бич: «Алдааны шугам 95% итгэх завсрыг харуулна.»

Ач холбогдлын тэмдэглэгээ: * p < 0.05; ** p < 0.01; *** p < 0.001; а.х.б. (ач холбогдолгүй). Зураг, хүснэгт бүрийн тайлбарт тэмдэглэгээг тайлбарла.

### Хүртээмж

- Өнгөт сохрол бүхий хүнд ялгагдах өнгө (цэнхэр-улбар шар, viridis); улаан-ногоон хослолоос зайлсхий.
- Зөвхөн өнгөөр ялгахгүй: хээ, хэлбэр, шошго нэм.
- Зургийг саарал өнгөнд шалга.
- Шугамын зузаан 0.5—1 пунктаас багагүй.

### Техникийн шаардлага

- **Вектор формат** (график, бүдүүвч): PDF, EPS, SVG.
- **Растер формат** (гэрэл зураг): TIFF, PNG; өгөгдлийн зурагт JPEG-ээс зайлсхий (MJER 300 dpi JPEG шаарддаг тул сэтгүүлийн шаардлагыг давуу үз).
- **Нягтрал:** шугаман зураг 300—600 dpi, гэрэл зураг 300 dpi.
- **Хэмжээ:** нэг баганад 8—9 см, хоёр баганад 17—18 см; сэтгүүлийн шаардлагыг шалга.
- **Зураг засварлах:** бүх зурагт жигд гэрэлтүүлэг, тодосгогч, тайрах, эргүүлэхийг зөвшөөрнө. Хэсэгчлэн засах, арилгах, наалдуулах зэрэг өгөгдлийг гуйвуулах засвар хориотой. Хийсэн засвараа арга зүйд бич.

### Дугаарлалт, бичвэрт дурдах

- Бичвэрт анх дурдсан дарааллаар араб тоогоор: Зураг 1, Зураг 2; Хүснэгт 1, Хүснэгт 2 (зураг, хүснэгтийг тусад нь дугаарлана). Хавсралтад: Зураг Х1, Хүснэгт Х1.
- Бичвэрт: «Үр дүнг Зураг 1-д харуулав.», «Оролцогчдын шинжийг Хүснэгт 2-т үзүүлэв.», «(Зураг 3—5)».
- «Доорх зураг», «дээрх хүснэгт» гэж бичихгүй (хуудаслалт өөрчлөгдөж болно); дугаараар нь дурд.

### Тайлбар (caption)

**Байрлал:** монгол сэтгүүлд ихэвчлэн зургийн тайлбар зургийн доор, хүснэгтийн нэр хүснэгтийн дээр (MJER: «Зураг 1.» доор нь 10 пунктаар, «Хүснэгт 1.» дээр нь). Сэтгүүлийн шаардлагыг мөрд.

**Зургийн тайлбар:**

```
Зураг 1. [Нэг өгүүлбэрт нэр]. [Нэмэлт тайлбар: товчлол, хэсэг (А, Б), статистик тест,
түүврийн хэмжээ].
```

**Агуулга:** юуг харуулж байгаа; дэлгэрэнгүй тайлбар; бүх товчлол, тэмдэг; түүврийн хэмжээ; статистик тест; алдааны шугам, тэмдэглэгээний утга; хэсгийн тайлбар.

**Жишээ:**

```
Зураг 3. Эмчилгээний 12 долоо хоногт танин мэдэхүйн гүйцэтгэл сайжирсан. (А) Эмчилгээний
(цэнхэр), хуурмаг эмийн (саарал) бүлгийн MMSE-ийн дундаж оноо эхэнд, 6, 12 дахь долоо хоногт.
(Б) Эмчилгээний бүлгийн оролцогч тус бүрийн өөрчлөлт. Алдааны шугам 95% итгэх завсрыг
харуулна. * p < 0.05, ** p < 0.01, *** p < 0.001 (давтан хэмжилтийн ANOVA, Бонферрони
засвартай). n = 42 (эмчилгээ), n = 40 (хуурмаг эм). MMSE (Mini-Mental State Examination)
0—30 оноотой, өндөр оноо сайн гүйцэтгэлийг илэрхийлнэ.
```

### Илгээхийн өмнөх шалгах хуудас

- [ ] Бүх зураг, хүснэгт зөв дугаарлагдсан, бичвэрт дарааллаар дурдагдсан
- [ ] Тайлбар бүрэн, дангаараа ойлгогдохуйц
- [ ] Товчлол бүр тайлбарлагдсан
- [ ] Формат, нягтрал, хэмжээ сэтгүүлийн шаардлагатай таарсан
- [ ] Өнгөт сохролд ялгагдахуйц
- [ ] Бусдын бүтээлээс авсан бол зөвшөөрөл авч, эх сурвалжийг заасан
- [ ] Бичвэр, хүснэгт, зургийн тоо хоорондоо таарсан
- [ ] Өгөгдлөөс бус, зохиосон зураг, график байхгүй

---

# Reference: references/mn/tailagnah-udirdamj.md

## Тайлагнах удирдамж

Эх сурвалж: K-Dense «Reporting Guidelines for Scientific Studies» (references/reporting_guidelines.md)-ийн монгол буулгалт; CONSORT 2025 мэдэгдэл (Hopewell нар, PLoS Medicine, 2025, 22(4):e1004587).

Тайлагнах удирдамж бол судалгааны төрөл бүрт өгүүлэлд заавал байх ёстой мэдээллийн хяналтын хуудас. Удирдамж мөрдөх нь судалгааг ил тод, давтан хийх боломжтой болгож, рецензентийн «мэдээлэл дутуу» гэсэн татгалзлаас сэргийлнэ. Олон сэтгүүл хяналтын хуудсыг өгүүлэлтэй хамт илгээхийг шаарддаг.

Удирдамжийг өгүүлэл бичиж дуусаад биш, **судалгааг төлөвлөх шатнаас** мөрд: дараа нь цуглуулаагүй өгөгдөл дутуу болохоос сэргийлнэ.

Удирдамж бүрийн албан ёсны хяналтын хуудас, тайлбарыг EQUATOR Network (https://www.equator-network.org/)-ээс ав. Хувилбар шинэчлэгддэг тул илгээхийн өмнө хамгийн сүүлийн хувилбарыг шалга.

### Судалгааны загвараар сонгох

| Загвар | Удирдамж | Сүүлийн хувилбар |
|---|---|---|
| Санамсаргүй хяналттай туршилт (RCT) | CONSORT | 2025 (30 зүйл) |
| Туршилтын протокол | SPIRIT | 2025 |
| Ажиглалтын судалгаа: когорт, тохиолдол-хяналт, хөндлөн огтлол | STROBE | 2007 (22 зүйл) |
| Системчилсэн тойм, мета-шинжилгээ | PRISMA | 2020 (27 зүйл) |
| Оношилгооны шинжилгээний нарийвчлал | STARD | 2015 |
| Таамаглах, оношлох загвар | TRIPOD | TRIPOD+AI (2024) |
| Амьтны in vivo судалгаа | ARRIVE | 2.0 (2020) |
| Тохиолдлын тайлан, цуврал | CARE | 2013 |
| Эрүүл мэндийн чанарыг сайжруулах | SQUIRE | 2.0 (2015) |
| Эрүүл мэндийн эдийн засгийн үнэлгээ | CHEERS | 2022 |
| Чанарын судалгаа | SRQR | 2014 |

Олон загвар хослуулсан бол (жишээ нь туршилт + эдийн засгийн үнэлгээ) хоёр удирдамжийг хамт мөрд.

Англи лавлах файлыг (references/reporting_guidelines.md) CONSORT 2025, SPIRIT 2025, TRIPOD+AI 2024-өөр шинэчилсэн. Аль ч удирдамжийн албан ёсны хяналтын хуудсыг мөрд.

### CONSORT: санамсаргүй хяналттай туршилт

**Бүрдэл:** хяналтын хуудас, оролцогчдын урсгалын бүдүүвч.

**Гол зүйл (CONSORT 2010-ын үндсэн зүйлүүд, монгол тайлбартай):**

1. Гарчигт санамсаргүй туршилт гэдгийг заах
2. Бүтэцлэгдсэн хураангуй
3. Шинжлэх ухааны суурь, үндэслэл
4. Тодорхой зорилго, таамаглал
5. Туршилтын загвар (зэрэгцээ, солбицсон, хүчин зүйлийн)
6. Оролцогчийг сонгох шалгуур
7. Өгөгдөл цуглуулсан газар, байршил
8. Давтан хийхэд хангалттай нарийн тайлбарласан арга хэмжээ (интервенц)
9. Гол ба туслах үр дагаврын тодорхойлолт
10. Түүврийн хэмжээ, чадлын тооцоо
11. Санамсаргүй дарааллыг үүсгэсэн арга
12. Хуваарилалтыг нууцалсан арга
13. Далдлалт (blinding)
14. Статистик арга
15. Оролцогчдын урсгал, гарсан шалтгаан
16. Элсүүлэлт, ажиглалтын хугацаа
17. Суурь шинжийн хүснэгт
18. Үр дагавар бүрийн шинжилгээний үр дүн
19. Хор уршиг, гаж нөлөө
20. Туршилтын хязгаарлалт
21. Нийтлэг дүгнэлтэд хамааруулах боломж
22. Үр дүнтэй нийцсэн тайлбар
23. Туршилтын бүртгэлийн дугаар
24. Бүтэн протоколын хүртээмж
25. Санхүүжилтийн эх үүсвэр

**CONSORT 2025-ын шинэ зүйл:** нээлттэй шинжлэх ухааны хэсэг (туршилтын бүртгэл; протокол, статистик шинжилгээний төлөвлөгөөний хүртээмж; өгөгдөл хуваалцах; санхүүжилт, ашиг сонирхлын зөрчил); өвчтөн, олон нийтийн оролцоо; судалгааны газар, арга хэмжээ хэрэгжүүлэгчийг сонгох шалгуур; хор уршгийг хэрхэн үнэлсэн; шинжилгээний хүн ам, дутуу өгөгдлийн боловсруулалт; арга хэмжээний хэрэгжилт, хавсарсан эмчилгээ.

**Урсгалын бүдүүвч (монгол нэр томьёо):**

```
Шалгуурт тэнцэх эсэхийг үнэлсэн (n = ...)
    ↓
Хассан (n = ...)
  • Шалгуур хангаагүй (n = ...)
  • Оролцохоос татгалзсан (n = ...)
  • Бусад шалтгаан (n = ...)
    ↓
Санамсаргүйгээр хуваарилсан (n = ...)
    ├──────────────────────┐
    ↓                      ↓
Оролцох бүлэгт          Хяналтын бүлэгт
хуваарилсан (n = ...)    хуваарилсан (n = ...)
    ↓                      ↓
Ажиглалтаас гарсан       Ажиглалтаас гарсан
(n = ..., шалтгаан)      (n = ..., шалтгаан)
    ↓                      ↓
Шинжилгээнд              Шинжилгээнд
хамруулсан (n = ...)     хамруулсан (n = ...)
```

Дөрвөн шат: элсүүлэлт, хуваарилалт, ажиглалт, шинжилгээ. Шат бүрт тоо, хассан шалтгааныг бич.

### STROBE: ажиглалтын судалгаа

- **Когорт:** өртсөн, өртөөгүй бүлгийг цаг хугацааны дагуу ажиглана.
- **Тохиолдол-хяналт:** өвчтэй, өвчгүй хүмүүсийн өмнөх өртөлтийг харьцуулна.
- **Хөндлөн огтлол:** өртөлт, үр дагаврыг нэг зэрэг хэмжинэ.

**22 зүйл:** гарчиг, хураангуйд загварыг заах; суурь, үндэслэл; зорилго; загвар, үндэслэл; газар, байршил, огноо; сонгох шалгуур, арга; хувьсагчийн тодорхойлолт (үр дагавар, өртөлт, төөрөгдүүлэгч хүчин зүйл); өгөгдлийн эх үүсвэр, хэмжих арга; хазайлтыг бууруулах арга; түүврийн хэмжээний үндэслэл; тоон хувьсагчийн боловсруулалт; төөрөгдүүлэгч хүчин зүйл, харилцан нөлөөг тооцсон статистик арга; мэдрэг байдлын шинжилгээ; оролцогчдын урсгал, оролцоогүй шалтгаан; ажиглалтын хугацаа зэрэг дүрслэх өгөгдөл; үр дагаврын өгөгдөл; тохируулаагүй ба тохируулсан үнэлгээ; дэд бүлгийн болон бусад шинжилгээ; гол үр дүнгийн хураангуй; хазайлтын боломжтой хязгаарлалт; тайлбар, нийтлэг дүгнэлтэд хамааруулах боломж; санхүүжилт, санхүүжүүлэгчийн үүрэг.

Хэлэлцүүлэгт ажиглалтын судалгаа учир шалтгааныг тогтоохгүй гэдгийг тодорхой бич: «нөлөөлсөн» биш «холбоотой байв».

### PRISMA: системчилсэн тойм, мета-шинжилгээ

**27 зүйл, урсгалын бүдүүвч.**

- **Гарчиг:** системчилсэн тойм, мета-шинжилгээ гэдгийг заах.
- **Арга зүй:** хамруулах шалгуур; мэдээллийн эх үүсвэр (сан, огноо); хайлтын бүтэн стратеги (дор хаяж нэг сангийнх); сонгох, өгөгдөл цуглуулах явц; хазайлтын эрсдэлийн үнэлгээ; нөлөөний хэмжүүр; нэгтгэх арга; тайлагналын хазайлт; нотолгооны итгэлцлийн үнэлгээ (GRADE г.м.).
- **Үр дүн:** сонголтын урсгалын бүдүүвч; судалгаануудын шинж; хазайлтын эрсдэл; нэгтгэлийн үр дүн; нотолгооны итгэлцэл.
- **Урсгалын шат:** илрүүлсэн (сан, бүртгэлээс) → давхардлыг хассан → шүүсэн, хассан → бүтэн бичвэрээр үнэлсэн → хамруулсан.

Монгол хэлний эх сурвалжийг хамруулах бол хайсан монгол сан (номын сангийн каталог, mongoliajol.info г.м.)-гаа арга зүйд нэрлэ.

### Бусад удирдамж (товч)

- **SPIRIT:** туршилтын протоколын бүх бүрдэл (зорилго, загвар, оролцогч, арга хэмжээ, үр дагавар, хуваарь, түүврийн хэмжээ, хуваарилалт, далдлалт, өгөгдөл, ёс зүй).
- **STARD:** оношилгооны шинжилгээний нарийвчлал: лавлах стандарт, оролцогчдын урсгал, мэдрэг байдал, өвөрмөц байдал, итгэх завсар.
- **TRIPOD:** таамаглах загвар боловсруулах, баталгаажуулах: таамаглагч, үр дагаврын тодорхойлолт, загварын гүйцэтгэл (ялгах чадвар, тохирц). Хиймэл оюун, машин сургалтын загварт TRIPOD+AI.
- **ARRIVE:** амьтны зүйл, омог, нас, хүйс, тэжээх нөхцөл, санамсаргүй хуваарилалт, далдлалт, түүврийн хэмжээ, ёс зүйн зөвшөөрөл.
- **CARE:** тохиолдлын цаг хугацааны дараалал, онош, эмчилгээ, үр дагавар, өвчтөний зөвшөөрөл.
- **SQUIRE:** чанарыг сайжруулах ажлын нөхцөл, арга хэмжээ, хэмжүүр, үр дүн.
- **CHEERS:** эдийн засгийн үнэлгээний хэтийн төлөв, хугацаа, зардал, үр дагавар, загвар, мэдрэг байдлын шинжилгээ.
- **SRQR:** чанарын судалгааны арга зүйн хандлага, судлаачийн байр суурь, түүвэрлэлт, өгөгдөл цуглуулах, шинжлэх арга, итгэл үнэмшил.

### Хэрхэн ашиглах

1. **Төлөвлөх шатанд:** загвартаа тохирох удирдамжийг сонгож, хяналтын хуудсаар ямар өгөгдөл цуглуулахаа төлөвлө.
2. **Бичих шатанд:** хэсэг бүрийг бичихдээ хяналтын хуудсын зүйлийг нэг нэгээр нь шалга.
3. **Илгээхийн өмнө:** зүйл бүрт өгүүллийн хуудас, мөрийн дугаарыг бөглө; хамааралгүй зүйлд «хамаарахгүй» гэж бич, хоосон бүү орхи.

Арга зүйд мэдэгдэл бичих жишээ: «Энэ өгүүллийг STROBE удирдамжийн дагуу тайлагнав (хяналтын хуудсыг хавсралт 1-д үзүүлэв).»

### Түгээмэл алдаа

1. Удирдамж огт мөрдөөгүй.
2. Өгүүлэл бичиж дууссаны дараа л удирдамж харсан (шаардлагатай өгөгдөл цуглуулаагүй байх).
3. Хяналтын хуудсыг дутуу бөглөсөн.
4. Хуучирсан хувилбар хэрэглэсэн.
5. Загварт тохирохгүй удирдамж сонгосон.
6. Сэтгүүл шаардсан хяналтын хуудсыг илгээгээгүй.
7. Ерөнхий, нарийн бус тайлагнал («стандарт аргаар» гэх мэт).

### Шалгах хуудас

- [ ] Судалгааны загварт тохирох удирдамжийг сонгосон
- [ ] Хамгийн сүүлийн хувилбарыг EQUATOR-оос татсан
- [ ] Зүйл бүрт хуудас, мөрийн дугаар бөглөсөн
- [ ] Урсгалын бүдүүвч (CONSORT, PRISMA, STARD) тоотой
- [ ] Туршилтын бүртгэлийн дугаар (шаардлагатай бол)
- [ ] Ёс зүйн зөвшөөрлийн мэдэгдэл
- [ ] Удирдамж мөрдсөн тухай мэдэгдэл арга зүйд

---

# Reference: references/mn/setguul-shaardlaga.md

## Монгол сэтгүүлийн шаардлага

Сэтгүүл бүр өөрийн зохиогчид өгөх заавартай. Энэ файлд хоёр жишээ сэтгүүлийн шаардлагыг нэгтгэв. Өөр сэтгүүлд илгээх бол хэрэглэгчээс тухайн сэтгүүлийн зааврыг асууж, түүнийг мөрд. Заавар шинэчлэгддэг тул илгээхийн өмнө сэтгүүлийн цахим хуудаснаас сүүлийн хувилбарыг шалга.

### «Лавай» (МУБИС)

Эх сурвалж: МУБИС-ийн «Лавай» эрдэм шинжилгээний бичгийн «Судалгааны өгүүлэл бичих зөвлөмж» (nairuulga.mn; хэрэглэгчийн хавсаргасан эх).

#### Нэг. Судалгааны өгүүллийн бүтэц

1. **Сэдэв буюу гарчиг.** Үндсэн бичвэрээс өөр фонтоор, бүгдийг том үсгээр. Өгүүллийн гол санааг агуулсан товч, тодорхой, оновчтой томьёолол.
2. **Зохиогчийн хаяг.** Ажил, албан тушаал, цол зэрэг, овог, нэр. Хэвлэлийн шаардлага хангасан зураг ирүүлнэ.
3. **Хураангуй (Abstract).** Судалгааны агуулгын гол утга санааг товч, тодорхой, ойлгомжтой; орос, англи хэлээр 8—12 мөр.
4. **Түлхүүр үг.** Өгүүллийн цөм утгыг илэрхийлж чадахуйц цөөн тооны нэр үг, холбоо үг.
5. **Удиртгал.** Судалгааны арга, зорилго, зорилт, хэрэгцээ шаардлага, дэвшүүлж буй асуудал, таамаглал; түүнийг батлахын тулд ямар сорил, туршилтыг ямар аргаар хэрхэн гүйцэтгэсэн; хэчнээн хэмжээний материал, мэдээлэл хуримтлуулсан; ямар аргаар боловсруулсан.
6. **Үндсэн хэсэг.** Өөрийн үр дүнг бусад судлаачийн үр дүн, онол, арга зүйн чиглэл, үзэл баримтлалтай хэрхэн холбогдох; таамаглалаа хэрхэн баталсан эсвэл үгүйсгэсэн; ямар дүгнэлтэд хүрсэн. Эшлэл, баримт, нотолгоотой. Тоон үзүүлэлтэд заавал математик боловсруулалт хийнэ.
7. **Судалгааны үр дүн.** Өөрийн гаргасан үр дүнг баталгаатай, логик дараалал сайтай, эмх цэгцтэй, ойлгомжтой.
8. **Судалгааны хязгаарлагдмал байдал.** Судалгаа хязгаарлагдмал хүрээнд явагддаг тул энэ талаар дурдана. Ямар асуудлыг аль талаас нь хөндсөн, цаашид ямар чиглэлээр судлах боломжтой.
9. **Дүгнэлт.** Үр дүнд гаргасан дүгнэлтүүдийг логик дэс дараатай, оновчтой, тодорхой.
10. **Иш татсан бүтээл, ашигласан материал.** Зөвхөн өгүүлэлд иш татсан, ашигласан бүтээл. Эшлэл, зүүлтийн журмыг баримтална.

#### Хоёр. Бүтээлд тавих шаардлага

**А. Техникийн шаардлага:**

| Үзүүлэлт | Шаардлага |
|---|---|
| Фонт | Times New Roman |
| Үсгийн хэмжээ | 10 |
| Мөр хоорондын зай | 1 (Single) |
| Цаас | A4 (210 × 297 мм) |
| Захын зай | Дээд 1.5 см, доод 1.5 см, зүүн 3 см, баруун 1.5 см |
| Бичвэрийн өндөр | 24 см |
| Хэмжээ | Эх зөвлөмжид «1хх-аас хэтрэхгүй» гэж бичсэн; утгыг (хэвлэлийн хуудас эсэх) редакцаас тодруул |
| Нэмэлт | Ном зүй, ашигласан бүтээлийн жагсаалт, хавсралттай байж болно |

**Б. Өгүүлэлд тавих шаардлага:**

- Шинжлэх ухааны зохих түвшинд бичигдсэн
- Тухайн салбарын онол, практикийн тулгамдсан асуудлыг хөндсөн
- Агуулга нь сэдэвтэйгээ уялдсан
- Эрдэм шинжилгээний хэл найруулгын шаардлагыг хангасан
- Шинэ санаа дэвшүүлсэн
- Тулгамдсан асуудлыг дэвшүүлсэн эсвэл шинэ туршилт, судалгааг нэвтрүүлсэн
- Эшлэл, зүүлтийг зохих журмын дагуу хийсэн
- Дүн шинжилгээ хийж тодорхой дүгнэлт гаргасан
- Зөв бичих, найруулгын алдаагүй

**В. Ном зүйд тавих шаардлага:**

Зохиогчдын нэрийг цагаан толгойн дарааллаар. Редакцын жишээ:

```
Эрдэнэбат. Ш., Хөгжмийн онолын сурах бичиг, Уб., 1971. 4-р тал.
```

#### «Лавай»-д илгээхийн өмнөх шалгах хуудас

- [ ] Гарчиг бүгд том үсгээр, өөр фонтоор
- [ ] Зохиогчийн ажил, албан тушаал, цол зэрэг, овог нэр, зураг
- [ ] Орос, англи хураангуй 8—12 мөр
- [ ] Түлхүүр үг
- [ ] Удиртгалд арга, зорилго, таамаглал, материалын хэмжээ, боловсруулалтын арга
- [ ] Үндсэн хэсэгт бусдын судалгаатай харьцуулалт, эшлэл
- [ ] Тоон үзүүлэлтэд математик боловсруулалт
- [ ] Судалгааны хязгаарлагдмал байдлын тусдаа хэсэг
- [ ] Ном зүй цагаан толгойн дарааллаар, редакцын хэлбэрээр
- [ ] Times New Roman 10, мөр хоорондын зай 1, A4, захын зай 1.5/1.5/3/1.5 см
- [ ] Зөв бичих, найруулгын алдаагүй

### Монголын эдийн засгийн тойм (MJER)

Эх сурвалж: mongoliajol.info дээрх MJER-ийн зохиохчид өгөх заавар (2026 оны 10 дугаар сард уншсан).

#### Бүтэц

Гарчиг (товчлолгүй; орон нутгийн судалгаанд улс, бүс нутгийг нэрлэх); зохиогчийн нэр, холбоо барих мэдээлэл, харьяалал (байгууллага, хот, улс; цол, шагналгүй); хураангуй, түлхүүр үг (англи, монгол); Удиртгал (бичвэрийн 5 орчим хувь); Арга зүй; Үр дүн; Хэлэлцүүлэг ба дүгнэлт; Ном зүй; Хавсралт (сонголтоор). Хэсгийг ром тоогоор дугаарлана. Удиртгал, Арга зүй, Үр дүн, Хэлэлцүүлэг, Ном зүй заавал.

#### Хураангуй, түлхүүр үг

- Хураангуй англи, монголоор 10—15 мөр: зорилго, асуудал, таамаглал, арга, үр дүн, дүгнэлт, ач холбогдол.
- 6—8 түлхүүр үг хоёр хэлээр, хураангуйн доор; ганц тоо, нэрлэхийн тийн ялгалаар; гарчгийн үгийг давтахгүй.

#### Хэлбэр

| Үзүүлэлт | Шаардлага |
|---|---|
| Хэмжээ | A4 10 хуудаснаас ихгүй; Word файлаар |
| Захын зай | Эхний 2 хуудас: дээд, доод 4.44 см, зүүн, баруун 2.5 см; бусад хуудас: дээд, доод 3.17 см, зүүн, баруун 2.5 см |
| Фонт | Times New Roman 12 |
| Толгой, хөл, зүүлт, хуудасны дугаар | Хэрэглэхгүй |
| Гарчиг | Үндсэн гарчиг 14 тод; хэсгийн гарчиг 12 тод, бүгд том үсгээр; дэд гарчиг 12 тод налуу |
| Зураг | 300 dpi JPEG, голлуулсан; тайлбар доор нь 10 пунктаар, «Зураг 1.» |
| Хүснэгт | Word-ын хүснэгтээр; нэр дээр нь «Хүснэгт 1.»; тэмдэглэл 9 налуу |
| Тэгшитгэл | Word-ын Equation-аар, голлуулсан, дугаар баруун талд хаалтад |
| Зураг, хүснэгтийн нийт тоо | 8-аас ихгүй |

#### Тоо, нэгж, товчлол

- Тоо, нэгжийн хооронд нэг зай (3 см); хувийг зайгүй (100%).
- 1—10 хүртэлх тоог үгээр, 11-ээс дээшийг цифрээр.
- Товчлолыг анх дурдахдаа бүтнээр нь; улсын нэрийг товчлохгүй.

#### Эшлэл

- Бичвэрт дөрвөлжин хаалтад, гарсан дарааллаар [1]; цэг тэмдэг хаалтын ард.
- Заавар «APA-ийн 7-р хувилбар» гэж заасан ч жишээ нь Vancouver маягтай; ном зүйн дараалал (эшилсэн дараалал эсвэл цагаан толгой), тод бичгийн шаардлага зааврын өөр өөр хэсэгт зөрүүтэй. Илгээхийн өмнө редакцаас тодруул.
- Хэвлэгдээгүй бүтээл, хувийн яриаг ном зүйд биш, зөвхөн бичвэрт.

#### Ёс зүй, хэл

- Нэг өгүүллийг олон сэтгүүлд зэрэг илгээхгүй; хэсэгчлэн хувааж нийтлэхгүй.
- Өмнө нийтлэгдсэн, дахин ашигласан материалыг мэдэгдэнэ.
- Бусдын бичвэр, өгөгдөл, онолыг эшлэлгүй хуулахгүй.
- Логик бүтэцтэй, стандарт нэр томьёотой, ярианы хэлгүй; нэгдүгээр биеийн төлөөний үгийг олон тоогоор («бид»).

### Сэтгүүлийн заавар байхгүй үед

Хэрэглэгч сэтгүүлээ хэлээгүй, эсвэл заавар олдохгүй бол:

1. IMRaD бүтэц, монгол гарчгаар (references/mn/butets.md).
2. Хураангуй 150—250 үг, нэг догол мөр; монгол, англи хэлээр.
3. 4—6 түлхүүр үг.
4. Эшлэлийн стандартыг салбараар (references/mn/eshlel.md): анагаахад Vancouver, нийгмийн ухаан, боловсролд APA 7.
5. Хэлбэрийн шаардлагыг (фонт, захын зай) тодорхой зааж чадахгүй гэдгээ хэл, зааврыг хэрэглэгчээс асуу.

### Ерөнхий шалгах хуудас

- [ ] Сэтгүүлийн зохиогчид өгөх зааврын сүүлийн хувилбарыг уншсан
- [ ] Бүтэц, гарчгийн нэр зааврынхтай таарсан
- [ ] Хураангуй, түлхүүр үг шаардсан хэл, хэмжээгээр
- [ ] Үг, хуудас, зураг, хүснэгтийн тоо хязгаарт багтсан
- [ ] Эшлэл, ном зүй шаардсан стандартаар
- [ ] Фонт, хэмжээ, захын зай, мөр хоорондын зай
- [ ] Ёс зүйн зөвшөөрөл, санхүүжилт, ашиг сонирхлын зөрчлийн мэдэгдэл
- [ ] Тайлагнах удирдамжийн хяналтын хуудас (шаардлагатай бол)
- [ ] Редакторт хандсан захидал (шаардлагатай бол)

---

# Reference: references/mn/mongol-nairuulga.md

## Шинжлэх ухааны монгол найруулга

Эх сурвалж: nairuulga.mn «Шинжлэх ухааны хэл найруулгын онцлог», «Амьсгал боосон "-лт" хэмээх хаалт», «Олон тооны дагавар эс авах тохиолын тухай», «Албан бичиг, хэвлэл мэдээллийн эхэд элбэг илэрч байгаа зөв бичих дүрмийн алдаатай зарим үгийг залруулъя!»; Монгол хэлний зөв бичих дүрэм (1983), Төрийн хэлний зөвлөлийн 2011 оны 01 дүгээр тогтоол; Монгол хэлний тухай хууль (2015), 6.5. Humanizer-MN ур чадварын лавлах файлаас товчлов.

### Шинжлэх ухааны найруулгын зорилго

Шинжлэх ухааны зохиолын гол үүрэг нь дэвшүүлсэн таамаглалынхаа үнэнийг батлах. Хэлний хэрэгсэл мэдээлэх, итгүүлэн батлах хоёр зорилгод үйлчилнэ. Шинжлэх ухаан логик дүгнэлтээр, уран зохиол уран дүрслэлээр үзүүлдэг (Белинский).

- Албан ёсны, төвийг сахисан өнгө аяс.
- Үгийг шууд утгаар, нэр томьёог нэг утгаар.
- Уран яруу хэрэглүүр, хувийн сэтгэгдэл, хошигнол хэрэглэхгүй. Шинжлэх ухааны сурталчилгааны зохиолд зохих хэмжээгээр болно.
- Ярианы хэлбэр («-чихсан», «ёстой» гэх мэт), этгээд үг хэрэглэхгүй.

### Гурван үндсэн шаардлага

1. **Учир шалтгааны дараалалтай.** Зохиолын доторх зүйлс нарийн дэс дараалалтай байрлаж, утгын хувьд нягт холбогдоно. Бүтэн эх төдийгүй хэсэг бүр дэс дараатай.
2. **Тодорхой.** Уншихад ойлгомжтой. Сурах бичгийг нийт уншигчдад, эрдэм шинжилгээний зохиолыг мэргэжлийн хүмүүст ойлгомжтой бичнэ.
3. **Оновчтой.** Санаагаа цөөн үгээр онож өгүүлнэ. Ухагдахуун нэг утгатай, тэмдэглэж буй зүйл ба тэмдэглэгдэж буй зүйл хоорондоо зөрөхгүй.

### Логикийн дөрвөн хууль

- **Адилтгалын хууль.** Өөр өөр бодлыг адилтгахгүй, адил бодлыг өөр өөр утгаар авахгүй. Нэг нэр томьёог ойролцоо үгээр солбин бичвэл нэг ойлголт хоёр утга авна.
- **Зөрчилгүйн хууль.** Үгүйсгэлцсэн хоёр бодомж нэг зэрэг үнэн байж чадахгүй. Хураангуй, үр дүн, дүгнэлт хоорондоо зөрчилдөж байгаа эсэхийг шалга.
- **Гурав дахийг үгүйсгэх хууль.** Зөрчилт хоёр бодомжийн нэг нь заавал үнэн. Тодорхой хариултаас зайлсхийж, байхгүй гуравдагч хувилбар эрэхгүй.
- **Хангалттай үндэслэлийн хууль.** Зөв бодол бүр хангалттай үндэслэлтэй. Эшлэлгүй «судлаачид үзэж байна», «олон судалгаагаар батлагдсан» мэт дүгнэлтийг хас эсвэл эх сурвалжийг нь заа.

### Нэр томьёо

- Боловсрол, шинжлэх ухаанд хэрэглэх нэр томьёог монгол хэлэнд хөрвүүлэн хэрэглэнэ (Монгол хэлний тухай хууль, 6.5).
- Монгол нэр томьёо байвал түүнийг хэрэглэ; анх дурдахдаа гадаад нэрийг хаалтад өг.
- Тогтсон нэр томьёог ойролцоо үгээр бүү соль.
- Төрийн хэлний зөвлөлийн 2011 оны тогтоолоор орчуулан хэрэглэх үгийн жишээ: потенциал → чадамж, сертификат → батламж, монитор → дэлгэц, комплекс → цогц, стресс → бухимдал, дарамт.
- Харь үгийг шаардлагагүй газар хэрэглэхгүй: менталитет → сэтгэлгээ, контент → агуулга, фокус → гол анхаарал, импакт → нөлөө.

### Түгээмэл алдаа

#### «-лт хийх» хаалт

«-лт» нэр ба хоосон үйл үг («хийх», «үзүүлэх», «явуулах») өгүүлбэрийг удаашруулна. Үйл үгээр нь бич.

| Буруу | Зөв |
|---|---|
| дүн шинжилгээ хийх | шинжлэх |
| судалгаа явуулах | судлах |
| хэмжилт хийх | хэмжих |
| харьцуулалт хийх | харьцуулах |
| нөлөө үзүүлэх | нөлөөлөх |
| сонголт хийх | сонгох |
| бууралт үзүүлэх | буурах |

Нэр болж тогтсон «-лт» үг эзэн, тусагдахуун болж утгаа өөрөө даадаг бол хэвийн. «Өглөө 8 цагт хэмжилт хийв»-ийн оронд «Өглөө 8 цагт хэмжив» гэж бич; харин «Хэмжилтийн алдаа ±2 мм» хэвийн.

#### Олон тооны илүүц дагавар

Олныг өөр үг аль хэдийн заасан бол олон тооны дагавар хэрэггүй.

| Буруу | Зөв |
|---|---|
| 1600 оюутнууд | 1600 оюутан |
| олон хүмүүс | олон хүн |
| оролцогч бүрүүд | оролцогч бүр |
| хонь малууд | хонь мал |
| охидууд, хүмүүсүүд | охид, хүмүүс |
| Улаанбаатарчууд | Улаанбаатарынхан |

#### Орчуулгын хуулбар

| Хуулбар | Монгол бүтэц |
|---|---|
| Өгүүлбэр бүр «Энэ нь ...»-ээр эхлэх | Өмнөх өгүүлбэртэй нийлүүл, юуг гэдгийг нэрлэ |
| «... -ын хувьд» өгүүлбэр бүрт | Хас, эсвэл тийн ялгалаар |
| «чухал үүрэг гүйцэтгэдэг» | Юу хийдгийг нэрлэ |
| «анхаарлаа төвлөрүүлэх» | «анхаарах», «голлох» |
| «алхам хийх» | «арга хэмжээ авах», үйлдлийг нэрлэ |
| «... дээр ажиллах» | «...-ыг хийх», «...-д ажиллах» |

#### Хөөрөгдөл

Шинжлэх ухааны бичвэрт баримтгүй үнэлгээг хас: «хувьсгалт нээлт», «шинэ эрин үеийг нээв», «онцгой ач холбогдолтой», «урьд өмнө байгаагүй». Оронд нь шинэ үр дүнг нэрлэ: юуг анх удаа хэмжсэн, юуг харьцуулсан, ямар тоо гарсан.

#### Хураангуйн тунхаглал

«Энэхүү өгүүлэлд ...-ын талаар авч үзэх болно» гэж бичихийн оронд үр дүнг шууд бич: «Судалгаагаар ... болохыг тогтоов.»

### Зөв бичгийн түгээмэл алдаа

| Буруу | Зөв |
|---|---|
| дараахь | дараах |
| идэвхи | идэвх |
| томъёо | томьёо |
| харъяа | харьяа |
| нилээд | нэлээд |
| ишлэл | эшлэл |
| олонхи, олонхийн | олонх, олонхын |
| талаархи, доторхи | талаарх, доторх |
| чадавхи | чадавх |
| объектийн | объектын |
| элемэнт | элемент |
| хоёрдахь | хоёр дахь |
| санаачлага | санаачилга |
| оношлогоо | оношилгоо |
| зөвлөлгөө | зөвлөгөө |

Бусад дүрэм:

- **бэ / вэ:** в, л, м, н-ээр төгссөн үгэнд «бэ», бусад үгэнд «вэ».
- **уу/үү, юу/юү:** урт, хос эгшгээр төгссөн үгэнд «юу/юү».
- **Том үсэг:** гарчгийн зөвхөн эхний үг, оноосон нэр (англи маягаар үг бүрийг томоор эхлэхгүй). Улсын төвийн байгууллага, олон улсын байгууллагын нэрийн бүх үгийг томоор.
- **Товчлол:** оноосон нэрийг үсгээр хураавал бүх үсгийг томоор, цэггүй (МУИС, ДЭМБ); хүний овгийн хураасан үсгийн ард цэг (Ш.Эрдэнэбат).
- **Хашилт:** шууд ярианы дараа «гэж»-ийн өмнө таслал тавихгүй.
- **Урт зураас:** хязгаарт (XV—XX зуун, 10—20 мг); англи маягаар завсарлага оруулахад хэрэглэхгүй.
- **Гадаад үг:** -ия-г хасна (академи, стратеги, энерги, компани).

Бүрэн жагсаалтыг Humanizer эсвэл Humanizer-MN ур чадварын зөв бичих дүрмийн лавлахаас (1983 оны дүрэм, 2011 оны журамласан үгс) үз.

### Хиймэл оюуны бичсэн шинжлэх ухааны бичвэрт элбэг шинж

| Шинж | Засвар |
|---|---|
| «Энэхүү судалгаа нь салбарт хувьсгалт өөрчлөлт авчрах онцгой ач холбогдолтой.» | Шинэ үр дүнг нэрлэ |
| «Олон судалгаагаар батлагдсанчлан ...» эшлэлгүй | Эшлэл нэм (эх сурвалжтай бол), эсвэл хас |
| Нэг нэр томьёог «загвар», «модель», «систем» гэж солбин бичих | Нэгийг сонгоод бүх бичвэрт мөрд |
| «магадгүй ... байж болох юм гэж үзэж болох талтай» | Нэг болгоомжлол: «байж болно» |
| Догол мөр бүр «Нэмж дурдахад», «Цаашлаад», «Эцэст нь хэлэхэд»-ээр эхлэх | Утгын холбоогоор шилжүүл |
| Хэлэлцүүлгийн төгсгөлд «Ирээдүйд энэ чиглэлийн судалгаа улам хөгжинө» | Тодорхой цаашдын судалгааг нэрлэ |
| Үр дүн, хэлэлцүүлэгт жагсаалт, тод шошго | Үргэлжилсэн догол мөр |

### Шалгах асуулт

1. Хураангуй, үр дүн, дүгнэлт хоорондоо зөрчилдөж байна уу?
2. Нэр томьёо бүх бичвэрт нэг утгатай юу?
3. Тоо, хэмжилт, статистикийн утга хүснэгт, зурагтай таарч байна уу?
4. Эшлэлгүй дүгнэлт үлдсэн үү?
5. Ажиглалтын судалгаанд учир шалтгааны үг («нөлөөлсөн», «шалтгаалсан») хэрэглэсэн үү?
6. «-лт хийх», олон тооны илүүц дагавар, «Энэ нь» гинж байна уу?
7. Зөв бичгийн алдаа (дараахь, томъёо, харъяа г.м.) үлдсэн үү?
