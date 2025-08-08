"""Sequential Workflow Agent - Using MultiAgent with SimpleAgentV3 patterns.

This module demonstrates creating sequential multi-agent workflows using the
MultiAgent as a base, with SimpleAgentV3 agents as components.

Shows various sequential patterns:
1. Simple linear workflows
2. Conditional branching workflows
3. Iterative refinement workflows
4. Pipeline-style processing
"""

from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.simple.agent import SimpleAgent


# Structured models for workflow stages
class ResearchBrief(BaseModel):
    """Research brief from analyzer."""

    topic: str = Field(description="Research topic")
    key_questions: list[str] = Field(description="Key questions to address")
    scope: str = Field(description="Scope and boundaries")
    priority_areas: list[str] = Field(description="Priority areas to focus on")


class ResearchFindings(BaseModel):
    """Detailed research findings."""

    topic: str = Field(description="Research topic")
    main_findings: list[str] = Field(description="Key findings")
    evidence: dict[str, list[str]] = Field(description="Evidence for each finding")
    gaps: list[str] = Field(description="Identified knowledge gaps")
    confidence_scores: dict[str, float] = Field(
        description="Confidence in each finding"
    )


class FinalReport(BaseModel):
    """Final formatted report."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")
    sections: list[dict[str, str]] = Field(description="Report sections")
    conclusions: list[str] = Field(description="Key conclusions")
    recommendations: list[str] = Field(description="Actionable recommendations")


class SequentialWorkflowAgent(MultiAgent):
    """Sequential workflow agent for multi-stage processing.

    This agent orchestrates a sequence of SimpleAgentV3 agents to
    accomplish complex tasks through staged processing.

    Example:
        >>> workflow = SequentialWorkflowAgent(
        ...     name="research_pipeline",
        ...     stages=["analyze", "research", "synthesize", "format"],
        ...     debug=True
        ... )
        >>> report = await workflow.arun("Research AI ethics implications")
    """

    # Workflow configuration
    stages: list[str] = Field(
        default_factory=lambda: ["analyze", "process", "output"],
        description="Ordered list of workflow stages",
    )

    stage_configs: dict[str, dict[str, Any]] = Field(
        default_factory=dict, description="Configuration for each stage"
    )

    def setup_agent(self) -> None:
        """Setup workflow stages as SimpleAgentV3 instances."""
        # Create default stage configurations if not provided
        default_configs = {
            "analyze": {
                "temperature": 0.3,
                "system_message": "You are an expert analyst. Break down complex requests into actionable research questions.",
                "structured_output_model": ResearchBrief,
            },
            "research": {
                "temperature": 0.5,
                "system_message": "You are a thorough researcher. Find comprehensive information and evidence.",
                "structured_output_model": ResearchFindings,
            },
            "synthesize": {
                "temperature": 0.4,
                "system_message": "You are a synthesis expert. Combine findings into coherent insights.",
            },
            "format": {
                "temperature": 0.3,
                "system_message": "You are a professional report writer. Create well-structured reports.",
                "structured_output_model": FinalReport,
            },
        }

        # Create agents for each stage
        agents = []
        for stage in self.stages:
            config = self.stage_configs.get(stage, default_configs.get(stage, {}))

            agent = SimpleAgent(
                name=f"{stage}_agent", engine=AugLLMConfig(**config), debug=self.debug
            )

            agents.append(agent)

        # Set agents list
        self.agents = agents

        # Call parent setup
        super().setup_agent()


class ConditionalWorkflowAgent(SequentialWorkflowAgent):
    """Conditional workflow with branching logic.

    This variant adds conditional routing between stages based on
    intermediate results.
    """

    routing_conditions: dict[str, callable] = Field(
        default_factory=dict, description="Conditions for routing between stages"
    )

    def setup_agent(self) -> None:
        """Setup conditional workflow with routing."""
        super().setup_agent()

        # Set execution mode to conditional
        self.execution_mode = "conditional"

        # Add default routing conditions
        if not self.routing_conditions:
            self.routing_conditions = {
                "needs_deep_research": lambda state: state.get("complexity", 0) > 0.7,
                "needs_fact_checking": lambda state: state.get("confidence", 1.0) < 0.8,
                "needs_revision": lambda state: state.get("quality_score", 1.0) < 0.85,
            }


class PipelineAgent(MultiAgent):
    """Pipeline-style agent for data transformation workflows.

    Each stage transforms data for the next stage in a pipeline pattern.
    """

    def __init__(self, **kwargs):
        # Set sequential execution by default
        kwargs.setdefault("execution_mode", "sequential")

        # Create pipeline stages
        kwargs.setdefault("agents", self._create_pipeline_stages())

        super().__init__(**kwargs)

    def _create_pipeline_stages(self) -> list[SimpleAgent]:
        """Create standard pipeline stages."""
        stages = []

        # Data extraction stage
        extractor = SimpleAgent(
            name="extractor",
            engine=AugLLMConfig(
                temperature=0.1,
                system_message="Extract key information from input data.",
            ),
            debug=True,
        )
        stages.append(extractor)

        # Data transformation stage
        transformer = SimpleAgent(
            name="transformer",
            engine=AugLLMConfig(
                temperature=0.3, system_message="Transform and enrich extracted data."
            ),
            debug=True,
        )
        stages.append(transformer)

        # Data validation stage
        validator = SimpleAgent(
            name="validator",
            engine=AugLLMConfig(
                temperature=0.1, system_message="Validate and ensure data quality."
            ),
            debug=True,
        )
        stages.append(validator)

        # Data loading stage
        loader = SimpleAgent(
            name="loader",
            engine=AugLLMConfig(
                temperature=0.1, system_message="Format data for final output."
            ),
            debug=True,
        )
        stages.append(loader)

        return stages


class IterativeRefinementAgent(MultiAgent):
    """Iterative refinement workflow with feedback loops.

    This pattern implements iterative improvement through multiple passes.
    """

    max_iterations: int = Field(default=3, description="Maximum refinement iterations")
    quality_threshold: float = Field(
        default=0.85, description="Quality threshold to stop"
    )

    def __init__(self, **kwargs):
        # Extract iteration settings
        max_iterations = kwargs.pop("max_iterations", 3)
        quality_threshold = kwargs.pop("quality_threshold", 0.85)

        # Create agents for iterative pattern
        agents = []

        # Initial creator
        creator = SimpleAgent(
            name="creator",
            engine=AugLLMConfig(
                temperature=0.7,
                system_message="Create initial content based on requirements.",
            ),
            debug=True,
        )
        agents.append(creator)

        # Quality evaluator
        evaluator = SimpleAgent(
            name="evaluator",
            engine=AugLLMConfig(
                temperature=0.3,
                system_message="Evaluate content quality and provide specific feedback.",
                structured_output_model=QualityAssessment,
            ),
            debug=True,
        )
        agents.append(evaluator)

        # Content refiner
        refiner = SimpleAgent(
            name="refiner",
            engine=AugLLMConfig(
                temperature=0.5,
                system_message="Refine content based on evaluation feedback.",
            ),
            debug=True,
        )
        agents.append(refiner)

        kwargs["agents"] = agents
        kwargs["execution_mode"] = "conditional"

        super().__init__(**kwargs)

        self.max_iterations = max_iterations
        self.quality_threshold = quality_threshold


# Supporting models
class QualityAssessment(BaseModel):
    """Quality assessment for iterative refinement."""

    quality_score: float = Field(ge=0.0, le=1.0, description="Overall quality score")
    strengths: list[str] = Field(description="Identified strengths")
    weaknesses: list[str] = Field(description="Areas for improvement")
    specific_feedback: list[str] = Field(description="Specific improvement suggestions")
    meets_threshold: bool = Field(description="Whether quality threshold is met")


# Factory functions
def create_research_workflow(
    name: str = "research_workflow", stages: list[str] | None = None, debug: bool = True
) -> SequentialWorkflowAgent:
    """Create a research workflow with default stages."""
    if stages is None:
        stages = ["analyze", "research", "synthesize", "format"]

    return SequentialWorkflowAgent(name=name, stages=stages, debug=debug)


def create_conditional_workflow(
    name: str = "conditional_workflow",
    routing_conditions: dict[str, callable] | None = None,
    debug: bool = True,
) -> ConditionalWorkflowAgent:
    """Create a conditional workflow with branching."""
    return ConditionalWorkflowAgent(
        name=name, routing_conditions=routing_conditions or {}, debug=debug
    )


def create_pipeline(name: str = "data_pipeline", debug: bool = True) -> PipelineAgent:
    """Create a data processing pipeline."""
    return PipelineAgent(name=name, debug=debug)


def create_iterative_workflow(
    name: str = "iterative_workflow",
    max_iterations: int = 3,
    quality_threshold: float = 0.85,
    debug: bool = True,
) -> IterativeRefinementAgent:
    """Create an iterative refinement workflow."""
    return IterativeRefinementAgent(
        name=name,
        max_iterations=max_iterations,
        quality_threshold=quality_threshold,
        debug=debug,
    )


# Example usage patterns
async def example_research_workflow():
    """Example of research workflow execution."""
    workflow = create_research_workflow(name="ai_ethics_research")

    result = await workflow.arun(
        {
            "task": "Research the ethical implications of AI in healthcare",
            "depth": "comprehensive",
            "audience": "policy makers",
        }
    )

    return result


async def example_conditional_workflow():
    """Example of conditional workflow with branching."""

    # Define custom routing conditions
    def needs_expert_review(state):
        return state.get("technical_complexity", 0) > 0.8

    def needs_simplification(state):
        return state.get("audience_level") == "general"

    workflow = create_conditional_workflow(
        name="adaptive_processor",
        routing_conditions={
            "expert_review": needs_expert_review,
            "simplification": needs_simplification,
        },
    )

    # Add conditional routing
    workflow.add_conditional_edge(
        from_agent="analyze_agent",
        condition=needs_expert_review,
        true_agent="expert_agent",
        false_agent="research_agent",
    )

    result = await workflow.arun(
        {
            "content": "Complex technical document about quantum computing",
            "audience_level": "general",
        }
    )

    return result


async def example_pipeline():
    """Example of pipeline processing."""
    pipeline = create_pipeline(name="document_processor")

    result = await pipeline.arun(
        {
            "document": "Raw document text with various data...",
            "format": "structured_json",
        }
    )

    return result


async def example_iterative_refinement():
    """Example of iterative refinement workflow."""
    workflow = create_iterative_workflow(
        name="content_perfecter", max_iterations=5, quality_threshold=0.9
    )

    result = await workflow.arun(
        {
            "task": "Write a compelling product description",
            "product": "AI-powered writing assistant",
            "target_audience": "content creators",
        }
    )

    return result
