"""Debug the EngineNode schema setup to find the structured output issue."""

import contextlib

from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


class TestModel(BaseModel):
    """Test structured output model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def debug_engine_node_schema():
    """Debug what's happening with EngineNode schema setup."""
    # Create SimpleAgent with structured output
    agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestModel,
        structured_output_version="v2",
        debug=True,
    )

    # Compile to trigger setup
    agent.compile()

    # Get the engine node from the graph
    if hasattr(agent, "graph") and agent.graph:
        nodes = agent.graph.nodes

        if "agent_node" in nodes:
            engine_node_config = nodes["agent_node"]

            if engine_node_config.input_schema:
                pass
            if engine_node_config.output_schema:
                pass

            engine = engine_node_config.engine
            if engine and hasattr(engine, "output_schema") and engine.output_schema:
                pass

            from haive.core.schema.field_registry import StandardFields

            with contextlib.suppress(Exception):
                StandardFields.structured_output(TestModel)

    # Check if the issue is in field def → schema conversion


if __name__ == "__main__":
    debug_engine_node_schema()
