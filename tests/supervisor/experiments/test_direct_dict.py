"""Test direct dict approach to understand the issue."""

import contextlib
from typing import Any

from pydantic import BaseModel, Field


# Test with a simple base model first
class SimpleState(BaseModel):
    agents: dict[str, Any] = Field(default_factory=dict)
    model_config = {"arbitrary_types_allowed": True}


class TestAgent:
    def __init__(self, name):
        self.name = name


def test_simple():
    """Test with simple models."""
    # Create test agent
    agent = TestAgent("test")

    # Test 1: Direct dict with Any
    with contextlib.suppress(Exception):
        SimpleState(agents={"test": agent})

    # Test 2: Let's try with AgentInfo type annotation
    from agent_info import AgentInfo

    class TypedState(BaseModel):
        agents: dict[str, AgentInfo] = Field(default_factory=dict)
        model_config = {"arbitrary_types_allowed": True}

    try:
        # Create AgentInfo
        info = AgentInfo(agent=agent, name="test", description="Test agent")
        TypedState(agents={"test": info})
    except Exception:
        pass

    # Test 3: With inheritance
    from haive.core.schema.prebuilt.messages_state import MessagesState

    class InheritedState(MessagesState):
        agents: dict[str, Any] = Field(default_factory=dict)
        model_config = {"arbitrary_types_allowed": True}

    with contextlib.suppress(Exception):
        InheritedState(agents={"test": agent})


if __name__ == "__main__":
    test_simple()
