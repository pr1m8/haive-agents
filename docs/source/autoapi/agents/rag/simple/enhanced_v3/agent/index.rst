
:py:mod:`agents.rag.simple.enhanced_v3.agent`
=============================================

.. py:module:: agents.rag.simple.enhanced_v3.agent

SimpleRAG V3 - Enhanced MultiAgent Implementation.

This module implements SimpleRAG using Enhanced MultiAgent V3 with the pattern:
SimpleRAG = EnhancedMultiAgent[RetrieverAgent, SimpleAnswerAgent]

The implementation provides:
- Type-safe agent composition
- Performance tracking and optimization
- Debug support and monitoring
- Adaptive routing capabilities
- Comprehensive state management

.. rubric:: Examples

Basic usage::

    rag = SimpleRAGV3.from_documents(
        documents=documents,
        embedding_config=embedding_config,
        performance_mode=True
    )

    result = await rag.arun("What is machine learning?")

Advanced usage with monitoring::

    rag = SimpleRAGV3(
        name="qa_system",
        vector_store_config=vector_store_config,
        performance_mode=True,
        debug_mode=True,
        adaptation_rate=0.2
    )

    result = await rag.arun("Complex query")
    analysis = rag.analyze_agent_performance()


.. autolink-examples:: agents.rag.simple.enhanced_v3.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.agent.RetrieverAgent
   agents.rag.simple.enhanced_v3.agent.SimpleAnswerAgent
   agents.rag.simple.enhanced_v3.agent.SimpleRAGState
   agents.rag.simple.enhanced_v3.agent.SimpleRAGV3


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RetrieverAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RetrieverAgent {
        node [shape=record];
        "RetrieverAgent" [label="RetrieverAgent"];
        "haive.agents.rag.base.agent.BaseRAGAgent" -> "RetrieverAgent";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.agent.RetrieverAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAnswerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAnswerAgent {
        node [shape=record];
        "SimpleAnswerAgent" [label="SimpleAnswerAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "SimpleAnswerAgent";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.agent.SimpleAnswerAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGState {
        node [shape=record];
        "SimpleRAGState" [label="SimpleRAGState"];
        "haive.core.schema.state_schema.StateSchema" -> "SimpleRAGState";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.agent.SimpleRAGState
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

.. autoclass:: agents.rag.simple.enhanced_v3.agent.SimpleRAGV3
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.simple.enhanced_v3.agent
   :collapse:
   
.. autolink-skip:: next
