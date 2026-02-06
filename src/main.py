"""
Main pipeline stub.
MODEL EXECUTION DISABLED – STRUCTURE ONLY
"""

# MODEL EXECUTION DISABLED – STRUCTURE ONLY

from typing import Dict, List

from segmentation import segment_solid_fluid_air
from geometry_inference import infer_geometry_2d_to_3d
from model_selector import select_physics_solver
from surrogate_solver import run_surrogate_solver


def demo_pipeline_flow(image_2d: List[List[float]]) -> Dict[str, object]:
    """
    Demonstrate pipeline flow with dummy arrays and stub modules.

    Args:
        image_2d: 2D array-like numeric input (stub).

    Returns:
        Dictionary of intermediate artifacts and final stub output.
    """
    # TODO: Replace with real orchestration and I/O handling.
    segmentation = segment_solid_fluid_air(image_2d)
    voxel_grid = infer_geometry_2d_to_3d(image_2d)
    selection = select_physics_solver(segmentation)
    result = run_surrogate_solver(voxel_grid, selection["solver"])

    return {
        "segmentation": segmentation,
        "voxel_grid": voxel_grid,
        "selection": selection,
        "result": result,
    }


def build_dummy_input(width: int = 4, height: int = 3) -> List[List[float]]:
    """
    Create a small dummy 2D array for demonstration purposes.

    Args:
        width: Number of columns.
        height: Number of rows.

    Returns:
        2D list of floats in [0, 1].
    """
    # TODO: Replace with real input loading.
    image_2d: List[List[float]] = []
    for r in range(height):
        row: List[float] = []
        for c in range(width):
            row.append(((r + 1) * (c + 1)) / (width * height))
        image_2d.append(row)
    return image_2d
