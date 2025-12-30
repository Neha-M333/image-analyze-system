def image_description_prompt() -> str:
    return """
You are an AI system specialized in image understanding.

Analyze the given image and provide:
1. A detailed description of all visible objects
2. Actions or interactions taking place
3. The overall context or scene

Explain clearly using simple, academic language.
Do not make assumptions beyond what is visible in the image.
"""


def image_qa_prompt(question: str) -> str:
    return f"""
You are given an image and a user question.

Answer the question strictly based on what is visible in the image.
If the answer cannot be determined from the image, clearly state that.

User Question:
"{question}"
"""
