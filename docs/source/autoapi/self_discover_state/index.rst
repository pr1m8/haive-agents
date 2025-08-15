self_discover_state
===================

.. py:module:: self_discover_state

.. autoapi-nested-parse::

   State schema for self-discover multi-agent system.


   .. autolink-examples:: self_discover_state
      :collapse:


Classes
-------

.. autoapisummary::

   self_discover_state.SelfDiscoverState


Module Contents
---------------

.. py:class:: SelfDiscoverState

   Bases: :py:obj:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`


   State schema for self-discover multi-agent workflow.

   This state schema handles the structured output flow between agents:
   1. select_agent: reasoning_modules + task_description → selected_modules
   2. adapt_agent: selected_modules + task_description → adapted_modules
   3. structure_agent: adapted_modules + task_description → reasoning_structure
   4. reason_agent: reasoning_structure + task_description → final_answer


   .. autolink-examples:: SelfDiscoverState
      :collapse:

   .. py:method:: get_adapt_inputs() -> dict[str, Any]

      Get inputs for adapt_agent.


      .. autolink-examples:: get_adapt_inputs
         :collapse:


   .. py:method:: get_reason_inputs() -> dict[str, Any]

      Get inputs for reason_agent.


      .. autolink-examples:: get_reason_inputs
         :collapse:


   .. py:method:: get_select_inputs() -> dict[str, Any]

      Get inputs for select_agent.


      .. autolink-examples:: get_select_inputs
         :collapse:


   .. py:method:: get_structure_inputs() -> dict[str, Any]

      Get inputs for structure_agent.


      .. autolink-examples:: get_structure_inputs
         :collapse:


   .. py:method:: update_from_agent_output(agent_name: str, output: dict[str, Any]) -> None

      Update state with agent output.


      .. autolink-examples:: update_from_agent_output
         :collapse:


   .. py:attribute:: adapted_modules
      :type:  haive.agents.reasoning_and_critique.self_discover.v2.models.AdaptedModules | None
      :value: None



   .. py:attribute:: final_answer
      :type:  haive.agents.reasoning_and_critique.self_discover.v2.models.FinalAnswer | None
      :value: None



   .. py:attribute:: reasoning_modules
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning_structure
      :type:  haive.agents.reasoning_and_critique.self_discover.v2.models.ReasoningStructure | None
      :value: None



   .. py:attribute:: selected_modules
      :type:  haive.agents.reasoning_and_critique.self_discover.v2.models.SelectedModules | None
      :value: None



   .. py:attribute:: task_description
      :type:  str
      :value: None



