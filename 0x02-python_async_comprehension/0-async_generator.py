#!/usr/bin/env python3
"""Python asynchronous generators"""
import asyncio
import typing
import random


async def async_generator():
    for _ in range(0, 10):
        asyncio.sleep(1)
        yield random.random() * 10

if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
