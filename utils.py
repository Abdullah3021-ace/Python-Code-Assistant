"""
utils.py — Shared helper utilities
"""

import os
import re
from config import PROMPTS_DIR


# ── Prompt loader ─────────────────────────────────────────────────────────────

def load_prompt(filename: str) -> str:
    """Load a prompt template from the prompts/ directory."""
    path = os.path.join(PROMPTS_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return f"You are a helpful AI code assistant. Answer the user's query about: {filename.replace('.txt', '')}."


# ── Code block extraction ─────────────────────────────────────────────────────

def extract_code_blocks(text: str) -> list[dict]:
    """
    Extract all fenced code blocks from markdown text.
    Returns a list of dicts: [{"lang": "python", "code": "..."}, ...]
    """
    pattern = r"```(\w*)\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [{"lang": lang or "text", "code": code.strip()} for lang, code in matches]


# ── Text sanitisation ─────────────────────────────────────────────────────────

def truncate(text: str, max_chars: int = 8000) -> str:
    """Truncate text to avoid exceeding token limits."""
    if len(text) > max_chars:
        return text[:max_chars] + "\n\n[... truncated for length ...]"
    return text


# ── Format helpers ────────────────────────────────────────────────────────────

def format_user_input(tag: str, user_text: str, code: str = "") -> str:
    """Build a well-structured user message combining description and code."""
    parts = [user_text.strip()]
    if code.strip():
        parts.append(f"\n\n```\n{truncate(code.strip())}\n```")
    return "\n".join(parts)