agents.base.hooks
=================

.. py:module:: agents.base.hooks

.. autoapi-nested-parse::

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


Attributes
----------

.. autoapisummary::

   agents.base.hooks.HookFunction
   agents.base.hooks.logger


Classes
-------

.. autoapisummary::

   agents.base.hooks.HookContext
   agents.base.hooks.HookEvent
   agents.base.hooks.HooksMixin


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


Module Contents
---------------

.. py:class:: HookContext(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Context passed to hook functions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HookContext
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: error
      :type:  Exception | None
      :value: None



   .. py:attribute:: event
      :type:  HookEvent
      :value: None



   .. py:attribute:: grade_data
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: input_data
      :type:  Any | None
      :value: None



   .. py:attribute:: messages
      :type:  list[Any] | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: node_name
      :type:  str | None
      :value: None



   .. py:attribute:: original_messages
      :type:  list[Any] | None
      :value: None



   .. py:attribute:: output_data
      :type:  Any | None
      :value: None



   .. py:attribute:: post_agent_result
      :type:  Any | None
      :value: None



   .. py:attribute:: pre_agent_result
      :type:  Any | None
      :value: None



   .. py:attribute:: reflection_data
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: state
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: structured_data
      :type:  Any | None
      :value: None



   .. py:attribute:: transformation_type
      :type:  str | None
      :value: None



   .. py:attribute:: transformed_messages
      :type:  list[Any] | None
      :value: None



.. py:class:: HookEvent

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Events where hooks can be attached.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HookEvent
      :collapse:

   .. py:attribute:: AFTER_ARUN
      :value: 'after_arun'



   .. py:attribute:: AFTER_BUILD_GRAPH
      :value: 'after_build_graph'



   .. py:attribute:: AFTER_GRADING
      :value: 'after_grading'



   .. py:attribute:: AFTER_MESSAGE_TRANSFORM
      :value: 'after_message_transform'



   .. py:attribute:: AFTER_NODE
      :value: 'after_node'



   .. py:attribute:: AFTER_REFLECTION
      :value: 'after_reflection'



   .. py:attribute:: AFTER_RUN
      :value: 'after_run'



   .. py:attribute:: AFTER_SETUP
      :value: 'after_setup'



   .. py:attribute:: AFTER_STATE_UPDATE
      :value: 'after_state_update'



   .. py:attribute:: AFTER_STRUCTURED_OUTPUT
      :value: 'after_structured_output'



   .. py:attribute:: BEFORE_ARUN
      :value: 'before_arun'



   .. py:attribute:: BEFORE_BUILD_GRAPH
      :value: 'before_build_graph'



   .. py:attribute:: BEFORE_GRADING
      :value: 'before_grading'



   .. py:attribute:: BEFORE_MESSAGE_TRANSFORM
      :value: 'before_message_transform'



   .. py:attribute:: BEFORE_NODE
      :value: 'before_node'



   .. py:attribute:: BEFORE_REFLECTION
      :value: 'before_reflection'



   .. py:attribute:: BEFORE_RUN
      :value: 'before_run'



   .. py:attribute:: BEFORE_SETUP
      :value: 'before_setup'



   .. py:attribute:: BEFORE_STATE_UPDATE
      :value: 'before_state_update'



   .. py:attribute:: BEFORE_STRUCTURED_OUTPUT
      :value: 'before_structured_output'



   .. py:attribute:: ON_ERROR
      :value: 'on_error'



   .. py:attribute:: ON_RETRY
      :value: 'on_retry'



   .. py:attribute:: POST_PROCESS
      :value: 'post_process'



   .. py:attribute:: PRE_PROCESS
      :value: 'pre_process'



.. py:class:: HooksMixin(*args, **kwargs)

   Mixin that adds hook functionality to agents.


   .. autolink-examples:: HooksMixin
      :collapse:

   .. py:method:: _execute_hooks(event: HookEvent, **context_kwargs) -> list[Any]

      Execute all hooks for an event.

      :param event: The event to execute hooks for
      :param \*\*context_kwargs: Additional context to pass to hooks

      :returns: List of results from hook functions


      .. autolink-examples:: _execute_hooks
         :collapse:


   .. py:method:: add_hook(event: HookEvent, hook: HookFunction) -> None

      Add a hook function for an event.

      :param event: The event to hook into
      :param hook: The function to call on the event

      .. rubric:: Example

      agent.add_hook(HookEvent.BEFORE_RUN, lambda ctx: print(f"Running {ctx.agent_name}"))


      .. autolink-examples:: add_hook
         :collapse:


   .. py:method:: after_grading(func: HookFunction) -> HookFunction

      Decorator to add an after_grading hook.


      .. autolink-examples:: after_grading
         :collapse:


   .. py:method:: after_message_transform(func: HookFunction) -> HookFunction

      Decorator to add an after_message_transform hook.


      .. autolink-examples:: after_message_transform
         :collapse:


   .. py:method:: after_reflection(func: HookFunction) -> HookFunction

      Decorator to add an after_reflection hook.


      .. autolink-examples:: after_reflection
         :collapse:


   .. py:method:: after_run(func: HookFunction) -> HookFunction

      Decorator to add an after_run hook.


      .. autolink-examples:: after_run
         :collapse:


   .. py:method:: after_setup(func: HookFunction) -> HookFunction

      Decorator to add an after_setup hook.


      .. autolink-examples:: after_setup
         :collapse:


   .. py:method:: after_structured_output(func: HookFunction) -> HookFunction

      Decorator to add an after_structured_output hook.


      .. autolink-examples:: after_structured_output
         :collapse:


   .. py:method:: before_grading(func: HookFunction) -> HookFunction

      Decorator to add a before_grading hook.


      .. autolink-examples:: before_grading
         :collapse:


   .. py:method:: before_message_transform(func: HookFunction) -> HookFunction

      Decorator to add a before_message_transform hook.


      .. autolink-examples:: before_message_transform
         :collapse:


   .. py:method:: before_reflection(func: HookFunction) -> HookFunction

      Decorator to add a before_reflection hook.


      .. autolink-examples:: before_reflection
         :collapse:


   .. py:method:: before_run(func: HookFunction) -> HookFunction

      Decorator to add a before_run hook.


      .. autolink-examples:: before_run
         :collapse:


   .. py:method:: before_setup(func: HookFunction) -> HookFunction

      Decorator to add a before_setup hook.


      .. autolink-examples:: before_setup
         :collapse:


   .. py:method:: before_structured_output(func: HookFunction) -> HookFunction

      Decorator to add a before_structured_output hook.


      .. autolink-examples:: before_structured_output
         :collapse:


   .. py:method:: clear_hooks(event: HookEvent | None = None) -> None

      Clear hooks for an event or all events.

      :param event: Specific event to clear hooks for, or None for all events


      .. autolink-examples:: clear_hooks
         :collapse:


   .. py:method:: on_error(func: HookFunction) -> HookFunction

      Decorator to add an on_error hook.


      .. autolink-examples:: on_error
         :collapse:


   .. py:method:: post_process(func: HookFunction) -> HookFunction

      Decorator to add a post_process hook.


      .. autolink-examples:: post_process
         :collapse:


   .. py:method:: pre_process(func: HookFunction) -> HookFunction

      Decorator to add a pre_process hook.


      .. autolink-examples:: pre_process
         :collapse:


   .. py:method:: remove_hook(event: HookEvent, hook: HookFunction) -> None

      Remove a hook function.

      :param event: The event to remove the hook from
      :param hook: The hook function to remove


      .. autolink-examples:: remove_hook
         :collapse:


   .. py:attribute:: _hooks
      :type:  dict[HookEvent, list[HookFunction]]


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

.. py:data:: HookFunction

.. py:data:: logger

