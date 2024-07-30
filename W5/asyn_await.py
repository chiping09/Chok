import asyncio

async def main():
    print('chok')
    await foo('text')

async def foo(text):
    print(text)
    await asyncio.sleep(5)

asyncio.run(main())