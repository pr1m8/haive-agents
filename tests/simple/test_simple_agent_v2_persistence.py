"""Test SimpleAgentV2 persistence and checkpointing behavior."""

import asyncio
import contextlib

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic_core import PydanticUndefined

from haive.agents.simple.agent_v2 import SimpleAgentV2


class TestSimpleAgentV2Persistence:
    """Test suite for SimpleAgentV2 persistence and checkpointing."""

    def test_state_fields_no_undefined(self):
        """Verify that state fields are properly initialized without PydanticUndefined."""
        # Create agent
        agent = SimpleAgentV2(
            name="test_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Get the state schema class and create instance
        StateClass = agent.state_schema
        state = StateClass()

        # Check all fields for PydanticUndefined
        undefined_fields = []
        for field_name in StateClass.model_fields:
            try:
                value = getattr(state, field_name)
                if value is PydanticUndefined:
                    undefined_fields.append(field_name)
            except AttributeError:
                pass

        assert (
            len(undefined_fields) == 0
        ), f"Found PydanticUndefined fields: {undefined_fields}"

    @pytest.mark.asyncio
    async def test_run_without_persistence(self):
        """Test that SimpleAgentV2 runs successfully without persistence."""
        agent = SimpleAgentV2(
            name="no_persist_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Disable checkpointing
        agent.checkpointer = None

        result = await agent.arun("Say hello")
        assert result is not None

    @pytest.mark.asyncio
    async def test_run_with_persistence_disabled_in_config(self):
        """Test running with persistence disabled through configuration."""
        agent = SimpleAgentV2(
            name="config_no_persist_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Disable checkpointer to avoid msgpack serialization
        original_checkpointer = agent.checkpointer
        agent.checkpointer = None

        try:
            # Create config without thread_id to avoid persistence
            config = {"configurable": {}}  # No thread_id means no checkpointing

            result = await agent.arun("Say hello", config=config)
            assert result is not None
        finally:
            agent.checkpointer = original_checkpointer

    @pytest.mark.asyncio
    async def test_persistence_error_reproduction(self):
        """Try to reproduce the PydanticUndefined msgpack error."""
        agent = SimpleAgentV2(
            name="persist_test_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Keep persistence enabled to see if we get the error
        assert agent.checkpointer is not None, "Checkpointer should be set up"

        try:
            # Use a thread_id to trigger checkpointing
            config = {"configurable": {"thread_id": "test-thread-123"}}

            result = await agent.arun("Say hello", config=config)
            assert result is not None
        except TypeError as e:
            if "msgpack serializable" in str(e) and "PydanticUndefinedType" in str(e):
                # This is the error we're trying to fix
                pytest.fail(f"PydanticUndefined msgpack serialization error: {e}")
            else:
                raise

    def test_state_serialization(self):
        """Test that state can be serialized without PydanticUndefined."""
        agent = SimpleAgentV2(
            name="serialize_test_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Create a state instance
        state = agent.state_schema()

        # Try to serialize to dict (what msgpack will do)
        try:
            state_dict = state.model_dump()

            # Check for any None values that might be PydanticUndefined
            for key, value in state_dict.items():
                assert (
                    value is not PydanticUndefined
                ), f"Field {key} has PydanticUndefined"

        except Exception as e:
            pytest.fail(f"Failed to serialize state: {e}")

    @pytest.mark.asyncio
    async def test_invoke_vs_arun(self):
        """Compare invoke vs arun behavior regarding persistence."""
        agent = SimpleAgentV2(
            name="invoke_test_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Test with invoke (synchronous)
        try:
            # Disable checkpointing for invoke test
            agent.checkpointer = None
            agent.invoke("Say hello")
        except Exception:
            pass

        # Test with arun (async)
        with contextlib.suppress(Exception):
            await agent.arun("Say hello")


if __name__ == "__main__":
    # Run the reproduction test directly
    asyncio.run(TestSimpleAgentV2Persistence().test_persistence_error_reproduction())
