
:py:mod:`agents.memory_reorganized.agents.long_term_v2`
=======================================================

.. py:module:: agents.memory_reorganized.agents.long_term_v2

Agent core module.

This module provides agent functionality for the Haive framework.

Classes:
    LongTermMemoryAgentConfig: LongTermMemoryAgentConfig implementation.
    LongTermMemoryAgent: LongTermMemoryAgent implementation.

Functions:
    load_memories: Load Memories functionality.
    setup_workflow: Setup Workflow functionality.


.. autolink-examples:: agents.memory_reorganized.agents.long_term_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.agents.long_term_v2.LongTermMemoryAgent
   agents.memory_reorganized.agents.long_term_v2.LongTermMemoryAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LongTermMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LongTermMemoryAgent {
        node [shape=record];
        "LongTermMemoryAgent" [label="LongTermMemoryAgent"];
        "ReactAgent" -> "LongTermMemoryAgent";
      }

.. autoclass:: agents.memory_reorganized.agents.long_term_v2.LongTermMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LongTermMemoryAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LongTermMemoryAgentConfig {
        node [shape=record];
        "LongTermMemoryAgentConfig" [label="LongTermMemoryAgentConfig"];
        "haive.agents.memory_reorganized.agents.react_agent2.agent.ReactAgentConfig" -> "LongTermMemoryAgentConfig";
      }

.. autoclass:: agents.memory_reorganized.agents.long_term_v2.LongTermMemoryAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.agents.long_term_v2
   :collapse:
   
.. autolink-skip:: next
