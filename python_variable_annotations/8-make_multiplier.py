#!/usr/bin/env python3
"""Module that provides a function to create a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Take a float multiplier and return
    a function that multiplies a float by it."""
    def multiply(n: float) -> float:
        """Multiply a float by the multiplier."""
        return n * multiplier
    return multiply
