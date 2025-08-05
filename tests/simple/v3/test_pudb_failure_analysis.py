#!/usr/bin/env python3
"""Detailed analysis of EXACTLY where Pydantic breaks without model_rebuild().

This shows the precise coverage and process of the failure.
"""

from pathlib import Path
import sys
import traceback


# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))


# Step 1: Show what happens during class definition

try:
    from haive.agents.simple.agent_v3 import SimpleAgentV3
    from haive.core.engine.aug_llm import AugLLMConfig

except Exception:
    traceback.print_exc()
    sys.exit(1)

# Step 2: Show what happens during instance creation

try:
    engine = AugLLMConfig(name="test_engine", temperature=0.1)

    # This is where it breaks
    agent = SimpleAgentV3(name="test_agent", engine=engine)

except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()

    # Get the exact frame where it fails
    frames = traceback.extract_tb(exc_traceback)
    for _i, frame in enumerate(frames):
        filename = Path(frame.filename).name

        # Identify the exact breaking point
        if (
            "mock_val_ser" in frame.filename
            or ("main.py" in frame.filename and "__init__" in frame.name)
            or "test_pudb_failure_analysis.py" in filename
        ):
            pass
