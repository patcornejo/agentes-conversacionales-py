import os
import llm.open_ai

ACTIVE_LLM = os.environ.get("ACTIVE_LLM", 'openai')

def get_answer(msg: str) -> str or None:
    match ACTIVE_LLM:
        case "openai":
            return open_ai.get_answer(msg)
    return None
