import asyncio
import time


async def get_num(number, divider):
    print(f'Here we divide number {number} on divider {divider}')
    await asyncio.sleep(3)
    print(number//divider)
    return number//divider


async def gather_worker():
    result = await asyncio.gather(
        get_num(50, 20),
        get_num(30, 10),
        get_num(70, 7),
        get_num(25, 5),
        get_num(12, 6),
        get_num(75, 3),
    )
    print(result)


event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(gather_worker())
]

tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()