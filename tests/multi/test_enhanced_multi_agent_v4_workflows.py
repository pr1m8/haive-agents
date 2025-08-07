"""Test EnhancedMultiAgentV4 workflows with real agents and tools.

Date: August 7, 2025
Purpose: Test various multi-agent patterns with tool isolation
"""

import pytest
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Define structured output models
class AnalysisResult(BaseModel):
    """Result from analysis phase."""
    findings: List[str] = Field(description="Key findings from analysis")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    next_steps: List[str] = Field(description="Recommended next steps")


class FormattedReport(BaseModel):
    """Final formatted report."""
    executive_summary: str = Field(description="Brief executive summary")
    detailed_findings: str = Field(description="Detailed findings section")
    recommendations: List[str] = Field(description="Action recommendations")
    conclusion: str = Field(description="Report conclusion")


class ClassificationResult(BaseModel):
    """Classification result for routing."""
    category: str = Field(description="Category: technical, business, or general")
    complexity: float = Field(ge=0.0, le=1.0, description="Complexity score")
    reasoning: str = Field(description="Classification reasoning")


# Define tools for different agents
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error calculating {expression}: {str(e)}"


@tool
def word_counter(text: str) -> str:
    """Count words in text."""
    words = text.split()
    return f"Word count: {len(words)} words"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text characteristics."""
    words = text.split()
    chars = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    return f"Analysis: {len(words)} words, {chars} characters, {sentences} sentences"


@tool
def formatter(text: str, style: str = "bullet") -> str:
    """Format text in different styles."""
    if style == "bullet":
        lines = text.split('\n')
        return '\n'.join([f"• {line.strip()}" for line in lines if line.strip()])
    elif style == "numbered":
        lines = text.split('\n')
        return '\n'.join([f"{i+1}. {line.strip()}" for i, line in enumerate(lines) if line.strip()])
    return text


class TestEnhancedMultiAgentV4Workflows:
    """Test various multi-agent workflow patterns."""

    @pytest.fixture
    def base_config(self) -> AugLLMConfig:
        """Base configuration for agents."""
        return AugLLMConfig(
            temperature=0.1,  # Low for consistent tests
            max_tokens=500
        )

    @pytest.mark.asyncio
    async def test_sequential_react_to_simple_workflow(self, base_config):
        """Test ReactAgent → SimpleAgent sequential workflow with structured output."""
        # Create ReactAgent with analysis tools
        analyzer = ReactAgentV4(
            name="analyzer",
            engine=base_config,
            tools=[calculator, word_counter],  # Agent-specific tools
            debug=True
        )
        
        # Create SimpleAgent with structured output
        formatter = SimpleAgentV3(
            name="formatter",
            engine=base_config,
            structured_output_model=FormattedReport,
            debug=True
        )
        
        # Create sequential workflow
        workflow = EnhancedMultiAgentV4(
            name="analysis_workflow",
            agents=[analyzer, formatter],
            execution_mode="sequential"
        )
        
        # Execute workflow
        result = await workflow.arun({
            "messages": [HumanMessage(content=
                "Analyze this data: Sales increased by 25% this quarter. "
                "We have 1500 new customers. Calculate the average if we had 6000 customers before."
            )]
        })
        
        # Verify structured output
        assert hasattr(workflow.state, "formatter")
        assert isinstance(workflow.state.formatter, FormattedReport)
        assert workflow.state.formatter.executive_summary
        assert len(workflow.state.formatter.recommendations) > 0
        
        # Verify tool isolation - each agent has only its tools
        assert len(analyzer.tools) == 2
        assert len(formatter.tools) == 0  # SimpleAgent has no tools
        
        # Mark task complete
        self.todos[0]['status'] = 'completed'
        self.todos[1]['status'] = 'completed'

    @pytest.mark.asyncio
    async def test_parallel_execution_with_different_tools(self, base_config):
        """Test parallel execution with agents having different tools."""
        # Create agents with different tools
        math_agent = ReactAgentV4(
            name="math_analyst",
            engine=base_config,
            tools=[calculator],  # Only calculator
            debug=True
        )
        
        text_agent = ReactAgentV4(
            name="text_analyst",
            engine=base_config,
            tools=[word_counter, text_analyzer],  # Only text tools
            debug=True
        )
        
        format_agent = ReactAgentV4(
            name="format_specialist",
            engine=base_config,
            tools=[formatter],  # Only formatter
            debug=True
        )
        
        # Create parallel workflow
        workflow = EnhancedMultiAgentV4(
            name="parallel_analysis",
            agents=[math_agent, text_agent, format_agent],
            execution_mode="parallel"
        )
        
        # Execute
        result = await workflow.arun({
            "messages": [HumanMessage(content=
                "Process this: Calculate 150 * 4. This message has multiple sentences. "
                "Format this list: apple\nbanana\norange"
            )]
        })
        
        # Verify all agents executed
        assert "math_analyst" in workflow.state.agent_outputs
        assert "text_analyst" in workflow.state.agent_outputs
        assert "format_specialist" in workflow.state.agent_outputs
        
        # Verify tool isolation
        assert calculator in math_agent.tools
        assert calculator not in text_agent.tools
        assert calculator not in format_agent.tools
        
        assert word_counter in text_agent.tools
        assert word_counter not in math_agent.tools
        
        # Mark task complete
        self.todos[2]['status'] = 'completed'
        self.todos[4]['status'] = 'completed'

    @pytest.mark.asyncio
    async def test_conditional_routing_workflow(self, base_config):
        """Test conditional routing based on classification."""
        # Create classifier agent
        classifier = SimpleAgentV3(
            name="classifier",
            engine=base_config,
            structured_output_model=ClassificationResult,
            debug=True
        )
        
        # Create specialized agents with different tools
        technical_agent = ReactAgentV4(
            name="technical_expert",
            engine=base_config,
            tools=[calculator, text_analyzer],
            debug=True
        )
        
        business_agent = SimpleAgentV3(
            name="business_expert",
            engine=base_config,
            structured_output_model=FormattedReport,
            debug=True
        )
        
        general_agent = SimpleAgentV3(
            name="general_assistant",
            engine=base_config,
            debug=True
        )
        
        # Create conditional workflow
        workflow = EnhancedMultiAgentV4(
            name="smart_router",
            agents=[classifier, technical_agent, business_agent, general_agent],
            execution_mode="conditional",
            build_mode="manual"
        )
        
        # Define routing condition
        def route_by_category(state):
            """Route based on classification."""
            if hasattr(state, 'classifier') and state.classifier:
                return state.classifier.category
            return "general"
        
        # Add routing edges
        workflow.add_edge("START", "classifier")
        workflow.add_multi_conditional_edge(
            from_agent="classifier",
            condition=route_by_category,
            routes={
                "technical": "technical_expert",
                "business": "business_expert",
                "general": "general_assistant"
            },
            default="general_assistant"
        )
        
        # Add edges to END
        workflow.add_edge("technical_expert", "END")
        workflow.add_edge("business_expert", "END")
        workflow.add_edge("general_assistant", "END")
        
        # Build the workflow
        workflow.build()
        
        # Test technical routing
        result = await workflow.arun({
            "messages": [HumanMessage(content=
                "Calculate the algorithmic complexity of a sorting algorithm with n=1000"
            )]
        })
        
        # Verify routing
        assert hasattr(workflow.state, "classifier")
        assert workflow.state.classifier.category in ["technical", "business", "general"]
        
        # Mark task complete
        self.todos[3]['status'] = 'completed'

    @pytest.mark.asyncio
    async def test_complex_data_flow_workflow(self, base_config):
        """Test complex workflow with data flowing through structured outputs."""
        # Define structured models for data flow
        class ResearchFindings(BaseModel):
            topics: List[str] = Field(description="Research topics found")
            key_facts: Dict[str, str] = Field(description="Key facts discovered")
            confidence_scores: Dict[str, float] = Field(description="Confidence per topic")
        
        class AnalysisOutput(BaseModel):
            primary_insights: List[str] = Field(description="Primary insights")
            supporting_data: Dict[str, Any] = Field(description="Supporting data")
            recommendations: List[str] = Field(description="Recommendations")
        
        class FinalReport(BaseModel):
            title: str = Field(description="Report title")
            executive_summary: str = Field(description="Executive summary")
            insights_section: str = Field(description="Insights from analysis")
            data_section: str = Field(description="Supporting data")
            conclusion: str = Field(description="Final conclusion")
        
        # Create agents with structured outputs
        researcher = SimpleAgentV3(
            name="researcher",
            engine=base_config,
            structured_output_model=ResearchFindings,
            debug=True
        )
        
        analyst = SimpleAgentV3(
            name="analyst",
            engine=base_config,
            structured_output_model=AnalysisOutput,
            prompt_template="Analyze the research findings:\nTopics: {researcher.topics}\nFacts: {researcher.key_facts}\nProvide insights.",
            debug=True
        )
        
        reporter = SimpleAgentV3(
            name="reporter",
            engine=base_config,
            structured_output_model=FinalReport,
            prompt_template="Create report from:\nInsights: {analyst.primary_insights}\nData: {analyst.supporting_data}\nTopics: {researcher.topics}",
            debug=True
        )
        
        # Create workflow
        workflow = EnhancedMultiAgentV4(
            name="research_pipeline",
            agents=[researcher, analyst, reporter],
            execution_mode="sequential"
        )
        
        # Execute
        result = await workflow.arun({
            "messages": [HumanMessage(content="Research the impact of AI on productivity in 2025")]
        })
        
        # Verify data flow through structured outputs
        assert hasattr(workflow.state, "researcher")
        assert hasattr(workflow.state, "analyst")
        assert hasattr(workflow.state, "reporter")
        
        assert isinstance(workflow.state.researcher, ResearchFindings)
        assert isinstance(workflow.state.analyst, AnalysisOutput)
        assert isinstance(workflow.state.reporter, FinalReport)
        
        # Verify data was passed through
        assert len(workflow.state.researcher.topics) > 0
        assert len(workflow.state.analyst.primary_insights) > 0
        assert workflow.state.reporter.title

    @pytest.mark.asyncio
    async def test_dynamic_agent_addition(self, base_config):
        """Test dynamically adding agents to workflow."""
        # Start with simple workflow
        workflow = EnhancedMultiAgentV4(
            name="dynamic_workflow",
            agents=[
                SimpleAgentV3(name="initial", engine=base_config)
            ],
            execution_mode="sequential",
            build_mode="auto"  # Auto-rebuild on changes
        )
        
        # Execute initial
        result = await workflow.arun({
            "messages": [HumanMessage(content="Start processing")]
        })
        
        # Add new agent dynamically
        validator = SimpleAgentV3(
            name="validator",
            engine=base_config,
            structured_output_model=AnalysisResult
        )
        
        workflow.add_agent(validator)
        
        # Verify agent was added
        assert "validator" in workflow.get_agent_names()
        assert workflow.state.agents_needing_recompile  # Should need recompile
        
        # Execute again - should include validator
        result = await workflow.arun({
            "messages": [HumanMessage(content="Process with validation")]
        })
        
        # Verify validator executed
        assert hasattr(workflow.state, "validator")

    @pytest.fixture(autouse=True)
    def todos(self):
        """Track test progress."""
        return [
            {"id": "1", "status": "in_progress"},
            {"id": "2", "status": "pending"},
            {"id": "3", "status": "pending"},
            {"id": "4", "status": "pending"},
            {"id": "5", "status": "pending"}
        ]


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])