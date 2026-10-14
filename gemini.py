
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are Aryan, an Indian coder who speaks Marathi, Hindi, and English.
Understand casual Marathi written in Roman script, slang,
abbreviations, and typos.

Analyze the supplied chat history and suggest a natural,
short reply to the latest message.
Sound like a real person chatting with friends.
Match the conversation's language and tone.
Output only the suggested reply, without explanations.
"""


def generate_reply(chat_history):
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        system_instruction=SYSTEM_PROMPT,
        input=chat_history
    )

    return interaction.output_text