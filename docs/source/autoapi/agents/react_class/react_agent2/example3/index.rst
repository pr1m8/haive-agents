agents.react_class.react_agent2.example3
========================================

.. py:module:: agents.react_class.react_agent2.example3


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent2.example3.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.example3.ReactAgent
   agents.react_class.react_agent2.example3.ReactAgentConfig
   agents.react_class.react_agent2.example3.ReactAgentSchema
   agents.react_class.react_agent2.example3.ReactAgentSchemaWithStructuredResponse


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.example3.create_react_agent
   agents.react_class.react_agent2.example3.tools_condition


Module Contents
---------------

.. py:class:: ReactAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   A React agent implementing the Reasoning-Action-Observation pattern.

   This agent extends SimpleAgent with:
   1. Tool execution capability
   2. A router to determine when to use tools vs. finish
   3. Optional structured output generation


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _create_router_function() -> collections.abc.Callable

      Create the router function for determining next steps.


      .. autolink-examples:: _create_router_function
         :collapse:


   .. py:method:: _create_structured_output_node() -> collections.abc.Callable

      Create a node that generates structured output.


      .. autolink-examples:: _create_structured_output_node
         :collapse:


   .. py:method:: _prepare_input(input_data: Any) -> dict[str, Any]

      Prepare input data for the agent.


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _route_based_on_messages(state: ReactAgentSchema) -> str | langgraph.types.Send | list[langgraph.types.Send]

      Determine the routing based on message content.

      :param state: Current state

      :returns: "tools", "structured_response", "end", or Send objects
      :rtype: Routing decision


      .. autolink-examples:: _route_based_on_messages
         :collapse:


   .. py:method:: _setup_tool_nodes(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Set up individual tool nodes for the v2 graph version.


      .. autolink-examples:: _setup_tool_nodes
         :collapse:


   .. py:method:: run(input_data: Any) -> dict[str, Any]

      Run the agent with the given input.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the React agent workflow graph.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgentConfig`


   Configuration for a React agent, extending SimpleAgentConfig.

   This agent implements the ReAct pattern with Tool usage:
   - Reasoning (R): LLM reasoning step
   - Action (A): Tool execution
   - Observation (O): Tool response processing


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:method:: from_tools_and_llm(tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | collections.abc.Callable], model: str = 'gpt-4o', temperature: float = 0.7, system_prompt: str | None = None, name: str | None = None, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig from tools and an LLM.

      :param tools: List of tools to use
      :param model: Model name to use
      :param temperature: Temperature for generation
      :param system_prompt: Optional system prompt text
      :param name: Optional name for the agent
      :param response_format: Optional schema for structured output
      :param \*\*kwargs: Additional kwargs for configuration

      :returns: ReactAgentConfig instance


      .. autolink-examples:: from_tools_and_llm
         :collapse:


   .. py:attribute:: interrupt_after
      :type:  list[str] | None
      :value: None



   .. py:attribute:: interrupt_before
      :type:  list[str] | None
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: response_format
      :type:  type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: router_node_name
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: tool_node_name
      :type:  str
      :value: None



   .. py:attribute:: tool_routing
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | collections.abc.Callable | haive.core.graph.tool_config.ToolConfig]
      :value: None



   .. py:attribute:: version
      :type:  Literal['v1', 'v2']
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:class:: ReactAgentSchema

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgentState`


   Schema for React Agent State, extending SimpleAgentSchema.


   .. autolink-examples:: ReactAgentSchema
      :collapse:

   .. py:attribute:: current_step
      :type:  int
      :value: None



   .. py:attribute:: is_last_step
      :type:  bool
      :value: None



   .. py:attribute:: remaining_steps
      :type:  int
      :value: None



   .. py:attribute:: tool_results
      :type:  list[dict[str, Any]]
      :value: None



.. py:class:: ReactAgentSchemaWithStructuredResponse

   Bases: :py:obj:`ReactAgentSchema`


   Schema for React Agent with structured response.


   .. autolink-examples:: ReactAgentSchemaWithStructuredResponse
      :collapse:

   .. py:attribute:: structured_response
      :type:  Any
      :value: None



.. py:function:: create_react_agent(tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | collections.abc.Callable], model: str = 'gpt-4o', temperature: float = 0.7, system_prompt: str | None = None, name: str | None = None, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, max_iterations: int = 10, checkpointer: langgraph.types.Checkpointer | None = None, store: langgraph.store.base.BaseStore | None = None, interrupt_before: list[str] | None = None, interrupt_after: list[str] | None = None, debug: bool = False, version: Literal['v1', 'v2'] = 'v1', visualize: bool = True, tool_routing: dict[str, str] | None = None, save_history: bool = True, output_dir: str | None = None, **kwargs) -> ReactAgent

   Create a React agent that follows the reasoning-action-observation pattern.

   :param tools: List of tools available to the agent
   :param model: LLM model name to use
   :param temperature: Temperature for generation
   :param system_prompt: System prompt text
   :param name: Optional name for the agent
   :param response_format: Schema for structured output
   :param max_iterations: Maximum number of reasoning steps
   :param checkpointer: Optional checkpointer for persistence
   :param store: Optional store for cross-thread data
   :param interrupt_before: List of node names to interrupt before
   :param interrupt_after: List of node names to interrupt after
   :param debug: Whether to enable debug mode
   :param version: Graph version (v1 or v2)
   :param visualize: Whether to generate graph visualization
   :param tool_routing: Custom routing map for tools
   :param save_history: Whether to save state history
   :param output_dir: Directory for output files
   :param \*\*kwargs: Additional configuration parameters

   :returns: ReactAgent instance


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: tools_condition(state: dict[str, Any], messages_key: str = 'messages') -> Literal['tools', 'end']

   Determine if the state should route to tools or end based on the last message.

   :param state: State to check for tool calls
   :param messages_key: Key to find messages in state

   :returns: "tools" if tool calls present, "end" otherwise


   .. autolink-examples:: tools_condition
      :collapse:

.. py:data:: logger

