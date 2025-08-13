
:py:mod:`enhanced_supervisor_agent`
===================================

.. py:module:: enhanced_supervisor_agent

Enhanced SupervisorAgent implementation using Agent[AugLLMConfig].

SupervisorAgent = Agent[AugLLMConfig] + worker management + delegation.


.. autolink-examples:: enhanced_supervisor_agent
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_supervisor_agent.MockWorker
   enhanced_supervisor_agent.SupervisorAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockWorker:

   .. graphviz::
      :align: center

      digraph inheritance_MockWorker {
        node [shape=record];
        "MockWorker" [label="MockWorker"];
      }

.. autoclass:: enhanced_supervisor_agent.MockWorker
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorAgent {
        node [shape=record];
        "SupervisorAgent" [label="SupervisorAgent"];
        "haive.agents.simple.enhanced_simple_real.EnhancedAgentBase" -> "SupervisorAgent";
      }

.. autoclass:: enhanced_supervisor_agent.SupervisorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: enhanced_supervisor_agent
   :collapse:
   
.. autolink-skip:: next
