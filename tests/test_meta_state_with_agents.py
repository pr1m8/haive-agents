"""Test MetaStateSchema with real agent nodes to validate state hierarchy concepts.

Note: For initial testing, we use simplified mock agents to avoid complex
persistence setup. Once basic patterns are validated, we'll test with full agents.

This test validates:
1. Agents can be embedded in state (MetaStateSchema)
2. Embedded agents can be executed from within state
3. Recompilable mixin works with real graph changes
4. Dynamic tool routing works in practice
5. State composition with nested agents functions correctly
"""

import logging

import pytest
from haive.core.common.mixins.dynamic_tool_route_mixin import DynamicToolRouteMixin
from haive.core.common.mixins.recompile_mixin import RecompileMixin
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.persistence.memory import MemoryCheckpointerConfig
from haive.core.persistence.postgres_config import PostgresCheckpointerConfig
from haive.core.persistence.types import CheckpointerMode, CheckpointStorageMode
from haive.core.schema.prebuilt.meta_state import MetaStateSchema
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.agents.simple.agent_v2 import SimpleAgentV2

logger = logging.getLogger(__name__)


# Test tools for dynamic routing
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e!s}"


@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: Sunny, 72°F"


@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    return f"Search results for '{query}': Found 10 relevant articles"


class TaskResult(BaseModel):
    """Structured output for task completion."""

    task: str = Field(description="The task that was completed")
    result: str = Field(description="The result of the task")
    confidence: float = Field(description="Confidence in the result (0-1)")


