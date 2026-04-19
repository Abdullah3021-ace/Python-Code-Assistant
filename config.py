"""
config.py — API keys and global settings
"""

import os
# ── Grok API ────────────────────────────────────────────────────────────────
GROK_API_KEY = os.getenv("GROK_API_KEY", "GROQ_API_KEY)")
GROK_BASE_URL = "https://api.groq.com/openai/v1"
GROK_MODEL = "allam-2-7b"
MAX_TOKENS = 2048
TEMPERATURE = 0.7

# ── App metadata ─────────────────────────────────────────────────────────────
APP_TITLE = "AI Code Assistant"
APP_ICON  = "⚡"
VERSION   = "1.0.0"

# ── Prompts directory ────────────────────────────────────────────────────────
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")

# ── Module / tag config ──────────────────────────────────────────────────────
TAGS = {
    "error": {
        "label":       "Error",
        "icon":        "🐛",
        "description": "Fix and debug code",
        "color":       "#ef4444",
        "prompt_file": "error.txt",
    },
    "improve": {
        "label":       "Improve",
        "icon":        "🚀",
        "description": "Optimize and refactor code",
        "color":       "#3b82f6",
        "prompt_file": "improve.txt",
    },
    "generate": {
        "label":       "Generate",
        "icon":        "⚙️",
        "description": "Generate code from description",
        "color":       "#10b981",
        "prompt_file": "generate.txt",
    },
    "ui": {
        "label":       "UI",
        "icon":        "🎨",
        "description": "Design and build UI components",
        "color":       "#8b5cf6",
        "prompt_file": "ui.txt",
    },
    "ideas": {
        "label":       "Ideas",
        "icon":        "💡",
        "description": "Brainstorm project ideas",
        "color":       "#f59e0b",
        "prompt_file": "ideas.txt",
    },
    "explain": {
        "label":       "Explain",
        "icon":        "📊",
        "description": "Explain code with visuals",
        "color":       "#06b6d4",
        "prompt_file": "explain.txt",
    },
}