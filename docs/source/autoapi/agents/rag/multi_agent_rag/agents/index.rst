agents.rag.multi_agent_rag.agents
=================================

.. py:module:: agents.rag.multi_agent_rag.agents

.. autoapi-nested-parse::

   Multi-Agent RAG System Components.

   This module provides specialized RAG agents that can be composed into complex workflows
   using the multi-agent framework. Each agent focuses on a specific aspect of the RAG process.


   .. autolink-examples:: agents.rag.multi_agent_rag.agents
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_agent_rag.agents.RAG_ANSWER_BASE_PROMPT_TEMPLATE
   agents.rag.multi_agent_rag.agents.RAG_DOCUMENT_ITERATOR_PROMPT_TEMPLATE
   agents.rag.multi_agent_rag.agents.RAG_RETRIEVAL_PROMPT_TEMPLATE
   agents.rag.multi_agent_rag.agents.SIMPLE_RAG_AGENT
   agents.rag.multi_agent_rag.agents.SIMPLE_RAG_ANSWER_AGENT
   agents.rag.multi_agent_rag.agents.conversation_documents
   agents.rag.multi_agent_rag.agents.documents
   agents.rag.multi_agent_rag.agents.from_documents
   agents.rag.multi_agent_rag.agents.grading_mode
   agents.rag.multi_agent_rag.agents.max_documents
   agents.rag.multi_agent_rag.agents.min_relevance_threshold
   agents.rag.multi_agent_rag.agents.use_citations


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.agents.DocumentGradingAgent
   agents.rag.multi_agent_rag.agents.IterativeDocumentGradingAgent
   agents.rag.multi_agent_rag.agents.SimpleRAGAgent
   agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.agents.create_document_grading_agent
   agents.rag.multi_agent_rag.agents.create_iterative_grading_agent
   agents.rag.multi_agent_rag.agents.create_rag_answer_agent
   agents.rag.multi_agent_rag.agents.create_simple_rag_agent
   agents.rag.multi_agent_rag.agents.generate_answer
   agents.rag.multi_agent_rag.agents.grade_document
   agents.rag.multi_agent_rag.agents.grade_documents
   agents.rag.multi_agent_rag.agents.retrieve_documents
   agents.rag.multi_agent_rag.agents.run_generation
   agents.rag.multi_agent_rag.agents.run_grading
   agents.rag.multi_agent_rag.agents.run_iterative_grading
   agents.rag.multi_agent_rag.agents.run_retrieval


Module Contents
---------------

