#!/usr/bin/env python3
""" Run time for four parralel comprehension"""
import asyncio
import random
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures total runtime of
    return: float random numbers
    """
    first_time = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter()

    return (elapsed - first_time)
