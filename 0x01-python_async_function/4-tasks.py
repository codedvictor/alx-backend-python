#!/usr/bin/env python3
"""
Concurrent coroutines with tasks
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task with delay."""
    tasks = []
    delays = []

    for x in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delays.append(await task)

    return delays
