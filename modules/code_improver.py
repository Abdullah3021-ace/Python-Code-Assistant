"""
modules/code_improver.py
Optimises, refactors, and improves code quality.
"""

from grok_client import call_grok
from utils import load_prompt, format_user_input


def improve_code(user_message: str, code: str = ""):
    """
    Refactor and optimise the provided code.

    Yields:
        Streaming text chunks from Grok.
    """
    system_prompt = load_prompt("improve.txt")
    user_input    = format_user_input("improve", user_message, code)
    yield from call_grok(system_prompt, user_input, stream=True)