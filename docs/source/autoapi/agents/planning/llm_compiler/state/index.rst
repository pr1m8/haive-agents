agents.planning.llm_compiler.state
==================================

.. py:module:: agents.planning.llm_compiler.state


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.state.CompilerState


Module Contents
---------------

.. py:class:: CompilerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State model for the LLM Compiler agent.

   Tracks:
   - The user's query
   - The current plan
   - Results from executed steps
   - Conversation history

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompilerState
      :collapse:

   .. py:method:: all_steps_complete() -> bool

      Check if all steps in the plan are complete.


      .. autolink-examples:: all_steps_complete
         :collapse:


   .. py:method:: get_executable_steps() -> list[agents.planning.llm_compiler.models.CompilerStep]

      Get steps that can be executed right now.


      .. autolink-examples:: get_executable_steps
         :collapse:


   .. py:method:: get_highest_step_id() -> int

      Get the highest step ID in the current plan.


      .. autolink-examples:: get_highest_step_id
         :collapse:


   .. py:method:: has_join_result() -> bool

      Check if the join step has been executed.


      .. autolink-examples:: has_join_result
         :collapse:


   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: plan
      :type:  agents.planning.llm_compiler.models.CompilerPlan | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: replan_count
      :type:  int
      :value: None



   .. py:attribute:: results
      :type:  dict[int, Any]
      :value: None



