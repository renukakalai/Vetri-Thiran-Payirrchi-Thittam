"""
QnA Module — uses the new google-genai Interactions API.
"""
from config import gemini_client, GEMINI_MODEL


def answer_question_with_gemini(question: str) -> str:
    if not question or not question.strip():
        return "⚠️ Please provide a question."

    try:
        interaction = gemini_client.interactions.create(
            model=GEMINI_MODEL,
            input=question.strip(),
        )
        return interaction.output_text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"