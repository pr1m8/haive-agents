agents.rag.agentic.agent
========================

.. py:module:: agents.rag.agentic.agent

.. autoapi-nested-parse::

   Agentic RAG Agent - ReAct + Retrieval with Proper Haive Patterns.

   This implementation follows the LangChain/LangGraph agentic RAG tutorial but uses
   proper Haive base agent infrastructure:
   - Inherits from ReActAgent for reasoning/acting patterns
   - Uses ToolRouteMixin for automatic tool routing
   - Proper Pydantic patterns (no __init__, model validators)
   - Generic type safety with bounds
   - Multiple engines (LLM + Retriever + Grader)


   .. autolink-examples:: agents.rag.agentic.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.agentic.agent.AgenticRAGAgent
   agents.rag.agentic.agent.AgenticRAGState
   agents.rag.agentic.agent.DocumentGrade
   agents.rag.agentic.agent.QueryRewrite


Functions
---------

.. autoapisummary::

   agents.rag.agentic.agent.create_agentic_rag_agent
   agents.rag.agentic.agent.create_memory_aware_agentic_rag


Module Contents
---------------

.. py:class:: AgenticRAGAgent

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`, :py:obj:`haive.core.common.mixins.tool_route_mixin.ToolRouteMixin`


   Agentic RAG agent combining ReAct reasoning with intelligent retrieval.

   This agent can:
   - Decide when to retrieve vs respond directly (agentic behavior)
   - Grade retrieved documents for relevance
   - Rewrite queries when documents are not relevant
   - Loop until relevant documents are found or max attempts reached

   Key features:
   - Proper Pydantic patterns (no __init__)
   - Multiple engines with proper typing
   - Automatic tool routing via ToolRouteMixin
   - Generic type safety


   .. autolink-examples:: AgenticRAGAgent
      :collapse:

   .. py:method:: _create_agentic_prompt() -> langchain_core.prompts.ChatPromptTemplate
      :staticmethod:


      Create agentic reasoning prompt for deciding when to retrieve.


      .. autolink-examples:: _create_agentic_prompt
         :collapse:


   .. py:method:: _create_answer_generation_tool() -> langchain_core.tools.BaseTool

      Create answer generation tool using retrieved context.


      .. autolink-examples:: _create_answer_generation_tool
         :collapse:


   .. py:method:: _create_grading_prompt() -> langchain_core.prompts.ChatPromptTemplate
      :staticmethod:


      Create prompt for document relevance grading.


      .. autolink-examples:: _create_grading_prompt
         :collapse:


   .. py:method:: _create_grading_tool() -> langchain_core.tools.BaseTool

      Create document grading tool.


      .. autolink-examples:: _create_grading_tool
         :collapse:


   .. py:method:: _create_retrieval_tool() -> langchain_core.tools.BaseTool

      Create semantic retrieval tool.


      .. autolink-examples:: _create_retrieval_tool
         :collapse:


   .. py:method:: _create_rewriting_prompt() -> langchain_core.prompts.ChatPromptTemplate
      :staticmethod:


      Create prompt for query rewriting.


      .. autolink-examples:: _create_rewriting_prompt
         :collapse:


   .. py:method:: _create_rewriting_tool() -> langchain_core.tools.BaseTool

      Create query rewriting tool.


      .. autolink-examples:: _create_rewriting_tool
         :collapse:


   .. py:method:: _setup_agentic_tools() -> None

      Setup tools for agentic RAG with proper routing.


      .. autolink-examples:: _setup_agentic_tools
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_config: Any | None = None, **kwargs) -> AgenticRAGAgent
      :classmethod:


      Create agentic RAG agent from documents using proper factory pattern.

      This follows Pydantic best practices by using a classmethod factory
      instead of complex __init__ logic.


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: setup_agentic_rag() -> AgenticRAGAgent

      Setup agentic RAG with multiple engines and tools.

      This follows proper Pydantic patterns using model_validator
      instead of __init__ for post-initialization setup.


      .. autolink-examples:: setup_agentic_rag
         :collapse:


   .. py:attribute:: enable_query_rewriting
      :type:  bool
      :value: None



   .. py:attribute:: grade_documents_threshold
      :type:  float
      :value: None



   .. py:attribute:: grader_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: max_retrieval_attempts
      :type:  int
      :value: None



   .. py:attribute:: retriever_engine
      :type:  haive.core.engine.retriever.BaseRetrieverConfig
      :value: None



   .. py:attribute:: rewriter_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:property:: state_schema
      :type: type[AgenticRAGState]


      Computed property for agentic RAG state schema.

      .. autolink-examples:: state_schema
         :collapse:


.. py:class:: AgenticRAGState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State schema for agentic RAG with retrieval metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgenticRAGState
      :collapse:

   .. py:attribute:: document_grades
      :type:  list[DocumentGrade]
      :value: None



   .. py:attribute:: max_retrieval_attempts
      :type:  int
      :value: None



   .. py:attribute:: messages
      :type:  list[Any]
      :value: None



   .. py:attribute:: query_rewrites
      :type:  list[QueryRewrite]
      :value: None



   .. py:attribute:: retrieval_attempts
      :type:  int
      :value: None



   .. py:attribute:: retrieved_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



.. py:class:: DocumentGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Grade for document relevance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentGrade
      :collapse:

   .. py:attribute:: binary_score
      :type:  Literal['yes', 'no']
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: QueryRewrite(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Rewritten query for better retrieval.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryRewrite
      :collapse:

   .. py:attribute:: changes_made
      :type:  str
      :value: None



   .. py:attribute:: rewritten_query
      :type:  str
      :value: None



.. py:function:: create_agentic_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG agent with sensible defaults.


   .. autolink-examples:: create_agentic_rag_agent
      :collapse:

.. py:function:: create_memory_aware_agentic_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, memory_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG with long-term memory capabilities.


   .. autolink-examples:: create_memory_aware_agentic_rag
      :collapse:

