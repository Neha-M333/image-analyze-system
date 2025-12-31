const chat = document.getElementById("chat");
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const progress = document.getElementById("progress");
const quotaInfo = document.getElementById("quotaInfo");

let imageFile = null;
let chatLog = [];
let theme = "light";

function timestamp() {
  return new Date().toLocaleTimeString();
}

function addMessage(text, type) {
  const div = document.createElement("div");
  div.className = `message ${type}`;

  const content = document.createElement("div");
  content.innerText = text;

  const time = document.createElement("div");
  time.className = "timestamp";
  time.innerText = timestamp();

  div.appendChild(content);
  div.appendChild(time);
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;

  chatLog.push(`[${type.toUpperCase()} ${time.innerText}] ${text}`);
}

imageInput.addEventListener("change", () => {
  imageFile = imageInput.files[0];
  preview.src = URL.createObjectURL(imageFile);
  preview.style.display = "block";
  addMessage("Image uploaded successfully.", "system");
});

async function generateExplanation() {
  if (!imageFile) return;

  addMessage("Explain this image.", "user");
  progress.style.display = "block";

  const formData = new FormData();
  formData.append("image", imageFile);

  const res = await fetch("http://127.0.0.1:8000/explain-image", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  progress.style.display = "none";

  addMessage(data.result, "ai");
  quotaInfo.innerText = `${data.used} / 20`;
}

async function askQuestion() {
  const question = document.getElementById("question").value;
  if (!imageFile || !question) return;

  addMessage(question, "user");
  document.getElementById("question").value = "";
  progress.style.display = "block";

  const formData = new FormData();
  formData.append("image", imageFile);
  formData.append("question", question);

  const res = await fetch("http://127.0.0.1:8000/ask-question", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  progress.style.display = "none";

  addMessage(data.result, "ai");
  quotaInfo.innerText = `${data.used} / 20`;
}

function resetChat() {
  chat.innerHTML = "";
  preview.style.display = "none";
  imageInput.value = "";
  imageFile = null;
  chatLog = [];
  addMessage("New image session started.", "system");
}

function exportChat() {
  const blob = new Blob([chatLog.join("\n\n")], { type: "text/plain" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "image_chat_log.txt";
  link.click();
}

function toggleTheme() {
  const body = document.body;
  theme = body.classList.contains("light") ? "dark" : "light";
  body.className = theme;
}
