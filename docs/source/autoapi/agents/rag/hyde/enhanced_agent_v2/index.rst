
:py:mod:`agents.rag.hyde.enhanced_agent_v2`
===========================================

.. py:module:: agents.rag.hyde.enhanced_agent_v2

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveHyDEGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveHyDEGenerator {
        node [shape=record];
        "AdaptiveHyDEGenerator" [label="AdaptiveHyDEGenerator"];
        "haive.agents.simple.agent.SimpleAgent" -> "AdaptiveHyDEGenerator";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.AdaptiveHyDEGenerator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DomainAnalysisAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DomainAnalysisAgent {
        node [shape=record];
        "DomainAnalysisAgent" [label="DomainAnalysisAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "DomainAnalysisAgent";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.DomainAnalysisAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedHyDERAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedHyDERAGAgentV2 {
        node [shape=record];
        "EnhancedHyDERAGAgentV2" [label="EnhancedHyDERAGAgentV2"];
        "haive.agents.multi.enhanced_sequential_agent.SequentialAgent" -> "EnhancedHyDERAGAgentV2";
        "haive.core.common.mixins.tool_route_mixin.ToolRouteMixin" -> "EnhancedHyDERAGAgentV2";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.EnhancedHyDERAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedHyDERetrieverV2:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedHyDERetrieverV2 {
        node [shape=record];
        "EnhancedHyDERetrieverV2" [label="EnhancedHyDERetrieverV2"];
        "haive.agents.base.agent.Agent" -> "EnhancedHyDERetrieverV2";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.EnhancedHyDERetrieverV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnsembleDocumentParser:

   .. graphviz::
      :align: center

      digraph inheritance_EnsembleDocumentParser {
        node [shape=record];
        "EnsembleDocumentParser" [label="EnsembleDocumentParser"];
        "haive.agents.simple.agent.SimpleAgent" -> "EnsembleDocumentParser";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.EnsembleDocumentParser
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnsembleHyDERetriever:

   .. graphviz::
      :align: center

      digraph inheritance_EnsembleHyDERetriever {
        node [shape=record];
        "EnsembleHyDERetriever" [label="EnsembleHyDERetriever"];
        "haive.agents.base.agent.Agent" -> "EnsembleHyDERetriever";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.EnsembleHyDERetriever
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HyDEAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_HyDEAgentConfig {
        node [shape=record];
        "HyDEAgentConfig" [label="HyDEAgentConfig"];
        "pydantic.BaseModel" -> "HyDEAgentConfig";
      }

.. autopydantic_model:: agents.rag.hyde.enhanced_agent_v2.HyDEAgentConfig
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

   Inheritance diagram for HyDEDocumentAnalyzer:

   .. graphviz::
      :align: center

      digraph inheritance_HyDEDocumentAnalyzer {
        node [shape=record];
        "HyDEDocumentAnalyzer" [label="HyDEDocumentAnalyzer"];
        "haive.agents.simple.agent.SimpleAgent" -> "HyDEDocumentAnalyzer";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.HyDEDocumentAnalyzer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HyDEGenerationMode:

   .. graphviz::
      :align: center

      digraph inheritance_HyDEGenerationMode {
        node [shape=record];
        "HyDEGenerationMode" [label="HyDEGenerationMode"];
        "str" -> "HyDEGenerationMode";
        "enum.Enum" -> "HyDEGenerationMode";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.HyDEGenerationMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HyDEGenerationMode** is an Enum defined in ``agents.rag.hyde.enhanced_agent_v2``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiDomainHyDERetriever:

   .. graphviz::
      :align: center

      digraph inheritance_MultiDomainHyDERetriever {
        node [shape=record];
        "MultiDomainHyDERetriever" [label="MultiDomainHyDERetriever"];
        "haive.agents.base.agent.Agent" -> "MultiDomainHyDERetriever";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.MultiDomainHyDERetriever
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryAnalysisAgent:

   .. graphviz::
      :align: center

      digraph inheritance_QueryAnalysisAgent {
        node [shape=record];
        "QueryAnalysisAgent" [label="QueryAnalysisAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "QueryAnalysisAgent";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent_v2.QueryAnalysisAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent_v2.create_enhanced_hyde_v2
   agents.rag.hyde.enhanced_agent_v2.create_ensemble_hyde
   agents.rag.hyde.enhanced_agent_v2.create_multi_perspective_hyde

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.hyde.enhanced_agent_v2
   :collapse:
   
.. autolink-skip:: next
