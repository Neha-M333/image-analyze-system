const imageInput = document.getElementById("imageInput");
const imagePreview = document.getElementById("imagePreview");

const explainBtn = document.getElementById("explainBtn");
const askBtn = document.getElementById("askBtn");

const explainLoading = document.getElementById("explainLoading");
const qaLoading = document.getElementById("qaLoading");

const explanationDiv = document.getElementById("explanation");
const qaHistoryDiv = document.getElementById("qaHistory");
const errorDiv = document.getElementById("error");

const questionInput = document.getElementById("questionInput");

let imageFile = null;

/* ---------------- Image Preview ---------------- */
imageInput.addEventListener("change", () => {
    imageFile = imageInput.files[0];
    if (!imageFile) return;

    const reader = new FileReader();
    reader.onload = () => {
        imagePreview.src = reader.result;
        imagePreview.style.display = "block";
    };
    reader.readAsDataURL(imageFile);
});

/* ---------------- Image Explanation ---------------- */
explainBtn.addEventListener("click", async () => {
    if (!imageFile) {
        errorDiv.innerText = "Please upload an image.";
        return;
    }

    errorDiv.innerText = "";
    explainLoading.style.display = "block";

    const formData = new FormData();
    formData.append("image", imageFile);

    try {
        const response = await fetch("http://localhost:8000/explain", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        explanationDiv.innerText = data.explanation;
    } catch {
        errorDiv.innerText = "Failed to generate explanation.";
    } finally {
        explainLoading.style.display = "none";
    }
});

/* ---------------- Question Answering ---------------- */
askBtn.addEventListener("click", async () => {
    const question = questionInput.value.trim();

    if (!imageFile || question === "") {
        errorDiv.innerText = "Upload an image and enter a question.";
        return;
    }

    errorDiv.innerText = "";
    qaLoading.style.display = "block";

    const formData = new FormData();
    formData.append("image", imageFile);
    formData.append("question", question);

    try {
        const response = await fetch("http://localhost:8000/ask", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        const qaItem = document.createElement("div");
        qaItem.classList.add("output");
        qaItem.innerHTML = `<strong>Q:</strong> ${question}<br><strong>A:</strong> ${data.answer}`;

        qaHistoryDiv.appendChild(qaItem);
        questionInput.value = "";
    } catch {
        errorDiv.innerText = "Failed to answer question.";
    } finally {
        qaLoading.style.display = "none";
    }
});
