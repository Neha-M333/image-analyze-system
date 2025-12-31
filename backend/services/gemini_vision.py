import base64
from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_image(image_bytes: bytes, prompt: str) -> str:
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": prompt},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_base64
                        }
                    }
                ]
            }
        ]
    )

    return response.text
