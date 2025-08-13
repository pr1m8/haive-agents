
:py:mod:`agents.rag.simple.multi_agent_simple_rag`
==================================================

.. py:module:: agents.rag.simple.multi_agent_simple_rag

SimpleRAG - Proper MultiAgent Implementation.

This is the CORRECT SimpleRAG implementation using the proper MultiAgent pattern:
    SimpleRAG extends MultiAgent with agents={"retriever": BaseRAGAgent, "generator": SimpleAgent}

The key insight is that SimpleRAG IS a MultiAgent that coordinates two specific agents:
1. BaseRAGAgent: Handles document retrieval
2. SimpleAgent: Generates answers from documents

This follows the MultiAgent[AgentsT] pattern where:
- SimpleRAG extends MultiAgent
- agents field contains the two agents
- execution_mode="sequence" for retrieval → generation flow

.. rubric:: Examples

Basic usage::

    rag = SimpleRAG(
        name="qa_system",
        retriever_config=VectorStoreConfig(vector_store=vector_store),
        llm_config=AugLLMConfig(temperature=0.7),
        top_k=5
    )

    result = await rag.arun("What is machine learning?")

From documents::

    rag = SimpleRAG.from_documents(
        documents=my_documents,
        embedding_config=embedding_config,
        llm_config=AugLLMConfig()
    )


.. autolink-examples:: agents.rag.simple.multi_agent_simple_rag
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.simple.multi_agent_simple_rag.SimpleRAG


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleRAG:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAG {
        node [shape=record];
        "SimpleRAG" [label="SimpleRAG"];
        "haive.agents.multi.agent.MultiAgent" -> "SimpleRAG";
      }

.. autoclass:: agents.rag.simple.multi_agent_simple_rag.SimpleRAG
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.simple.multi_agent_simple_rag.demo




.. rubric:: Related Links

.. autolink-examples:: agents.rag.simple.multi_agent_simple_rag
   :collapse:
   
.. autolink-skip:: next
