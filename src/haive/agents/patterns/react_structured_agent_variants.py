"""React Structured Agent Variants - Building on base Agent patterns.

This module creates various ReactAgent → SimpleAgent patterns using the base
agent.py architecture, as requested. Shows different ways to combine agents
for structured workflows with reasoning and output formatting.

Variants include:
1. Basic React → Simple structured flow
2. Multi-stage reasoning with structured outputs
3. Tool-enhanced React → Simple patterns
4. Reflection-enabled variants
"""

from typing import Any, Dict, List, Type

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langgraph.graph import END, START
from pydantic import BaseModel, Field

from haive.agents.base.agent import Agent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class AnalysisResult(BaseModel):
    """Structured analysis from reasoning."""

    problem_statement: str = Field(description="Clear problem statement")
    key_factors: List[str] = Field(description="Key factors identified")
    analysis_approach: str = Field(description="Approach taken for analysis")
    findings: Dict[str, Any] = Field(description="Detailed findings")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in analysis")


class StructuredSolution(BaseModel):
    """Structured solution output."""

    solution_summary: str = Field(description="Brief solution summary")
    implementation_steps: List[str] = Field(description="Step-by-step implementation")
    requirements: List[str] = Field(description="Requirements for implementation")
    risks: List[str] = Field(description="Potential risks and mitigation")
    success_metrics: List[str] = Field(description="How to measure success")


class ReactToStructuredAgent(Agent):
    """React → Structured output agent pattern.

    This agent combines ReactAgent for reasoning with SimpleAgentV3 for
    structured output generation, following the base Agent pattern.

    Example:
        >>> agent = ReactToStructuredAgent(
        ...     name="analyzer",
        ...     tools=[calculator, search_tool],
        ...     output_model=AnalysisResult,
        ...     debug=True
        ... )
        >>> result = await agent.arun("Analyze market trends")
    """

    # Sub-agents
    react_agent: ReactAgent = Field(None, description="Reasoning agent")
    structure_agent: SimpleAgentV3 = Field(None, description="Structuring agent")

    # Configuration
    reasoning_temperature: float = Field(
        default=0.5, description="Temperature for reasoning"
    )
    structuring_temperature: float = Field(
        default=0.3, description="Temperature for structuring"
    )
    output_model: Type[BaseModel] = Field(
        default=StructuredSolution, description="Output structure"
    )
    tools: List[Any] = Field(default_factory=list, description="Tools for reasoning")

    def setup_agent(self) -> None:
        """Setup React and Simple agents."""
        # Create ReactAgent for reasoning
        if not self.react_agent:
            self.react_agent = ReactAgent(
                name=f"{self.name}_reasoner",
                engine=AugLLMConfig(
                    temperature=self.reasoning_temperature,
                    system_message="You are a reasoning agent. Use tools to gather information and analyze problems thoroughly.",
                    tools=self.tools,
                ),
            )

        # Create SimpleAgentV3 for structured output
        if not self.structure_agent:
            self.structure_agent = SimpleAgentV3(
                name=f"{self.name}_structurer",
                engine=AugLLMConfig(
                    temperature=self.structuring_temperature,
                    system_message="You are a structured output specialist. Convert analysis into well-formatted structured data.",
                    structured_output_model=self.output_model,
                ),
                prompt_template=ChatPromptTemplate.from_messages(
                    [
                        ("system", "{system_message}"),
                        (
                            "human",
                            """Based on this analysis:
{reasoning_output}

Create a structured output with all required fields properly filled.""",
                        ),
                    ]
                ),
            )

        # Add agents to engines
        self.engines = {
            "reasoner": self.react_agent,
            "structurer": self.structure_agent,
        }

    def build_graph(self) -> BaseGraph:
        """Build React → Structured graph."""
        graph = BaseGraph(name=f"{self.name}_graph")

        # Add nodes
        react_node = create_agent_node_v3("reasoner", self.react_agent)
        structure_node = create_agent_node_v3("structurer", self.structure_agent)

        graph.add_node("reasoner", react_node)
        graph.add_node("structurer", structure_node)

        # Connect: START -> reasoner -> structurer -> END
        graph.add_edge(START, "reasoner")
        graph.add_edge("reasoner", "structurer")
        graph.add_edge("structurer", END)

        return graph


