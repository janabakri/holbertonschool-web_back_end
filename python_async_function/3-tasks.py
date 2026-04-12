#!/usr/bin/env python3
"""Module that provides a function to create
an asyncio Task for wait_random."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Take an integer max_delay and return
    an asyncio Task for wait_random."""
    return asyncio.create_task(wait_random(max_delay))
