agents.react_class.react_agent2.dynamic_agent
=============================================

.. py:module:: agents.react_class.react_agent2.dynamic_agent

.. autoapi-nested-parse::

   Dynamic React Agent - an extension of React agent with tool selection capabilities.


   .. autolink-examples:: agents.react_class.react_agent2.dynamic_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.react_class.react_agent2.dynamic_agent.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.dynamic_agent.DynamicReactAgent
   agents.react_class.react_agent2.dynamic_agent.DynamicReactAgentConfig
   agents.react_class.react_agent2.dynamic_agent.DynamicReactAgentState


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.dynamic_agent.create_dynamic_react_agent


Module Contents
---------------

.. py:class:: DynamicReactAgent(config: DynamicReactAgentConfig)

   Bases: :py:obj:`haive.agents.react_class.react_agent2.agent2.ReactAgent`


   A React agent with dynamic tool selection.

   This agent extends the React pattern with dynamic tool selection,
   making it efficient when dealing with a large number of tools.

   Initialize the dynamic react agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicReactAgent
      :collapse:

   .. py:method:: _create_fixed_tool_node()

      Create a fixed version of the tool node that handles tool_call_id properly.


      .. autolink-examples:: _create_fixed_tool_node
         :collapse:


   .. py:method:: _create_tool_selection_function(state)

      Create a function that selects tools based on the context.


      .. autolink-examples:: _create_tool_selection_function
         :collapse:


   .. py:method:: _initialize_in_memory_vector_store(tool_documents: list[langchain_core.documents.Document])

      Initialize an in-memory vector store with the tool documents.


      .. autolink-examples:: _initialize_in_memory_vector_store
         :collapse:


   .. py:method:: register_tools(tools: list[langchain_core.tools.BaseTool]) -> None

      Register tools with the agent and create tool embeddings.

      :param tools: List of tools to register


      .. autolink-examples:: register_tools
         :collapse:


   .. py:method:: run(input_data: str | list[str] | dict[str, Any] | pydantic.BaseModel, **kwargs) -> dict[str, Any]

      Run the agent with the given input.

      :param input_data: Input data in various formats
      :param \*\*kwargs: Additional runtime configuration

      :returns: Final state or output


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow with dynamic tool selection.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: _vector_store
      :value: None



   .. py:attribute:: tool_registry


   .. py:attribute:: tools


   .. py:property:: vector_store
      :type: Any


      Get the vector store property.

      .. autolink-examples:: vector_store
         :collapse:


   .. py:attribute:: vector_store_config


.. py:class:: DynamicReactAgentConfig

   Bases: :py:obj:`haive.agents.react_class.react_agent2.config2.ReactAgentConfig`


   Configuration for a React agent with dynamic tool selection.

   This agent can handle a large number of tools by dynamically selecting
   which tools to make available to the LLM based on the context.


   .. autolink-examples:: DynamicReactAgentConfig
      :collapse:

   .. py:method:: from_tools(tools: list[langchain_core.tools.BaseTool], system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, name: str | None = None, max_tools_per_turn: int = 5, max_iterations: int = 10, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, use_memory: bool = True, visualize: bool = True, repeat_selection: bool = True, **kwargs) -> DynamicReactAgentConfig
      :classmethod:


      Create a DynamicReactAgentConfig from a list of tools.

      :param tools: List of tools to use
      :param system_prompt: Optional system prompt
      :param model: Model name
      :param temperature: Temperature for generation
      :param name: Optional agent name
      :param max_tools_per_turn: Maximum number of tools to select per turn
      :param max_iterations: Maximum iterations for React agent
      :param response_format: Optional structured output model
      :param use_memory: Whether to use memory
      :param visualize: Whether to visualize the graph
      :param repeat_selection: Whether to repeat tool selection after each tool invocation
      :param \*\*kwargs: Additional kwargs for the config

      :returns: DynamicReactAgentConfig instance


      .. autolink-examples:: from_tools
         :collapse:


   .. py:attribute:: max_tools_per_turn
      :type:  int
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: repeat_selection
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: tool_documents
      :type:  list[langchain_core.documents.Document] | None
      :value: None



   .. py:attribute:: tool_embedding_model
      :type:  str
      :value: None



   .. py:attribute:: tool_selection_node_name
      :type:  str
      :value: None



   .. py:attribute:: vector_store_config
      :type:  haive.core.models.vectorstore.base.VectorStoreConfig | None
      :value: None



.. py:class:: DynamicReactAgentState

   Bases: :py:obj:`haive.agents.react_class.react_agent2.state2.ReactAgentState`


   Extended schema for dynamic tool selection.


   .. autolink-examples:: DynamicReactAgentState
      :collapse:

   .. py:attribute:: model_config


   .. py:attribute:: selected_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: tool_call_id
      :type:  str | None
      :value: None



   .. py:attribute:: tool_registry
      :type:  dict[str, Any]
      :value: None



.. py:function:: create_dynamic_react_agent(tools: list[langchain_core.tools.BaseTool], system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, name: str | None = None, max_tools_per_turn: int = 5, max_iterations: int = 10, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, use_memory: bool = True, visualize: bool = True, repeat_selection: bool = True, vector_store_config: haive.core.models.vectorstore.base.VectorStoreConfig | None = None, tool_documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> DynamicReactAgent

   Create a dynamic react agent with minimal configuration.

   :param tools: List of tools the agent can use
   :param system_prompt: Optional system prompt
   :param model: Model name to use
   :param temperature: Temperature for generation
   :param name: Optional agent name
   :param max_tools_per_turn: Maximum number of tools to select per turn
   :param max_iterations: Maximum iterations for React agent
   :param response_format: Optional structured output model
   :param use_memory: Whether to use memory
   :param visualize: Whether to visualize the graph
   :param repeat_selection: Whether to repeat tool selection after each tool invocation
   :param vector_store_config: Optional vector store configuration
   :param tool_documents: Optional pre-created tool documents
   :param \*\*kwargs: Additional configuration parameters

   :returns: DynamicReactAgent instance


   .. autolink-examples:: create_dynamic_react_agent
      :collapse:

.. py:data:: logger

