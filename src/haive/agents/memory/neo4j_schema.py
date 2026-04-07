"""Neo4j schema initialization and Cypher templates for the Memory KG.

Schema:
  (:Entity {name, type, user_id, created_at})
  (:Memory {content, importance, user_id, created_at})
  (:Summary {content, token_count, user_id, created_at})

Relationships:
  (Entity)-[:RELATES_TO {predicate}]->(Entity)
  (Entity)-[:MENTIONED_IN]->(Memory)
  (Memory)-[:SUMMARIZED_BY]->(Summary)

Compatible with the existing graph_db RAG agent's Neo4j patterns.
Uses same env vars: NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE.
"""

# ---- Schema creation ----

SCHEMA_INIT_CYPHER = [
    # Constraints (uniqueness)
    "CREATE CONSTRAINT entity_name IF NOT EXISTS FOR (e:Entity) REQUIRE e.name IS UNIQUE",
    "CREATE CONSTRAINT memory_id IF NOT EXISTS FOR (m:Memory) REQUIRE m.id IS UNIQUE",
    "CREATE CONSTRAINT summary_id IF NOT EXISTS FOR (s:Summary) REQUIRE s.id IS UNIQUE",

    # Indexes for fast lookup
    "CREATE INDEX entity_type IF NOT EXISTS FOR (e:Entity) ON (e.type)",
    "CREATE INDEX entity_user IF NOT EXISTS FOR (e:Entity) ON (e.user_id)",
    "CREATE INDEX memory_user IF NOT EXISTS FOR (m:Memory) ON (m.user_id)",
    "CREATE INDEX memory_importance IF NOT EXISTS FOR (m:Memory) ON (m.importance)",
    "CREATE INDEX summary_user IF NOT EXISTS FOR (s:Summary) ON (s.user_id)",

    # Full-text search index (APOC)
    # "CALL db.index.fulltext.createNodeIndex('entitySearch', ['Entity'], ['name', 'type'])",
    # "CALL db.index.fulltext.createNodeIndex('memorySearch', ['Memory'], ['content'])",
]

# ---- Triple CRUD ----

UPSERT_TRIPLE = """
MERGE (s:Entity {name: $subject})
  ON CREATE SET s.user_id = $user_id, s.created_at = datetime(), s.type = $subject_type
MERGE (o:Entity {name: $object})
  ON CREATE SET o.user_id = $user_id, o.created_at = datetime(), o.type = $object_type
MERGE (s)-[r:RELATES_TO {predicate: $predicate}]->(o)
  ON CREATE SET r.created_at = datetime(), r.source = $source
  ON MATCH SET r.updated_at = datetime()
RETURN s.name AS subject, r.predicate AS predicate, o.name AS object
"""

DELETE_TRIPLE = """
MATCH (s:Entity {name: $subject})-[r:RELATES_TO {predicate: $predicate}]->(o:Entity {name: $object})
DELETE r
RETURN count(r) AS deleted
"""

# ---- Memory CRUD ----

SAVE_MEMORY = """
CREATE (m:Memory {
  id: $id,
  content: $content,
  importance: $importance,
  user_id: $user_id,
  created_at: datetime()
})
RETURN m.id AS id
"""

LINK_ENTITY_TO_MEMORY = """
MATCH (e:Entity {name: $entity_name})
MATCH (m:Memory {id: $memory_id})
MERGE (e)-[:MENTIONED_IN]->(m)
"""

# ---- Query templates ----

# Find all triples for an entity
QUERY_ENTITY_TRIPLES = """
MATCH (s:Entity {name: $entity})-[r:RELATES_TO]->(o:Entity)
RETURN s.name AS subject, r.predicate AS predicate, o.name AS object
UNION
MATCH (s:Entity)-[r:RELATES_TO]->(o:Entity {name: $entity})
RETURN s.name AS subject, r.predicate AS predicate, o.name AS object
"""

# Find all entities for a user
QUERY_USER_ENTITIES = """
MATCH (e:Entity {user_id: $user_id})
RETURN e.name AS name, e.type AS type
ORDER BY e.created_at DESC
LIMIT $limit
"""

# Find all triples for a user
QUERY_USER_TRIPLES = """
MATCH (s:Entity {user_id: $user_id})-[r:RELATES_TO]->(o:Entity)
RETURN s.name AS subject, r.predicate AS predicate, o.name AS object
ORDER BY r.created_at DESC
LIMIT $limit
"""

# Shortest path between two entities
QUERY_PATH = """
MATCH path = shortestPath(
  (s:Entity {name: $start})-[*..4]-(e:Entity {name: $end})
)
RETURN [n IN nodes(path) | n.name] AS entities,
       [r IN relationships(path) | r.predicate] AS predicates,
       length(path) AS hops
"""

# Neighborhood query (1-2 hops)
QUERY_NEIGHBORHOOD = """
MATCH (center:Entity {name: $entity})-[r1:RELATES_TO]-(neighbor:Entity)
OPTIONAL MATCH (neighbor)-[r2:RELATES_TO]-(hop2:Entity)
WHERE hop2 <> center
RETURN center.name AS center,
       r1.predicate AS rel1,
       neighbor.name AS neighbor,
       r2.predicate AS rel2,
       hop2.name AS hop2_entity
LIMIT $limit
"""

# Graph summary statistics
QUERY_GRAPH_STATS = """
MATCH (e:Entity)
WITH count(e) AS entities
MATCH ()-[r:RELATES_TO]->()
WITH entities, count(r) AS relationships
MATCH (m:Memory)
WITH entities, relationships, count(m) AS memories
RETURN entities, relationships, memories
"""

# Search entities by type
QUERY_ENTITIES_BY_TYPE = """
MATCH (e:Entity {type: $type, user_id: $user_id})
RETURN e.name AS name, e.type AS type
LIMIT $limit
"""

# Find related memories for an entity
QUERY_ENTITY_MEMORIES = """
MATCH (e:Entity {name: $entity})-[:MENTIONED_IN]->(m:Memory)
RETURN m.content AS content, m.importance AS importance, m.created_at AS created
ORDER BY m.created_at DESC
LIMIT $limit
"""


def init_schema(driver, database: str = "neo4j") -> None:
    """Initialize the Neo4j schema with constraints and indexes.

    Args:
        driver: Neo4j driver instance
        database: Database name
    """
    with driver.session(database=database) as session:
        for cypher in SCHEMA_INIT_CYPHER:
            try:
                session.run(cypher)
            except Exception as e:
                # Some constraints may already exist
                if "already exists" not in str(e).lower():
                    raise
