"""Knowledge Graph store integration for MemoryAgent.

Provides Neo4j-backed KG storage that works alongside the LangGraph store.
Triples stored in both:
- LangGraph store (for vector search/retrieval via memory tools)
- Neo4j (for graph traversal, Cypher queries, APOC algorithms)

Uses same env vars as graph_db RAG: NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD.
"""

import logging
import os
from typing import Any

from pydantic import BaseModel, Field

from .neo4j_schema import (
    QUERY_ENTITY_MEMORIES,
    QUERY_ENTITY_TRIPLES,
    QUERY_GRAPH_STATS,
    QUERY_NEIGHBORHOOD,
    QUERY_PATH,
    QUERY_USER_ENTITIES,
    QUERY_USER_TRIPLES,
    UPSERT_TRIPLE,
    init_schema,
)

logger = logging.getLogger(__name__)


class Neo4jKGConfig(BaseModel):
    """Configuration for Neo4j knowledge graph connection.

    Uses same env vars as haive.agents.rag.db_rag.graph_db for consistency:
    NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE
    """
    uri: str = Field(default="", description="Neo4j Bolt URI (or NEO4J_URI env var)")
    user: str = Field(default="", description="Neo4j username (or NEO4J_USER env var)")
    password: str = Field(default="", description="Neo4j password (or NEO4J_PASSWORD env var)")
    database: str = Field(default="neo4j", description="Neo4j database name")

    def model_post_init(self, __context):
        """Resolve from env vars if not provided."""
        if not self.uri:
            self.uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        if not self.user:
            self.user = os.getenv("NEO4J_USER", "neo4j")
        if not self.password:
            self.password = os.getenv("NEO4J_PASSWORD", "haivepass")


