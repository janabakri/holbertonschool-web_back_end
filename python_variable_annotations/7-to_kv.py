#!/usr/bin/env python3
"""Module that provides a function to create a key-value tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Take a string and a number, return a tuple of the
    string and the square of the number."""
    return (k, float(v ** 2))
