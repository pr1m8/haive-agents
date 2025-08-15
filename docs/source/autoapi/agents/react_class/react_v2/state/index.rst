agents.react_class.react_v2.state
=================================

.. py:module:: agents.react_class.react_v2.state


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.state.ReactAgentState


Module Contents
---------------

.. py:class:: ReactAgentState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State schema for React agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactAgentState
      :collapse:

   .. py:attribute:: human_request
      :type:  str | None
      :value: None



   .. py:attribute:: intermediate_steps
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: iteration
      :type:  int
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



   .. py:attribute:: requires_human_input
      :type:  bool
      :value: None



   .. py:attribute:: structured_output
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: tool_results
      :type:  list[dict[str, Any]]
      :value: None



