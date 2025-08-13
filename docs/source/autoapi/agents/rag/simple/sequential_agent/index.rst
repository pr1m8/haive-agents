
:py:mod:`agents.rag.simple.sequential_agent`
============================================

.. py:module:: agents.rag.simple.sequential_agent

SimpleRAG - Sequential MultiAgent Implementation (BaseRAG → SimpleAgent).

This is the correct SimpleRAG implementation following the sequential multi-agent pattern:
    SimpleRAG = Sequential[BaseRAGAgent, SimpleAgent]

Architecture:
1. **BaseRAGAgent**: Performs document retrieval from vector store
2. **SimpleAgent**: Generates structured answers from retrieved documents
3. **Sequential Execution**: BaseRAG output → SimpleAgent input

Key Features:
- **Sequential Multi-Agent Pattern**: Proper composition of specialized agents
- **Pydantic Best Practices**: No __init__ overrides, field validation, inheritance
- **Type Safety**: Full type hints and proper agent composition
- **Real Component Integration**: Uses actual BaseRAGAgent and SimpleAgent
- **Structured Output**: Support for custom response models
- **Comprehensive Documentation**: Google-style docstrings with examples

Design Philosophy:
- **Composition over Monolith**: Uses existing proven agents
- **Clear Separation of Concerns**: Retrieval vs Generation
- **Reusable Components**: Each agent can be used independently
- **Testable Architecture**: Easy to test each component separately

.. rubric:: Examples

Basic usage::

    from haive.agents.rag.simple import SimpleRAG
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.core.engine.vectorstore import VectorStoreConfig

    rag = SimpleRAG(
        name="qa_assistant",
        retriever_config=VectorStoreConfig(vector_store=your_vector_store),
        llm_config=AugLLMConfig(temperature=0.7),
        top_k=5
    )

    result = await rag.arun("What is machine learning?")

With structured output::

    class QAResponse(BaseModel):
        answer: str
        sources: list[str]
        confidence: float

    rag = SimpleRAG(
        name="structured_qa",
        retriever_config=retriever_config,
        llm_config=AugLLMConfig(),
        structured_output_model=QAResponse
    )


.. autolink-examples:: agents.rag.simple.sequential_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.simple.sequential_agent.RAGResponse
   agents.rag.simple.sequential_agent.SimpleRAG


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGResponse:

   .. graphviz::
      :align: center

      digraph inheritance_RAGResponse {
        node [shape=record];
        "RAGResponse" [label="RAGResponse"];
        "pydantic.BaseModel" -> "RAGResponse";
      }

.. autopydantic_model:: agents.rag.simple.sequential_agent.RAGResponse
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

   Inheritance diagram for SimpleRAG:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAG {
        node [shape=record];
        "SimpleRAG" [label="SimpleRAG"];
        "pydantic.BaseModel" -> "SimpleRAG";
      }

.. autopydantic_model:: agents.rag.simple.sequential_agent.SimpleRAG
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

.. autolink-examples:: agents.rag.simple.sequential_agent
   :collapse:
   
.. autolink-skip:: next
