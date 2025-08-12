"""Test to verify agent base consolidation was successful."""

from haive.agents.base import Agent, Workflow
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def test_imports_working():
    """Test that all imports are working after consolidation."""
    # These imports should work
    assert Agent is not None
    assert Workflow is not None
    assert SimpleAgent is not None


def test_simple_agent_creation():
    """Test that SimpleAgent can be created."""
    agent = SimpleAgent(
        name="test_agent",
        engine=AugLLMConfig(
            system_message="You are a helpful assistant"
        )
    )

    assert agent.name == "test_agent"
    assert isinstance(agent, SimpleAgent)
    assert isinstance(agent, Agent)  # Should inherit from Agent


def test_class_hierarchy():
    """Test that the class hierarchy is correct."""
    # SimpleAgent should inherit from Agent
    assert issubclass(SimpleAgent, Agent)

    # Check the base classes
    bases = [c.__name__ for c in SimpleAgent.__bases__]
    assert "Agent[AugLLMConfig]" in str(SimpleAgent.__bases__[0])
    assert "RecompileMixin" in bases
    assert "DynamicToolRouteMixin" in bases


def test_workflow_independence():
    """Test that Workflow is in its own module."""
    from haive.agents.base.workflow import Workflow as WorkflowDirect

    assert Workflow is WorkflowDirect
    assert Workflow.__module__ == "haive.agents.base.workflow"


if __name__ == "__main__":
    # Run tests directly
    test_imports_working()
    print("✓ Imports working")

    test_simple_agent_creation()
    print("✓ SimpleAgent creation working")

    test_class_hierarchy()
    print("✓ Class hierarchy correct")

    test_workflow_independence()
    print("✓ Workflow in separate module")

    print("\n✅ All consolidation tests passed!")
