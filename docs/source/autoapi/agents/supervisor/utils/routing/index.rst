
:py:mod:`agents.supervisor.utils.routing`
=========================================

.. py:module:: agents.supervisor.utils.routing

Dynamic Routing Engine for Haive Supervisor System.

Handles intelligent routing decisions using DynamicChoiceModel and LLM-based analysis.
Provides context-aware agent selection with validation and fallback mechanisms.


.. autolink-examples:: agents.supervisor.utils.routing
   :collapse:

Classes
-------

.. autoapisummary::

   agents.supervisor.utils.routing.BaseRoutingStrategy
   agents.supervisor.utils.routing.DynamicRoutingEngine
   agents.supervisor.utils.routing.LLMRoutingStrategy
   agents.supervisor.utils.routing.RoutingContext
   agents.supervisor.utils.routing.RoutingDecision
   agents.supervisor.utils.routing.RuleBasedRoutingStrategy
   agents.supervisor.utils.routing.TaskClassifier


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

.. autoclass:: agents.supervisor.utils.routing.BaseRoutingStrategy
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

.. autoclass:: agents.supervisor.utils.routing.DynamicRoutingEngine
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

.. autoclass:: agents.supervisor.utils.routing.LLMRoutingStrategy
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

.. autopydantic_model:: agents.supervisor.utils.routing.RoutingContext
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

.. autopydantic_model:: agents.supervisor.utils.routing.RoutingDecision
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

.. autoclass:: agents.supervisor.utils.routing.RuleBasedRoutingStrategy
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

.. autoclass:: agents.supervisor.utils.routing.TaskClassifier
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.utils.routing
   :collapse:
   
.. autolink-skip:: next
