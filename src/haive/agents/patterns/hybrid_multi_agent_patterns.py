"""Hybrid Multi-Agent Patterns - Advanced compositions using base patterns.

This module demonstrates advanced multi-agent patterns that combine different
agent types and execution modes, using the base agent.py and SimpleAgentV3
patterns as building blocks.

Patterns include:
1. Parallel-then-Sequential workflows
2. Conditional routing with multiple branches
3. Hierarchical agent structures
4. Dynamic agent composition
"""

from collections.abc import Callable
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langchain_core.tools import tool
from langgraph.graph import END, START
from pydantic import BaseModel, Field

from haive.agents.base.agent import Agent
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured models for different patterns
class TaskClassification(BaseModel):
    """Task classification result."""

    task_type: str = Field(
        description="Type of task: simple, complex, research, creative"
    )
    complexity_score: float = Field(ge=0.0, le=1.0, description="Task complexity")
    required_capabilities: list[str] = Field(description="Required agent capabilities")
    recommended_approach: str = Field(description="Recommended processing approach")


class ParallelResults(BaseModel):
    """Results from parallel agent execution."""

    agent_outputs: dict[str, Any] = Field(description="Outputs from each agent")
    consensus_points: list[str] = Field(description="Points of agreement")
    divergent_points: list[str] = Field(description="Points of disagreement")
    confidence_scores: dict[str, float] = Field(
        description="Confidence from each agent"
    )


