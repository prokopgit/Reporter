import asyncpg
from config import POSTGRES_URL

async def get_conn():
    return await asyncpg.connect(POSTGRES_URL)

async def is_published(link):
    conn = await get_conn()
    result = await conn.fetchval("SELECT 1 FROM published_links WHERE url = $1", link)
    await conn.close()
    return result is not None

async def mark_as_published(link):
    conn = await get_conn()
    await conn.execute("INSERT INTO published_links (url) VALUES ($1)", link)
    await conn.close()
