agents.reasoning_and_critique.self_discover.state
=================================================

.. py:module:: agents.reasoning_and_critique.self_discover.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.state.SelfDiscoverState


Module Contents
---------------

.. py:class:: SelfDiscoverState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State schema for the SelfDiscover agent.

   This schema tracks all information needed for the SelfDiscover process:
   - messages: Conversation history
   - reasoning_modules: Available reasoning modules
   - task_description: The problem to solve
   - selected_modules: Modules chosen for this task
   - adapted_modules: Customized modules for this task
   - reasoning_structure: JSON plan for solving the task
   - answer: Final solution

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelfDiscoverState
      :collapse:

   .. py:attribute:: adapted_modules
      :type:  str | None
      :value: None



   .. py:attribute:: answer
      :type:  str | None
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: reasoning_modules
      :type:  str
      :value: None



   .. py:attribute:: reasoning_structure
      :type:  str | None
      :value: None



   .. py:attribute:: selected_modules
      :type:  str | None
      :value: None



   .. py:attribute:: task_description
      :type:  str
      :value: None



