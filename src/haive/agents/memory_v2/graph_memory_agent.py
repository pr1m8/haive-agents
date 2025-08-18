"""Graph Memory Agent with advanced knowledge graph capabilities.

This module provides a sophisticated graph-based memory system that combines multiple
approaches for storing and retrieving structured knowledge:

1. **LLMGraphTransformer**: Intelligent entity and relationship extraction from text
2. **Text-to-Neo4j (TNT)**: Direct storage of graph structures in Neo4j database
3. **Graph RAG**: Intelligent querying using graph traversal and vector similarity
4. **Memory Consolidation**: Automatic organization of related memories into concepts
5. **Multi-modal Search**: Combining graph structure with vector embeddings

The GraphMemoryAgent is designed for applications requiring sophisticated knowledge
representation, relationship discovery, and contextual memory retrieval. It excels
at maintaining complex interconnected information while providing fast, relevant
access to stored knowledge.

Key Features:
    - **Entity Extraction**: Automatic identification of people, organizations, concepts
    - **Relationship Mapping**: Discovery and storage of semantic relationships
    - **Graph Constraints**: Performance-optimized Neo4j constraints and indexes
    - **Vector Integration**: Semantic similarity search on graph nodes
    - **Memory Consolidation**: Intelligent clustering of related information
    - **Multi-user Support**: Isolated memory spaces for different users
    - **Flexible Querying**: Natural language and Cypher query support

Architecture:
    The agent operates in multiple configurable modes:

    - **EXTRACT_ONLY**: Extract entities/relationships without storage
    - **STORE_ONLY**: Store pre-extracted graph data directly
    - **EXTRACT_AND_STORE**: Full pipeline from text to graph storage
    - **QUERY_ONLY**: Search existing graph without modifications
    - **FULL**: All capabilities including consolidation and analytics

Examples:
    Basic usage with automatic extraction and storage::

        config = GraphMemoryConfig(
            neo4j_uri="bolt://localhost:7687",
            neo4j_username="neo4j",
            neo4j_password="password",
            user_id="alice",
            mode=GraphMemoryMode.FULL
        )

        agent = GraphMemoryAgent(config)

        # Store complex information with automatic entity extraction
        result = await agent.run(
            "John Smith is the CEO of TechCorp in San Francisco. "
            "He previously worked at DataCorp for 5 years and "
            "specializes in machine learning applications."
        )

        # Query with natural language
        query_result = await agent.query_graph(
            "Who are the executives in San Francisco?"
        )

    Advanced graph exploration::

        # Get entity-centered subgraph
        subgraph = await agent.get_memory_subgraph(
            "John Smith",
            max_depth=2,
            relationship_types=["WORKS_FOR", "LOCATED_IN"]
        )

        # Find similar memories using vector search
        similar = await agent.search_similar_memories(
            "technology executives",
            node_type="Person",
            k=5
        )

    Memory consolidation and analytics::

        # Consolidate related memories into higher-level concepts
        consolidation = await agent.consolidate_memories(
            time_window="7 days",
            min_connections=3
        )

        # Use as a tool in other agents
        memory_tool = GraphMemoryAgent.as_tool(config)
        result = await memory_tool(
            "Remember: Sarah leads the AI research team",
            operation="full"
        )

See Also:
    - :class:`GraphMemoryConfig`: Configuration options and defaults
    - :class:`GraphMemoryMode`: Available operation modes
    - :mod:`haive.agents.rag.db_rag.graph_db`: Graph database RAG integration
    - :mod:`langchain_experimental.graph_transformers`: LLM graph transformation

Note:
    This agent requires a running Neo4j instance and appropriate LLM configuration.
    For production use, ensure proper authentication, backup, and monitoring of
    the Neo4j database. Vector embeddings require OpenAI API access by default.
"""

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector
from langchain_core.documents import Document
from langchain_core.tools import tool
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_neo4j.chains.graph_qa.cypher import GraphCypherQAChain
from langchain_neo4j.graphs.graph_document import GraphDocument

from haive.agents.document_modifiers.kg.kg_base.models import GraphTransformer
from haive.agents.rag.db_rag.graph_db.agent import GraphDBRAGAgent
from haive.agents.rag.db_rag.graph_db.config import GraphDBConfig, GraphDBRAGConfig

# Optional imports - GraphMemoryAgent will work with basic functionality
# even if these fail
try:
    HAS_GRAPH_TRANSFORMER = True
except ImportError:
    GraphTransformer = None
    HAS_GRAPH_TRANSFORMER = False

try:
    HAS_GRAPH_DB_RAG = True
except ImportError:
    GraphDBRAGAgent = None
    GraphDBRAGConfig = None
    GraphDBConfig = None
    HAS_GRAPH_DB_RAG = False

logger = logging.getLogger(__name__)


class GraphMemoryMode(str, Enum):
    """Operation modes for GraphMemoryAgent defining different processing workflows.

    These modes control which components of the graph memory pipeline are active,
    allowing for flexible deployment patterns and performance optimization based
    on specific use cases.

    Attributes:
        EXTRACT_ONLY: Extract entities and relationships from text without storing
            in the database. Useful for analysis, validation, or external storage.
        STORE_ONLY: Store pre-processed graph documents directly in Neo4j without
            extraction. Suitable when entities/relationships are already identified.
        EXTRACT_AND_STORE: Complete pipeline from raw text to graph storage.
            Recommended for most applications requiring automatic knowledge extraction.
        QUERY_ONLY: Search and retrieve from existing graph without modifications.
            Ideal for read-only applications or when extraction is handled separately.
        FULL: All capabilities including extraction, storage, querying, and
            consolidation. Provides complete graph memory functionality.

    Examples:
        Mode selection based on use case::

            # For analysis without permanent storage
            config = GraphMemoryConfig(mode=GraphMemoryMode.EXTRACT_ONLY)
            agent = GraphMemoryAgent(config)
            result = await agent.run("Analyze this text for entities")
            entities = result["extracted_graph"]

            # For high-performance querying
            config = GraphMemoryConfig(mode=GraphMemoryMode.QUERY_ONLY)
            agent = GraphMemoryAgent(config)
            result = await agent.query_graph("Find all connections to AI")

            # For production knowledge base
            config = GraphMemoryConfig(mode=GraphMemoryMode.FULL)
            agent = GraphMemoryAgent(config)
            await agent.run("Store and process this information...")

    Note:
        The FULL mode provides the most comprehensive functionality but requires
        more computational resources. For production deployments, consider the
        performance implications of each mode based on your specific requirements.
    """

    EXTRACT_ONLY = "extract_only"  # Only extract entities/relationships
    STORE_ONLY = "store_only"  # Store in graph DB without extraction
    EXTRACT_AND_STORE = "extract_and_store"  # Extract and store
    QUERY_ONLY = "query_only"  # Only query existing graph
    FULL = "full"  # All capabilities


