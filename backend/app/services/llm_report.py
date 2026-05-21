import os

from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

client = MistralClient(api_key=api_key)

def generate_report(events):

    prompt = f"""
    Analyze the following interview proctoring events.

    Events:
    {events}

    Generate:
    1. Suspicion level
    2. Violations
    3. Professional cheating report
    """

    response = client.chat(
        model="open-mistral-7b",
        messages=[
            ChatMessage(
                role="user",
                content=prompt
            )
        ]
    )

    return response.choices[0].message.content