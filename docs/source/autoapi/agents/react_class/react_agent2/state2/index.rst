agents.react_class.react_agent2.state2
======================================

.. py:module:: agents.react_class.react_agent2.state2


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.state2.ReactAgentState


Module Contents
---------------

.. py:class:: ReactAgentState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for React agents with tool usage.

   This state schema handles proper message normalization
   and tracking for ReAct agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactAgentState
      :collapse:

   .. py:method:: get(key: str, default: Any = None) -> Any

      Get a field value, similar to dict.get().


      .. autolink-examples:: get
         :collapse:


   .. py:method:: has_tool_calls() -> bool

      Check if the last message has tool calls.


      .. autolink-examples:: has_tool_calls
         :collapse:


   .. py:method:: increment_step() -> None

      Increment the current step counter.


      .. autolink-examples:: increment_step
         :collapse:


   .. py:method:: should_continue() -> bool

      Determine if agent iteration should continue.


      .. autolink-examples:: should_continue
         :collapse:


   .. py:method:: update_tool_usage_stats(tool_name: str) -> None

      Update tool usage statistics.


      .. autolink-examples:: update_tool_usage_stats
         :collapse:


   .. py:method:: with_structured_output(output_model_type: type) -> type
      :classmethod:


      Create a specialized state with a typed structured_output field.

      :param output_model_type: Type for structured output

      :returns: A new state class with the specified structured output type


      .. autolink-examples:: with_structured_output
         :collapse:


   .. py:attribute:: current_step
      :type:  int
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: is_last_step
      :type:  bool
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: memory
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: messages
      :type:  collections.abc.Sequence[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: remaining_steps
      :type:  int
      :value: None



   .. py:attribute:: structured_output
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: thought
      :type:  str | None
      :value: None



   .. py:attribute:: tool_results
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: tool_usage_stats
      :type:  dict[str, int]
      :value: None



