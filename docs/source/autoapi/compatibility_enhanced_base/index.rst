
:py:mod:`compatibility_enhanced_base`
=====================================

.. py:module:: compatibility_enhanced_base

Compatibility-Enhanced Multi-Agent Base.

from typing import Any
This module extends the multi-agent base with built-in compatibility checking,
ensuring agents are compatible before building workflows and providing
automatic adaptation when possible.


.. autolink-examples:: compatibility_enhanced_base
   :collapse:

Classes
-------

.. autoapisummary::

   compatibility_enhanced_base.CompatibilityEnhancedConditionalAgent
   compatibility_enhanced_base.CompatibilityEnhancedMultiAgent
   compatibility_enhanced_base.CompatibilityEnhancedParallelAgent
   compatibility_enhanced_base.CompatibilityEnhancedSequentialAgent
   compatibility_enhanced_base.CompatibilityMode
   compatibility_enhanced_base.CompatibilityResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibilityEnhancedConditionalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibilityEnhancedConditionalAgent {
        node [shape=record];
        "CompatibilityEnhancedConditionalAgent" [label="CompatibilityEnhancedConditionalAgent"];
        "CompatibilityEnhancedMultiAgent" -> "CompatibilityEnhancedConditionalAgent";
      }

.. autoclass:: compatibility_enhanced_base.CompatibilityEnhancedConditionalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibilityEnhancedMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibilityEnhancedMultiAgent {
        node [shape=record];
        "CompatibilityEnhancedMultiAgent" [label="CompatibilityEnhancedMultiAgent"];
        "haive.agents.multi.base.MultiAgent" -> "CompatibilityEnhancedMultiAgent";
      }

.. autoclass:: compatibility_enhanced_base.CompatibilityEnhancedMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibilityEnhancedParallelAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibilityEnhancedParallelAgent {
        node [shape=record];
        "CompatibilityEnhancedParallelAgent" [label="CompatibilityEnhancedParallelAgent"];
        "CompatibilityEnhancedMultiAgent" -> "CompatibilityEnhancedParallelAgent";
      }

.. autoclass:: compatibility_enhanced_base.CompatibilityEnhancedParallelAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibilityEnhancedSequentialAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibilityEnhancedSequentialAgent {
        node [shape=record];
        "CompatibilityEnhancedSequentialAgent" [label="CompatibilityEnhancedSequentialAgent"];
        "CompatibilityEnhancedMultiAgent" -> "CompatibilityEnhancedSequentialAgent";
      }

.. autoclass:: compatibility_enhanced_base.CompatibilityEnhancedSequentialAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibilityMode:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibilityMode {
        node [shape=record];
        "CompatibilityMode" [label="CompatibilityMode"];
        "str" -> "CompatibilityMode";
        "enum.Enum" -> "CompatibilityMode";
      }

.. autoclass:: compatibility_enhanced_base.CompatibilityMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CompatibilityMode** is an Enum defined in ``compatibility_enhanced_base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibilityResult:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibilityResult {
        node [shape=record];
        "CompatibilityResult" [label="CompatibilityResult"];
      }

.. autoclass:: compatibility_enhanced_base.CompatibilityResult
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   compatibility_enhanced_base.create_compatible_multi_agent

.. py:function:: create_compatible_multi_agent(agents: list[haive.agents.base.agent.Agent], execution_mode: ExecutionMode = ExecutionMode.SEQUENCE, compatibility_mode: CompatibilityMode = CompatibilityMode.ADAPTIVE, **kwargs) -> CompatibilityEnhancedMultiAgent

   Create a multi-agent system with automatic compatibility checking.

   This function creates a multi-agent system and automatically checks and fixes
   compatibility issues based on the specified compatibility mode.


   .. autolink-examples:: create_compatible_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: compatibility_enhanced_base
   :collapse:
   
.. autolink-skip:: next
