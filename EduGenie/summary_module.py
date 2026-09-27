"""
Summary Module — uses the new google-genai Interactions API.
"""
from config import gemini_client, GEMINI_MODEL


def summarize_text(text: str) -> str:
    if not text or not text.strip():
        return "⚠️ Please provide text to summarize."

    try:
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        interaction = gemini_client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt,
        )
        return interaction.output_text.strip()
    except Exception as e:
        return f"⚠️ Error in Summary: {e}"