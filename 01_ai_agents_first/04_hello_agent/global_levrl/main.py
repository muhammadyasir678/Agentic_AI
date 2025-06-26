from agents import Agent, Runner, AsyncOpenAI
from agents import set_default_openai_client, set_tracing_disabled, set_default_openai_api
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api("chat_completions")

client_provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
    
set_default_openai_client(client_provider)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model="gemini-2.0-flash",
)

result = Runner.run_sync(agent, "What is a class in Python, and how do you use it?")
print(result.final_output)