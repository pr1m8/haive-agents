"""Memory tools for save/search/KG operations.

Tools use closures to capture the store instance.
Designed for use with ReactAgent's tool-calling loop.
"""

import json
import logging
import uuid
from typing import Any

from langchain_core.tools import StructuredTool

logger = logging.getLogger(__name__)


def create_memory_tools(store: Any, user_id: str = "default") -> list[StructuredTool]:
    """Create memory tools bound to a specific store and user.

    Args:
        store: LangGraph BaseStore instance (InMemoryStore or PostgresStore)
        user_id: User ID for namespace scoping

    Returns:
        List of tools: [save_memory, search_memory, save_knowledge]
    """
    user_ns = ("user", user_id)
    kg_ns = ("kg", user_id)

    def save_memory(content: str, importance: str = "medium") -> str:
        """Save an important fact, preference, or detail about the user for future conversations.

        Use this when you learn something worth remembering:
        - User preferences (likes Python, prefers concise answers)
        - Personal facts (works at TechCorp, lives in NYC)
        - Important context (working on a web app, studying ML)

        Args:
            content: The memory to save (be specific and factual)
            importance: How important: 'low', 'medium', 'high', 'critical'
        """
        try:
            key = str(uuid.uuid4())
            store.put(user_ns, key, {"content": content, "importance": importance, "type": "memory"})
            logger.info(f"Saved memory: {content[:50]}...")
            return f"Memory saved: {content}"
        except Exception as e:
            logger.warning(f"Failed to save memory: {e}")
            return f"Error saving memory: {e}"

    def search_memory(query: str) -> str:
        """Search for relevant memories about the user.

        Use this to recall information from previous conversations.

        Args:
            query: What to search for (e.g. 'programming preferences', 'work projects')
        """
        try:
            results = store.search(user_ns, query=query, limit=5)
            if not results:
                return "No relevant memories found."
            memories = []
            for item in results:
                val = item.value if hasattr(item, "value") else item
                content = val.get("content", str(val)) if isinstance(val, dict) else str(val)
                memories.append(f"- {content}")
            return "Relevant memories:\n" + "\n".join(memories)
        except Exception as e:
            logger.warning(f"Failed to search memory: {e}")
            return f"Error searching: {e}"

    def save_knowledge(subject: str, predicate: str, object_: str) -> str:
        """Save a knowledge graph triple (subject-predicate-object fact).

        Use this for structured facts like relationships and attributes.
        Examples:
            save_knowledge("Python", "was created by", "Guido van Rossum")
            save_knowledge("user", "works at", "TechCorp")
            save_knowledge("user", "prefers", "TypeScript over JavaScript")

        Args:
            subject: The entity (e.g. 'Python', 'user')
            predicate: The relationship (e.g. 'was created by', 'works at')
            object_: The target (e.g. 'Guido van Rossum', 'TechCorp')
        """
        try:
            key = f"{subject}_{predicate}_{object_}".replace(" ", "_")[:100]
            store.put(
                kg_ns,
                key,
                {
                    "subject": subject,
                    "predicate": predicate,
                    "object": object_,
                    "type": "kg_triple",
                },
            )
            return f"Knowledge saved: {subject} {predicate} {object_}"
        except Exception as e:
            logger.warning(f"Failed to save knowledge: {e}")
            return f"Error: {e}"

    def search_knowledge(query: str) -> str:
        """Search knowledge graph triples for structured facts.

        Use this to find specific relationships and facts stored as triples.

        Args:
            query: What to search for (e.g. 'works at', 'prefers', 'user')
        """
        try:
            results = store.search(kg_ns, query=query, limit=10)
            if not results:
                return "No knowledge triples found."
            triples = []
            for item in results:
                val = item.value if hasattr(item, "value") else item
                if isinstance(val, dict) and val.get("type") == "kg_triple":
                    triples.append(f"- {val['subject']} {val['predicate']} {val['object']}")
                else:
                    triples.append(f"- {val}")
            return "Knowledge graph facts:\n" + "\n".join(triples)
        except Exception as e:
            logger.warning(f"Failed to search knowledge: {e}")
            return f"Error: {e}"

    return [
        StructuredTool.from_function(save_memory, name="save_memory", description=save_memory.__doc__),
        StructuredTool.from_function(search_memory, name="search_memory", description=search_memory.__doc__),
        StructuredTool.from_function(save_knowledge, name="save_knowledge", description=save_knowledge.__doc__),
        StructuredTool.from_function(search_knowledge, name="search_knowledge", description=search_knowledge.__doc__),
    ]