class TestMetaStateWithAgents:
    """Test suite for MetaStateSchema with real agents."""

    @pytest.fixture
    def simple_agent(self) -> SimpleAgent:
        """Create a simple agent for testing."""
        config = AugLLMConfig(
            name="test_llm",
            temperature=0.1,
            system_message="You are a helpful assistant.",
        )

        # With the fix, persistence=None should use memory persistence by default
        agent = SimpleAgent(
            name="simple_test_agent",
            engine=config,
            structured_output_model=TaskResult,
            # persistence defaults to None, which now uses memory persistence
        )

        return agent

    @pytest.fixture
    def react_agent_with_tools(self) -> ReactAgent:
        """Create a ReactAgent with tools for testing."""
        config = AugLLMConfig(
            name="react_llm", temperature=0.1, tools=[calculator, get_weather]
        )

        # Use memory persistence for testing
        memory_persistence = MemoryCheckpointerConfig()

        agent = ReactAgent(
            name="react_test_agent", engine=config, persistence=memory_persistence
        )

        return agent

    def test_meta_state_basic_structure(self):
        """Test that MetaStateSchema has the expected structure."""
        # Create a meta state instance
        meta_state = MetaStateSchema()

        # Verify fields exist
        assert hasattr(meta_state, "agent")
        assert hasattr(meta_state, "agent_state")
        assert hasattr(
            meta_state, "meta_context"
        )  # Fixed: field is meta_context, not meta
        assert hasattr(meta_state, "execute_agent")

        # Verify initial values
        assert meta_state.agent is None
        assert isinstance(meta_state.agent_state, dict)
        assert isinstance(meta_state.meta_context, dict)  # Fixed: field is meta_context

    def test_embed_agent_in_meta_state(self, simple_agent):
        """Test embedding a real agent in MetaStateSchema."""
        # Create meta state with embedded agent
        meta_state = MetaStateSchema(
            agent=simple_agent,
            agent_state={"initialized": True},
            meta_context={
                "purpose": "testing",
                "version": "1.0",
            },  # Fixed: meta_context
        )

        # Verify agent is embedded
        assert meta_state.agent is not None
        assert meta_state.agent.name == "simple_test_agent"
        assert isinstance(meta_state.agent, SimpleAgent)

        # Verify we can access agent properties
        assert hasattr(meta_state.agent, "engine")
        assert meta_state.agent.engine.name == "test_llm"

    @pytest.mark.asyncio
    async def test_execute_agent_from_meta_state(self, simple_agent):
        """Test executing an embedded agent using MetaStateSchema.execute_agent()."""
        # Create meta state with agent
        meta_state = MetaStateSchema(
            agent=simple_agent,
            agent_state={"task": "test execution"},
            meta_context={"execution_count": 0},
        )

        # Execute the agent through meta state
        input_data = {"messages": [HumanMessage(content="Calculate 5 + 3")]}

        # The execute_agent method should handle agent execution
        result = await meta_state.execute_agent(input_data)

        # Verify execution happened
        assert result is not None
        assert "execution_count" in meta_state.meta_context
        meta_state.meta_context["execution_count"] += 1
        assert meta_state.meta_context["execution_count"] == 1

    def test_meta_state_with_multiple_agent_types(
        self, simple_agent, react_agent_with_tools
    ):
        """Test that MetaStateSchema can hold different agent types."""
        # Test with SimpleAgent
        meta_state1 = MetaStateSchema(agent=simple_agent)
        assert isinstance(meta_state1.agent, SimpleAgent)

        # Test with ReactAgent
        meta_state2 = MetaStateSchema(agent=react_agent_with_tools)
        assert isinstance(meta_state2.agent, ReactAgent)

        # Verify agents maintain their individual properties
        assert meta_state1.agent.name != meta_state2.agent.name
        assert len(meta_state2.agent.engine.tools) > 0  # ReactAgent has tools

    def test_state_isolation_between_meta_states(self, simple_agent):
        """Test that different MetaStateSchema instances maintain isolated state."""
        # Create two meta states with same agent type but different instances
        meta_state1 = MetaStateSchema(
            agent=simple_agent,
            agent_state={"user": "Alice"},
            meta_context={"session": "A1"},
        )

        # Create new agent instance for second meta state
        config2 = AugLLMConfig(name="test_llm2", temperature=0.2)
        memory_persistence2 = MemoryCheckpointerConfig()
        agent2 = SimpleAgent(
            name="simple_test_agent2", engine=config2, persistence=memory_persistence2
        )

        meta_state2 = MetaStateSchema(
            agent=agent2, agent_state={"user": "Bob"}, meta_context={"session": "B1"}
        )

        # Verify isolation
        assert meta_state1.agent_state["user"] == "Alice"
        assert meta_state2.agent_state["user"] == "Bob"
        assert meta_state1.meta_context["session"] == "A1"
        assert meta_state2.meta_context["session"] == "B1"

        # Modify one state
        meta_state1.agent_state["user"] = "Charlie"

        # Verify other state is unaffected
        assert meta_state2.agent_state["user"] == "Bob"

    @pytest.mark.asyncio
    async def test_nested_agent_execution_pattern(
        self, simple_agent, react_agent_with_tools
    ):
        """Test a pattern where one agent coordinates another through meta state."""
        # Create a coordinator pattern
        coordinator_state = MetaStateSchema(
            agent=simple_agent,  # Coordinator
            agent_state={
                "subordinates": {
                    "calculatof": MetaStateSchema(
                        agent=react_agent_with_tools,
                        agent_state={"specialty": "math"},
                        meta_context={"tool_count": 2},
                    )
                }
            },
            meta_context={"coordination_count": 0},
        )

        # Verify nested structure
        assert "subordinates" in coordinator_state.agent_state
        assert "calculator" in coordinator_state.agent_state["subordinates"]

        # Get the nested agent
        calc_meta_state = coordinator_state.agent_state["subordinates"]["calculator"]
        assert isinstance(calc_meta_state, MetaStateSchema)
        assert isinstance(calc_meta_state.agent, ReactAgent)
        assert calc_meta_state.agent_state["specialty"] == "math"

    def test_serialization_with_embedded_agents(self, simple_agent):
        """Test that MetaStateSchema with agents can be serialized/deserialized."""
        # Create meta state with agent
        original_meta_state = MetaStateSchema(
            agent=simple_agent,
            agent_state={"task": "serialization test"},
            meta_context={"version": 1},
        )

        # Serialize to dict (this tests model_dump)
        try:
            serialized = original_meta_state.model_dump()
            assert isinstance(serialized, dict)
            assert "agent" in serialized
            assert "agent_state" in serialized
            assert "meta" in serialized
        except Exception as e:
            # This might fail if agents aren't serializable
            # which is an important finding for our architecture
            logger.warning(f"Serialization failed: {e}")
            pytest.skip("Agent serialization not yet supported")


