agents.rag.factories.compatible_rag_factory
===========================================

.. py:module:: agents.rag.factories.compatible_rag_factory

.. autoapi-nested-parse::

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


Functions
---------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory.create_plug_and_play_component
   agents.rag.factories.compatible_rag_factory.get_component_compatibility_info


Module Contents
---------------

.. py:class:: CompatibleRAGFactory(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_search_tools: bool = False, default_embedding_model: str | None = None)

   Factory for building RAG workflows with I/O schema compatibility.

   Uses the enhanced multi-agent base with automatic compatibility checking,
   agent replacement, and workflow optimization.

   Initialize factory with common dependencies.

   :param documents: Document collection for retrieval
   :param llm_config: LLM configuration for all components
   :param enable_search_tools: Whether to integrate external search tools
   :param default_embedding_model: Default embedding model for vector stores


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompatibleRAGFactory
      :collapse:

   .. py:method:: _build_adaptive_decomposition(**kwargs) -> haive.agents.rag.query_decomposition.agent.AdaptiveQueryDecomposerAgent

      Build adaptive query decomposition agent.


      .. autolink-examples:: _build_adaptive_decomposition
         :collapse:


   .. py:method:: _build_adaptive_pattern(**kwargs) -> ConditionalAgent

      Adaptive: Query Analysis → Route to Best Strate.....gy.


      .. autolink-examples:: _build_adaptive_pattern
         :collapse:


   .. py:method:: _build_adaptive_rag(**kwargs) -> haive.agents.rag.adaptive.agent.AdaptiveRAGAgent

      Build adaptive RAG agent.


      .. autolink-examples:: _build_adaptive_rag
         :collapse:


   .. py:method:: _build_advanced_hallucination_grading(**kwargs) -> haive.agents.rag.hallucination_grading.agent.AdvancedHallucinationGraderAgent

      Build advanced hallucination grading agent.


      .. autolink-examples:: _build_advanced_hallucination_grading
         :collapse:


   .. py:method:: _build_agentic_pattern(**kwargs) -> ConditionalAgent

      Agentic: Tool Selection → Execute → Aggre.....gate.


      .. autolink-examples:: _build_agentic_pattern
         :collapse:


   .. py:method:: _build_answer_generation(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build answer generation agent.


      .. autolink-examples:: _build_answer_generation
         :collapse:


   .. py:method:: _build_arxiv_search(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build ArXiv search agent.


      .. autolink-examples:: _build_arxiv_search
         :collapse:


   .. py:method:: _build_base_retrieval(**kwargs) -> haive.agents.rag.base.agent.BaseRAGAgent

      Build basic retrieval agent.


      .. autolink-examples:: _build_base_retrieval
         :collapse:


   .. py:method:: _build_comprehensive_grading(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build comprehensive document grading agent.


      .. autolink-examples:: _build_comprehensive_grading
         :collapse:


   .. py:method:: _build_contextual_decomposition(**kwargs) -> haive.agents.rag.query_decomposition.agent.ContextualQueryDecomposerAgent

      Build contextual query decomposition agent.


      .. autolink-examples:: _build_contextual_decomposition
         :collapse:


   .. py:method:: _build_corrective_pattern(**kwargs) -> ConditionalAgent

      CRAG: Retrieval → Grade → Route (Refine/Web/Conti.....nue).


      .. autolink-examples:: _build_corrective_pattern
         :collapse:


   .. py:method:: _build_corrective_rag(**kwargs) -> haive.agents.rag.corrective.agent_v2.CorrectiveRAGAgentV2

      Build corrective RAG agent.


      .. autolink-examples:: _build_corrective_rag
         :collapse:


   .. py:method:: _build_custom_workflow(components: list[RAGComponent], routing_conditions: dict[str, collections.abc.Callable] | None = None, **kwargs) -> SequentialAgent | ConditionalAgent

      Build custom workflow from component list.


      .. autolink-examples:: _build_custom_workflow
         :collapse:


   .. py:method:: _build_document_grading(**kwargs) -> haive.agents.rag.document_grading.agent.DocumentGradingAgent

      Build document grading agent.


      .. autolink-examples:: _build_document_grading
         :collapse:


   .. py:method:: _build_fusion_generation(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build fusion answer generation for multi-source results.


      .. autolink-examples:: _build_fusion_generation
         :collapse:


   .. py:method:: _build_fusion_pattern(**kwargs) -> SequentialAgent

      Fusion: Multi-Source → Rank Fusion → Gene.....rate.


      .. autolink-examples:: _build_fusion_pattern
         :collapse:


   .. py:method:: _build_graded_pattern(**kwargs) -> SequentialAgent

      Graded: Retrieval → Document Grading → Answer Genera.....tion.


      .. autolink-examples:: _build_graded_pattern
         :collapse:


   .. py:method:: _build_hallucination_detection(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build basic hallucination detection agent.


      .. autolink-examples:: _build_hallucination_detection
         :collapse:


   .. py:method:: _build_hallucination_grading(**kwargs) -> haive.agents.rag.hallucination_grading.agent.HallucinationGraderAgent

      Build standalone hallucination grading agent.


      .. autolink-examples:: _build_hallucination_grading
         :collapse:


   .. py:method:: _build_hierarchical_decomposition(**kwargs) -> haive.agents.rag.query_decomposition.agent.HierarchicalQueryDecomposerAgent

      Build hierarchical query decomposition agent.


      .. autolink-examples:: _build_hierarchical_decomposition
         :collapse:


   .. py:method:: _build_hyde_pattern(**kwargs) -> SequentialAgent

      HyDE: Query → Hypothetical Doc → Retrieval → .....Answer.


      .. autolink-examples:: _build_hyde_pattern
         :collapse:


   .. py:method:: _build_hyde_rag(**kwargs) -> haive.agents.rag.hyde.agent_v2.HyDERAGAgentV2

      Build HyDE RAG agent.


      .. autolink-examples:: _build_hyde_rag
         :collapse:


   .. py:method:: _build_multi_query_pattern(**kwargs) -> SequentialAgent

      Multi-Query: Query Expansion → Parallel Retrieval → An.....swer.


      .. autolink-examples:: _build_multi_query_pattern
         :collapse:


   .. py:method:: _build_multi_query_rag(**kwargs) -> haive.agents.rag.multi_query.agent.MultiQueryRAGAgent

      Build multi-query RAG agent.


      .. autolink-examples:: _build_multi_query_rag
         :collapse:


   .. py:method:: _build_quality_assessment(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build quality assessment agent.


      .. autolink-examples:: _build_quality_assessment
         :collapse:


   .. py:method:: _build_query_analysis(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build query analysis agent.


      .. autolink-examples:: _build_query_analysis
         :collapse:


   .. py:method:: _build_query_decomposition(**kwargs) -> haive.agents.rag.query_decomposition.agent.QueryDecomposerAgent

      Build basic query decomposition agent.


      .. autolink-examples:: _build_query_decomposition
         :collapse:


   .. py:method:: _build_query_expansion(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build query expansion agent.


      .. autolink-examples:: _build_query_expansion
         :collapse:


   .. py:method:: _build_realtime_hallucination_grading(**kwargs) -> haive.agents.rag.hallucination_grading.agent.RealtimeHallucinationGraderAgent

      Build realtime hallucination grading agent.


      .. autolink-examples:: _build_realtime_hallucination_grading
         :collapse:


   .. py:method:: _build_simple_pattern(**kwargs) -> SequentialAgent

      Simple: Retrieval → Answer Generati.....on.


      .. autolink-examples:: _build_simple_pattern
         :collapse:


   .. py:method:: _build_simple_rag(**kwargs) -> haive.agents.rag.simple.agent.SimpleRAGAgent

      Build simple RAG agent.


      .. autolink-examples:: _build_simple_rag
         :collapse:


   .. py:method:: _build_web_search(**kwargs) -> haive.agents.simple.agent.SimpleAgent

      Build web search agent with tool integration.


      .. autolink-examples:: _build_web_search
         :collapse:


   .. py:method:: _create_input_mapper() -> collections.abc.Callable

      Create input mapping function.


      .. autolink-examples:: _create_input_mapper
         :collapse:


   .. py:method:: _create_output_mapper() -> collections.abc.Callable

      Create output mapping function.


      .. autolink-examples:: _create_output_mapper
         :collapse:


   .. py:method:: _suggest_component_replacements(workflow: SequentialAgent | ConditionalAgent) -> list[dict[str, Any]]

      Suggest component replacements for better compatibility.


      .. autolink-examples:: _suggest_component_replacements
         :collapse:


   .. py:method:: analyze_workflow_compatibility(workflow: SequentialAgent | ConditionalAgent) -> dict[str, Any]

      Analyze I/O compatibility of existing workflow.

      :param workflow: Workflow to analyze

      :returns: Compatibility analysis report


      .. autolink-examples:: analyze_workflow_compatibility
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with compatibility-aware callable sequence.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_agentic_search_workflow(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> ConditionalAgent
      :classmethod:


      Create agentic workflow with search tool integration.


      .. autolink-examples:: create_agentic_search_workflow
         :collapse:


   .. py:method:: create_decomposed_graded_workflow(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_hallucination_grading: bool = True, **kwargs) -> SequentialAgent
      :classmethod:


      Create Query Decomposition → Retrieval → Grading → Hallucination Check → Answer workflow.


      .. autolink-examples:: create_decomposed_graded_workflow
         :collapse:


   .. py:method:: create_from_schema_compatibility(component_sequence: list[RAGComponent], auto_optimize: bool = True, **kwargs) -> SequentialAgent

      Create workflow by chaining components with compatible I/O schemas.

      This is the core generic functionality - it analyzes I/O schemas
      and builds a compatible chain using the enhanced multi-agent base.

      :param component_sequence: Ordered list of components to chain
      :param auto_optimize: Whether to auto-optimize agent order
      :param \*\*kwargs: Additional configuration

      :returns: SequentialAgent with compatible component chain


      .. autolink-examples:: create_from_schema_compatibility
         :collapse:


   .. py:method:: create_full_pipeline_workflow(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> SequentialAgent
      :classmethod:


      Create comprehensive pipeline with all major components.

      Pipeline: Decomposition → HyDE → Retrieval → Grading → Hallucination Check → Answer


      .. autolink-examples:: create_full_pipeline_workflow
         :collapse:


   .. py:method:: create_graded_hyde_workflow(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_search_tools: bool = False, **kwargs) -> SequentialAgent
      :classmethod:


      Create HyDE → Comprehensive Grading → Answer workflow.


      .. autolink-examples:: create_graded_hyde_workflow
         :collapse:


   .. py:method:: create_modular_rag_workflow(documents: list[langchain_core.documents.Document], components: list[RAGComponent], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> SequentialAgent
      :classmethod:


      Create custom workflow from list of components.

      This is the most generic method - just pass the components you want!


      .. autolink-examples:: create_modular_rag_workflow
         :collapse:


   .. py:method:: create_workflow(pattern: WorkflowPattern, components: list[RAGComponent] | None = None, routing_conditions: dict[str, collections.abc.Callable] | None = None, **kwargs) -> SequentialAgent | ConditionalAgent | ParallelAgent

      Create a workflow based on pattern and components.

      :param pattern: Workflow pattern to use
      :param components: Optional component overrides
      :param routing_conditions: Conditional routing logic
      :param \*\*kwargs: Additional configuration

      :returns: Configured multi-agent workflow


      .. autolink-examples:: create_workflow
         :collapse:


   .. py:method:: replace_agent_in_workflow(workflow: SequentialAgent | ConditionalAgent, target_agent_name: str, replacement_component: RAGComponent, **kwargs) -> bool

      Replace an agent in existing workflow based on I/O compatibility.

      Uses the enhanced multi-agent base compatibility checking.

      :param workflow: Existing workflow to modify
      :param target_agent_name: Name of agent to replace
      :param replacement_component: New component to use
      :param \*\*kwargs: Configuration for new component

      :returns: True if replacement successful


      .. autolink-examples:: replace_agent_in_workflow
         :collapse:


   .. py:method:: suggest_workflow_optimizations(workflow: SequentialAgent | ConditionalAgent) -> dict[str, Any]

      Suggest optimizations for workflow based on I/O compatibility.

      :param workflow: Workflow to optimize

      :returns: Optimization suggestions


      .. autolink-examples:: suggest_workflow_optimizations
         :collapse:


   .. py:attribute:: _component_builders


   .. py:attribute:: _pattern_builders


   .. py:attribute:: default_embedding_model
      :value: None



   .. py:attribute:: documents


   .. py:attribute:: enable_search_tools
      :value: False



   .. py:attribute:: llm_config


.. py:class:: RAGComponent

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available RAG components for composition.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGComponent
      :collapse:

   .. py:attribute:: ADAPTIVE_DECOMPOSITION
      :value: 'adaptive_decomposition'



   .. py:attribute:: ADAPTIVE_RAG
      :value: 'adaptive_rag'



   .. py:attribute:: ADVANCED_HALLUCINATION_GRADING
      :value: 'advanced_hallucination_grading'



   .. py:attribute:: ANSWER_GENERATION
      :value: 'answer_generation'



   .. py:attribute:: ARXIV_SEARCH
      :value: 'arxiv_search'



   .. py:attribute:: BASE_RETRIEVAL
      :value: 'base_retrieval'



   .. py:attribute:: COMPREHENSIVE_GRADING
      :value: 'comprehensive_grading'



   .. py:attribute:: CONTEXTUAL_DECOMPOSITION
      :value: 'contextual_decomposition'



   .. py:attribute:: CORRECTIVE_RAG
      :value: 'corrective_rag'



   .. py:attribute:: DOCUMENT_GRADING
      :value: 'document_grading'



   .. py:attribute:: FUSION_GENERATION
      :value: 'fusion_generation'



   .. py:attribute:: HALLUCINATION_DETECTION
      :value: 'hallucination_detection'



   .. py:attribute:: HALLUCINATION_GRADING
      :value: 'hallucination_grading'



   .. py:attribute:: HIERARCHICAL_DECOMPOSITION
      :value: 'hierarchical_decomposition'



   .. py:attribute:: HYDE_RAG
      :value: 'hyde_rag'



   .. py:attribute:: MULTI_QUERY_RAG
      :value: 'multi_query_rag'



   .. py:attribute:: QUALITY_ASSESSMENT
      :value: 'quality_assessment'



   .. py:attribute:: QUERY_ANALYSIS
      :value: 'query_analysis'



   .. py:attribute:: QUERY_DECOMPOSITION
      :value: 'query_decomposition'



   .. py:attribute:: QUERY_EXPANSION
      :value: 'query_expansion'



   .. py:attribute:: REALTIME_HALLUCINATION_GRADING
      :value: 'realtime_hallucination_grading'



   .. py:attribute:: SIMPLE_RAG
      :value: 'simple_rag'



   .. py:attribute:: WEB_SEARCH
      :value: 'web_search'



.. py:class:: WorkflowPattern

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Common workflow patterns from the architecture guide.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WorkflowPattern
      :collapse:

   .. py:attribute:: ADAPTIVE
      :value: 'adaptive'



   .. py:attribute:: AGENTIC
      :value: 'agentic'



   .. py:attribute:: CORRECTIVE
      :value: 'corrective'



   .. py:attribute:: FUSION
      :value: 'fusion'



   .. py:attribute:: GRADED
      :value: 'graded'



   .. py:attribute:: HYDE
      :value: 'hyde'



   .. py:attribute:: MULTI_QUERY
      :value: 'multi_query'



   .. py:attribute:: SIMPLE
      :value: 'simple'



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

