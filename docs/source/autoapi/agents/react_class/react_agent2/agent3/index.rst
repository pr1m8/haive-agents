agents.react_class.react_agent2.agent3
======================================

.. py:module:: agents.react_class.react_agent2.agent3


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent2.agent3.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.agent3.ReactAgent
   agents.react_class.react_agent2.agent3.ReactAgentConfig
   agents.react_class.react_agent2.agent3.ReactAgentState


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.agent3.create_react_agent
   agents.react_class.react_agent2.agent3.from_tools
   agents.react_class.react_agent2.agent3.run
   agents.react_class.react_agent2.agent3.search
   agents.react_class.react_agent2.agent3.search
   agents.react_class.react_agent2.agent3.setup_workflow
   agents.react_class.react_agent2.agent3.structured_output_node


Module Contents
---------------

.. py:class:: ReactAgent

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`ReactAgentConfig`\ ]


   ReAct agent implementation with tool usage and routing capabilities.


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _create_structured_output_node_config() -> haive.core.graph.node.config.NodeConfig

      Create the configuration for the structured output node.


      .. autolink-examples:: _create_structured_output_node_config
         :collapse:


   .. py:method:: _route_to_specific_tools(state: ReactAgentState) -> str | list[langgraph.types.Send] | Literal['END']

      Route to specific tool nodes based on tool calls.


      .. autolink-examples:: _route_to_specific_tools
         :collapse:


   .. py:method:: _should_continue(state: ReactAgentState) -> str | list[langgraph.types.Send] | Literal['END']

      Determine if we should continue to tools or end.


      .. autolink-examples:: _should_continue
         :collapse:


   .. py:method:: run(input_text: str | dict | ReactAgentState)

      Run the agent with the given input.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the agent workflow with nodes and edges.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the ReAct agent.


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:method:: from_tools(tools: list[langchain_core.tools.BaseTool], system_prompt: str = 'You are a helpful assistant with access to tools.', max_iterations: int = 5, model: str = 'gpt-4o', temperature: float = 0.7, parallel_tool_execution: bool = True, tool_routing: dict[str, str] | None = None, structured_output_model: type[pydantic.BaseModel] | None = None, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig from a list of tools.


      .. autolink-examples:: from_tools
         :collapse:


   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: model
      :type:  str
      :value: None



   .. py:attribute:: parallel_tool_execution
      :type:  bool
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: system_prompt
      :type:  str
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



   .. py:attribute:: tool_names
      :type:  list[str]
      :value: None



   .. py:attribute:: tool_routing
      :type:  dict[str, str]
      :value: None



.. py:class:: ReactAgentState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State schema for ReAct agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactAgentState
      :collapse:

   .. py:attribute:: iteration_count
      :type:  int
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



   .. py:attribute:: remaining_iterations
      :type:  int
      :value: None



   .. py:attribute:: status
      :type:  str
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



.. py:function:: create_react_agent(tools: list[langchain_core.tools.BaseTool], system_prompt: str = 'You are a helpful assistant with access to tools.', max_iterations: int = 5, model: str = 'gpt-4o', temperature: float = 0.7, parallel_tool_execution: bool = True, tool_routing: dict[str, str] | None = None, structured_output_model: type[pydantic.BaseModel] | None = None, name: str | None = None) -> ReactAgent

   Create a ReAct agent with the specified configuration.


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: from_tools(tools, **kwargs)

   Module-level from_tools function.


   .. autolink-examples:: from_tools
      :collapse:

.. py:function:: run(agent, input_data)

   Module-level run function.


   .. autolink-examples:: run
      :collapse:

.. py:function:: search(query: str) -> str

   Search for information about a topic.


   .. autolink-examples:: search
      :collapse:

.. py:function:: search(query)

   Module-level search function.


   .. autolink-examples:: search
      :collapse:

.. py:function:: setup_workflow()

   Module-level setup_workflow function.


   .. autolink-examples:: setup_workflow
      :collapse:

.. py:function:: structured_output_node(state)

   Module-level structured_output_node function.


   .. autolink-examples:: structured_output_node
      :collapse:

.. py:data:: logger

