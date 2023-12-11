#!/usr/bin/env python3
"""
basic sync
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    pend = random.uniform(0, max_delay)
    await asyncio.sleep(pend)
    return pend

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