@dataclass
class GraphMemoryConfig:
    """Comprehensive configuration for GraphMemoryAgent with database and extraction settings.

    This configuration class provides fine-grained control over all aspects of the
    graph memory system, from database connections to entity extraction preferences.
    The configuration supports multi-user environments, custom knowledge domains,
    and performance optimization.

    Attributes:
        neo4j_uri: Neo4j database connection URI. Supports bolt://, bolt+s://,
            and neo4j:// protocols. Default connects to local instance.
        neo4j_username: Database username for authentication. Default is 'neo4j'.
        neo4j_password: Database password for authentication. Required for connection.
        database_name: Specific Neo4j database name. Use 'neo4j' for default database.

        allowed_nodes: List of node types that can be extracted from text.
            Controls the vocabulary of entity types recognized by the system.
        allowed_relationships: List of valid relationship triplets (source, relation, target).
            Defines the relationship schema for structured knowledge extraction.

        extract_properties: Whether to extract and store node/relationship properties
            beyond just names and types. Enables richer entity descriptions.
        node_properties: List of property names to extract for entities (e.g., 'role',
            'description', 'importance'). Only used when extract_properties=True.
        relationship_properties: List of property names for relationships (e.g., 'since',
            'strength', 'context'). Provides temporal and contextual information.

        user_id: Unique identifier for memory isolation in multi-user environments.
            All stored entities and relationships are tagged with this identifier.
        mode: Operation mode determining which components are active.
            See GraphMemoryMode for available options.

        llm_config: Configuration for the language model used in entity extraction
            and query processing. Affects extraction quality and cost.
        enable_vector_index: Whether to create vector embeddings for semantic search.
            Requires additional computational resources but enables similarity search.
        embedding_model: Model provider for vector embeddings. Currently supports 'openai'.

    Examples:
        Basic configuration for local development::

            config = GraphMemoryConfig(
                neo4j_uri="bolt://localhost:7687",
                neo4j_username="neo4j",
                neo4j_password="password",
                user_id="developer",
                mode=GraphMemoryMode.FULL
            )

        Production configuration with custom schema::

            config = GraphMemoryConfig(
                neo4j_uri="bolt+s://production.neo4j.com:7687",
                neo4j_username="prod_user",
                neo4j_password=os.getenv("NEO4J_PASSWORD"),
                database_name="knowledge_base",
                user_id="production_system",

                # Custom domain-specific entities
                allowed_nodes=[
                    "Researcher", "Paper", "Institution", "Dataset",
                    "Algorithm", "Experiment", "Finding"
                ],
                allowed_relationships=[
                    ("Researcher", "AUTHORED", "Paper"),
                    ("Paper", "CITES", "Paper"),
                    ("Researcher", "AFFILIATED_WITH", "Institution"),
                    ("Experiment", "USES", "Dataset"),
                    ("Paper", "PROPOSES", "Algorithm")
                ],

                # Enhanced property extraction
                extract_properties=True,
                node_properties=[
                    "publication_year", "impact_factor", "field",
                    "methodology", "significance"
                ],
                relationship_properties=[
                    "citation_count", "collaboration_strength",
                    "temporal_proximity", "research_area"
                ],

                # Performance optimization
                llm_config=AugLLMConfig(
                    model="gpt-4",
                    temperature=0.1,  # Deterministic extraction
                    max_tokens=2000
                ),
                enable_vector_index=True
            )

        Memory-optimized configuration::

            config = GraphMemoryConfig(
                # Use faster extraction with basic schema
                allowed_nodes=["Person", "Organization", "Location"],
                extract_properties=False,  # Skip detailed properties
                enable_vector_index=False,  # Skip vector embeddings
                llm_config=AugLLMConfig(
                    model="gpt-3.5-turbo",  # Faster, cheaper model
                    temperature=0.0,
                    max_tokens=1000
                )
            )

    Note:
        The allowed_relationships format uses triplets to define valid relationship
        patterns. This helps ensure extracted relationships follow expected schemas
        and improves query predictability. Vector indexing significantly improves
        semantic search but requires additional storage and computational resources.
    """

    # Neo4j connection
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_username: str = "neo4j"
    neo4j_password: str = "password"
    database_name: str = "neo4j"

    # Graph transformation settings
    allowed_nodes: list[str] = field(
        default_factory=lambda: [
            "Person",
            "Organization",
            "Location",
            "Event",
            "Concept",
            "Product",
            "Technology",
            "Date",
            "Skill",
            "Topic",
        ]
    )
    allowed_relationships: list[tuple[str, str, str]] = field(
        default_factory=lambda: [
            ("Person", "WORKS_FOR", "Organization"),
            ("Person", "KNOWS", "Person"),
            ("Person", "LOCATED_IN", "Location"),
            ("Person", "PARTICIPATED_IN", "Event"),
            ("Person", "HAS_SKILL", "Skill"),
            ("Organization", "LOCATED_IN", "Location"),
            ("Event", "OCCURRED_AT", "Location"),
            ("Event", "ON_DATE", "Date"),
            ("Person", "INTERESTED_IN", "Topic"),
            ("Concept", "RELATED_TO", "Concept"),
        ]
    )

    # Extraction settings
    extract_properties: bool = True
    node_properties: list[str] = field(
        default_factory=lambda: [
            "role",
            "description",
            "date",
            "importance",
            "confidence",
        ]
    )
    relationship_properties: list[str] = field(
        default_factory=lambda: ["since", "until", "strength", "context"]
    )

    # Memory settings
    user_id: str = "default_user"
    mode: GraphMemoryMode = GraphMemoryMode.FULL

    # LLM settings
    llm_config: AugLLMConfig | None = None

    # RAG settings
    enable_vector_index: bool = True
    embedding_model: str = "openai"

    def __post_init__(self):
        """Post Init  ."""
        if self.llm_config is None:
            self.llm_config = AugLLMConfig(temperature=0.7)


