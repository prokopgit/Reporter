import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from news_parser import fetch_and_post_news
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()
scheduler = AsyncIOScheduler()

async def main():
    scheduler.add_job(fetch_and_post_news, "interval", hours=8)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
