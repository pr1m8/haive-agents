agents.rag.branched_chain
=========================

.. py:module:: agents.rag.branched_chain

.. autoapi-nested-parse::

   Branched RAG using ChainAgent.

   RAG system that branches into multiple specialized retrieval paths based on query type,
   then merges results for comprehensive answers.


   .. autolink-examples:: agents.rag.branched_chain
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.branched_chain.BranchResult
   agents.rag.branched_chain.MergedResult
   agents.rag.branched_chain.QueryClassification
   agents.rag.branched_chain.QueryType


Functions
---------

.. autoapisummary::

   agents.rag.branched_chain.create_adaptive_branched_rag
   agents.rag.branched_chain.create_branched_rag_chain
   agents.rag.branched_chain.create_parallel_branched_rag
   agents.rag.branched_chain.get_branched_rag_io_schema


Module Contents
---------------

.. py:class:: BranchResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from a retrieval branch.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BranchResult
      :collapse:

   .. py:attribute:: branch_answer
      :type:  str
      :value: None



   .. py:attribute:: branch_type
      :type:  str
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: retrieved_docs
      :type:  list[str]
      :value: None



.. py:class:: MergedResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final merged result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MergedResult
      :collapse:

   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: primary_answer
      :type:  str
      :value: None



   .. py:attribute:: sources_used
      :type:  list[str]
      :value: None



   .. py:attribute:: supporting_evidence
      :type:  list[str]
      :value: None



.. py:class:: QueryClassification(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Query classification result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryClassification
      :collapse:

   .. py:attribute:: complexity
      :type:  Literal['simple', 'medium', 'complex']
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: primary_type
      :type:  QueryType
      :value: None



   .. py:attribute:: secondary_type
      :type:  QueryType | None
      :value: None



.. py:class:: QueryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of queries for branching.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryType
      :collapse:

   .. py:attribute:: ANALYTICAL
      :value: 'analytical'



   .. py:attribute:: CREATIVE
      :value: 'creative'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



.. py:function:: create_adaptive_branched_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create an adaptive branched RAG that selects branches based on query type.


   .. autolink-examples:: create_adaptive_branched_rag
      :collapse:

.. py:function:: create_branched_rag_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Branched RAG') -> haive.agents.chain.ChainAgent

   Create a branched RAG system using ChainAgent.


   .. autolink-examples:: create_branched_rag_chain
      :collapse:

.. py:function:: create_parallel_branched_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a parallel branched RAG that runs all branches simultaneously.


   .. autolink-examples:: create_parallel_branched_rag
      :collapse:

.. py:function:: get_branched_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for branched RAG.


   .. autolink-examples:: get_branched_rag_io_schema
      :collapse:

