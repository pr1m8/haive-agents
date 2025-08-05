# tests/base/test_hooks.py
"""Test the hook system for agent lifecycle events.

This module tests the comprehensive hook system that allows users to inject
custom logic at various points in agent execution.

Tests cover:
- Hook registration and removal
- Lifecycle hooks (setup, graph building)
- Execution hooks (before/after run)
- Error handling hooks
- Hook decorators
- Common hook functions (logging, timing, etc.)
"""

import logging
import time

import pytest

from haive.agents.base.hooks import (
    HookContext,
    HookEvent,
    logging_hook,
    retry_limit_hook,
    state_validation_hook,
    timing_hook,
)
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


logger = logging.getLogger(__name__)


class TestHooksMixin:
    """Test the HooksMixin functionality."""

    def test_add_and_execute_hook(self):
        """Test basic hook addition and execution."""
        # Create an agent with hooks
        agent = SimpleAgent(name="test_agent")

        # Track hook execution
        executed = []

        def test_hook(context: HookContext) -> None:
            executed.append(context.event)

        # Add hook
        agent.add_hook(HookEvent.BEFORE_RUN, test_hook)

        # Execute hooks
        agent._execute_hooks(HookEvent.BEFORE_RUN, input_data="test")

        assert HookEvent.BEFORE_RUN in executed

    def test_multiple_hooks_same_event(self):
        """Test multiple hooks on the same event."""
        agent = SimpleAgent(name="test_agent")

        results = []

        def hook1(context: HookContext) -> str:
            results.append("hook1")
            return "result1"

        def hook2(context: HookContext) -> str:
            results.append("hook2")
            return "result2"

        # Add multiple hooks
        agent.add_hook(HookEvent.BEFORE_RUN, hook1)
        agent.add_hook(HookEvent.BEFORE_RUN, hook2)

        # Execute hooks
        hook_results = agent._execute_hooks(HookEvent.BEFORE_RUN)

        assert results == ["hook1", "hook2"]
        assert hook_results == ["result1", "result2"]

    def test_remove_hook(self):
        """Test hook removal."""
        agent = SimpleAgent(name="test_agent")

        executed = []

        def test_hook(context: HookContext) -> None:
            executed.append("executed")

        # Add and remove hook
        agent.add_hook(HookEvent.BEFORE_RUN, test_hook)
        agent.remove_hook(HookEvent.BEFORE_RUN, test_hook)

        # Execute hooks
        agent._execute_hooks(HookEvent.BEFORE_RUN)

        assert not executed

    def test_clear_hooks(self):
        """Test clearing hooks."""
        agent = SimpleAgent(name="test_agent")

        def hook1(context: HookContext) -> None:
            pass

        def hook2(context: HookContext) -> None:
            pass

        # Add hooks to different events
        agent.add_hook(HookEvent.BEFORE_RUN, hook1)
        agent.add_hook(HookEvent.AFTER_RUN, hook2)

        # Clear specific event
        agent.clear_hooks(HookEvent.BEFORE_RUN)
        assert HookEvent.BEFORE_RUN not in agent._hooks or not agent._hooks[HookEvent.BEFORE_RUN]
        assert agent._hooks.get(HookEvent.AFTER_RUN)

        # Clear all
        agent.clear_hooks()
        assert not agent._hooks

    def test_hook_error_handling(self):
        """Test that hook errors don't break execution."""
        agent = SimpleAgent(name="test_agent")

        results = []

        def failing_hook(context: HookContext) -> None:
            results.append("before_error")
            raise Exception("Hook error")

        def working_hook(context: HookContext) -> None:
            results.append("after_error")

        # Add hooks
        agent.add_hook(HookEvent.BEFORE_RUN, failing_hook)
        agent.add_hook(HookEvent.BEFORE_RUN, working_hook)

        # Execute hooks - should not raise
        agent._execute_hooks(HookEvent.BEFORE_RUN)

        assert results == ["before_error", "after_error"]

    def test_hook_context(self):
        """Test hook context contains correct information."""
        agent = SimpleAgent(name="test_agent", temperature=0.7)

        captured_context = None

        def capture_context(context: HookContext) -> None:
            nonlocal captured_context
            captured_context = context

        agent.add_hook(HookEvent.BEFORE_RUN, capture_context)

        # Execute with various context data
        agent._execute_hooks(
            HookEvent.BEFORE_RUN, input_data="test input", metadata={"key": "value"}
        )

        assert captured_context is not None
        assert captured_context.event == HookEvent.BEFORE_RUN
        assert captured_context.agent_name == "test_agent"
        assert captured_context.agent_type == "SimpleAgent"
        assert captured_context.input_data == "test input"
        assert captured_context.metadata["key"] == "value"


