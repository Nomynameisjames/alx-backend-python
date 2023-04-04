#!/usr/bin/env python3
"""
   import asyncio to utilize the async syntax
   import task_wait_random from 3-task.py
   import typing to use List
"""
import asyncio
from typing import List

"""
    function close to the previous task_wait_n
    except it calls task_wait_random function
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
         function that returns the list of all the wait time
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    waitTime = []
    for _ in range(n):
        waitTime.append(task_wait_random(max_delay))
    task = [await delay for delay in asyncio.as_completed(waitTime)]
    return task
