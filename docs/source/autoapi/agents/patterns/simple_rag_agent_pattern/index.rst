agents.patterns.simple_rag_agent_pattern
========================================

.. py:module:: agents.patterns.simple_rag_agent_pattern

.. autoapi-nested-parse::

   Simple RAG Agent Pattern - Using SimpleAgentV3 as base for RAG implementation.

   This module demonstrates creating a RAG (Retrieval-Augmented Generation) agent
   using SimpleAgentV3 as the foundation, following the user's request to use
   agent.py and SimpleAgentV3 patterns.

   The pattern shows:
   1. Extending SimpleAgentV3 for specialized functionality
   2. Proper state schema composition
   3. Tool integration for retrieval
   4. Structured output for answers


   .. autolink-examples:: agents.patterns.simple_rag_agent_pattern
      :collapse:


Classes
-------

.. autoapisummary::

   agents.patterns.simple_rag_agent_pattern.AnswerWithSources
   agents.patterns.simple_rag_agent_pattern.HybridRAGAgent
   agents.patterns.simple_rag_agent_pattern.IterativeRAGAgent
   agents.patterns.simple_rag_agent_pattern.RetrievalResult
   agents.patterns.simple_rag_agent_pattern.SimpleRAGAgent


Functions
---------

.. autoapisummary::

   agents.patterns.simple_rag_agent_pattern.create_hybrid_rag_agent
   agents.patterns.simple_rag_agent_pattern.create_iterative_rag_agent
   agents.patterns.simple_rag_agent_pattern.create_simple_rag_agent
   agents.patterns.simple_rag_agent_pattern.example_hybrid_rag
   agents.patterns.simple_rag_agent_pattern.example_iterative_rag
   agents.patterns.simple_rag_agent_pattern.example_simple_rag
   agents.patterns.simple_rag_agent_pattern.retrieve_documents


Module Contents
---------------

.. py:class:: AnswerWithSources(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured answer with source citations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnswerWithSources
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: follow_up_questions
      :type:  list[str]
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



.. py:class:: HybridRAGAgent

   Bases: :py:obj:`SimpleRAGAgent`


   Hybrid RAG Agent combining multiple retrieval strategies.

   This variant uses multiple retrieval approaches:
   - Semantic similarity search
   - Keyword-based retrieval
   - Knowledge graph traversal
   - Combines results for comprehensive answers


   .. autolink-examples:: HybridRAGAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Setup hybrid retrieval tools.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: use_keyword_search
      :type:  bool
      :value: None



   .. py:attribute:: use_knowledge_graph
      :type:  bool
      :value: None



   .. py:attribute:: use_semantic_search
      :type:  bool
      :value: None



.. py:class:: IterativeRAGAgent

   Bases: :py:obj:`SimpleRAGAgent`


   Iterative RAG Agent that refines answers through multiple retrievals.

   This variant performs iterative retrieval and refinement:
   1. Initial retrieval and answer generation
   2. Identifies gaps or unclear areas
   3. Performs targeted follow-up retrievals
   4. Refines the answer with additional context


   .. autolink-examples:: IterativeRAGAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Setup iterative RAG configuration.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: refinement_threshold
      :type:  float
      :value: None



.. py:class:: RetrievalResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured retrieval result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RetrievalResult
      :collapse:

   .. py:attribute:: documents
      :type:  list[str]
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: relevance_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: total_results
      :type:  int
      :value: None



.. py:class:: SimpleRAGAgent

   Bases: :py:obj:`SimpleAgentV3`


   Simple RAG Agent built on SimpleAgentV3 foundation.

   This agent extends SimpleAgentV3 to provide RAG capabilities:
   - Document retrieval through tools
   - Context-aware answer generation
   - Source attribution
   - Structured output with confidence scores

   .. rubric:: Example

   >>> rag_agent = SimpleRAGAgent(
   ...     name="knowledge_assistant",
   ...     temperature=0.3,
   ...     debug=True
   ... )
   >>> result = await rag_agent.arun("What is quantum computing?")


   .. autolink-examples:: SimpleRAGAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Setup RAG-specific configuration.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: include_sources
      :type:  bool
      :value: None



   .. py:attribute:: min_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: retrieval_top_k
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type
      :value: None



.. py:function:: create_hybrid_rag_agent(name: str = 'hybrid_rag', retrieval_strategies: list[str] | None = None, **kwargs) -> HybridRAGAgent

   Create a hybrid RAG agent with multiple retrieval strategies.


   .. autolink-examples:: create_hybrid_rag_agent
      :collapse:

.. py:function:: create_iterative_rag_agent(name: str = 'iterative_rag', max_iterations: int = 3, **kwargs) -> IterativeRAGAgent

   Create an iterative RAG agent for complex queries.


   .. autolink-examples:: create_iterative_rag_agent
      :collapse:

.. py:function:: create_simple_rag_agent(name: str = 'rag_assistant', temperature: float = 0.3, debug: bool = True, **kwargs) -> SimpleRAGAgent

   Create a simple RAG agent with sensible defaults.


   .. autolink-examples:: create_simple_rag_agent
      :collapse:

.. py:function:: example_hybrid_rag()
   :async:


   Example of hybrid retrieval.


   .. autolink-examples:: example_hybrid_rag
      :collapse:

.. py:function:: example_iterative_rag()
   :async:


   Example of iterative refinement.


   .. autolink-examples:: example_iterative_rag
      :collapse:

.. py:function:: example_simple_rag()
   :async:


   Example of using SimpleRAGAgent.


   .. autolink-examples:: example_simple_rag
      :collapse:

.. py:function:: retrieve_documents(query: str, top_k: int = 5) -> str

   Retrieve documents based on query.


   .. autolink-examples:: retrieve_documents
      :collapse:

