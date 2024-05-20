# https://i.imgur.com/G4hqFYY.jpeg
import time
import asyncio

from api_key import stats_bot_username


STATS_PERIOD = 3600


async def main():
  while 1:
    await asyncio.sleep(STATS_PERIOD - (time.time() % STATS_PERIOD))
    await borg.send_message(stats_bot_username, '/stats')


def unload():
  if main_loop:
    main_loop.cancel()


main_loop = asyncio.ensure_future(main())