agents.rag.factories.compatible_rag_factory_simple
==================================================

.. py:module:: agents.rag.factories.compatible_rag_factory_simple

.. autoapi-nested-parse::

   Simplified Compatible RAG Factory.

   Simplified version without legacy functions that have import issues.


   .. autolink-examples:: agents.rag.factories.compatible_rag_factory_simple
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory_simple.logger


Classes
-------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory_simple.CompatibleRAGFactory
   agents.rag.factories.compatible_rag_factory_simple.RAGComponent
   agents.rag.factories.compatible_rag_factory_simple.WorkflowPattern


Functions
---------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory_simple.create_plug_and_play_component
   agents.rag.factories.compatible_rag_factory_simple.get_component_compatibility_info


Module Contents
---------------

.. py:class:: CompatibleRAGFactory(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Compatible RAG Workflow')

   Factory for building RAG workflows with I/O schema compatibility.

   Initialize factory with documents and configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompatibleRAGFactory
      :collapse:

   .. py:method:: create_graded_hyde_workflow(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_search_tools: bool = False, **kwargs) -> haive.agents.multi.base.SequentialAgent
      :classmethod:


      Create workflow with HyDE and document grading.


      .. autolink-examples:: create_graded_hyde_workflow
         :collapse:


   .. py:method:: create_simple_workflow(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.multi.base.SequentialAgent
      :classmethod:


      Create simple RAG workflow.


      .. autolink-examples:: create_simple_workflow
         :collapse:


   .. py:attribute:: documents


   .. py:attribute:: llm_config


   .. py:attribute:: name
      :value: 'Compatible RAG Workflow'



.. py:class:: RAGComponent(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Available RAG component types for plug-and-play composition.


   .. autolink-examples:: RAGComponent
      :collapse:

   .. py:attribute:: ADAPTIVE_DECOMPOSITION
      :value: 'adaptive_decomposition'



   .. py:attribute:: ADVANCED_HALLUCINATION_GRADING
      :value: 'advanced_hallucination_grading'



   .. py:attribute:: COMPREHENSIVE_GRADING
      :value: 'comprehensive_grading'



   .. py:attribute:: CONTEXTUAL_DECOMPOSITION
      :value: 'contextual_decomposition'



   .. py:attribute:: CORRECTIVE_GENERATION
      :value: 'corrective_generation'



   .. py:attribute:: DOCUMENT_GRADING
      :value: 'document_grading'



   .. py:attribute:: FUSION_GENERATION
      :value: 'fusion_generation'



   .. py:attribute:: HALLUCINATION_GRADING
      :value: 'hallucination_grading'



   .. py:attribute:: HIERARCHICAL_DECOMPOSITION
      :value: 'hierarchical_decomposition'



   .. py:attribute:: HYDE_RETRIEVAL
      :value: 'hyde_retrieval'



   .. py:attribute:: MULTI_QUERY_RETRIEVAL
      :value: 'multi_query_retrieval'



   .. py:attribute:: QUERY_DECOMPOSITION
      :value: 'query_decomposition'



   .. py:attribute:: REALTIME_HALLUCINATION_GRADING
      :value: 'realtime_hallucination_grading'



   .. py:attribute:: SIMPLE_GENERATION
      :value: 'simple_generation'



   .. py:attribute:: SIMPLE_RETRIEVAL
      :value: 'simple_retrieval'



.. py:class:: WorkflowPattern(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Pre-defined workflow patterns.


   .. autolink-examples:: WorkflowPattern
      :collapse:

   .. py:attribute:: DECOMPOSED_GRADED
      :value: 'decomposed_graded'



   .. py:attribute:: FULL_PIPELINE
      :value: 'full_pipeline'



   .. py:attribute:: GRADED_HYDE
      :value: 'graded_hyde'



   .. py:attribute:: MODULAR_RAG
      :value: 'modular_rag'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:function:: create_plug_and_play_component(component_type: RAGComponent, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.simple.agent.SimpleAgent | haive.agents.rag.base.agent.BaseRAGAgent

   Create any RAG component as a standalone agent.


   .. autolink-examples:: create_plug_and_play_component
      :collapse:

.. py:function:: get_component_compatibility_info(component_type: RAGComponent) -> dict[str, list[str]]

   Get I/O schema information for a component type.


   .. autolink-examples:: get_component_compatibility_info
      :collapse:

.. py:data:: logger

