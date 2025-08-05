from haive.agents.long_term_memory.aug_llm import lt_mem_agent_aug_llm
from haive.agents.long_term_memory.state import LongTermMemoryState
from haive.agents.long_term_memory.tools import (
    search_recall_memories)
from haive.agents.react.agent import ReactAgent
from haive.agents.react.config import ReactAgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.vectorstore.base import VectorStoreConfig
from langchain_core.messages import get_buffer_string
import tiktoken
from langchain_core.runnables import RunnableConfig
from pydantic import Field
from typing import Dict, Any


class LongTermMemoryAgentConfig(ReactAgentConfig):
    """Config for the long term memory agent."""

    vs_config: VectorStoreConfig = Field(default_factory=VectorStoreConfig)
    state: LongTermMemoryState = Field(default_factory=LongTermMemoryState)
    state_schema: LongTermMemoryState = Field(default_factory=LongTermMemoryState)
    aug_llm: AugLLMConfig = Field(default_factory=lt_mem_agent_aug_llm)


class LongTermMemoryAgent(ReactAgent):
    """Agent for the long term memory."""

    config: LongTermMemoryAgentConfig

    def __init__(self, config: LongTermMemoryAgentConfig):
        super().__init__(config)

    def load_memories(self, state: Dict[str, Any], config: RunnableConfig) -> Dict[str, Any]:
        """Load memories for the current conversation.

        Args:
            state (Dict[str, Any]): The current state of the conversation.
            config (RunnableConfig): The runtime configuration for the agent.

        Returns:
            Dict[str, Any]: The updated state with loaded memories.
        """
        convo_str = get_buffer_string(state["messages"])
        # Truncate to 2048 tokens using tiktoken
        encoding = tiktoken.get_encoding("cl100k_base")  # Standard OpenAI encoding
        tokens = encoding.encode(convo_str)[:2048]
        convo_str = encoding.decode(tokens)
        recall_memories = search_recall_memories.invoke(convo_str, config)
        return {
            "recall_memories": recall_memories,
        }

    def setup_workflow(self) -> None:
        self.graph.add_node(load_memories)
        self.graph.add_node(agent)
        self.graph.add_node("tools", ToolNode(tools))

        # Add edges to the graph
        self.graph.add_edge(START, "load_memories")
        self.graph.add_edge("load_memories", "agent")
        self.graph.add_conditional_edges("agent", route_tools, ["tools", END])
        self.graph.add_edge("tools", "agent")

        # Compile the graph
