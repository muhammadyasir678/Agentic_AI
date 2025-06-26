from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

def gemini1():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[
            {"content": "Hello, how are you?", "role": "user"}
        ]
    )

    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[
            {"content": "Hello, how are you?", "role": "user"}
        ]
    )

    print(response)