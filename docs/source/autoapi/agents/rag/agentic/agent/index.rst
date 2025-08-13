
:py:mod:`agents.rag.agentic.agent`
==================================

.. py:module:: agents.rag.agentic.agent

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGAgent {
        node [shape=record];
        "AgenticRAGAgent" [label="AgenticRAGAgent"];
        "haive.agents.react.agent.ReactAgent" -> "AgenticRAGAgent";
        "haive.core.common.mixins.tool_route_mixin.ToolRouteMixin" -> "AgenticRAGAgent";
      }

.. autoclass:: agents.rag.agentic.agent.AgenticRAGAgent
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
        "pydantic.BaseModel" -> "AgenticRAGState";
      }

.. autopydantic_model:: agents.rag.agentic.agent.AgenticRAGState
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

   Inheritance diagram for DocumentGrade:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGrade {
        node [shape=record];
        "DocumentGrade" [label="DocumentGrade"];
        "pydantic.BaseModel" -> "DocumentGrade";
      }

.. autopydantic_model:: agents.rag.agentic.agent.DocumentGrade
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

.. autopydantic_model:: agents.rag.agentic.agent.QueryRewrite
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

   agents.rag.agentic.agent.create_agentic_rag_agent
   agents.rag.agentic.agent.create_memory_aware_agentic_rag

.. py:function:: create_agentic_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG agent with sensible defaults.


   .. autolink-examples:: create_agentic_rag_agent
      :collapse:

.. py:function:: create_memory_aware_agentic_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, memory_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG with long-term memory capabilities.


   .. autolink-examples:: create_memory_aware_agentic_rag
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic.agent
   :collapse:
   
.. autolink-skip:: next
