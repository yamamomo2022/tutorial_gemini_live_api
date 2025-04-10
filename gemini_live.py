import asyncio
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options={'api_version': 'v1alpha'})
model = "gemini-2.0-flash-live-001"

config = {"response_modalities": ["TEXT"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        while True:
            message = input("User> ")
            if message.lower() == "exit":
                break
            await session.send(input=message, end_of_turn=True)

            async for response in session.receive():
                if response.text is not None:
                    print(response.text, end="")

if __name__ == "__main__":
    asyncio.run(main())