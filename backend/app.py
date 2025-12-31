from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from services.gemini_vision import analyze_image
from prompts.vision_prompts import image_description_prompt, image_qa_prompt

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Quota tracking (ESTIMATED)
API_LIMIT = 20
api_usage = 0

@app.post("/explain-image")
async def explain_image(image: UploadFile = File(...)):
    global api_usage
    api_usage += 1

    image_bytes = await image.read()
    result = analyze_image(image_bytes, image_description_prompt())

    return {
        "result": result,
        "used": api_usage,
        "remaining": max(0, API_LIMIT - api_usage)
    }

@app.post("/ask-question")
async def ask_question(
    image: UploadFile = File(...),
    question: str = Form(...)
):
    global api_usage
    api_usage += 1

    image_bytes = await image.read()
    result = analyze_image(image_bytes, image_qa_prompt(question))

    return {
        "result": result,
        "used": api_usage,
        "remaining": max(0, API_LIMIT - api_usage)
    }
