#!/usr/bin/env python3
"""Trace EXACTLY where and how the Pydantic validation breaks without model_rebuild().

This will show the precise call stack and failure point.
"""

from pathlib import Path
import sys
import traceback


# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))


try:
    from haive.agents.simple.agent_v3 import SimpleAgentV3
    from haive.core.engine.aug_llm import AugLLMConfig

except Exception:
    traceback.print_exc()
    sys.exit(1)

try:
    engine = AugLLMConfig(name="test_engine", temperature=0.1)
except Exception:
    traceback.print_exc()
    sys.exit(1)


try:
    # This is where it should break
    agent = SimpleAgentV3(name="test_agent", engine=engine)

except Exception:
    traceback.print_exc()

    # Get the exception details
    exc_type, exc_value, exc_traceback = sys.exc_info()

    for _i, frame_summary in enumerate(traceback.extract_tb(exc_traceback)):
        filename = Path(frame_summary.filename).name

    if (
        "PydanticUserError" in str(exc_type)
        or "AttributeError" in str(exc_type)
        or "ValidationError" in str(exc_type)
    ):
        pass
    else:
        pass

    last_frame = traceback.extract_tb(exc_traceback)[-1]
