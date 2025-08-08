from haive.core.schema.prebuilt.messages_state import MessagesState
from pydantic import ConfigDict, Field

from haive.agents.memory.models import KnowledgeTriple, MemoryItem


class MemoryAgentState(MessagesState):
    """State for Memory Agent, extending MessagesState.

    Adds fields for storing and retrieving memories.
    """

    # Loaded memories for the current conversation
    recall_memories: list[str] = Field(
        default_factory=list, description="Memories retrieved for context"
    )

    # Memories extracted from the current conversation
    extracted_memories: list[MemoryItem | KnowledgeTriple] = Field(
        default_factory=list,
        description="Memories extracted from the current conversation",
    )

    # User information
    user_id: str | None = Field(default=None, description="ID of the current user")

    # Memory operation flags
    should_save_memories: bool = Field(
        default=True, description="Whether to save memories"
    )
    memory_type: str = Field(
        default="unstructured", description="Type of memory: unstructured or structured"
    )

    model_config = ConfigDict(arbitrary_types_allowed=True)