class TestHookDecorators:
    """Test hook decorator methods."""

    def test_before_run_decorator(self):
        """Test @agent.before_run decorator."""
        agent = SimpleAgent(name="test_agent")

        executed = False

        @agent.before_run
        def my_hook(context: HookContext) -> None:
            nonlocal executed
            executed = True

        agent._execute_hooks(HookEvent.BEFORE_RUN)
        assert executed

    def test_after_run_decorator(self):
        """Test @agent.after_run decorator."""
        agent = SimpleAgent(name="test_agent")

        executed = False

        @agent.after_run
        def my_hook(context: HookContext) -> None:
            nonlocal executed
            executed = True

        agent._execute_hooks(HookEvent.AFTER_RUN)
        assert executed

    def test_on_error_decorator(self):
        """Test @agent.on_error decorator."""
        agent = SimpleAgent(name="test_agent")

        captured_error = None

        @agent.on_error
        def error_hook(context: HookContext) -> None:
            nonlocal captured_error
            captured_error = context.error

        test_error = Exception("Test error")
        agent._execute_hooks(HookEvent.ON_ERROR, error=test_error)
        assert captured_error == test_error


class TestCommonHooks:
    """Test the provided common hook functions."""

    def test_logging_hook(self, caplog):
        """Test the logging hook function."""
        agent = SimpleAgent(name="test_agent")

        with caplog.at_level(logging.INFO):
            agent.add_hook(HookEvent.BEFORE_RUN, logging_hook)
            agent._execute_hooks(
                HookEvent.BEFORE_RUN, input_data="test input", output_data="test output"
            )

        assert "Hook before_run triggered for test_agent" in caplog.text

    def test_timing_hook(self, caplog):
        """Test the timing hook function."""
        agent = SimpleAgent(name="test_agent")

        # Add timing hooks to both before and after
        agent.add_hook(HookEvent.BEFORE_RUN, timing_hook)
        agent.add_hook(HookEvent.AFTER_RUN, timing_hook)

        # Create shared metadata dict for timing
        metadata = {}

        with caplog.at_level(logging.INFO):
            # Execute before hook
            agent._execute_hooks(HookEvent.BEFORE_RUN, metadata=metadata)

            # Simulate some work
            time.sleep(0.1)

            # Execute after hook with same metadata
            agent._execute_hooks(HookEvent.AFTER_RUN, metadata=metadata)

        assert "test_agent execution took" in caplog.text

    def test_state_validation_hook(self, caplog):
        """Test the state validation hook."""
        agent = SimpleAgent(name="test_agent")

        agent.add_hook(HookEvent.BEFORE_STATE_UPDATE, state_validation_hook)

        # Test with missing required field
        with caplog.at_level(logging.WARNING):
            agent._execute_hooks(HookEvent.BEFORE_STATE_UPDATE, state={"other_field": "value"})

        assert "Missing required field in state: messages" in caplog.text

        # Test with valid state
        caplog.clear()
        agent._execute_hooks(
            HookEvent.BEFORE_STATE_UPDATE,
            state={"messages": [], "other_field": "value"},
        )

        assert "Missing required field" not in caplog.text

    def test_retry_limit_hook(self):
        """Test the retry limit hook factory."""
        agent = SimpleAgent(name="test_agent")

        # Create hook with max 2 retries
        retry_hook = retry_limit_hook(max_retries=2)
        agent.add_hook(HookEvent.ON_RETRY, retry_hook)

        # First two retries should work
        agent._execute_hooks(HookEvent.ON_RETRY, node_name="test_node")
        agent._execute_hooks(HookEvent.ON_RETRY, node_name="test_node")

        # Third retry should raise
        with pytest.raises(Exception, match="Max retries \\(2\\) exceeded"):
            agent._execute_hooks(HookEvent.ON_RETRY, node_name="test_node")


