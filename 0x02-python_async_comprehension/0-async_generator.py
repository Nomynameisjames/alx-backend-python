#!/usr/bin/env python3
"""
    import random to generate random numbers
    import asyncio to create async functions
    import typing to specify the type of the function
"""
import random
import asyncio
from typing import AsyncGenerator

"""
    async_generator function that takes no arguments
    and returns a random number between 0 and 10
"""


async def async_generator() -> AsyncGenerator[float, None]:
    """
    The function yields a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
