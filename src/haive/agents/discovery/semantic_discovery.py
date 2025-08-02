"""Semantic Discovery Engine with Vector-Based Tool Selection.

This module implements semantic discovery capabilities inspired by LangGraph's
many-tools pattern, using vector embeddings to match tools and components
based on query content and semantic similarity.

Key Features:
- Vector-based tool discovery and ranking
- Semantic capability matching
- Query analysis and tool recommendation
- Dynamic tool binding and selection
- Context-aware component matching
"""
import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Protocol
from haive.core.registry import ComponentMetadata
from haive.core.graph.patterns.base import ComponentType
from haive.core.models.embeddings.base import BaseEmbeddingConfig
from haive.core.engine.embeddings import EmbeddingsEngineConfig
from haive.core.engine.vectorstore.vectorstore import VectorStoreConfig
EnhancedComponentRegistry = Any

def create_component_registry(**kwargs):
    return None
try:
    from haive.core.utils.haive_discovery import discover_tools, get_all_tools
    UnifiedHaiveDiscovery = Any
except ImportError:
    discover_tools = lambda: []
    get_all_tools = lambda: []
    UnifiedHaiveDiscovery = Any
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from langchain_openai import OpenAIEmbeddings
from pydantic import BaseModel, Field, model_validator, ConfigDict
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from haive.agents.discovery.selection_strategies import AdaptiveSelectionStrategy, BaseSelectionStrategy, CapabilityBasedStrategy, ContextualSelectionStrategy, EnsembleSelectionStrategy, SemanticSelectionStrategy
BaseSelectionStrategy = None
SemanticSelectionStrategy = None
CapabilityBasedStrategy = None
AdaptiveSelectionStrategy = None
ContextualSelectionStrategy = None
EnsembleSelectionStrategy = None

def _lazy_import_strategies():
    """Lazy import to avoid circular imports."""
    global BaseSelectionStrategy, SemanticSelectionStrategy, CapabilityBasedStrategy
    global AdaptiveSelectionStrategy, ContextualSelectionStrategy, EnsembleSelectionStrategy
    if BaseSelectionStrategy is None:
        from haive.agents.discovery.selection_strategies import BaseSelectionStrategy as _BaseSelectionStrategy, SemanticSelectionStrategy as _SemanticSelectionStrategy, CapabilityBasedStrategy as _CapabilityBasedStrategy, AdaptiveSelectionStrategy as _AdaptiveSelectionStrategy, ContextualSelectionStrategy as _ContextualSelectionStrategy, EnsembleSelectionStrategy as _EnsembleSelectionStrategy
        BaseSelectionStrategy = _BaseSelectionStrategy
        SemanticSelectionStrategy = _SemanticSelectionStrategy
        CapabilityBasedStrategy = _CapabilityBasedStrategy
        AdaptiveSelectionStrategy = _AdaptiveSelectionStrategy
        ContextualSelectionStrategy = _ContextualSelectionStrategy
        EnsembleSelectionStrategy = _EnsembleSelectionStrategy
logger = logging.getLogger(__name__)

class DiscoveryMode(str, Enum):
    """Different modes for semantic discovery."""
    SIMILARITY = 'similarity'
    CAPABILITY = 'capability'
    HYBRID = 'hybrid'
    CONTEXTUAL = 'contextual'
    MEMORY_ENHANCED = 'memory_enhanced'

class ToolSelectionStrategy(str, Enum):
    """Strategies for tool selection."""
    TOP_K = 'top_k'
    THRESHOLD = 'threshold'
    HYBRID = 'hybrid'
    ADAPTIVE = 'adaptive'
    CONTEXTUAL = 'contextual'

@dataclass
class QueryAnalysis:
    """Analysis of user query for tool selection."""
    original_query: str
    extracted_keywords: list[str]
    inferred_capabilities: list[str]
    domain_tags: list[str]
    complexity_score: float
    intent_classification: str
    suggested_tools: list[str] = field(default_factory=list)

