"""Knowledge Graph store integration for MemoryAgent.

Provides Neo4j-backed KG storage that works alongside the LangGraph store
for structured knowledge persistence. Triples stored in both:
- LangGraph store (for search/retrieval via memory tools)
- Neo4j (for graph traversal, relationship queries, APOC algorithms)

Uses langchain_neo4j for graph operations.
"""

import logging
from typing import Any

from pydantic import BaseModel, Field

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
        import os
        if not self.uri:
            self.uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        if not self.user:
            self.user = os.getenv("NEO4J_USER", "neo4j")
        if not self.password:
            self.password = os.getenv("NEO4J_PASSWORD", "haivepass")


class Neo4jKGStore:
    """Neo4j-backed knowledge graph store.

    Stores KG triples in Neo4j for graph traversal while keeping them
    in the LangGraph store for vector search. This dual-storage approach
    enables both semantic search and structural graph queries.

    Usage:
        kg_store = Neo4jKGStore(Neo4jKGConfig())
        kg_store.save_triple("Will", "builds", "Haive")
        results = kg_store.query_neighbors("Will")
        kg_store.close()
    """

    def __init__(self, config: Neo4jKGConfig):
        self.config = config
        self._driver = None
        self._graph = None

    def _ensure_driver(self):
        """Lazily initialize Neo4j driver."""
        if self._driver is None:
            try:
                from neo4j import GraphDatabase
                self._driver = GraphDatabase.driver(
                    self.config.uri,
                    auth=(self.config.user, self.config.password),
                )
                # Create indexes for fast lookup
                with self._driver.session(database=self.config.database) as session:
                    session.run("CREATE INDEX IF NOT EXISTS FOR (e:Entity) ON (e.name)")
                    session.run("CREATE INDEX IF NOT EXISTS FOR (e:Entity) ON (e.type)")
                logger.info(f"Neo4j connected: {self.config.uri}")
            except ImportError:
                raise ImportError("Neo4j driver required: pip install neo4j")
            except Exception as e:
                logger.error(f"Neo4j connection failed: {e}")
                raise

    def save_triple(self, subject: str, predicate: str, obj: str,
                    subject_type: str = "Entity", object_type: str = "Entity",
                    properties: dict | None = None) -> None:
        """Save a KG triple to Neo4j.

        Creates or merges nodes and relationship.

        Args:
            subject: Source entity name
            predicate: Relationship type (will be uppercased)
            obj: Target entity name
            subject_type: Label for source node
            object_type: Label for target node
            properties: Optional properties for the relationship
        """
        self._ensure_driver()
        rel_type = predicate.upper().replace(" ", "_")
        props = properties or {}

        query = f"""
        MERGE (s:{subject_type} {{name: $subject}})
        MERGE (o:{object_type} {{name: $object}})
        MERGE (s)-[r:`{rel_type}`]->(o)
        SET r += $props
        RETURN s.name, type(r), o.name
        """

        try:
            with self._driver.session(database=self.config.database) as session:
                session.run(query, subject=subject, object=obj, props=props)
                logger.debug(f"Neo4j: {subject} -{rel_type}-> {obj}")
        except Exception as e:
            logger.warning(f"Neo4j save_triple failed: {e}")

    def save_triples_batch(self, triples: list[dict]) -> int:
        """Save multiple triples efficiently."""
        self._ensure_driver()
        saved = 0
        try:
            with self._driver.session(database=self.config.database) as session:
                for t in triples:
                    subj = t.get("subject", "")
                    pred = t.get("predicate", "")
                    obj = t.get("object", "")
                    if subj and pred and obj:
                        rel_type = pred.upper().replace(" ", "_")
                        session.run(
                            f"MERGE (s:Entity {{name: $s}}) "
                            f"MERGE (o:Entity {{name: $o}}) "
                            f"MERGE (s)-[:`{rel_type}`]->(o)",
                            s=subj, o=obj,
                        )
                        saved += 1
        except Exception as e:
            logger.warning(f"Neo4j batch save failed: {e}")
        return saved

    def query_neighbors(self, entity: str, depth: int = 1, limit: int = 20) -> list[dict]:
        """Query all relationships for an entity.

        Args:
            entity: Entity name to query
            depth: How many hops to traverse (1-3)
            limit: Maximum results

        Returns:
            List of {subject, predicate, object} dicts
        """
        self._ensure_driver()
        query = f"""
        MATCH (s:Entity {{name: $entity}})-[r]-(o)
        RETURN s.name as subject, type(r) as predicate, o.name as object
        LIMIT $limit
        """
        results = []
        try:
            with self._driver.session(database=self.config.database) as session:
                records = session.run(query, entity=entity, limit=limit)
                for record in records:
                    results.append({
                        "subject": record["subject"],
                        "predicate": record["predicate"],
                        "object": record["object"],
                    })
        except Exception as e:
            logger.warning(f"Neo4j query failed: {e}")
        return results

    def query_path(self, start: str, end: str, max_depth: int = 4) -> list[list[dict]]:
        """Find paths between two entities.

        Args:
            start: Start entity name
            end: End entity name
            max_depth: Maximum path length

        Returns:
            List of paths, each path is a list of {subject, predicate, object}
        """
        self._ensure_driver()
        query = """
        MATCH path = shortestPath(
            (s:Entity {name: $start})-[*..%d]-(e:Entity {name: $end})
        )
        RETURN [r IN relationships(path) |
            {subject: startNode(r).name, predicate: type(r), object: endNode(r).name}
        ] as triples
        LIMIT 5
        """ % max_depth

        paths = []
        try:
            with self._driver.session(database=self.config.database) as session:
                records = session.run(query, start=start, end=end)
                for record in records:
                    paths.append(record["triples"])
        except Exception as e:
            logger.warning(f"Neo4j path query failed: {e}")
        return paths

    def get_graph_summary(self, limit: int = 50) -> dict:
        """Get a summary of the knowledge graph."""
        self._ensure_driver()
        summary = {"entity_count": 0, "relationship_count": 0, "relationship_types": [], "sample_triples": []}
        try:
            with self._driver.session(database=self.config.database) as session:
                # Count entities
                result = session.run("MATCH (n:Entity) RETURN count(n) as c")
                summary["entity_count"] = result.single()["c"]

                # Count relationships
                result = session.run("MATCH ()-[r]->() RETURN count(r) as c")
                summary["relationship_count"] = result.single()["c"]

                # Relationship types
                result = session.run("CALL db.relationshipTypes()")
                summary["relationship_types"] = [r["relationshipType"] for r in result]

                # Sample triples
                result = session.run(
                    "MATCH (s)-[r]->(o) RETURN s.name, type(r), o.name LIMIT $limit",
                    limit=limit,
                )
                for r in result:
                    summary["sample_triples"].append({
                        "subject": r["s.name"],
                        "predicate": r["type(r)"],
                        "object": r["o.name"],
                    })
        except Exception as e:
            logger.warning(f"Neo4j summary failed: {e}")
        return summary

    def close(self):
        """Close the Neo4j driver."""
        if self._driver:
            self._driver.close()
            self._driver = None

    def __del__(self):
        self.close()
