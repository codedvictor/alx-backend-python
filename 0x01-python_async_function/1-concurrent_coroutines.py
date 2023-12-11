#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return delays
