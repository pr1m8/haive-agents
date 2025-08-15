agents.reasoning_and_critique.reflection.state
==============================================

.. py:module:: agents.reasoning_and_critique.reflection.state

.. autoapi-nested-parse::

   State schema for the Reflection Agent.


   .. autolink-examples:: agents.reasoning_and_critique.reflection.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflection.state.ReflectionAgentState


Module Contents
---------------

.. py:class:: ReflectionAgentState

   Bases: :py:obj:`haive.agents.simple.state.SimpleAgentState`


   State schema for the Reflection agent.


   .. autolink-examples:: ReflectionAgentState
      :collapse:

   .. py:method:: add_reflection(reflection: haive.agents.reflection.models.ReflectionResult) -> None

      Add a reflection result to the history.


      .. autolink-examples:: add_reflection
         :collapse:


   .. py:attribute:: feedback
      :type:  str | None
      :value: None



   .. py:attribute:: improved_response
      :type:  str | None
      :value: None



   .. py:property:: last_ai_message
      :type: str | None


      Extract the last AI message content.

      .. autolink-examples:: last_ai_message
         :collapse:


   .. py:property:: last_human_message
      :type: str | None


      Extract the last human message content.

      .. autolink-examples:: last_human_message
         :collapse:


   .. py:attribute:: original_request
      :type:  str | None
      :value: None



   .. py:attribute:: reflection_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: reflection_round
      :type:  int
      :value: None



   .. py:attribute:: reflection_score
      :type:  float | None
      :value: None



   .. py:attribute:: response
      :type:  str | None
      :value: None



   .. py:attribute:: search_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: search_results
      :type:  list[dict[str, Any]]
      :value: None



