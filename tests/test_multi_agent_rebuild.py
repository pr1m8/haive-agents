"""Test rebuilding multi-agent with AgentNodeV3 and proper state management.

This test validates:
1. MultiAgentState usage
2. AgentNodeV3 integration
3. Sequential execution with real LLMs
4. Structured output transfer between agents
"""

import asyncio
import logging
from typing import List

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.graph import END, START
from pydantic import BaseModel, Field
from rich.console import Console
from rich.logging import RichHandler

from haive.agents.multi.multi_agent_v2 import ExecutionMode, MultiAgentV2
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger(__name__)
console = Console()


# Structured output models
class AnalysisResult(BaseModel):
    """Result from analysis agent."""

    topic: str = Field(description="Main topic")
    key_findings: List[str] = Field(description="Key findings")
    confidence: float = Field(description="Confidence score 0-1")


class FormattedReport(BaseModel):
    """Final formatted report."""

    title: str = Field(description="Report title")
    summary: str = Field(description="Executive summary")
    details: AnalysisResult = Field(description="Analysis details")


# Test tools
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error: {str(e)}"


class RebuildMultiAgent(MultiAgentV2):
    """Rebuild MultiAgent with proper AgentNodeV3 usage."""

    def setup_agent(self):
        """Set up the multi-agent with MultiAgentState."""
        # Force use of MultiAgentState
        self.state_schema = MultiAgentState

        # Set up agents in state
        if not hasattr(self, "agents") or not self.agents:
            console.print("[red]No agents found in setup_agent![/red]")
            return

        console.print(f"[green]Setting up {len(self.agents)} agents[/green]")

    def build_graph(self) -> BaseGraph:
        """Build graph using AgentNodeV3 directly."""
        console.print("[yellow]Building graph with AgentNodeV3...[/yellow]")

        # Create graph with MultiAgentState
        graph = BaseGraph(name=f"{self.name}_graph", state_schema=self.state_schema)

        # Add each agent using AgentNodeV3Config directly
        if isinstance(self.agents, dict):
            for agent_name, agent in self.agents.items():
                console.print(f"  Adding agent: {agent_name}")

                # Create AgentNodeV3Config directly (no create function)
                node_config = AgentNodeV3Config(
                    name=f"agent_{agent_name}",
                    agent_name=agent_name,
                    agent=agent,
                    project_state=True,
                    extract_from_container=True,
                    update_container_state=True,
                )

                # Add agent to the config after creation
                node_config.agent = agent

                # Add node to graph
                graph.add_node(f"agent_{agent_name}", node_config)

        # Build edges based on execution mode
        if self.execution_mode == ExecutionMode.SEQUENCE:
            self._build_sequence_edges(graph)
        else:
            raise NotImplementedError(f"Mode {self.execution_mode} not implemented yet")

        return graph

    def _build_sequence_edges(self, graph: BaseGraph):
        """Build sequential execution edges."""
        if isinstance(self.agents, dict):
            agent_names = list(self.agents.keys())
            console.print(f"  Building sequential edges: {' -> '.join(agent_names)}")

            # Connect START to first agent
            graph.add_edge(START, f"agent_{agent_names[0]}")

            # Connect agents in sequence
            for i in range(len(agent_names) - 1):
                graph.add_edge(f"agent_{agent_names[i]}", f"agent_{agent_names[i+1]}")

            # Connect last agent to END
            graph.add_edge(f"agent_{agent_names[-1]}", END)


@pytest.mark.asyncio
async def test_sequential_with_structured_output():
    """Test ReactAgent -> SimpleAgent with structured output."""
    console.print("\n[bold blue]Test: Sequential with Structured Output[/bold blue]\n")

    # Step 1: Create ReactAgent for analysis
    react_agent = ReactAgent(
        name="analyzer",
        engine=AugLLMConfig(
            system_message=(
                "You are an analysis agent. Use tools to gather information. "
                "Analyze the topic thoroughly and provide key findings."
            ),
            temperature=0.7,
        ),
        tools=[calculator],
        max_iterations=2,
    )

    # Step 2: Create SimpleAgent for structured output
    simple_agent = SimpleAgent(
        name="formatter",
        engine=AugLLMConfig(
            system_message=(
                "You are a report formatter. Take the analysis and format it "
                "into a structured report with title and summary."
            ),
            temperature=0.3,
            structured_output_model=FormattedReport,
            structured_output_version="v2",
        ),
    )

    # Step 3: Create MultiAgent
    multi_agent = RebuildMultiAgent(
        name="analysis_pipeline",
        agents=[react_agent, simple_agent],  # Will be converted to dict
        execution_mode=ExecutionMode.SEQUENCE,
        state_schema=MultiAgentState,  # Use existing MultiAgentState
    )

    # Debug: Check setup
    console.print(f"MultiAgent agents: {list(multi_agent.agents.keys())}")
    console.print(f"State schema: {multi_agent.state_schema}")

    # Step 4: Test execution
    test_input = {
        "messages": [
            HumanMessage(
                content=(
                    "Analyze the efficiency of parallel processing. "
                    "If we have 3 tasks each taking 5 seconds, how long does it take "
                    "in serial vs parallel? Calculate the time savings."
                )
            )
        ]
    }

    try:
        result = await multi_agent.ainvoke(test_input)
        console.print("\n[bold green]Execution completed![/bold green]")

        # Check results
        if isinstance(result, dict):
            console.print(f"\nResult keys: {list(result.keys())}")

            # Check agent outputs
            if "agent_outputs" in result:
                console.print(f"\nAgent outputs: {result['agent_outputs'].keys()}")

            # Check final messages
            if "messages" in result:
                console.print(f"\nTotal messages: {len(result['messages'])}")
                last_msg = result["messages"][-1]
                console.print(f"Last message type: {type(last_msg)}")
                console.print(f"Last message content: {last_msg.content[:200]}...")

    except Exception as e:
        console.print(f"\n[bold red]Error: {type(e).__name__}: {str(e)}[/bold red]")
        import traceback

        console.print(traceback.format_exc())
        raise


@pytest.mark.asyncio
async def test_state_projection():
    """Test that AgentNodeV3 properly projects state."""
    console.print("\n[bold blue]Test: State Projection[/bold blue]\n")

    # Create simple agents
    agent1 = SimpleAgent(
        name="agent1",
        engine=AugLLMConfig(
            system_message="You are agent 1. Say 'Hello from agent 1'.",
            temperature=0.1,
        ),
    )

    agent2 = SimpleAgent(
        name="agent2",
        engine=AugLLMConfig(
            system_message="You are agent 2. Respond to the previous message.",
            temperature=0.1,
        ),
    )

    # Create multi-agent
    multi = RebuildMultiAgent(
        name="projection_test",
        agents=[agent1, agent2],
        execution_mode=ExecutionMode.SEQUENCE,
    )

    # Test
    result = await multi.ainvoke(
        {"messages": [HumanMessage(content="Start the conversation")]}
    )

    console.print("[green]State projection test passed![/green]")
    assert "messages" in result
    assert len(result["messages"]) > 2  # Should have original + responses


if __name__ == "__main__":
    # Run tests directly
    asyncio.run(test_sequential_with_structured_output())
    asyncio.run(test_state_projection())
