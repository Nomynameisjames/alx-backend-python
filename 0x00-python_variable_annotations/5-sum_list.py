#!/usr/bin/env python3
""" module typing method List """
from typing import List
"""
   declaring a list annonated type and summing the list using
   the sun_list function
"""


def sum_list(input_list: List[float]) -> float:
    """
       summing the list of float values passed to the list
       and returning the sum as a float value
    """
    return sum(input_list)
