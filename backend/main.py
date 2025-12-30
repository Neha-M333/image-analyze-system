from utils.image_utils import validate_and_prepare_image
from services.gemini_vision import analyze_image
from prompts.vision_prompts import (
    image_description_prompt,
    image_qa_prompt
)

IMAGE_PATH = "sample.jpg"  # replace with your image path


def run_image_description():
    image_bytes = validate_and_prepare_image(IMAGE_PATH)
    prompt = image_description_prompt()
    result = analyze_image(image_bytes, prompt)
    print("\nIMAGE DESCRIPTION:\n")
    print(result)


def run_image_question_answering():
    question = input("\nEnter your question about the image: ").strip()

    if not question:
        print("Question cannot be empty.")
        return

    image_bytes = validate_and_prepare_image(IMAGE_PATH)
    prompt = image_qa_prompt(question)
    result = analyze_image(image_bytes, prompt)
    print("\nANSWER:\n")
    print(result)


if __name__ == "__main__":
    print("1. Image Description")
    print("2. Image Question Answering")
    choice = input("Choose option (1/2): ")

    if choice == "1":
        run_image_description()
    elif choice == "2":
        run_image_question_answering()
    else:
        print("Invalid choice.")
