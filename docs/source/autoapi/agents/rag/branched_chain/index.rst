
:py:mod:`agents.rag.branched_chain`
===================================

.. py:module:: agents.rag.branched_chain

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BranchResult:

   .. graphviz::
      :align: center

      digraph inheritance_BranchResult {
        node [shape=record];
        "BranchResult" [label="BranchResult"];
        "pydantic.BaseModel" -> "BranchResult";
      }

.. autopydantic_model:: agents.rag.branched_chain.BranchResult
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

   Inheritance diagram for MergedResult:

   .. graphviz::
      :align: center

      digraph inheritance_MergedResult {
        node [shape=record];
        "MergedResult" [label="MergedResult"];
        "pydantic.BaseModel" -> "MergedResult";
      }

.. autopydantic_model:: agents.rag.branched_chain.MergedResult
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

   Inheritance diagram for QueryClassification:

   .. graphviz::
      :align: center

      digraph inheritance_QueryClassification {
        node [shape=record];
        "QueryClassification" [label="QueryClassification"];
        "pydantic.BaseModel" -> "QueryClassification";
      }

.. autopydantic_model:: agents.rag.branched_chain.QueryClassification
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

   Inheritance diagram for QueryType:

   .. graphviz::
      :align: center

      digraph inheritance_QueryType {
        node [shape=record];
        "QueryType" [label="QueryType"];
        "str" -> "QueryType";
        "enum.Enum" -> "QueryType";
      }

.. autoclass:: agents.rag.branched_chain.QueryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryType** is an Enum defined in ``agents.rag.branched_chain``.



Functions
---------

.. autoapisummary::

   agents.rag.branched_chain.create_adaptive_branched_rag
   agents.rag.branched_chain.create_branched_rag_chain
   agents.rag.branched_chain.create_parallel_branched_rag
   agents.rag.branched_chain.get_branched_rag_io_schema

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.branched_chain
   :collapse:
   
.. autolink-skip:: next
