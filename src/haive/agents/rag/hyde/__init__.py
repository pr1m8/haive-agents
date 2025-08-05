"""Module exports."""

from haive.agents.rag.hyde.agent import HyDERAGAgent
from haive.agents.rag.hyde.agent_v2 import (
    HyDERAGAgentV2,
    HyDERetrieverAgent,
    build_graph,
    transform_to_query,
)
from haive.agents.rag.hyde.enhanced_agent import (
    EnhancedHyDERAGAgent,
    EnhancedHyDERetriever,
    adaptive_retrieval,
    build_graph,
    create_enhanced_hyde_agent,
    demonstrate_enhancement_vs_traditional,
)
# Commented out due to Pydantic schema issues with SequentialAgent inheritance
# from haive.agents.rag.hyde.enhanced_agent_v2 import (
#     AdaptiveHyDEGenerator,
#     DomainAnalysisAgent,
#     EnhancedHyDERAGAgentV2,
#     EnhancedHyDERetrieverV2,
#     EnsembleDocumentParser,
#     EnsembleHyDERetriever,
#     HyDEAgentConfig,
#     HyDEDocumentAnalyzer,
#     HyDEGenerationMode,
#     MultiDomainHyDERetriever,
#     QueryAnalysisAgent,
#     build_graph,
#     create_enhanced_hyde_v2,
#     create_ensemble_hyde,
#     create_multi_perspective_hyde,
#     ensemble_retrieval,
#     multi_domain_retrieval,
#     run,
#     setup_hyde_agent,
#     smart_retrieval)

__all__ = [
    # "AdaptiveHyDEGenerator",  # Commented out due to enhanced_agent_v2 issues
    # "DomainAnalysisAgent",
    "EnhancedHyDERAGAgent",
    # "EnhancedHyDERAGAgentV2",
    "EnhancedHyDERetriever",
    # "EnhancedHyDERetrieverV2",
    # "EnsembleDocumentParser",
    # "EnsembleHyDERetriever",
    # "HyDEAgentConfig",
    # "HyDEDocumentAnalyzer",
    # "HyDEGenerationMode",
    "HyDERAGAgent",
    "HyDERAGAgentV2",
    "HyDERetrieverAgent",
    # "MultiDomainHyDERetriever",
    # "QueryAnalysisAgent",
    "adaptive_retrieval",
    "build_graph",
    "create_enhanced_hyde_agent",
    # "create_enhanced_hyde_v2",
    # "create_ensemble_hyde",
    # "create_multi_perspective_hyde",
    "demonstrate_enhancement_vs_traditional",
    # "ensemble_retrieval",
    # "multi_domain_retrieval",
    # "run",
    # "setup_hyde_agent",
    # "smart_retrieval",
    "transform_to_query",
]
