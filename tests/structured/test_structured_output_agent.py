"""Tests for the StructuredOutputAgent.

These tests demonstrate how to use StructuredOutputAgent in various scenarios,
including multi-agent workflows and different output models.
"""

from pydantic import BaseModel, Field
import pytest

from haive.agents.react import ReactAgent
from haive.agents.simple import SimpleAgent
from haive.agents.structured import GenericStructuredOutput, StructuredOutputAgent
from haive.agents.structured.agent import create_structured_agent
from haive.agents.structured.models import AnalysisOutput, DecisionOutput, TaskOutput
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState


class TestStructuredOutputAgent:
    """Test suite for StructuredOutputAgent functionality."""

    def test_basic_structured_extraction(self):
        """Test basic extraction with GenericStructuredOutput."""
        agent = StructuredOutputAgent(
            name="basic_structurer",
            engine=AugLLMConfig(temperature=0.1),
            output_model=GenericStructuredOutput,
        )

        input_text = """
        The analysis of our Q4 performance shows three key findings:
        1. Revenue increased by 15% compared to Q3
        2. Customer satisfaction scores improved to 4.5/5
        3. New product adoption rate exceeded targets by 20%

        We should focus on maintaining this momentum and addressing
        the minor issues in customer support response times.
        """

        result = agent.run(input_text)

        # Verify it's the right type
        assert isinstance(result, GenericStructuredOutput)
        assert len(result.key_points) > 0
        assert result.main_content
        assert 0.0 <= result.confidence <= 1.0

    def test_analysis_output_extraction(self):
        """Test extraction with AnalysisOutput model."""
        agent = create_structured_agent(
            output_model=AnalysisOutput,
            name="analysis_structurer",
            custom_context="Focus on business metrics and recommendations",
        )

        input_text = """
        After analyzing the market data, we found that our product has strong
        potential in the enterprise segment. The data shows 70% of enterprises
        are looking for similar solutions. However, we need to improve our
        pricing model to be competitive. I recommend a tiered pricing approach
        and investing in enterprise features.
        """

        result = agent.run(input_text)

        assert isinstance(result, AnalysisOutput)
        assert result.summary
        assert len(result.findings) > 0
        assert len(result.recommendations) > 0

    def test_multi_agent_workflow_with_react(self):
        """Test StructuredOutputAgent in multi-agent workflow with ReactAgent."""

        # Define custom output model
        class PlanOutput(BaseModel):
            objective: str = Field(description="Main objective")
            steps: list[str] = Field(description="Steps to achieve objective")
            timeline: str = Field(description="Estimated timeline")
            risks: list[str] = Field(
                default_factory=list, description="Potential risks"
            )

        # Create multi-agent state
        class PlanningState(MultiAgentState):
            # Input
            request: str = ""

            # ReactAgent output (unstructured, in messages)

            # StructuredOutputAgent fields (from PlanOutput)
            objective: str = ""
            steps: list[str] = Field(default_factory=list)
            timeline: str = ""
            risks: list[str] = Field(default_factory=list)

        # Create agents
        planner = ReactAgent(
            name="planner",
            engine=AugLLMConfig(
                system_message="You are a strategic planner. Create detailed plans."
            ),
            tools=[],  # Could add planning tools
        )

        structurer = StructuredOutputAgent(
            name="plan_structurer",
            engine=AugLLMConfig(temperature=0.1),
            output_model=PlanOutput,
            structured_output_model=PlanOutput,
        )

        # Initialize state
        state = PlanningState(
            agents=[planner, structurer],
            request="Create a plan to launch a new mobile app",
        )

        # Execute workflow
        config = {"configurable": {"thread_id": "test_planning"}}

        # ReactAgent creates unstructured plan
        planner_node = create_agent_node_v3("planner")
        planner_node(state, config)

        # StructuredOutputAgent structures it
        structurer_node = create_agent_node_v3("plan_structurer")
        structurer_node(state, config)

        # Verify structured output in state
        assert state.objective
        assert len(state.steps) > 0
        assert state.timeline
        # Risks might be empty but field should exist
        assert isinstance(state.risks, list)

    def test_sequential_simple_agents(self):
        """Test StructuredOutputAgent after SimpleAgent."""

        # Create state
        class ResearchState(MultiAgentState):
            topic: str = ""

            # SimpleAgent output (unstructured)

            # Structured output
            task_description: str = ""
            steps: list[str] = Field(default_factory=list)
            requirements: list[str] = Field(default_factory=list)
            complexity: int = 5

        # Create agents
        researcher = SimpleAgent(
            name="researcher",
            engine=AugLLMConfig(
                system_message="Research topics and provide detailed information."
            ),
            # No structured_output_model - outputs unstructured text
        )

        task_converter = StructuredOutputAgent(
            name="task_converter",
            output_model=TaskOutput,
            custom_context="Convert research into actionable tasks",
        )

        state = ResearchState(
            agents=[researcher, task_converter], topic="Implementing AI chatbots"
        )

        config = {"configurable": {"thread_id": "test_research"}}

        # Run both agents
        researcher_node = create_agent_node_v3("researcher")
        converter_node = create_agent_node_v3("task_converter")

        researcher_node(state, config)
        converter_node(state, config)

        # Check structured output
        assert state.task_description
        assert len(state.steps) > 0
        assert 1 <= state.complexity <= 10

    def test_custom_prompt_template(self):
        """Test StructuredOutputAgent with custom prompt."""
        from langchain_core.prompts import ChatPromptTemplate

        custom_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Extract only the most important information. Be extremely concise.",
                ),
                ("human", "{input}"),
            ]
        )

        agent = StructuredOutputAgent(
            name="concise_structurer",
            engine=AugLLMConfig(),
            output_model=GenericStructuredOutput,
            custom_prompt=custom_prompt,
        )

        result = agent.run("This is a very long text with many details...")

        assert isinstance(result, GenericStructuredOutput)
        assert result.main_content  # Should be concise

    def test_extract_from_messages(self):
        """Test extracting from message list."""
        from langchain_core.messages import AIMessage, HumanMessage

        agent = create_structured_agent(
            output_model=DecisionOutput, name="decision_extractor"
        )

        messages = [
            HumanMessage(content="Should we proceed with the merger?"),
            AIMessage(
                content="""
            Yes, we should proceed with the merger. The financial analysis
            shows strong synergies, and the cultural fit is good. However,
            we need to consider regulatory approval timelines. The alternative
            would be organic growth, but that would take much longer.
            """
            ),
        ]

        result = agent.extract_from_messages(messages)

        assert isinstance(result, DecisionOutput)
        assert result.decision
        assert result.reasoning
        assert 0.0 <= result.confidence <= 1.0


@pytest.mark.integration
class TestStructuredOutputIntegration:
    """Integration tests with real LLMs."""

    def test_real_llm_extraction(self):
        """Test with real LLM (requires API keys)."""
        agent = create_structured_agent(
            output_model=AnalysisOutput, name="real_analysis"
        )

        complex_text = """
        Our comprehensive study of user behavior reveals several critical insights.
        First, mobile users spend 40% more time on our platform compared to desktop users.
        Second, the new recommendation algorithm has increased engagement by 25%.
        However, we identified that page load times over 3 seconds cause a 50% drop
        in user retention.

        Based on these findings, we recommend prioritizing mobile optimization,
        continuing to refine the recommendation system, and investing heavily
        in performance improvements. The confidence in these findings is high,
        based on data from over 100,000 users over 6 months.
        """

        result = agent.run(complex_text)

        # With real LLM, we should get quality extraction
        assert isinstance(result, AnalysisOutput)
        assert len(result.findings) >= 3
        assert len(result.recommendations) >= 2
        assert result.confidence_score >= 0.7
        assert result.summary
