
:py:mod:`agents.rag.agentic`
============================

.. py:module:: agents.rag.agentic

Module exports.


.. autolink-examples:: agents.rag.agentic
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.agentic.AgenticRAGAgent
   agents.rag.agentic.AgenticRAGState
   agents.rag.agentic.DocumentGrade
   agents.rag.agentic.QueryRewrite
   agents.rag.agentic.ReactRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGAgent {
        node [shape=record];
        "AgenticRAGAgent" [label="AgenticRAGAgent"];
        "haive.agents.simple.SimpleAgent" -> "AgenticRAGAgent";
      }

.. autoclass:: agents.rag.agentic.AgenticRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGState {
        node [shape=record];
        "AgenticRAGState" [label="AgenticRAGState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "AgenticRAGState";
      }

.. autoclass:: agents.rag.agentic.AgenticRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGrade:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGrade {
        node [shape=record];
        "DocumentGrade" [label="DocumentGrade"];
        "pydantic.BaseModel" -> "DocumentGrade";
      }

.. autopydantic_model:: agents.rag.agentic.DocumentGrade
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryRewrite:

   .. graphviz::
      :align: center

      digraph inheritance_QueryRewrite {
        node [shape=record];
        "QueryRewrite" [label="QueryRewrite"];
        "pydantic.BaseModel" -> "QueryRewrite";
      }

.. autopydantic_model:: agents.rag.agentic.QueryRewrite
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactRAGAgent {
        node [shape=record];
        "ReactRAGAgent" [label="ReactRAGAgent"];
        "haive.agents.react.ReactAgent" -> "ReactRAGAgent";
      }

.. autoclass:: agents.rag.agentic.ReactRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.agentic.create_agentic_rag_agent
   agents.rag.agentic.create_document_grader_agent
   agents.rag.agentic.create_memory_aware_agentic_rag
   agents.rag.agentic.create_query_rewriter_agent

.. py:function:: create_agentic_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG agent with sensible defaults.


   .. autolink-examples:: create_agentic_rag_agent
      :collapse:

.. py:function:: create_document_grader_agent(name: str = 'document_grader', temperature: float = 0.0, **kwargs) -> haive.agents.simple.SimpleAgent

   Create a document grader agent using direct SimpleAgent instantiation.

   :param name: Agent name (default: "document_grader")
   :param temperature: LLM temperature (default: 0.0 for consistency)
   :param \*\*kwargs: Additional configuration options

   :returns: SimpleAgent configured for document grading

   .. rubric:: Example

   .. code-block:: python

       # Create grader agent
       grader = create_document_grader_agent(
       name="doc_grader",
       temperature=0.0
       )

       # Grade documents
       result = await grader.arun({
       "query": "What is quantum computing?",
       "documents": [
       {"content": "Quantum computing uses quantum mechanics...", "id": "doc1"},
       {"content": "Classical computing uses binary digits...", "id": "doc2"}
       ]
       })

       # Access results
       for decision in result.document_decisions:
       print(f"Document {decision.document_id}: {decision.decision}")
       print(f"Reason: {decision.justification}")


   .. autolink-examples:: create_document_grader_agent
      :collapse:

.. py:function:: create_memory_aware_agentic_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, memory_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG with long-term memory capabilities.


   .. autolink-examples:: create_memory_aware_agentic_rag
      :collapse:

.. py:function:: create_query_rewriter_agent(name: str = 'query_rewriter', temperature: float = 0.7, **kwargs) -> haive.agents.simple.SimpleAgent

   Create a query rewriter agent using direct SimpleAgent instantiation.

   :param name: Agent name (default: "query_rewriter")
   :param temperature: LLM temperature (default: 0.7 for creativity)
   :param \*\*kwargs: Additional configuration options

   :returns: SimpleAgent configured for query refinement

   .. rubric:: Example

   .. code-block:: python

       # Create query rewriter agent
       rewriter = create_query_rewriter_agent(
       name="query_rewriter",
       temperature=0.7
       )

       # Rewrite a query
       result = await rewriter.arun({
       "query": "quantum computing basics"
       })

       # Access results
       print(f"Original: {result.original_query}")
       print(f"Best rewrite: {result.best_refined_query}")
       for suggestion in result.refinement_suggestions:
       print(f"- {suggestion.refined_query} ({suggestion.improvement_type})")


   .. autolink-examples:: create_query_rewriter_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic
   :collapse:
   
.. autolink-skip:: next
