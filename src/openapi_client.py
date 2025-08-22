from config import OPENAI_API_KEY
from openai import AsyncOpenAI, OpenAIError
import asyncio
class OpenAIClient:
    def __init__(self):
        self._client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def ask(self, user_message, system_prompt: str = "You are a helpful assistant") -> str:
        try:
            response = await self._client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            # logging here
            raise
