agents.rag.agentic.react_rag_agent
==================================

.. py:module:: agents.rag.agentic.react_rag_agent

.. autoapi-nested-parse::

   Enhanced ReactAgent with Retriever Node and Routing for Agentic RAG.

   This agent extends ReactAgent to add a dedicated retrieval node to the graph,
   with intelligent routing between tool calls and retrieval based on the query.


   .. autolink-examples:: agents.rag.agentic.react_rag_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.agentic.react_rag_agent.ReactRAGAgent


Module Contents
---------------

.. py:class:: ReactRAGAgent

   Bases: :py:obj:`haive.agents.react.ReactAgent`


   Enhanced ReactAgent with a dedicated retrieval node and intelligent routing.

   This agent extends ReactAgent by adding a retrieval node to the graph that works
   alongside regular tool nodes. The agent can route between:
   1. Regular tool execution (calculator, web search, etc.)
   2. Retrieval from vector store/knowledge base
   3. Both in combination

   The routing is handled by the LLM through a special retriever tool that triggers
   the retrieval node when called.

   .. rubric:: Example

   .. code-block:: python

       # Create ReactRAG agent with both types of tools
       agent = ReactRAGAgent.create_default(
       name="react_rag",
       retriever_config=vector_store_config,
       tools=[calculator_tool, web_search_tool],
       temperature=0.1
       )

       # The agent will intelligently decide whether to:
       # 1. Use retriever for knowledge queries
       # 2. Use tools for computational/action queries
       # 3. Use both when needed

       result = await agent.arun("What is the capital of France?")  # Uses retriever
       result = await agent.arun("Calculate 15 * 23")  # Uses calculator tool
       result = await agent.arun("Search for Python tutorials")  # Uses web search


   .. autolink-examples:: ReactRAGAgent
      :collapse:

   .. py:method:: _create_retriever_tool(retriever_config: haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig) -> langchain_core.tools.Tool
      :staticmethod:


      Create a retriever tool that triggers the retrieval node.

      This tool doesn't actually perform retrieval - it just signals
      that retrieval should happen via the dedicated retrieval node.

      :param retriever_config: The retriever or vector store configuration

      :returns: Tool that triggers the retrieval node


      .. autolink-examples:: _create_retriever_tool
         :collapse:


   .. py:method:: _route_to_retrieval_or_tools(state) -> str

      Route to retrieval node, tool node, or end based on agent output.


      .. autolink-examples:: _route_to_retrieval_or_tools
         :collapse:


   .. py:method:: add_retriever_tool(retriever_config: haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig) -> None

      Add or update the retriever tool and rebuild graph.

      :param retriever_config: New retriever configuration


      .. autolink-examples:: add_retriever_tool
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the enhanced React graph with retrieval node.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_default(**kwargs) -> ReactRAGAgent
      :classmethod:


      Create a default ReactRAG agent with retriever and tools.

      :param \*\*kwargs: Configuration options
                         - name: Agent name
                         - retriever_config: Retriever or vector store config
                         - tools: List of regular tools
                         - temperature: LLM temperature
                         - routing_strategy: How to route between retriever and tools
                         - engine: Custom AugLLMConfig if needed

      :returns: ReactRAGAgent configured for RAG with tools


      .. autolink-examples:: create_default
         :collapse:


   .. py:method:: from_vectorstore(vector_store_config: haive.core.engine.vectorstore.VectorStoreConfig, **kwargs) -> ReactRAGAgent
      :classmethod:


      Create ReactRAG agent from a vector store configuration.

      :param vector_store_config: Vector store configuration
      :param \*\*kwargs: Additional agent configuration

      :returns: ReactRAGAgent with retriever tool


      .. autolink-examples:: from_vectorstore
         :collapse:


   .. py:attribute:: retriever_config
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig | None
      :value: None



   .. py:attribute:: routing_strategy
      :type:  str
      :value: None



   .. py:attribute:: use_retriever_for_knowledge
      :type:  bool
      :value: None



