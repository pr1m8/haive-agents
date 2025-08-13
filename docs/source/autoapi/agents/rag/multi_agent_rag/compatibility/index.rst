
:py:mod:`agents.rag.multi_agent_rag.compatibility`
==================================================

.. py:module:: agents.rag.multi_agent_rag.compatibility

Safe Agent Compatibility Testing.

This module provides comprehensive compatibility testing for RAG agents using the
compatibility module without modifying or breaking existing agents.


.. autolink-examples:: agents.rag.multi_agent_rag.compatibility
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.compatibility.AgentCompatibilityReport
   agents.rag.multi_agent_rag.compatibility.CompatibilityLevel
   agents.rag.multi_agent_rag.compatibility.MultiAgentCompatibilityReport
   agents.rag.multi_agent_rag.compatibility.SafeCompatibilityTester


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentCompatibilityReport:

   .. graphviz::
      :align: center

      digraph inheritance_AgentCompatibilityReport {
        node [shape=record];
        "AgentCompatibilityReport" [label="AgentCompatibilityReport"];
      }

.. autoclass:: agents.rag.multi_agent_rag.compatibility.AgentCompatibilityReport
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibilityLevel:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibilityLevel {
        node [shape=record];
        "CompatibilityLevel" [label="CompatibilityLevel"];
        "str" -> "CompatibilityLevel";
        "enum.Enum" -> "CompatibilityLevel";
      }

.. autoclass:: agents.rag.multi_agent_rag.compatibility.CompatibilityLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CompatibilityLevel** is an Enum defined in ``agents.rag.multi_agent_rag.compatibility``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgentCompatibilityReport:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentCompatibilityReport {
        node [shape=record];
        "MultiAgentCompatibilityReport" [label="MultiAgentCompatibilityReport"];
      }

.. autoclass:: agents.rag.multi_agent_rag.compatibility.MultiAgentCompatibilityReport
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SafeCompatibilityTester:

   .. graphviz::
      :align: center

      digraph inheritance_SafeCompatibilityTester {
        node [shape=record];
        "SafeCompatibilityTester" [label="SafeCompatibilityTester"];
      }

.. autoclass:: agents.rag.multi_agent_rag.compatibility.SafeCompatibilityTester
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.compatibility.quick_agent_compatibility_check
   agents.rag.multi_agent_rag.compatibility.safe_test_rag_compatibility
   agents.rag.multi_agent_rag.compatibility.test_custom_agent_workflow

.. py:function:: quick_agent_compatibility_check(agent1: haive.agents.base.agent.Agent, agent2: haive.agents.base.agent.Agent) -> bool

   Quick compatibility check between two agents.

   :returns: True if agents are safe to chain, False otherwise


   .. autolink-examples:: quick_agent_compatibility_check
      :collapse:

.. py:function:: safe_test_rag_compatibility() -> dict[str, Any]

   Safely test RAG agent compatibility without breaking anything.

   This is the main function to use for testing RAG agent compatibility.


   .. autolink-examples:: safe_test_rag_compatibility
      :collapse:

.. py:function:: test_custom_agent_workflow(agents: list[haive.agents.base.agent.Agent], workflow_name: str) -> MultiAgentCompatibilityReport

   Test compatibility of a custom agent workflow.

   :param agents: List of agents to test
   :param workflow_name: Name for the workflow

   :returns: Comprehensive compatibility report


   .. autolink-examples:: test_custom_agent_workflow
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.compatibility
   :collapse:
   
.. autolink-skip:: next
