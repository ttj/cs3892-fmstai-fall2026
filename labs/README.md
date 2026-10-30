# Tools and setup

**You are never required to install anything to pass this course.** Every tool has a zero-install
path. Local installation is fully supported as a backup and is worth doing if you plan a
tool-heavy project.

## Zero-install paths

| Tool | Used in | In the browser, no account | With a GitHub account |
|---|---|---|---|
| **Z3** | HW1, Unit 3 | [Z3 Guide](https://microsoft.github.io/z3guide/) — runs Z3 in-browser | Codespaces / [Colab](https://colab.research.google.com/github/ttj/fmaiv/blob/main/notebooks/01_day1_logic_sat_smt.ipynb) |
| **NuSMV / nuXmv** | HW2, Units 4–6 | [smvis](https://smvis-378135919048.us-central1.run.app/) — NuSMV with state/BDD visualization, accepts your own `.smv` | Codespaces (`NuSMV` preinstalled) |
| **CBMC** | HW3, Unit 7 | — | Codespaces |
| **Frama-C** | Unit 7 | — | Local or container |
| **Lean 4** | HW4, Unit 8 | [Lean web editor](https://live.lean-lang.org/) · [Natural Number Game](https://adam.math.hhu.de/) | Codespaces or local (required for Cslib) |
| **auto_LiRPA / α,β-CROWN** | HW5, Unit 10 | — | [Colab](https://colab.research.google.com/github/ttj/fmaiv/blob/main/notebooks/05_day4_nn_robustness.ipynb) |

**Container with everything preinstalled:** open [`ttj/fmaiv`](https://github.com/ttj/fmaiv) in
GitHub Codespaces. It ships `z3`, `cbmc`, `cryptol`, `saw`, `NuSMV`, `lean`, and `smvis`, plus CPU
`torch` and `auto_LiRPA` for the neural-network notebooks. Free within GitHub's monthly allowance
(180 core-hours for verified students through GitHub Education — sign up early, verification takes
a few days).

**nuXmv itself is licence-gated** and cannot be redistributed, so it is not in the container. Use
smvis or the preinstalled `NuSMV`: the SMV language and the `is true` / `is false` verdicts are the
same for everything we do. If you want nuXmv locally, register at <https://nuxmv.fbk.eu/>.

## Lean 4 — read this before installing

Lean releases monthly, and there will be two or three releases during the semester. Chasing them
mid-term will break your project.

**Pin this triple for the whole term:**

```toml
# lean-toolchain
leanprover/lean4:v4.33.0
```

```toml
# lakefile.toml
[[require]]
name = "cslib"
scope = "leanprover"
rev = "v4.33.0"
```

Mathlib is pinned to `v4.33.0` to match.

**Do not follow Cslib's own README.** It instructs you to use `rev = "main"`, and `main` currently
pins a *release-candidate* toolchain. A student who installs Lean stable and follows that README
ends up dragging in an RC. The cost of pinning is small: only a handful of files exist on `main`
and not in `v4.33.0`.

**Install order (the recommended path changed in 2026):**

1. Install [VS Code](https://code.visualstudio.com/Download).
2. Install the **Lean 4** extension (`leanprover`) from the Extensions panel.
3. Let the extension run its guided setup — it installs `elan` and the toolchain for you.

Manual `elan-init` is the fallback, not the default.

**The browser Lean editors ship Mathlib only.** `import Cslib` will not work at
<https://live.lean-lang.org/> or on the HHU mirror. Those are fine for week 1 and for the Natural
Number Game; Cslib work happens in Codespaces or locally.

**Build cost — measured, so you can plan.** Mathlib ships a prebuilt object cache
(`lake exe cache get`, ~8 s). Cslib's ~200 files have **no** such cache and compile locally the
first time. On a 24-core reference machine the cold build is **1 m 34 s** (2,803 jobs, ~17
CPU-minutes, peak RSS 3.1 GB); dependency fetch adds about 1 m 45 s. On a typical 4-core laptop
expect **roughly 5–10 minutes of compilation, ~10 minutes end to end**.

That is fine. What is *not* automatic:

- **Disk: budget ~11 GB** — about 7.8 GB for the project's `.lake` directory plus 2.9 GB for the
  Lean toolchain. This is the constraint that actually bites, not time.
- **RAM: keep ~4 GB free** during the build.
- **Do it before the lab session**, not during it. Run `lake build` once at home in week 9 and
  confirm it finishes; if it does not, come to office hours with the error rather than losing the
  session.

If your machine cannot spare 11 GB, a Codespace with that much disk works too, but the course container does **not** come with Mathlib or Cslib built: `lake exe cache get` and `lake build` run there just as locally. Nothing graded needs Cslib: session 21's slides and its example folder show every output.

**AI assistance in Lean:** use
[`lean-lsp-mcp`](https://github.com/oOo0oOo/lean-lsp-mcp) — it rides the Lean language server, is
toolchain-agnostic (so it will not fight the version pin), installs with pip/uvx, needs no GPU, and
plugs into the MCP clients you already have. It exposes goal states, diagnostics, and hover docs to
your assistant, which is what actually makes AI useful for proving. Skip LeanCopilot this term (its
releases lag stable Lean and will conflict with the Cslib pin) and skip LeanAgent (dormant since
mid-2025).

## The running example

Every tool in this course verifies a variant of the *same* property — a bounded counter whose
value `x` never exceeds 10 — and the machine, the property, and the verdict you should get from
each tool are defined once, in **[`running-example.md`](running-example.md)**.

Read that page before HW1. It is the single source of truth: if a homework, a quiz or a slide
disagrees with it, it is right and the other one is a bug.

Five verdicts, five different meanings of the word "verified." Working out precisely how they
differ — which ones would miss a bug past the bound, which ones force you to supply an inductive
invariant — is the intellectual point of the homework sequence.

## Getting help

- Course discussion board on Brightspace — first stop, so answers help everyone.
- Lean: [Lean Zulip](https://leanprover.zulipchat.com/) is welcoming to beginners.
- Office hours: by appointment, easiest right before or after class.

**If you lose more than an hour to a setup problem, stop and ask.** The zero-install paths exist
precisely so that no one's grade depends on their laptop.
