from aiogram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID

bot = Bot(token=TELEGRAM_TOKEN)

def format_post(title, summary, url, date):
    return (
        f"<b>{title}</b>\n\n"
        f"{summary}\n\n"
        f"<i>{date}</i>\n"
        f"<a href='{url}'>Джерело</a>"
    )

async def publish_news(title, summary, url, date, image=None):
    text = format_post(title, summary, url, date)
    if image:
        try:
            await bot.send_photo(chat_id=CHANNEL_ID, photo=image, caption=text)
        except:
            await bot.send_message(chat_id=CHANNEL_ID, text=text)
    else:
        await bot.send_message(chat_id=CHANNEL_ID, text=text)
