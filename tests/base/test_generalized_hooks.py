"""Test the generalized hook system in the enhanced base agent."""

from unittest.mock import AsyncMock

import pytest

from haive.agents.base.hooks import (
    HookContext,
    HookEvent,
    comprehensive_workflow_hook,
    create_multi_stage_hook,
    message_transformation_hook,
    reflection_hook,
)
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class TestGeneralizedHooks:
    """Test the generalized hook system."""

    def test_hook_event_coverage(self):
        """Test that all expected hook events are available."""
        # Core lifecycle events
        assert HookEvent.BEFORE_SETUP == "before_setup"
        assert HookEvent.AFTER_SETUP == "after_setup"

        # Execution events
        assert HookEvent.BEFORE_RUN == "before_run"
        assert HookEvent.AFTER_RUN == "after_run"

        # New enhanced events
        assert HookEvent.PRE_PROCESS == "pre_process"
        assert HookEvent.POST_PROCESS == "post_process"
        assert HookEvent.BEFORE_MESSAGE_TRANSFORM == "before_message_transform"
        assert HookEvent.AFTER_MESSAGE_TRANSFORM == "after_message_transform"
        assert HookEvent.BEFORE_REFLECTION == "before_reflection"
        assert HookEvent.AFTER_REFLECTION == "after_reflection"
        assert HookEvent.BEFORE_GRADING == "before_grading"
        assert HookEvent.AFTER_GRADING == "after_grading"
        assert HookEvent.BEFORE_STRUCTURED_OUTPUT == "before_structured_output"
        assert HookEvent.AFTER_STRUCTURED_OUTPUT == "after_structured_output"

    def test_hook_context_enhanced_fields(self):
        """Test that HookContext has all enhanced fields."""
        context = HookContext(
            event=HookEvent.BEFORE_REFLECTION,
            agent_name="test_agent",
            agent_type="SimpleAgent",
            messages=[],
            transformed_messages=[],
            structured_data={"test": "data"},
            grade_data={"score": 85},
            reflection_data={"improvement": "suggestion"},
            transformation_type="reflection",
        )

        assert context.event == HookEvent.BEFORE_REFLECTION
        assert context.agent_name == "test_agent"
        assert context.messages == []
        assert context.transformed_messages == []
        assert context.structured_data == {"test": "data"}
        assert context.grade_data == {"score": 85}
        assert context.reflection_data == {"improvement": "suggestion"}
        assert context.transformation_type == "reflection"

    def test_agent_has_enhanced_hook_decorators(self):
        """Test that enhanced agents have all hook decorators."""
        agent = SimpleAgent(name="test_agent", engine=AugLLMConfig(temperature=0.1))

        # Test that all new decorators are available
        assert hasattr(agent, "pre_process")
        assert hasattr(agent, "post_process")
        assert hasattr(agent, "before_message_transform")
        assert hasattr(agent, "after_message_transform")
        assert hasattr(agent, "before_reflection")
        assert hasattr(agent, "after_reflection")
        assert hasattr(agent, "before_grading")
        assert hasattr(agent, "after_grading")
        assert hasattr(agent, "before_structured_output")
        assert hasattr(agent, "after_structured_output")

    def test_hook_decorator_functionality(self):
        """Test that hook decorators work correctly."""
        agent = SimpleAgent(name="test_agent", engine=AugLLMConfig(temperature=0.1))

        # Track hook calls
        hook_calls = []

        @agent.before_reflection
        def test_reflection_hook(context: HookContext):
            hook_calls.append(f"before_reflection:{context.agent_name}")

        @agent.after_grading
        def test_grading_hook(context: HookContext):
            hook_calls.append(f"after_grading:{context.agent_name}")

        # Execute hooks manually
        agent.execute_hooks(HookEvent.BEFORE_REFLECTION)
        agent.execute_hooks(HookEvent.AFTER_GRADING)

        assert "before_reflection:test_agent" in hook_calls
        assert "after_grading:test_agent" in hook_calls

    def test_comprehensive_workflow_hook(self):
        """Test the comprehensive workflow hook."""
        context = HookContext(
            event=HookEvent.BEFORE_RUN,
            agent_name="test_agent",
            agent_type="SimpleAgent",
            input_data="test input",
        )

        # Should not raise any exceptions
        comprehensive_workflow_hook(context)

        # Test with message transformation
        context = HookContext(
            event=HookEvent.BEFORE_MESSAGE_TRANSFORM,
            agent_name="test_agent",
            agent_type="SimpleAgent",
            messages=["message1", "message2"],
            transformation_type="reflection",
        )

        message_transformation_hook(context)

    def test_multi_stage_hook_factory(self):
        """Test the multi-stage hook factory."""
        stages = ["grading", "reflection", "improvement"]
        hook = create_multi_stage_hook(stages)

        # Test pre-process stage
        pre_context = HookContext(
            event=HookEvent.PRE_PROCESS,
            agent_name="multi_stage_agent",
            agent_type="TestAgent",
        )

        hook(pre_context)

        # Test individual stage completion
        grade_context = HookContext(
            event=HookEvent.AFTER_GRADING,
            agent_name="multi_stage_agent",
            agent_type="TestAgent",
        )

        hook(grade_context)

        # Test post-process stage
        post_context = HookContext(
            event=HookEvent.POST_PROCESS,
            agent_name="multi_stage_agent",
            agent_type="TestAgent",
        )

        hook(post_context)

    def test_reflection_hook_patterns(self):
        """Test reflection-specific hook patterns."""
        # Test before reflection
        before_context = HookContext(
            event=HookEvent.BEFORE_REFLECTION,
            agent_name="reflection_agent",
            agent_type="ReflectionAgent",
            grade_data={"score": 75, "feedback": "Good but could improve"},
        )

        reflection_hook(before_context)

        # Test after reflection
        after_context = HookContext(
            event=HookEvent.AFTER_REFLECTION,
            agent_name="reflection_agent",
            agent_type="ReflectionAgent",
            reflection_data={"improvements": ["Add more examples", "Clarify conclusion"]},
        )

        reflection_hook(after_context)

    def test_agent_pre_post_mixin_integration(self):
        """Test that agents have pre/post processing capabilities."""
        agent = SimpleAgent(name="test_agent", engine=AugLLMConfig(temperature=0.1))

        # Test that pre/post processing fields are available
        assert hasattr(agent, "pre_agent")
        assert hasattr(agent, "post_agent")
        assert hasattr(agent, "use_pre_transform")
        assert hasattr(agent, "use_post_transform")
        assert hasattr(agent, "pre_transform_type")
        assert hasattr(agent, "post_transform_type")

        # Test default values
        assert agent.pre_agent is None
        assert agent.post_agent is None
        assert agent.use_pre_transform is False
        assert agent.use_post_transform is False
        assert agent.pre_transform_type == "ai_to_human"
        assert agent.post_transform_type == "reflection"

    @pytest.mark.asyncio
    async def test_hook_execution_during_arun(self):
        """Test that hooks are executed during agent runs."""
        agent = SimpleAgent(
            name="hook_test_agent",
            engine=AugLLMConfig(system_message="You are a test agent.", temperature=0.1),
        )

        # Track hook executions
        hook_executions = []

        @agent.before_arun
        def track_before_arun(context: HookContext):
            hook_executions.append("before_arun")

        @agent.after_arun
        def track_after_arun(context: HookContext):
            hook_executions.append("after_arun")

        # Mock the underlying arun to avoid actual LLM calls
        original_arun = agent.arun
        agent.arun = AsyncMock(return_value={"messages": [{"content": "test response"}]})

        try:
            # Run the agent
            await agent.arun("test input")

            # Verify hooks were executed
            assert "before_arun" in hook_executions
            assert "after_arun" in hook_executions

        finally:
            # Restore original method
            agent.arun = original_arun

    def test_specialized_hook_functions(self):
        """Test that specialized hook functions work correctly."""
        from haive.agents.base.hooks import (
            grading_hook,
            pre_post_processing_hook,
            structured_output_hook,
        )

        # Test grading hook
        grading_context = HookContext(
            event=HookEvent.AFTER_GRADING,
            agent_name="grader",
            agent_type="GradingAgent",
            grade_data={"score": 88, "letter_grade": "B+"},
        )

        grading_hook(grading_context)

        # Test structured output hook
        structured_context = HookContext(
            event=HookEvent.AFTER_STRUCTURED_OUTPUT,
            agent_name="structurer",
            agent_type="StructuredOutputAgent",
            structured_data={"result": "structured", "confidence": 0.95},
        )

        structured_output_hook(structured_context)

        # Test pre/post processing hook
        pre_context = HookContext(
            event=HookEvent.PRE_PROCESS,
            agent_name="processor",
            agent_type="ProcessingAgent",
            input_data="raw input",
        )

        pre_post_processing_hook(pre_context)

    def test_hook_error_handling(self):
        """Test that hook errors don't break agent execution."""
        agent = SimpleAgent(name="error_test_agent", engine=AugLLMConfig(temperature=0.1))

        # Add a hook that raises an exception
        @agent.before_run
        def problematic_hook(context: HookContext):
            raise ValueError("Test hook error")

        # Add a normal hook
        @agent.before_run
        def normal_hook(context: HookContext):
            return "normal_hook_executed"

        # Execute hooks - should not raise exception
        results = agent.execute_hooks(HookEvent.BEFORE_RUN)

        # Normal hook should still execute
        assert "normal_hook_executed" in results
