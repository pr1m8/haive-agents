"""Debug the EngineNode schema setup to find the structured output issue."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


class TestModel(BaseModel):
    """Test structured output model."""

    answer: str = Field(description="The answer")
    confidence: float = Field(description="Confidence 0-1")


def debug_engine_node_schema():
    """Debug what's happening with EngineNode schema setup."""

    print("🔍 DEBUGGING ENGINE NODE SCHEMA SETUP")
    print("=" * 60)

    # Create SimpleAgent with structured output
    agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1)),
        structured_output_model=TestModel,
        structured_output_version="v2",
        debug=True,
    )

    print(f"✅ Agent created with structured model: {TestModel}")
    print(
        f"   - Engine structured model: {getattr(agent.engine, 'structured_output_model', None)}"
    )

    # Compile to trigger setup
    agent.compile()

    print("\n=== AGENT STATE SCHEMA ===")
    print(f"Agent state schema: {agent.state_schema}")
    print(f"Agent state fields: {list(agent.state_schema.model_fields.keys())}")

    print("\n=== ENGINE NODE ANALYSIS ===")
    # Get the engine node from the graph
    if hasattr(agent, "graph") and agent.graph:
        nodes = agent.graph.nodes
        print(f"Graph nodes: {list(nodes.keys())}")

        if "agent_node" in nodes:
            engine_node_config = nodes["agent_node"]
            print(f"Engine node type: {type(engine_node_config)}")
            print(f"Engine node name: {engine_node_config.name}")
            print(f"Engine node engine: {engine_node_config.engine}")

            print("\n--- EngineNode Field Definitions ---")
            print(f"Input field defs: {engine_node_config.input_field_defs}")
            print(f"Output field defs: {engine_node_config.output_field_defs}")

            print("\n--- EngineNode Schemas ---")
            print(f"Input schema: {engine_node_config.input_schema}")
            print(f"Output schema: {engine_node_config.output_schema}")

            if engine_node_config.input_schema:
                print(
                    f"Input schema fields: {list(engine_node_config.input_schema.model_fields.keys())}"
                )
            if engine_node_config.output_schema:
                print(
                    f"Output schema fields: {list(engine_node_config.output_schema.model_fields.keys())}"
                )

            print("\n--- Engine Analysis ---")
            engine = engine_node_config.engine
            if engine:
                print(
                    f"Engine structured model: {getattr(engine, 'structured_output_model', None)}"
                )
                print(f"Engine output schema: {getattr(engine, 'output_schema', None)}")
                if hasattr(engine, "output_schema") and engine.output_schema:
                    print(
                        f"Engine output schema fields: {list(engine.output_schema.model_fields.keys())}"
                    )

            print("\n--- StandardFields Analysis ---")
            from haive.core.schema.field_registry import StandardFields

            try:
                structured_field = StandardFields.structured_output(TestModel)
                print(f"StandardFields structured output: {structured_field}")
                print(f"Structured field name: {structured_field.name}")
                print(f"Structured field type: {structured_field.field_type}")
            except Exception as e:
                print(f"Error creating structured field: {e}")

    print("\n=== DIAGNOSIS ===")
    # Check if the issue is in field def → schema conversion


if __name__ == "__main__":
    debug_engine_node_schema()
