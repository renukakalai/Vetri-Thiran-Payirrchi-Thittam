"""
Explanation Module
Uses LaMini-Flan-T5-783M for explanations; falls back to Gemini.
"""
_explainer_pipeline = None


def _load_local_model():
    global _explainer_pipeline
    if _explainer_pipeline is None:
        try:
            from transformers import pipeline
            print("⏳ Loading LaMini-Flan-T5-783M (first run may take a while)...")
            _explainer_pipeline = pipeline(
                "text2text-generation",
                model="MBZUAI/LaMini-Flan-T5-783M",
                max_length=256,
                do_sample=False,
            )
            print("✅ Local explanation model loaded.")
        except Exception as e:
            print(f"⚠️ Could not load local model: {e}")
            _explainer_pipeline = None
    return _explainer_pipeline


def explain_topic(topic: str) -> str:
    if not topic or not topic.strip():
        return "⚠️ Please provide a topic to explain."

    topic = topic.strip()

    # 1) Try local model first
    pipe = _load_local_model()
    if pipe is not None:
        try:
            prompt = (
                f"Explain the following topic in simple, clear language "
                f"for a beginner: {topic}"
            )
            result = pipe(prompt)
            if result and isinstance(result, list) and "generated_text" in result[0]:
                text = result[0]["generated_text"].strip()
                if text:
                    return text
        except Exception as e:
            print(f"⚠️ Local explanation failed: {e}")

    # 2) Fallback to Gemini (new SDK)
    try:
        from config import gemini_client, GEMINI_MODEL
        prompt = (
            f"Explain the following topic in simple, clear language "
            f"for a beginner: {topic}"
        )
        interaction = gemini_client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt,
        )
        return interaction.output_text.strip()
    except Exception as e:
        return f"⚠️ Error in Explanation: {e}"