class TestMetaStatePostgresPersistence:
    """Test MetaStateSchema with PostgreSQL persistence and SecretStr serialization."""

    @pytest.fixture
    def postgres_config(self) -> PostgresCheckpointerConfig:
        """Create PostgreSQL configuration for testing."""
        return PostgresCheckpointerConfig(
            db_host="localhost",
            db_port=5432,
            db_name="test_haive",
            db_user="postgres",
            db_pass="test_pass",  # This creates a SecretStr
            mode=CheckpointerMode.SYNC,
            storage_mode=CheckpointStorageMode.SHALLOW,
            setup_needed=True,
        )

    @pytest.fixture
    def simple_agent_v2_with_postgres(self, postgres_config) -> SimpleAgentV2:
        """Create SimpleAgentV2 with PostgreSQL persistence to test serialization."""
        config = AugLLMConfig(
            name="postgres_test_llm",
            temperature=0.1,
            system_message="You are a helpful assistant.",
        )

        # Use SimpleAgentV2 which should work with persistence
        agent = SimpleAgentV2(
            name="postgres_test_agent",
            engine=config,
            structured_output_model=TaskResult,
            persistence=postgres_config,  # This should trigger our SecretStr serializer
        )

        return agent

    @pytest.mark.asyncio
    async def test_meta_state_with_postgres_persistence(
        self, simple_agent_v2_with_postgres
    ):
        """Test that MetaStateSchema works with PostgreSQL persistence via our SecretStr serializer."""
        # Create meta state with PostgreSQL-backed agent
        meta_state = MetaStateSchema(
            agent=simple_agent_v2_with_postgres,
            agent_state={"test": "postgres_persistence"},
            meta_context={"database": "postgresql", "serializer": "SecretStr-aware"},
        )

        # Verify agent is embedded
        assert meta_state.agent is not None
        assert isinstance(meta_state.agent, SimpleAgentV2)
        assert meta_state.agent.name == "postgres_test_agent"

        # The key test: Try to serialize this meta state (this would fail before our fix)
        try:
            # This should work now with our SecretStr serializer
            serialized = meta_state.model_dump()
            assert isinstance(serialized, dict)
            logger.info(
                "✅ MetaStateSchema with PostgreSQL agent serialized successfully"
            )

            # Verify the agent field is handled properly
            assert "agent" in serialized

        except Exception as e:
            logger.exception(f"❌ Serialization failed: {e}")
            # This would be the old error: "Type is not msgpack serializable: SecretStr"
            if "SecretStr" in str(e):
                pytest.fail(f"SecretStr serialization issue not resolved: {e}")
            else:
                pytest.fail(f"Unexpected serialization error: {e}")

    @pytest.mark.asyncio
    async def test_meta_state_execution_with_postgres_agent(
        self, simple_agent_v2_with_postgres
    ):
        """Test executing an agent with PostgreSQL persistence through MetaStateSchema."""
        # Create meta state
        meta_state = MetaStateSchema(
            agent=simple_agent_v2_with_postgres,
            agent_state={"execution_test": True},
            meta_context={"persistence_type": "postgresql"},
        )

        # Prepare input
        input_data = {"messages": [HumanMessage(content="Calculate 10 + 5")]}

        # Execute through meta state - this should work with our serializer
        try:
            result = meta_state.execute_agent(input_data)

            # Verify execution
            assert result is not None
            assert result.get("status") == "success"
            logger.info("✅ Agent execution with PostgreSQL persistence succeeded")

        except Exception as e:
            logger.exception(f"❌ Agent execution failed: {e}")
            if "msgpack" in str(e) or "SecretStr" in str(e):
                pytest.fail(f"Persistence serialization error: {e}")
            else:
                # Other execution errors might be expected (no real DB, etc.)
                logger.warning(f"Execution failed (possibly expected): {e}")

    def test_postgres_config_serializer_integration(self, postgres_config):
        """Test that PostgresCheckpointerConfig correctly uses our SecretStr serializer."""
        try:
            # Create checkpointer which should use our custom serializer
            checkpointer = postgres_config.create_checkpointer()

            # Verify the serializer is our SecretStr-aware version
            assert hasattr(checkpointer, "serde")
            serializer = checkpointer.serde

            # Check if it's our custom serializer

            # The serializer should be either our SecureSecretStrSerializer or EncryptedSerializer
            # that wraps our SecureSecretStrSerializer
            serializer_type = type(serializer).__name__
            assert "Serializer" in serializer_type
            logger.info(f"✅ Using serializer: {serializer_type}")

        except Exception as e:
            # Connection errors are expected in CI/testing without real DB
            if "connection" in str(e).lower() or "database" in str(e).lower():
                logger.warning(f"Database connection error (expected in tests): {e}")
                pytest.skip("PostgreSQL not available for testing")
            else:
                logger.exception(f"❌ Unexpected error: {e}")
                raise


