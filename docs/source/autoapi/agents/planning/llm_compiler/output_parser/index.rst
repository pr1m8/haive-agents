agents.planning.llm_compiler.output_parser
==========================================

.. py:module:: agents.planning.llm_compiler.output_parser


Attributes
----------

.. autoapisummary::

   agents.planning.llm_compiler.output_parser.ACTION_PATTERN
   agents.planning.llm_compiler.output_parser.END_OF_PLAN
   agents.planning.llm_compiler.output_parser.ID_PATTERN
   agents.planning.llm_compiler.output_parser.THOUGHT_PATTERN


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.output_parser.LLMCompilerPlanParser
   agents.planning.llm_compiler.output_parser.Task


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler.output_parser._ast_parse
   agents.planning.llm_compiler.output_parser._get_dependencies_from_graph
   agents.planning.llm_compiler.output_parser._parse_llm_compiler_action_args
   agents.planning.llm_compiler.output_parser.default_dependency_rule
   agents.planning.llm_compiler.output_parser.instantiate_task


Module Contents
---------------

.. py:class:: LLMCompilerPlanParser

   Bases: :py:obj:`langchain_core.output_parsers.transform.BaseTransformOutputParser`\ [\ :py:obj:`dict`\ ]


   Planning output parser.


   .. autolink-examples:: LLMCompilerPlanParser
      :collapse:

   .. py:method:: _parse_task(line: str, thought: str | None = None)


   .. py:method:: _transform(input: collections.abc.Iterator[str | langchain_core.messages.BaseMessage]) -> collections.abc.Iterator[Task]


   .. py:method:: ingest_token(token: str, buffer: list[str], thought: str | None) -> collections.abc.Iterator[tuple[Task | None, str]]


   .. py:method:: parse(text: str) -> list[Task]

      Parse a single string model output into some structure.

      :param text: String output of a language model.

      :returns: Structured output.


      .. autolink-examples:: parse
         :collapse:


   .. py:method:: stream(input: str | langchain_core.messages.BaseMessage, config: langchain_core.runnables.RunnableConfig | None = None, **kwargs: Any | None) -> collections.abc.Iterator[Task]


   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool]


.. py:class:: Task

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Task
      :collapse:

   .. py:attribute:: args
      :type:  list


   .. py:attribute:: dependencies
      :type:  dict[str, list]


   .. py:attribute:: idx
      :type:  int


   .. py:attribute:: thought
      :type:  str | None


   .. py:attribute:: tool
      :type:  langchain_core.tools.BaseTool


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

.. py:data:: ACTION_PATTERN
   :value: '\\n*(\\d+)\\. ()\\((.*)\\)(\\s*#\\n)?'


.. py:data:: END_OF_PLAN
   :value: ''


.. py:data:: ID_PATTERN
   :value: '\\$\\{?(\\d+)\\}?'


.. py:data:: THOUGHT_PATTERN
   :value: 'Thought: ([^\\n]*)'


