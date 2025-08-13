
:py:mod:`enhanced_react_agent`
==============================

.. py:module:: enhanced_react_agent

Enhanced ReactAgent implementation using Agent[AugLLMConfig].

ReactAgent = Agent[AugLLMConfig] + reasoning loop with tools.


.. autolink-examples:: enhanced_react_agent
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_react_agent.ReactAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "haive.agents.simple.enhanced_simple_real.EnhancedAgentBase" -> "ReactAgent";
      }

.. autoclass:: enhanced_react_agent.ReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: enhanced_react_agent
   :collapse:
   
.. autolink-skip:: next