class MultiStageReasoningAgent(Agent):
    """Multi-stage reasoning with structured outputs at each stage.

    This pattern chains multiple reasoning stages, each producing
    structured outputs that feed into the next stage.
    """

    stages: List[Dict[str, Any]] = Field(
        default_factory=list, description="Configuration for each reasoning stage"
    )

    def setup_agent(self) -> None:
        """Setup multi-stage reasoning pipeline."""
        # Default stages if not provided
        if not self.stages:
            self.stages = [
                {
                    "name": "problem_analysis",
                    "type": "react",
                    "output_model": AnalysisResult,
                    "system_message": "Analyze the problem and identify key factors.",
                },
                {
                    "name": "solution_design",
                    "type": "simple",
                    "output_model": StructuredSolution,
                    "system_message": "Design a solution based on the analysis.",
                },
                {
                    "name": "validation",
                    "type": "react",
                    "tools": [self._create_validator_tool()],
                    "system_message": "Validate the proposed solution.",
                },
            ]

        # Create agents for each stage
        self.stage_agents = {}
        for stage in self.stages:
            if stage["type"] == "react":
                agent = ReactAgent(
                    name=stage["name"],
                    engine=AugLLMConfig(
                        temperature=0.5,
                        system_message=stage.get("system_message", ""),
                        tools=stage.get("tools", []),
                        structured_output_model=stage.get("output_model"),
                    ),
                )
            else:  # simple
                agent = SimpleAgentV3(
                    name=stage["name"],
                    engine=AugLLMConfig(
                        temperature=0.3,
                        system_message=stage.get("system_message", ""),
                        structured_output_model=stage.get("output_model"),
                    ),
                )

            self.stage_agents[stage["name"]] = agent
            self.engines[stage["name"]] = agent

    def _create_validator_tool(self):
        """Create validation tool."""

        @tool
        def validate_solution(solution: str) -> str:
            """Validate a proposed solution."""
            return f"Validation result: Solution appears feasible with minor adjustments needed."

        return validate_solution

    def build_graph(self) -> BaseGraph:
        """Build multi-stage graph."""
        graph = BaseGraph(name=f"{self.name}_graph")

        # Add nodes for each stage
        stage_names = []
        for stage_name, agent in self.stage_agents.items():
            node = create_agent_node_v3(stage_name, agent)
            graph.add_node(stage_name, node)
            stage_names.append(stage_name)

        # Connect stages sequentially
        if stage_names:
            graph.add_edge(START, stage_names[0])

            for i in range(len(stage_names) - 1):
                graph.add_edge(stage_names[i], stage_names[i + 1])

            graph.add_edge(stage_names[-1], END)

        return graph


class ToolEnhancedStructuredAgent(ReactToStructuredAgent):
    """Enhanced React → Structured agent with specialized tools.

    This variant adds domain-specific tools for enhanced reasoning.
    """

    def setup_agent(self) -> None:
        """Setup with enhanced tools."""

        # Create domain-specific tools
        @tool
        def analyze_data(data_description: str) -> str:
            """Analyze described data patterns."""
            return f"Analysis of {data_description}: Identified 3 key patterns and 2 anomalies."

        @tool
        def research_topic(topic: str) -> str:
            """Research a specific topic."""
            return (
                f"Research on {topic}: Found 5 relevant studies and 3 expert opinions."
            )

        @tool
        def calculate_metrics(expression: str) -> str:
            """Calculate business metrics."""
            try:
                result = eval(expression)
                return f"Calculation result: {result}"
            except:
                return "Calculation error - please check expression"

        # Add tools if not already provided
        if not self.tools:
            self.tools = [analyze_data, research_topic, calculate_metrics]

        # Call parent setup
        super().setup_agent()


