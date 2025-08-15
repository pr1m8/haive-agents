agents.react_class.react_agent.agent
====================================

.. py:module:: agents.react_class.react_agent.agent


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent.agent.default_react_should_continue_output_dict


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent.agent.ReactAgent
   agents.react_class.react_agent.agent.ReactAgentConfig


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent.agent.chat_react_agent
   agents.react_class.react_agent.agent.chat_react_agent_with_tool_node
   agents.react_class.react_agent.agent.create_react_agent
   agents.react_class.react_agent.agent.run_react_agent
   agents.react_class.react_agent.agent.should_continue


Module Contents
---------------

.. py:class:: ReactAgent(config: ReactAgentConfig = ReactAgentConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`ReactAgentConfig`\ ]


   .. py:method:: _initialize_tool_node()

      Initialize ToolNode if required.


      .. autolink-examples:: _initialize_tool_node
         :collapse:


   .. py:method:: chat() -> None

      Interactive chat loop.


      .. autolink-examples:: chat
         :collapse:


   .. py:method:: default_agent_node(state: haive.agents.react_class.react_agent.state.ReactAgentState) -> langgraph.types.Command

      Default implementation of the agent node.


      .. autolink-examples:: default_agent_node
         :collapse:


   .. py:method:: default_agent_node_without_tool_node(state: haive.agents.react_class.react_agent.state.ReactAgentState) -> langgraph.types.Command

      Agent node implementation when ToolNode is not used.


      .. autolink-examples:: default_agent_node_without_tool_node
         :collapse:


   .. py:method:: replace_agent_node(new_agent_node: collections.abc.Callable)

      Replace the agent node function.


      .. autolink-examples:: replace_agent_node
         :collapse:


   .. py:method:: run(input_text: str)

      Run the agent.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Configure the workflow graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: structured_output_agent_node(state: haive.agents.react_class.react_agent.state.ReactAgentState) -> langgraph.types.Command

      Agent node implementation when structured output is required.


      .. autolink-examples:: structured_output_agent_node
         :collapse:


   .. py:method:: visualize_graph(output_name: str = 'react_agent_graph.png')

      Visualize the workflow graph.


      .. autolink-examples:: visualize_graph
         :collapse:


   .. py:attribute:: agent_node_fn


   .. py:attribute:: aug_llm_model


   .. py:attribute:: conditional_routing_function_output_dict
      :value: None



   .. py:attribute:: core_routing_function
      :value: None



   .. py:attribute:: create_tool_node


   .. py:attribute:: llm_tools
      :value: []



   .. py:attribute:: node_name
      :value: None



   .. py:attribute:: tool_node
      :value: None



   .. py:attribute:: tool_node_tools


.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   .. py:method:: build_agent() -> ReactAgent


   .. py:method:: ensure_list(v) -> Any
      :classmethod:


      Ensure tools are always a list.


      .. autolink-examples:: ensure_list
         :collapse:


   .. py:method:: ensure_serializable(v) -> Any
      :classmethod:


      Ensure structured output schema is serializable.


      .. autolink-examples:: ensure_serializable
         :collapse:


   .. py:method:: validate_engine(v) -> Any
      :classmethod:


      Ensure `engine` is always provided and valid.


      .. autolink-examples:: validate_engine
         :collapse:


   .. py:attribute:: aug_llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: conditional_routing_function_output_dict
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: core_routing_function
      :type:  collections.abc.Callable
      :value: None



   .. py:attribute:: default_agent_node
      :type:  collections.abc.Callable | None
      :value: None



   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: node_name
      :type:  str
      :value: None



   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig
      :value: None



   .. py:attribute:: should_compile
      :type:  bool
      :value: None



   .. py:attribute:: should_setup_workflow
      :type:  bool
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel] | dict[str, Any] | Any
      :value: None



   .. py:attribute:: structured_output_model
      :type:  pydantic.BaseModel | None
      :value: None



   .. py:attribute:: tool_node_tools
      :type:  list[langchain_core.tools.Tool | langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool]
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.Tool | langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool]
      :value: None



   .. py:attribute:: visualize_graph_output_name
      :type:  str | None
      :value: None



.. py:function:: chat_react_agent(config: ReactAgentConfig = ReactAgentConfig())

   Start a chat session with ReactAgent.


   .. autolink-examples:: chat_react_agent
      :collapse:

.. py:function:: chat_react_agent_with_tool_node(config: ReactAgentConfig = ReactAgentConfig())

   Start a chat session with ReactAgent.


   .. autolink-examples:: chat_react_agent_with_tool_node
      :collapse:

.. py:function:: create_react_agent(config: ReactAgentConfig = ReactAgentConfig()) -> ReactAgent

   Factory function to create a ReactAgent.


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: run_react_agent(input_text: str, config: ReactAgentConfig = ReactAgentConfig())

   Execute ReactAgent with a given input.


   .. autolink-examples:: run_react_agent
      :collapse:

.. py:function:: should_continue(state: haive.agents.react_class.react_agent.state.ReactAgentState) -> str

.. py:data:: default_react_should_continue_output_dict

