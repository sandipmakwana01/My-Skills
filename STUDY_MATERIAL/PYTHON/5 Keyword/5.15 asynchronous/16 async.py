'''
async: This keyword is used to define an asynchronous function. An asynchronous function can contain await expressions and can be executed concurrently with other asynchronous operations.
'''
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    print("World")

async def main():
    await say_hello()

asyncio.run(main())
