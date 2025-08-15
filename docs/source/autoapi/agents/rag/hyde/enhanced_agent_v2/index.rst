agents.rag.hyde.enhanced_agent_v2
=================================

.. py:module:: agents.rag.hyde.enhanced_agent_v2

.. autoapi-nested-parse::

   Enhanced HyDE RAG Agent v2 with Advanced Prompt Selection and Multi-Document Generation.

   This version integrates the new enhanced prompt system with:
   - Automatic prompt type selection based on query analysis
   - Multi-document generation from different perspectives
   - Improved separation of generation from parsing
   - Domain-specific prompt templates
   - Ensemble retrieval using multiple hypothetical documents


   .. autolink-examples:: agents.rag.hyde.enhanced_agent_v2
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent_v2.AdaptiveHyDEGenerator
   agents.rag.hyde.enhanced_agent_v2.DomainAnalysisAgent
   agents.rag.hyde.enhanced_agent_v2.EnhancedHyDERAGAgentV2
   agents.rag.hyde.enhanced_agent_v2.EnhancedHyDERetrieverV2
   agents.rag.hyde.enhanced_agent_v2.EnsembleDocumentParser
   agents.rag.hyde.enhanced_agent_v2.EnsembleHyDERetriever
   agents.rag.hyde.enhanced_agent_v2.HyDEAgentConfig
   agents.rag.hyde.enhanced_agent_v2.HyDEDocumentAnalyzer
   agents.rag.hyde.enhanced_agent_v2.HyDEGenerationMode
   agents.rag.hyde.enhanced_agent_v2.MultiDomainHyDERetriever
   agents.rag.hyde.enhanced_agent_v2.QueryAnalysisAgent


Functions
---------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent_v2.create_enhanced_hyde_v2
   agents.rag.hyde.enhanced_agent_v2.create_ensemble_hyde
   agents.rag.hyde.enhanced_agent_v2.create_multi_perspective_hyde


Module Contents
---------------

