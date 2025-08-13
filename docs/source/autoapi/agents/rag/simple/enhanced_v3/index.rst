
:py:mod:`agents.rag.simple.enhanced_v3`
=======================================

.. py:module:: agents.rag.simple.enhanced_v3

Enhanced SimpleRAG V3 using Enhanced MultiAgent V3.

This package provides SimpleRAG implementation using the Enhanced MultiAgent V3 pattern
with performance tracking, debug support, and adaptive routing capabilities.

Classes:
    - SimpleRAGV3: Main SimpleRAG implementation with Enhanced MultiAgent V3
    - RetrieverAgent: Specialized agent for document retrieval
    - AnswerGeneratorAgent: Specialized agent for answer generation
    - SimpleRAGState: Enhanced state schema for SimpleRAG pipeline

.. rubric:: Examples

Basic usage::

    from haive.agents.rag.simple.enhanced_v3 import SimpleRAGV3

    rag = SimpleRAGV3.from_documents(
        documents=documents,
        embedding_config=embedding_config,
        performance_mode=True
    )

    result = await rag.arun("What is machine learning?")

With performance tracking::

    rag = SimpleRAGV3(
        name="qa_system",
        vector_store_config=vs_config,
        performance_mode=True,
        debug_mode=True
    )

    result = await rag.arun("Complex query")

    # Monitor performance
    analysis = rag.analyze_agent_performance()
    print(f"Retriever success rate: {analysis['agents']['retriever']['success_rate']}")


.. autolink-examples:: agents.rag.simple.enhanced_v3
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.RetrieverAgent
   agents.rag.simple.enhanced_v3.SimpleAnswerAgent
   agents.rag.simple.enhanced_v3.SimpleRAGState
   agents.rag.simple.enhanced_v3.SimpleRAGV3


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RetrieverAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RetrieverAgent {
        node [shape=record];
        "RetrieverAgent" [label="RetrieverAgent"];
        "haive.agents.rag.base.agent.BaseRAGAgent" -> "RetrieverAgent";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.RetrieverAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAnswerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAnswerAgent {
        node [shape=record];
        "SimpleAnswerAgent" [label="SimpleAnswerAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "SimpleAnswerAgent";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.SimpleAnswerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGState {
        node [shape=record];
        "SimpleRAGState" [label="SimpleRAGState"];
        "haive.core.schema.state_schema.StateSchema" -> "SimpleRAGState";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.SimpleRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleRAGV3:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGV3 {
        node [shape=record];
        "SimpleRAGV3" [label="SimpleRAGV3"];
        "haive.agents.multi.enhanced_multi_agent_v3.EnhancedMultiAgent[RAGAgentCollection]" -> "SimpleRAGV3";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.SimpleRAGV3
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.simple.enhanced_v3
   :collapse:
   
.. autolink-skip:: next
