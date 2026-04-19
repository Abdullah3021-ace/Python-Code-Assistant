"""
modules/error_handler.py
Fixes bugs, explains errors, and suggests patches.
"""

from grok_client import call_grok
from utils import load_prompt, format_user_input


def handle_error(user_message: str, code: str = ""):
    """
    Analyse code for bugs / runtime errors and provide fixes.

    Yields:
        Streaming text chunks from Grok.
    """
    system_prompt = load_prompt("error.txt")
    user_input    = format_user_input("error", user_message, code)
    yield from call_grok(system_prompt, user_input, stream=True)