.. py:class:: AdaptiveHyDEGenerator(llm_config: haive.core.models.llm.base.LLMConfig, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Generator that adapts its prompt based on query analysis.


   .. autolink-examples:: AdaptiveHyDEGenerator
      :collapse:

   .. py:method:: run(input_data: dict[str, Any]) -> dict[str, Any]

      Generate document using adaptively selected prompt.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: target_length
      :type:  int
      :value: None



.. py:class:: DomainAnalysisAgent(llm_config: haive.core.models.llm.base.LLMConfig, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Analyzes queries to determine relevant domains for multi-domain generation.


   .. autolink-examples:: DomainAnalysisAgent
      :collapse:

.. py:class:: EnhancedHyDERAGAgentV2

   Bases: :py:obj:`haive.agents.multi.enhanced_sequential_agent.SequentialAgent`, :py:obj:`haive.core.common.mixins.tool_route_mixin.ToolRouteMixin`


   Enhanced HyDE RAG Agent with advanced prompt selection and multi-document generation.

   Key Features:
   - Automatic prompt type selection based on query analysis
   - Multi-document generation from different perspectives/domains
   - Ensemble retrieval using multiple hypothetical documents
   - Proper separation of generation from parsing
   - Configurable generation strategies
   - Enhanced error handling and fallback mechanisms


   .. autolink-examples:: EnhancedHyDERAGAgentV2
      :collapse:

   .. py:method:: _create_ensemble_pipeline(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_model: str | None, config: HyDEAgentConfig) -> list[haive.agents.base.agent.Agent]
      :classmethod:


      Create pipeline for ensemble document generation.


      .. autolink-examples:: _create_ensemble_pipeline
         :collapse:


   .. py:method:: _create_multi_domain_pipeline(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_model: str | None, config: HyDEAgentConfig) -> list[haive.agents.base.agent.Agent]
      :classmethod:


      Create pipeline for multi-domain document generation.


      .. autolink-examples:: _create_multi_domain_pipeline
         :collapse:


   .. py:method:: _create_multi_perspective_pipeline(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_model: str | None, config: HyDEAgentConfig) -> list[haive.agents.base.agent.Agent]
      :classmethod:


      Create pipeline for multi-perspective document generation.


      .. autolink-examples:: _create_multi_perspective_pipeline
         :collapse:


   .. py:method:: _create_single_document_pipeline(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_model: str | None, config: HyDEAgentConfig) -> list[haive.agents.base.agent.Agent]
      :classmethod:


      Create pipeline for single document generation.


      .. autolink-examples:: _create_single_document_pipeline
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, embedding_model: str | None = None, config: HyDEAgentConfig | None = None, **kwargs) -> EnhancedHyDERAGAgentV2
      :classmethod:


      Create Enhanced HyDE RAG Agent v2 from documents.

      :param documents: Documents to index for retrieval
      :param llm_config: LLM configuration
      :param embedding_model: Optional embedding model
      :param config: HyDE agent configuration
      :param \*\*kwargs: Additional arguments

      :returns: Configured Enhanced HyDE RAG Agent v2


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: setup_hyde_agent() -> EnhancedHyDERAGAgentV2

      Setup HyDE agent with enhanced prompts.


      .. autolink-examples:: setup_hyde_agent
         :collapse:


   .. py:attribute:: config
      :type:  HyDEAgentConfig
      :value: None



.. py:class:: EnhancedHyDERetrieverV2

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Enhanced retriever with better state handling and fallback mechanisms.


   .. autolink-examples:: EnhancedHyDERetrieverV2
      :collapse:

   .. py:method:: build_graph() -> Any


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: embedding_model
      :type:  str | None
      :value: None



.. py:class:: EnsembleDocumentParser(llm_config: haive.core.models.llm.base.LLMConfig, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Parses ensemble document output into individual documents.


   .. autolink-examples:: EnsembleDocumentParser
      :collapse:

.. py:class:: EnsembleHyDERetriever

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Retriever that handles multiple documents for ensemble retrieval.


   .. autolink-examples:: EnsembleHyDERetriever
      :collapse:

   .. py:method:: build_graph() -> Any


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: embedding_model
      :type:  str | None
      :value: None



   .. py:attribute:: ensemble_mode
      :type:  bool
      :value: None



   .. py:attribute:: perspectives
      :type:  list[str]
      :value: None



.. py:class:: HyDEAgentConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for Enhanced HyDE RAG Agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HyDEAgentConfig
      :collapse:

   .. py:attribute:: auto_select_prompt
      :type:  bool
      :value: None



   .. py:attribute:: enable_query_rewriting
      :type:  bool
      :value: None



   .. py:attribute:: generation_mode
      :type:  HyDEGenerationMode
      :value: None



   .. py:attribute:: num_ensemble_docs
      :type:  int
      :value: None



   .. py:attribute:: perspectives
      :type:  list[haive.agents.rag.common.query_constructors.hyde.enhanced_prompts.HyDEPerspective]
      :value: None



   .. py:attribute:: prompt_type
      :type:  haive.agents.rag.common.query_constructors.hyde.enhanced_prompts.HyDEPromptType
      :value: None



   .. py:attribute:: target_length
      :type:  int
      :value: None



   .. py:attribute:: use_structured_analysis
      :type:  bool
      :value: None



.. py:class:: HyDEDocumentAnalyzer(llm_config: haive.core.models.llm.base.LLMConfig, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Analyzes generated hypothetical documents and extracts structured information.


   .. autolink-examples:: HyDEDocumentAnalyzer
      :collapse:

   .. py:attribute:: enable_query_rewriting
      :type:  bool
      :value: None



.. py:class:: HyDEGenerationMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Different modes for HyDE document generation.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HyDEGenerationMode
      :collapse:

   .. py:attribute:: ENSEMBLE
      :value: 'ensemble'



   .. py:attribute:: MULTI_DOMAIN
      :value: 'multi_domain'



   .. py:attribute:: MULTI_PERSPECTIVE
      :value: 'multi_perspective'



   .. py:attribute:: SINGLE
      :value: 'single'



.. py:class:: MultiDomainHyDERetriever

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Retriever that handles documents from multiple domains.


   .. autolink-examples:: MultiDomainHyDERetriever
      :collapse:

   .. py:method:: build_graph() -> Any


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: domain_types
      :type:  list[str]
      :value: None



   .. py:attribute:: embedding_model
      :type:  str | None
      :value: None



.. py:class:: QueryAnalysisAgent(llm_config: haive.core.models.llm.base.LLMConfig, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent that analyzes queries and selects appropriate prompt types.


   .. autolink-examples:: QueryAnalysisAgent
      :collapse:

   .. py:method:: run(input_data: dict[str, Any]) -> dict[str, Any]

      Run query analysis and add prompt type selection.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: auto_select
      :type:  bool
      :value: None



   .. py:attribute:: default_prompt_type
      :type:  haive.agents.rag.common.query_constructors.hyde.enhanced_prompts.HyDEPromptType
      :value: None



.. py:function:: create_enhanced_hyde_v2(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, generation_mode: HyDEGenerationMode = HyDEGenerationMode.SINGLE, auto_select_prompt: bool = True, **kwargs) -> EnhancedHyDERAGAgentV2

   Create Enhanced HyDE RAG Agent v2 with specified configuration.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param generation_mode: Mode for document generation
   :param auto_select_prompt: Whether to auto-select prompt types
   :param \*\*kwargs: Additional configuration options

   :returns: Configured Enhanced HyDE RAG Agent v2


   .. autolink-examples:: create_enhanced_hyde_v2
      :collapse:

.. py:function:: create_ensemble_hyde(documents: list[langchain_core.documents.Document], num_docs: int = 3, llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> EnhancedHyDERAGAgentV2

   Create HyDE agent with ensemble document generation.

   :param documents: Documents for retrieval
   :param num_docs: Number of documents to generate
   :param llm_config: LLM configuration
   :param \*\*kwargs: Additional options

   :returns: Ensemble HyDE agent


   .. autolink-examples:: create_ensemble_hyde
      :collapse:

.. py:function:: create_multi_perspective_hyde(documents: list[langchain_core.documents.Document], perspectives: list[haive.agents.rag.common.query_constructors.hyde.enhanced_prompts.HyDEPerspective], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> EnhancedHyDERAGAgentV2

   Create HyDE agent with multi-perspective generation.

   :param documents: Documents for retrieval
   :param perspectives: List of perspectives to use
   :param llm_config: LLM configuration
   :param \*\*kwargs: Additional options

   :returns: Multi-perspective HyDE agent


   .. autolink-examples:: create_multi_perspective_hyde
      :collapse:

