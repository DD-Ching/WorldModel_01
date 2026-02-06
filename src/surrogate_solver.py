"""
Surrogate solver module stub.
MODEL EXECUTION DISABLED – STRUCTURE ONLY
"""

# MODEL EXECUTION DISABLED – STRUCTURE ONLY

from typing import Dict, List


def run_surrogate_solver(voxel_grid: List[List[List[float]]], solver_id: str) -> Dict[str, str]:
    """
    Placeholder surrogate solver that returns dummy outputs.

    Args:
        voxel_grid: 3D voxel grid placeholder.
        solver_id: Selected solver identifier.

    Returns:
        Dummy results and metadata.
    """
    # TODO: Replace with a real surrogate or physics solver.
    _ = voxel_grid
    return {
        "solver_id": solver_id,
        "status": "not_executed",
        "message": "MODEL EXECUTION DISABLED – STRUCTURE ONLY",
    }
