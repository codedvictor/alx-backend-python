#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task for wait_random function."""
    task = asyncio.create_task(wait_random(max_delay))
    return task
