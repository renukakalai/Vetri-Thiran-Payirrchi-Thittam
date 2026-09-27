"""
Configuration file for EduGenie.
Uses the NEW google-genai SDK (Interactions API).
"""
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "❌ GEMINI_API_KEY not found. Please add it to your .env file."
    )

# ✅ NEW SDK: create a shared client
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# ✅ NEW model name (as per updated Google docs)
GEMINI_MODEL = "gemini-3.5-flash-lite"

# Local model for explanations
LOCAL_MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"

# App metadata
APP_TITLE = "EduGenie"
APP_DESCRIPTION = "Google Gemini Powered Learning Assistant"
APP_VERSION = "1.0.0"