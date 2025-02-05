import asyncio
import sys


from weather import get_today_weather
from bot import command_start_handler, start_bot, get_weather, take_umberella

async def main() -> None:
    print("="*30)
    await take_umberella()

if __name__ == "__main__":
    asyncio.run(main())

