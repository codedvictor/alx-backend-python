#!/usr/bin/env python3

"""
Concurrent coroutines
"""
import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times with specified max_delay"""
    a_delay = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return a_delay

if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