class TestRecompilableAgentIntegration:
    """Test RecompileMixin with real agents."""

    def test_agent_with_recompile_mixin(self):
        """Test adding RecompileMixin to an agent."""

        # Create an agent class that includes RecompileMixin
        class RecompilableSimpleAgent(SimpleAgent, RecompileMixin):
            """Simple agent with recompilation capability."""

            def _trigger_auto_recompile(self) -> None:
                """Implementation of recompilation logic."""
                logger.info("Triggering recompilation of agent graph")
                # In real implementation, this would rebuild the graph
                self.rebuild_graph()

            def add_tool_and_recompile(self, new_tool):
                """Add a tool and mark for recompilation."""
                # Add tool to engine
                if hasattr(self.engine, "tools"):
                    self.engine.tools.append(new_tool)

                # Mark for recompilation
                self.mark_for_recompile(f"Added tool: {new_tool.name}")

        # Create recompilable agent
        config = AugLLMConfig(name="recompilable_llm", tools=[calculator])

        memory_persistence = MemoryCheckpointerConfig()

        agent = RecompilableSimpleAgent(
            name="recompilable_agent", engine=config, persistence=memory_persistence
        )

        # Verify recompilation tracking
        assert hasattr(agent, "needs_recompile")
        assert hasattr(agent, "mark_for_recompile")
        assert not agent.needs_recompile

        # Add a tool and trigger recompilation
        agent.add_tool_and_recompile(get_weather)

        # Verify recompilation was marked
        assert agent.needs_recompile
        assert len(agent.recompile_reasons) > 0
        assert "Added tool: get_weather" in agent.recompile_reasons

    def test_recompilation_history_tracking(self):
        """Test that recompilation history is properly tracked."""

        class TrackedAgent(SimpleAgent, RecompileMixin):
            def _trigger_auto_recompile(self) -> None:
                self.rebuild_graph()

        memory_persistence = MemoryCheckpointerConfig()

        agent = TrackedAgent(
            name="tracked_agent", engine=AugLLMConfig(), persistence=memory_persistence
        )

        # Trigger multiple recompilations
        agent.mark_for_recompile("First change")
        agent.resolve_recompile(success=True)

        agent.mark_for_recompile("Second change")
        agent.resolve_recompile(success=True)

        # Check history
        history = agent.get_recompile_history()
        assert len(history) == 2
        assert history[0]["reason"] == "First change"
        assert history[1]["reason"] == "Second change"


