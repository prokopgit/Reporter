import feedparser
from datetime import datetime
from translator import translate_text
from publisher import publish_news
from news_sources import RSS_FEEDS
from database import is_published, mark_as_published

async def fetch_and_post_news():
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            title = entry.title
            summary = entry.summary if 'summary' in entry else ""
            link = entry.link
            published = entry.get('published', str(datetime.utcnow()))
            image = None
            if 'media_content' in entry:
                image = entry.media_content[0].get('url')

            if await is_published(link):
                continue

            if not title or not summary:
                continue

            translated_title = await translate_text(title)
            translated_summary = await translate_text(summary)

            await publish_news(translated_title, translated_summary, link, published, image)
            await mark_as_published(link)
