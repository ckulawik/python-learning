#!/usr/bin/env python
import asyncio

async def do_first() -> None:
    print(f"Running do first block 1")
    # This sleep is intentionally 0, because it just triggers
    # a execution context release to the event loop 
    await asyncio.sleep(10)

    print("Running do first block 2")

async def do_second() -> None:
    print(f"Running do second block 1")
    # This sleep is intentionally 0, because it just triggers
    # a execution context release to the event loop 
    await asyncio.sleep(10)

    print("Running do second block 2")

async def main():
    task_1 = asyncio.create_task(do_first())
    task_2 = asyncio.create_task(do_second())

    await asyncio.wait([task_1, task_2])

if __name__ == "__main__":
    asyncio.run(main())
