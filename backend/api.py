from fastapi import FastAPI, UploadFile, Form
from services.gemini_vision import analyze_image
from prompts.vision_prompts import image_description_prompt, image_qa_prompt

app = FastAPI()

@app.post("/explain")
async def explain_image(image: UploadFile):
    image_bytes = await image.read()
    prompt = image_description_prompt()
    explanation = analyze_image(image_bytes, prompt)
    return {"explanation": explanation}

@app.post("/ask")
async def ask_question(
    image: UploadFile,
    question: str = Form(...)
):
    image_bytes = await image.read()
    prompt = image_qa_prompt(question)
    answer = analyze_image(image_bytes, prompt)
    return {"answer": answer}
