"""
EduGenie — FastAPI Backend
Google Gemini Powered Learning Assistant
"""
from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import APP_TITLE, APP_DESCRIPTION, APP_VERSION
from explanation_module import explain_topic
from qna import answer_question_with_gemini
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ---------------- ROOT ----------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main HTML page."""
    return templates.TemplateResponse("index.html", {"request": request})


# ---------------- Q&A ----------------
@app.get("/qa")
async def qa_api(question: str = Query(..., description="User question")):
    answer = answer_question_with_gemini(question)
    return {"question": question, "answer": answer}


# ---------------- Explanation ----------------
@app.post("/explain")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(
            content={"error": "Please provide a topic."}, status_code=400
        )
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}


# ---------------- Summarization ----------------
@app.post("/summarize")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(
            content={"error": "Please provide text to summarize."}, status_code=400
        )
    summary = summarize_text(text)
    return {"summary": summary}


# ---------------- Quiz Generation ----------------
@app.post("/quiz")
async def quiz_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(
            content={"error": "Please provide text for quiz."}, status_code=400
        )
    quiz = generate_quiz(text)
    print("Generated quiz:", quiz)
    return JSONResponse(content={"quiz": quiz})


# ---------------- Learning Recommendations ----------------
@app.get("/learn/recommendations")
async def learning_recommendation_api(
    topic: str = Query(..., description="Topic to learn")
):
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}


# ---------------- Health Check ----------------
@app.get("/health")
async def health():
    return {"status": "ok", "app": APP_TITLE, "version": APP_VERSION}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)