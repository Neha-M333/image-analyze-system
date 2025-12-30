import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY is None:
    raise EnvironmentError(
        "GEMINI_API_KEY not found. Please set it in your .env file."
    )
