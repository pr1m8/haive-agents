"""Test SimpleAgentV2 functionality with the fixed LLMState schema composition."""

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.simple.agent_v2 import SimpleAgentV2


class TestSimpleAgentV2:
    """Test suite for SimpleAgentV2 functionality."""

    def test_simple_agent_v2_creation(self):
        """Test that SimpleAgentV2 can be created successfully."""
        # Create basic agent
        agent = SimpleAgentV2(
            name="test_agent_v2", engine=AugLLMConfig(temperature=0.7)
        )

        assert agent.name == "test_agent_v2"
        assert agent.engine is not None

        # Verify schema is properly set up
        assert agent.state_schema is not None
        assert agent.input_schema is not None
        assert agent.output_schema is not None

    def test_simple_agent_v2_uses_llm_state(self):
        """Test that SimpleAgentV2 uses LLMState as the base schema."""
        agent = SimpleAgentV2(name="llm_test_agent", engine=AugLLMConfig())

        # Check the MRO to ensure LLMState is used
        mro_names = [cls.__name__ for cls in agent.state_schema.__mro__]
        assert "LLMState" in mro_names, f"Expected LLMState in MRO but got: {mro_names}"

        # Verify token_usage field is available
        assert "token_usage" in agent.state_schema.model_fields
        assert "engine" in agent.state_schema.model_fields
        assert "messages" in agent.state_schema.model_fields

    def test_simple_agent_v2_state_creation(self):
        """Test that we can create state instances with proper fields."""
        agent = SimpleAgentV2(name="state_test_agent", engine=AugLLMConfig())

        # Should be able to create state with engine
        state = agent.state_schema(engine=agent.engine)
        assert hasattr(state, "token_usage")
        assert hasattr(state, "engine")
        assert hasattr(state, "messages")
        assert state.engine == agent.engine

    def test_state_instance_creation_debug(self):
        """Debug test to understand state instance creation."""
        from pydantic_core import PydanticUndefined

        # Create agent
        agent = SimpleAgentV2(
            name="debug_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Get the state schema class
        StateClass = agent.state_schema
        print(f"\nState class: {StateClass.__name__}")
        print(f"MRO: {[c.__name__ for c in StateClass.__mro__]}")

        # Check field definitions
        print("\n=== Field Definitions ===")
        for field_name, field_info in StateClass.model_fields.items():
            default = getattr(field_info, "default", PydanticUndefined)
            default_factory = getattr(field_info, "default_factory", None)
            print(f"{field_name}: default={default}, default_factory={default_factory}")

        # Create instance and check actual values
        print("\n=== Creating Instance ===")
        instance = StateClass()

        print("\n=== Instance Field Values ===")
        undefined_fields = []
        for field_name in StateClass.model_fields:
            try:
                value = getattr(instance, field_name)
                if value is PydanticUndefined:
                    undefined_fields.append(field_name)
                    print(f"{field_name}: PydanticUndefined ❌")
                else:
                    print(f"{field_name}: {type(value).__name__} ✓")
            except AttributeError as e:
                print(f"{field_name}: AttributeError - {e}")

        assert (
            len(undefined_fields) == 0
        ), f"Found PydanticUndefined fields: {undefined_fields}"

    @pytest.mark.asyncio
    async def test_simple_agent_v2_basic_run(self):
        """Test basic execution of SimpleAgentV2."""
        # Create agent
        agent = SimpleAgentV2(
            name="execution_test_agent",
            engine=AugLLMConfig(temperature=0.1),  # Low temp for consistency
        )

        # Try to run without persistence first
        print("\n--- Testing without persistence ---")
        original_checkpointer = agent.checkpointer
        agent.checkpointer = None  # Disable checkpointing to avoid msgpack issue

        try:
            result = await agent.arun("Hello! Please respond with a greeting.")
            print(f"SUCCESS without persistence: Got response: {result}")
            print(f"Response type: {type(result)}")
            assert result is not None

            # Handle both string and object responses
            if isinstance(result, str):
                assert len(result) > 0
            else:
                # It's a structured output - check it has content
                print(f"Response attributes: {dir(result)}")
                if hasattr(result, "content"):
                    assert result.content is not None
                elif hasattr(result, "messages"):
                    assert result.messages is not None
        except Exception as e:
            print(f"FAILED without persistence: {e}")
            raise
        finally:
            agent.checkpointer = original_checkpointer

    def test_simple_agent_v2_with_structured_output(self):
        """Test SimpleAgentV2 with structured output model."""
        from pydantic import BaseModel, Field

        class GreetingResponse(BaseModel):
            """Simple greeting response model."""

            greeting: str = Field(description="A greeting message")
            language: str = Field(description="Language used for greeting")

        agent = SimpleAgentV2(
            name="structured_test_agent",
            engine=AugLLMConfig(
                structured_output_model=GreetingResponse, structured_output_version="v2"
            ),
        )

        # Verify agent was created successfully
        assert agent.name == "structured_test_agent"
        assert agent.engine.structured_output_model == GreetingResponse

    def test_simple_agent_v2_schema_fields(self):
        """Test that all expected schema fields are present."""
        agent = SimpleAgentV2(name="fields_test_agent", engine=AugLLMConfig())

        # Check state schema fields
        state_fields = agent.state_schema.model_fields
        expected_fields = ["engine", "engines", "messages", "token_usage"]

        for field in expected_fields:
            assert field in state_fields, f"Missing expected field: {field}"

        # Check input schema fields
        input_fields = agent.input_schema.model_fields
        assert "messages" in input_fields

    def test_simple_agent_v2_engine_registration(self):
        """Test that engine is properly registered."""
        agent = SimpleAgentV2(
            name="registry_test_agent", engine=AugLLMConfig(name="test_engine")
        )

        # Verify engine is registered
        from haive.core.engine.base.registry import EngineRegistry

        registry = EngineRegistry.get_instance()

        # Should be able to find the engine
        found_engine = registry.find("test_engine")
        assert found_engine is not None
        assert found_engine == agent.engine
