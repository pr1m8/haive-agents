
:py:mod:`agents.discovery.dynamic_tool_selector`
================================================

.. py:module:: agents.discovery.dynamic_tool_selector

Dynamic Tool Selector implementing LangGraph-style tool management patterns.

This module implements sophisticated tool selection and management patterns
inspired by LangGraph's many-tools approach, providing dynamic tool binding,
context-aware selection, and intelligent tool routing.

Key Features:
- Dynamic tool selection and binding like LangGraph
- Context-aware tool recommendation
- Intelligent tool routing and management
- State-aware tool selection
- Tool usage learning and optimization


.. autolink-examples:: agents.discovery.dynamic_tool_selector
   :collapse:

Classes
-------

.. autoapisummary::

   agents.discovery.dynamic_tool_selector.ContextAwareSelector
   agents.discovery.dynamic_tool_selector.ContextAwareState
   agents.discovery.dynamic_tool_selector.DynamicToolSelector
   agents.discovery.dynamic_tool_selector.LangGraphStyleSelector
   agents.discovery.dynamic_tool_selector.SelectionMode
   agents.discovery.dynamic_tool_selector.ToolBindingStrategy
   agents.discovery.dynamic_tool_selector.ToolSelectionResult
   agents.discovery.dynamic_tool_selector.ToolSelectionStrategy
   agents.discovery.dynamic_tool_selector.ToolUsageStats


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContextAwareSelector:

   .. graphviz::
      :align: center

      digraph inheritance_ContextAwareSelector {
        node [shape=record];
        "ContextAwareSelector" [label="ContextAwareSelector"];
        "DynamicToolSelector" -> "ContextAwareSelector";
      }

.. autoclass:: agents.discovery.dynamic_tool_selector.ContextAwareSelector
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContextAwareState:

   .. graphviz::
      :align: center

      digraph inheritance_ContextAwareState {
        node [shape=record];
        "ContextAwareState" [label="ContextAwareState"];
        "pydantic.BaseModel" -> "ContextAwareState";
      }

.. autopydantic_model:: agents.discovery.dynamic_tool_selector.ContextAwareState
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

   Inheritance diagram for DynamicToolSelector:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicToolSelector {
        node [shape=record];
        "DynamicToolSelector" [label="DynamicToolSelector"];
        "haive.core.common.mixins.tool_route_mixin.ToolRouteMixin" -> "DynamicToolSelector";
      }

.. autoclass:: agents.discovery.dynamic_tool_selector.DynamicToolSelector
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LangGraphStyleSelector:

   .. graphviz::
      :align: center

      digraph inheritance_LangGraphStyleSelector {
        node [shape=record];
        "LangGraphStyleSelector" [label="LangGraphStyleSelector"];
        "DynamicToolSelector" -> "LangGraphStyleSelector";
      }

.. autoclass:: agents.discovery.dynamic_tool_selector.LangGraphStyleSelector
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelectionMode:

   .. graphviz::
      :align: center

      digraph inheritance_SelectionMode {
        node [shape=record];
        "SelectionMode" [label="SelectionMode"];
        "str" -> "SelectionMode";
        "enum.Enum" -> "SelectionMode";
      }

.. autoclass:: agents.discovery.dynamic_tool_selector.SelectionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **SelectionMode** is an Enum defined in ``agents.discovery.dynamic_tool_selector``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolBindingStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_ToolBindingStrategy {
        node [shape=record];
        "ToolBindingStrategy" [label="ToolBindingStrategy"];
        "str" -> "ToolBindingStrategy";
        "enum.Enum" -> "ToolBindingStrategy";
      }

.. autoclass:: agents.discovery.dynamic_tool_selector.ToolBindingStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ToolBindingStrategy** is an Enum defined in ``agents.discovery.dynamic_tool_selector``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolSelectionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ToolSelectionResult {
        node [shape=record];
        "ToolSelectionResult" [label="ToolSelectionResult"];
        "pydantic.BaseModel" -> "ToolSelectionResult";
      }

.. autopydantic_model:: agents.discovery.dynamic_tool_selector.ToolSelectionResult
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

   Inheritance diagram for ToolSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_ToolSelectionStrategy {
        node [shape=record];
        "ToolSelectionStrategy" [label="ToolSelectionStrategy"];
        "Protocol" -> "ToolSelectionStrategy";
      }

.. autoclass:: agents.discovery.dynamic_tool_selector.ToolSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolUsageStats:

   .. graphviz::
      :align: center

      digraph inheritance_ToolUsageStats {
        node [shape=record];
        "ToolUsageStats" [label="ToolUsageStats"];
        "pydantic.BaseModel" -> "ToolUsageStats";
      }

.. autopydantic_model:: agents.discovery.dynamic_tool_selector.ToolUsageStats
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



Functions
---------

.. autoapisummary::

   agents.discovery.dynamic_tool_selector.create_context_aware_selector
   agents.discovery.dynamic_tool_selector.create_dynamic_tool_selector
   agents.discovery.dynamic_tool_selector.create_langgraph_style_selector

.. py:function:: create_context_aware_selector(max_tools: int = 5, min_confidence: float = 0.7) -> ContextAwareSelector

   Create a context-aware tool selector.


   .. autolink-examples:: create_context_aware_selector
      :collapse:

.. py:function:: create_dynamic_tool_selector(selection_mode: SelectionMode = SelectionMode.DYNAMIC, max_tools: int = 5, semantic_discovery: SemanticDiscoveryEngine | None = None) -> DynamicToolSelector

   Create a dynamic tool selector with sensible defaults.


   .. autolink-examples:: create_dynamic_tool_selector
      :collapse:

.. py:function:: create_langgraph_style_selector(max_tools: int = 5, learning_enabled: bool = True) -> LangGraphStyleSelector

   Create a LangGraph-style tool selector.


   .. autolink-examples:: create_langgraph_style_selector
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.discovery.dynamic_tool_selector
   :collapse:
   
.. autolink-skip:: next