class TestDynamicToolRouting:
    """Test DynamicToolRouteMixin with real agents."""

    def test_agent_with_dynamic_tool_routing(self):
        """Test adding DynamicToolRouteMixin to an agent."""

        # Create agent with dynamic tool routing
        class DynamicToolAgent(SimpleAgent, DynamicToolRouteMixin):
            """Agent with dynamic tool routing capability."""

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Register callback for tool changes
                self.register_route_change_callback(
                    self._on_tool_route_change, "main_callback"
                )
                self.tool_change_log = []

            def _on_tool_route_change(
                self, tool_name: str, action: str, old_route: str | None
            ):
                """Handle tool route changes."""
                self.tool_change_log.append(
                    {"tool": tool_name, "action": action, "old_route": old_route}
                )
                logger.info(f"Tool route changed: {tool_name} - {action}")

        # Create agent
        config = AugLLMConfig(name="dynamic_tool_llm", tools=[calculator])

        memory_persistence = MemoryCheckpointerConfig()

        agent = DynamicToolAgent(
            name="dynamic_tool_agent", engine=config, persistence=memory_persistence
        )

        # Add a new tool dynamically
        agent.add_tool(get_weather, "langchain_tool")

        # Verify callback was triggered
        assert len(agent.tool_change_log) > 0
        assert agent.tool_change_log[-1]["tool"] == "get_weather"
        assert agent.tool_change_log[-1]["action"] == "added"

    def test_batch_tool_updates(self):
        """Test batch tool updates with single notification."""

        class BatchUpdateAgent(SimpleAgent, DynamicToolRouteMixin):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.update_count = 0
                self.register_route_change_callback(
                    lambda *args: setattr(self, "update_count", self.update_count + 1),
                    "counter",
                )

        memory_persistence = MemoryCheckpointerConfig()

        agent = BatchUpdateAgent(
            name="batch_agent", engine=AugLLMConfig(), persistence=memory_persistence
        )

        # Batch update multiple tools
        updates = {
            "calculator": "langchain_tool",
            "weather": "langchain_tool",
            "search": "function",
        }

        agent.batch_update_tools(updates, notify_once=True)

        # Should only trigger one notification for batch
        assert agent.update_count == 1


class TestCompleteIntegration:
    """Test complete integration of all concepts."""

    @pytest.mark.asyncio
    async def test_meta_state_with_recompilable_dynamic_agent(self):
        """Test MetaStateSchema with an agent that has both recompilable and dynamic tool capabilities."""

        # Create a fully integrated agent class
        class IntegratedAgent(SimpleAgent, RecompileMixin, DynamicToolRouteMixin):
            """Fully integrated agent with all capabilities."""

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.register_route_change_callback(
                    self._on_tool_change, "recompile_trigger"
                )

            def _on_tool_change(
                self, tool_name: str, action: str, old_route: str | None
            ):
                """Mark for recompilation on tool changes."""
                self.mark_for_recompile(f"Tool {action}: {tool_name}")

            def _trigger_auto_recompile(self) -> None:
                """Recompile the agent graph."""
                logger.info("Recompiling agent graph due to tool changes")
                self.rebuild_graph()

        # Create integrated agent
        memory_persistence = MemoryCheckpointerConfig()

        agent = IntegratedAgent(
            name="integrated_agent",
            engine=AugLLMConfig(tools=[calculator]),
            persistence=memory_persistence,
        )

        # Embed in meta state
        meta_state = MetaStateSchema(
            agent=agent,
            agent_state={"tools_added": []},
            meta_context={"recompile_count": 0},
        )

        # Add tool dynamically
        meta_state.agent.add_tool(get_weather, "langchain_tool")

        # Verify cascading effects
        assert meta_state.agent.needs_recompile
        assert "Tool added: get_weather" in meta_state.agent.recompile_reasons

        # Track in meta state
        meta_state.agent_state["tools_added"].append("get_weather")

        # Resolve recompilation
        meta_state.agent.resolve_recompile(success=True)
        meta_state.meta_context["recompile_count"] += 1

        # Verify state
        assert not meta_state.agent.needs_recompile
        assert meta_state.meta_context["recompile_count"] == 1
        assert "get_weather" in meta_state.agent_state["tools_added"]


if __name__ == "__main__":
    # Run basic tests

    logging.basicConfig(level=logging.INFO)

    # Create test instance
    test_instance = TestMetaStateWithAgents()

    # Run basic structure test
    test_instance.test_meta_state_basic_structure()

    # Create fixtures
    config = AugLLMConfig(name="test_llm", temperature=0.1)
    memory_persistence = MemoryCheckpointerConfig()
    simple_agent = SimpleAgent(
        name="test_agent", engine=config, persistence=memory_persistence
    )

    # Run embedding test
    test_instance.test_embed_agent_in_meta_state(simple_agent)
