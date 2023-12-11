#!/usr/bin/env python3
"""
Measure runtime
"""
import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time_per_iteration = total_time / n

    return average_time_per_iteration

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
