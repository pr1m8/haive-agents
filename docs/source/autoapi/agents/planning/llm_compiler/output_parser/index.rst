
:py:mod:`agents.planning.llm_compiler.output_parser`
====================================================

.. py:module:: agents.planning.llm_compiler.output_parser


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.output_parser.LLMCompilerPlanParser
   agents.planning.llm_compiler.output_parser.Task


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMCompilerPlanParser:

   .. graphviz::
      :align: center

      digraph inheritance_LLMCompilerPlanParser {
        node [shape=record];
        "LLMCompilerPlanParser" [label="LLMCompilerPlanParser"];
        "langchain_core.output_parsers.transform.BaseTransformOutputParser[dict]" -> "LLMCompilerPlanParser";
      }

.. autoclass:: agents.planning.llm_compiler.output_parser.LLMCompilerPlanParser
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Task:

   .. graphviz::
      :align: center

      digraph inheritance_Task {
        node [shape=record];
        "Task" [label="Task"];
        "typing_extensions.TypedDict" -> "Task";
      }

.. autoclass:: agents.planning.llm_compiler.output_parser.Task
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler.output_parser._ast_parse
   agents.planning.llm_compiler.output_parser._get_dependencies_from_graph
   agents.planning.llm_compiler.output_parser._parse_llm_compiler_action_args
   agents.planning.llm_compiler.output_parser.default_dependency_rule
   agents.planning.llm_compiler.output_parser.instantiate_task

.. py:function:: _ast_parse(arg: str) -> Any

.. py:function:: _get_dependencies_from_graph(idx: int, tool_name: str, args: dict[str, Any]) -> dict[str, list[str]]

   Get dependencies from a graph.


   .. autolink-examples:: _get_dependencies_from_graph
      :collapse:

.. py:function:: _parse_llm_compiler_action_args(args: str, tool: str | langchain_core.tools.BaseTool) -> list[Any]

   Parse arguments from a string.


   .. autolink-examples:: _parse_llm_compiler_action_args
      :collapse:

.. py:function:: default_dependency_rule(idx, args: str)

.. py:function:: instantiate_task(tools: collections.abc.Sequence[langchain_core.tools.BaseTool], idx: int, tool_name: str, args: str | Any, thought: str | None = None) -> Task



.. rubric:: Related Links

.. autolink-examples:: agents.planning.llm_compiler.output_parser
   :collapse:
   
.. autolink-skip:: next
