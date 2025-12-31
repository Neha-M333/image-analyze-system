# 🖼️ Image Explanation and Visual Question Answering System

> A cloud-based Vision AI system for intelligent image analysis and conversational question answering

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-Academic-yellow.svg)](#)

---

## 📌 Overview

This project implements an **Image Explanation and Visual Question Answering (VQA) System** powered by Google's Gemini Vision API. The system provides a ChatGPT-style interface where users can upload images, receive detailed explanations, and ask multiple natural language questions about the same image.

**Key Highlights:**
- ☁️ Cloud-based vision AI (no local GPU required)
- 💬 Conversational interface with multi-turn QA
- 🎨 Modern UI with light/dark mode
- 🚀 CPU-only system compatible
- 📊 Real-time API usage tracking

---

## 🎯 Features

### Core Functionality
- **📷 Image Upload & Preview** - Support for JPG, PNG, and other common formats
- **🔍 Automatic Image Explanation** - Detailed AI-generated description of uploaded images
- **❓ Multi-Turn Question Answering** - Ask unlimited questions about the same image
- **💾 Context Preservation** - System maintains image context across multiple questions

### User Interface
- **🎨 ChatGPT-Style Interface** - Clean, modern conversational UI
- **🌓 Theme Switching** - Toggle between light and dark modes
- **⏱️ Timestamps** - All messages include timestamp information
- **📢 System Messages** - Clear feedback for uploads and actions
- **💬 Chat History Export** - Download conversation as a text file
- **🔄 Session Reset** - Easy "New Image" button to start fresh

### Technical Features
- **⚡ Fast API Backend** - RESTful API built with FastAPI
- **📊 Usage Monitoring** - Estimated API call counter
- **⏳ Loading Indicators** - Visual feedback during processing
- **🛡️ Error Handling** - Graceful handling of API limits and errors

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────┐
│   Frontend (HTML/CSS/JavaScript)    │
│  - ChatGPT-style UI                 │
│  - Image upload interface           │
│  - Question input & chat display    │
└──────────────┬──────────────────────┘
               │ REST API
               ▼
┌─────────────────────────────────────┐
│    Backend (FastAPI - Python)       │
│  - /explain endpoint                │
│  - /ask endpoint                    │
│  - Request validation               │
└──────────────┬──────────────────────┘
               │ API Calls
               ▼
┌─────────────────────────────────────┐
│    Google Gemini Vision API         │
│  - Image understanding              │
│  - Visual question answering        │
│  - Natural language processing      │
└─────────────────────────────────────┘
```

### Data Flow
1. User uploads an image through the frontend
2. Frontend sends base64-encoded image to backend `/explain` endpoint
3. Backend calls Gemini Vision API with structured prompt
4. API returns detailed image explanation
5. User asks questions via frontend
6. Backend sends image + question to `/ask` endpoint
7. Gemini processes and returns contextual answers
8. Frontend displays responses in chat interface

---

## 💻 Requirements

### Hardware
- **CPU:** Any modern processor (no GPU required)
- **RAM:** Minimum 4 GB, recommended 8 GB+
- **Storage:** ~500 MB for project files and dependencies
- **Internet:** Stable connection for API calls

### Software
- **Python:** 3.10 or higher
- **Web Browser:** Chrome, Edge, Firefox, or Safari (latest versions)
- **Operating System:** Windows, macOS, or Linux

### API Requirements
- Google Gemini API key (free tier available)
- API quota: ~20 requests per minute

---

## 📁 Project Structure

```
image-understanding-system/
│
├── backend/
│   ├── app.py                    # Main FastAPI application
│   ├── services/
│   │   └── gemini_vision.py      # Gemini API integration
│   ├── prompts/
│   │   └── vision_prompts.py     # Prompt templates
│   ├── config/
│   │   └── settings.py           # Configuration & API key loading
│   ├── requirements.txt          # Python dependencies
│   └── .env                      # Environment variables (API key)
│
├── frontend/
│   ├── index.html                # Main UI structure
│   ├── style.css                 # Styling with light/dark themes
│   └── script.js                 # Frontend logic & API calls
│
├── venv/                         # Virtual environment (generated)
│
└── README.md                     # This file
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/image-understanding-system.git
cd image-understanding-system
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

**Dependencies include:**
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `google-generativeai` - Gemini API client
- `python-multipart` - File upload handling
- `python-dotenv` - Environment variable management
- `pillow` - Image processing

### Step 4: Configure API Key

1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

2. Create a `.env` file in the `backend/` directory:
```bash
cd backend
touch .env  # Linux/macOS
# or create manually on Windows
```

3. Add your API key to `.env`:
```env
GEMINI_API_KEY=your_api_key_here
```

⚠️ **Important:** Never commit your `.env` file to version control!

### Step 5: Start the Backend Server
```bash
cd backend
uvicorn app:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

### Step 6: Open the Frontend

Simply open `frontend/index.html` in your web browser:
- **Windows:** Double-click the file or right-click → Open with → Browser
- **macOS:** Double-click or use `open frontend/index.html`
- **Linux:** `xdg-open frontend/index.html`

Alternatively, serve via Python:
```bash
cd frontend
python -m http.server 8080
# Then open http://localhost:8080 in your browser
```

---

## 🚀 Usage Guide

### Basic Workflow

1. **Upload an Image**
   - Click the "Choose Image" button
   - Select an image file (JPG, PNG, etc.)
   - Preview will appear automatically

2. **Get Image Explanation**
   - Click "Explain Image" button
   - Wait for AI-generated description
   - Explanation appears in chat interface

3. **Ask Questions**
   - Type your question in the input box
   - Click "Send" or press Enter
   - Receive contextual answers about the image

4. **Continue Conversation**
   - Ask multiple follow-up questions
   - System maintains image context
   - All responses appear in chat history

5. **Start New Session**
   - Click "New Image" to reset
   - Upload a different image
   - Begin new conversation

### Example Use Cases

**Academic Research:**
- Analyze scientific diagrams and charts
- Identify objects in microscope images
- Understand complex visualizations

**Education:**
- Explain historical photographs
- Analyze artwork and paintings
- Study architectural designs

**General Use:**
- Identify plants and animals
- Understand infographics
- Analyze product images

---

## 🎨 User Interface

### Light Mode
Clean, professional interface with:
- White background
- Dark text for readability
- Blue accent colors
- Subtle shadows

### Dark Mode
Eye-friendly dark theme with:
- Dark gray background
- Light text
- Purple accent colors
- Reduced eye strain

### Chat Interface Elements
- **User Messages:** Right-aligned, blue/purple bubbles
- **AI Responses:** Left-aligned, gray bubbles
- **System Messages:** Centered, italic, muted color
- **Timestamps:** Small text below each message
- **Scrollable History:** Auto-scrolls to latest message

---

## 📊 API Usage & Limits

### Gemini API Free Tier
- **Rate Limit:** ~15-20 requests per minute
- **Daily Quota:** Check [Google AI Studio](https://ai.google.dev/) for current limits
- **Image Size:** Up to 4MB per image
- **Supported Formats:** JPG, PNG, WEBP, GIF

### Usage Monitoring
The application includes an estimated API usage counter that tracks:
- Number of explanation requests
- Number of question requests
- Total API calls in current session

⚠️ **Note:** The counter is client-side only and resets on page reload.

### Rate Limit Handling
If you encounter rate limits:
1. Wait 60 seconds before retrying
2. Reduce frequency of requests
3. Consider upgrading to paid tier for higher limits

---

## 🔧 Configuration

### Backend Configuration (`backend/config/settings.py`)
```python
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"  # or "gemini-pro-vision"
MAX_IMAGE_SIZE = 4 * 1024 * 1024  # 4MB
TEMPERATURE = 0.4
```

### Prompt Customization (`backend/prompts/vision_prompts.py`)
Modify prompt templates to adjust:
- Explanation detail level
- Response tone and style
- Answer format
- Language preferences

---

## 🛠️ Troubleshooting

### Common Issues

**Problem:** Backend won't start
```
Solution: Ensure all dependencies are installed
pip install -r requirements.txt
```

**Problem:** API key error
```
Solution: Check .env file exists and contains valid key
GEMINI_API_KEY=your_actual_key_here
```

**Problem:** Rate limit exceeded
```
Solution: Wait 60 seconds, reduce request frequency
```

**Problem:** Image upload fails
```
Solution: Check image size (<4MB) and format (JPG/PNG)
```

**Problem:** CORS errors in browser
```
Solution: Run frontend through a local server
python -m http.server 8080
```

### Debug Mode
Enable debug logging in `backend/app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 🔐 Security Considerations

- ✅ API keys stored in `.env` file (not in code)
- ✅ `.env` file excluded from git via `.gitignore`
- ✅ No sensitive data logged
- ⚠️ Images processed in memory only (not saved to disk)
- ⚠️ For production: Add authentication and HTTPS

---

## 🚧 Known Limitations

1. **API Dependency:** Requires internet connection
2. **Rate Limits:** Free tier has request quotas
3. **No Persistence:** Chat history cleared on page reload
4. **Single Image:** One image at a time (no batch processing)
5. **No Streaming:** Responses not streamed (appear all at once)

---

## 🔮 Future Enhancements

### Planned Features
- [ ] Video analysis and frame-by-frame QA
- [ ] Batch image processing
- [ ] Persistent chat history (database)
- [ ] User authentication system
- [ ] Streaming responses
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Mobile app version

### Technical Improvements
- [ ] Cloud deployment (AWS/GCP/Azure)
- [ ] Containerization (Docker)
- [ ] Load balancing
- [ ] Caching layer (Redis)
- [ ] WebSocket for real-time updates

---

## 🤝 Contributing

This is an academic project, but contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is developed for **academic and educational purposes only**.

- ✅ Free to use for learning and research
- ✅ Modify and experiment as needed
- ❌ Not for commercial use without proper licensing
- ❌ No redistribution of modified versions without attribution

---

## 🙏 Acknowledgments

- **Google Gemini Team** - For providing the Vision API
- **FastAPI Community** - For excellent documentation
- **Dayananda Sagar University** - For academic support

---

## 📞 Contact & Support

**Author:** Neha M  
**Degree:** B.Tech – Computer Science (AI & ML)  
**Institution:** Dayananda Sagar University  

For questions or issues:
- Open an issue on GitHub
- Email: [your-email@example.com]
- LinkedIn: [Your LinkedIn Profile]

---

## 📚 References

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vision-Language Models Overview](https://arxiv.org/abs/2304.00685)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for academic learning

</div>
