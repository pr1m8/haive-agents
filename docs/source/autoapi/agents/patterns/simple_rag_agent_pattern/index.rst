
:py:mod:`agents.patterns.simple_rag_agent_pattern`
==================================================

.. py:module:: agents.patterns.simple_rag_agent_pattern

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AnswerWithSources:

   .. graphviz::
      :align: center

      digraph inheritance_AnswerWithSources {
        node [shape=record];
        "AnswerWithSources" [label="AnswerWithSources"];
        "pydantic.BaseModel" -> "AnswerWithSources";
      }

.. autopydantic_model:: agents.patterns.simple_rag_agent_pattern.AnswerWithSources
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

   Inheritance diagram for HybridRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HybridRAGAgent {
        node [shape=record];
        "HybridRAGAgent" [label="HybridRAGAgent"];
        "SimpleRAGAgent" -> "HybridRAGAgent";
      }

.. autoclass:: agents.patterns.simple_rag_agent_pattern.HybridRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeRAGAgent {
        node [shape=record];
        "IterativeRAGAgent" [label="IterativeRAGAgent"];
        "SimpleRAGAgent" -> "IterativeRAGAgent";
      }

.. autoclass:: agents.patterns.simple_rag_agent_pattern.IterativeRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RetrievalResult:

   .. graphviz::
      :align: center

      digraph inheritance_RetrievalResult {
        node [shape=record];
        "RetrievalResult" [label="RetrievalResult"];
        "pydantic.BaseModel" -> "RetrievalResult";
      }

.. autopydantic_model:: agents.patterns.simple_rag_agent_pattern.RetrievalResult
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

   Inheritance diagram for SimpleRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGAgent {
        node [shape=record];
        "SimpleRAGAgent" [label="SimpleRAGAgent"];
        "SimpleAgentV3" -> "SimpleRAGAgent";
      }

.. autoclass:: agents.patterns.simple_rag_agent_pattern.SimpleRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


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



.. rubric:: Related Links

.. autolink-examples:: agents.patterns.simple_rag_agent_pattern
   :collapse:
   
.. autolink-skip:: next
