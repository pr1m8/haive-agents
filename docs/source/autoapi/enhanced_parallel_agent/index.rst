
:py:mod:`enhanced_parallel_agent`
=================================

.. py:module:: enhanced_parallel_agent

Enhanced ParallelAgent implementation using Agent[AugLLMConfig].

ParallelAgent = Agent[AugLLMConfig] + parallel execution of agents.


.. autolink-examples:: enhanced_parallel_agent
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_parallel_agent.MockExpert
   enhanced_parallel_agent.ParallelAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockExpert:

   .. graphviz::
      :align: center

      digraph inheritance_MockExpert {
        node [shape=record];
        "MockExpert" [label="MockExpert"];
      }

.. autoclass:: enhanced_parallel_agent.MockExpert
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelAgent {
        node [shape=record];
        "ParallelAgent" [label="ParallelAgent"];
        "haive.agents.simple.enhanced_simple_real.EnhancedAgentBase" -> "ParallelAgent";
      }

.. autoclass:: enhanced_parallel_agent.ParallelAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: enhanced_parallel_agent
   :collapse:
   
.. autolink-skip:: next
