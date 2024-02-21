'''
await: This keyword is used inside an asynchronous function to pause its execution until the result of an asynchronous operation (like another asynchronous function call or a coroutine) is available. It's used to "await" the completion of the asynchronous operation without blocking the entire program.
'''
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    print("World")

async def main():
    await say_hello()

asyncio.run(main())
