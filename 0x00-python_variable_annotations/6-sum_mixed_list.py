#!/usr/bin/env python3
""" module typing method List and Union """
from typing import List, Union

"""
    the module contains a function that sums a list of floats and ints
    annotated values types and returns the sum as a float
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sums a list of floats and ints by using the List and Union
        method from the typing module
        annotated values types and returns the sum as a float """
    return sum(mxd_lst)
