#!/usr/bin/env python3
"""Test full graph flow to see where recursion happens."""

import logging

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Enable detailed logging
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s"
)

# Focus on graph execution
for logger_name in [
    "langgraph.graph.graph",
    "langgraph.pregel",
    "haive.core.graph.node",
]:
    logging.getLogger(logger_name).setLevel(logging.DEBUG)

print("\n" + "="*80)
print("TRACING FULL GRAPH FLOW")
print("="*80)

class Task(BaseModel):
    description: str = Field(description="Task description")
    priority: int = Field(default=1)

class Plan[T](BaseModel):
    objective: str = Field(description="Overall objective")
    steps: list[T] = Field(description="List of steps")

def test_graph_execution():
    """Test graph execution to see where recursion happens."""
    print("\n1️⃣ Creating Agent with Plan[Task]")
    print("-" * 40)

    config = AugLLMConfig(
        temperature=0.1,
        structured_output_model=Plan[Task]
    )

    agent = SimpleAgent(
        name="test_planner",
        engine=config,
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a task planner."),
            ("human", "Create a plan for: {objective}")
        ])
    )

    # Inspect graph structure
    print(f"\nGraph nodes: {list(agent.graph.nodes)}")
    print("Graph edges:")
    for edge in agent.graph.edges:
        print(f"  {edge}")

    # Check conditional edges
    print("\nConditional edges:")
    if hasattr(agent.graph, "_all_edges"):
        for node, edges in agent.graph._all_edges.items():
            if edges:
                print(f"  {node}: {edges}")

    # Create a mock state to trace execution
    print("\n\n2️⃣ Simulating Graph Execution")
    print("-" * 40)

    # Simulate what happens after agent generates tool call
    mock_messages = [
        HumanMessage(content="Create a plan for: Test objective"),
        AIMessage(
            content="",
            tool_calls=[{
                "id": "call_123",
                "name": "plan_task_generic",
                "args": {
                    "objective": "Test objective",
                    "steps": [{"description": "Step 1", "priority": 1}]
                }
            }]
        )
    ]

    # After validation node adds ToolMessage
    mock_messages.append(
        ToolMessage(
            content='{"objective":"Test objective","steps":[{"description":"Step 1","priority":1}]}',
            name="plan_task_generic",
            tool_call_id="call_123"
        )
    )

    print("State after validation:")
    print(f"- Messages: {len(mock_messages)}")
    print("- Last message: ToolMessage")

    # The issue might be:
    # 1. Graph goes to agent_node after validation
    # 2. Agent generates the same tool call again
    # 3. Validation happens again
    # 4. Loop continues...

    print("\nPossible recursion causes:")
    print("1. Agent doesn't recognize the ToolMessage as completion")
    print("2. Graph routing sends back to agent instead of ending")
    print("3. Parser node isn't being reached")

def test_parser_node_existence():
    """Check if parser node exists in the graph."""
    print("\n\n3️⃣ Checking Parser Node")
    print("-" * 40)

    config = AugLLMConfig(structured_output_model=Plan[Task])
    agent = SimpleAgent(name="test", engine=config)

    print(f"Graph nodes: {list(agent.graph.nodes)}")

    # Check for parser node
    has_parser = any("parser" in node.lower() for node in agent.graph.nodes)
    print(f"\nHas parser node: {has_parser}")

    # Check if parse_output route is handled
    if hasattr(agent, "validation_router"):
        print("\nValidation router exists")

    # The issue might be that parse_output route needs to go to a parser node
    # but the graph doesn't have one or doesn't route to it correctly

if __name__ == "__main__":
    test_graph_execution()
    test_parser_node_existence()
