#!/usr/bin/env python3
"""
    async_generator from 0-async_generator.py 
"""
from typing import List
"""
    async_comprehension function that takes no arguments
    coroutine collects 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
"""


async def async_comprehension() -> List[float]:
    """
        async_comprehension function declaration
    """
    async_generator = __import__('0-async_generator').async_generator
    task = [i async for i in async_generator()]
    return task