class HybridMultiAgent(Agent):
    """Hybrid multi-agent with mixed execution patterns.

    This agent can combine parallel and sequential execution,
    conditional routing, and dynamic agent selection.

    Example:
        >>> agent = HybridMultiAgent(
        ...     name="hybrid_processor",
        ...     initial_agents=[classifier],
        ...     processing_agents=[simple_proc, complex_proc, research_proc],
        ...     synthesis_agents=[combiner, formatter],
        ...     execution_pattern="classify_then_process"
        ... )
    """

    # Agent groups
    initial_agents: list[Agent] = Field(
        default_factory=list, description="Initial processing agents"
    )
    processing_agents: list[Agent] = Field(
        default_factory=list, description="Main processing agents"
    )
    synthesis_agents: list[Agent] = Field(
        default_factory=list, description="Synthesis/output agents"
    )

    # Execution configuration
    execution_pattern: str = Field(
        default="parallel_then_sequential",
        description="Execution pattern: parallel_then_sequential, classify_then_process, hierarchical")

    routing_function: Callable | None = Field(
        None, description="Custom routing function"
    )

    def setup_agent(self) -> None:
        """Setup hybrid agent structure."""
        # Create default agents if not provided
        if not self.initial_agents:
            self.initial_agents = [self._create_classifier_agent()]

        if not self.processing_agents:
            self.processing_agents = [
                self._create_simple_processor(),
                self._create_complex_processor(),
                self._create_research_processor(),
            ]

        if not self.synthesis_agents:
            self.synthesis_agents = [
                self._create_synthesis_agent(),
                self._create_formatter_agent(),
            ]

        # Register all agents
        self.engines = {}
        for agent in (
            self.initial_agents + self.processing_agents + self.synthesis_agents
        ):
            self.engines[agent.name] = agent

    def _create_classifier_agent(self) -> SimpleAgentV3:
        """Create task classifier agent."""
        return SimpleAgentV3(
            name="classifier",
            engine=AugLLMConfig(
                temperature=0.3,
                system_message="Classify tasks and determine the best processing approach.",
                structured_output_model=TaskClassification),
            debug=True)

    def _create_simple_processor(self) -> SimpleAgentV3:
        """Create simple task processor."""
        return SimpleAgentV3(
            name="simple_processor",
            engine=AugLLMConfig(
                temperature=0.5, system_message="Process simple tasks efficiently."
            ),
            debug=True)

    def _create_complex_processor(self) -> ReactAgent:
        """Create complex task processor with tools."""

        @tool
        def analyze_complexity(task: str) -> str:
            """Analyze task complexity."""
            return f"Task '{task}' requires multi-step reasoning"

        return ReactAgent(
            name="complex_processor",
            engine=AugLLMConfig(
                temperature=0.6,
                system_message="Handle complex tasks with reasoning and tools.",
                tools=[analyze_complexity]))

    def _create_research_processor(self) -> ReactAgent:
        """Create research processor with tools."""

        @tool
        def search_knowledge(query: str) -> str:
            """Search knowledge base."""
            return f"Found information about: {query}"

        @tool
        def verify_facts(claim: str) -> str:
            """Verify factual claims."""
            return f"Verification result for '{claim}': Confirmed"

        return ReactAgent(
            name="research_processor",
            engine=AugLLMConfig(
                temperature=0.4,
                system_message="Conduct research and verify information.",
                tools=[search_knowledge, verify_facts]))

    def _create_synthesis_agent(self) -> SimpleAgentV3:
        """Create synthesis agent."""
        return SimpleAgentV3(
            name="synthesizer",
            engine=AugLLMConfig(
                temperature=0.4,
                system_message="Synthesize results from multiple sources.",
                structured_output_model=ParallelResults),
            debug=True)

    def _create_formatter_agent(self) -> SimpleAgentV3:
        """Create final formatter agent."""
        return SimpleAgentV3(
            name="formatter",
            engine=AugLLMConfig(
                temperature=0.3, system_message="Format final output professionally."
            ),
            debug=True)

    def build_graph(self) -> BaseGraph:
        """Build hybrid execution graph."""
        graph = BaseGraph(name=f"{self.name}_graph")

        if self.execution_pattern == "parallel_then_sequential":
            self._build_parallel_then_sequential(graph)
        elif self.execution_pattern == "classify_then_process":
            self._build_classify_then_process(graph)
        elif self.execution_pattern == "hierarchical":
            self._build_hierarchical(graph)
        else:
            raise ValueError(f"Unknown execution pattern: {self.execution_pattern}")

        return graph

    def _build_parallel_then_sequential(self, graph: BaseGraph):
        """Build parallel execution followed by sequential synthesis."""
        # Add all processing agents in parallel
        for agent in self.processing_agents:
            node = create_agent_node_v3(agent.name, agent)
            graph.add_node(agent.name, node)
            graph.add_edge(START, agent.name)

        # Add synthesis agents sequentially
        prev_node = None
        for i, agent in enumerate(self.synthesis_agents):
            node = create_agent_node_v3(agent.name, agent)
            graph.add_node(agent.name, node)

            # Connect from all processing agents to first synthesis
            if i == 0:
                for proc_agent in self.processing_agents:
                    graph.add_edge(proc_agent.name, agent.name)
            else:
                graph.add_edge(prev_node, agent.name)

            prev_node = agent.name

        # Last synthesis to END
        if prev_node:
            graph.add_edge(prev_node, END)

    def _build_classify_then_process(self, graph: BaseGraph):
        """Build classification followed by conditional processing."""
        # Add classifier
        classifier = self.initial_agents[0]
        graph.add_node(
            classifier.name, create_agent_node_v3(classifier.name, classifier)
        )
        graph.add_edge(START, classifier.name)

        # Add all processing agents
        for agent in self.processing_agents:
            graph.add_node(agent.name, create_agent_node_v3(agent.name, agent))

        # Add routing condition
        def route_by_classification(state: dict[str, Any]) -> str:
            """Route based on task classification."""
            # Get classification from state
            classification = state.get("task_type", "simple")

            if classification == "simple":
                return "simple_processor"
            if classification == "complex":
                return "complex_processor"
            if classification == "research":
                return "research_processor"
            return "simple_processor"  # default

        # Add conditional routing
        routes = {
            "simple_processor": "simple_processor",
            "complex_processor": "complex_processor",
            "research_processor": "research_processor",
        }

        graph.add_conditional_edges(classifier.name, route_by_classification, routes)

        # Connect processors to synthesis
        if self.synthesis_agents:
            first_synthesis = self.synthesis_agents[0].name
            graph.add_node(
                first_synthesis,
                create_agent_node_v3(first_synthesis, self.synthesis_agents[0]))

            for proc in self.processing_agents:
                graph.add_edge(proc.name, first_synthesis)

            graph.add_edge(first_synthesis, END)
        else:
            for proc in self.processing_agents:
                graph.add_edge(proc.name, END)

    def _build_hierarchical(self, graph: BaseGraph):
        """Build hierarchical agent structure."""
        # Not implemented - placeholder for hierarchical patterns
        raise NotImplementedError("Hierarchical pattern not yet implemented")


