
:py:mod:`agents.react_class.react_agent2.nodes`
===============================================

.. py:module:: agents.react_class.react_agent2.nodes



Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.nodes.act_node
   agents.react_class.react_agent2.nodes.create_tool_node
   agents.react_class.react_agent2.nodes.execute_tool
   agents.react_class.react_agent2.nodes.get_tool_by_name
   agents.react_class.react_agent2.nodes.get_tool_description
   agents.react_class.react_agent2.nodes.get_tool_name
   agents.react_class.react_agent2.nodes.observe_node
   agents.react_class.react_agent2.nodes.route_by_status
   agents.react_class.react_agent2.nodes.think_node

.. py:function:: act_node(state: dict[str, Any]) -> langgraph.types.Command

   Execute the action from the current thought.


   .. autolink-examples:: act_node
      :collapse:

.. py:function:: create_tool_node(tool_name: str) -> collections.abc.Callable

   Create a node function for a specific tool.

   :param tool_name: Name of the tool

   :returns: Node function for LangGraph


   .. autolink-examples:: create_tool_node
      :collapse:

.. py:function:: execute_tool(tool, input_value) -> Any

   Execute a tool with the given input.
   Handles different tool formats (function, BaseTool, or class with __call__).


   .. autolink-examples:: execute_tool
      :collapse:

.. py:function:: get_tool_by_name(tools: list[str], name: str)

   Get a tool by name from the tools dictionary or list.
   Handles different tool formats (function, BaseTool, or class with name attribute).


   .. autolink-examples:: get_tool_by_name
      :collapse:

.. py:function:: get_tool_description(tool) -> Any | None

   Get the description of a tool.
   Handles different tool formats (function, BaseTool, or class with description).


   .. autolink-examples:: get_tool_description
      :collapse:

.. py:function:: get_tool_name(tool) -> Any | None

   Get the name of a tool.
   Handles different tool formats (function, BaseTool, or class with name).


   .. autolink-examples:: get_tool_name
      :collapse:

.. py:function:: observe_node(state: dict[str, Any]) -> langgraph.types.Command

   Observe the results and decide next steps.


   .. autolink-examples:: observe_node
      :collapse:

.. py:function:: route_by_status(state: dict[str, Any]) -> str

   Route based on the current status.


   .. autolink-examples:: route_by_status
      :collapse:

.. py:function:: think_node(state: dict[str, Any], aug_llm: haive.core.engine.aug_llm.AugLLMConfig | None = None) -> langgraph.types.Command

   Think about the current state and decide on an action.

   :param state: Current state dict or ReactState
   :param aug_llm: Optional AugLLMConfig for thinking (if provided, overrides the default)

   :returns: Command object with next state updates


   .. autolink-examples:: think_node
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.nodes
   :collapse:
   
.. autolink-skip:: next