class TestHooksIntegration:
    """Test hooks integration with real agent execution."""

    @pytest.mark.asyncio
    async def test_hooks_with_agent_execution(self):
        """Test hooks during actual agent execution."""
        # Create agent with real LLM
        config = AugLLMConfig(temperature=0.1)
        agent = SimpleAgent(name="test_agent", engine=config)

        # Track hook execution order
        execution_order = []

        def track_hook(event_name: str):
            def hook(context: HookContext) -> None:
                execution_order.append(event_name)

            return hook

        # Add hooks for various events
        agent.add_hook(HookEvent.BEFORE_RUN, track_hook("before_run"))
        agent.add_hook(HookEvent.AFTER_RUN, track_hook("after_run"))

        # Run agent (this would trigger hooks in a real implementation)
        # Note: The base Agent class needs to call _execute_hooks in run/arun
        # This is a test to verify the hook system works

        # Simulate what the agent should do
        agent._execute_hooks(HookEvent.BEFORE_RUN, input_data="Hello")
        # ... agent execution ...
        agent._execute_hooks(HookEvent.AFTER_RUN, output_data="Response")

        assert execution_order == ["before_run", "after_run"]

    def test_hooks_with_multiple_agents(self):
        """Test that hooks are isolated between agents."""
        agent1 = SimpleAgent(name="agent1")
        agent2 = SimpleAgent(name="agent2")

        results1 = []
        results2 = []

        def hook1(context: HookContext) -> None:
            results1.append(context.agent_name)

        def hook2(context: HookContext) -> None:
            results2.append(context.agent_name)

        # Add different hooks to different agents
        agent1.add_hook(HookEvent.BEFORE_RUN, hook1)
        agent2.add_hook(HookEvent.BEFORE_RUN, hook2)

        # Execute hooks
        agent1._execute_hooks(HookEvent.BEFORE_RUN)
        agent2._execute_hooks(HookEvent.BEFORE_RUN)

        assert results1 == ["agent1"]
        assert results2 == ["agent2"]


class TestCustomHooks:
    """Test custom hook implementations."""

    def test_metrics_collection_hook(self):
        """Test a custom metrics collection hook."""
        metrics = {"execution_count": 0, "total_tokens": 0, "errors": 0}

        def metrics_hook(context: HookContext) -> None:
            if context.event == HookEvent.BEFORE_RUN:
                metrics["execution_count"] += 1
            elif context.event == HookEvent.AFTER_RUN:
                if context.metadata.get("token_count"):
                    metrics["total_tokens"] += context.metadata["token_count"]
            elif context.event == HookEvent.ON_ERROR:
                metrics["errors"] += 1

        agent = SimpleAgent(name="test_agent")
        agent.add_hook(HookEvent.BEFORE_RUN, metrics_hook)
        agent.add_hook(HookEvent.AFTER_RUN, metrics_hook)
        agent.add_hook(HookEvent.ON_ERROR, metrics_hook)

        # Simulate executions
        agent._execute_hooks(HookEvent.BEFORE_RUN)
        agent._execute_hooks(HookEvent.AFTER_RUN, metadata={"token_count": 100})
        agent._execute_hooks(HookEvent.BEFORE_RUN)
        agent._execute_hooks(HookEvent.AFTER_RUN, metadata={"token_count": 150})
        agent._execute_hooks(HookEvent.ON_ERROR, error=Exception("Test"))

        assert metrics["execution_count"] == 2
        assert metrics["total_tokens"] == 250
        assert metrics["errors"] == 1

    def test_conditional_hook(self):
        """Test a hook that only executes under certain conditions."""
        results = []

        def conditional_hook(context: HookContext) -> None:
            # Only log if input contains "important"
            if context.input_data and "important" in str(context.input_data):
                results.append(f"Important: {context.input_data}")

        agent = SimpleAgent(name="test_agent")
        agent.add_hook(HookEvent.BEFORE_RUN, conditional_hook)

        # Test with various inputs
        agent._execute_hooks(HookEvent.BEFORE_RUN, input_data="normal message")
        agent._execute_hooks(HookEvent.BEFORE_RUN, input_data="important message")
        agent._execute_hooks(HookEvent.BEFORE_RUN, input_data="another normal one")

        assert results == ["Important: important message"]
