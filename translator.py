import os
import httpx
import google.generativeai as genai

# Конфігурація Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-pro")

async def translate_with_gpt(text: str) -> str:
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Переклади українською максимально точно:"},
            {"role": "user", "content": text}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

async def translate_with_gemini(text: str) -> str:
    prompt = f"Переклади наступний текст українською мовою:

{text}"
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

async def translate_text(text: str) -> str:
    try:
        return await translate_with_gpt(text)
    except Exception:
        return await translate_with_gemini(text)
