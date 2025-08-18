import asyncio
import base64

# Some javascript we will run on each step
# to take a screenshot of the page, select the
# elements to annotate, and add bounding boxes
from pathlib import Path

from langchain_core.runnables import chain

# Find the mark.js file relative to this module
current_dir = Path(__file__).parent
mark_js_path = current_dir.parent / "web_nav" / "utils" / "mark.js"

if mark_js_path.exists():
    with open(mark_js_path) as f:
        mark_page_script = f.read()
else:
    # Fallback if file doesn't exist
    mark_page_script = "// mark.js not found"


@chain
async def mark_page(page):
    """Mark Page.

    Args:
        page: [TODO: Add description]
    """
    await page.evaluate(mark_page_script)
    for _ in range(10):
        try:
            bboxes = await page.evaluate("markPage()")
            break
        except Exception:
            # May be loading...
            asyncio.sleep(3)
    screenshot = await page.screenshot()
    # Ensure the bboxes don't follow us around
    await page.evaluate("unmarkPage()")
    return {
        "img": base64.b64encode(screenshot).decode(),
        "bboxes": bboxes,
    }


def parse(text: str) -> dict:
    """Parse.

    Args:
        text: [TODO: Add description]

    Returns:
        [TODO: Add return description]
    """
    action_prefix = "Action: "
    if not text.strip().split("\n")[-1].startswith(action_prefix):
        return {"action": "retry", "args": f"Could not parse LLM Output: {text}"}
    action_block = text.strip().split("\n")[-1]

    action_str = action_block[len(action_prefix) :]
    split_output = action_str.split(" ", 1)
    if len(split_output) == 1:
        action, action_input = split_output[0], None
    else:
        action, action_input = split_output
    action = action.strip()
    if action_input is not None:
        action_input = [
            inp.strip().strip("[]") for inp in action_input.strip().split(";")
        ]
    return {"action": action, "args": action_input}
