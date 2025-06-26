import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv
import os

set_tracing_disabled(disabled=True)
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("BASE_URL")

MODEL="deepseek/deepseek-r1-0528-qwen3-8b:free"

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(
            model=MODEL,
            openai_client=client,)
    )

    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())