class VectorBasedToolSelector(BaseModel):
    """Selects tools using vector similarity search."""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    vector_store_config: VectorStoreConfig | None = Field(default=None, description='Vector store configuration for tool embeddings')
    similarity_threshold: float = Field(default=0.7, description='Minimum similarity score for tool selection')
    max_tools: int = Field(default=5, description='Maximum number of tools to select')
    component_registry: EnhancedComponentRegistry | None = Field(default=None, description='Enhanced component registry')

    @model_validator(mode='after')
    def setup_vector_store(self) -> 'VectorBasedToolSelector':
        """Setup vector store if not provided."""
        if self.component_registry is None:
            self.component_registry = create_component_registry(use_embeddings=True, embedding_provider='openai:text-embedding-3-small')
        return self

    def index_tools(self, tools: list[Any]) -> None:
        """Index tools in vector store and component registry."""
        if self.component_registry:
            for tool in tools:
                self.component_registry.register_component(tool, ComponentType.TOOL)
        documents = []
        for tool in tools:
            name = getattr(tool, 'name', str(tool))
            description = getattr(tool, 'description', '')
            doc_text = f'Tool: {name}\nDescription: {description}'
            if hasattr(tool, 'capabilities'):
                doc_text += f'\nCapabilities: {', '.join(tool.capabilities)}'
            doc = Document(page_content=doc_text, metadata={'tool_name': name, 'type': 'tool', 'capabilities': getattr(tool, 'capabilities', [])})
            documents.append(doc)
        if documents and self.vector_store_config:
            vector_store = self.vector_store_config.create_vectorstore()
            vector_store.add_documents(documents)
            logger.info(f'Indexed {len(documents)} tools in vector store')

    async def select_tools(self, query: str, strategy: ToolSelectionStrategy=ToolSelectionStrategy.TOP_K) -> list[ComponentMetadata]:
        """Select tools based on query using specified strategy."""
        if strategy == ToolSelectionStrategy.TOP_K:
            return await self._select_top_k(query)
        if strategy == ToolSelectionStrategy.THRESHOLD:
            return await self._select_by_threshold(query)
        if strategy == ToolSelectionStrategy.HYBRID:
            return await self._select_hybrid(query)
        if self.component_registry:
            results = self.component_registry.search_components(query, component_types=[ComponentType.TOOL], max_results=self.max_tools)
            return results
        return await self._select_top_k(query)

    async def _select_top_k(self, query: str) -> list[ComponentMetadata]:
        """Select top K most similar tools."""
        if self.component_registry:
            return self.component_registry.search_components(query, component_types=[ComponentType.TOOL], max_results=self.max_tools)
        if not self.vector_store_config:
            return []
        vector_store = self.vector_store_config.create_vectorstore()
        results = vector_store.similarity_search_with_score(query, k=self.max_tools)
        selected_tools = []
        for doc, score in results:
            metadata = ComponentMetadata(name=doc.metadata.get('tool_name', 'Unknown'), component_type=ComponentType.TOOL, description=doc.page_content, capabilities=doc.metadata.get('capabilities', []), similarity_score=score)
            selected_tools.append(metadata)
        return selected_tools

    async def _select_by_threshold(self, query: str) -> list[ComponentMetadata]:
        """Select tools above similarity threshold."""
        if self.component_registry:
            all_results = self.component_registry.search_components(query, component_types=[ComponentType.TOOL], max_results=20)
            return [r for r in all_results if r.similarity_score >= self.similarity_threshold]
        if not self.vector_store_config:
            return []
        vector_store = self.vector_store_config.create_vectorstore()
        results = vector_store.similarity_search_with_score(query, k=20)
        selected_tools = []
        for doc, score in results:
            if score >= self.similarity_threshold:
                metadata = ComponentMetadata(name=doc.metadata.get('tool_name', 'Unknown'), component_type=ComponentType.TOOL, description=doc.page_content, capabilities=doc.metadata.get('capabilities', []), similarity_score=score)
                selected_tools.append(metadata)
        return selected_tools[:self.max_tools]

    async def _select_hybrid(self, query: str) -> list[ComponentMetadata]:
        """Hybrid selection combining similarity and capability matching."""
        if self.component_registry:
            similar_tools = await self._select_top_k(query)
            query_analysis = QueryAnalyzer().analyze_query(query)
            capability_tools = self.component_registry.find_by_capabilities(query_analysis.inferred_capabilities, component_types=[ComponentType.TOOL])
            all_tools = {t.name: t for t in similar_tools}
            for tool in capability_tools:
                if tool.name not in all_tools:
                    all_tools[tool.name] = tool
                else:
                    existing = all_tools[tool.name]
                    existing.capability_match_score = tool.capability_match_score
                    existing.composite_score = existing.similarity_score * 0.6 + existing.capability_match_score * 0.4
            sorted_tools = sorted(all_tools.values(), key=lambda t: t.composite_score, reverse=True)
            return sorted_tools[:self.max_tools]
        return await self._select_top_k(query)

