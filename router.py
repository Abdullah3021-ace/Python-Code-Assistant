"""
router.py — Routes the selected tag to the correct module and returns a streaming response.
"""

from modules.error_handler   import handle_error
from modules.code_improver   import improve_code
from modules.code_generator  import generate_code
from modules.ui_helper       import help_ui
from modules.idea_generator  import generate_ideas
from modules.explainer       import explain_code


ROUTE_MAP = {
    "error":    handle_error,
    "improve":  improve_code,
    "generate": generate_code,
    "ui":       help_ui,
    "ideas":    generate_ideas,
    "explain":  explain_code,
}


def route(tag: str, user_message: str, code: str = ""):
    """
    Route the request to the appropriate module.

    Args:
        tag:          One of the six tag keys defined in config.TAGS.
        user_message: The user's natural-language query.
        code:         Optional code snippet the user pasted.

    Yields:
        Text chunks from the Grok streaming response.
    """
    handler = ROUTE_MAP.get(tag)
    if handler is None:
        yield f"❌ Unknown tag: `{tag}`. Please select a valid mode."
        return

    yield from handler(user_message, code)