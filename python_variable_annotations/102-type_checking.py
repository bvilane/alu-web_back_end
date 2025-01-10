#!/usr/bin/env python3
'''Type Checking'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Function to zoom in an array by duplicating its elements."""
    zoomed_in = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

