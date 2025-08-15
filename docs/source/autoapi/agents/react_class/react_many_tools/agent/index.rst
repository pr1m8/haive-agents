agents.react_class.react_many_tools.agent
=========================================

.. py:module:: agents.react_class.react_many_tools.agent


Attributes
----------

.. autoapisummary::

   agents.react_class.react_many_tools.agent.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_many_tools.agent.ReactManyToolsAgent


Module Contents
---------------

.. py:class:: ReactManyToolsAgent(config: haive.agents.react_class.react_many_tools.config.ReactManyToolsConfig)

   Bases: :py:obj:`haive.agents.react_class.react.agent.ReactAgent`


   React Agent implementation that can handle many tools efficiently.

   Extends ReactAgent with advanced tool filtering and selection
   to manage large numbers of tools, and integrates RAG capabilities.

   Initialize the agent with its configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactManyToolsAgent
      :collapse:

   .. py:method:: _add_system_message_node(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Add a node for adding a system message to the state.


      .. autolink-examples:: _add_system_message_node
         :collapse:


   .. py:method:: _create_tool_embeddings() -> None

      Create embeddings for tools for semantic filtering.


      .. autolink-examples:: _create_tool_embeddings
         :collapse:


   .. py:method:: _extract_query(state: dict[str, Any]) -> dict[str, Any]

      Extract query from messages and store in state.

      :param state: Current state with messages

      :returns: Updated state with extracted query


      .. autolink-examples:: _extract_query
         :collapse:


   .. py:method:: _extract_query_from_state(state: dict[str, Any]) -> str

      Extract query from state.

      :param state: Current state

      :returns: Extracted query


      .. autolink-examples:: _extract_query_from_state
         :collapse:


   .. py:method:: _filter_tools(state: dict[str, Any]) -> dict[str, Any]

      Filter tools based on the query.

      :param state: Current state with query or messages

      :returns: Updated state with filtered tools


      .. autolink-examples:: _filter_tools
         :collapse:


   .. py:method:: _filter_tools_categorical(query: str) -> list[str]

      Filter tools using category matching.

      :param query: User query

      :returns: List of tool names


      .. autolink-examples:: _filter_tools_categorical
         :collapse:


   .. py:method:: _filter_tools_keyword(query: str) -> list[str]

      Filter tools using keyword matching.

      :param query: User query

      :returns: List of tool names


      .. autolink-examples:: _filter_tools_keyword
         :collapse:


   .. py:method:: _filter_tools_semantic(query: str) -> list[str]

      Filter tools using semantic similarity.

      :param query: User query

      :returns: List of tool names


      .. autolink-examples:: _filter_tools_semantic
         :collapse:


   .. py:method:: _generate_answer(state: dict[str, Any]) -> langgraph.types.Command

      Generate an answer based on retrieved documents.

      :param state: Current state with query and retrieved documents

      :returns: Command with generated answer


      .. autolink-examples:: _generate_answer
         :collapse:


   .. py:method:: _initialize_rag_components() -> None

      Initialize RAG components from configuration.


      .. autolink-examples:: _initialize_rag_components
         :collapse:


   .. py:method:: _retrieve_documents(state: dict[str, Any]) -> langgraph.types.Command

      Retrieve relevant documents based on the query.

      :param state: Current state with query

      :returns: Command for updating state with retrieved documents


      .. autolink-examples:: _retrieve_documents
         :collapse:


   .. py:method:: _setup_llm_node(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Set up the LLM node with filtered tool binding.


      .. autolink-examples:: _setup_llm_node
         :collapse:


   .. py:method:: _should_retrieve_documents(state: dict[str, Any]) -> str

      Decide whether to retrieve documents based on state.

      :param state: Current state

      :returns: Next node name


      .. autolink-examples:: _should_retrieve_documents
         :collapse:


   .. py:method:: run(input_data: str | dict[str, Any], **kwargs) -> dict[str, Any]

      Run the agent with dynamic tool filtering and RAG capabilities.

      :param input_data: Input query or state
      :param \*\*kwargs: Additional parameters

      :returns: Result from agent execution


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow with tool filtering nodes and RAG integration.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: config


   .. py:property:: retriever
      :type: Any


      Lazy initialization of retriever.

      .. autolink-examples:: retriever
         :collapse:


.. py:data:: logger

