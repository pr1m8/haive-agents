from haive.core.models.llm.base import AzureLLMConfig, LLMConfig
from langchain_core.documents import BaseDocumentTransformer, Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_neo4j.graphs.graph_document import GraphDocument

# ASYNC MODES.


class GraphTransformer(BaseDocumentTransformer):
    """A document transformer that transforms a document into a graph."""

    def transform_documents(
        self,
        documents: list[Document],
        llm_config: LLMConfig = AzureLLMConfig(),
        allowed_nodes: list[str] = [],
        allowed_relationships: list[str] | list[tuple[str, str, str]] = [],
        prompt: ChatPromptTemplate | None = None,
        strict_mode: bool = True,
        node_properties: bool | list[str] = [],
        relationship_properties: bool | list[str] = [],
        ignore_tool_usage: bool = True,
        additional_instructions: str = "",
    ) -> list[GraphDocument]:
        """Transform a document into a graph.

        Args:
            documents: The documents to transform.
            llm_config: The LLM configuration.
            allowed_nodes: The allowed nodes.
            allowed_relationships: The allowed relationships.
            prompt: The prompt.
            strict_mode: The strict mode.
            node_properties: The node properties.
            relationship_properties: The relationship properties.
            ignore_tool_usage: The ignore tool usage.
            additional_instructions: The additional instructions.
        """
        llm = llm_config.instantiate()

        print(
            "DEBUG: Type of allowed_relationships ->", type(allowed_relationships)
        )  # ✅ Debugging statement

        if not isinstance(allowed_relationships, list):
            raise TypeError("allowed_relationships must be a list!")

        # ✅ Check if the LLM supports function calling before passing properties
        graph_transformer_kwargs = {
            "llm": llm,
            "allowed_nodes": allowed_nodes,
            "allowed_relationships": allowed_relationships,
            "prompt": prompt,
            "strict_mode": strict_mode,
            "ignore_tool_usage": ignore_tool_usage,
            "additional_instructions": additional_instructions,
        }

        if getattr(
            llm, "supports_function_calling", False
        ):  # ✅ Only pass if supported
            graph_transformer_kwargs["node_properties"] = node_properties
            graph_transformer_kwargs["relationship_properties"] = (
                relationship_properties
            )

        graph_transformer = LLMGraphTransformer(**graph_transformer_kwargs)

        return graph_transformer.convert_to_graph_documents(documents)
