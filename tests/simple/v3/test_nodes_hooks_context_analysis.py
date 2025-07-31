#!/usr/bin/env python3
"""Analysis of nodes context, hooks representation, and message transformer issues.

Understanding future references as strings in the context of:
1. Nodes and their relationships
2. What hooks really represent
3. Message transformer issues compared to v2
"""

from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))


# ========================================================================
# PART 1: NODES CONTEXT - What are the actual node relationships?
# ========================================================================


try:
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.core.graph.node.engine_node import EngineNodeConfig
    from haive.core.graph.node.validation_node_v2 import ValidationNodeV2

    # Current approach - what SimpleAgentV3 actually uses
    engine = AugLLMConfig(name="test_engine")
    engine_node = EngineNodeConfig(name="agent_node", engine=engine)
    validation_node = ValidationNodeV2(name="validation_v2")

    # Check forward references in node configs

except Exception:
    pass

# ========================================================================
# PART 2: WHAT HOOKS REALLY REPRESENT
# ========================================================================


try:
    from haive.agents.base.pre_post_agent_mixin import MessageTransformer

    # Test hook context creation

    # Test message transformer
    transformer = MessageTransformer(transformation_type="reflection")

except Exception:
    pass

# ========================================================================
# PART 3: MESSAGE TRANSFORMER V2 ISSUE
# ========================================================================


try:
    from langchain_core.messages import AIMessage

    from haive.agents.base.pre_post_agent_mixin import MessageTransformer

    # Test the current transformer
    transformer = MessageTransformer(transformation_type="reflection")

    # Create test AI message with tool calls (like ValidationNodeV2 produces)
    ai_msg = AIMessage(
        content="I need to use a tool",
        tool_calls=[
            {"name": "calculator", "args": {"expression": "2+2"}, "id": "call_123"}
        ],
        additional_kwargs={"engine_name": "test_engine"},
        response_metadata={"model": "gpt-4"},
    )

    # Transform the message
    transformed = transformer.transform_messages([ai_msg])

    if transformed:
        result_msg = transformed[0]

        # This is the problem!
        if hasattr(ai_msg, "tool_calls") and ai_msg.tool_calls:
            if not hasattr(result_msg, "tool_calls") or not result_msg.tool_calls:
                pass

        if hasattr(ai_msg, "response_metadata") and ai_msg.response_metadata:
            if (
                not hasattr(result_msg, "response_metadata")
                or not result_msg.response_metadata
            ):
                pass

except Exception:
    import traceback

    traceback.print_exc()

# ========================================================================
# PART 4: FORWARD REFERENCES IN NODE CONTEXT
# ========================================================================
