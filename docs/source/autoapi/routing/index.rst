
:py:mod:`routing`
=================

.. py:module:: routing

Dynamic Routing Engine for Haive Supervisor System.

Handles intelligent routing decisions using DynamicChoiceModel and LLM-based analysis.
Provides context-aware agent selection with validation and fallback mechanisms.


.. autolink-examples:: routing
   :collapse:

Classes
-------

.. autoapisummary::

   routing.BaseRoutingStrategy
   routing.DynamicRoutingEngine
   routing.LLMRoutingStrategy
   routing.RoutingContext
   routing.RoutingDecision
   routing.RuleBasedRoutingStrategy
   routing.TaskClassifier


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseRoutingStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_BaseRoutingStrategy {
        node [shape=record];
        "BaseRoutingStrategy" [label="BaseRoutingStrategy"];
        "abc.ABC" -> "BaseRoutingStrategy";
      }

.. autoclass:: routing.BaseRoutingStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicRoutingEngine:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicRoutingEngine {
        node [shape=record];
        "DynamicRoutingEngine" [label="DynamicRoutingEngine"];
      }

.. autoclass:: routing.DynamicRoutingEngine
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMRoutingStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_LLMRoutingStrategy {
        node [shape=record];
        "LLMRoutingStrategy" [label="LLMRoutingStrategy"];
        "BaseRoutingStrategy" -> "LLMRoutingStrategy";
      }

.. autoclass:: routing.LLMRoutingStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingContext:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingContext {
        node [shape=record];
        "RoutingContext" [label="RoutingContext"];
        "pydantic.BaseModel" -> "RoutingContext";
      }

.. autopydantic_model:: routing.RoutingContext
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingDecision:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingDecision {
        node [shape=record];
        "RoutingDecision" [label="RoutingDecision"];
        "pydantic.BaseModel" -> "RoutingDecision";
      }

.. autopydantic_model:: routing.RoutingDecision
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RuleBasedRoutingStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RuleBasedRoutingStrategy {
        node [shape=record];
        "RuleBasedRoutingStrategy" [label="RuleBasedRoutingStrategy"];
        "BaseRoutingStrategy" -> "RuleBasedRoutingStrategy";
      }

.. autoclass:: routing.RuleBasedRoutingStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskClassifier:

   .. graphviz::
      :align: center

      digraph inheritance_TaskClassifier {
        node [shape=record];
        "TaskClassifier" [label="TaskClassifier"];
      }

.. autoclass:: routing.TaskClassifier
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: routing
   :collapse:
   
.. autolink-skip:: next
