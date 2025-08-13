
:py:mod:`agents.document_processing.agent`
==========================================

.. py:module:: agents.document_processing.agent

Comprehensive Document Processing Agent.

This agent provides end-to-end document processing capabilities including:
- Document fetching with ReactAgent + search tools
- Auto-loading with bulk processing
- Transform/split/annotate/embed pipeline
- Advanced RAG features (refined queries, self-query, etc.)
- State management and persistence

The agent integrates all existing Haive document processing components into
a unified, powerful system for document-based AI workflows.

.. rubric:: Examples

Basic document processing::

    agent = DocumentProcessingAgent()
    result = agent.process_query("Load and analyze reports from https://company.com/reports")

Advanced RAG with custom retrieval::

    config = DocumentProcessingConfig(
        retrieval_strategy="self_query",
        query_refinement=True,
        annotation_enabled=True,
        embedding_model="text-embedding-3-large"
    )
    agent = DocumentProcessingAgent(config=config)
    result = agent.process_query("Find all financial projections from Q4 2024")

Multi-source document processing::

    sources = [
        "/path/to/local/docs/",
        "https://wiki.company.com/procedures",
        "s3://bucket/documents/",
        {"url": "https://api.service.com/docs", "headers": {"Authorization": "Bearer token"}}
    ]
    agent = DocumentProcessingAgent()
    result = agent.process_sources(sources, query="Extract key insights")

Author: Claude (Haive AI Agent Framework)
Version: 1.0.0


.. autolink-examples:: agents.document_processing.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_processing.agent.DocumentProcessingAgent
   agents.document_processing.agent.DocumentProcessingConfig
   agents.document_processing.agent.DocumentProcessingResult
   agents.document_processing.agent.DocumentProcessingState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentProcessingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentProcessingAgent {
        node [shape=record];
        "DocumentProcessingAgent" [label="DocumentProcessingAgent"];
      }

.. autoclass:: agents.document_processing.agent.DocumentProcessingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentProcessingConfig:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentProcessingConfig {
        node [shape=record];
        "DocumentProcessingConfig" [label="DocumentProcessingConfig"];
        "pydantic.BaseModel" -> "DocumentProcessingConfig";
      }

.. autopydantic_model:: agents.document_processing.agent.DocumentProcessingConfig
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

   Inheritance diagram for DocumentProcessingResult:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentProcessingResult {
        node [shape=record];
        "DocumentProcessingResult" [label="DocumentProcessingResult"];
        "pydantic.BaseModel" -> "DocumentProcessingResult";
      }

.. autopydantic_model:: agents.document_processing.agent.DocumentProcessingResult
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

   Inheritance diagram for DocumentProcessingState:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentProcessingState {
        node [shape=record];
        "DocumentProcessingState" [label="DocumentProcessingState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "DocumentProcessingState";
      }

.. autoclass:: agents.document_processing.agent.DocumentProcessingState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_processing.agent
   :collapse:
   
.. autolink-skip:: next
