#!/usr/bin/env python3
''' import asyncio module to use async/await syntax
    import random module to use random function
'''
import asyncio
import random

"""
    function declares an async function named wait_random that waits
    for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
"""


async def wait_random(max_delay: int = 10) -> float:
    ''' waiTime stores a random delay between 0 and max_delay value '''
    waitTime = random.uniform(0, max_delay)
    await asyncio.sleep(waitTime)
    ''' return the random delay '''
    return waitTime
