agents.rag.simple.clean_simple_rag
==================================

.. py:module:: agents.rag.simple.clean_simple_rag

.. autoapi-nested-parse::

   SimpleRAG - Clean MultiAgent Implementation.

   This is the CORRECT SimpleRAG implementation using the clean MultiAgent pattern.

   Architecture:
       SimpleRAG extends MultiAgent from clean.py
       agents = [BaseRAGAgent, SimpleAgent]  # List initialization (converted to dict)
       execution_mode = "sequential" (default)

       Flow: BaseRAGAgent retrieves documents → SimpleAgent generates answers

   Key Features:
   - Uses the clean MultiAgent pattern from haive.agents.multi.clean
   - Proper list initialization: MultiAgent(agents=[retriever, generator])
   - Sequential execution (retriever → generator)
   - No custom routing needed - uses intelligent routing
   - Proper Pydantic patterns with no __init__ overrides
   - Comprehensive field validation and documentation

   .. rubric:: Examples

   Basic usage::

       from haive.agents.rag.simple.clean_simple_rag import SimpleRAG
       from haive.core.engine.aug_llm import AugLLMConfig
       from haive.core.engine.vectorstore import VectorStoreConfig

       rag = SimpleRAG(
           name="qa_assistant",
           retriever_config=VectorStoreConfig(vector_store=vector_store),
           llm_config=AugLLMConfig(temperature=0.7),
           top_k=5
       )

       result = await rag.arun("What is machine learning?")

   With structured output::

       class QAResponse(BaseModel):
           answer: str
           sources: List[str]
           confidence: float

       rag = SimpleRAG(
           name="structured_qa",
           retriever_config=retriever_config,
           llm_config=llm_config,
           structured_output_model=QAResponse
       )

   From documents::

       rag = SimpleRAG.from_documents(
           documents=my_documents,
           embedding_config=embedding_config,
           llm_config=AugLLMConfig()
       )


   .. autolink-examples:: agents.rag.simple.clean_simple_rag
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.simple.clean_simple_rag.SimpleRAGAgent


Classes
-------

.. autoapisummary::

   agents.rag.simple.clean_simple_rag.SimpleRAG


Module Contents
---------------

