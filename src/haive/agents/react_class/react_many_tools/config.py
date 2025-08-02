import logging
from typing import Any, Literal
from haive.agents.rag.base.config import BaseRAGConfig
from haive.agents.react.react.config import ReactAgentConfig
from haive.agents.react.react_many_tools.state import ReactManyToolsState
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.retriever import BaseRetrieverConfig, VectorStoreRetrieverConfig
from haive.core.engine.vectorstore import VectorStoreConfig
from langchain_core.embeddings import Embeddings
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, model_validator

class ReactManyToolsConfig(ReactAgentConfig):
    """Configuration for React Agent with many tools.

    Extends ReactAgentConfig with features for handling large numbers of tools
    and integrates with RAG capabilities.
    """
    state_schema: type[BaseModel] = Field(default=ReactManyToolsState)
    max_tools_per_request: int = Field(default=10, description='Maximum number of tools to expose to the agent per request')
    tool_categories: dict[str, list[str]] = Field(default_factory=dict, description='Mapping of category names to lists of tool names')
    embeddings_model: Embeddings | None = Field(default=None, description='Embedding model for semantic tool filtering')
    tool_selection_mode: Literal['semantic', 'categorical', 'keyword', 'auto'] = Field(default='auto', description='Method for selecting relevant tools')
    tool_filter_prompt: str | None = Field(default=None, description='Prompt for the filtering LLM to select tools')
    rag_config: BaseRAGConfig | None = Field(default=None, description='Optional RAG configuration for document retrieval')
    retriever_config: BaseRetrieverConfig | VectorStoreConfig | None = Field(default=None, description='Configuration for the retriever component')
    answer_generator: AugLLMConfig | None = Field(default=None, description='Configuration for the answer generator')
    use_rag: bool = Field(default=True, description='Whether to enable RAG capabilities')

    @model_validator(mode='after')
    def ensure_valid_configuration(self) -> Any:
        """Validate the configuration."""
        super().ensure_valid_configuration()
        if self.tool_categories:
            tool_names = {tool.name for tool in self.tools if isinstance(tool, BaseTool)}
            for category, tools in self.tool_categories.items():
                unknown_tools = [t for t in tools if t not in tool_names]
                if unknown_tools:
                    logging.warning(f'Unknown tools in category {category}: {unknown_tools}')
        if not self.tool_filter_prompt:
            self.tool_filter_prompt = 'You are a tool selection assistant.\nGiven a user query and available tools, select the most relevant tools that would help answer the query.\nChoose no more than {max_tools} tools.\n\nAvailable tools:\n{tool_descriptions}\n\nUser query: {query}\n\nSelected tools (tool names only, one per line):'
        if self.use_rag:
            if not self.rag_config and (not self.retriever_config):
                logging.warning('RAG is enabled but no retriever_config or rag_config provided')
            if isinstance(self.retriever_config, VectorStoreConfig):
                self.retriever_config = VectorStoreRetrieverConfig(name=f'retriever_for_{self.name}', vector_store_config=self.retriever_config)
        return self