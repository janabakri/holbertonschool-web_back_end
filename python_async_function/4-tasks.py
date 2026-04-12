#!/usr/bin/env python3
"""Task 4: task_wait_n function"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns a sorted list of the delays.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay value passed to task_wait_random.

    Returns:
        List[float]: Sorted list of delays from each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
