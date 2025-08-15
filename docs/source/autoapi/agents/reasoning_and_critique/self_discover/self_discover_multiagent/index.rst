agents.reasoning_and_critique.self_discover.self_discover_multiagent
====================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_multiagent

.. autoapi-nested-parse::

   Self-Discover Agent using the unified MultiAgent implementation.

   This implementation demonstrates how to use the new MultiAgent class to create
   a sophisticated reasoning system that follows the Self-Discover methodology:
   1. Select relevant reasoning modules
   2. Adapt modules to the specific task
   3. Structure a step-by-step plan
   4. Execute the reasoning plan

   This showcases sequential execution with the unified MultiAgent.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_multiagent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_multiagent.SelfDiscoverMultiAgentState


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_multiagent.create_adapter_agent
   agents.reasoning_and_critique.self_discover.self_discover_multiagent.create_reasoner_agent
   agents.reasoning_and_critique.self_discover.self_discover_multiagent.create_selector_agent
   agents.reasoning_and_critique.self_discover.self_discover_multiagent.create_self_discover_multiagent
   agents.reasoning_and_critique.self_discover.self_discover_multiagent.create_self_discover_with_conditional_routing
   agents.reasoning_and_critique.self_discover.self_discover_multiagent.create_structurer_agent
   agents.reasoning_and_critique.self_discover.self_discover_multiagent.get_default_reasoning_modules
   agents.reasoning_and_critique.self_discover.self_discover_multiagent.run_self_discover_example


Module Contents
---------------

.. py:class:: SelfDiscoverMultiAgentState

   Bases: :py:obj:`haive.core.schema.StateSchema`


   State schema for the Self-Discover multi-agent workflow.


   .. autolink-examples:: SelfDiscoverMultiAgentState
      :collapse:

   .. py:attribute:: adapted_modules
      :type:  list[haive.agents.reasoning_and_critique.self_discover.models.AdaptedModule] | None
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning_modules
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning_results
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: reasoning_structure
      :type:  haive.agents.reasoning_and_critique.self_discover.models.ReasoningStructure | None
      :value: None



   .. py:attribute:: selected_modules
      :type:  list[haive.agents.reasoning_and_critique.self_discover.models.SelectedModule] | None
      :value: None



   .. py:attribute:: task_description
      :type:  str
      :value: None



.. py:function:: create_adapter_agent() -> haive.agents.simple.SimpleAgent

   Create the module adapter agent.


   .. autolink-examples:: create_adapter_agent
      :collapse:

.. py:function:: create_reasoner_agent() -> haive.agents.simple.SimpleAgent

   Create the reasoning execution agent.


   .. autolink-examples:: create_reasoner_agent
      :collapse:

.. py:function:: create_selector_agent() -> haive.agents.simple.SimpleAgent

   Create the module selector agent.


   .. autolink-examples:: create_selector_agent
      :collapse:

.. py:function:: create_self_discover_multiagent(name: str = 'self_discover_system', reasoning_modules: list[str] | None = None) -> haive.agents.multi.agent.MultiAgent

   Create a Self-Discover system using MultiAgent.

   This demonstrates sequential execution with the unified MultiAgent implementation.

   :param name: Name for the multi-agent system
   :param reasoning_modules: Optional custom reasoning modules

   :returns: MultiAgent configured for Self-Discover workflow


   .. autolink-examples:: create_self_discover_multiagent
      :collapse:

.. py:function:: create_self_discover_with_conditional_routing() -> haive.agents.multi.agent.MultiAgent

   Create Self-Discover with conditional routing for demonstration.

   This shows how you could add conditional logic if needed, though
   sequential execution is sufficient for Self-Discover.


   .. autolink-examples:: create_self_discover_with_conditional_routing
      :collapse:

.. py:function:: create_structurer_agent() -> haive.agents.simple.SimpleAgent

   Create the reasoning structure agent.


   .. autolink-examples:: create_structurer_agent
      :collapse:

.. py:function:: get_default_reasoning_modules() -> list[str]

   Get the default set of reasoning modules.


   .. autolink-examples:: get_default_reasoning_modules
      :collapse:

.. py:function:: run_self_discover_example()
   :async:


   Run an example of the Self-Discover multi-agent system.


   .. autolink-examples:: run_self_discover_example
      :collapse:

