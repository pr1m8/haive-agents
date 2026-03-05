import concurrent.futures
import json
import logging
import time
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langgraph.graph import END, START
from pydantic import Field, PrivateAttr

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.rag.dynamic.models import DataSourceConfig

logger = logging.getLogger(__name__)


class DynamicRAGAgent(BaseRAGAgent):
    """Implements a dynamic RAG pipeline that routes queries to appropriate data sources."""

    data_sources: dict[str, DataSourceConfig] = Field(
        default_factory=dict, description="Map of data source names to configurations"
    )
    query_router_config: AugLLMConfig | None = Field(
        default=None, description="Configuration for query router"
    )
    result_merger_config: AugLLMConfig | None = Field(
        default=None, description="Configuration for result merger"
    )
    default_source: str | None = Field(
        default=None, description="Default data source if routing fails"
    )
    enable_parallel_retrieval: bool = Field(
        default=False, description="Whether to retrieve from multiple sources in parallel"
    )
    max_sources_per_query: int = Field(
        default=3, description="Maximum number of sources to query simultaneously"
    )

    _retrievers: dict = PrivateAttr(default_factory=dict)
    _router: Any = PrivateAttr(default=None)
    _merger: Any = PrivateAttr(default=None)

    def setup_agent(self) -> None:
        """Initialize dynamic RAG components."""
        super().setup_agent()
        self._init_data_sources()
        self._init_router()
        self._init_merger()

    def _init_data_sources(self):
        """Initialize all configured data sources."""
        self._retrievers = {}
        for name, source_config in self.data_sources.items():
            try:
                self._retrievers[name] = source_config.create_retriever()
                logger.info(f"Initialized data source: {name}")
            except Exception as e:
                logger.exception(f"Failed to initialize data source {name}: {e}")

    def _init_router(self):
        """Initialize the query router."""
        if self.query_router_config:
            self._router = self.query_router_config.create_runnable()
        else:
            self._router = None

    def _init_merger(self):
        """Initialize the result merger."""
        if self.result_merger_config:
            self._merger = self.result_merger_config.create_runnable()
        else:
            self._merger = None

    def route_query(self, state: dict[str, Any]):
        """Route the query to appropriate data sources."""
        query = state.query

        if not self._router:
            # Use default source or all sources if no router
            if (
                self.default_source
                and self.default_source in self._retrievers
            ):
                selected_sources = [self.default_source]
            else:
                selected_sources = list(self._retrievers.keys())

            return {"selected_sources": selected_sources}

        # Use router to select data sources
        try:
            # Prepare input for router with available sources
            source_descriptions = {
                name: config.description
                for name, config in self.data_sources.items()
            }

            router_result = self._router.invoke(
                {"query": query, "available_sources": source_descriptions}
            )

            if isinstance(router_result, dict):
                selected_sources = router_result.get("selected_sources", [])
                explanation = router_result.get("explanation", "")
            elif isinstance(router_result, list):
                selected_sources = router_result
                explanation = ""
            else:
                # Try to parse from string
                try:
                    selected_sources = json.loads(router_result)
                    if not isinstance(selected_sources, list):
                        selected_sources = [router_result]
                    explanation = ""
                except BaseException:
                    selected_sources = [router_result]
                    explanation = ""

            # Validate that sources exist
            validated_sources = [s for s in selected_sources if s in self._retrievers]

            # Limit number of sources if needed
            if len(validated_sources) > self.max_sources_per_query:
                validated_sources = validated_sources[
                    : self.max_sources_per_query
                ]

            if not validated_sources and self.default_source:
                validated_sources = [self.default_source]

            return {
                "selected_sources": validated_sources,
                "routing_explanation": explanation,
            }

        except Exception as e:
            logger.exception(f"Error in query routing: {e}")

            # Fall back to default source
            if (
                self.default_source
                and self.default_source in self._retrievers
            ):
                return {"selected_sources": [self.default_source]}

            # Or use all sources as last resort
            return {"selected_sources": list(self._retrievers.keys())}

    def retrieve_from_sources(self, state: dict[str, Any]):
        """Retrieve documents from selected sources."""
        query = state.query
        selected_sources = state.selected_sources

        source_documents = {}
        source_metrics = {}

        if self.enable_parallel_retrieval:
            # Implement parallel retrieval with concurrent.futures or asyncio

            def retrieve_from_source(source_name) -> Any:
                """Retrieve From Source.

                Args:
                    source_name: [TODO: Add description]

                Returns:
                    [TODO: Add return description]
                """
                try:
                    retriever = self._retrievers.get(source_name)
                    if retriever:
                        start_time = time.time()
                        docs = retriever.invoke(query)
                        retrieve_time = time.time() - start_time

                        return (
                            source_name,
                            docs,
                            {
                                "retrieve_time": retrieve_time,
                                "document_count": len(docs),
                            },
                        )
                    return source_name, [], {"error": "Retriever not found"}
                except Exception as e:
                    return source_name, [], {"error": str(e)}

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(retrieve_from_source, source)
                    for source in selected_sources
                ]

                for future in concurrent.futures.as_completed(futures):
                    try:
                        source_name, docs, metrics = future.result()
                        source_documents[source_name] = docs
                        source_metrics[source_name] = metrics
                    except Exception as e:
                        logger.exception(f"Error in parallel retrieval: {e}")

        else:
            # Sequential retrieval
            for source_name in selected_sources:
                retriever = self._retrievers.get(source_name)
                if retriever:
                    try:
                        start_time = time.time()
                        docs = retriever.invoke(query)
                        retrieve_time = time.time() - start_time

                        source_documents[source_name] = docs
                        source_metrics[source_name] = {
                            "retrieve_time": retrieve_time,
                            "document_count": len(docs),
                        }
                    except Exception as e:
                        logger.exception(f"Error retrieving from {source_name}: {e}")
                        source_documents[source_name] = []
                        source_metrics[source_name] = {"error": str(e)}

        return {"source_documents": source_documents, "source_metrics": source_metrics}

    def merge_results(self, state: dict[str, Any]):
        """Merge results from multiple sources."""
        source_documents = state.source_documents

        if not source_documents:
            return {"retrieved_documents": []}

        # If only one source has results, use them directly
        if len(source_documents) == 1:
            source_name = next(iter(source_documents.keys()))
            return {"retrieved_documents": source_documents[source_name]}

        # Flatten all documents
        all_docs = []
        for source_name, docs in source_documents.items():
            # Add source to metadata
            for doc in docs:
                doc.metadata["source"] = source_name
            all_docs.extend(docs)

        if not self._merger:
            # Simple deduplication and selection
            unique_docs = {}
            for doc in all_docs:
                doc_id = doc.metadata.get("id", hash(doc.page_content))
                if doc_id not in unique_docs:
                    unique_docs[doc_id] = doc

            # Sort by "relevance" if available in metadata
            sorted_docs = sorted(
                unique_docs.values(),
                key=lambda d: d.metadata.get("relevance", 0),
                reverse=True,
            )

            # Limit to a reasonable number
            return {"retrieved_documents": sorted_docs[:10]}

        # Use merger for more sophisticated merging
        try:
            # Group documents by source for the merger
            docs_by_source = {
                source: docs for source, docs in source_documents.items() if docs
            }

            merged_docs = self._merger.invoke(
                {"query": state.query, "docs_by_source": docs_by_source}
            )

            if isinstance(merged_docs, list):
                return {"retrieved_documents": merged_docs}
            if isinstance(merged_docs, dict) and "documents" in merged_docs:
                return {"retrieved_documents": merged_docs["documents"]}
            logger.error(f"Unexpected merger output format: {type(merged_docs)}")
            # Fall back to simple deduplication
            unique_docs = {}
            for doc in all_docs:
                doc_id = doc.metadata.get("id", hash(doc.page_content))
                if doc_id not in unique_docs:
                    unique_docs[doc_id] = doc

            return {"retrieved_documents": list(unique_docs.values())}

        except Exception as e:
            logger.exception(f"Error in result merging: {e}")
            # Fall back to all documents
            return {"retrieved_documents": all_docs}

    def build_graph(self) -> BaseGraph:
        """Build the Dynamic RAG workflow graph."""
        graph = BaseGraph(name=self.name or "DynamicRAGAgent")

        # Add nodes
        graph.add_node("route_query", self.route_query)
        graph.add_node("retrieve_from_sources", self.retrieve_from_sources)
        graph.add_node("merge_results", self.merge_results)

        # Connect nodes
        graph.add_edge(START, "route_query")
        graph.add_edge("route_query", "retrieve_from_sources")
        graph.add_edge("retrieve_from_sources", "merge_results")
        graph.add_edge("merge_results", END)

        return graph
