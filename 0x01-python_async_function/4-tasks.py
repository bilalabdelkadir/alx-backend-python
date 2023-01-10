#!/usr/bin/env python3
""" measure the run time"""
import asyncio
import time
import random
from typing import List


task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Args:
    n and max_delays

    Returns Total_time/n
    """
    delays: List[float] = []
    tasks: List = []

    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
