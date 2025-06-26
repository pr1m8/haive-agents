"""Tests for the MultiAgent implementation."""

import json
from typing import Any, Dict

from langchain_core.messages import AIMessage, HumanMessage

from haive.agents.multi.agent import MultiAgent, MultiAgentState
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


def test_multi_agent_state():
    """Test the MultiAgentState class."""
    # Create state
    state = MultiAgentState()

    # Check initial state
    assert state.agents == {}
    assert state.active_agent_id is None
    assert state.messages == []

    # Create agent
    agent = SimpleAgent(name="Test Agent")

    # Add agent to state
    agent_id = state.add_agent(agent)

    # Check agent was added and set as active
    assert agent_id in state.agents
    assert state.active_agent_id == agent_id
    assert state.get_agent() == agent

    # Test adding message
    state.add_message(HumanMessage(content="Hello"))
    assert len(state.messages) == 1
    assert state.messages[0].content == "Hello"

    # Test serialization
    state_dict = state.to_dict()
    assert "agents" in state_dict
    assert agent_id in state_dict["agents"]
    assert len(state_dict["messages"]) == 1

    # Verify we can convert to JSON and back
    state_json = state.to_json()
    reconstructed = MultiAgentState.from_json(state_json)

    # Verify that reconstructed state has the agent
    assert agent_id in reconstructed.agents
    assert reconstructed.active_agent_id == agent_id
    assert len(reconstructed.messages) == 1


def test_multi_agent_with_agents():
    """Test creating a MultiAgent with agents."""
    # Create some agents
    agent1 = SimpleAgent(name="Simple Agent")
    agent2 = ReactAgent(name="React Agent")

    # Create multi-agent
    multi_agent = MultiAgent.with_agents(
        agents=[agent1, agent2],
        name="Test Multi-Agent",
        coordination_strategy="sequential",
    )

    # Check agents were added
    assert len(multi_agent._state_instance.agents) == 2

    # Verify we have distinct schemas
    assert multi_agent.input_schema is not None
    assert multi_agent.output_schema is not None
    assert multi_agent.state_schema is not None

    # Verify state schema has expected fields
    assert "messages" in multi_agent.state_schema.model_fields
    assert "agents" in multi_agent.state_schema.model_fields
    assert "active_agent_id" in multi_agent.state_schema.model_fields

    # Verify shared fields
    assert "messages" in multi_agent.state_schema.__shared_fields__
    assert "active_agent_id" in multi_agent.state_schema.__shared_fields__
    assert "shared_state" in multi_agent.state_schema.__shared_fields__


def test_schema_composition():
    """Test composing schemas from agents."""
    # Create some agents
    agent1 = SimpleAgent(name="Simple Agent")
    agent2 = ReactAgent(name="React Agent")

    # Compose schema
    schema = MultiAgent.compose_schema_from_agents(
        agents=[agent1, agent2], name="TestComposedSchema"
    )

    # Verify schema has expected fields
    assert "messages" in schema.model_fields
    assert "active_agent_id" in schema.model_fields

    # Verify shared fields
    assert "messages" in schema.__shared_fields__

    # Create instance of schema
    state = schema()

    # Add messages
    state.add_message(HumanMessage(content="Test message"))
    assert len(state.messages) == 1

    # Verify it's a proper StateSchema
    assert hasattr(state, "to_dict")
    assert hasattr(state, "apply_reducers")
    assert hasattr(state, "add_messages")


def test_multi_agent_execution():
    """Test executing the multi-agent system."""

    # Create a simple test agent
    class TestAgent(SimpleAgent):
        def invoke(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
            # Just echo input with an AI message
            messages = input_data.get("messages", [])

            # Find last human message
            human_msg = None
            for msg in reversed(messages):
                if msg.type == "human":
                    human_msg = msg
                    break

            if human_msg:
                response = f"Agent {self.name} responding to: {human_msg.content}"
            else:
                response = f"Agent {self.name} says hello"

            return {"messages": messages + [AIMessage(content=response)]}

    # Create agents
    agent1 = TestAgent(name="Agent 1")
    agent2 = TestAgent(name="Agent 2")

    # Create multi-agent
    multi_agent = MultiAgent.with_agents(
        agents=[agent1, agent2],
        name="Test Multi-Agent",
        coordination_strategy="sequential",
    )

    # Run multi-agent
    input_data = {"messages": [HumanMessage(content="Hello, agents!")]}

    output = multi_agent.invoke(input_data)

    # Verify output
    assert "messages" in output
    assert len(output["messages"]) >= 3  # Original + at least 2 agent responses

    # Check that outputs were collected
    assert len(multi_agent._state_instance.outputs) == 2


def test_multi_agent_serialization():
    """Test serializing and deserializing the multi-agent system."""
    # Create agents
    agent1 = SimpleAgent(name="Agent 1")
    agent2 = ReactAgent(name="Agent 2")

    # Create multi-agent
    multi_agent = MultiAgent.with_agents(
        agents=[agent1, agent2], name="Test Multi-Agent"
    )

    # Add a message
    multi_agent._state_instance.add_message(HumanMessage(content="Test message"))

    # Serialize state
    state_dict = multi_agent._state_instance.to_dict()
    state_json = json.dumps(state_dict)

    # Create new state from serialized data
    new_state = MultiAgentState.from_json(state_json)

    # Verify state was properly reconstructed
    assert len(new_state.agents) == 2
    assert len(new_state.messages) == 1
    assert new_state.messages[0].content == "Test message"

    # Get agent and verify it can be used
    agent = new_state.get_agent()
    assert agent is not None
    assert agent.name in ["Agent 1", "Agent 2"]

    # Test rebuilding graph
    if hasattr(agent, "_graph_built"):
        assert not agent._graph_built  # Graph should need rebuilding

    # Getting the agent should rebuild the graph
    agent = new_state.get_agent()
    if hasattr(agent, "_graph_built"):
        assert agent._graph_built  # Graph should be rebuilt