class AdaptiveMultiAgent(EnhancedMultiAgentV4):
    """Adaptive multi-agent that changes behavior based on context.

    This agent dynamically adjusts its execution pattern based on
    input characteristics and intermediate results.
    """

    adaptation_rules: dict[str, Callable] = Field(
        default_factory=dict, description="Rules for adapting execution"
    )

    def __init__(self, **kwargs):
        # Create adaptive agents
        agents = [
            SimpleAgentV3(
                name="analyzer",
                engine=AugLLMConfig(
                    temperature=0.3,
                    system_message="Analyze input and determine processing needs."),
                debug=True),
            SimpleAgentV3(
                name="quick_processor",
                engine=AugLLMConfig(
                    temperature=0.5, system_message="Process simple requests quickly."
                ),
                debug=True),
            ReactAgent(
                name="deep_processor",
                engine=AugLLMConfig(
                    temperature=0.6,
                    system_message="Process complex requests with reasoning.")),
            SimpleAgentV3(
                name="validator",
                engine=AugLLMConfig(
                    temperature=0.3, system_message="Validate and ensure quality."
                ),
                debug=True),
        ]

        kwargs["agents"] = agents
        kwargs["execution_mode"] = "conditional"

        super().__init__(**kwargs)

        # Add adaptation rules
        self._setup_adaptation_rules()

    def _setup_adaptation_rules(self):
        """Setup default adaptation rules."""
        self.add_conditional_edge(
            from_agent="analyzer",
            condition=lambda state: state.get("complexity", 0) < 0.3,
            true_agent="quick_processor",
            false_agent="deep_processor")

        # Both processors go to validator
        self.add_edge("quick_processor", "validator")
        self.add_edge("deep_processor", "validator")


class CollaborativeMultiAgent(EnhancedMultiAgentV4):
    """Collaborative multi-agent where agents work together.

    Agents share information and build on each other's work.
    """

    collaboration_mode: str = Field(
        default="peer_review",
        description="How agents collaborate: peer_review, consensus, debate")

    def __init__(self, **kwargs):
        # Create collaborative agents
        agents = []

        # Expert agents with different perspectives
        for _i, perspective in enumerate(["technical", "business", "user"]):
            agent = SimpleAgentV3(
                name=f"{perspective}_expert",
                engine=AugLLMConfig(
                    temperature=0.6,
                    system_message=f"You are a {perspective} expert. Provide insights from the {perspective} perspective."),
                debug=True)
            agents.append(agent)

        # Consensus builder
        consensus = SimpleAgentV3(
            name="consensus_builder",
            engine=AugLLMConfig(
                temperature=0.4,
                system_message="Build consensus from multiple expert perspectives.",
                structured_output_model=ParallelResults),
            debug=True)
        agents.append(consensus)

        kwargs["agents"] = agents
        kwargs["execution_mode"] = "manual"

        super().__init__(**kwargs)

        # Setup collaboration pattern
        self._setup_collaboration()

    def _setup_collaboration(self):
        """Setup collaboration edges."""
        if self.collaboration_mode == "peer_review":
            # Each expert reviews others
            self.add_edge("technical_expert", "business_expert")
            self.add_edge("business_expert", "user_expert")
            self.add_edge("user_expert", "consensus_builder")
        elif self.collaboration_mode == "consensus":
            # All experts to consensus
            for expert in ["technical_expert", "business_expert", "user_expert"]:
                self.add_edge(expert, "consensus_builder")


# Factory functions
def create_hybrid_agent(
    name: str = "hybrid",
    execution_pattern: str = "classify_then_process",
    debug: bool = True) -> HybridMultiAgent:
    """Create a hybrid multi-agent."""
    return HybridMultiAgent(name=name, execution_pattern=execution_pattern, debug=debug)


def create_adaptive_agent(
    name: str = "adaptive", debug: bool = True
) -> AdaptiveMultiAgent:
    """Create an adaptive multi-agent."""
    return AdaptiveMultiAgent(name=name, debug=debug)


def create_collaborative_agent(
    name: str = "collaborative",
    collaboration_mode: str = "consensus",
    debug: bool = True) -> CollaborativeMultiAgent:
    """Create a collaborative multi-agent."""
    return CollaborativeMultiAgent(
        name=name, collaboration_mode=collaboration_mode, debug=debug
    )


# Example usage
async def example_hybrid_classify_process():
    """Example of classification-based processing."""
    agent = create_hybrid_agent(
        name="smart_processor", execution_pattern="classify_then_process"
    )

    result = await agent.arun(
        {"task": "Analyze the impact of AI on employment", "depth": "comprehensive"}
    )

    return result


async def example_adaptive_processing():
    """Example of adaptive processing."""
    agent = create_adaptive_agent(name="adaptive_system")

    # Simple task
    simple_result = await agent.arun({"request": "What is 2 + 2?", "complexity": 0.1})

    # Complex task
    complex_result = await agent.arun(
        {
            "request": "Design a distributed system for real-time analytics",
            "complexity": 0.9,
        }
    )

    return simple_result, complex_result


async def example_collaborative():
    """Example of collaborative multi-agent."""
    agent = create_collaborative_agent(
        name="collaborative_team", collaboration_mode="consensus"
    )

    result = await agent.arun(
        {
            "proposal": "Implement a new AI-powered customer service system",
            "consider": ["technical feasibility", "business impact", "user experience"],
        }
    )

    return result