class QueryAnalyzer(BaseModel):
    """Analyzes queries to extract relevant information for tool selection."""
    capability_keywords: dict[str, list[str]] = Field(default_factory=lambda: {'search': ['search', 'find', 'look', 'query', 'discover'], 'analysis': ['analyze', 'examine', 'inspect', 'evaluate', 'assess'], 'generation': ['generate', 'create', 'make', 'produce', 'build'], 'transformation': ['transform', 'convert', 'change', 'modify', 'alter'], 'communication': ['send', 'email', 'notify', 'message', 'communicate'], 'storage': ['save', 'store', 'persist', 'cache', 'archive'], 'retrieval': ['get', 'fetch', 'retrieve', 'load', 'read'], 'processing': ['process', 'handle', 'execute', 'run', 'perform']}, description='Mapping of capabilities to keywords')

    def analyze_query(self, query: str) -> QueryAnalysis:
        """Analyze query to extract useful information."""
        query_lower = query.lower()
        words = query_lower.split()
        extracted_keywords = [w for w in words if len(w) > 3]
        inferred_capabilities = []
        for capability, keywords in self.capability_keywords.items():
            if any((keyword in query_lower for keyword in keywords)):
                inferred_capabilities.append(capability)
        domain_tags = self._extract_domain_tags(query_lower)
        complexity_score = self._calculate_complexity(query)
        intent = self._classify_intent(query_lower, inferred_capabilities)
        return QueryAnalysis(original_query=query, extracted_keywords=extracted_keywords, inferred_capabilities=inferred_capabilities, domain_tags=domain_tags, complexity_score=complexity_score, intent_classification=intent)

    def _extract_domain_tags(self, query: str) -> list[str]:
        """Extract domain-specific tags from query."""
        domains = {'web': ['web', 'website', 'url', 'internet', 'online'], 'file': ['file', 'document', 'pdf', 'csv', 'excel'], 'data': ['data', 'dataset', 'database', 'table', 'record'], 'api': ['api', 'endpoint', 'service', 'rest', 'graphql'], 'email': ['email', 'mail', 'smtp', 'inbox', 'message']}
        tags = []
        for domain, keywords in domains.items():
            if any((keyword in query for keyword in keywords)):
                tags.append(domain)
        return tags

    def _calculate_complexity(self, query: str) -> float:
        """Calculate query complexity score."""
        words = query.split()
        complexity = min(len(words) / 20.0, 1.0)
        if any((conj in query.lower() for conj in ['and', 'or', 'then', 'but'])):
            complexity += 0.2
        if any((step in query.lower() for step in ['first', 'then', 'finally', 'after'])):
            complexity += 0.3
        return min(complexity, 1.0)

    def _classify_intent(self, query: str, capabilities: list[str]) -> str:
        """Classify the primary intent of the query."""
        if not capabilities:
            return 'unknown'
        intent_priority = ['generation', 'analysis', 'search', 'transformation', 'communication', 'retrieval', 'processing', 'storage']
        for intent in intent_priority:
            if intent in capabilities:
                return intent
        return capabilities[0] if capabilities else 'unknown'

class CapabilityMatcher(BaseModel):
    """Matches tools based on required capabilities."""
    capability_matrix: dict[str, list[str]] = Field(default_factory=dict, description='Matrix mapping tools to capabilities')
    component_registry: EnhancedComponentRegistry | None = Field(default=None, description='Component registry for capability lookup')

    def build_capability_matrix(self, tools: list[Any]) -> None:
        """Build capability matrix from tools."""
        for tool in tools:
            name = getattr(tool, 'name', str(tool))
            capabilities = getattr(tool, 'capabilities', [])
            if not capabilities:
                capabilities = self._infer_capabilities(tool)
            self.capability_matrix[name] = capabilities

    def match_tools(self, required_capabilities: list[str], optional_capabilities: list[str] | None=None) -> list[tuple[str, float]]:
        """Match tools based on capabilities."""
        if self.component_registry:
            results = self.component_registry.find_by_capabilities(required_capabilities, component_types=[ComponentType.TOOL])
            return [(r.name, r.capability_match_score) for r in results]
        matches = []
        for tool_name, tool_capabilities in self.capability_matrix.items():
            required_match = all((cap in tool_capabilities for cap in required_capabilities))
            if not required_match:
                continue
            score = len(set(required_capabilities).intersection(set(tool_capabilities)))
            if optional_capabilities:
                optional_match = sum((1 for cap in optional_capabilities if cap in tool_capabilities))
                score += optional_match * 0.5
            matches.append((tool_name, score))
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches

    def _infer_capabilities(self, tool: Any) -> list[str]:
        """Infer capabilities from tool attributes."""
        capabilities = []
        name = getattr(tool, 'name', '').lower()
        description = getattr(tool, 'description', '').lower()
        patterns = {'search': ['search', 'find', 'query', 'lookup'], 'read': ['read', 'load', 'fetch', 'get'], 'write': ['write', 'save', 'store', 'persist'], 'process': ['process', 'transform', 'convert', 'analyze'], 'communicate': ['send', 'email', 'notify', 'message']}
        for capability, keywords in patterns.items():
            if any((kw in name or kw in description for kw in keywords)):
                capabilities.append(capability)
        return capabilities if capabilities else ['general']

