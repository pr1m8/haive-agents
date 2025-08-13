
:py:mod:`agents.base.hooks`
===========================

.. py:module:: agents.base.hooks

Hook system for agent lifecycle events.

This module provides a flexible hook system that allows users to inject
custom logic at various points in agent execution.

The hook system supports the following event types:
- Lifecycle: setup, graph building
- Execution: before/after run and arun
- Node execution: before/after individual nodes
- Error handling: errors and retries
- State management: state updates

.. rubric:: Examples

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

.. note::

   Hooks are executed in the order they were added. Hook errors are caught
   and logged but don't interrupt agent execution. Use hooks for monitoring,
   logging, metrics, validation, and other cross-cutting concerns.


.. autolink-examples:: agents.base.hooks
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.hooks.HookContext
   agents.base.hooks.HookEvent
   agents.base.hooks.HooksMixin


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HookContext:

   .. graphviz::
      :align: center

      digraph inheritance_HookContext {
        node [shape=record];
        "HookContext" [label="HookContext"];
        "pydantic.BaseModel" -> "HookContext";
      }

.. autopydantic_model:: agents.base.hooks.HookContext
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HookEvent:

   .. graphviz::
      :align: center

      digraph inheritance_HookEvent {
        node [shape=record];
        "HookEvent" [label="HookEvent"];
        "str" -> "HookEvent";
        "enum.Enum" -> "HookEvent";
      }

.. autoclass:: agents.base.hooks.HookEvent
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HookEvent** is an Enum defined in ``agents.base.hooks``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HooksMixin:

   .. graphviz::
      :align: center

      digraph inheritance_HooksMixin {
        node [shape=record];
        "HooksMixin" [label="HooksMixin"];
      }

.. autoclass:: agents.base.hooks.HooksMixin
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.base.hooks.comprehensive_workflow_hook
   agents.base.hooks.create_multi_stage_hook
   agents.base.hooks.grading_hook
   agents.base.hooks.logging_hook
   agents.base.hooks.message_transformation_hook
   agents.base.hooks.pre_post_processing_hook
   agents.base.hooks.reflection_hook
   agents.base.hooks.retry_limit_hook
   agents.base.hooks.state_validation_hook
   agents.base.hooks.structured_output_hook
   agents.base.hooks.timing_hook

.. py:function:: comprehensive_workflow_hook(context: HookContext) -> None

   Comprehensive hook that logs all workflow events.

   A single hook that can handle all types of workflow events for complete
   monitoring and debugging of agent execution.

   :param context: Hook context with event details.


   .. autolink-examples:: comprehensive_workflow_hook
      :collapse:

.. py:function:: create_multi_stage_hook(stages: list[str]) -> HookFunction

   Create a hook that tracks multi-stage agent workflows.

   Factory function for creating hooks that monitor complex workflows
   like reflection, grading, and structured output processing.

   :param stages: List of stage names to track (e.g., ["grading", "reflection", "improvement"])

   :returns: A hook function that tracks multi-stage workflows.

   .. rubric:: Example

   hook = create_multi_stage_hook(["grading", "reflection", "improvement"])
   agent.add_hook(HookEvent.PRE_PROCESS, hook)
   agent.add_hook(HookEvent.POST_PROCESS, hook)


   .. autolink-examples:: create_multi_stage_hook
      :collapse:

.. py:function:: grading_hook(context: HookContext) -> None

   Log grading events and track quality metrics.

   Monitors grading processes and logs quality assessment results.

   :param context: Hook context with grading details.


   .. autolink-examples:: grading_hook
      :collapse:

.. py:function:: logging_hook(context: HookContext) -> None

   Log hook events.

   A general-purpose logging hook that logs event details at appropriate levels.

   :param context: Hook context with event details.

   .. note:: Uses INFO level for events, DEBUG for data, ERROR for errors.


   .. autolink-examples:: logging_hook
      :collapse:

.. py:function:: message_transformation_hook(context: HookContext) -> None

   Log message transformation events.

   Logs details about message transformations including the transformation type
   and number of messages processed.

   :param context: Hook context with transformation details.


   .. autolink-examples:: message_transformation_hook
      :collapse:

.. py:function:: pre_post_processing_hook(context: HookContext) -> None

   Log pre/post processing events.

   Monitors pre and post processing stages in multi-agent workflows.

   :param context: Hook context with processing details.


   .. autolink-examples:: pre_post_processing_hook
      :collapse:

.. py:function:: reflection_hook(context: HookContext) -> None

   Log reflection events and provide insights.

   Tracks reflection processing including grading and improvement suggestions.

   :param context: Hook context with reflection details.


   .. autolink-examples:: reflection_hook
      :collapse:

.. py:function:: retry_limit_hook(max_retries: int = 3) -> HookFunction

   Create a hook that limits retries.

   Factory function that creates a hook to limit retry attempts per agent/node.

   :param max_retries: Maximum number of retries allowed per agent/node combination.

   :returns: A hook function that tracks and limits retries.

   :raises Exception: When retry limit is exceeded.

   .. rubric:: Example

   agent.add_hook(HookEvent.ON_RETRY, retry_limit_hook(max_retries=5))


   .. autolink-examples:: retry_limit_hook
      :collapse:

.. py:function:: state_validation_hook(context: HookContext) -> None

   Validate state updates.


   .. autolink-examples:: state_validation_hook
      :collapse:

.. py:function:: structured_output_hook(context: HookContext) -> None

   Log structured output processing events.

   Tracks structural output parsing and validation.

   :param context: Hook context with structured output details.


   .. autolink-examples:: structured_output_hook
      :collapse:

.. py:function:: timing_hook(context: HookContext) -> None

   Track execution time.

   Measures and logs the execution time between BEFORE_RUN/ARUN and AFTER_RUN/ARUN events.

   :param context: Hook context. Uses context.metadata to store start time.

   .. note:: Must be added to both BEFORE and AFTER events to work properly.

   .. rubric:: Example

   agent.add_hook(HookEvent.BEFORE_RUN, timing_hook)
   agent.add_hook(HookEvent.AFTER_RUN, timing_hook)


   .. autolink-examples:: timing_hook
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.base.hooks
   :collapse:
   
.. autolink-skip:: next
