agents.react_class.react.state
==============================

.. py:module:: agents.react_class.react.state


Classes
-------

.. autoapisummary::

   agents.react_class.react.state.ReactAgentState


Module Contents
---------------

.. py:class:: ReactAgentState

   Bases: :py:obj:`haive.agents.simple.state.SimpleAgentState`


   State for React Agent, extending SimpleAgentState.

   Adds fields for tool results, intermediate reasoning,
   and structured output.


   .. autolink-examples:: ReactAgentState
      :collapse:

   .. py:attribute:: active_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: intermediate_steps
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



   .. py:attribute:: selected_tools
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: structured_output
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: tool_results
      :type:  list[dict[str, Any]]
      :value: None



