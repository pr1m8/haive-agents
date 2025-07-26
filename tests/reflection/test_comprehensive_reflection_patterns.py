"""
Comprehensive Reflection Pattern Tests

This test demonstrates all reflection patterns available in haive-agents:
1. Simple reflection with message transformation
2. Graded reflection with structured feedback
3. Multi-stage reflection workflows
4. Custom hook integration
"""

import asyncio
from datetime import datetime
from typing import Any, Dict, List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.base.hooks import (
    HookContext,
    HookEvent,
    comprehensive_workflow_hook,
    create_multi_stage_hook,
    grading_hook,
    reflection_hook,
)
from haive.agents.base.pre_post_agent_mixin import (
    PrePostAgentMixin,
    create_graded_reflection_agent,
    create_reflection_agent,
    create_structured_output_agent,
)
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3

# ============================================================================
# STRUCTURED OUTPUT MODELS FOR REFLECTION
# ============================================================================


class ContentAnalysis(BaseModel):
    """Analysis of content quality."""

    strengths: List[str] = Field(description="Strong points in the content")
    weaknesses: List[str] = Field(description="Areas needing improvement")
    suggestions: List[str] = Field(description="Specific improvement suggestions")
    overall_quality: float = Field(ge=0.0, le=10.0, description="Overall quality score")


class ReflectionResult(BaseModel):
    """Result of reflection process."""

    original_summary: str = Field(description="Summary of original content")
    key_insights: List[str] = Field(description="Key insights from reflection")
    improvements_made: List[str] = Field(description="Specific improvements")
    revised_content: str = Field(description="Improved version of content")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in improvements")


class GradedOutput(BaseModel):
    """Graded output with detailed scores."""

    content_grade: float = Field(ge=0.0, le=100.0, description="Content quality grade")
    structure_grade: float = Field(ge=0.0, le=100.0, description="Structure grade")
    clarity_grade: float = Field(ge=0.0, le=100.0, description="Clarity grade")
    overall_grade: float = Field(ge=0.0, le=100.0, description="Overall grade")
    feedback: str = Field(description="Detailed feedback")
    pass_fail: bool = Field(description="Whether output passes quality threshold")


# ============================================================================
# CUSTOM HOOKS FOR REFLECTION MONITORING
# ============================================================================


class ReflectionMonitor:
    """Monitor reflection processes with detailed tracking."""

    def __init__(self):
        self.events: List[Dict[str, Any]] = []
        self.reflection_count = 0
        self.improvement_scores: List[float] = []
        self.start_time = None
        self.end_time = None

    def create_hook(self):
        """Create monitoring hook function."""

        def monitor_hook(context: HookContext):
            event_data = {
                "timestamp": datetime.now().isoformat(),
                "event": context.event.value,
                "agent": context.agent_name,
            }

            # Track reflection-specific events
            if context.event == HookEvent.BEFORE_REFLECTION:
                self.reflection_count += 1
                event_data["reflection_number"] = self.reflection_count
                if not self.start_time:
                    self.start_time = datetime.now()

            elif context.event == HookEvent.AFTER_REFLECTION:
                event_data["reflection_complete"] = True
                self.end_time = datetime.now()

                # Try to extract improvement score
                if hasattr(context, "result") and isinstance(context.result, dict):
                    if "confidence" in context.result:
                        self.improvement_scores.append(context.result["confidence"])

            elif context.event == HookEvent.AFTER_MESSAGE_TRANSFORM:
                event_data["transform_type"] = getattr(
                    context, "transform_type", "unknown"
                )
                event_data["message_count"] = len(getattr(context, "messages", []))

            self.events.append(event_data)

            # Print progress
            if context.event in [
                HookEvent.BEFORE_REFLECTION,
                HookEvent.AFTER_REFLECTION,
            ]:
                print(
                    f"🔄 Reflection Event: {context.event.value} - Agent: {context.agent_name}"
                )

        return monitor_hook

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of reflection monitoring."""
        duration = None
        if self.start_time and self.end_time:
            duration = (self.end_time - self.start_time).total_seconds()

        return {
            "total_events": len(self.events),
            "reflection_count": self.reflection_count,
            "average_improvement": (
                sum(self.improvement_scores) / len(self.improvement_scores)
                if self.improvement_scores
                else 0
            ),
            "duration_seconds": duration,
            "event_types": list(set(e["event"] for e in self.events)),
        }


# ============================================================================
# AGENT FACTORY FUNCTIONS
# ============================================================================


def create_content_writer() -> SimpleAgentV3:
    """Create a content writer agent."""
    config = AugLLMConfig(
        temperature=0.8,
        system_message="You are a creative content writer. Write engaging and informative content.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            ("human", "Write about: {topic}\n\nStyle: {style}\nLength: {length} words"),
        ]
    )

    return SimpleAgentV3(name="content_writer", engine=config, prompt_template=prompt)


def create_content_analyzer() -> SimpleAgentV3:
    """Create content analyzer with structured output."""
    config = AugLLMConfig(
        temperature=0.4,
        structured_output_model=ContentAnalysis,
        system_message="You are a critical content analyzer. Provide detailed analysis.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                "Analyze this content:\n\n{content}\n\nProvide detailed feedback.",
            ),
        ]
    )

    return SimpleAgentV3(name="content_analyzer", engine=config, prompt_template=prompt)


def create_reflection_improver() -> SimpleAgentV3:
    """Create reflection improver with structured output."""
    config = AugLLMConfig(
        temperature=0.6,
        structured_output_model=ReflectionResult,
        system_message="You are a thoughtful editor who improves content through reflection.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                """Original content:
{original_content}

