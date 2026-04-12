#!/usr/bin/env python3
"""Module that provides a function to return elements with their lengths."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Take an iterable of sequences and return a list
    of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
