"""Debug SimpleAgent graph routing for structured output."""

from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


class SimpleResponse(BaseModel):
    """Simple response model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def debug_graph_routing():
    """Debug SimpleAgent graph routing."""
    # Create SimpleAgent with structured output
    agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=SimpleResponse,
        structured_output_version="v2",
        debug=True,
    )

    # Compile to build graph
    agent.compile()

    if hasattr(agent, "graph") and agent.graph:

        # Check the compiled LangGraph structure
        if hasattr(agent, "_app") and agent._app:
            compiled_graph = agent._app

            # Try to inspect the graph structure
            if hasattr(compiled_graph, "graph") or hasattr(compiled_graph, "nodes"):
                pass

    engine = agent.engine
    if engine:
        pass


if __name__ == "__main__":
    debug_graph_routing()