.. py:class:: DocumentGradingAgent(grading_mode: str = 'binary', min_relevance_threshold: float = 0.5, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Document grading agent that evaluates document relevance.

   This agent can iterate over retrieved documents and grade each one for
   relevance to the query using configurable grading strategies.


   .. autolink-examples:: DocumentGradingAgent
      :collapse:

   .. py:method:: grade_document(query: str, document: langchain_core.documents.Document) -> haive.agents.rag.multi_agent_rag.state.DocumentGradingResult

      Grade a single document for relevance.


      .. autolink-examples:: grade_document
         :collapse:


   .. py:method:: grade_documents(query: str, documents: list[langchain_core.documents.Document]) -> list[haive.agents.rag.multi_agent_rag.state.DocumentGradingResult]

      Grade multiple documents.


      .. autolink-examples:: grade_documents
         :collapse:


   .. py:method:: run_grading(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> dict[str, Any]

      Run document grading and update state.


      .. autolink-examples:: run_grading
         :collapse:


   .. py:attribute:: _grading_mode
      :value: 'binary'



   .. py:attribute:: _min_relevance_threshold
      :value: 0.5



   .. py:property:: grading_mode
      :type: str


      Get the grading mode.

      .. autolink-examples:: grading_mode
         :collapse:


   .. py:property:: min_relevance_threshold
      :type: float


      Get the minimum relevance threshold.

      .. autolink-examples:: min_relevance_threshold
         :collapse:


.. py:class:: IterativeDocumentGradingAgent(custom_grader: collections.abc.Callable | None = None, **kwargs)

   Bases: :py:obj:`DocumentGradingAgent`


   Specialized grading agent that processes documents one by one.

   This agent demonstrates the capability to iterate over retrieved documents
   and process each one individually with custom callables.


   .. autolink-examples:: IterativeDocumentGradingAgent
      :collapse:

   .. py:method:: run_iterative_grading(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> dict[str, Any]

      Run iterative document grading with custom processing.


      .. autolink-examples:: run_iterative_grading
         :collapse:


   .. py:attribute:: custom_grader
      :value: None



.. py:class:: SimpleRAGAgent(documents: list[langchain_core.documents.Document] | None = None, max_documents: int = 5, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Simple RAG agent that retrieves documents and provides basic answers.

   This agent provides fundamental RAG functionality using conversation documents
   as the knowledge base. It can be composed with other agents for more complex workflows.


   .. autolink-examples:: SimpleRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], prompt_template: langchain_core.prompts.ChatPromptTemplate | None = None, **kwargs) -> SimpleRAGAgent
      :classmethod:


      Create SimpleRAGAgent from a document collection.


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: retrieve_documents(query: str, top_k: int | None = None) -> list[langchain_core.documents.Document]

      Simple document retrieval based on text matching.


      .. autolink-examples:: retrieve_documents
         :collapse:


   .. py:method:: run_retrieval(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> dict[str, Any]

      Run document retrieval and update state.


      .. autolink-examples:: run_retrieval
         :collapse:


   .. py:attribute:: _documents


   .. py:attribute:: _max_documents
      :value: 5



   .. py:property:: documents
      :type: list[langchain_core.documents.Document]


      Get the documents for this RAG agent.

      .. autolink-examples:: documents
         :collapse:


   .. py:property:: max_documents
      :type: int


      Get the maximum number of documents to retrieve.

      .. autolink-examples:: max_documents
         :collapse:


.. py:class:: SimpleRAGAnswerAgent(use_citations: bool = False, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   RAG answer generation agent that creates responses from retrieved documents.

   This agent focuses specifically on generating high-quality answers from
   retrieved documents using structured prompts.


   .. autolink-examples:: SimpleRAGAnswerAgent
      :collapse:

   .. py:method:: generate_answer(query: str, documents: list[langchain_core.documents.Document]) -> str

      Generate answer from query and documents.


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: run_generation(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> dict[str, Any]

      Run answer generation and update state.


      .. autolink-examples:: run_generation
         :collapse:


   .. py:attribute:: _use_citations
      :value: False



   .. py:property:: use_citations
      :type: bool


      Get whether to use citations in answers.

      .. autolink-examples:: use_citations
         :collapse:


.. py:function:: create_document_grading_agent(grading_mode: str = 'binary', min_threshold: float = 0.5, **kwargs) -> DocumentGradingAgent

   Create a document grading agent with default configuration.


   .. autolink-examples:: create_document_grading_agent
      :collapse:

.. py:function:: create_iterative_grading_agent(custom_grader: collections.abc.Callable | None = None, **kwargs) -> IterativeDocumentGradingAgent

   Create an iterative document grading agent.


   .. autolink-examples:: create_iterative_grading_agent
      :collapse:

.. py:function:: create_rag_answer_agent(use_citations: bool = False, **kwargs) -> SimpleRAGAnswerAgent

   Create a RAG answer agent with default configuration.


   .. autolink-examples:: create_rag_answer_agent
      :collapse:

.. py:function:: create_simple_rag_agent(documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> SimpleRAGAgent

   Create a simple RAG agent with default configuration.


   .. autolink-examples:: create_simple_rag_agent
      :collapse:

.. py:function:: generate_answer(query, docs)

.. py:function:: grade_document(doc)

.. py:function:: grade_documents(docs)

.. py:function:: retrieve_documents(query)

.. py:function:: run_generation(state)

.. py:function:: run_grading(state)

.. py:function:: run_iterative_grading(state)

.. py:function:: run_retrieval(state)

.. py:data:: RAG_ANSWER_BASE_PROMPT_TEMPLATE

.. py:data:: RAG_DOCUMENT_ITERATOR_PROMPT_TEMPLATE

.. py:data:: RAG_RETRIEVAL_PROMPT_TEMPLATE

.. py:data:: SIMPLE_RAG_AGENT

.. py:data:: SIMPLE_RAG_ANSWER_AGENT

.. py:data:: conversation_documents

.. py:data:: documents

.. py:data:: from_documents

.. py:data:: grading_mode
   :value: 'binary'


.. py:data:: max_documents
   :value: 10


.. py:data:: min_relevance_threshold
   :value: 0.5


.. py:data:: use_citations
   :value: False


