import streamlit as st
from services.gemini_vision import analyze_image
from prompts.vision_prompts import image_description_prompt, image_qa_prompt
from PIL import Image

st.set_page_config(
    page_title="Image Understanding System",
    layout="centered"
)

# -------------------- SESSION STATE --------------------
if "explanation" not in st.session_state:
    st.session_state.explanation = None

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []   # stores multiple Q&A
# ------------------------------------------------------

# Title & Description
st.title("Image Explanation and Visual Question Answering System")
st.write(
    "Upload an image to get a detailed explanation and ask multiple questions "
    "based on the same image."
)

# Image Upload
uploaded_file = st.file_uploader(
    "Upload an image (JPG or PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is None:
    st.info("Please upload an image to proceed.")
    st.stop()

# Image Preview
image = Image.open(uploaded_file)
st.image(image, caption="Uploaded Image", use_column_width=True)

image_bytes = uploaded_file.getvalue()

# ================= IMAGE EXPLANATION =================
st.markdown("---")
st.subheader("Image Explanation")

if st.button("Generate Image Explanation"):
    with st.spinner("Generating image explanation..."):
        try:
            prompt = image_description_prompt()
            st.session_state.explanation = analyze_image(image_bytes, prompt)
        except Exception:
            st.error("Failed to generate image explanation.")

# Show explanation (persistent)
if st.session_state.explanation:
    st.success("Image Explanation")
    st.markdown(st.session_state.explanation)

# ================= IMAGE QUESTION ANSWERING =================
st.markdown("---")
st.subheader("Ask Questions About the Image")

question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Answering your question..."):
            try:
                prompt = image_qa_prompt(question)
                answer = analyze_image(image_bytes, prompt)

                # Store Q&A pair
                st.session_state.qa_history.append({
                    "question": question,
                    "answer": answer
                })
            except Exception:
                st.error("Failed to answer the question.")

# ================= DISPLAY Q&A HISTORY =================
if st.session_state.qa_history:
    st.markdown("---")
    st.subheader("Question & Answer History")

    for i, qa in enumerate(st.session_state.qa_history, start=1):
        st.markdown(f"**Q{i}:** {qa['question']}")
        st.markdown(f"**A{i}:** {qa['answer']}")
