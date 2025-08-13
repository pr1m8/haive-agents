
:py:mod:`agents.rag.simple.clean_simple_rag`
============================================

.. py:module:: agents.rag.simple.clean_simple_rag

SimpleRAG - Clean MultiAgent Implementation.

This is the CORRECT SimpleRAG implementation using the clean MultiAgent pattern.

Architecture:
    SimpleRAG extends MultiAgent from clean.py
    agents = [BaseRAGAgent, SimpleAgent]  # List initialization (converted to dict)
    execution_mode = "sequential" (default)

    Flow: BaseRAGAgent retrieves documents → SimpleAgent generates answers

Key Features:
- Uses the clean MultiAgent pattern from haive.agents.multi.clean
- Proper list initialization: MultiAgent(agents=[retriever, generator])
- Sequential execution (retriever → generator)
- No custom routing needed - uses intelligent routing
- Proper Pydantic patterns with no __init__ overrides
- Comprehensive field validation and documentation

.. rubric:: Examples

Basic usage::

    from haive.agents.rag.simple.clean_simple_rag import SimpleRAG
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.core.engine.vectorstore import VectorStoreConfig

    rag = SimpleRAG(
        name="qa_assistant",
        retriever_config=VectorStoreConfig(vector_store=vector_store),
        llm_config=AugLLMConfig(temperature=0.7),
        top_k=5
    )

    result = await rag.arun("What is machine learning?")

With structured output::

    class QAResponse(BaseModel):
        answer: str
        sources: List[str]
        confidence: float

    rag = SimpleRAG(
        name="structured_qa",
        retriever_config=retriever_config,
        llm_config=llm_config,
        structured_output_model=QAResponse
    )

From documents::

    rag = SimpleRAG.from_documents(
        documents=my_documents,
        embedding_config=embedding_config,
        llm_config=AugLLMConfig()
    )


.. autolink-examples:: agents.rag.simple.clean_simple_rag
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.simple.clean_simple_rag.SimpleRAG


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

.. autoclass:: agents.rag.simple.clean_simple_rag.SimpleRAG
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.simple.clean_simple_rag.demo




.. rubric:: Related Links

.. autolink-examples:: agents.rag.simple.clean_simple_rag
   :collapse:
   
.. autolink-skip:: next
