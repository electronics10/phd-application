"""Contract test for stride-trial T1 (see PLAN.md).

Written before implementation, per AGENTS.md: "Write the tests before
execution when possible." This will fail with ImportError until T1 creates
`stride-trial/reconstruct.py` exporting `run_reconstruction`.

Expected interface `reconstruct.run_reconstruction`:

    def run_reconstruction(
        true_model: np.ndarray,
        starting_model: np.ndarray,
        source_x_indices: list[int],
        source_z_index: int,
        receiver_x_indices: list[int],
        receiver_z_index: int,
        grid_spacing_m: float,
    ) -> np.ndarray:
        '''Return a recovered velocity model of the same shape as true_model,
        reconstructed with Stride from synthetic data generated at
        true_model.'''
"""

import pytest

from reference_case import (
    GRID_SPACING_M,
    RECEIVER_X_INDICES,
    RECEIVER_Z_INDEX,
    SOURCE_X_INDICES,
    SOURCE_Z_INDEX,
    WELL_POSED_RELATIVE_L2_THRESHOLD,
    relative_l2_error,
    true_velocity_model,
    well_posed_starting_model,
)


def test_well_posed_reconstruction_meets_error_threshold():
    reconstruct = pytest.importorskip(
        "reconstruct", reason="T1 not yet implemented"
    )

    true_model = true_velocity_model()
    recovered = reconstruct.run_reconstruction(
        true_model=true_model,
        starting_model=well_posed_starting_model(),
        source_x_indices=SOURCE_X_INDICES,
        source_z_index=SOURCE_Z_INDEX,
        receiver_x_indices=RECEIVER_X_INDICES,
        receiver_z_index=RECEIVER_Z_INDEX,
        grid_spacing_m=GRID_SPACING_M,
    )

    assert recovered.shape == true_model.shape
    error = relative_l2_error(recovered, true_model)
    assert error < WELL_POSED_RELATIVE_L2_THRESHOLD, (
        f"relative L2 error {error:.4f} exceeds threshold "
        f"{WELL_POSED_RELATIVE_L2_THRESHOLD}"
    )
