
:py:mod:`example`
=================

.. py:module:: example

Example demonstrating the MultiAgent system.

from typing import Any
This example shows how to create and use a multi-agent system
with different agent types and coordination strategies.


.. autolink-examples:: example
   :collapse:

Classes
-------

.. autoapisummary::

   example.ResearchAgent
   example.WritingAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResearchAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchAgent {
        node [shape=record];
        "ResearchAgent" [label="ResearchAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "ResearchAgent";
      }

.. autoclass:: example.ResearchAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WritingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_WritingAgent {
        node [shape=record];
        "WritingAgent" [label="WritingAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "WritingAgent";
      }

.. autoclass:: example.WritingAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   example.create_parallel_specialist_system
   example.create_research_writing_system
   example.demo_multi_agent_system
   example.save_and_load_demo

.. py:function:: create_parallel_specialist_system() -> Any

   Create a multi-agent system with multiple specialist agents.

   This would use parallel coordination strategy.

   :returns: MultiAgent system


   .. autolink-examples:: create_parallel_specialist_system
      :collapse:

.. py:function:: create_research_writing_system() -> haive.agents.multi.agent.MultiAgent

   Create a multi-agent system with research and writing agents.

   :returns: MultiAgent system


   .. autolink-examples:: create_research_writing_system
      :collapse:

.. py:function:: demo_multi_agent_system() -> None

   Demonstrate a multi-agent system in action.


   .. autolink-examples:: demo_multi_agent_system
      :collapse:

.. py:function:: save_and_load_demo() -> None

   Demonstrate saving and loading a multi-agent system.


   .. autolink-examples:: save_and_load_demo
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: example
   :collapse:
   
.. autolink-skip:: next
