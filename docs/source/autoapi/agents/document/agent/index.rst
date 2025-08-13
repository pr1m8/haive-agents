
:py:mod:`agents.document.agent`
===============================

.. py:module:: agents.document.agent

Document Agent for comprehensive document processing pipeline.

from typing import Any
This module provides the DocumentAgent class which implements the full document processing
pipeline: FETCH -> LOAD -> TRANSFORM -> SPLIT -> ANNOTATE -> EMBED -> STORE -> RETRIEVE.

The agent leverages the Document Engine from haive-core to handle 97+ document types
and sources with advanced processing capabilities including chunking, metadata
extraction, and parallel processing.

Classes:
    DocumentAgent: Main agent for document processing pipeline
    DocumentProcessingResult: Structured result from document processing

.. rubric:: Examples

Basic usage::

    from haive.agents.document import DocumentAgent
    from haive.core.engine.document import DocumentEngineConfig

    agent = DocumentAgent(name="doc_processor")
    result = agent.process_sources(["document.pdf"])
    print(f"Processed {result.total_documents} documents")

Advanced configuration::

    config = DocumentEngineConfig(
        chunking_strategy=ChunkingStrategy.SEMANTIC,
        parallel_processing=True,
        max_workers=8
    )
    agent = DocumentAgent(name="enterprise_processor", engine=config)
    result = agent.process_directory("/path/to/documents")

.. seealso::

   - :class:`~haive.core.engine.document.DocumentEngine`: Core processing engine
   - :class:`~haive.agents.base.Agent`: Base agent class


.. autolink-examples:: agents.document.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document.agent.DocumentAgent
   agents.document.agent.DocumentProcessingResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentAgent {
        node [shape=record];
        "DocumentAgent" [label="DocumentAgent"];
        "haive.agents.base.agent.Agent" -> "DocumentAgent";
      }

.. autoclass:: agents.document.agent.DocumentAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentProcessingResult:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentProcessingResult {
        node [shape=record];
        "DocumentProcessingResult" [label="DocumentProcessingResult"];
        "pydantic.BaseModel" -> "DocumentProcessingResult";
      }

.. autopydantic_model:: agents.document.agent.DocumentProcessingResult
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





.. rubric:: Related Links

.. autolink-examples:: agents.document.agent
   :collapse:
   
.. autolink-skip:: next
