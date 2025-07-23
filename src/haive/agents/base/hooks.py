# src/haive/agents/base/hooks.py

"""Hook system for agent lifecycle events.

This module provides a flexible hook system that allows users to inject
custom logic at various points in agent execution.

The hook system supports the following event types:
- Lifecycle: setup, graph building
- Execution: before/after run and arun
- Node execution: before/after individual nodes
- Error handling: errors and retries
- State management: state updates

Examples:
    Basic hook usage::

        from haive.agents.simple import SimpleAgent
        from haive.agents.base.hooks import HookEvent, logging_hook

        agent = SimpleAgent(name="my_agent")

        # Add logging hook
        agent.add_hook(HookEvent.BEFORE_RUN, logging_hook)

        # Add custom hook
        def my_hook(context):
            print(f"Starting {context.agent_name}")

        agent.add_hook(HookEvent.BEFORE_RUN, my_hook)

    Using decorators::

        agent = SimpleAgent(name="my_agent")

        @agent.before_run
        def log_start(context):
            print(f"Starting execution of {context.agent_name}")

        @agent.after_run
        def log_end(context):
            print(f"Completed: {context.output_data}")

    Error handling::

        @agent.on_error
        def handle_error(context):
            logger.error(f"Error in {context.agent_name}: {context.error}")
            # Could send alerts, retry, etc.

Note:
    Hooks are executed in the order they were added. Hook errors are caught
    and logged but don't interrupt agent execution. Use hooks for monitoring,
    logging, metrics, validation, and other cross-cutting concerns.
"""

import logging
from collections.abc import Callable
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class HookEvent(str, Enum):
    """Events where hooks can be attached."""

    # Lifecycle hooks
    BEFORE_SETUP = "before_setup"
    AFTER_SETUP = "after_setup"
    BEFORE_BUILD_GRAPH = "before_build_graph"
    AFTER_BUILD_GRAPH = "after_build_graph"

    # Execution hooks
    BEFORE_RUN = "before_run"
    AFTER_RUN = "after_run"
    BEFORE_ARUN = "before_arun"
    AFTER_ARUN = "after_arun"

    # Node execution hooks
    BEFORE_NODE = "before_node"
    AFTER_NODE = "after_node"

    # Error hooks
    ON_ERROR = "on_error"
    ON_RETRY = "on_retry"

    # State hooks
    BEFORE_STATE_UPDATE = "before_state_update"
    AFTER_STATE_UPDATE = "after_state_update"


class HookContext(BaseModel):
    """Context passed to hook functions."""

    model_config = {"arbitrary_types_allowed": True}

    event: HookEvent = Field(..., description="The hook event")
    agent_name: str = Field(..., description="Name of the agent")
    agent_type: str = Field(..., description="Type of the agent")

    # Optional fields depending on event
    input_data: Any | None = Field(default=None, description="Input data")
    output_data: Any | None = Field(default=None, description="Output data")
    error: Exception | None = Field(default=None, description="Error if any")
    node_name: str | None = Field(default=None, description="Current node name")
    state: dict[str, Any] | None = Field(default=None, description="Current state")
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )


# Hook function type
HookFunction = Callable[[HookContext], Any | None]


