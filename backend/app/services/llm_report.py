import os
import json

from dotenv import load_dotenv

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

client = MistralClient(api_key=api_key)

def generate_report(session_data):

    prompt = f"""
    You are an AI interview proctoring evaluator.

    Analyze the following session statistics.

    Session Data:
    {json.dumps(session_data, indent=2)}

    Generate:
    1. Overall suspicion level
    2. Detailed violation analysis
    3. Interview behavior summary
    4. Final recommendation

    Keep the report professional and concise.
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