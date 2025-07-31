"""Advanced Multi-Agent Pattern Tests.

This test demonstrates:
1. Sequential multi-agent flow with prompt templates and input variables
2. ReactAgent → SimpleAgent with structured output
3. Reflection patterns with pre/post hooks
4. Complete hook lifecycle monitoring
"""

import asyncio

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.base.hooks import HookContext, HookEvent
from haive.agents.base.pre_post_agent_mixin import (
    create_reflection_agent,
)
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# ============================================================================
# STRUCTURED OUTPUT MODELS
# ============================================================================


class ResearchFindings(BaseModel):
    """Structured output for research agent."""

    topics: list[str] = Field(description="Main topics discovered")
    key_facts: list[str] = Field(description="Key facts found")
    sources: list[str] = Field(description="Information sources referenced")
    confidence_score: float = Field(
        ge=0.0, le=1.0, description="Confidence in findings"
    )


class ArticleOutline(BaseModel):
    """Structured output for article outline."""

    title: str = Field(description="Article title")
    introduction: str = Field(description="Introduction paragraph")
    sections: list[str] = Field(description="Main section headings")
    key_points: list[str] = Field(description="Key points to cover")
    conclusion_focus: str = Field(description="Main conclusion focus")


class FinalArticle(BaseModel):
    """Structured output for final article."""

    title: str = Field(description="Article title")
    content: str = Field(description="Full article content")
    word_count: int = Field(description="Total word count")
    sections_count: int = Field(description="Number of sections")
    quality_score: float = Field(ge=0.0, le=1.0, description="Self-assessed quality")


class ReflectionGrade(BaseModel):
    """Grade for reflection."""

    clarity: float = Field(ge=0.0, le=10.0, description="Clarity score")
    completeness: float = Field(ge=0.0, le=10.0, description="Completeness score")
    accuracy: float = Field(ge=0.0, le=10.0, description="Accuracy score")
    overall: float = Field(ge=0.0, le=10.0, description="Overall score")
    feedback: str = Field(description="Specific feedback for improvement")
    needs_revision: bool = Field(description="Whether revision is needed")


# ============================================================================
# HOOK FUNCTIONS FOR MONITORING
# ============================================================================


def create_monitoring_hooks():
    """Create comprehensive monitoring hooks."""
    execution_log = []

    def log_event(context: HookContext):
        """Log all hook events."""
        event_info = {
            "event": context.event.value,
            "agent": context.agent_name,
            "timestamp": context.timestamp.isoformat() if context.timestamp else None,
        }

        # Add specific context based on event
        if context.event in [HookEvent.AFTER_RUN, HookEvent.AFTER_ARUN]:
            if hasattr(context, "result"):
                event_info["has_result"] = True
                if isinstance(context.result, dict):
                    event_info["result_keys"] = list(context.result.keys())

        if context.event in [HookEvent.PRE_PROCESS, HookEvent.POST_PROCESS]:
            if hasattr(context, "pre_agent") and context.pre_agent:
                event_info["pre_agent"] = context.pre_agent.name
            if hasattr(context, "post_agent") and context.post_agent:
                event_info["post_agent"] = context.post_agent.name

        execution_log.append(event_info)

    return log_event, execution_log


# ============================================================================
# AGENT CREATION FUNCTIONS
# ============================================================================


def create_research_agent() -> ReactAgentV3:
    """Create research agent with tools and structured output."""
    from langchain_core.tools import tool

    @tool
    def search_knowledge_base(query: str) -> str:
        """Search internal knowledge base."""
        return f"Found information about {query}: This is detailed information about the topic..."

    @tool
    def analyze_topic(topic: str) -> str:
        """Analyze a specific topic in depth."""
        return f"Analysis of {topic}: Key aspects include complexity, relevance, and impact..."

    config = AugLLMConfig(
        temperature=0.7,
        structured_output_model=ResearchFindings,
        system_message="You are a thorough research analyst. Always provide structured findings.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                "Research topic: {topic}\nSpecific focus: {focus}\nDepth level: {depth}",
            ),
        ]
    )

    agent = ReactAgentV3(
        name="researcher",
        engine=config,
        prompt_template=prompt,
        tools=[search_knowledge_base, analyze_topic],
    )

    return agent


