"""
modules/ui_helper.py
Helps design, critique, or build UI/UX components and layouts.
"""

from grok_client import call_grok
from utils import load_prompt, format_user_input


def help_ui(user_message: str, code: str = ""):
    """
    Assist with UI/UX design questions and frontend code.

    Yields:
        Streaming text chunks from Grok.
    """
    system_prompt = load_prompt("ui.txt")
    user_input    = format_user_input("ui", user_message, code)
    yield from call_grok(system_prompt, user_input, stream=True)