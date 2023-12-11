#!/usr/bin/env python3
"""
basic sync
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
