agents.rag.document_grading.agent
=================================

.. py:module:: agents.rag.document_grading.agent

.. autoapi-nested-parse::

   Document Grading RAG Agent.

   from typing import Any
   Iterative document grading with structured output.
   Uses CallableNodeConfig to iterate over retrieved documents.


   .. autolink-examples:: agents.rag.document_grading.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.document_grading.agent.SINGLE_DOC_GRADING_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.document_grading.agent.DocumentGradingAgent
   agents.rag.document_grading.agent.DocumentGradingRAGAgent
   agents.rag.document_grading.agent.SingleDocumentGrade


Module Contents
---------------

.. py:class:: DocumentGradingAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that iterates over documents and grades each one.

   Initialize with LLM config.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentGradingAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with document grading using CallableNode iteration.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Document Grader'



   .. py:attribute:: relevance_threshold
      :type:  float
      :value: 0.7



.. py:class:: DocumentGradingRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   RAG with document grading and filtering.


   .. autolink-examples:: DocumentGradingRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, relevance_threshold: float = 0.7, **kwargs)
      :classmethod:


      Create Document Grading RAG from documents.


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: SingleDocumentGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Grade for a single document.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SingleDocumentGrade
      :collapse:

   .. py:attribute:: is_relevant
      :type:  bool
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



.. py:data:: SINGLE_DOC_GRADING_PROMPT

