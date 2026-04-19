"""
modules/code_generator.py
Generates new code from a natural-language description.
"""

from grok_client import call_grok
from utils import load_prompt, format_user_input


def generate_code(user_message: str, code: str = ""):
    """
    Generate code from a description or requirement.

    Yields:
        Streaming text chunks from Grok.
    """
    system_prompt = load_prompt("generate.txt")
    user_input    = format_user_input("generate", user_message, code)
    yield from call_grok(system_prompt, user_input, stream=True)