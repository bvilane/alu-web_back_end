#!/usr/bin/env python3
'''Type Checking'''
from typing import Sequence, List, Union


def zoom_array(lst: Sequence[Union[int, float]], factor: int = 2) -> List[Union[int, float]]:
    """Function to zoom in an array by duplicating its elements."""
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
