
:py:mod:`agents.rag.enhanced_memory_react`
==========================================

.. py:module:: agents.rag.enhanced_memory_react

Enhanced Memory RAG with ReAct Pattern.

RAG system that maintains conversation memory and uses ReAct (Reasoning + Acting)
pattern for complex multi-step queries requiring reasoning and tool use.


.. autolink-examples:: agents.rag.enhanced_memory_react
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.enhanced_memory_react.EnhancedResponse
   agents.rag.enhanced_memory_react.MemoryAnalysis
   agents.rag.enhanced_memory_react.MemoryEntry
   agents.rag.enhanced_memory_react.MemoryType
   agents.rag.enhanced_memory_react.ReActStep
   agents.rag.enhanced_memory_react.ReActStepResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedResponse:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedResponse {
        node [shape=record];
        "EnhancedResponse" [label="EnhancedResponse"];
        "pydantic.BaseModel" -> "EnhancedResponse";
      }

.. autopydantic_model:: agents.rag.enhanced_memory_react.EnhancedResponse
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

   Inheritance diagram for MemoryAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryAnalysis {
        node [shape=record];
        "MemoryAnalysis" [label="MemoryAnalysis"];
        "pydantic.BaseModel" -> "MemoryAnalysis";
      }

.. autopydantic_model:: agents.rag.enhanced_memory_react.MemoryAnalysis
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

   Inheritance diagram for MemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryEntry {
        node [shape=record];
        "MemoryEntry" [label="MemoryEntry"];
        "pydantic.BaseModel" -> "MemoryEntry";
      }

.. autopydantic_model:: agents.rag.enhanced_memory_react.MemoryEntry
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

   Inheritance diagram for MemoryType:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryType {
        node [shape=record];
        "MemoryType" [label="MemoryType"];
        "str" -> "MemoryType";
        "enum.Enum" -> "MemoryType";
      }

.. autoclass:: agents.rag.enhanced_memory_react.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.rag.enhanced_memory_react``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReActStep:

   .. graphviz::
      :align: center

      digraph inheritance_ReActStep {
        node [shape=record];
        "ReActStep" [label="ReActStep"];
        "str" -> "ReActStep";
        "enum.Enum" -> "ReActStep";
      }

.. autoclass:: agents.rag.enhanced_memory_react.ReActStep
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ReActStep** is an Enum defined in ``agents.rag.enhanced_memory_react``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReActStepResult:

   .. graphviz::
      :align: center

      digraph inheritance_ReActStepResult {
        node [shape=record];
        "ReActStepResult" [label="ReActStepResult"];
        "pydantic.BaseModel" -> "ReActStepResult";
      }

.. autopydantic_model:: agents.rag.enhanced_memory_react.ReActStepResult
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



Functions
---------

.. autoapisummary::

   agents.rag.enhanced_memory_react.create_enhanced_memory_react_rag
   agents.rag.enhanced_memory_react.create_memory_react_with_tools
   agents.rag.enhanced_memory_react.create_simple_memory_react_rag
   agents.rag.enhanced_memory_react.get_enhanced_memory_react_io_schema

.. py:function:: create_enhanced_memory_react_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Enhanced Memory ReAct RAG') -> haive.agents.chain.ChainAgent

   Create an enhanced memory-aware RAG with ReAct pattern.


   .. autolink-examples:: create_enhanced_memory_react_rag
      :collapse:

.. py:function:: create_memory_react_with_tools(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create memory ReAct RAG with tool integration.


   .. autolink-examples:: create_memory_react_with_tools
      :collapse:

.. py:function:: create_simple_memory_react_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a simplified memory-aware ReAct RAG.


   .. autolink-examples:: create_simple_memory_react_rag
      :collapse:

.. py:function:: get_enhanced_memory_react_io_schema() -> dict[str, list[str]]

   Get I/O schema for enhanced memory ReAct RAG.


   .. autolink-examples:: get_enhanced_memory_react_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.enhanced_memory_react
   :collapse:
   
.. autolink-skip:: next
