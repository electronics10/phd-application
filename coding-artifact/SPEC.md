# SPEC: coding-artifact

Written by the level above. Read-only for agents in this folder.

## Purpose

A from-scratch technical artifact demonstrating adjoint-based, PDE-constrained
optimization on wave problems. It is the primary technical differentiator for a
PhD application (linked from a CV/portfolio once public, see D2), fixing the
known gaps in the applicant's MS thesis (no own solver, no density filter /
Heaviside projection / robust formulation, no finite-difference check of the
adjoint gradient). It also tests whether the applicant enjoys the method as daily
practice, feeding back into the still-open field choice tracked in `application/`.

## Requirements

- **R1** A 2D frequency-domain finite-difference (FDFD) electromagnetic wave
  solver with PML absorbing boundaries, implemented from scratch. Standard
  numpy/scipy linear algebra routines are allowed; no commercial or black-box
  solver may be the physics core.
- **R2** The adjoint-method gradient of an objective (e.g. transmission or field
  intensity at a port) with respect to the material/density field, hand-derived
  and hand-coded (no autodiff framework).
- **R3** A density filter, Heaviside projection, and β-continuation scheme,
  applied to topology-optimize a waveguide bend.
- **R4** The same solver/adjoint/filter machinery ported to the 2D acoustic wave
  equation as a toy full-waveform-inversion (FWI) problem.
- **R5** One deliberately cycle-skipped FWI run, documented.
- **R6** A README deriving the adjoint method for this specific problem (not a
  generic textbook derivation), written by the applicant.
- **R7** Stride (an existing open-source USCT/FWI framework built on Devito) run
  on a representative problem, compared/contrasted against the from-scratch toy
  FWI (R4). Delegated to the child `stride-trial/` (see Interfaces).

## Constraints

- **Language:** Python 3.
- **Core dependencies (R1-R6):** `numpy==2.5.4`, `scipy==1.18.1`,
  `matplotlib==3.11.2` only (current stable as of 2026-10-12; T1 pins the
  actually-installed versions in a lockfile). No autodiff framework (JAX,
  PyTorch, autograd) — the point of R2 is a hand-coded gradient, validated by
  the finite-difference check in PLAN.md, not computed by a framework.
- **Folder layout:** this project lives at `coding-artifact/` inside the private
  `phd-application` repository (see D2). `stride-trial/` is its one subfolder
  child; its own dependency chain (Stride, Devito) is isolated there and must
  never become a dependency of R1-R6's core code.
- No GPU, no 3D, no performance/production engineering (see Non-goals).

## Non-goals

- No 3D extension of the solver or topology optimization.
- No GPU acceleration or performance engineering.
- No physical fabrication or hardware.
- Not an attempt at a novel, publishable research result — this is a
  demonstration/learning artifact.
- No packaging, CI/CD, or distribution beyond the repository itself.
- No autodiff dependency in the core solver/adjoint code (R1-R6); see Constraints.

## Decisions

- **D1** (2026-10-12) Stride (R7) is in scope, not deferred. *Reason:* user
  explicitly chose to include it when asked whether to defer it.
- **D2** (2026-10-12) `coding-artifact/` stays a subfolder of the private
  `phd-application` repo for now, not a separate public repo. *Reason:* user's
  explicit choice, aware this means it isn't yet link-able from a CV. *Revisit
  before:* applications are actually submitted, since the handoff doc's
  findability plan (3.2) calls for "a GitHub link in the CV."
- **D3** (2026-10-12) The adjoint gradient (R2) is hand-coded, not computed via
  an autodiff framework. *Reason:* the finite-difference check already validates
  it; the point of the artifact is demonstrating the applicant derived and coded
  it themselves.
- **D4** (2026-10-12) R1-R6 are executed directly by the applicant (Executor: you
  in PLAN.md), with Claude reviewing, debugging, and handling boilerplate
  scaffolding. R7 is delegated to Claude via the `stride-trial/` child, since
  running an existing framework does not carry the same authorship stakes as the
  from-scratch work. *Reason:* this artifact is presented as evidence of the
  applicant's own research ability; authenticity of authorship matters for R1-R6
  in a way it does not for R7.

## Interfaces

- `stride-trial/` provides: a runnable script that reconstructs a synthetic
  velocity model with Stride, producing a result (recovered model + convergence
  metric) in a format comparable to R4's toy-FWI output (same synthetic model
  class, same error metric). Behavior on error: the script must fail loudly
  (non-zero exit), never silently produce a partial result.

  The canonical reference case both R4 (your own T4 test) and `stride-trial/`
  must reconstruct against is fixed in
  `stride-trial/contracts/reference_case.py`: a 40x40 grid, 10 m spacing,
  background velocity 1500 m/s with a 1800 m/s square perturbation, a fixed
  source/receiver line geometry, and a normalized-L2 relative-error metric with
  a 0.10 pass threshold for a well-posed start. When you write T4's own test,
  import this module rather than redefining the model, so both results are
  checked against the same numbers.

  *Contract tests:* `stride-trial/contracts/test_reference_case.py`.
