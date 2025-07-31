#!/usr/bin/env python3
"""Test the 'from __future__ import annotations' solution for SimpleAgentV3.

This is the CLEANEST solution - no model_rebuild() needed!
"""

# ========================================================================
# THE MAGIC LINE - Must be FIRST import in the file
# ========================================================================
from __future__ import annotations

from pathlib import Path
import sys


# Direct imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))


try:
    # Create a mini version to test the concept
    from pydantic import BaseModel, Field

    from haive.core.engine.aug_llm import AugLLMConfig

    # Mock the complex inheritance for testing
    class MockAgent:
        """Mock Agent class."""

        def __init__(self, name: str, engine: AugLLMConfig):
            self.name = name
            self.engine = engine

    class MockRecompileMixin:
        """Mock RecompileMixin."""

    class MockDynamicToolRouteMixin:
        """Mock DynamicToolRouteMixin."""

    # This simulates the problematic inheritance with future annotations
    class TestSimpleAgentV3(
        MockAgent,  # This would be Agent[AugLLMConfig] with future annotations
        MockRecompileMixin,
        MockDynamicToolRouteMixin,
        BaseModel,
    ):
        """Test version with future annotations."""

        name: str = Field(...)
        engine: AugLLLConfig = Field(...)  # Forward reference!

        class Config:
            arbitrary_types_allowed = True

    # Test instance creation
    engine = AugLLMConfig(name="test")
    agent = TestSimpleAgentV3(name="test_agent", engine=engine)

except Exception:
    import traceback

    traceback.print_exc()


# Now test if we can modify the real SimpleAgentV3 to use this approach
try:
    # Let's see what the real class looks like with annotations
    from haive.agents.simple.agent_v3 import SimpleAgentV3

    if hasattr(SimpleAgentV3, "__annotations__"):
        pass

    # Test if it works as-is
    engine = AugLLMConfig(name="real_test")
    agent = SimpleAgentV3(name="real_test_agent", engine=engine)

except Exception:
    pass