def create_outline_agent() -> SimpleAgentV3:
    """Create outline agent with structured output."""
    config = AugLLMConfig(
        temperature=0.6,
        structured_output_model=ArticleOutline,
        system_message="You are an expert content strategist who creates detailed article outlines.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                """Based on these research findings:
{research_findings}

Create a comprehensive article outline for topic: {topic}
Target audience: {audience}
Article length: {length} words""",
            ),
        ]
    )

    agent = SimpleAgentV3(name="outliner", engine=config, prompt_template=prompt)

    return agent


def create_writer_agent() -> SimpleAgentV3:
    """Create writer agent with structured output."""
    config = AugLLMConfig(
        temperature=0.8,
        structured_output_model=FinalArticle,
        system_message="You are a skilled content writer who creates engaging, well-structured articles.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                """Write a complete article based on this outline:
{outline}

Additional context:
- Topic: {topic}
- Target audience: {audience}
- Desired tone: {tone}
- Length: {length} words

Ensure the article is engaging, informative, and well-structured.""",
            ),
        ]
    )

    agent = SimpleAgentV3(name="writer", engine=config, prompt_template=prompt)

    return agent


def create_reflection_critic() -> SimpleAgentV3:
    """Create reflection critic agent."""
    config = AugLLMConfig(
        temperature=0.4,
        structured_output_model=ReflectionGrade,
        system_message="You are a critical editor who provides constructive feedback on written content.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                """Review this article and provide detailed feedback:

{article_content}

Evaluation criteria:
- Clarity and readability
- Completeness of coverage
- Accuracy and coherence
- Overall quality

Provide specific, actionable feedback.""",
            ),
        ]
    )

    agent = SimpleAgentV3(name="critic", engine=config, prompt_template=prompt)

    return agent


# ============================================================================
# TEST CASES
# ============================================================================


class TestAdvancedMultiAgentPatterns:

    async def test_sequential_with_structured_output(self):
        """Test ReactAgent → SimpleAgent flow with structured outputs."""
        # Create agents
        researcher = create_research_agent()
        outliner = create_outline_agent()
        writer = create_writer_agent()

        # Create sequential workflow
        workflow = EnhancedMultiAgentV4(
            agents=[researcher, outliner, writer], mode="sequential"
        )

        # Create initial state with messages

        initial_state = {
            "messages": [
                HumanMessage(
                    content="""Research the following:
Topic: The Future of AI in Healthcare
Focus: diagnostic tools and patient care
Depth: comprehensive

Please provide structured findings."""
                )
            ],
            "topic": "The Future of AI in Healthcare",
            "focus": "diagnostic tools and patient care",
            "depth": "comprehensive",
            "audience": "healthcare professionals",
            "length": "1500",
            "tone": "professional yet accessible",
            "research_findings": "",  # Will be filled by researcher
            "outline": "",  # Will be filled by outliner
        }

        # Execute workflow
        result = await workflow.arun(initial_state)

        # Print results
        if "messages" in result:
            for msg in result["messages"]:
                if isinstance(msg, AIMessage):
                    pass

        return result

    async def test_reflection_pattern_with_hooks(self):
        """Test reflection pattern with comprehensive hooks."""
        # Create monitoring hooks
        log_hook, execution_log = create_monitoring_hooks()

        # Create base writer agent
        writer = create_writer_agent()

        # Add hooks to monitor execution
        writer.add_hook(HookEvent.BEFORE_RUN, log_hook)
        writer.add_hook(HookEvent.AFTER_RUN, log_hook)
        writer.add_hook(HookEvent.PRE_PROCESS, log_hook)
        writer.add_hook(HookEvent.POST_PROCESS, log_hook)

        # Create reflection-enhanced writer
        enhanced_writer = create_reflection_agent(
            main_agent=writer,
            reflection_config=AugLLMConfig(
                temperature=0.3,
                system_message="You are a thoughtful critic who improves writing through constructive reflection.",
            ),
        )

        # Execute with reflection
        inputs = {
            "outline": """
            Title: AI in Healthcare: The Next Frontier
            1. Introduction: Current state of healthcare
            2. AI Technologies in Diagnostics
            3. Patient Care Enhancement
            4. Challenges and Ethics
            5. Future Outlook
            """,
            "topic": "AI in Healthcare",
            "audience": "general public",
            "tone": "informative and optimistic",
            "length": "800",
        }

        result = await enhanced_writer.arun(inputs)

        # Print hook execution log
        for _event in execution_log:
            pass

        return result, execution_log

    async def test_graded_reflection_pattern(self):
        """Test graded reflection with critic feedback."""
        # Create agents
        researcher = create_research_agent()
        writer = create_writer_agent()
        critic = create_reflection_critic()

        # Create workflow: Research → Write → Critique
        workflow = EnhancedMultiAgentV4(
            agents=[researcher, writer, critic], mode="sequential"
        )

        # Configure message passing
        initial_state = {
            "topic": "Quantum Computing Applications",
            "focus": "practical business applications",
            "depth": "intermediate",
            "audience": "business executives",
            "length": "1000",
            "tone": "professional",
            "system_message": "Focus on practical applications.",
            "article_content": "",  # Will be filled by writer
        }

        # Execute workflow
        result = await workflow.arun(initial_state)

        # Extract structured outputs

        # Check for research findings
        if "messages" in result:
            for msg in result["messages"]:
                if isinstance(msg, AIMessage) and hasattr(msg, "additional_kwargs"):
                    if "name" in msg.additional_kwargs:
                        msg.additional_kwargs["name"]

                        # Try to parse structured content
                        try:
                            import json

                            content = json.loads(msg.content)
                            for _key, _value in content.items():
                                pass
                        except:
                            pass

        return result

    async def test_pre_post_processing_pattern(self):
        """Test pre and post processing with custom transformations."""
        # Create main agent
        main_agent = SimpleAgentV3(
            name="main_processor",
            engine=AugLLMConfig(temperature=0.7),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "You are a content processor."),
                    ("human", "Process this content: {content}"),
                ]
            ),
        )

        # Create pre-processor
        pre_agent = SimpleAgentV3(
            name="pre_processor",
            engine=AugLLMConfig(temperature=0.5),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "You prepare content for processing."),
                    ("human", "Prepare this for processing: {content}"),
                ]
            ),
        )

        # Create post-processor
        post_agent = SimpleAgentV3(
            name="post_processor",
            engine=AugLLMConfig(temperature=0.6, structured_output_model=FinalArticle),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "You finalize and structure processed content."),
                    ("human", "Finalize this content: {content}"),
                ]
            ),
        )

        # Compose with pre/post processing
        main_agent.pre_agent = pre_agent
        main_agent.post_agent = post_agent
        main_agent.use_post_transform = True
        main_agent.post_transform_type = "reflection"

        # Add comprehensive hooks
        hook_func, _ = create_monitoring_hooks()
        for event in [
            HookEvent.PRE_PROCESS,
            HookEvent.POST_PROCESS,
            HookEvent.BEFORE_MESSAGE_TRANSFORM,
            HookEvent.AFTER_MESSAGE_TRANSFORM,
        ]:
            main_agent.add_hook(event, hook_func)

        # Execute with pre/post processing
        result = await main_agent.arun(
            {
                "content": "Raw content about artificial intelligence that needs processing, enhancement, and structuring."
            }
        )

        return result


# ============================================================================
# MAIN EXECUTION
# ============================================================================


async def main():
    """Run all advanced pattern tests."""
    test = TestAdvancedMultiAgentPatterns()

    # Test 1: Sequential with structured output
    await test.test_sequential_with_structured_output()

    # Test 2: Reflection with hooks
    result2, hook_log = await test.test_reflection_pattern_with_hooks()

    # Test 3: Graded reflection
    await test.test_graded_reflection_pattern()

    # Test 4: Pre/post processing
    await test.test_pre_post_processing_pattern()


if __name__ == "__main__":
    asyncio.run(main())
