#!/usr/bin/env python3
''' import the asyncio module to use async/await
    import the random module to generate random numbers
    import the typing module to use AsyncGenerator type annotations
'''
import asyncio
import random
from typing import AsyncGenerator


'''
    a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
'''


async def async_generator() -> AsyncGenerator[float, None]:
    '''
        async_generator function
        coroutine that will loop 10 times,
        each time asynchronously wait 1 second.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