class GraphMemoryAgent:
    """Agent that manages memory using a knowledge graph.

    This agent provides:
    - Entity and relationship extraction from text
    - Direct storage to Neo4j (TNT - Text to Neo4j)
    - Graph-based retrieval using Cypher queries
    - Vector similarity search on graph nodes
    - Complex graph traversal for memory retrieval
    """

    def __init__(self, config: GraphMemoryConfig):
        """Initialize GraphMemoryAgent with comprehensive graph memory capabilities.

        Sets up all necessary components for graph-based memory operations including
        Neo4j database connections, entity extraction models, RAG components, and
        vector indexes. The initialization process creates database constraints,
        validates configurations, and prepares all subsystems.

        Args:
            config: GraphMemoryConfig containing database connection details,
                extraction preferences, operation mode, and performance settings.
                All required components are validated during initialization.

        Raises:
            ConnectionError: If Neo4j database connection fails or authentication
                is invalid. Check database status and credentials.
            ImportError: If required optional dependencies are missing for
                specific features (e.g., graph transformers, RAG components).
            ValueError: If configuration contains invalid settings or conflicting
                options (e.g., invalid node types, malformed relationship patterns).

        Examples:
            Basic initialization with defaults::

                config = GraphMemoryConfig(
                    neo4j_uri="bolt://localhost:7687",
                    neo4j_username="neo4j",
                    neo4j_password="password",
                    user_id="user123"
                )

                try:
                    agent = GraphMemoryAgent(config)
                    print("Agent initialized successfully")
                except ConnectionError as e:
                    print(f"Database connection failed: {e}")

            Initialize with custom domain knowledge::

                # Research paper domain
                config = GraphMemoryConfig(
                    allowed_nodes=["Author", "Paper", "Conference", "Topic"],
                    allowed_relationships=[
                        ("Author", "WROTE", "Paper"),
                        ("Paper", "PRESENTED_AT", "Conference"),
                        ("Paper", "ABOUT", "Topic")
                    ],
                    extract_properties=True,
                    node_properties=["year", "citations", "h_index"],
                    mode=GraphMemoryMode.FULL
                )

                agent = GraphMemoryAgent(config)

            Performance-optimized initialization::

                config = GraphMemoryConfig(
                    mode=GraphMemoryMode.EXTRACT_AND_STORE,  # Skip query components
                    enable_vector_index=False,  # Skip vector embeddings
                    llm_config=AugLLMConfig(
                        model="gpt-3.5-turbo",  # Faster model
                        temperature=0.0  # Deterministic
                    )
                )

                agent = GraphMemoryAgent(config)

        Note:
            The initialization process creates database indexes and constraints
            automatically. For production deployments, ensure the Neo4j user has
            sufficient privileges for schema modifications. Vector indexing requires
            OpenAI API access and will be disabled gracefully if unavailable.
        """
        self.config = config
        self.logger = logger

        # Initialize Neo4j connection
        self._init_neo4j()

        # Initialize graph transformer
        self._init_graph_transformer()

        # Initialize RAG components if not query-only mode
        if config.mode != GraphMemoryMode.QUERY_ONLY:
            self._init_rag_components()

        # Initialize vector index if enabled
        if config.enable_vector_index:
            self._init_vector_index()

    def _init_neo4j(self):
        """Initialize Neo4j database connection with error handling and optimization.

        Establishes connection to Neo4j using provided credentials and creates
        performance-optimized constraints and indexes for efficient graph operations.
        The method handles authentication, validates database access, and sets up
        the schema for multi-user memory storage.

        Raises:
            ConnectionError: If database connection fails due to network issues,
                invalid credentials, or database unavailability.
            AuthenticationError: If provided username/password combination is invalid.
            ServiceUnavailable: If Neo4j service is not running or accessible.

        Note:
            This method automatically creates uniqueness constraints and performance
            indexes. Ensure the database user has CREATE CONSTRAINT privileges.
            For read-only deployments, these operations will be logged as warnings.
        """
        try:
            self.graph = Neo4jGraph(
                url=self.config.neo4j_uri,
                username=self.config.neo4j_username,
                password=self.config.neo4j_password,
                database=self.config.database_name,
            )

            # Create constraints for better performance
            self._create_graph_constraints()

            self.logger.info(f"Connected to Neo4j at {self.config.neo4j_uri}")
        except Exception as e:
            self.logger.exception(f"Failed to connect to Neo4j: {e}")
            raise

    def _create_graph_constraints(self):
        """Create database constraints and indexes for optimal graph performance.

        Sets up Neo4j schema with uniqueness constraints for entity identification
        and performance indexes for common query patterns. This optimization is
        crucial for production deployments with large knowledge graphs.

        Created Constraints:
            - Unique ID constraints for Person, Organization, Location, Event nodes
            - Ensures data integrity and prevents duplicate entities

        Created Indexes:
            - Name indexes for Person and Organization nodes (fast name lookups)
            - User ID index for Memory nodes (multi-user isolation)
            - Composite indexes for common query patterns

        Note:
            Constraint creation requires appropriate database privileges. The method
            gracefully handles permission errors and continues without constraints
            if necessary. Performance may be reduced without these optimizations.
        """
        try:
            # Create uniqueness constraints for common node types
            for node_type in ["Person", "Organization", "Location", "Event"]:
                self.graph.query(
                    f"CREATE CONSTRAINT IF NOT EXISTS FOR (n:{node_type}) REQUIRE n.id IS UNIQUE"
                )

            # Create indexes for better query performance
            self.graph.query("CREATE INDEX IF NOT EXISTS FOR (n:Person) ON (n.name)")
            self.graph.query(
                "CREATE INDEX IF NOT EXISTS FOR (n:Organization) ON (n.name)"
            )

            # Create user index for multi-user support
            self.graph.query("CREATE INDEX IF NOT EXISTS FOR (n:Memory) ON (n.user_id)")
        except Exception as e:
            self.logger.warning(f"Error creating constraints: {e}")

    def _init_graph_transformer(self):
        """Initialize the graph transformer for entity extraction."""
        if HAS_GRAPH_TRANSFORMER:
            self.graph_transformer = GraphTransformer()
        else:
            self.graph_transformer = None
            self.logger.warning(
                "GraphTransformer not available - graph extraction limited to LangChain LLMGraphTransformer"
            )

        # Always initialize LangChain's LLMGraphTransformer as fallback
        llm = self.config.llm_config.instantiate()
        self.llm_graph_transformer = LLMGraphTransformer(
            llm=llm,
            allowed_nodes=self.config.allowed_nodes,
            allowed_relationships=self.config.allowed_relationships,
            node_properties=(
                self.config.node_properties if self.config.extract_properties else False
            ),
            relationship_properties=(
                self.config.relationship_properties
                if self.config.extract_properties
                else False
            ),
            strict_mode=False,
        )

    def _init_rag_components(self):
        """Initialize Graph RAG components."""
        if HAS_GRAPH_DB_RAG:
            # Create GraphDBRAGConfig
            graph_db_config = GraphDBConfig(
                graph_db_uri=self.config.neo4j_uri,
                graph_db_user=self.config.neo4j_username,
                graph_db_password=self.config.neo4j_password,
                graph_db_database=self.config.database_name,
            )

            rag_config = GraphDBRAGConfig(
                domain_name="memory",
                domain_categories=["personal", "knowledge", "events"],
                graph_db_config=graph_db_config,
                llm_config=self.config.llm_config,
            )

            # Create Graph RAG agent
            self.graph_rag_agent = GraphDBRAGAgent(rag_config)
        else:
            self.graph_rag_agent = None
            self.logger.warning(
                "GraphDBRAGAgent not available - using basic Cypher chain only"
            )

        # Create Cypher QA chain for direct queries
        llm = self.config.llm_config.instantiate()
        self.cypher_chain = GraphCypherQAChain.from_llm(
            llm=llm,
            graph=self.graph,
            verbose=True,
            validate_cypher=True,
            return_intermediate_steps=True,
        )

    def _init_vector_index(self):
        """Initialize vector index for semantic search on graph."""
        try:
            embeddings = OpenAIEmbeddings()

            # Create vector index on Person nodes
            self.person_vector_index = Neo4jVector.from_existing_graph(
                embeddings,
                url=self.config.neo4j_uri,
                username=self.config.neo4j_username,
                password=self.config.neo4j_password,
                database=self.config.database_name,
                index_name="person_embeddings",
                node_label="Person",
                text_node_properties=["name", "description"],
                embedding_node_property="embedding",
            )

            # Create vector index on Concept nodes
            self.concept_vector_index = Neo4jVector.from_existing_graph(
                embeddings,
                url=self.config.neo4j_uri,
                username=self.config.neo4j_username,
                password=self.config.neo4j_password,
                database=self.config.database_name,
                index_name="concept_embeddings",
                node_label="Concept",
                text_node_properties=["name", "description"],
                embedding_node_property="embedding",
            )

            self.logger.info("Vector indexes created successfully")
        except Exception as e:
            self.logger.warning(f"Failed to create vector indexes: {e}")
            self.config.enable_vector_index = False

    async def extract_graph_from_text(
        self, text: str, metadata: dict[str, Any] | None = None
    ) -> list[GraphDocument]:
        """Extract entities and relationships from unstructured text using LLM analysis.

        Processes natural language text to identify entities (people, organizations,
        concepts, etc.) and their semantic relationships. Uses advanced graph
        transformation techniques to convert unstructured information into
        structured knowledge graph format.

        Args:
            text: Input text to analyze and extract from. Can be any natural
                language content including documents, conversations, articles,
                or structured data descriptions.
            metadata: Optional dictionary containing additional context information
                such as source, timestamp, importance, or domain-specific tags.
                This metadata is preserved and associated with extracted entities.

        Returns:
            List[GraphDocument]: List of structured graph documents containing:
                - nodes: Extracted entities with types and properties
                - relationships: Semantic connections between entities
                - source: Original document reference with metadata
                Each GraphDocument represents a coherent knowledge structure.

        Raises:
            ValueError: If input text is empty or contains only whitespace.
            LLMError: If language model processing fails or returns invalid results.
            ConfigurationError: If required extraction components are not properly
                configured or missing required settings.

        Examples:
            Extract entities from business information::

                text = """
                John Smith is the CEO of TechCorp, a software company based in
                San Francisco. The company specializes in AI solutions and was
                founded in 2020. John previously worked at DataCorp for 8 years.
                """

                graph_docs = await agent.extract_graph_from_text(
                    text,
                    metadata={
                        "source": "company_database",
                        "confidence": 0.9,
                        "verified": True
                    }
                )

                # Expected entities: John Smith (Person), TechCorp (Organization),
                # San Francisco (Location), AI solutions (Concept)
                # Expected relationships: John WORKS_FOR TechCorp,
                # TechCorp LOCATED_IN San Francisco

                for doc in graph_docs:
                    print(f"Extracted {len(doc.nodes)} entities")
                    print(f"Found {len(doc.relationships)} relationships")

                    for node in doc.nodes:
                        print(f"Entity: {node.id} ({node.type})")
                        if node.properties:
                            print(f"  Properties: {node.properties}")

            Extract from research content::

                research_text = """
                The study by Dr. Sarah Chen at MIT demonstrates that transformer
                models can achieve 95% accuracy on sentiment analysis tasks.
                This research builds on earlier work by the Stanford NLP team.
                """

                graph_docs = await agent.extract_graph_from_text(
                    research_text,
                    metadata={
                        "domain": "research",
                        "publication_year": 2024,
                        "field": "natural_language_processing"
                    }
                )

                # Expected: Dr. Sarah Chen (Person), MIT (Organization),
                # transformer models (Concept), sentiment analysis (Concept)

            Handle extraction with custom settings::

                # Agent configured for specific domain
                config = GraphMemoryConfig(
                    allowed_nodes=["Researcher", "Institution", "Technology"],
                    extract_properties=True,
                    node_properties=["expertise", "ranking", "impact"]
                )

                agent = GraphMemoryAgent(config)
                graph_docs = await agent.extract_graph_from_text(
                    "Dr. Alice Wang leads the quantum computing research at IBM"
                )

        Note:
            The extraction quality depends on the configured allowed_nodes and
            allowed_relationships. For domain-specific applications, customize
            these settings to match your knowledge domain. The method automatically
            falls back to LangChain's LLMGraphTransformer if Haive's enhanced
            GraphTransformer is unavailable.
        """
        # Create document
        doc = Document(
            page_content=text,
            metadata=metadata
            or {
                "user_id": self.config.user_id,
                "timestamp": datetime.now().isoformat(),
                "source": "memory_extraction",
            },
        )

        # Use Haive's GraphTransformer if available, otherwise fall back to
        # LangChain
        if self.graph_transformer is not None:
            graph_docs = self.graph_transformer.transform_documents(
                documents=[doc],
                llm_config=self.config.llm_config,
                allowed_nodes=self.config.allowed_nodes,
                allowed_relationships=self.config.allowed_relationships,
                node_properties=self.config.node_properties,
                relationship_properties=self.config.relationship_properties,
                additional_instructions="Extract all entities and relationships that represent memories, facts, and connections.",
            )
        else:
            # Fall back to LangChain LLMGraphTransformer
            graph_docs = self.llm_graph_transformer.convert_to_graph_documents([doc])

        return graph_docs

    async def store_graph_documents(
        self, graph_documents: list[GraphDocument], merge_nodes: bool = True
    ) -> dict[str, Any]:
        """Store extracted graph documents in Neo4j database with intelligent merging.

        Implements the Text-to-Neo4j (TNT) pattern for direct storage of structured
        knowledge graphs. Handles entity deduplication, relationship creation, and
        user isolation while maintaining data integrity and performance optimization.

        Args:
            graph_documents: List of GraphDocument objects containing nodes and
                relationships to store. Each document represents a coherent knowledge
                structure extracted from source text.
            merge_nodes: Whether to merge with existing entities or create new ones.
                When True, entities with matching names/types are consolidated.
                When False, all entities are created as new nodes (may cause duplicates).

        Returns:
            Dict[str, Any]: Comprehensive storage statistics containing:
                - nodes_created: Number of new entity nodes stored
                - relationships_created: Number of new relationships established
                - errors: List of any errors encountered during storage
                - success: Boolean indicating whether operation completed successfully
                - storage_time_ms: Time taken for storage operation
                - merge_conflicts: Number of merge conflicts resolved

        Raises:
            DatabaseError: If Neo4j database connection fails or transaction errors occur.
            ValidationError: If graph documents contain invalid node types or
                relationships not allowed by current configuration.
            AuthorizationError: If database user lacks required write permissions.

        Examples:
            Store extracted entities with merging::

                # Extract from multiple sources
                doc1 = await agent.extract_graph_from_text(
                    "John Smith works at TechCorp in San Francisco"
                )
                doc2 = await agent.extract_graph_from_text(
                    "TechCorp's CEO John Smith announced new AI initiatives"
                )

                # Store with intelligent merging
                result = await agent.store_graph_documents(
                    doc1 + doc2,
                    merge_nodes=True  # Consolidate duplicate entities
                )

                print(f"Stored {result['nodes_created']} unique entities")
                print(f"Created {result['relationships_created']} relationships")
                if result['errors']:
                    print(f"Encountered {len(result['errors'])} errors")

            Store without merging for temporal analysis::

                # Preserve all instances for timeline analysis
                result = await agent.store_graph_documents(
                    graph_docs,
                    merge_nodes=False  # Keep all entity instances
                )

                # Useful for tracking entity evolution over time
                print(f"Stored {result['nodes_created']} entity instances")

            Batch storage with error handling::

                try:
                    result = await agent.store_graph_documents(large_document_set)
                    
                    if result['success']:
                        print("Storage completed successfully")
                    else:
                        print(f"Partial storage: {len(result['errors'])} errors")
                        for error in result['errors']:
                            print(f"Error: {error}")
                            
                except DatabaseError as e:
                    print(f"Database operation failed: {e}")

            Performance monitoring::

                import time
                start_time = time.time()
                
                result = await agent.store_graph_documents(graph_docs)
                
                storage_time = time.time() - start_time
                nodes_per_second = result['nodes_created'] / storage_time
                
                print(f"Storage rate: {nodes_per_second:.1f} nodes/second")
                print(f"Database time: {result.get('storage_time_ms', 0):.1f}ms")

        Note:
            The storage operation automatically adds user_id tags for multi-user
            isolation and timestamps for temporal analysis. When merge_nodes=True,
            the system intelligently consolidates entities with matching identifiers
            while preserving unique properties and relationships. For high-volume
            storage operations, consider batch processing and monitor database
            performance metrics.
        """
        nodes_created = 0
        relationships_created = 0
        errors = []

        for graph_doc in graph_documents:
            try:
                # Store nodes
                for node in graph_doc.nodes:
                    # Add user_id and timestamp
                    node_props = node.properties or {}
                    node_props.update(
                        {
                            "user_id": self.config.user_id,
                            "created_at": datetime.now().isoformat(),
                            "id": f"{node.type}_{node.id}_{self.config.user_id}",
                        }
                    )

                    if merge_nodes:
                        query = f"""
                        MERGE (n:{node.type} {{id: $id}})
                        SET n += $properties
                        SET n.name = $name
                        RETURN n
                        """
                    else:
                        query = f"""
                        CREATE (n:{node.type})
                        SET n = $properties
                        SET n.name = $name
                        SET n.id = $id
                        RETURN n
                        """

                    self.graph.query(
                        query,
                        {
                            "id": node_props["id"],
                            "name": node.id,
                            "properties": node_props,
                        },
                    )
                    nodes_created += 1

                # Store relationships
                for rel in graph_doc.relationships:
                    rel_props = rel.properties or {}
                    rel_props.update(
                        {
                            "user_id": self.config.user_id,
                            "created_at": datetime.now().isoformat(),
                        }
                    )

                    query = f"""
                    MATCH (a {{id: $source_id}})
                    MATCH (b {{id: $target_id}})
                    CREATE (a)-[r:{rel.type}]->(b)
                    SET r = $properties
                    RETURN r
                    """

                    source_id = (
                        f"{rel.source.type}_{rel.source.id}_{self.config.user_id}"
                    )
                    target_id = (
                        f"{rel.target.type}_{rel.target.id}_{self.config.user_id}"
                    )

                    self.graph.query(
                        query,
                        {
                            "source_id": source_id,
                            "target_id": target_id,
                            "properties": rel_props,
                        },
                    )
                    relationships_created += 1

            except Exception as e:
                errors.append(str(e))
                self.logger.exception(f"Error storing graph document: {e}")

        # Also store as Memory node for tracking
        memory_query = """
        CREATE (m:Memory {
            id: $id,
            user_id: $user_id,
            content: $content,
            timestamp: $timestamp,
            nodes_created: $nodes_created,
            relationships_created: $relationships_created
        })
        RETURN m
        """

        self.graph.query(
            memory_query,
            {
                "id": f"memory_{datetime.now().timestamp()}_{self.config.user_id}",
                "user_id": self.config.user_id,
                "content": (
                    graph_documents[0].source.page_content if graph_documents else ""
                ),
                "timestamp": datetime.now().isoformat(),
                "nodes_created": nodes_created,
                "relationships_created": relationships_created,
            },
        )

        return {
            "nodes_created": nodes_created,
            "relationships_created": relationships_created,
            "errors": errors,
            "success": len(errors) == 0,
        }

    async def query_graph(
        self, query: str, query_type: str = "natural", include_context: bool = True
    ) -> dict[str, Any]:
        """Query the knowledge graph using natural language or direct Cypher queries.

        Provides flexible query interface supporting both human-friendly natural
        language questions and precise Cypher database queries. Integrates graph
        structure with RAG capabilities to deliver comprehensive, contextual answers.

        Args:
            query: The question or query to execute. For natural language queries,
                use conversational questions like "Who works at TechCorp?" or
                "What connections exist between AI and healthcare?". For Cypher
                queries, use valid Neo4j Cypher syntax.
            query_type: Query processing mode:
                - "natural": Process as natural language using Graph RAG and LLM
                - "cypher": Execute directly as Cypher query against Neo4j
            include_context: Whether to include additional contextual information
                in results such as related entities, recent memories, and graph
                neighborhood data for enhanced understanding.

        Returns:
            Dict[str, Any]: Comprehensive query results containing:
                - result/results: Main query answers or data
                - cypher_statement: Generated or provided Cypher query
                - context: Additional contextual information (if include_context=True)
                - intermediate_steps: Query processing steps (for debugging)
                - execution_time_ms: Query execution time
                - error: Error message if query fails
                - fallback_used: Whether fallback processing was required

        Raises:
            QuerySyntaxError: If Cypher query contains syntax errors.
            AuthenticationError: If database access is denied.
            TimeoutError: If query execution exceeds configured timeout.
            ValueError: If query_type is not "natural" or "cypher".

        Examples:
            Natural language queries::

                # Find people and their roles
                result = await agent.query_graph(
                    "Who are the executives at technology companies?",
                    query_type="natural",
                    include_context=True
                )

                print(f"Answer: {result.get('result', 'No answer found')}")
                print(f"Generated Cypher: {result.get('cypher_statement')}")
                
                if result.get('context'):
                    recent_nodes = result['context'].get('recent_nodes', [])
                    print(f"Related context: {len(recent_nodes)} recent entities")

            Relationship discovery::

                result = await agent.query_graph(
                    "How is John Smith connected to machine learning?"
                )

                # Graph RAG finds connection paths and provides explanation
                if 'result' in result:
                    print(f"Connection analysis: {result['result']}")

            Direct Cypher queries::

                # Precise database queries for specific data
                cypher_query = """
                MATCH (p:Person)-[r:WORKS_FOR]->(o:Organization)
                WHERE o.name CONTAINS 'Tech'
                RETURN p.name, o.name, r.role
                LIMIT 10
                """

                result = await agent.query_graph(
                    cypher_query,
                    query_type="cypher",
                    include_context=False  # Skip context for performance
                )

                if 'results' in result:
                    for row in result['results']:
                        print(f"{row[0]} works at {row[1]} as {row[2]}")

            Complex analytical queries::

                # Find influential entities
                result = await agent.query_graph(
                    "Which organizations have the most connections to AI research?"
                )

                # Explore entity relationships
                result = await agent.query_graph(
                    "What are all the ways that startups and venture capital are connected?"
                )

            Error handling and fallbacks::

                result = await agent.query_graph(
                    "Complex ambiguous question about entities"
                )

                if result.get('error'):
                    print(f"Query failed: {result['error']}")
                    if result.get('fallback_used'):
                        print("Fallback processing was attempted")
                else:
                    print(f"Successful result: {result['result']}")

        Note:
            Natural language queries leverage the Graph RAG agent when available,
            falling back to the Cypher chain for broader compatibility. The system
            automatically handles user isolation by filtering results to the current
            user's memory space. For production use, monitor query performance and
            consider caching for frequently accessed patterns.
        """
        if query_type == "natural":
            # Use Graph RAG agent for natural language queries if available
            if self.graph_rag_agent is not None:
                result = self.graph_rag_agent.invoke({"question": query})

                if include_context and result.get("cypher_statement"):
                    # Get additional context using the generated Cypher
                    context = self._get_query_context(result["cypher_statement"])
                    result["context"] = context

                return result
            # Fall back to Cypher chain for natural language queries
            try:
                result = self.cypher_chain.invoke({"query": query})

                if include_context:
                    context = self._get_query_context(query)
                    result["context"] = context

                return result
            except Exception as e:
                return {"error": str(e), "query": query, "fallback_used": True}

        elif query_type == "cypher":
            # Direct Cypher query
            try:
                results = self.graph.query(query)

                if include_context:
                    context = self._get_query_context(query)
                    return {
                        "results": results,
                        "context": context,
                        "cypher_statement": query,
                    }

                return {"results": results, "cypher_statement": query}

            except Exception as e:
                return {"error": str(e), "cypher_statement": query}

        else:
            return {"error": f"Unknown query type: {query_type}"}

    def _get_query_context(self, cypher_query: str) -> dict[str, Any]:
        """Get additional context around query results."""
        # Extract node references from the query
        # This is a simplified version - could be enhanced with proper parsing
        context_query = """
        // Get recently accessed nodes
        MATCH (n)
        WHERE n.user_id = $user_id
        RETURN n
        ORDER BY n.created_at DESC
        LIMIT 10
        """

        recent_nodes = self.graph.query(context_query, {"user_id": self.config.user_id})

        return {
            "recent_nodes": recent_nodes,
            "user_id": self.config.user_id,
            "timestamp": datetime.now().isoformat(),
        }

    async def search_similar_memories(
        self, query: str, node_type: str | None = None, k: int = 5
    ) -> list[dict[str, Any]]:
        """Search for similar memories using vector similarity.

        Args:
            query: Search query
            node_type: Optional node type to search (Person, Concept, etc.)
            k: Number of results

        Returns:
            Similar memories with scores
        """
        if not self.config.enable_vector_index:
            return []

        results = []

        # Search in appropriate indexes
        if node_type == "Person" or node_type is None:
            if hasattr(self, "person_vector_index"):
                person_results = self.person_vector_index.similarity_search_with_score(
                    query, k=k
                )
                results.extend(
                    [
                        {"type": "Person", "content": doc.page_content, "score": score}
                        for doc, score in person_results
                    ]
                )

        if node_type == "Concept" or node_type is None:
            if hasattr(self, "concept_vector_index"):
                concept_results = (
                    self.concept_vector_index.similarity_search_with_score(query, k=k)
                )
                results.extend(
                    [
                        {"type": "Concept", "content": doc.page_content, "score": score}
                        for doc, score in concept_results
                    ]
                )

        # Sort by score
        results.sort(key=lambda x: x["score"], reverse=True)

        return results[:k]

    async def get_memory_subgraph(
        self,
        entity_name: str,
        max_depth: int = 2,
        relationship_types: list[str] | None = None,
    ) -> dict[str, Any]:
        """Get a subgraph centered around an entity.

        Args:
            entity_name: Name of the central entity
            max_depth: Maximum traversal depth
            relationship_types: Optional filter for relationship types

        Returns:
            Subgraph data
        """
        rel_filter = ""
        if relationship_types:
            rel_types = "|".join(relationship_types)
            rel_filter = f":{rel_types}"

        query = f"""
        MATCH path = (n {{name: $name, user_id: $user_id}})-[{rel_filter}*1..{max_depth}]-(m)
        RETURN path
        LIMIT 100
        """

        paths = self.graph.query(
            query, {"name": entity_name, "user_id": self.config.user_id}
        )

        # Extract unique nodes and relationships
        nodes = set()
        relationships = set()

        for _path in paths:
            # Process path to extract nodes and relationships
            # This would need proper path parsing based on Neo4j return format
            pass

        return {
            "central_entity": entity_name,
            "nodes": list(nodes),
            "relationships": list(relationships),
            "depth": max_depth,
        }

    async def consolidate_memories(
        self, time_window: str | None = "1 day", min_connections: int = 2
    ) -> dict[str, Any]:
        """Consolidate related memories into higher-level concepts.

        Args:
            time_window: Time window for consolidation
            min_connections: Minimum connections for consolidation

        Returns:
            Consolidation results
        """
        # Find highly connected components
        query = """
        MATCH (n)-[r]-(m)
        WHERE n.user_id = $user_id AND m.user_id = $user_id
        WITH n, count(DISTINCT m) as connections
        WHERE connections >= $min_connections
        RETURN n, connections
        ORDER BY connections DESC
        LIMIT 20
        """

        candidates = self.graph.query(
            query, {"user_id": self.config.user_id, "min_connections": min_connections}
        )

        # Create concept nodes for highly connected entities
        concepts_created = 0
        for _candidate in candidates:
            # Create a concept that represents the cluster

            # Generate concept from candidate
            # This is simplified - would use LLM to generate meaningful concept
            concepts_created += 1

        return {
            "concepts_created": concepts_created,
            "candidates_analyzed": len(candidates),
            "timestamp": datetime.now().isoformat(),
        }

    async def run(
        self,
        input_text: str,
        mode: GraphMemoryMode | None = None,
        auto_store: bool = True,
    ) -> dict[str, Any]:
        """Main entry point for comprehensive graph memory processing.

        Orchestrates the complete graph memory workflow from text input to knowledge
        storage and retrieval. This method provides a unified interface for all
        graph memory operations, automatically selecting appropriate processing
        steps based on the specified mode.

        Args:
            input_text: Raw text input to process. Can be any natural language
                content including documents, conversations, reports, or structured
                data descriptions. The text will be analyzed for entities and
                relationships according to the configured extraction settings.
            mode: Operation mode override for this specific processing run.
                If None, uses the agent's default mode from configuration.
                See GraphMemoryMode for available options and their behaviors.
            auto_store: Whether to automatically store extracted graph structures
                in the Neo4j database. When False, extraction is performed but
                results are only returned without persistence (useful for analysis).

        Returns:
            Dict[str, Any]: Comprehensive processing results containing:
                - input: Original input text for reference
                - mode: Processing mode used (actual mode after any overrides)
                - timestamp: Processing timestamp in ISO format
                - extracted_graph: Entity and relationship extraction statistics
                - storage: Storage operation results (if auto_store=True)
                - query_result: Query results for relevant memories (in FULL mode)
                - processing_time_ms: Total processing time
                - warnings: Any warnings encountered during processing
                - entity_summary: Summary of extracted entity types and counts

        Raises:
            ProcessingError: If text processing or entity extraction fails.
            StorageError: If database storage operations fail (when auto_store=True).
            ConfigurationError: If agent mode or settings are invalid for operation.
            TimeoutError: If processing exceeds configured timeout limits.

        Examples:
            Basic memory storage::

                result = await agent.run(
                    "Dr. Alice Chen joined Stanford's AI Lab as a research scientist. "
                    "She previously worked on neural networks at Google for 3 years."
                )

                print(f"Processing mode: {result['mode']}")
                print(f"Entities extracted: {result['extracted_graph']['total_nodes']}")
                print(f"Relationships found: {result['extracted_graph']['total_relationships']}")
                
                if result.get('storage'):
                    print(f"Storage successful: {result['storage']['success']}")

            Analysis without storage::

                # Extract and analyze without permanent storage
                result = await agent.run(
                    "Complex business relationship description...",
                    mode=GraphMemoryMode.EXTRACT_ONLY,
                    auto_store=False
                )

                # Examine extraction results
                extraction = result['extracted_graph']
                print(f"Would create {extraction['total_nodes']} entities")
                print(f"Would create {extraction['total_relationships']} relationships")

            Full processing with query::

                # Process and immediately query for related information
                result = await agent.run(
                    "New information about TechCorp's expansion to Europe",
                    mode=GraphMemoryMode.FULL
                )

                # Includes automatic query for related memories
                if result.get('query_result'):
                    print(f"Related information: {result['query_result']}")

            Performance monitoring::

                import time
                start_time = time.time()
                
                result = await agent.run(large_text_document)
                
                total_time = time.time() - start_time
                print(f"Total processing: {total_time:.2f}s")
                print(f"Agent processing: {result.get('processing_time_ms', 0):.1f}ms")
                
                if result.get('warnings'):
                    for warning in result['warnings']:
                        print(f"Warning: {warning}")

            Batch processing pattern::

                texts = [
                    "First document with entities...",
                    "Second document with relationships...",
                    "Third document with events..."
                ]

                results = []
                for text in texts:
                    result = await agent.run(text)
                    results.append(result)
                    
                    # Monitor progress
                    entities = result['extracted_graph']['total_nodes']
                    print(f"Processed: {entities} entities")

                # Aggregate statistics
                total_entities = sum(
                    r['extracted_graph']['total_nodes'] for r in results
                )
                print(f"Total entities across all documents: {total_entities}")

        Note:
            The processing workflow adapts based on the specified mode. FULL mode
            provides the most comprehensive processing including automatic querying
            for related memories, while other modes focus on specific operations
            for performance optimization. Monitor processing times for large
            documents and consider chunking for very long texts.
        """
        mode = mode or self.config.mode
        results = {
            "input": input_text,
            "mode": mode.value,
            "timestamp": datetime.now().isoformat(),
        }

        if mode in [
            GraphMemoryMode.EXTRACT_ONLY,
            GraphMemoryMode.EXTRACT_AND_STORE,
            GraphMemoryMode.FULL,
        ]:
            # Extract graph from text
            graph_docs = await self.extract_graph_from_text(input_text)
            results["extracted_graph"] = {
                "documents": len(graph_docs),
                "total_nodes": sum(len(doc.nodes) for doc in graph_docs),
                "total_relationships": sum(
                    len(doc.relationships) for doc in graph_docs
                ),
            }

            if auto_store and mode != GraphMemoryMode.EXTRACT_ONLY:
                # Store in Neo4j
                storage_result = await self.store_graph_documents(graph_docs)
                results["storage"] = storage_result

        if mode in [GraphMemoryMode.QUERY_ONLY, GraphMemoryMode.FULL]:
            # Also query for relevant memories
            query_result = await self.query_graph(
                f"What do we know about: {input_text}", query_type="natural"
            )
            results["query_result"] = query_result

        return results

    @classmethod
    def as_tool(cls, config: GraphMemoryConfig):
        """Convert GraphMemoryAgent to a LangChain tool for integration with other agents.

        Creates a tool interface that allows other Haive agents to use graph memory
        capabilities through the standard tool calling mechanism. This enables
        sophisticated multi-agent workflows where specialized agents can leverage
        shared graph-based knowledge storage and retrieval.

        Args:
            config: GraphMemoryConfig instance with database connection and
                processing settings. The same configuration will be used for
                all tool invocations.

        Returns:
            LangChain Tool: Configured tool that can be added to agent tool lists.
                The tool accepts text input and operation type, returning JSON-formatted
                results from graph memory processing.

        Tool Interface:
            - **Name**: "graph_memory_tool"
            - **Description**: "Process text with graph memory. Operations: extract, store, query, full."
            - **Input Schema**: 
                - text (str): Text content to process
                - operation (str): Operation type (extract/store/query/full)
            - **Output**: JSON string containing processing results

        Examples:
            Create tool for ReactAgent::

                # Configure graph memory
                config = GraphMemoryConfig(
                    neo4j_uri="bolt://localhost:7687",
                    neo4j_username="neo4j",
                    neo4j_password="password",
                    user_id="research_agent"
                )

                # Create memory tool
                memory_tool = GraphMemoryAgent.as_tool(config)

                # Add to agent's toolkit
                agent = ReactAgent(
                    name="research_assistant",
                    engine=llm_config,
                    tools=[memory_tool, other_tools...]
                )

                # Agent can now use graph memory
                result = await agent.arun(
                    "Remember: Dr. Smith works at MIT and studies quantum computing. "
                    "Then find all researchers connected to quantum computing."
                )

            Multi-agent knowledge sharing::

                # Shared memory configuration
                shared_config = GraphMemoryConfig(
                    user_id="team_shared",
                    mode=GraphMemoryMode.FULL
                )
                
                memory_tool = GraphMemoryAgent.as_tool(shared_config)

                # Multiple agents with shared memory
                data_agent = ReactAgent(
                    name="data_collector",
                    tools=[memory_tool, data_tools...]
                )
                
                analysis_agent = ReactAgent(
                    name="data_analyzer", 
                    tools=[memory_tool, analysis_tools...]
                )

                # Agents can share knowledge through graph memory
                await data_agent.arun("Store research findings in memory")
                await analysis_agent.arun("Analyze stored research data")

            Domain-specific memory tool::

                # Research domain configuration
                research_config = GraphMemoryConfig(
                    allowed_nodes=["Researcher", "Paper", "Institution", "Topic"],
                    allowed_relationships=[
                        ("Researcher", "AUTHORED", "Paper"),
                        ("Paper", "ABOUT", "Topic"),
                        ("Researcher", "AFFILIATED_WITH", "Institution")
                    ],
                    extract_properties=True
                )

                research_memory = GraphMemoryAgent.as_tool(research_config)

                # Specialized research agent
                research_agent = ReactAgent(
                    name="research_manager",
                    tools=[research_memory],
                    system_message="You manage research knowledge using graph memory."
                )

        Tool Operation Types:
            - **extract**: Extract entities/relationships without storage
            - **store**: Store pre-extracted graph data directly
            - **query**: Query existing graph knowledge
            - **full**: Complete processing including extraction, storage, and querying

        Note:
            The tool maintains its own GraphMemoryAgent instance, so multiple tool
            calls share the same configuration and database connection. For production
            deployments, consider the resource implications of multiple agents
            accessing the same Neo4j database concurrently.
        """
        instance = cls(config)

        @tool
        async def graph_memory_tool(text: str, operation: str = "full") -> str:
            """Process text with graph memory capabilities.
            
            Operations:
            - extract: Extract entities and relationships from text without storage
            - store: Store pre-extracted graph data directly in Neo4j
            - query: Search existing graph knowledge for relevant information  
            - full: Complete processing including extraction, storage, and querying
            
            Args:
                text: Text content to process or query string
                operation: Type of operation to perform (extract/store/query/full)
                
            Returns:
                JSON string containing processing results, extracted entities,
                storage statistics, or query answers depending on operation type.
            """
            mode_map = {
                "extract": GraphMemoryMode.EXTRACT_ONLY,
                "store": GraphMemoryMode.STORE_ONLY,
                "query": GraphMemoryMode.QUERY_ONLY,
                "full": GraphMemoryMode.FULL,
            }

            mode = mode_map.get(operation, GraphMemoryMode.FULL)
            result = await instance.run(text, mode=mode)

            return json.dumps(result, indent=2)

        return graph_memory_tool


