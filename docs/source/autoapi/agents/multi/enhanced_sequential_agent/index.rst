
:py:mod:`agents.multi.enhanced_sequential_agent`
================================================

.. py:module:: agents.multi.enhanced_sequential_agent

Enhanced SequentialAgent implementation using Agent[AugLLMConfig].

SequentialAgent = Agent[AugLLMConfig] + sequential execution of agents.


.. autolink-examples:: agents.multi.enhanced_sequential_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.enhanced_sequential_agent.MockAgent
   agents.multi.enhanced_sequential_agent.SequentialAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MockAgent {
        node [shape=record];
        "MockAgent" [label="MockAgent"];
      }

.. autoclass:: agents.multi.enhanced_sequential_agent.MockAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgent {
        node [shape=record];
        "SequentialAgent" [label="SequentialAgent"];
        "haive.agents.simple.enhanced_simple_real.EnhancedAgentBase" -> "SequentialAgent";
      }

.. autoclass:: agents.multi.enhanced_sequential_agent.SequentialAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.enhanced_sequential_agent
   :collapse:
   
.. autolink-skip:: next
