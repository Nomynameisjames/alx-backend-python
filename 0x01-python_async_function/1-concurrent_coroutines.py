#!/usr/bin/env python3
'''
  importing asyncio to use the async/await syntax
'''
import asyncio

'''
    this module defines an async routine called wait_n that takes in 2 int
    arguments(in this order): n and max_delay.
    wait_random is spawn n times with the specified max_delay and finally
    returns the list of all the delays (float values) in ascending order.
'''


async def wait_n(n: int, max_delay: int) -> list:
    '''
        wait_random is called n times with the specified max_delay
        importing wait_random from 0-basic_async_syntax module which 
        generates a random delay between 0 and max_delay
    '''
    wait_random = __import__('0-basic_async_syntax').wait_random
    waitTime = []
    i = 0
    for i in range(n):
        waitTime.append(wait_random(max_delay))
    task = [await delay for delay in asyncio.as_completed(waitTime)]
    return task
