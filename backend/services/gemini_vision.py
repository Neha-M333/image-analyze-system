import base64
from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_image(image_bytes: bytes, prompt: str) -> str:
    """
    Sends image and prompt to Gemini Vision (correct base64 encoding)
    """
    try:
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": prompt},
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": image_base64,
                            }
                        },
                    ],
                }
            ],
        )

        if not response.text:
            return "No meaningful response generated from the image."

        return response.text

    except Exception as e:
        print("Gemini API error:", e)
        return "Image analysis service is temporarily unavailable. Please try again later."
