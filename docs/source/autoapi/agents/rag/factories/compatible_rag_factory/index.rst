
:py:mod:`agents.rag.factories.compatible_rag_factory`
=====================================================

.. py:module:: agents.rag.factories.compatible_rag_factory

Compatible RAG Workflow Factory.

Generic factory for building composable RAG workflows based on I/O schema compatibility.
Uses the enhanced multi-agent base with automatic compatibility checking, agent replacement,
and workflow optimization. Allows replacing agents by compatible I/O schemas.

Key Features:
    - Automatic I/O schema compatibility analysis
    - Agent replacement based on schema compatibility
    - Workflow optimization for better field flow
    - Component-based RAG workflow building
    - Integration with search tools from haive.tools
    - Enhanced system prompts and grading


.. autolink-examples:: agents.rag.factories.compatible_rag_factory
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory.CompatibleRAGFactory
   agents.rag.factories.compatible_rag_factory.RAGComponent
   agents.rag.factories.compatible_rag_factory.WorkflowPattern


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibleRAGFactory:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibleRAGFactory {
        node [shape=record];
        "CompatibleRAGFactory" [label="CompatibleRAGFactory"];
      }

.. autoclass:: agents.rag.factories.compatible_rag_factory.CompatibleRAGFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGComponent:

   .. graphviz::
      :align: center

      digraph inheritance_RAGComponent {
        node [shape=record];
        "RAGComponent" [label="RAGComponent"];
        "str" -> "RAGComponent";
        "enum.Enum" -> "RAGComponent";
      }

.. autoclass:: agents.rag.factories.compatible_rag_factory.RAGComponent
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGComponent** is an Enum defined in ``agents.rag.factories.compatible_rag_factory``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WorkflowPattern:

   .. graphviz::
      :align: center

      digraph inheritance_WorkflowPattern {
        node [shape=record];
        "WorkflowPattern" [label="WorkflowPattern"];
        "str" -> "WorkflowPattern";
        "enum.Enum" -> "WorkflowPattern";
      }

.. autoclass:: agents.rag.factories.compatible_rag_factory.WorkflowPattern
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **WorkflowPattern** is an Enum defined in ``agents.rag.factories.compatible_rag_factory``.



Functions
---------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory._calculate_avg_relevance
   agents.rag.factories.compatible_rag_factory._extract_relevant_docs
   agents.rag.factories.compatible_rag_factory.create_compatible_adaptive_rag
   agents.rag.factories.compatible_rag_factory.create_compatible_corrective_rag
   agents.rag.factories.compatible_rag_factory.create_compatible_hyde_rag
   agents.rag.factories.compatible_rag_factory.create_compatible_rag_workflow
   agents.rag.factories.compatible_rag_factory.create_compatible_self_rag
   agents.rag.factories.compatible_rag_factory.create_plug_and_play_component
   agents.rag.factories.compatible_rag_factory.example_modular_rag_usage
   agents.rag.factories.compatible_rag_factory.get_component_compatibility_info








.. py:function:: create_plug_and_play_component(component_type: RAGComponent, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Create any RAG component as a standalone agent.

   This function allows creating any component independently for plug-and-play usage.

   :param component_type: Type of component to create
   :param documents: Documents for components that need them
   :param llm_config: LLM configuration
   :param \*\*kwargs: Component-specific arguments

   :returns: Standalone agent that can be plugged into any workflow

   .. rubric:: Example

   # Create standalone components
   decomposer = create_plug_and_play_component(
       RAGComponent.ADAPTIVE_DECOMPOSITION, docs
   )
   hallucination_grader = create_plug_and_play_component(
       RAGComponent.ADVANCED_HALLUCINATION_GRADING, docs
   )

   # Use with any workflow
   workflow = SequentialAgent(agents=[decomposer, retriever, hallucination_grader])


   .. autolink-examples:: create_plug_and_play_component
      :collapse:


.. py:function:: get_component_compatibility_info(component_type: RAGComponent) -> dict[str, list[str]]

   Get I/O schema information for a component type.

   :param component_type: Component to get info for

   :returns: Dict with 'inputs' and 'outputs' lists


   .. autolink-examples:: get_component_compatibility_info
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.factories.compatible_rag_factory
   :collapse:
   
.. autolink-skip:: next
