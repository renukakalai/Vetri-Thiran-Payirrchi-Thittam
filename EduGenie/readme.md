# EduGenie 🧠✨
### Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant that:
- Answers academic questions
- Explains complex concepts simply
- Generates quizzes from text
- Summarizes long passages
- Creates personalized learning paths

---

## Tech Stack
- **Backend:** FastAPI + Uvicorn
- **Frontend:** HTML + CSS + Vanilla JS
- **AI Models:**
  - Google Gemini 1.5 Pro (cloud) — Q&A, Quiz, Summary, Learning Path
  - LaMini-Flan-T5-783M (local) — Concept Explanation
- **Templating:** Jinja2

---

## Quick Start

### 1. Create and activate a virtual environment
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate