"""
modules/explainer.py
Explains code clearly with ASCII diagrams or structured breakdowns.
"""

from grok_client import call_grok
from utils import load_prompt, format_user_input


def explain_code(user_message: str, code: str = ""):
    """
    Explain how code works, step by step, with visual aids where possible.

    Yields:
        Streaming text chunks from Grok.
    """
    system_prompt = load_prompt("explain.txt")
    user_input    = format_user_input("explain", user_message, code)
    yield from call_grok(system_prompt, user_input, stream=True)