class Neo4jKGStore:
    """Neo4j-backed knowledge graph store for MemoryAgent.

    Stores KG triples in Neo4j for graph traversal while keeping them
    in the LangGraph store for vector search. Provides Cypher-based
    queries for relationship exploration, path finding, and neighborhood
    analysis.

    Usage:
        kg = Neo4jKGStore(Neo4jKGConfig())
        kg.save_triple("Will", "works_at", "Anthropic", user_id="will")
        kg.save_triple("Will", "uses", "Python", user_id="will")
        triples = kg.query_entity("Will")
        neighbors = kg.query_neighborhood("Will")
        path = kg.query_path("Will", "Python")
        kg.close()
    """

    def __init__(self, config: Neo4jKGConfig | None = None):
        self.config = config or Neo4jKGConfig()
        self._driver = None

    def _ensure_driver(self):
        """Lazily initialize Neo4j driver and schema."""
        if self._driver is None:
            try:
                from neo4j import GraphDatabase
                self._driver = GraphDatabase.driver(
                    self.config.uri,
                    auth=(self.config.user, self.config.password),
                )
                # Verify connection
                self._driver.verify_connectivity()
                # Initialize schema
                init_schema(self._driver, self.config.database)
                logger.info(f"Neo4j KG connected: {self.config.uri}")
            except ImportError:
                raise ImportError("Neo4j driver required: pip install neo4j")
            except Exception as e:
                logger.error(f"Neo4j connection failed: {e}")
                raise

    # ---- Triple operations ----

    def save_triple(self, subject: str, predicate: str, obj: str,
                    user_id: str = "default",
                    subject_type: str = "Entity",
                    object_type: str = "Entity",
                    source: str = "memory_agent") -> bool:
        """Save a KG triple to Neo4j using MERGE (upsert).

        Args:
            subject: Source entity name
            predicate: Relationship type
            obj: Target entity name
            user_id: User scope
            subject_type: Label for source node
            object_type: Label for target node
            source: Where this triple came from
        """
        self._ensure_driver()
        try:
            with self._driver.session(database=self.config.database) as session:
                session.run(
                    UPSERT_TRIPLE,
                    subject=subject, predicate=predicate, object=obj,
                    user_id=user_id, subject_type=subject_type,
                    object_type=object_type, source=source,
                )
                logger.debug(f"Neo4j: {subject} -{predicate}-> {obj}")
                return True
        except Exception as e:
            logger.warning(f"Neo4j save_triple failed: {e}")
            return False

    def save_triples_batch(self, triples: list[dict], user_id: str = "default") -> int:
        """Save multiple triples efficiently.

        Args:
            triples: List of {subject, predicate, object} dicts
            user_id: User scope

        Returns:
            Number of triples saved
        """
        self._ensure_driver()
        saved = 0
        try:
            with self._driver.session(database=self.config.database) as session:
                for t in triples:
                    subj = t.get("subject", "")
                    pred = t.get("predicate", "")
                    obj = t.get("object", "")
                    if subj and pred and obj:
                        session.run(
                            UPSERT_TRIPLE,
                            subject=subj, predicate=pred, object=obj,
                            user_id=user_id,
                            subject_type=t.get("subject_type", "Entity"),
                            object_type=t.get("object_type", "Entity"),
                            source=t.get("source", "memory_agent"),
                        )
                        saved += 1
            logger.info(f"Neo4j: saved {saved} triples batch")
        except Exception as e:
            logger.warning(f"Neo4j batch save failed: {e}")
        return saved

    # ---- KG creation from memories ----

    def create_kg_from_memories(self, store: Any, user_id: str = "default") -> int:
        """Build KG in Neo4j from existing KG triples in the LangGraph store.

        Reads all KG triples from store namespace ("kg", user_id) and
        creates them in Neo4j for graph traversal.

        Args:
            store: LangGraph BaseStore with existing triples
            user_id: User to extract triples for

        Returns:
            Number of triples synced to Neo4j
        """
        try:
            kg_ns = ("kg", user_id)
            results = store.search(kg_ns, limit=500)
            triples = []
            for item in results:
                val = item.value if hasattr(item, "value") else item
                if isinstance(val, dict) and val.get("type") == "kg_triple":
                    triples.append(val)

            if triples:
                return self.save_triples_batch(triples, user_id=user_id)
            return 0
        except Exception as e:
            logger.warning(f"Failed to create KG from memories: {e}")
            return 0

    # ---- Query operations ----

    def query_entity(self, entity: str) -> list[dict]:
        """Get all triples involving an entity.

        Args:
            entity: Entity name to query

        Returns:
            List of {subject, predicate, object} dicts
        """
        self._ensure_driver()
        results = []
        try:
            with self._driver.session(database=self.config.database) as session:
                records = session.run(QUERY_ENTITY_TRIPLES, entity=entity)
                for r in records:
                    results.append({
                        "subject": r["subject"],
                        "predicate": r["predicate"],
                        "object": r["object"],
                    })
        except Exception as e:
            logger.warning(f"Neo4j query_entity failed: {e}")
        return results

    def query_user_triples(self, user_id: str, limit: int = 50) -> list[dict]:
        """Get all triples for a user.

        Args:
            user_id: User to query
            limit: Max results

        Returns:
            List of {subject, predicate, object} dicts
        """
        self._ensure_driver()
        results = []
        try:
            with self._driver.session(database=self.config.database) as session:
                records = session.run(QUERY_USER_TRIPLES, user_id=user_id, limit=limit)
                for r in records:
                    results.append({
                        "subject": r["subject"],
                        "predicate": r["predicate"],
                        "object": r["object"],
                    })
        except Exception as e:
            logger.warning(f"Neo4j query_user_triples failed: {e}")
        return results

    def query_neighborhood(self, entity: str, limit: int = 20) -> list[dict]:
        """Query 1-2 hop neighborhood of an entity.

        Args:
            entity: Center entity name
            limit: Max results

        Returns:
            List of neighborhood records
        """
        self._ensure_driver()
        results = []
        try:
            with self._driver.session(database=self.config.database) as session:
                records = session.run(QUERY_NEIGHBORHOOD, entity=entity, limit=limit)
                for r in records:
                    results.append({
                        "center": r["center"],
                        "rel1": r["rel1"],
                        "neighbor": r["neighbor"],
                        "rel2": r["rel2"],
                        "hop2_entity": r["hop2_entity"],
                    })
        except Exception as e:
            logger.warning(f"Neo4j neighborhood query failed: {e}")
        return results

    def query_path(self, start: str, end: str) -> list[dict]:
        """Find shortest path between two entities.

        Args:
            start: Start entity name
            end: End entity name

        Returns:
            List of path records with entities, predicates, hops
        """
        self._ensure_driver()
        results = []
        try:
            with self._driver.session(database=self.config.database) as session:
                records = session.run(QUERY_PATH, start=start, end=end)
                for r in records:
                    results.append({
                        "entities": r["entities"],
                        "predicates": r["predicates"],
                        "hops": r["hops"],
                    })
        except Exception as e:
            logger.warning(f"Neo4j path query failed: {e}")
        return results

    def query_cypher(self, cypher: str, params: dict | None = None) -> list[dict]:
        """Execute a raw Cypher query.

        Args:
            cypher: Cypher query string
            params: Query parameters

        Returns:
            List of result records as dicts
        """
        self._ensure_driver()
        results = []
        try:
            with self._driver.session(database=self.config.database) as session:
                records = session.run(cypher, **(params or {}))
                for r in records:
                    results.append(dict(r))
        except Exception as e:
            logger.warning(f"Neo4j query failed: {e}")
        return results

    def get_stats(self) -> dict:
        """Get graph statistics."""
        self._ensure_driver()
        try:
            with self._driver.session(database=self.config.database) as session:
                result = session.run(QUERY_GRAPH_STATS)
                record = result.single()
                if record:
                    return {
                        "entities": record["entities"],
                        "relationships": record["relationships"],
                        "memories": record["memories"],
                    }
        except Exception as e:
            logger.warning(f"Neo4j stats failed: {e}")
        return {"entities": 0, "relationships": 0, "memories": 0}

    def close(self):
        """Close the Neo4j driver."""
        if self._driver:
            self._driver.close()
            self._driver = None

    def __del__(self):
        self.close()
