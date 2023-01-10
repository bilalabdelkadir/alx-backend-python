#!/usr/bin/env python3
""" importation of async function"""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generate numbers with async comprehension
    args: void
    return : float random numbers
    """
    return ([i async for i in async_generator()])
    """
    in other words
    result = []
    async for i in async_generator():
        result.append(i)
    return result
    """
