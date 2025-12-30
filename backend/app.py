import streamlit as st
from services.gemini_vision import analyze_image
from prompts.vision_prompts import image_description_prompt, image_qa_prompt
from PIL import Image
import io

st.set_page_config(page_title="Image Understanding System", layout="centered")

st.title("Image Explanation and Visual Question Answering")
st.write("Upload an image and ask a question to understand its content.")

uploaded_file = st.file_uploader(
    "Upload an image (JPG or PNG)",
    type=["jpg", "jpeg", "png"]
)

question = st.text_input(
    "Ask a question about the image (optional for explanation)"
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Image"):
        with st.spinner("Analyzing image..."):
            try:
                image_bytes = uploaded_file.getvalue()

                if question.strip():
                    prompt = image_qa_prompt(question)
                else:
                    prompt = image_description_prompt()

                result = analyze_image(image_bytes, prompt)

                st.subheader("Result")
                st.markdown(result)

            except Exception:
                st.error("Something went wrong while analyzing the image.")
