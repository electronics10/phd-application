"""Canonical reference case shared by stride-trial and the parent's own T4 test.

Fixed per coding-artifact/SPEC.md Interfaces. Both the from-scratch toy FWI
(parent T4) and the Stride reconstruction (this folder's T1) must reconstruct
this exact model and report error the same way, so the two results are
directly comparable.

Deliberately small and cheap to run: this is a comparability fixture, not a
realistic imaging scenario.
"""

import numpy as np

GRID_SHAPE = (40, 40)          # (nx, nz) grid cells
GRID_SPACING_M = 10.0          # isotropic spacing, meters

BACKGROUND_VELOCITY_MPS = 1500.0
PERTURBATION_VELOCITY_MPS = 1800.0
# Square perturbation centered in the grid, 10x10 cells.
PERTURBATION_SLICE = (slice(15, 25), slice(15, 25))

# Source/receiver geometry: a line of sources along the top edge, a line of
# receivers along the bottom edge, both spanning the full width.
SOURCE_Z_INDEX = 0
RECEIVER_Z_INDEX = GRID_SHAPE[1] - 1
SOURCE_X_INDICES = list(range(0, GRID_SHAPE[0], 4))     # every 4th cell
RECEIVER_X_INDICES = list(range(0, GRID_SHAPE[0], 2))   # every 2nd cell

# Well-posed starting model for the pass/fail threshold below: homogeneous at
# the background velocity (i.e. "no prior knowledge of the perturbation").
WELL_POSED_RELATIVE_L2_THRESHOLD = 0.10


def true_velocity_model() -> np.ndarray:
    """The fixed ground-truth model this reference case reconstructs."""
    model = np.full(GRID_SHAPE, BACKGROUND_VELOCITY_MPS, dtype=float)
    model[PERTURBATION_SLICE] = PERTURBATION_VELOCITY_MPS
    return model


def well_posed_starting_model() -> np.ndarray:
    """The starting model for the well-posed (non-cycle-skipped) case."""
    return np.full(GRID_SHAPE, BACKGROUND_VELOCITY_MPS, dtype=float)


def relative_l2_error(recovered: np.ndarray, true: np.ndarray = None) -> float:
    """Normalized L2 error between a recovered model and the true model."""
    if true is None:
        true = true_velocity_model()
    return float(np.linalg.norm(recovered - true) / np.linalg.norm(true))
