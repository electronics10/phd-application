# SPEC: stride-trial

Written by the level above. Read-only for agents in this folder.

## Purpose

Satisfy `coding-artifact/`'s R7: run Stride (an existing open-source
ultrasound-computed-tomography / full-waveform-inversion framework, built on
Devito) on a representative problem, producing a result that can be compared
against the parent's from-scratch toy FWI (its T4).

## Requirements

- **R1** A runnable script that reconstructs a synthetic velocity model using
  Stride, on the same synthetic-model class and error metric as the parent's
  T4, so the two results are directly comparable.
- **R2** A short written comparison: what Stride gives you (performance,
  features, maturity) that the from-scratch version does not, and vice versa.

## Constraints

- **Language:** Python 3.
- **Packages:** `stride==0.1.6`, `devito==4.8.23` (current stable as of
  2026-10-12). These dependencies are isolated to this folder and must never
  be imported by the parent's R1-R6 code.

## Non-goals

- Modifying or contributing to Stride/Devito itself.
- Matching Stride's performance or accuracy exactly — the point is comparison,
  not besting it.

## Decisions

- *(none yet)*

## Interfaces

- *(none; no children)*
