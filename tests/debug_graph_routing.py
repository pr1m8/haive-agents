"""Debug SimpleAgent graph routing for structured output."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


class SimpleResponse(BaseModel):
    """Simple response model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def debug_graph_routing():
    """Debug SimpleAgent graph routing."""

    print("🔍 DEBUGGING GRAPH ROUTING")
    print("=" * 50)

    # Create SimpleAgent with structured output
    agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=SimpleResponse,
        structured_output_version="v2",
        debug=True,
    )

    print("✅ Agent created")
    print(f"   - Structured model: {agent.structured_output_model}")
    print(f"   - Force tool use check: {agent._has_force_tool_use()}")
    print(
        f"   - Engine force_tool_use: {getattr(agent.engine, 'force_tool_use', None)}"
    )
    print(
        f"   - Engine force_tool_choice: {getattr(agent.engine, 'force_tool_choice', None)}"
    )

    # Compile to build graph
    agent.compile()

    print("\n=== GRAPH ANALYSIS ===")
    if hasattr(agent, "graph") and agent.graph:
        print(f"Graph nodes: {list(agent.graph.nodes.keys())}")
        print(f"Graph edges: {list(agent.graph.edges)}")

        # Check the compiled LangGraph structure
        if hasattr(agent, "_app") and agent._app:
            compiled_graph = agent._app
            print(f"Compiled graph type: {type(compiled_graph)}")

            # Try to inspect the graph structure
            if hasattr(compiled_graph, "graph"):
                print(f"LangGraph nodes: {list(compiled_graph.graph.nodes.keys())}")
                print(f"LangGraph edges: {list(compiled_graph.graph.edges)}")
            elif hasattr(compiled_graph, "nodes"):
                print(f"Direct nodes: {list(compiled_graph.nodes.keys())}")

    print("\n=== ENGINE FORCE TOOL ANALYSIS ===")
    engine = agent.engine
    if engine:
        print(f"Engine type: {type(engine)}")
        print(
            f"Engine structured_output_model: {getattr(engine, 'structured_output_model', None)}"
        )
        print(f"Engine force_tool_use: {getattr(engine, 'force_tool_use', None)}")
        print(f"Engine force_tool_choice: {getattr(engine, 'force_tool_choice', None)}")
        print(f"Engine tools: {getattr(engine, 'tools', None)}")
        print(f"Engine tool_choice_mode: {getattr(engine, 'tool_choice_mode', None)}")


if __name__ == "__main__":
    debug_graph_routing()
