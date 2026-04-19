"""
grok_client.py — Handles all calls to the Grok API (OpenAI-compatible endpoint)
"""

from openai import OpenAI
from config import GROK_API_KEY, GROK_BASE_URL, GROK_MODEL, MAX_TOKENS, TEMPERATURE


def get_client() -> OpenAI:
    """Return a configured OpenAI-compatible client pointing at x.ai."""
    return OpenAI(
        api_key="GROQ_API_KEY",
        base_url="https://api.groq.com/openai/v1",
    )


def call_grok(system_prompt: str, user_message: str, stream: bool = True):
    """
    Call Grok-3 with a system prompt and user message.

    Args:
        system_prompt: The module-specific system prompt.
        user_message:  The user's query / code input.
        stream:        If True, returns a streaming generator; otherwise full text.

    Returns:
        Generator of text chunks (stream=True) or full response string (stream=False).
    """
    client = get_client()

    messages = [
        {"role": "system",  "content": system_prompt},
        {"role": "user",    "content": user_message},
    ]

    if stream:
        response = client.chat.completions.create(
            model=GROK_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            stream=True,
        )
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                yield delta.content
    else:
        response = client.chat.completions.create(
            model=GROK_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            stream=False,
        )
        return response.choices[0].message.content