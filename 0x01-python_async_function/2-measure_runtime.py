#!/usr/bin/env python3
"""
  importing the asyncio module
  import the time module to measure the runtime performance
  importing wait_n function from 1-concurrent_coroutines.py
"""
import asyncio
import time

"""
    module implements a measure_time function with integers n and max_delay as
    arguments that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. as a float value.
"""


def measure_time(n: int, max_delay: int) -> float:
    """
        measure the total execution time for wait_n(n, max_delay)
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    StartTime = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    EndTime = time.perf_counter()
    TotalTime = EndTime - StartTime
    performance = TotalTime / n
    performance = f'{performance:.2f}'
    return float(performance)
