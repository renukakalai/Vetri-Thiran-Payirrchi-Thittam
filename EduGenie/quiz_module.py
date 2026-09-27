"""
Quiz Module — uses the new google-genai Interactions API.
"""
import re
import json
from config import gemini_client, GEMINI_MODEL


def clean_json_block(text: str) -> str:
    """Remove Markdown code fences (```json ... ```) from a string."""
    return re.sub(r"(?i)```(?:json)?\n?(.*?)```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    if not text or not text.strip():
        return [{"error": "Please provide text for the quiz."}]

    prompt = f"""
You are a quiz generator.

From the following passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""

    try:
        interaction = gemini_client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt,
        )
        quiz_text = interaction.output_text.strip()
        cleaned_text = clean_json_block(quiz_text)
        quiz_list = json.loads(cleaned_text)

        if not isinstance(quiz_list, list):
            raise ValueError("Model did not return a JSON list.")

        return quiz_list
    except json.JSONDecodeError as e:
        return [{"error": f"Failed to parse quiz JSON: {e}"}]
    except Exception as e:
        return [{"error": f"Error generating quiz: {e}"}]