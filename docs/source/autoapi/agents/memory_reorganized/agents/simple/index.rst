
:py:mod:`agents.memory_reorganized.agents.simple`
=================================================

.. py:module:: agents.memory_reorganized.agents.simple

SimpleMemoryAgent with token-aware memory management and summarization.

This agent follows V3 enhanced patterns with automatic summarization when approaching
token limits, similar to LangMem's approach.


.. autolink-examples:: agents.memory_reorganized.agents.simple
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.agents.simple.SimpleMemoryAgent
   agents.memory_reorganized.agents.simple.TokenAwareMemoryConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleMemoryAgent {
        node [shape=record];
        "SimpleMemoryAgent" [label="SimpleMemoryAgent"];
        "haive.agents.simple.enhanced_agent_v3.EnhancedSimpleAgent" -> "SimpleMemoryAgent";
      }

.. autoclass:: agents.memory_reorganized.agents.simple.SimpleMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TokenAwareMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_TokenAwareMemoryConfig {
        node [shape=record];
        "TokenAwareMemoryConfig" [label="TokenAwareMemoryConfig"];
        "haive.agents.memory_reorganized.core.memory_tools.MemoryConfig" -> "TokenAwareMemoryConfig";
      }

.. autoclass:: agents.memory_reorganized.agents.simple.TokenAwareMemoryConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.agents.simple
   :collapse:
   
.. autolink-skip:: next
