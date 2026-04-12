#!/usr/bin/env python3
"""Module that provides a function to sum a list of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Take a list of integers and floats and return their sum as a float."""
    return float(sum(mxd_lst))
