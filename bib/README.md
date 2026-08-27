# Bibliography — CS 3892 / 5892, Fall 2026

`course.bib` is the single source. Everything else here is generated from it.

```
python3 bib/make_bibliographies.py          # split + typeset all bibliographies
python3 bib/make_bibliographies.py --check  # verify it all compiles, keep nothing
```

Output lands in `bib/build/`: one **comprehensive** bibliography plus one per module
(`d1`, `week01`, `session01`, `unit0`, `unit1`, …), driven by each entry's `keywords` field.
`bib/by-module/*.bib` are the generated subsets, usable directly in a paper.

## What "verified" means here

Every entry was checked against a primary source, not against a search result:

- **Journal articles** — the DOI was resolved through `doi.org` content negotiation (CSL-JSON)
  and the returned title, authors, journal, volume, issue and pages compared field by field
  against the citation. Two were additionally cross-checked against PubMed.
- **Reports, standards and court filings** — the PDF was downloaded and every quoted phrase
  located inside it with `pdftotext`. Page counts in the reading packets were checked against
  the real documents, which is how the NHTSA closing summary turned out to be 6 pp rather than
  the 11 pp the packet claimed.

Each entry's `note` field records what was verified and any live caveat — an erratum, an author
conflict of interest, a paywall, a host that blocks automated fetchers.

**One entry exists only to be cited alongside another.** `wong2021sepsis-erratum` corrects the
number needed to evaluate in the Epic Sepsis Model paper from 15 to 8. The packets quote 8, the
corrected figure; a student who downloads the original PDF sees 15. Cite both.

## Conventions

- Keys are `<firstauthor><year><shorttopic>`.
- **Brace-protect proper nouns in titles.** The `plain` style lowercases everything it is not
  told to preserve, which turns a case citation into `no. 6:24-cv-1903-acc-uam (m.d. fla.)`.
- Build with `pdflatex` → `bibtex` → `pdflatex` × 2. **Not biblatex**: `biber` is not installed
  on the course machine, and `plain` needs no external `.bst`.
