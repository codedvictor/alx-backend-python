#!/usr/bin/env python3
"""
Async generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """random number generator"""

    for _ in range(10):
        """range"""
        await asyncio.sleep(1)
        yield random.random() * 10
