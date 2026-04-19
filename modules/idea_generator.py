"""
modules/idea_generator.py
Brainstorms and expands project ideas.
"""

from grok_client import call_grok
from utils import load_prompt, format_user_input


def generate_ideas(user_message: str, code: str = ""):
    """
    Generate creative project ideas and expand on concepts.

    Yields:
        Streaming text chunks from Grok.
    """
    system_prompt = load_prompt("ideas.txt")
    user_input    = format_user_input("ideas", user_message, code)
    yield from call_grok(system_prompt, user_input, stream=True)