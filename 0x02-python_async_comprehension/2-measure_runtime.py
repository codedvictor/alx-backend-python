#!/usr/bin/env python3
"""
measure runtime
"""

import asyncio
from typing import List
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """import async comprehension"""
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()
    return end_time - start_time