class SemanticDiscoveryEngine(BaseModel):
    """Main semantic discovery engine combining all capabilities."""
    vector_selector: VectorBasedToolSelector = Field(default_factory=VectorBasedToolSelector, description='Vector-based tool selector')
    query_analyzer: QueryAnalyzer = Field(default_factory=QueryAnalyzer, description='Query analyzer')
    capability_matcher: CapabilityMatcher = Field(default_factory=CapabilityMatcher, description='Capability matcher')
    selection_strategy: BaseSelectionStrategy = Field(default_factory=lambda: (_lazy_import_strategies(), SemanticSelectionStrategy)[1](), description='Selection strategy to use')
    component_registry: EnhancedComponentRegistry | None = Field(default=None, description='Shared component registry')

    @model_validator(mode='after')
    def setup_registry(self) -> 'SemanticDiscoveryEngine':
        """Setup shared component registry."""
        if self.component_registry is None:
            self.component_registry = create_component_registry(use_embeddings=True)
        self.vector_selector.component_registry = self.component_registry
        self.capability_matcher.component_registry = self.component_registry
        return self

    async def discover_tools(self, tools: list[Any] | None=None, haive_root: str | None=None) -> list[ComponentMetadata]:
        """Discover available tools."""
        if tools is None:
            if haive_root:
                discovery = UnifiedHaiveDiscovery(haive_root)
                discovered = discovery.discover_all()
                tools = discovered.get('tools', [])
            else:
                tool_components = discover_tools()
                tools = get_all_tools(tool_components)
        tool_metadata = []
        for tool in tools:
            metadata = self.component_registry.register_component(tool, ComponentType.TOOL)
            tool_metadata.append(metadata)
        self.vector_selector.index_tools(tools)
        self.capability_matcher.build_capability_matrix(tools)
        logger.info(f'Discovered and indexed {len(tools)} tools')
        return tool_metadata

    async def semantic_tool_selection(self, query: str, max_tools: int=5, strategy: ToolSelectionStrategy=ToolSelectionStrategy.HYBRID, capability_filter: list[str] | None=None) -> tuple[list[ComponentMetadata], QueryAnalysis]:
        """Perform semantic tool selection for a query."""
        query_analysis = self.query_analyzer.analyze_query(query)
        if self.component_registry:
            selected_tools = self.component_registry.search_components(query, component_types=[ComponentType.TOOL], max_results=max_tools * 2)
            if capability_filter:
                filtered_tools = []
                for tool in selected_tools:
                    if any((cap in tool.capabilities for cap in capability_filter)):
                        filtered_tools.append(tool)
                selected_tools = filtered_tools
            if hasattr(self.selection_strategy, 'select'):
                context = {'query': query, 'query_analysis': query_analysis, 'capability_filter': capability_filter}
                selected_tools = self.selection_strategy.select(selected_tools[:max_tools * 2], context, max_tools)
            else:
                selected_tools = selected_tools[:max_tools]
        else:
            selected_tools = await self.vector_selector.select_tools(query, strategy)
        query_analysis.suggested_tools = [t.name for t in selected_tools]
        return (selected_tools, query_analysis)

    async def get_tools_for_capabilities(self, required_capabilities: list[str], optional_capabilities: list[str] | None=None, max_tools: int=5) -> list[ComponentMetadata]:
        """Get tools that match specific capabilities."""
        if self.component_registry:
            all_capabilities = required_capabilities.copy()
            if optional_capabilities:
                all_capabilities.extend(optional_capabilities)
            results = self.component_registry.find_by_capabilities(all_capabilities, component_types=[ComponentType.TOOL])
            filtered = []
            for result in results:
                if all((cap in result.capabilities for cap in required_capabilities)):
                    filtered.append(result)
            return filtered[:max_tools]
        matches = self.capability_matcher.match_tools(required_capabilities, optional_capabilities)
        results = []
        for tool_name, score in matches[:max_tools]:
            metadata = ComponentMetadata(name=tool_name, component_type=ComponentType.TOOL, description=f'Tool: {tool_name}', capabilities=self.capability_matcher.capability_matrix.get(tool_name, []), capability_match_score=score)
            results.append(metadata)
        return results

    def update_selection_strategy(self, strategy: BaseSelectionStrategy | str) -> None:
        """Update the selection strategy."""
        if isinstance(strategy, str):
            _lazy_import_strategies()
            strategy_map = {'semantic': SemanticSelectionStrategy, 'capability': CapabilityBasedStrategy, 'adaptive': AdaptiveSelectionStrategy, 'contextual': ContextualSelectionStrategy, 'ensemble': EnsembleSelectionStrategy}
            strategy_class = strategy_map.get(strategy, SemanticSelectionStrategy)
            self.selection_strategy = strategy_class()
        else:
            self.selection_strategy = strategy

def create_semantic_discovery() -> SemanticDiscoveryEngine:
    """Create a semantic discovery engine with default configuration."""
    return SemanticDiscoveryEngine()