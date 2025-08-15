agents.rag.simple.multi_agent_simple_rag
========================================

.. py:module:: agents.rag.simple.multi_agent_simple_rag

.. autoapi-nested-parse::

   SimpleRAG - Proper MultiAgent Implementation.

   This is the CORRECT SimpleRAG implementation using the proper MultiAgent pattern:
       SimpleRAG extends MultiAgent with agents={"retriever": BaseRAGAgent, "generator": SimpleAgent}

   The key insight is that SimpleRAG IS a MultiAgent that coordinates two specific agents:
   1. BaseRAGAgent: Handles document retrieval
   2. SimpleAgent: Generates answers from documents

   This follows the MultiAgent[AgentsT] pattern where:
   - SimpleRAG extends MultiAgent
   - agents field contains the two agents
   - execution_mode="sequence" for retrieval → generation flow

   .. rubric:: Examples

   Basic usage::

       rag = SimpleRAG(
           name="qa_system",
           retriever_config=VectorStoreConfig(vector_store=vector_store),
           llm_config=AugLLMConfig(temperature=0.7),
           top_k=5
       )

       result = await rag.arun("What is machine learning?")

   From documents::

       rag = SimpleRAG.from_documents(
           documents=my_documents,
           embedding_config=embedding_config,
           llm_config=AugLLMConfig()
       )


   .. autolink-examples:: agents.rag.simple.multi_agent_simple_rag
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.simple.multi_agent_simple_rag.SimpleRAGAgent


Classes
-------

.. autoapisummary::

   agents.rag.simple.multi_agent_simple_rag.SimpleRAG


Module Contents
---------------

.. py:class:: SimpleRAG

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   SimpleRAG - MultiAgent coordinating BaseRAGAgent and SimpleAgent.

   This is the proper implementation of SimpleRAG following the MultiAgent pattern:

   Structure:
       SimpleRAG extends MultiAgent
       agents = {
           "retriever": BaseRAGAgent,  # Handles document retrieval
           "generator": SimpleAgent    # Generates answers from documents
       }
       execution_mode = "sequence"  # retriever → generator

   The MultiAgent pattern means:
   - SimpleRAG IS a MultiAgent
   - It contains other agents in its agents field
   - It coordinates their execution in sequence
   - It uses the proper graph building and state management

   This is much cleaner than custom composition because it leverages
   the existing MultiAgent infrastructure for routing, state management,
   and execution patterns.

   .. rubric:: Examples

   Basic RAG::

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


   .. autolink-examples:: SimpleRAG
      :collapse:

   .. py:method:: __repr__() -> str

      String representation showing MultiAgent structure.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any], debug: bool = False, **kwargs) -> Any
      :async:


      Execute RAG pipeline using MultiAgent sequential execution.

      This leverages the MultiAgent infrastructure but processes the results
      to provide RAG-specific functionality like document extraction and context formatting.

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

      Get the generator agent.


      .. autolink-examples:: get_generator_agent
         :collapse:


   .. py:method:: get_rag_info() -> dict[str, Any]

      Get information about the RAG configuration.


      .. autolink-examples:: get_rag_info
         :collapse:


   .. py:method:: get_retriever_agent() -> haive.agents.rag.base.agent.BaseRAGAgent

      Get the retriever agent.


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

      Setup the retriever and generator agents after validation.


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

