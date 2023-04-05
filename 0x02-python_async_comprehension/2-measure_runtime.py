#!/usr/bin/env python3
"""
   import time to measure the runtime of a function
   import asyncio to run a coroutine
"""
import asyncio
import time

"""
    measure_runtime function coroutine that execute async_comprehension
    four times in parallel using asyncio.gather.
    measure the total runtime and return it.
"""


async def measure_runtime() -> float:
    """
        measure_runtime function declaration
    """
    async_comprehension = __import__('1-async_comprehension')\
        .async_comprehension
    startTime = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    endTime = time.perf_counter()
    totalTime = endTime - startTime
    return float(f'{totalTime:.3f}')

"""
    The total runtime taken is roughly 10 seconds because each
    async_comprehension call within the asyncio.gather takes 1 sec
    to complete. however because we are executing four async_comprehension
    calls in simultaneously, the average runtime should be roughly four
    seconds. However, there are some misalignment associated with managing
    coroutines, so it may have slightly altered runtime longer.
"""
