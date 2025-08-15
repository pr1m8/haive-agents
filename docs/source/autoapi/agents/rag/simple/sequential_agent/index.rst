agents.rag.simple.sequential_agent
==================================

.. py:module:: agents.rag.simple.sequential_agent

.. autoapi-nested-parse::

   SimpleRAG - Sequential MultiAgent Implementation (BaseRAG → SimpleAgent).

   This is the correct SimpleRAG implementation following the sequential multi-agent pattern:
       SimpleRAG = Sequential[BaseRAGAgent, SimpleAgent]

   Architecture:
   1. **BaseRAGAgent**: Performs document retrieval from vector store
   2. **SimpleAgent**: Generates structured answers from retrieved documents
   3. **Sequential Execution**: BaseRAG output → SimpleAgent input

   Key Features:
   - **Sequential Multi-Agent Pattern**: Proper composition of specialized agents
   - **Pydantic Best Practices**: No __init__ overrides, field validation, inheritance
   - **Type Safety**: Full type hints and proper agent composition
   - **Real Component Integration**: Uses actual BaseRAGAgent and SimpleAgent
   - **Structured Output**: Support for custom response models
   - **Comprehensive Documentation**: Google-style docstrings with examples

   Design Philosophy:
   - **Composition over Monolith**: Uses existing proven agents
   - **Clear Separation of Concerns**: Retrieval vs Generation
   - **Reusable Components**: Each agent can be used independently
   - **Testable Architecture**: Easy to test each component separately

   .. rubric:: Examples

   Basic usage::

       from haive.agents.rag.simple import SimpleRAG
       from haive.core.engine.aug_llm import AugLLMConfig
       from haive.core.engine.vectorstore import VectorStoreConfig

       rag = SimpleRAG(
           name="qa_assistant",
           retriever_config=VectorStoreConfig(vector_store=your_vector_store),
           llm_config=AugLLMConfig(temperature=0.7),
           top_k=5
       )

       result = await rag.arun("What is machine learning?")

   With structured output::

       class QAResponse(BaseModel):
           answer: str
           sources: list[str]
           confidence: float

       rag = SimpleRAG(
           name="structured_qa",
           retriever_config=retriever_config,
           llm_config=AugLLMConfig(),
           structured_output_model=QAResponse
       )


   .. autolink-examples:: agents.rag.simple.sequential_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.simple.sequential_agent.SimpleRAGAgent


Classes
-------

.. autoapisummary::

   agents.rag.simple.sequential_agent.RAGResponse
   agents.rag.simple.sequential_agent.SimpleRAG


Module Contents
---------------

.. py:class:: RAGResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive RAG response model.

   Contains the generated answer along with comprehensive metadata about
   the retrieval and generation process, including sources, confidence
   scores, and execution metrics.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGResponse
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: retrieval_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieved_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



.. py:class:: SimpleRAG(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   SimpleRAG - Sequential composition of BaseRAGAgent and SimpleAgent.

   This implementation properly composes two specialized agents:
   1. BaseRAGAgent: Handles document retrieval from vector stores
   2. SimpleAgent: Generates answers from retrieved documents

   The sequential flow is: Query → BaseRAG → Documents → SimpleAgent → Answer

   This follows the multi-agent pattern established in the Haive framework
   where complex capabilities are built by composing simpler, focused agents.

   .. rubric:: Examples

   Basic usage::

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

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SimpleRAG
      :collapse:

   .. py:method:: __repr__() -> str

      String representation showing composition.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _extract_documents(retrieval_result: Any) -> list[langchain_core.documents.Document]

      Extract documents from retrieval result.


      .. autolink-examples:: _extract_documents
         :collapse:


   .. py:method:: _extract_query(input_data: str | dict[str, Any]) -> str

      Extract query string from input data.


      .. autolink-examples:: _extract_query
         :collapse:


   .. py:method:: _format_response(query: str, answer: Any, documents: list[langchain_core.documents.Document], execution_time: float, debug: bool = False) -> str | RAGResponse | pydantic.BaseModel

      Format the final response.


      .. autolink-examples:: _format_response
         :collapse:


   .. py:method:: _prepare_context(documents: list[langchain_core.documents.Document], query: str) -> str

      Prepare context from retrieved documents.


      .. autolink-examples:: _prepare_context
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any], debug: bool = False, **kwargs) -> str | RAGResponse | pydantic.BaseModel
      :async:


      Execute RAG pipeline with sequential agent composition.

      Flow:
      1. Extract query from input
      2. Use BaseRAGAgent to retrieve relevant documents
      3. Format documents as context
      4. Use SimpleAgent to generate answer from context
      5. Return formatted response

      :param input_data: Query string or structured input dict with 'query' field
      :param debug: Enable debug logging and detailed output
      :param \*\*kwargs: Additional execution parameters

      :returns:

                - str: Simple answer string (default)
                - RAGResponse: Full response with metadata (if debug=True)
                - BaseModel: Custom structured output (if structured_output_model set)
      :rtype: Generated response - format depends on structured_output_model

      :raises ValueError: If input validation fails
      :raises RuntimeError: If critical pipeline components fail


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


   .. py:method:: get_agent_info() -> dict[str, Any]

      Get information about the composed agents.


      .. autolink-examples:: get_agent_info
         :collapse:


   .. py:method:: run(input_data: str | dict[str, Any], debug: bool = False, **kwargs) -> str | RAGResponse | pydantic.BaseModel

      Synchronous execution wrapper.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_agents() -> SimpleRAG

      Setup internal agent instances after validation.


      .. autolink-examples:: setup_agents
         :collapse:


   .. py:method:: validate_context_template(v: str) -> str
      :classmethod:


      Validate context template has required placeholders.


      .. autolink-examples:: validate_context_template
         :collapse:


   .. py:attribute:: _generator_agent
      :type:  haive.agents.simple.agent.SimpleAgent | None
      :value: None



   .. py:attribute:: _retriever_agent
      :type:  haive.agents.rag.base.agent.BaseRAGAgent | None
      :value: None



   .. py:attribute:: context_template
      :type:  str
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
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

