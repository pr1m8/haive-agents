
:py:mod:`agents.reasoning_and_critique.self_discover.self_discover_multiagent`
==============================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_multiagent

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfDiscoverMultiAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_SelfDiscoverMultiAgentState {
        node [shape=record];
        "SelfDiscoverMultiAgentState" [label="SelfDiscoverMultiAgentState"];
        "haive.core.schema.StateSchema" -> "SelfDiscoverMultiAgentState";
      }

.. autoclass:: agents.reasoning_and_critique.self_discover.self_discover_multiagent.SelfDiscoverMultiAgentState
   :members:
   :undoc-members:
   :show-inheritance:


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



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_multiagent
   :collapse:
   
.. autolink-skip:: next