class HooksMixin:
    """Mixin that adds hook functionality to agents."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hooks: dict[HookEvent, list[HookFunction]] = {}

    def add_hook(self, event: HookEvent, hook: HookFunction) -> None:
        """Add a hook function for an event.

        Args:
            event: The event to hook into
            hook: The function to call on the event

        Example:
            agent.add_hook(HookEvent.BEFORE_RUN, lambda ctx: print(f"Running {ctx.agent_name}"))
        """
        if event not in self._hooks:
            self._hooks[event] = []
        self._hooks[event].append(hook)
        logger.debug(f"Added hook for {event} on {getattr(self, 'name', 'agent')}")

    def remove_hook(self, event: HookEvent, hook: HookFunction) -> None:
        """Remove a hook function.

        Args:
            event: The event to remove the hook from
            hook: The hook function to remove
        """
        if event in self._hooks and hook in self._hooks[event]:
            self._hooks[event].remove(hook)
            logger.debug(
                f"Removed hook for {event} on {getattr(self, 'name', 'agent')}"
            )

    def clear_hooks(self, event: HookEvent | None = None) -> None:
        """Clear hooks for an event or all events.

        Args:
            event: Specific event to clear hooks for, or None for all events
        """
        if event:
            self._hooks[event] = []
            logger.debug(
                f"Cleared hooks for {event} on {getattr(self, 'name', 'agent')}"
            )
        else:
            self._hooks.clear()
            logger.debug(f"Cleared all hooks on {getattr(self, 'name', 'agent')}")

    def _execute_hooks(self, event: HookEvent, **context_kwargs) -> list[Any]:
        """Execute all hooks for an event.

        Args:
            event: The event to execute hooks for
            **context_kwargs: Additional context to pass to hooks

        Returns:
            List of results from hook functions
        """
        if event not in self._hooks or not self._hooks[event]:
            return []

        # Create context
        context = HookContext(
            event=event,
            agent_name=getattr(self, "name", "unknown"),
            agent_type=self.__class__.__name__,
            **context_kwargs,
        )

        results = []
        for hook in self._hooks[event]:
            try:
                result = hook(context)
                if result is not None:
                    results.append(result)
            except Exception as e:
                logger.exception(f"Error in hook for {event}: {e}")
                # Don't let hook errors break execution
                continue

        return results

    # ========================================================================
    # HOOK DECORATORS
    # ========================================================================

    def before_setup(self, func: HookFunction) -> HookFunction:
        """Decorator to add a before_setup hook."""
        self.add_hook(HookEvent.BEFORE_SETUP, func)
        return func

    def after_setup(self, func: HookFunction) -> HookFunction:
        """Decorator to add an after_setup hook."""
        self.add_hook(HookEvent.AFTER_SETUP, func)
        return func

    def before_run(self, func: HookFunction) -> HookFunction:
        """Decorator to add a before_run hook."""
        self.add_hook(HookEvent.BEFORE_RUN, func)
        return func

    def after_run(self, func: HookFunction) -> HookFunction:
        """Decorator to add an after_run hook."""
        self.add_hook(HookEvent.AFTER_RUN, func)
        return func

    def on_error(self, func: HookFunction) -> HookFunction:
        """Decorator to add an on_error hook."""
        self.add_hook(HookEvent.ON_ERROR, func)
        return func


# ========================================================================
# COMMON HOOK FUNCTIONS
# ========================================================================


def logging_hook(context: HookContext) -> None:
    """Log hook events.

    A general-purpose logging hook that logs event details at appropriate levels.

    Args:
        context: Hook context with event details.

    Note:
        Uses INFO level for events, DEBUG for data, ERROR for errors.
    """
    logger.info(f"Hook {context.event} triggered for {context.agent_name}")
    if context.input_data:
        logger.debug(f"Input: {context.input_data}")
    if context.output_data:
        logger.debug(f"Output: {context.output_data}")
    if context.error:
        logger.error(f"Error: {context.error}")


def timing_hook(context: HookContext) -> None:
    """Track execution time.

    Measures and logs the execution time between BEFORE_RUN/ARUN and AFTER_RUN/ARUN events.

    Args:
        context: Hook context. Uses context.metadata to store start time.

    Note:
        Must be added to both BEFORE and AFTER events to work properly.

    Example:
        agent.add_hook(HookEvent.BEFORE_RUN, timing_hook)
        agent.add_hook(HookEvent.AFTER_RUN, timing_hook)
    """
    import time

    if context.event in (HookEvent.BEFORE_RUN, HookEvent.BEFORE_ARUN):
        context.metadata["start_time"] = time.time()
    elif context.event in (HookEvent.AFTER_RUN, HookEvent.AFTER_ARUN):
        if "start_time" in context.metadata:
            elapsed = time.time() - context.metadata["start_time"]
            logger.info(f"{context.agent_name} execution took {elapsed:.2f}s")


def state_validation_hook(context: HookContext) -> None:
    """Validate state updates."""
    if context.event == HookEvent.BEFORE_STATE_UPDATE and context.state:
        # Add validation logic here
        required_fields = ["messages"]
        for field in required_fields:
            if field not in context.state:
                logger.warning(f"Missing required field in state: {field}")


def retry_limit_hook(max_retries: int = 3) -> HookFunction:
    """Create a hook that limits retries.

    Factory function that creates a hook to limit retry attempts per agent/node.

    Args:
        max_retries: Maximum number of retries allowed per agent/node combination.

    Returns:
        A hook function that tracks and limits retries.

    Raises:
        Exception: When retry limit is exceeded.

    Example:
        agent.add_hook(HookEvent.ON_RETRY, retry_limit_hook(max_retries=5))
    """
    retry_count = {}

    def hook(context: HookContext) -> None:
        if context.event == HookEvent.ON_RETRY:
            key = f"{context.agent_name}:{context.node_name}"
            retry_count[key] = retry_count.get(key, 0) + 1
            if retry_count[key] > max_retries:
                raise Exception(f"Max retries ({max_retries}) exceeded for {key}")

    return hook