.. py:class:: SimpleRAG

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   SimpleRAG - Clean MultiAgent implementation with BaseRAGAgent + SimpleAgent.

   This is the proper SimpleRAG following the clean MultiAgent pattern:

   Architecture:
       - Extends MultiAgent from clean.py
       - agents = [BaseRAGAgent, SimpleAgent] (list initialization)
       - execution_mode = "sequential" (default intelligent routing)
       - No custom routing needed - uses BaseGraph intelligent routing

   Flow:
       1. BaseRAGAgent retrieves relevant documents from vector store
       2. SimpleAgent generates answers from retrieved documents
       3. MultiAgent handles the sequential coordination automatically

   This leverages the full MultiAgent infrastructure:
       - Proper state management via MultiAgentState
       - Graph building and execution
       - Sequential routing and coordination
       - Error handling and debugging

   .. rubric:: Examples

   Basic RAG::

       rag = SimpleRAG(
           name="qa_system",
           retriever_config=VectorStoreConfig(vector_store=vector_store),
           llm_config=AugLLMConfig(temperature=0.7),
           top_k=5
       )

       result = await rag.arun("What is machine learning?")

   With structured output::

       class QAResponse(BaseModel):
           answer: str
           sources: List[str]
           confidence: float

       rag = SimpleRAG(
           name="structured_qa",
           retriever_config=retriever_config,
           llm_config=llm_config,
           structured_output_model=QAResponse
       )

   From documents::

       rag = SimpleRAG.from_documents(
           documents=my_documents,
           embedding_config=embedding_config,
           llm_config=AugLLMConfig()
       )


   .. autolink-examples:: SimpleRAG
      :collapse:

   .. py:method:: __repr__() -> str

      String representation showing clean MultiAgent structure.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any], debug: bool = False, **kwargs) -> Any
      :async:


      Execute RAG pipeline using clean MultiAgent sequential execution.

      This leverages the clean MultiAgent infrastructure for proper sequential
      execution of retriever → generator with full state management.

      :param input_data: Query string or structured input dict with 'query' field
      :param debug: Enable debug logging and detailed output
      :param \*\*kwargs: Additional execution parameters

      :returns: Generated response from the generator agent

      :raises ValueError: If input validation fails
      :raises RuntimeError: If pipeline execution fails


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], embedding_config: Any, llm_config: haive.core.engine.aug_llm.AugLLMConfig, name: str = 'SimpleRAG_from_docs', **kwargs) -> SimpleRAG
      :classmethod:


      Create SimpleRAG from a list of documents.

      :param documents: List of documents to create vector store from
      :param embedding_config: Embedding configuration for vector store
      :param llm_config: LLM configuration for answer generation
      :param name: Name for the RAG agent
      :param \*\*kwargs: Additional configuration parameters

      :returns: Configured SimpleRAG instance


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: from_vectorstore(vector_store_config: haive.core.engine.vectorstore.VectorStoreConfig, llm_config: haive.core.engine.aug_llm.AugLLMConfig, name: str = 'SimpleRAG_from_vs', **kwargs) -> SimpleRAG
      :classmethod:


      Create SimpleRAG from existing vector store configuration.

      :param vector_store_config: Vector store configuration
      :param llm_config: LLM configuration for answer generation
      :param name: Name for the RAG agent
      :param \*\*kwargs: Additional configuration parameters

      :returns: Configured SimpleRAG instance


      .. autolink-examples:: from_vectorstore
         :collapse:


   .. py:method:: generate_answer(query: str, documents: list[langchain_core.documents.Document], **kwargs) -> Any
      :async:


      Generate answer using the generator agent.

      :param query: Original query
      :param documents: Retrieved documents for context
      :param \*\*kwargs: Additional generation parameters

      :returns: Generated answer (format depends on structured_output_model)


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: get_generator_agent() -> haive.agents.simple.agent.SimpleAgent

      Get the generator agent from the agents dict.


      .. autolink-examples:: get_generator_agent
         :collapse:


   .. py:method:: get_rag_info() -> dict[str, Any]

      Get comprehensive information about the RAG configuration.


      .. autolink-examples:: get_rag_info
         :collapse:


   .. py:method:: get_retriever_agent() -> haive.agents.rag.base.agent.BaseRAGAgent

      Get the retriever agent from the agents dict.


      .. autolink-examples:: get_retriever_agent
         :collapse:


   .. py:method:: retrieve_documents(query: str, k: int | None = None, score_threshold: float | None = None, **kwargs) -> list[langchain_core.documents.Document]
      :async:


      Retrieve documents using the retriever agent.

      :param query: Query string for retrieval
      :param k: Number of documents to retrieve (defaults to self.top_k)
      :param score_threshold: Minimum similarity score (defaults to self.similarity_threshold)
      :param \*\*kwargs: Additional retrieval parameters

      :returns: List of retrieved documents


      .. autolink-examples:: retrieve_documents
         :collapse:


   .. py:method:: setup_rag_agents() -> SimpleRAG

      Setup the retriever and generator agents using the clean MultiAgent pattern.


      .. autolink-examples:: setup_rag_agents
         :collapse:


   .. py:method:: validate_context_template(v: str) -> str
      :classmethod:


      Validate context template has required placeholders.


      .. autolink-examples:: validate_context_template
         :collapse:


   .. py:attribute:: context_template
      :type:  str
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: retriever_config
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig
      :value: None



   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: system_prompt_template
      :type:  str
      :value: None



   .. py:attribute:: top_k
      :type:  int
      :value: None



.. py:data:: SimpleRAGAgent