Analysis feedback:
{analysis_feedback}

Please reflect on this feedback and create an improved version.""",
            ),
        ]
    )

    return SimpleAgentV3(
        name="reflection_improver", engine=config, prompt_template=prompt
    )


def create_grading_agent() -> SimpleAgentV3:
    """Create grading agent with structured scoring."""
    config = AugLLMConfig(
        temperature=0.3,
        structured_output_model=GradedOutput,
        system_message="You are a fair grader who evaluates content quality objectively.",
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                """Grade this content:
{content}

Grading criteria:
- Content quality and accuracy
- Structure and organization  
- Clarity and readability
- Overall effectiveness

Passing threshold: 70/100""",
            ),
        ]
    )

    return SimpleAgentV3(name="grader", engine=config, prompt_template=prompt)


# ============================================================================
# TEST CASES
# ============================================================================


class TestComprehensiveReflectionPatterns:

    async def test_simple_reflection_pattern(self):
        """Test basic reflection pattern with message transformation."""
        print("\n" + "=" * 60)
        print("Testing Simple Reflection Pattern")
        print("=" * 60)

        # Create base writer
        writer = create_content_writer()

        # Create reflection-enhanced writer using factory
        enhanced_writer = create_reflection_agent(
            main_agent=writer,
            reflection_config=AugLLMConfig(
                temperature=0.5,
                system_message="You are a thoughtful critic. Reflect on the content and suggest improvements.",
            ),
        )

        # Add reflection hook
        enhanced_writer.add_hook(HookEvent.BEFORE_REFLECTION, reflection_hook)
        enhanced_writer.add_hook(HookEvent.AFTER_REFLECTION, reflection_hook)

        # Execute with reflection
        result = await enhanced_writer.arun(
            {
                "topic": "The Impact of Remote Work on Productivity",
                "style": "analytical",
                "length": "500",
                "system_message": "Write thoughtfully about this topic.",
            }
        )

        print("\n📝 Reflection Complete")
        if isinstance(result, dict) and "messages" in result:
            print(f"Total messages: {len(result['messages'])}")

        return result

    async def test_multi_stage_reflection_workflow(self):
        """Test multi-stage reflection with analysis and improvement."""
        print("\n" + "=" * 60)
        print("Testing Multi-Stage Reflection Workflow")
        print("=" * 60)

        # Create monitoring
        monitor = ReflectionMonitor()

        # Create agents
        writer = create_content_writer()
        analyzer = create_content_analyzer()
        improver = create_reflection_improver()

        # Add monitoring hooks
        for agent in [writer, analyzer, improver]:
            agent.add_hook(HookEvent.BEFORE_RUN, monitor.create_hook())
            agent.add_hook(HookEvent.AFTER_RUN, monitor.create_hook())

        # Stage 1: Initial writing
        print("\n📝 Stage 1: Initial Writing")
        content = await writer.arun(
            {
                "topic": "Artificial Intelligence in Education",
                "style": "informative",
                "length": "300",
                "system_message": "Write clearly about AI in education.",
            }
        )

        # Stage 2: Analysis
        print("\n🔍 Stage 2: Content Analysis")
        analysis = await analyzer.arun(
            {
                "content": (
                    content.get("messages", [AIMessage(content="")])[-1].content
                    if isinstance(content, dict)
                    else str(content)
                ),
                "system_message": "Analyze critically but constructively.",
            }
        )

        # Stage 3: Reflection and improvement
        print("\n✨ Stage 3: Reflection and Improvement")

        # Set up improver with reflection hooks
        improver.add_hook(HookEvent.BEFORE_REFLECTION, monitor.create_hook())
        improver.add_hook(HookEvent.AFTER_REFLECTION, monitor.create_hook())

        improvement = await improver.arun(
            {
                "original_content": (
                    content.get("messages", [AIMessage(content="")])[-1].content
                    if isinstance(content, dict)
                    else str(content)
                ),
                "analysis_feedback": str(analysis),
                "system_message": "Improve based on feedback.",
            }
        )

        # Print monitoring summary
        summary = monitor.get_summary()
        print("\n📊 Reflection Monitoring Summary:")
        for key, value in summary.items():
            print(f"  - {key}: {value}")

        return {
            "original": content,
            "analysis": analysis,
            "improved": improvement,
            "monitoring": summary,
        }

    async def test_graded_reflection_pattern(self):
        """Test graded reflection with pass/fail criteria."""
        print("\n" + "=" * 60)
        print("Testing Graded Reflection Pattern")
        print("=" * 60)

        # Create writer
        writer = create_content_writer()

        # Create graded reflection writer using factory
        graded_writer = create_graded_reflection_agent(
            main_agent=writer,
            grading_config=AugLLMConfig(
                temperature=0.3,
                structured_output_model=GradedOutput,
                system_message="Grade content objectively using the criteria provided.",
            ),
            reflection_config=AugLLMConfig(
                temperature=0.6,
                system_message="Improve content based on grading feedback.",
            ),
        )

        # Add comprehensive workflow hook
        graded_writer.add_hook(HookEvent.BEFORE_RUN, comprehensive_workflow_hook)
        graded_writer.add_hook(HookEvent.AFTER_RUN, comprehensive_workflow_hook)
        graded_writer.add_hook(HookEvent.BEFORE_GRADING, grading_hook)
        graded_writer.add_hook(HookEvent.AFTER_GRADING, grading_hook)

        # Execute with grading
        result = await graded_writer.arun(
            {
                "topic": "Cybersecurity Best Practices for Small Businesses",
                "style": "practical guide",
                "length": "400",
                "system_message": "Write a comprehensive guide.",
                "content": "",  # Will be filled by grading
            }
        )

        print("\n✅ Graded Reflection Complete")
        return result

    async def test_custom_reflection_with_hooks(self):
        """Test custom reflection implementation with all hooks."""
        print("\n" + "=" * 60)
        print("Testing Custom Reflection with All Hooks")
        print("=" * 60)

        # Create agents
        writer = create_content_writer()
        grader = create_grading_agent()

        # Manually implement pre/post pattern
        class CustomReflectionAgent(PrePostAgentMixin, SimpleAgentV3):
            """Custom agent with reflection capabilities."""

            pass

        # Create custom reflection agent
        custom_agent = CustomReflectionAgent(
            name="custom_reflector",
            engine=AugLLMConfig(temperature=0.7),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "You are a writer who reflects and improves."),
                    ("human", "Topic: {topic}"),
                ]
            ),
        )

        # Configure pre/post agents
        custom_agent.post_agent = grader
        custom_agent.use_post_transform = True
        custom_agent.post_transform_type = "reflection"

        # Create multi-stage hook
        stages = ["writing", "grading", "reflection", "finalization"]
        multi_hook = create_multi_stage_hook(stages)

        # Add all hook types
        hook_events = [
            HookEvent.BEFORE_SETUP,
            HookEvent.AFTER_SETUP,
            HookEvent.BEFORE_RUN,
            HookEvent.AFTER_RUN,
            HookEvent.PRE_PROCESS,
            HookEvent.POST_PROCESS,
            HookEvent.BEFORE_MESSAGE_TRANSFORM,
            HookEvent.AFTER_MESSAGE_TRANSFORM,
        ]

        for event in hook_events:
            custom_agent.add_hook(event, multi_hook)

        # Execute
        result = await custom_agent.arun(
            {"topic": "The Future of Sustainable Energy", "content": ""}  # For grader
        )

        print("\n🎯 Custom Reflection Complete")
        return result

    async def test_iterative_reflection(self):
        """Test iterative reflection until quality threshold is met."""
        print("\n" + "=" * 60)
        print("Testing Iterative Reflection Pattern")
        print("=" * 60)

        # Create agents
        writer = create_content_writer()
        grader = create_grading_agent()
        improver = create_reflection_improver()

        # Initial content
        content = await writer.arun(
            {
                "topic": "Blockchain Technology Explained",
                "style": "beginner-friendly",
                "length": "400",
                "system_message": "Explain blockchain simply.",
            }
        )

        # Extract content
        current_content = (
            content.get("messages", [AIMessage(content="")])[-1].content
            if isinstance(content, dict)
            else str(content)
        )

        # Iterative improvement loop
        max_iterations = 3
        quality_threshold = 75.0

        for i in range(max_iterations):
            print(f"\n🔄 Iteration {i+1}")

            # Grade current content
            grade_result = await grader.arun(
                {
                    "content": current_content,
                    "system_message": "Grade fairly and provide feedback.",
                }
            )

            # Parse grade (assuming structured output)
            if isinstance(grade_result, dict):
                # Extract grade from structured output
                grade_data = grade_result
                if "overall_grade" in grade_data:
                    current_grade = grade_data["overall_grade"]
                else:
                    current_grade = 0.0
            else:
                current_grade = 0.0

            print(f"  Current grade: {current_grade}/100")

            # Check if threshold met
            if current_grade >= quality_threshold:
                print(f"  ✅ Quality threshold met!")
                break

            # Improve content
            improvement = await improver.arun(
                {
                    "original_content": current_content,
                    "analysis_feedback": str(grade_result),
                    "system_message": "Improve based on grading feedback.",
                }
            )

            # Update current content
            if isinstance(improvement, dict) and "revised_content" in improvement:
                current_content = improvement["revised_content"]
            else:
                # Extract from messages if needed
                msgs = (
                    improvement.get("messages", [])
                    if isinstance(improvement, dict)
                    else []
                )
                if msgs:
                    current_content = msgs[-1].content

        print("\n✨ Iterative Reflection Complete")
        return {
            "final_content": current_content,
            "iterations": i + 1,
            "final_grade": current_grade,
        }


# ============================================================================
# MAIN EXECUTION
# ============================================================================


async def main():
    """Run all reflection pattern tests."""
    test = TestComprehensiveReflectionPatterns()

    # Test 1: Simple reflection
    print("\n🧪 Running Test 1: Simple Reflection")
    result1 = await test.test_simple_reflection_pattern()

    # Test 2: Multi-stage workflow
    print("\n🧪 Running Test 2: Multi-Stage Reflection")
    result2 = await test.test_multi_stage_reflection_workflow()

    # Test 3: Graded reflection
    print("\n🧪 Running Test 3: Graded Reflection")
    result3 = await test.test_graded_reflection_pattern()

    # Test 4: Custom reflection with hooks
    print("\n🧪 Running Test 4: Custom Reflection")
    result4 = await test.test_custom_reflection_with_hooks()

    # Test 5: Iterative reflection
    print("\n🧪 Running Test 5: Iterative Reflection")
    result5 = await test.test_iterative_reflection()

    print("\n" + "=" * 60)
    print("All Reflection Pattern Tests Complete!")
    print("=" * 60)

    # Summary
    print("\n📊 Test Summary:")
    print("  1. Simple Reflection: ✅")
    print("  2. Multi-Stage Workflow: ✅")
    print("  3. Graded Reflection: ✅")
    print("  4. Custom with Hooks: ✅")
    print("  5. Iterative Reflection: ✅")


if __name__ == "__main__":
    asyncio.run(main())
