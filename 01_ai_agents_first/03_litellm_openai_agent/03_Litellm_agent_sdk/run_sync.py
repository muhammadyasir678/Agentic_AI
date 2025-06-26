from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
import os
set_tracing_disabled(disabled=True)

load_dotenv()

MODEL = 'gemini/gemini-2.0-flash'
gemini_api_key = os.getenv('GEMINI_API_KEY')

@function_tool
def get_weather(city: str)->str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


def main(model: str, api_key: str):
  agent = Agent(
      name="Assistant",
      instructions="You only respond in haikus.",
      model=LitellmModel(model=model, api_key=api_key),

  )

  result = Runner.run_sync(agent, "What's the weather in Tokyo?")
  print(result.final_output)


main(model=MODEL, api_key=gemini_api_key)