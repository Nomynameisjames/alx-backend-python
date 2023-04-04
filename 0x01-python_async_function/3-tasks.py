#!/usr/bin/env python3
"""
   import asyncio to use the async keyword
"""
import asyncio

"""
    function that takes an integer max_delay and returns an asyncio.Task
"""


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
        return an asyncio.Task
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
