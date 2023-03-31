#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of an
    integer or float.

    Args:
        k (str): A string.
        v (Union[int, float]): An integer or float.

    Returns:
        Tuple[str, float]: A tuple with string k and the square
        of the int/float v.
    """
    return (k, float(v ** 2))