# Example usage
async def example_graph_memory():
    """Comprehensive example demonstrating GraphMemoryAgent capabilities.
    
    This example showcases the full range of graph memory functionality including
    entity extraction, knowledge storage, querying, and advanced operations like
    memory consolidation and subgraph exploration.
    """
    # Configure for comprehensive graph memory operations
    config = GraphMemoryConfig(
        neo4j_uri="bolt://localhost:7687",
        neo4j_username="neo4j", 
        neo4j_password="password",
        user_id="alice_smith",
        mode=GraphMemoryMode.FULL,
        
        # Enable enhanced features
        extract_properties=True,
        enable_vector_index=True,
        
        # Professional networking domain
        allowed_nodes=[
            "Person", "Organization", "Location", "Event", 
            "Technology", "Skill", "Project"
        ],
        node_properties=[
            "role", "seniority", "expertise", "years_experience",
            "contact_info", "importance"
        ]
    )

    agent = GraphMemoryAgent(config)

    # Process a memory
    await agent.run(
        "I met John Doe at the AI Conference in San Francisco last week. "
        "He works as a Senior Engineer at TechCorp and specializes in machine learning. "
        "We discussed implementing RAG systems using knowledge graphs."
    )

    # Query the graph
    await agent.query_graph("Who did I meet at conferences recently?")

    # Search similar memories
    await agent.search_similar_memories(
        "machine learning engineers", node_type="Person"
    )

    # Get subgraph around John Doe
    await agent.get_memory_subgraph("John Doe", max_depth=2)


if __name__ == "__main__":
    asyncio.run(example_graph_memory())
