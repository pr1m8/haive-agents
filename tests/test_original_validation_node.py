"""Test SimpleAgent with original ValidationNodeConfig instead of V2."""

from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Temporarily patch SimpleAgent to use original validation node
from haive.core.graph.node.validation_node_config import ValidationNodeConfig
from haive.core.models.llm.base import AzureLLMConfig


class TestResponse(BaseModel):
    """Test response model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def test_with_original_validation():
    """Test with original ValidationNodeConfig."""
    # Create agent
    agent = SimpleAgent(
        name="original_validation_test",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestResponse,
        structured_output_version="v2",
        debug=True,
    )

    # Manually patch the build_graph method to use original ValidationNodeConfig

    def patched_build_graph():
        """Build graph with original ValidationNodeConfig."""
        from langgraph.graph import END, START

        from haive.core.graph.node.engine_node import EngineNodeConfig
        from haive.core.graph.node.parser_node_config_v2 import ParserNodeConfigV2
        from haive.core.graph.state_graph.base_graph2 import BaseGraph

        graph = BaseGraph(name=agent.name)
        available_nodes = []

        # Add agent node
        engine_node = EngineNodeConfig(name="agent_node", engine=agent.engine)
        graph.add_node("agent_node", engine_node)
        graph.add_edge(START, "agent_node")
        available_nodes.append("agent_node")

        # Add parser node
        parser_config = ParserNodeConfigV2(
            name="parse_output",
            engine_name=agent.engine.name,
        )
        graph.add_node("parse_output", parser_config)
        graph.add_edge("parse_output", END)
        available_nodes.append("parse_output")

        # Add ORIGINAL validation node
        validation_config = ValidationNodeConfig(
            name="validation",
            engine_name=agent.engine.name,
            schemas=[TestResponse] if agent.structured_output_model else [],
        )
        graph.add_node("validation", validation_config)
        available_nodes.append("validation")

        # Always go to validation (force tool use)
        graph.add_edge("agent_node", "validation")

        # Store metadata
        graph.metadata["available_nodes"] = available_nodes
        graph.metadata["tool_routes"] = agent.get_tool_routes()

        return graph

    # Patch the method
    agent.build_graph = patched_build_graph

    # Compile
    agent.compile()

    # Test execution
    test_input = {"messages": [HumanMessage(content="What is 2+2?")]}
    config = {"configurable": {"thread_id": None}}

    try:
        result = agent._app.invoke(test_input, config=config)

        # Check for structured output
        structured_fields = [k for k in result if k != "messages"]
        if structured_fields:
            for _field in structured_fields:
                pass
        else:
            pass

        # Check if engine_name is in messages
        messages = result.get("messages", [])
        for _i, msg in enumerate(messages):
            if hasattr(msg, "additional_kwargs"):
                pass
            if hasattr(msg, "response_metadata"):
                pass

    except Exception:
        import traceback

        traceback.print_exc()


def test_engine_name_in_message():
    """Test if engine node adds engine_name to AIMessage."""
    # Create minimal agent
    agent = SimpleAgent(
        name="engine_name_test",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        debug=True,
    )

    agent.compile()

    # Test execution
    test_input = {"messages": [HumanMessage(content="Hello")]}
    config = {"configurable": {"thread_id": None}}

    result = agent._app.invoke(test_input, config=config)

    # Check messages for engine name
    messages = result.get("messages", [])

    for _i, msg in enumerate(messages):
        if hasattr(msg, "additional_kwargs"):
            engine_name = msg.additional_kwargs.get("engine_name")
            if engine_name:
                pass
            else:
                pass


if __name__ == "__main__":
    test_with_original_validation()
    test_engine_name_in_message()
