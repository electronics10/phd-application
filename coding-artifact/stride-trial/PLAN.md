# PLAN: stride-trial

Written by the level above. Read-only for agents in this folder.

**Goal of this plan:** a Stride reconstruction comparable to the parent's toy
FWI, plus a written comparison. Covers R1-R2.

## Tasks

### T1 Install and run a Stride reconstruction (direct)

- **Do:** install Stride/Devito at the pinned versions; build or adapt a
  synthetic velocity-model reconstruction matching the parent's T4 model class
  and error metric.
- **Done when:**
  - `pytest contracts/test_reference_case.py` passes against the fixed
    reference case (provided)
  - the recovered-model error is reported in the same units/metric as the
    parent's T4

### T2 Write the comparison (direct)

- **Depends on:** T1
- **Do:** write a short note comparing Stride's result/workflow against the
  from-scratch toy FWI.
- **Done when:**
  - `stride-vs-custom.md` exists in this folder and names at least one
    concrete advantage and one concrete limitation of each approach

## Not in this plan

- Any real experimental/USCT dataset — synthetic only, per the parent's scope.
