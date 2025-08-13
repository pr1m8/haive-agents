
:py:mod:`agents.react_class.react.tool_utils`
=============================================

.. py:module:: agents.react_class.react.tool_utils



Functions
---------

.. autoapisummary::

   agents.react_class.react.tool_utils.create_tool_executor
   agents.react_class.react.tool_utils.create_tool_executor_v2
   agents.react_class.react.tool_utils.filter_tools_for_query
   agents.react_class.react.tool_utils.prepare_tools
   agents.react_class.react.tool_utils.tools_router
   agents.react_class.react.tool_utils.tools_router_v2

.. py:function:: create_tool_executor(tools: list[langchain_core.tools.BaseTool]) -> collections.abc.Callable

   Create a function that executes tools based on tool calls.

   :param tools: List of tools available for execution

   :returns: Function that takes state and executes tools


   .. autolink-examples:: create_tool_executor
      :collapse:

.. py:function:: create_tool_executor_v2(tools: list[langchain_core.tools.BaseTool]) -> collections.abc.Callable

   Create a function that executes a single tool for v2 architecture.

   :param tools: List of tools available for execution

   :returns: Function that takes state and a tool call and executes it


   .. autolink-examples:: create_tool_executor_v2
      :collapse:

.. py:function:: filter_tools_for_query(tools: list[langchain_core.tools.BaseTool], query: str) -> list[langchain_core.tools.BaseTool]

   Filter tools based on relevance to the query.

   :param tools: List of available tools
   :param query: User query or relevant context

   :returns: Filtered list of relevant tools


   .. autolink-examples:: filter_tools_for_query
      :collapse:

.. py:function:: prepare_tools(tools: list[langchain_core.tools.BaseTool | dict[str, Any] | collections.abc.Callable]) -> list[langchain_core.tools.BaseTool]

   Prepare tools for the React Agent.

   :param tools: List of tools that can be BaseTool instances, dictionaries, or callables.

   :returns: List of BaseTool instances.


   .. autolink-examples:: prepare_tools
      :collapse:

.. py:function:: tools_router(state: dict[str, Any]) -> str | list[langgraph.types.Send]

   Router function for deciding next step after agent node.

   :param state: Current state with messages field

   :returns: Next node to route to, or END if no tools needed


   .. autolink-examples:: tools_router
      :collapse:

.. py:function:: tools_router_v2(state: dict[str, Any]) -> str | list[langgraph.types.Send]

   Router function for v2 - sending each tool call to a separate tool node instance.

   :param state: Current state with messages field

   :returns: Next node to route to, list of Send objects, or END


   .. autolink-examples:: tools_router_v2
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react.tool_utils
   :collapse:
   
.. autolink-skip:: next
