
:py:mod:`agents.base.smart_output_parsing`
==========================================

.. py:module:: agents.base.smart_output_parsing

Smart Output Parsing with Post-Hooks Integration.

This module demonstrates how to use GenericEngineNodeConfig and post-hooks
to handle specific output parsing in a smart, flexible manner.


.. autolink-examples:: agents.base.smart_output_parsing
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.smart_output_parsing.SmartCallableOutputParser
   agents.base.smart_output_parsing.SmartGenericEngineNode
   agents.base.smart_output_parsing.SmartOutputParsingMixin


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SmartCallableOutputParser:

   .. graphviz::
      :align: center

      digraph inheritance_SmartCallableOutputParser {
        node [shape=record];
        "SmartCallableOutputParser" [label="SmartCallableOutputParser"];
        "haive.core.graph.node.callable_node.CallableNodeConfig" -> "SmartCallableOutputParser";
      }

.. autoclass:: agents.base.smart_output_parsing.SmartCallableOutputParser
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SmartGenericEngineNode:

   .. graphviz::
      :align: center

      digraph inheritance_SmartGenericEngineNode {
        node [shape=record];
        "SmartGenericEngineNode" [label="SmartGenericEngineNode"];
        "haive.core.graph.node.engine_node_generic.GenericEngineNodeConfig[TInput, TOutput]" -> "SmartGenericEngineNode";
      }

.. autoclass:: agents.base.smart_output_parsing.SmartGenericEngineNode
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SmartOutputParsingMixin:

   .. graphviz::
      :align: center

      digraph inheritance_SmartOutputParsingMixin {
        node [shape=record];
        "SmartOutputParsingMixin" [label="SmartOutputParsingMixin"];
      }

.. autoclass:: agents.base.smart_output_parsing.SmartOutputParsingMixin
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.base.smart_output_parsing.create_smart_engine_node
   agents.base.smart_output_parsing.create_smart_parsing_callable
   agents.base.smart_output_parsing.detect_content_type
   agents.base.smart_output_parsing.parse_json_content
   agents.base.smart_output_parsing.parse_structured_content

.. py:function:: create_smart_engine_node(engine, name: str, input_schema: type[pydantic.BaseModel] | None = None, output_schema: type[pydantic.BaseModel] | None = None, parsing_strategies: list[str] | None = None, **kwargs) -> SmartGenericEngineNode

   Create a smart generic engine node with output parsing.


   .. autolink-examples:: create_smart_engine_node
      :collapse:

.. py:function:: create_smart_parsing_callable(parsing_functions: dict[str, collections.abc.Callable], detection_function: collections.abc.Callable, name: str = 'smart_parser', **kwargs) -> SmartCallableOutputParser

   Create a smart callable parser with content detection.


   .. autolink-examples:: create_smart_parsing_callable
      :collapse:

.. py:function:: detect_content_type(state) -> str

   Example content type detection function.


   .. autolink-examples:: detect_content_type
      :collapse:

.. py:function:: parse_json_content(state) -> dict

   Example JSON parsing function.


   .. autolink-examples:: parse_json_content
      :collapse:

.. py:function:: parse_structured_content(state) -> dict

   Example structured content parsing function.


   .. autolink-examples:: parse_structured_content
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.base.smart_output_parsing
   :collapse:
   
.. autolink-skip:: next
