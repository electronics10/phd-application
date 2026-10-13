# PLAN: coding-artifact

Written by the level above. Read-only for agents in this folder.

**Goal of this plan:** a working FDFD solver, hand-coded and FD-validated
adjoint, topology-optimized waveguide bend, a toy-FWI port with one
cycle-skipped run, a derivation README, and a Stride comparison — covering
R1-R7.

Each task not marked otherwise is **Executor: you** (the applicant writes the
code; Claude reviews, debugs, and scaffolds boilerplate around it per SPEC D4).
T7 is delegated to the child `stride-trial/` and its Executor is Claude.

## Tasks

### T1 FDFD solver with PML (direct, Executor: you)

- **Do:** implement the 2D FDFD EM solver with PML boundaries from scratch.
- **Done when:**
  - solver reproduces an analytic test case (e.g. a known waveguide mode or a
    plane wave in a homogeneous medium) within a stated numerical tolerance
  - `pytest tests/test_solver.py` passes

### T2 Adjoint gradient + FD check (direct, Executor: you)

- **Depends on:** T1
- **Do:** derive and hand-code the adjoint gradient of the chosen objective
  with respect to the material/density field.
- **Done when:**
  - `pytest tests/test_adjoint_fd_check.py` passes: adjoint gradient vs.
    central-difference gradient, relative error < 1e-4

### T3 Density filter + Heaviside + β-continuation on a waveguide bend (direct, Executor: you)

- **Depends on:** T2
- **Do:** implement the density filter, Heaviside projection, and β-continuation
  schedule; run the topology optimization on a waveguide bend.
- **Done when:**
  - final design is near-binary (e.g. ≥95% of density pixels within ε of 0 or 1)
  - objective improves across the continuation schedule, shown in a saved
    convergence plot
  - `pytest tests/test_topopt_waveguide.py` passes

### T4 Port to 2D acoustic-wave toy FWI (direct, Executor: you)

- **Depends on:** T2
- **Do:** port the solver/adjoint machinery to the 2D acoustic wave equation;
  run a toy FWI that recovers a known synthetic velocity model from synthetic
  data in a well-posed starting case.
- **Done when:**
  - recovered model matches the known synthetic model within a stated error
    tolerance
  - `pytest tests/test_fwi_wellposed.py` passes

### T5 Deliberate cycle-skipping run (direct, Executor: you)

- **Depends on:** T4
- **Do:** run FWI from a starting model intentionally far enough from the true
  model to trigger cycle-skipping; document the failure.
- **Done when:**
  - a saved run shows convergence to a wrong local minimum
  - the result and explanation are written up (in the README or a dedicated
    note)

### T6 README deriving the adjoint (direct, Executor: you)

- **Depends on:** T2
- **Do:** write a README deriving the adjoint method for this specific problem
  (not a generic textbook derivation).
- **Done when:**
  - you confirm the derivation is complete and accurate to your own
    understanding (human-confirmation check — R6 is deliberately not
    machine-checkable; authorship is the point)

### T7 Stride comparison (delegated → `stride-trial/`, Executor: Claude)

- **Depends on:** T4
- **Do:** plan and verify the child `stride-trial/`, implementing the interface
  in SPEC.md Interfaces.
- **Done when:**
  - all `stride-trial/` tasks are verified by you (the agent working in this
    folder, per AGENTS.md "Verifying a delegated task")
  - `stride-trial/contracts/` tests pass

## Not in this plan

- Making this repository (or a copy of this folder) public for CV linkage —
  deferred until closer to application submission; see SPEC.md D2.
- Any real experimental/USCT dataset — this plan uses synthetic models only.
- GPU, 3D, or performance work — these are SPEC.md non-goals, not deferrals.