class ReflectiveStructuredAgent(Agent):
    """React → Structured → Reflection pattern.

    This adds a reflection stage that reviews and improves the
    structured output before final delivery.
    """

    include_reflection: bool = Field(
        default=True, description="Include reflection stage"
    )
    output_model: Type[BaseModel] = Field(default=StructuredSolution)

    def setup_agent(self) -> None:
        """Setup reasoning, structuring, and reflection agents."""
        # Reasoning agent
        self.reasoner = ReactAgent(
            name=f"{self.name}_reasoner",
            engine=AugLLMConfig(
                temperature=0.5,
                system_message="Analyze problems using reasoning and available tools.",
            ),
        )

        # Structuring agent
        self.structurer = SimpleAgentV3(
            name=f"{self.name}_structurer",
            engine=AugLLMConfig(
                temperature=0.3,
                system_message="Convert analysis into structured format.",
                structured_output_model=self.output_model,
            ),
        )

        # Reflection agent
        if self.include_reflection:
            self.reflector = SimpleAgentV3(
                name=f"{self.name}_reflector",
                engine=AugLLMConfig(
                    temperature=0.4,
                    system_message="Review and improve the structured output for clarity and completeness.",
                ),
            )

        # Register engines
        self.engines = {"reasoner": self.reasoner, "structurer": self.structurer}
        if self.include_reflection:
            self.engines["reflector"] = self.reflector

    def build_graph(self) -> BaseGraph:
        """Build graph with optional reflection."""
        graph = BaseGraph(name=f"{self.name}_graph")

        # Add nodes
        graph.add_node("reasoner", create_agent_node_v3("reasoner", self.reasoner))
        graph.add_node(
            "structurer", create_agent_node_v3("structurer", self.structurer)
        )

        if self.include_reflection:
            graph.add_node(
                "reflector", create_agent_node_v3("reflector", self.reflector)
            )

        # Connect nodes
        graph.add_edge(START, "reasoner")
        graph.add_edge("reasoner", "structurer")

        if self.include_reflection:
            graph.add_edge("structurer", "reflector")
            graph.add_edge("reflector", END)
        else:
            graph.add_edge("structurer", END)

        return graph


# Factory functions
def create_react_structured_agent(
    name: str = "react_structured",
    tools: List[Any] = None,
    output_model: Type[BaseModel] = StructuredSolution,
    debug: bool = True,
) -> ReactToStructuredAgent:
    """Create a React → Structured agent."""
    return ReactToStructuredAgent(
        name=name, tools=tools or [], output_model=output_model, debug=debug
    )


def create_multi_stage_reasoning_agent(
    name: str = "multi_stage", stages: List[Dict[str, Any]] = None, debug: bool = True
) -> MultiStageReasoningAgent:
    """Create a multi-stage reasoning agent."""
    return MultiStageReasoningAgent(name=name, stages=stages or [], debug=debug)


def create_tool_enhanced_agent(
    name: str = "tool_enhanced",
    output_model: Type[BaseModel] = AnalysisResult,
    debug: bool = True,
) -> ToolEnhancedStructuredAgent:
    """Create a tool-enhanced structured agent."""
    return ToolEnhancedStructuredAgent(
        name=name, output_model=output_model, debug=debug
    )


def create_reflective_structured_agent(
    name: str = "reflective",
    include_reflection: bool = True,
    output_model: Type[BaseModel] = StructuredSolution,
    debug: bool = True,
) -> ReflectiveStructuredAgent:
    """Create a reflective structured agent."""
    return ReflectiveStructuredAgent(
        name=name,
        include_reflection=include_reflection,
        output_model=output_model,
        debug=debug,
    )


# Example usage
async def example_basic_react_structured():
    """Example of basic React → Structured flow."""
    agent = create_react_structured_agent(
        name="problem_solver", output_model=StructuredSolution
    )

    result = await agent.arun("How can we improve customer retention?")
    return result


async def example_multi_stage():
    """Example of multi-stage reasoning."""
    stages = [
        {
            "name": "understand",
            "type": "react",
            "system_message": "Understand the problem deeply.",
        },
        {
            "name": "analyze",
            "type": "react",
            "output_model": AnalysisResult,
            "system_message": "Analyze all aspects thoroughly.",
        },
        {
            "name": "solve",
            "type": "simple",
            "output_model": StructuredSolution,
            "system_message": "Create a comprehensive solution.",
        },
    ]

    agent = create_multi_stage_reasoning_agent(
        name="comprehensive_solver", stages=stages
    )

    result = await agent.arun("Design a scalable microservices architecture")
    return result


async def example_reflective():
    """Example of reflective structured output."""
    agent = create_reflective_structured_agent(
        name="thoughtful_solver", include_reflection=True
    )

    result = await agent.arun("Create a disaster recovery plan for our systems")
    return result
