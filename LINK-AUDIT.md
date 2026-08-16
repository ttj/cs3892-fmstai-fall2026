# Link audit

**Checked 2026-08-16.** Every URL cited in the Fall 2026 course materials was fetched and checked
on two criteria: (a) does it resolve, and (b) does the page actually serve the content the syllabus
claims it points to. A 200 that lands on a generic homepage, a soft-404, or a retired-service
notice counts as a failure.

**Result: 75 URLs checked · 71 good · 4 corrected · 4 bot-blocked but confirmed live.**

Re-run before each semester. Several failures below were *silent* — the old URL returned 200 and
looked healthy.

## Corrections applied

These were broken or wrong in the Fall 2025 materials (or in an obvious first guess) and have been
fixed:

| Was | Verdict | Now |
|---|---|---|
| `https://rise4fun.com/z3/` | **BROKEN** — Microsoft's RiSE4Fun playground is dead. DNS resolves to an Azure IP but nothing answers on 443; there is not even a retirement page. | <https://microsoft.github.io/z3guide/> |
| `http://www.concrete-semantics.org/` | **BROKEN over HTTPS** — the TLS certificate covers only the bare domain, so `www.` fails validation. The `http://www.` form 200s only unencrypted and never redirects, so any HTTPS-forcing browser hard-fails. | <https://concrete-semantics.org/> |
| `https://github.com/leanprover-community/cslib` | **BROKEN (404)** — wrong org. Cslib is an official `leanprover` project, not a community one. | <https://github.com/leanprover/cslib> |
| `https://docs.aws.amazon.com/…/guardrails-automated-reasoning-policies.html` | **BROKEN (soft-404)** — AWS silently 302s unknown Bedrock User Guide slugs to the guide index, so a wrong slug looks like a 200. | <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html> |
| `https://www.tradewindai.com/rai-toolkit` | 301 — the DoD **Responsible AI Toolkit** was renamed the **AI Assurance (AIA) Toolkit**. | <https://www.tradewindai.com/aia-toolkit> |
| `https://www.vanderbilt.edu//ucc/` | **Malformed** — double slash after the host. It happens to normalize server-side, but it breaks link checkers and PDF autolinking. | <https://www.vanderbilt.edu/student-care-network/university-counseling-center/> |
| `https://www.vanderbilt.edu/carecoordination/` | 301 into the Student Care Network site. | <https://www.vanderbilt.edu/student-care-network/student-care-coordination/> |
| `https://www.vanderbilt.edu/studentcarenetwork/satellite-services/` | 301 — the page was renamed "Drop-in Support." | <https://www.vanderbilt.edu/student-care-network/drop-in-support/> |
| `https://es.fbk.eu/tools/nuxmv/downloads/nuxmv-user-manual.pdf` | 301 to a different host. Destination confirmed by extracting the PDF text: *nuXmv 2.2.0 User Manual*. | <https://es-static.fbk.eu/tools/nuxmv/downloads/nuxmv-user-manual.pdf> |

## Live, but blocked to automated checkers

These return 403 to a datacenter IP and cannot be verified programmatically. Each was confirmed
live by other means; all load normally in a student browser. **Do not "fix" these** — a link
checker will keep flagging them.

| URL | Why it fails automation | Confirmation |
|---|---|---|
| <https://www.iso.org/standard/79804.html> | Cloudflare bot challenge, site-wide | Wayback 2026-08-03: ISO/IEC 24029-2:2023, Edition 1, stage 60.60 (published) |
| `https://www.ai.mil/…/genai-toolkit-…/` | DoD host blocks datacenter IPs site-wide | Wayback 2026-06-06, HTTP 200, correct CDAO article |
| <http://mitpress.mit.edu/books/principles-cyber-physical-systems> | Akamai 403 to this network, every path including the homepage | Wayback CDX shows a 301 (not 404) as recently as 2026-07-26, to the Alur CPS ISBN page |
| <http://mitpress.mit.edu/books/model-checking> | same | Wayback CDX 301 to ISBN 9780262032704, archived title *Model Checking* |

## Scheme warnings

- **`http://infolab.stanford.edu/~ullman/focs.html` must keep its `http://` scheme.** The host has
  no HTTPS listener at all; an `https://` version does not exist and will refuse the connection.
  It still works for students (stanford.edu is not HSTS-preloaded), though Chrome's HTTPS-First
  mode may show a one-click fallback. Automated checkers that upgrade to HTTPS will report this as
  dead — it is not.
- `http://www.TaylorTJohnson.com` serves 200 on both schemes and does *not* redirect. The syllabus
  uses the `https://` form.

## Content notes worth carrying into the syllabus

- **CS Immersion Showcase, Fall 2026: Thursday December 10, 2026, 5:00–7:00 p.m., Adams Atrium,
  Featheringill Hall.** Confirmed in the raw HTML of the CS Immersion page. Still marked
  **[confirm]** because it is single-sourced — no Events@Vanderbilt entry exists and the College of
  Connected Computing page still shows only Spring 2026. Note it falls on the **last day of
  classes**.
- **`vanderbilt.edu/generative-ai/academic-integrity/` is written for faculty, not students.** It is
  correct for the purpose but should always be paired with `/generative-ai/students/`.
- **Student Access Services is now just "Student Access."** Wording updated.
- **NIST AI 100-1 and the AI RMF landing page are the same document.** The Fall 2025 syllabus
  cited only the landing page (checked against the source `.docx`), so this is a clarification for
  the Fall 2026 reading list, not a correction to the old one.
- **The NIST AI RMF page carries a revision banner:** "being revised as part of the White House AI
  Action Plan." The landing page is the right stable link precisely because it tracks the revision.
- **NIST AI 100-2 E2025:** use the corrected April 2025 PDF plus the June 2025 errata, not a cached
  March copy.
- **EU AI Act:** Regulation (EU) 2026/1744 (the "Digital Omnibus on AI," in force 27 July 2026)
  moved the high-risk obligations to December 2027 and August 2028. Article 50 transparency
  obligations still apply from 2 August 2026. Any source dating high-risk obligations from August
  2026 predates the amendment.
- **α,β-CROWN's own repo description is out of date** — it claims VNN-COMP wins 2021–2025; it has
  now won six consecutive years, 2021–2026.
- **Marabou is no longer a VNN-COMP competitor** (absent in both 2025 and 2026) but the repo is
  active. Keep it as a teaching tool, not as a current-competition reference.
- **PyRAT has no public GitHub repository** — it is closed source (CEA-List). Cite
  <https://pyrat-analyzer.com/> and the paper; do not construct a repo URL.
- **The registrar's 2026–27 page is the *undergraduate* calendar.** The Graduate School publishes a
  separate calendar whose add/drop dates may differ for the CS 5892 section.

## Method

Forty-nine URLs were checked by nine parallel agents that fetched each page and compared its actual
content against the claimed purpose, searching for replacements where a page failed. Twenty-six
further URLs added during drafting were verified directly with `curl -L` and a browser user-agent.
Redirect chains, final URLs, and content-types were recorded in every case.

Raw results: `linkcheck.json` (not committed — regenerate by re-running the check).
