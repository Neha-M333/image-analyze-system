def image_description_prompt():
    return (
        "Analyze the image and provide a clear, detailed explanation of "
        "what is visible. Describe objects, actions, and overall context."
    )

def image_qa_prompt(question: str):
    return (
        f"Based only on the image, answer the following question:\n{question}"
    )
