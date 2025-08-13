
:py:mod:`agents.discovery.selection_strategies`
===============================================

.. py:module:: agents.discovery.selection_strategies

Tool selection strategies for dynamic tool selection.

This module implements various strategies for selecting tools based on
different criteria and approaches, providing flexibility in how tools
are chosen for different contexts and use cases.


.. autolink-examples:: agents.discovery.selection_strategies
   :collapse:

Classes
-------

.. autoapisummary::

   agents.discovery.selection_strategies.AdaptiveSelectionStrategy
   agents.discovery.selection_strategies.BaseSelectionStrategy
   agents.discovery.selection_strategies.CapabilityBasedStrategy
   agents.discovery.selection_strategies.ContextualSelectionStrategy
   agents.discovery.selection_strategies.EnsembleSelectionStrategy
   agents.discovery.selection_strategies.LearningSelectionStrategy
   agents.discovery.selection_strategies.SemanticSelectionStrategy


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveSelectionStrategy {
        node [shape=record];
        "AdaptiveSelectionStrategy" [label="AdaptiveSelectionStrategy"];
        "BaseSelectionStrategy" -> "AdaptiveSelectionStrategy";
      }

.. autoclass:: agents.discovery.selection_strategies.AdaptiveSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_BaseSelectionStrategy {
        node [shape=record];
        "BaseSelectionStrategy" [label="BaseSelectionStrategy"];
        "abc.ABC" -> "BaseSelectionStrategy";
      }

.. autoclass:: agents.discovery.selection_strategies.BaseSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CapabilityBasedStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_CapabilityBasedStrategy {
        node [shape=record];
        "CapabilityBasedStrategy" [label="CapabilityBasedStrategy"];
        "BaseSelectionStrategy" -> "CapabilityBasedStrategy";
      }

.. autoclass:: agents.discovery.selection_strategies.CapabilityBasedStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContextualSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_ContextualSelectionStrategy {
        node [shape=record];
        "ContextualSelectionStrategy" [label="ContextualSelectionStrategy"];
        "BaseSelectionStrategy" -> "ContextualSelectionStrategy";
      }

.. autoclass:: agents.discovery.selection_strategies.ContextualSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnsembleSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_EnsembleSelectionStrategy {
        node [shape=record];
        "EnsembleSelectionStrategy" [label="EnsembleSelectionStrategy"];
        "BaseSelectionStrategy" -> "EnsembleSelectionStrategy";
      }

.. autoclass:: agents.discovery.selection_strategies.EnsembleSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LearningSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_LearningSelectionStrategy {
        node [shape=record];
        "LearningSelectionStrategy" [label="LearningSelectionStrategy"];
        "BaseSelectionStrategy" -> "LearningSelectionStrategy";
      }

.. autoclass:: agents.discovery.selection_strategies.LearningSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SemanticSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_SemanticSelectionStrategy {
        node [shape=record];
        "SemanticSelectionStrategy" [label="SemanticSelectionStrategy"];
        "BaseSelectionStrategy" -> "SemanticSelectionStrategy";
      }

.. autoclass:: agents.discovery.selection_strategies.SemanticSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.discovery.selection_strategies._get_tool_selection_result
   agents.discovery.selection_strategies.create_selection_strategy

.. py:function:: _get_tool_selection_result()

   Lazy import of ToolSelectionResult to avoid circular imports.


   .. autolink-examples:: _get_tool_selection_result
      :collapse:

.. py:function:: create_selection_strategy(strategy_name: str, **kwargs) -> BaseSelectionStrategy

   Create a selection strategy by name.


   .. autolink-examples:: create_selection_strategy
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.discovery.selection_strategies
   :collapse:
   
.. autolink-skip:: next
