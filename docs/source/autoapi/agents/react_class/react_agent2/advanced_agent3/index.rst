agents.react_class.react_agent2.advanced_agent3
===============================================

.. py:module:: agents.react_class.react_agent2.advanced_agent3


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent2.advanced_agent3.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.advanced_agent3.AdvancedReactAgent
   agents.react_class.react_agent2.advanced_agent3.AdvancedReactAgentConfig


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.advanced_agent3.add_tool
   agents.react_class.react_agent2.advanced_agent3.create_advanced_react_agent


Module Contents
---------------

.. py:class:: AdvancedReactAgent(config: AdvancedReactAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`AdvancedReactAgentConfig`\ ]


   Advanced React agent with specialized tool routing.

   Features:
   - Tool-specific routing based on tool name
   - Custom processing for different tool types
   - Support for specialized tool nodes
   - Optional tool usage analysis

   Initialize the Advanced React Agent with its configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdvancedReactAgent
      :collapse:

   .. py:method:: _group_tools_by_routing()

      Group tools based on their routing destination.


      .. autolink-examples:: _group_tools_by_routing
         :collapse:


   .. py:method:: add_tool(tool: langchain_core.tools.BaseTool, routing: str | None = None) -> AdvancedReactAgent

      Add a tool to the agent with optional custom routing.

      :param tool: The tool to add
      :param routing: Optional node name for routing this tool

      :returns: Self for chaining


      .. autolink-examples:: add_tool
         :collapse:


   .. py:method:: create_custom_tool_node(node_name: str, processor: collections.abc.Callable) -> AdvancedReactAgent

      Create a custom tool node with a specialized processor.

      :param node_name: Name for the node
      :param processor: Function to process tool results

      :returns: Self for chaining


      .. autolink-examples:: create_custom_tool_node
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow graph with specialized tool routing.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: tool_groups


   .. py:attribute:: tool_nodes


   .. py:attribute:: tools


.. py:class:: AdvancedReactAgentConfig

   Bases: :py:obj:`haive.agents.react_class.react_agent2.config2.ReactAgentConfig`


   Extended configuration for the Advanced React Agent.


   .. autolink-examples:: AdvancedReactAgentConfig
      :collapse:

   .. py:attribute:: agent_node_name
      :type:  str
      :value: None



   .. py:attribute:: analyze_tool_usage
      :type:  bool
      :value: None



   .. py:attribute:: default_tool_node_name
      :type:  str
      :value: None



   .. py:attribute:: tool_processors
      :type:  dict[str, collections.abc.Callable]
      :value: None



   .. py:attribute:: tool_routing
      :type:  dict[str, str]
      :value: None



.. py:function:: add_tool(agent, tool)

   Module-level add_tool function.


   .. autolink-examples:: add_tool
      :collapse:

.. py:function:: create_advanced_react_agent(system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, tools: list[langchain_core.tools.BaseTool] | None = None, tool_routing: dict[str, str] | None = None, name: str | None = None, structured_output_model: type[pydantic.BaseModel] | None = None, **kwargs) -> AdvancedReactAgent

   Create an advanced React agent with tool-specific routing.

   :param system_prompt: Optional system prompt
   :param model: Model name to use
   :param temperature: Temperature for generation
   :param tools: List of tools to use
   :param tool_routing: Mapping from tool names to node names
   :param name: Optional name for the agent
   :param structured_output_model: Optional schema for structured output
   :param \*\*kwargs: Additional configuration parameters

   :returns: AdvancedReactAgent instance


   .. autolink-examples:: create_advanced_react_agent
      :collapse:

.. py:data:: logger

