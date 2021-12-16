import asyncio

from pytgcalls import idle

from config import call_py


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | LUCIFER Started! |
    ------------------
"""
    )
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
