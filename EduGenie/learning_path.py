"""
Learning Path Module — uses the new google-genai Interactions API.
"""
import traceback
from config import gemini_client, GEMINI_MODEL


def get_learning_recommendations(topic: str) -> str:
    if not topic or not topic.strip():
        return "⚠️ Please provide a topic."

    prompt = f"""
You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics,
order of learning, and resources (videos, articles, books).
Include beginner, intermediate, and advanced levels if needed.
"""

    try:
        interaction = gemini_client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt,
        )
        print("🔎 Gemini raw response received.")
        text = interaction.output_text
        if text and text.strip():
            return text
        return "❌ Could not extract content from Gemini response."
    except Exception as e:
        traceback.print_exc()
        return f"❌ Error occurred: {str(e)}"