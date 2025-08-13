
:py:mod:`agents.base.types`
===========================

.. py:module:: agents.base.types

Core type system for the Haive agent framework.

Defines type variables, constraints, and base protocols for type-safe agent design.


.. autolink-examples:: agents.base.types
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.types.Agent
   agents.base.types.AgentInput
   agents.base.types.AgentOutput
   agents.base.types.AgentState
   agents.base.types.EngineProvider
   agents.base.types.GraphProvider
   agents.base.types.GraphSegment
   agents.base.types.HookContext
   agents.base.types.HookPoint
   agents.base.types.Invokable
   agents.base.types.NodeConnection
   agents.base.types.StateProvider


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Agent:

   .. graphviz::
      :align: center

      digraph inheritance_Agent {
        node [shape=record];
        "Agent" [label="Agent"];
        "GraphProvider[TState]" -> "Agent";
        "StateProvider[TState]" -> "Agent";
        "Invokable[TInput, TOutput]" -> "Agent";
        "EngineProvider[TEngine]" -> "Agent";
        "Protocol[TEngine, TInput, TOutput, TState]" -> "Agent";
      }

.. autoclass:: agents.base.types.Agent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentInput:

   .. graphviz::
      :align: center

      digraph inheritance_AgentInput {
        node [shape=record];
        "AgentInput" [label="AgentInput"];
        "pydantic.BaseModel" -> "AgentInput";
      }

.. autopydantic_model:: agents.base.types.AgentInput
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

   Inheritance diagram for AgentOutput:

   .. graphviz::
      :align: center

      digraph inheritance_AgentOutput {
        node [shape=record];
        "AgentOutput" [label="AgentOutput"];
        "pydantic.BaseModel" -> "AgentOutput";
      }

.. autopydantic_model:: agents.base.types.AgentOutput
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

   Inheritance diagram for AgentState:

   .. graphviz::
      :align: center

      digraph inheritance_AgentState {
        node [shape=record];
        "AgentState" [label="AgentState"];
        "pydantic.BaseModel" -> "AgentState";
      }

.. autopydantic_model:: agents.base.types.AgentState
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

   Inheritance diagram for EngineProvider:

   .. graphviz::
      :align: center

      digraph inheritance_EngineProvider {
        node [shape=record];
        "EngineProvider" [label="EngineProvider"];
        "Protocol[TEngine]" -> "EngineProvider";
      }

.. autoclass:: agents.base.types.EngineProvider
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphProvider:

   .. graphviz::
      :align: center

      digraph inheritance_GraphProvider {
        node [shape=record];
        "GraphProvider" [label="GraphProvider"];
        "Protocol[TState]" -> "GraphProvider";
      }

.. autoclass:: agents.base.types.GraphProvider
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphSegment:

   .. graphviz::
      :align: center

      digraph inheritance_GraphSegment {
        node [shape=record];
        "GraphSegment" [label="GraphSegment"];
        "pydantic.BaseModel" -> "GraphSegment";
        "Generic[TState]" -> "GraphSegment";
      }

.. autopydantic_model:: agents.base.types.GraphSegment
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

   Inheritance diagram for HookContext:

   .. graphviz::
      :align: center

      digraph inheritance_HookContext {
        node [shape=record];
        "HookContext" [label="HookContext"];
        "pydantic.BaseModel" -> "HookContext";
        "Generic[TState]" -> "HookContext";
      }

.. autopydantic_model:: agents.base.types.HookContext
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

   Inheritance diagram for HookPoint:

   .. graphviz::
      :align: center

      digraph inheritance_HookPoint {
        node [shape=record];
        "HookPoint" [label="HookPoint"];
        "str" -> "HookPoint";
        "enum.Enum" -> "HookPoint";
      }

.. autoclass:: agents.base.types.HookPoint
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HookPoint** is an Enum defined in ``agents.base.types``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Invokable:

   .. graphviz::
      :align: center

      digraph inheritance_Invokable {
        node [shape=record];
        "Invokable" [label="Invokable"];
        "Protocol[TInput, TOutput]" -> "Invokable";
      }

.. autoclass:: agents.base.types.Invokable
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NodeConnection:

   .. graphviz::
      :align: center

      digraph inheritance_NodeConnection {
        node [shape=record];
        "NodeConnection" [label="NodeConnection"];
        "pydantic.BaseModel" -> "NodeConnection";
        "Generic[TState]" -> "NodeConnection";
      }

.. autopydantic_model:: agents.base.types.NodeConnection
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

   Inheritance diagram for StateProvider:

   .. graphviz::
      :align: center

      digraph inheritance_StateProvider {
        node [shape=record];
        "StateProvider" [label="StateProvider"];
        "Protocol[TState]" -> "StateProvider";
      }

.. autoclass:: agents.base.types.StateProvider
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.base.types
   :collapse:
   
.. autolink-skip:: next
