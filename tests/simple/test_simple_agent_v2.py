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

    @pytest.mark.asyncio
    async def test_simple_agent_v2_basic_run(self):
        """Test basic execution of SimpleAgentV2."""
        agent = SimpleAgentV2(
            name="execution_test_agent",
            engine=AugLLMConfig(temperature=0.1),  # Low temp for consistency
        )

        # Test simple query
        result = await agent.arun("Hello! Please respond with a greeting.")

        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

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
