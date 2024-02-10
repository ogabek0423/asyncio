import asyncio
import datetime

async def task1():
    await asyncio.sleep(1)
    print("task 1 complete ->", datetime.datetime.now())


async def task2():
    await asyncio.sleep(2)
    print("task 2 complete ->", datetime.datetime.now())


async def task3():
    await asyncio.sleep(3)
    print("task 3 complete ->", datetime.datetime.now())


async def task4():
    await asyncio.sleep(4)
    print("task 4 complete ->", datetime.datetime.now())


async def task5():
    await asyncio.sleep(5)
    print("task 5 complete ->", datetime.datetime.now())


async def task6():
    await asyncio.sleep(6)
    print("task 6 complete ->", datetime.datetime.now())


async def task7():
    await asyncio.sleep(7)
    print("task 7 complete ->", datetime.datetime.now())


async def task8():
    await asyncio.sleep(8)
    print("task 8 complete ->", datetime.datetime.now())


async def task9():
    await asyncio.sleep(9)
    print("task 9 complete ->", datetime.datetime.now())


async def task10():
    await asyncio.sleep(10)
    print("task 10 complete ->", datetime.datetime.now())


async def task11():
    await asyncio.sleep(11)
    print("task 11 complete ->", datetime.datetime.now())


async def task12():
    await asyncio.sleep(12)
    print("task 12 complete ->", datetime.datetime.now())


async def task13():
    await asyncio.sleep(13)
    print("task 13 complete ->", datetime.datetime.now())


async def task14():
    await asyncio.sleep(14)
    print("task 14 complete ->", datetime.datetime.now())

async def task15():
    await asyncio.sleep(15)
    print("task 15 complete ->", datetime.datetime.now())


async def task16():
    await asyncio.sleep(16)
    print("task 16 complete ->", datetime.datetime.now())


async def task17():
    await asyncio.sleep(17)
    print("task 17 complete ->", datetime.datetime.now())


async def task18():
    await asyncio.sleep(18)
    print("task 18 complete ->", datetime.datetime.now())


async def task19():
    await asyncio.sleep(19)
    print("task 19 complete ->", datetime.datetime.now())


async def task20():
    await asyncio.sleep(20)
    print("task 20 complete ->", datetime.datetime.now())



async def main():
    await asyncio.gather(task1(), task2(), task3(), task4(), task5(), task6(), task7(), task8(), task9(), task10(), task11(), task12(), task13(), task14(), task15(), task16(), task17(), task18(), task19(), task20())

if __name__ == "__main__":
    asyncio.run(main())
