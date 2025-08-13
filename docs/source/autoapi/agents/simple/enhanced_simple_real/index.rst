
:py:mod:`agents.simple.enhanced_simple_real`
============================================

.. py:module:: agents.simple.enhanced_simple_real

Enhanced SimpleAgent - Real implementation using Agent[AugLLMConfig].

This is the real SimpleAgent implementation showing it as Agent[AugLLMConfig].
It carefully imports only what's needed to avoid circular imports.


.. autolink-examples:: agents.simple.enhanced_simple_real
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.enhanced_simple_real.EnhancedAgentBase
   agents.simple.enhanced_simple_real.SimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedAgentBase:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedAgentBase {
        node [shape=record];
        "EnhancedAgentBase" [label="EnhancedAgentBase"];
      }

.. autoclass:: agents.simple.enhanced_simple_real.EnhancedAgentBase
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgent {
        node [shape=record];
        "SimpleAgent" [label="SimpleAgent"];
        "EnhancedAgentBase" -> "SimpleAgent";
      }

.. autoclass:: agents.simple.enhanced_simple_real.SimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.enhanced_simple_real
   :collapse:
   
.. autolink-skip:: next
