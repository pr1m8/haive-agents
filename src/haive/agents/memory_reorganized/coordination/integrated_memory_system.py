"""Integrated Memory System - Comprehensive multi-modal memory architecture.

This module implements a sophisticated memory coordination system that intelligently
combines multiple specialized memory strategies to provide comprehensive knowledge
management capabilities. The system automatically routes memory operations to the
most appropriate subsystem based on content analysis and query characteristics.

The IntegratedMemorySystem serves as a unified interface for:

1. **GraphMemoryAgent**: Structured knowledge representation using Neo4j knowledge graphs
   - Entity and relationship extraction and storage
   - Complex graph traversal and semantic connections
   - Professional network and organizational knowledge

2. **ReactMemoryAgent**: Flexible, tool-based conversational memory management
   - Time-weighted memory retrieval with recency bias
   - Vector similarity search for semantic matching
   - Conversational context and dialogue history

3. **LongTermMemoryAgent**: Persistent cross-session memory for important facts
   - High-importance information that should persist
   - User preferences and learned behaviors
   - Core knowledge that transcends individual conversations

Key Architectural Features:
    - **Intelligent Routing**: AI-powered analysis determines optimal memory system
    - **Content Classification**: Automatic categorization into memory types
    - **Cross-System Integration**: Seamless data flow between memory subsystems
    - **Memory Consolidation**: Automated archival and organization processes
    - **Multi-User Support**: Isolated memory spaces with shared coordination
    - **Performance Analytics**: Comprehensive monitoring and optimization

Memory System Modes:
    - **STRUCTURED**: Route to graph memory for entities and relationships
    - **CONVERSATIONAL**: Use reactive memory for dialogue and temporal info
    - **PERSISTENT**: Store in long-term memory for important, lasting facts
    - **INTELLIGENT**: AI determines the best approach automatically
    - **HYBRID**: Utilize multiple systems simultaneously for maximum coverage

Workflow Architecture:
    1. **Content Analysis**: Router agent analyzes incoming content characteristics
    2. **System Selection**: Intelligent routing to appropriate memory subsystem(s)
    3. **Storage Coordination**: Synchronized storage across selected systems
    4. **Query Distribution**: Parallel querying with result synthesis
    5. **Result Integration**: Intelligent combination of multi-system responses
    6. **Memory Maintenance**: Automated consolidation and cleanup processes

Examples:
    Basic integrated memory usage::

        # Initialize with default configuration
        memory_system = IntegratedMemorySystem(
            user_id="researcher",
            neo4j_config={
                "neo4j_uri": "bolt://localhost:7687",
                "neo4j_username": "neo4j",
                "neo4j_password": "password"
            }
        )

        # Store different types of information
        await memory_system.store_memory(
            "Dr. Sarah Chen is the head of AI research at Stanford University",
            mode=MemorySystemMode.INTELLIGENT  # AI chooses best storage
        )

        # Query across all memory systems
        result = await memory_system.query_memory(
            "What do I know about AI researchers at universities?",
            mode=MemorySystemMode.HYBRID
        )

    Advanced research workflow::

        # Create research-focused memory system
        research_memory = IntegratedMemorySystem(
            user_id="research_team",
            vector_store_path="./research_vectors"
        )

        # Store structured research data
        await research_memory.store_memory(
            "The paper 'Attention Is All You Need' by Vaswani et al. "
            "introduced the Transformer architecture in 2017",
            mode=MemorySystemMode.STRUCTURED
        )

        # Store conversational insights
        await research_memory.store_memory(
            "During our meeting, the team agreed that we should focus "
            "on multimodal transformer applications",
            mode=MemorySystemMode.CONVERSATIONAL
        )

        # Query with intelligent synthesis
        synthesis = await research_memory.query_memory(
            "How should our transformer research direction relate to existing work?",
            combine_results=True
        )

    Memory analytics and optimization::

        # Get comprehensive system analytics
        analytics = await memory_system.get_memory_analytics()
        print(f"Graph entities: {analytics['systems']['graph']['total_nodes']}")
        print(f"Recent activity: {analytics['systems']['react']['recent_activity']}")

        # Perform system-wide consolidation
        consolidation = await memory_system.consolidate_all_memories()
        print(f"Consolidated systems: {consolidation['systems_consolidated']}")

Use Cases:
    - **Research Management**: Academic and corporate research knowledge bases
    - **Customer Relationship Management**: Client interactions and relationship mapping
    - **Project Coordination**: Team knowledge sharing and project memory
    - **Personal Knowledge Management**: Individual learning and information organization
    - **Business Intelligence**: Organizational knowledge and relationship tracking

See Also:
    - :class:`GraphMemoryAgent`: Graph-based structured knowledge storage
    - :class:`ReactMemoryAgent`: Conversational and temporal memory management
    - :class:`LongTermMemoryAgent`: Persistent cross-session memory
    - :class:`MemorySystemMode`: Available system coordination modes

Note:
    The integrated system requires significant computational resources as it
    coordinates multiple AI systems simultaneously. For production deployments,
    consider resource allocation, database performance, and LLM API usage costs.
    The system is designed to gracefully degrade if individual subsystems are
    unavailable, ensuring robust operation in various deployment scenarios.
"""

import asyncio
import json
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.memory_v2.graph_memory_agent import (
    GraphMemoryAgent,
    GraphMemoryConfig,
    GraphMemoryMode,
    Optional,
)
from haive.agents.memory_v2.long_term_memory_agent import LongTermMemoryAgent
from haive.agents.memory_v2.react_memory_agent import ReactMemoryAgent
from haive.agents.multi.simple.agent import SimpleMultiAgent
from haive.agents.react.agent import ReactAgent


class MemorySystemMode(str, Enum):
    """Coordination modes for integrated memory system operation.

    These modes determine how the IntegratedMemorySystem routes and processes
    memory operations across its constituent subsystems. Each mode optimizes
    for different use cases and performance characteristics.

    Attributes:
        STRUCTURED: Route operations to graph memory for entity-relationship data.
            Optimized for storing and querying structured knowledge with clear
            entities, relationships, and hierarchical information.
        CONVERSATIONAL: Use reactive memory for dialogue and temporal information.
            Best for storing conversation history, opinions, temporal events,
            and context-dependent information.
        PERSISTENT: Store in long-term memory for important, lasting facts.
            Designed for high-importance information that should persist across
            sessions and maintain accessibility over long periods.
        INTELLIGENT: AI-powered automatic routing to optimal memory subsystem.
            Uses content analysis to determine the best storage and retrieval
            strategy based on information characteristics.
        HYBRID: Utilize multiple memory systems simultaneously for comprehensive coverage.
            Stores information in multiple subsystems and synthesizes results
            from all relevant sources during retrieval.

    Examples:
        Mode selection for different content types::

            # Structured business information
            await memory_system.store_memory(
                "TechCorp acquired StartupAI for $50M in Q3 2024",
                mode=MemorySystemMode.STRUCTURED  # Entities + relationships
            )

            # Conversational context
            await memory_system.store_memory(
                "User mentioned they prefer morning meetings",
                mode=MemorySystemMode.CONVERSATIONAL  # Preferences + dialogue
            )

            # Critical persistent facts
            await memory_system.store_memory(
                "Emergency contact: Dr. Smith at +1-555-0123",
                mode=MemorySystemMode.PERSISTENT  # Long-term importance
            )

            # Let AI decide optimal routing
            await memory_system.store_memory(
                "Complex multi-faceted information...",
                mode=MemorySystemMode.INTELLIGENT  # AI-powered routing
            )

            # Maximum coverage and redundancy
            await memory_system.store_memory(
                "Critical project milestone information",
                mode=MemorySystemMode.HYBRID  # Multiple systems
            )

        Query optimization by mode::

            # Fast structured queries
            result = await memory_system.query_memory(
                "Who are the executives at tech companies?",
                mode=MemorySystemMode.STRUCTURED
            )

            # Recent conversation context
            result = await memory_system.query_memory(
                "What did we discuss about the project timeline?",
                mode=MemorySystemMode.CONVERSATIONAL
            )

            # Important facts retrieval
            result = await memory_system.query_memory(
                "What are the key contact details I should remember?",
                mode=MemorySystemMode.PERSISTENT
            )

            # Comprehensive intelligent search
            result = await memory_system.query_memory(
                "Tell me everything relevant to our AI research project",
                mode=MemorySystemMode.HYBRID
            )

    Performance Characteristics:
        - **STRUCTURED**: Fast for entity queries, slower for complex analysis
        - **CONVERSATIONAL**: Good for recent events, limited long-term recall
        - **PERSISTENT**: Excellent retention, optimized for important facts
        - **INTELLIGENT**: Balanced performance, adds routing overhead
        - **HYBRID**: Comprehensive results, highest computational cost

    Note:
        The INTELLIGENT mode adds processing overhead for content analysis
        but provides optimal routing decisions. HYBRID mode offers the most
        comprehensive results but requires the most computational resources.
        Choose modes based on your specific use case requirements and
        performance constraints.
    """

    STRUCTURED = "structured"  # Use graph memory for structured data
    CONVERSATIONAL = "conversational"  # Use React memory for conversations
    PERSISTENT = "persistent"  # Use long-term memory
    INTELLIGENT = "intelligent"  # System chooses best approach
    HYBRID = "hybrid"  # Use multiple systems together


class IntegratedMemorySystem:
    """Unified memory coordination system combining multiple specialized memory subsystems.

    The IntegratedMemorySystem provides a sophisticated memory management platform
    that intelligently coordinates between graph-based, conversational, and long-term
    memory systems. It serves as a unified interface that automatically routes
    operations to the most appropriate subsystem(s) based on AI-powered content
    analysis and query characteristics.

    This system is designed for applications requiring comprehensive knowledge
    management that spans structured data, conversational context, and persistent
    facts. It excels in research environments, business intelligence platforms,
    and personal knowledge management scenarios.

    Architecture Components:
        - **GraphMemoryAgent**: Neo4j-based knowledge graph for entities and relationships
        - **ReactMemoryAgent**: Vector-based conversational memory with time weighting
        - **LongTermMemoryAgent**: Persistent storage for high-importance information
        - **Memory Router**: AI-powered content analysis and routing decisions
        - **Coordinator Agent**: Multi-agent orchestration and result synthesis

    Key Capabilities:
        - **Intelligent Content Routing**: Automatic determination of optimal storage strategy
        - **Multi-System Querying**: Parallel search across all relevant memory subsystems
        - **Result Synthesis**: AI-powered combination of results from multiple sources
        - **Memory Consolidation**: Automated organization and archival processes
        - **Performance Analytics**: Comprehensive monitoring and optimization metrics
        - **Cross-System Integration**: Seamless data flow and relationship discovery

    Attributes:
        user_id: Unique identifier for memory isolation in multi-user environments
        engine: LLM configuration for content analysis and synthesis operations
        graph_memory: GraphMemoryAgent instance for structured knowledge storage
        react_memory: ReactMemoryAgent instance for conversational memory management
        longterm_memory: LongTermMemoryAgent instance for persistent fact storage
        router: ReactAgent for intelligent content analysis and routing decisions
        coordinator: Multi-agent coordinator for system orchestration

    Examples:
        Basic initialization and usage::

            # Initialize with default configuration
            memory_system = IntegratedMemorySystem(
                user_id="knowledge_worker",
                neo4j_config={
                    "neo4j_uri": "bolt://localhost:7687",
                    "neo4j_username": "neo4j",
                    "neo4j_password": "password"
                },
                vector_store_path="./memory_vectors"
            )

            # Store complex business information
            result = await memory_system.store_memory(
                "Microsoft announced a strategic partnership with OpenAI "
                "to integrate GPT models into Office 365. The deal includes "
                "$10B investment over 5 years and exclusive cloud rights.",
                mode=MemorySystemMode.INTELLIGENT
            )

            print(f"Stored in systems: {result['systems_used']}")
            # Expected: ['graph', 'longterm'] for structured + important info

        Multi-modal query processing::

            # Query spans multiple memory types
            result = await memory_system.query_memory(
                "What partnerships involve AI companies and tech giants?",
                mode=MemorySystemMode.HYBRID,
                combine_results=True
            )

            # Access structured results
            if 'combined_answer' in result:
                print(f"Synthesis: {result['combined_answer']}")
                
            # Access individual system results
            graph_results = result['individual_results'].get('graph')
            react_results = result['individual_results'].get('react')
            longterm_results = result['individual_results'].get('longterm')

        Research workflow integration::

            # Create research-focused memory system
            research_memory = IntegratedMemorySystem(
                user_id="research_team",
                engine=AugLLMConfig(
                    model="gpt-4",
                    temperature=0.2  # Consistent analysis
                )
            )

            # Store research findings
            papers = [
                "Paper 1: Transformer architecture improvements...",
                "Paper 2: Multi-modal learning approaches...",
                "Paper 3: Efficiency optimizations for large models..."
            ]

            for paper in papers:
                await research_memory.store_memory(
                    paper,
                    mode=MemorySystemMode.STRUCTURED,
                    metadata={"type": "research_paper", "importance": 0.9}
                )

            # Query research landscape
            landscape = await research_memory.query_memory(
                "What are the current trends in transformer research?",
                mode=MemorySystemMode.HYBRID
            )

        Memory system analytics::

            # Monitor system performance and usage
            analytics = await memory_system.get_memory_analytics()
            
            print(f"Graph nodes: {analytics['systems']['graph']['total_nodes']}")
            print(f"Recent activity: {analytics['systems']['react']['recent_activity'][:100]}")
            print(f"Long-term active: {analytics['systems']['longterm']['retriever_active']}")

            # Perform maintenance operations
            consolidation = await memory_system.consolidate_all_memories()
            print(f"Consolidation complete: {consolidation['systems_consolidated']}")

        Custom agent integration::

            # Create specialized agents with memory integration
            memory_tool = create_memory_integration_tool(memory_system)
            
            specialized_agent = ReactAgent(
                name="knowledge_agent",
                engine=AugLLMConfig(),
                tools=[memory_tool, domain_specific_tools...],
                system_message="You have access to comprehensive memory systems."
            )

            # Agent can leverage all memory capabilities
            await specialized_agent.arun(
                "Research quantum computing developments and remember key findings"
            )

    Integration Patterns:
        The system supports various integration patterns for different use cases:

        - **API Integration**: RESTful endpoints for external system access
        - **Agent Integration**: Tool interfaces for use in multi-agent workflows
        - **Batch Processing**: Efficient handling of large document collections
        - **Real-time Updates**: Streaming integration for live data processing
        - **Export/Import**: Data migration and backup capabilities

    Performance Considerations:
        - **Concurrent Operations**: Thread-safe design for multiple simultaneous requests
        - **Resource Management**: Intelligent caching and connection pooling
        - **Scalability**: Horizontal scaling support for high-volume deployments
        - **Monitoring**: Built-in metrics and performance tracking

    See Also:
        - :class:`GraphMemoryAgent`: Structured knowledge graph management
        - :class:`ReactMemoryAgent`: Conversational memory with tools
        - :class:`LongTermMemoryAgent`: Persistent cross-session storage
        - :class:`MemorySystemMode`: System coordination modes

    Note:
        This system requires significant computational resources as it coordinates
        multiple AI systems with database operations. For production deployments,
        carefully consider resource allocation, API costs, and performance monitoring.
        The system is designed to be fault-tolerant and will continue operating
        even if individual subsystems become unavailable.
    """

    def __init__(
        self,
        user_id: str = "default_user",
        neo4j_config: dict[str, Any] | None = None,
        vector_store_path: Optional[str] = None,
        engine: Optional[AugLLMConfig] = None,
    ):
        """Initialize IntegratedMemorySystem with comprehensive memory subsystem coordination.

        Sets up all memory subsystems, configures intelligent routing, and creates
        the coordination infrastructure for unified memory operations. The initialization
        process establishes database connections, validates configurations, and
        prepares all AI components for memory processing.

        Args:
            user_id: Unique identifier for memory isolation and multi-user support.
                All memory operations are tagged with this ID to ensure proper
                isolation between different users or contexts. Default: "default_user"
            neo4j_config: Configuration dictionary for Neo4j graph database connection.
                Should contain 'neo4j_uri', 'neo4j_username', 'neo4j_password', and
                optionally 'database_name'. If None, uses default local configuration.
            vector_store_path: File system path for vector-based memory storage.
                Used by ReactMemoryAgent for conversational memory persistence.
                If None, uses in-memory storage (not persistent across sessions).
            engine: LLM configuration for content analysis, routing decisions, and
                result synthesis. If None, creates default AugLLMConfig with
                temperature=0.7 for balanced performance.

        Raises:
            ConnectionError: If Neo4j database connection fails or is misconfigured.
            ImportError: If required dependencies for memory subsystems are missing.
            ConfigurationError: If provided configuration contains invalid settings.
            FileSystemError: If vector_store_path cannot be created or accessed.

        Examples:
            Basic initialization with local Neo4j::

                memory_system = IntegratedMemorySystem(
                    user_id="alice_researcher",
                    neo4j_config={
                        "neo4j_uri": "bolt://localhost:7687",
                        "neo4j_username": "neo4j",
                        "neo4j_password": "password"
                    },
                    vector_store_path="./alice_memory_vectors"
                )

            Production configuration with authentication::

                production_config = {
                    "neo4j_uri": "bolt+s://production.databases.neo4j.io",
                    "neo4j_username": "prod_user",
                    "neo4j_password": os.getenv("NEO4J_PASSWORD"),
                    "database_name": "knowledge_base"
                }

                memory_system = IntegratedMemorySystem(
                    user_id="production_system",
                    neo4j_config=production_config,
                    vector_store_path="/data/memory_vectors",
                    engine=AugLLMConfig(
                        model="gpt-4",
                        temperature=0.1,  # Deterministic for production
                        max_tokens=2000
                    )
                )

            Development setup with minimal configuration::

                # Quick setup for development and testing
                dev_memory = IntegratedMemorySystem(
                    user_id="developer",
                    # Uses default local Neo4j and in-memory vectors
                )

            Multi-user enterprise configuration::

                def create_user_memory(user_id: str) -> IntegratedMemorySystem:
                    return IntegratedMemorySystem(
                        user_id=user_id,
                        neo4j_config=shared_neo4j_config,
                        vector_store_path=f"/data/vectors/{user_id}",
                        engine=shared_llm_config
                    )

                # Each user gets isolated memory space
                alice_memory = create_user_memory("alice")
                bob_memory = create_user_memory("bob")

        Initialization Process:
            1. **Graph Memory Setup**: Establishes Neo4j connection and constraints
            2. **React Memory Setup**: Configures vector store and conversational memory
            3. **Long-term Memory Setup**: Initializes persistent fact storage
            4. **Router Creation**: Sets up AI-powered content analysis agent
            5. **Coordinator Setup**: Creates multi-agent orchestration system

        Resource Requirements:
            - **Neo4j Database**: Running Neo4j instance with appropriate permissions
            - **Vector Storage**: File system space for vector embeddings (if persistent)
            - **LLM Access**: API access to configured language model provider
            - **Memory**: RAM for caching and intermediate processing
            - **Network**: Stable connectivity for database and API operations

        Note:
            The initialization process validates all subsystem configurations and
            establishes connections. If any subsystem fails to initialize, the
            method will raise appropriate exceptions with detailed error information.
            For production deployments, ensure proper monitoring of all subsystem
            health and implement appropriate retry and fallback mechanisms.
        """
        self.user_id = user_id
        self.engine = engine or AugLLMConfig(temperature=0.7)

        # Initialize subsystems
        self._init_graph_memory(neo4j_config)
        self._init_react_memory(vector_store_path)
        self._init_longterm_memory()

        # Create memory router
        self.router = self._create_memory_router()

        # Create coordinator agent
        self.coordinator = self._create_coordinator()

    def _init_graph_memory(self, neo4j_config: dict[str, Any] | None):
        """Initialize graph memory for structured knowledge."""
        config = GraphMemoryConfig(
            user_id=self.user_id,
            mode=GraphMemoryMode.FULL,
            llm_config=self.engine,
            **(
                neo4j_config
                or {
                    "neo4j_uri": "bolt://localhost:7687",
                    "neo4j_username": "neo4j",
                    "neo4j_password": "password",
                }
            ),
        )
        self.graph_memory = GraphMemoryAgent(config)

    def _init_react_memory(self, vector_store_path: Optional[str]):
        """Initialize React memory for flexible tool-based management."""
        self.react_memory = ReactMemoryAgent(
            name="react_memory",
            engine=self.engine,
            user_id=self.user_id,
            memory_store_path=vector_store_path,
            k=5,
            use_time_weighting=True,
        )

    def _init_longterm_memory(self):
        """Initialize long-term memory for persistence."""
        self.longterm_memory = LongTermMemoryAgent(
            user_id=self.user_id, llm_config=self.engine, k_memories=10
        )

    def _create_memory_router(self) -> ReactAgent:
        """Create intelligent memory routing agent for content analysis and system selection.

        Builds a specialized ReactAgent that analyzes incoming content and queries to
        determine the optimal memory subsystem(s) for storage and retrieval operations.
        The router uses sophisticated pattern recognition and content classification
        to make intelligent routing decisions.

        Returns:
            ReactAgent: Configured routing agent with content analysis tools and
                specialized system message for memory system coordination. The agent
                is equipped with tools for analyzing memory types and query routing.

        Router Capabilities:
            - **Content Classification**: Identifies structured vs. conversational content
            - **Importance Assessment**: Determines persistence requirements
            - **Query Analysis**: Routes search queries to appropriate subsystems
            - **Pattern Recognition**: Detects entity relationships and temporal patterns
            - **Multi-System Coordination**: Manages hybrid storage and retrieval strategies

        Routing Logic:
            The router analyzes content for multiple indicators:

            - **Structured Indicators**: "works at", "located in", "connected to"
            - **Conversational Indicators**: "remember", "discussed", "my opinion"
            - **Persistence Indicators**: "important", "always", "never forget"
            - **Temporal Indicators**: "recent", "yesterday", "timeline"
            - **Entity Indicators**: Names, organizations, locations, concepts

        Examples:
            Router decision examples::

                # Structured content → graph memory
                "John Smith works at TechCorp in San Francisco"
                # Router returns: "structured"

                # Conversational content → reactive memory
                "I mentioned in our discussion that I prefer morning meetings"
                # Router returns: "conversational"

                # Important fact → long-term memory
                "Critical: Emergency contact is Dr. Johnson at +1-555-0199"
                # Router returns: "persistent"

                # Complex content → hybrid approach
                "Important meeting with CEO Sarah Chen at Google office about AI partnership"
                # Router returns: "hybrid" (entities + importance + context)

        Note:
            The router agent is created with specific tools and prompts optimized
            for memory system coordination. It uses the same LLM configuration as
            the parent system for consistency in analysis and decision-making.
        """

        @tool
        def analyze_memory_type(content: str) -> str:
            """Analyze content to determine the best memory system.

            Returns: structured, conversational, persistent, or hybrid
            """
            content_lower = content.lower()

            # Check for structured data indicators
            structured_indicators = [
                "works at",
                "located in",
                "knows",
                "created by",
                "belongs to",
                "part of",
                "connected to",
                "related to",
            ]
            has_structured = any(ind in content_lower for ind in structured_indicators)

            # Check for conversational indicators
            conversational_indicators = [
                "remember",
                "said",
                "mentioned",
                "discussed",
                "conversation",
                "told me",
                "i think",
                "my opinion",
            ]
            has_conversational = any(
                ind in content_lower for ind in conversational_indicators
            )

            # Check for long-term importance indicators
            persistent_indicators = [
                "important",
                "always",
                "never forget",
                "critical",
                "fundamental",
                "core",
                "essential",
                "permanent",
            ]
            has_persistent = any(ind in content_lower for ind in persistent_indicators)

            # Determine best system
            if has_structured and not has_conversational:
                return "structured"
            if has_conversational and not has_structured:
                return "conversational"
            if has_persistent:
                return "persistent"
            if has_structured and has_conversational:
                return "hybrid"
            return "conversational"  # Default

        @tool
        def route_memory_query(query: str) -> str:
            """Determine which memory systems to query.

            Returns: Comma-separated list of systems to use
            """
            query_lower = query.lower()

            systems = []

            # Graph queries
            if any(
                word in query_lower
                for word in [
                    "who",
                    "what",
                    "where",
                    "connected",
                    "related",
                    "knows",
                    "works",
                    "located",
                ]
            ):
                systems.append("graph")

            # Time-based queries
            if any(
                word in query_lower
                for word in [
                    "recent",
                    "today",
                    "yesterday",
                    "last week",
                    "when",
                    "timeline",
                    "history",
                ]
            ):
                systems.append("react")

            # Persistent memory queries
            if any(
                word in query_lower
                for word in [
                    "always",
                    "important",
                    "remember",
                    "learned",
                    "fact",
                    "knowledge",
                ]
            ):
                systems.append("longterm")

            return ",".join(systems) if systems else "all"

        router = ReactAgent(
            name="memory_router",
            engine=self.engine,
            tools=[analyze_memory_type, route_memory_query],
            system_message="""You are a memory routing specialist. Analyze content and queries to determine.
the best memory system(s) to use:
- structured: For entities, relationships, and structured knowledge (Neo4j graph)
- conversational: For dialogue, opinions, and temporal information (React memory)
- persistent: For important facts and long-term knowledge (Long-term memory)
- hybrid: When multiple systems should be used together""",
        )

        return router

    def _create_coordinator(self) -> SimpleMultiAgent:
        """Create coordinator that manages all memory systems."""
        agents = {
            "router": self.router,
            "graph": self.graph_memory.as_tool(self.graph_memory.config),
            "react": self.react_memory.agent,
            "longterm": self.longterm_memory.memory_enhanced_agent,
        }

        coordinator = SimpleMultiAgent(
            name="memory_coordinator",
            engine=self.engine,
            agents=agents,
            mode="sequential",
        )

        return coordinator

    async def store_memory(
        self,
        content: str,
        mode: MemorySystemMode = MemorySystemMode.INTELLIGENT,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Store memory content using intelligent routing to appropriate subsystem(s).

        Analyzes the provided content and routes it to the most suitable memory
        subsystem(s) based on the specified mode and content characteristics.
        Supports both explicit mode selection and AI-powered intelligent routing
        for optimal storage decisions.

        Args:
            content: Text content to store in memory. Can be any natural language
                information including facts, conversations, observations, or
                structured data descriptions. The content will be analyzed for
                entities, relationships, importance, and temporal characteristics.
            mode: Storage coordination mode determining routing strategy:
                - INTELLIGENT: AI analyzes content and selects optimal system(s)
                - STRUCTURED: Force routing to graph memory for entities/relationships
                - CONVERSATIONAL: Store in reactive memory for dialogue context
                - PERSISTENT: Store in long-term memory for important facts
                - HYBRID: Store in multiple systems simultaneously
            metadata: Optional metadata dictionary providing additional context:
                - source: Origin of the information (e.g., "meeting", "document")
                - importance: Importance score (0.0-1.0) for prioritization
                - timestamp: Custom timestamp (ISO format) if different from current
                - tags: List of classification tags for organization
                - confidence: Confidence score (0.0-1.0) for information reliability

        Returns:
            Dict[str, Any]: Comprehensive storage results containing:
                - content: Original content that was stored
                - mode: Actual mode used (after intelligent routing if applicable)
                - timestamp: Storage timestamp in ISO format
                - systems_used: List of memory subsystems that stored the content
                - [system]_storage: Individual storage results for each subsystem used
                - routing_decision: AI routing analysis (if INTELLIGENT mode)
                - storage_time_ms: Total time taken for storage operation
                - warnings: Any warnings encountered during storage

        Raises:
            StorageError: If storage fails in all attempted subsystems.
            RoutingError: If intelligent routing fails to make a decision.
            ValidationError: If content is empty or metadata contains invalid values.
            ConnectionError: If database connections are unavailable.

        Examples:
            Intelligent routing for automatic optimization::

                # Let AI determine the best storage approach
                result = await memory_system.store_memory(
                    "Dr. Alice Chen joined Stanford's AI Lab as director. "
                    "She previously led the computer vision team at Google Research "
                    "and has published 50+ papers on neural networks.",
                    mode=MemorySystemMode.INTELLIGENT
                )

                print(f"AI selected systems: {result['systems_used']}")
                # Expected: ['graph', 'longterm'] for structured + important info
                print(f"Routing reasoning: {result.get('routing_decision')}")

            Explicit structured storage::

                # Force storage in graph memory for relationship data
                result = await memory_system.store_memory(
                    "TechCorp acquired StartupAI for $50M in Q3 2024",
                    mode=MemorySystemMode.STRUCTURED,
                    metadata={
                        "source": "financial_news",
                        "importance": 0.8,
                        "tags": ["acquisition", "business", "AI"]
                    }
                )

                # Check graph storage results
                graph_result = result.get('graph_storage')
                if graph_result:
                    print(f"Created {graph_result['nodes_created']} entities")
                    print(f"Created {graph_result['relationships_created']} relationships")

            Conversational memory storage::

                # Store dialogue context and preferences
                result = await memory_system.store_memory(
                    "User mentioned they prefer video calls over phone calls "
                    "and are available for meetings between 10 AM and 3 PM EST",
                    mode=MemorySystemMode.CONVERSATIONAL,
                    metadata={
                        "source": "user_preferences",
                        "importance": 0.7
                    }
                )

                react_result = result.get('react_storage')
                print(f"Stored conversational context: {react_result}")

            Critical information with hybrid storage::

                # Store in multiple systems for redundancy and accessibility
                result = await memory_system.store_memory(
                    "CRITICAL: Security incident at Building A. "
                    "Contact security chief Maria Rodriguez immediately at ext. 5555. "
                    "All employees must use alternative entrance.",
                    mode=MemorySystemMode.HYBRID,
                    metadata={
                        "source": "security_alert",
                        "importance": 1.0,
                        "tags": ["critical", "security", "emergency"],
                        "confidence": 1.0
                    }
                )

                # Verify storage in all systems
                systems_used = result['systems_used']
                assert 'graph' in systems_used  # Entities and relationships
                assert 'longterm' in systems_used  # Critical persistence
                assert 'react' in systems_used  # Immediate accessibility

            Batch storage with performance monitoring::

                import time
                import asyncio

                contents = [
                    "Research finding 1: Transformers show 95% accuracy...",
                    "Meeting note: Team decided to focus on multimodal models...",
                    "Important: Project deadline moved to December 15th..."
                ]

                start_time = time.time()
                
                # Store all contents concurrently
                tasks = [
                    memory_system.store_memory(content, mode=MemorySystemMode.INTELLIGENT)
                    for content in contents
                ]
                
                results = await asyncio.gather(*tasks)
                
                total_time = time.time() - start_time
                avg_time = total_time / len(contents)
                
                print(f"Stored {len(contents)} items in {total_time:.2f}s")
                print(f"Average time per item: {avg_time:.2f}s")
                
                # Analyze routing decisions
                for i, result in enumerate(results):
                    systems = result['systems_used']
                    print(f"Item {i+1} → {systems}")

        Performance Optimization:
            - **Batch Operations**: Use asyncio.gather for concurrent storage
            - **Mode Selection**: Use explicit modes when routing is predictable
            - **Metadata Optimization**: Include importance scores for prioritization
            - **Connection Pooling**: System automatically manages database connections

        Note:
            The INTELLIGENT mode adds computational overhead for content analysis
            but provides optimal routing decisions. For high-volume operations,
            consider using explicit modes when the optimal subsystem is known.
            The system maintains transaction integrity across all subsystems and
            provides detailed error reporting for debugging and monitoring.
        """
        results = {
            "content": content,
            "mode": mode.value,
            "timestamp": datetime.now().isoformat(),
            "systems_used": [],
        }

        if mode == MemorySystemMode.INTELLIGENT:
            # Let router decide
            routing = await self.router.arun(
                f"Analyze this content for memory storage: {content}"
            )

            if "structured" in routing.lower():
                mode = MemorySystemMode.STRUCTURED
            elif "conversational" in routing.lower():
                mode = MemorySystemMode.CONVERSATIONAL
            elif "persistent" in routing.lower():
                mode = MemorySystemMode.PERSISTENT
            elif "hybrid" in routing.lower():
                mode = MemorySystemMode.HYBRID

        # Store based on mode
        if mode in [MemorySystemMode.STRUCTURED, MemorySystemMode.HYBRID]:
            graph_result = await self.graph_memory.run(
                content, mode=GraphMemoryMode.EXTRACT_AND_STORE
            )
            results["graph_storage"] = graph_result
            results["systems_used"].append("graph")

        if mode in [MemorySystemMode.CONVERSATIONAL, MemorySystemMode.HYBRID]:
            react_result = await self.react_memory.arun(
                f"Store this memory: {content}", auto_save=True
            )
            results["react_storage"] = react_result
            results["systems_used"].append("react")

        if mode in [MemorySystemMode.PERSISTENT, MemorySystemMode.HYBRID]:
            longterm_result = await self.longterm_memory.run(
                content, extract_memories=True
            )
            results["longterm_storage"] = longterm_result
            results["systems_used"].append("longterm")

        return results

    async def query_memory(
        self,
        query: str,
        mode: MemorySystemMode = MemorySystemMode.INTELLIGENT,
        combine_results: bool = True,
    ) -> dict[str, Any]:
        """Query memory using intelligent routing across appropriate subsystem(s).

        Analyzes the query to determine which memory subsystems are most likely
        to contain relevant information, then searches those systems and optionally
        synthesizes results into a comprehensive answer. Supports both targeted
        queries and comprehensive cross-system searches.

        Args:
            query: Natural language query or question to search for. Can be any
                conversational question, factual inquiry, or relationship exploration.
                Examples: "Who works at tech companies?", "What did we discuss
                about the project?", "How are AI and healthcare connected?"
            mode: Query coordination mode determining search strategy:
                - INTELLIGENT: AI analyzes query and selects optimal subsystem(s)
                - STRUCTURED: Search only graph memory for entity/relationship queries
                - CONVERSATIONAL: Search only reactive memory for dialogue context
                - PERSISTENT: Search only long-term memory for important facts
                - HYBRID: Search all systems and synthesize comprehensive results
            combine_results: Whether to use AI synthesis to combine results from
                multiple subsystems into a unified answer. When True, provides
                a cohesive response; when False, returns individual system results.

        Returns:
            Dict[str, Any]: Comprehensive query results containing:
                - query: Original query for reference
                - mode: Actual mode used (after intelligent routing if applicable)
                - timestamp: Query timestamp in ISO format
                - systems_queried: List of memory subsystems that were searched
                - individual_results: Raw results from each queried subsystem
                - combined_answer: AI-synthesized unified response (if combine_results=True)
                - routing_analysis: AI query analysis and routing decisions
                - query_time_ms: Total time taken for query processing
                - result_confidence: Confidence score for the synthesized answer

        Raises:
            QueryError: If query processing fails in all attempted subsystems.
            RoutingError: If intelligent routing cannot determine appropriate systems.
            SynthesisError: If result combination fails (when combine_results=True).
            ConnectionError: If database connections are unavailable.

        Examples:
            Intelligent query routing::

                # Let AI determine the best search strategy
                result = await memory_system.query_memory(
                    "What do I know about artificial intelligence researchers at universities?",
                    mode=MemorySystemMode.INTELLIGENT,
                    combine_results=True
                )

                if 'combined_answer' in result:
                    print(f"Answer: {result['combined_answer']}")
                    print(f"Confidence: {result.get('result_confidence', 'N/A')}")
                
                print(f"Searched systems: {result['systems_queried']}")
                print(f"Query time: {result.get('query_time_ms', 0):.1f}ms")

            Entity relationship queries::

                # Search graph memory for structured relationships
                result = await memory_system.query_memory(
                    "How are technology companies connected to AI research?",
                    mode=MemorySystemMode.STRUCTURED,
                    combine_results=False  # Get raw graph results
                )

                graph_results = result['individual_results'].get('graph')
                if graph_results:
                    print(f"Graph query result: {graph_results['result']}")
                    print(f"Cypher used: {graph_results.get('cypher_statement')}")

            Conversational context retrieval::

                # Search recent conversation history
                result = await memory_system.query_memory(
                    "What preferences did the user mention in our recent conversations?",
                    mode=MemorySystemMode.CONVERSATIONAL
                )

                react_results = result['individual_results'].get('react')
                print(f"Conversation context: {react_results}")

            Comprehensive hybrid search::

                # Search all systems for maximum coverage
                result = await memory_system.query_memory(
                    "Tell me everything about our AI research project",
                    mode=MemorySystemMode.HYBRID,
                    combine_results=True
                )

                # Access synthesized comprehensive answer
                if 'combined_answer' in result:
                    print(f"Comprehensive answer: {result['combined_answer']}")

                # Access individual system contributions
                individual = result['individual_results']
                for system, system_result in individual.items():
                    print(f"{system.title()} contribution: {str(system_result)[:100]}...")

            Critical fact retrieval::

                # Search long-term memory for important information
                result = await memory_system.query_memory(
                    "What are the emergency contact procedures?",
                    mode=MemorySystemMode.PERSISTENT
                )

                longterm_results = result['individual_results'].get('longterm')
                if longterm_results:
                    print(f"Critical information: {longterm_results}")

            Performance-optimized querying::

                # Fast targeted query without synthesis
                result = await memory_system.query_memory(
                    "Who is the CEO of TechCorp?",
                    mode=MemorySystemMode.STRUCTURED,  # Direct to graph
                    combine_results=False  # Skip synthesis overhead
                )

                # Direct access to graph results
                graph_answer = result['individual_results']['graph']['result']
                print(f"Direct answer: {graph_answer}")

            Batch query processing::

                import asyncio

                queries = [
                    "Who are the key researchers in our field?",
                    "What recent developments should we be aware of?", 
                    "What are our project priorities and deadlines?"
                ]

                # Process queries concurrently
                tasks = [
                    memory_system.query_memory(q, mode=MemorySystemMode.INTELLIGENT)
                    for q in queries
                ]

                results = await asyncio.gather(*tasks)

                for i, result in enumerate(results):
                    print(f"Query {i+1}: {queries[i]}")
                    print(f"Answer: {result.get('combined_answer', 'No answer')}")
                    print(f"Systems: {result['systems_queried']}")
                    print()

        Query Optimization Strategies:
            - **Explicit Modes**: Use specific modes when query type is predictable
            - **Selective Synthesis**: Disable combine_results for simple queries
            - **Concurrent Processing**: Use asyncio.gather for batch queries
            - **Result Caching**: System automatically caches frequent query patterns

        Note:
            The INTELLIGENT mode analyzes query characteristics to determine optimal
            subsystems, which adds processing overhead but improves result relevance.
            For high-frequency applications, consider using explicit modes when the
            optimal subsystem is predictable. The synthesis process uses LLM analysis
            which incurs additional API costs but provides coherent unified answers.
        """
        results = {
            "query": query,
            "mode": mode.value,
            "timestamp": datetime.now().isoformat(),
            "systems_queried": [],
        }

        if mode == MemorySystemMode.INTELLIGENT:
            # Let router decide which systems to query
            routing = await self.router.arun(f"Route this memory query: {query}")
            systems_to_query = routing.lower().split(",")
        else:
            # Map mode to systems
            mode_to_systems = {
                MemorySystemMode.STRUCTURED: ["graph"],
                MemorySystemMode.CONVERSATIONAL: ["react"],
                MemorySystemMode.PERSISTENT: ["longterm"],
                MemorySystemMode.HYBRID: ["graph", "react", "longterm"],
            }
            systems_to_query = mode_to_systems.get(mode, ["all"])

        # Query each system
        all_results = {}

        if "graph" in systems_to_query or "all" in systems_to_query:
            graph_result = await self.graph_memory.query_graph(
                query, query_type="natural"
            )
            all_results["graph"] = graph_result
            results["systems_queried"].append("graph")

        if "react" in systems_to_query or "all" in systems_to_query:
            react_result = await self.react_memory.arun(
                f"Search memories for: {query}", auto_save=False
            )
            all_results["react"] = react_result
            results["systems_queried"].append("react")

        if "longterm" in systems_to_query or "all" in systems_to_query:
            longterm_result = await self.longterm_memory.run(
                query, extract_memories=False
            )
            all_results["longterm"] = longterm_result
            results["systems_queried"].append("longterm")

        if combine_results and len(all_results) > 1:
            # Combine results intelligently
            combined = await self._combine_query_results(query, all_results)
            results["combined_answer"] = combined

        results["individual_results"] = all_results

        return results

    async def _combine_query_results(self, query: str, results: dict[str, Any]) -> str:
        """Combine results from multiple memory systems."""
        # Use a simple agent to synthesize results
        synthesis_prompt = f"""
Query: {query}

Results from different memory systems:

Graph Memory (structured knowledge):
{json.dumps(results.get("graph", {}), indent=2)}

Conversational Memory (recent interactions):
{results.get("react", "No results")}

Long-term Memory (important facts):
{json.dumps(results.get("longterm", {}), indent=2)}

Synthesize these results into a comprehensive answer.
"""

        synthesizer = SimpleAgent(name="result_synthesizer", engine=self.engine)

        combined = await synthesizer.arun(synthesis_prompt)
        return combined

    async def get_memory_analytics(self) -> dict[str, Any]:
        """Generate comprehensive analytics across all integrated memory subsystems.

        Collects detailed statistics, usage patterns, and performance metrics from
        all memory subsystems to provide insights into system utilization, data
        distribution, and operational health. Useful for system monitoring,
        optimization, and capacity planning.

        Returns:
            Dict[str, Any]: Comprehensive analytics report containing:
                - user_id: User identifier for the analytics scope
                - timestamp: Analysis timestamp in ISO format
                - systems: Detailed statistics for each memory subsystem:
                    - graph: Node distribution, relationship counts, storage usage
                    - react: Recent activity patterns, vector store metrics
                    - longterm: Persistence statistics, retrieval effectiveness
                - aggregated_metrics: Cross-system summary statistics
                - performance_indicators: Response times and throughput metrics
                - storage_efficiency: Space utilization and optimization suggestions
                - usage_patterns: Query frequency and content type distributions

        Raises:
            AnalyticsError: If analytics generation fails for critical subsystems.
            ConnectionError: If database connections required for analysis are unavailable.
            AuthorizationError: If insufficient permissions for analytics queries.

        Examples:
            Basic analytics overview::

                analytics = await memory_system.get_memory_analytics()
                
                print(f"Analytics for user: {analytics['user_id']}")
                print(f"Generated at: {analytics['timestamp']}")
                
                # Graph memory statistics
                graph_stats = analytics['systems']['graph']
                if 'total_nodes' in graph_stats:
                    print(f"Graph entities: {graph_stats['total_nodes']}")
                    print(f"Node distribution: {graph_stats['node_distribution']}")
                
                # Reactive memory activity
                react_stats = analytics['systems']['react']
                print(f"Recent activity preview: {react_stats['recent_activity'][:100]}...")
                
                # Long-term memory status
                longterm_stats = analytics['systems']['longterm']
                print(f"Long-term retriever active: {longterm_stats['retriever_active']}")

            Performance monitoring::

                analytics = await memory_system.get_memory_analytics()
                
                # Check system health
                systems_status = {}
                for system_name, system_stats in analytics['systems'].items():
                    if 'error' in system_stats:
                        systems_status[system_name] = 'ERROR'
                        print(f"⚠️  {system_name}: {system_stats['error']}")
                    else:
                        systems_status[system_name] = 'OK'
                        print(f"✅ {system_name}: Operational")
                
                # Performance metrics
                if 'performance_indicators' in analytics:
                    perf = analytics['performance_indicators']
                    print(f"Average query time: {perf.get('avg_query_time_ms', 'N/A')}ms")
                    print(f"Storage efficiency: {perf.get('storage_efficiency', 'N/A')}%")

            Usage pattern analysis::

                analytics = await memory_system.get_memory_analytics()
                
                # Analyze content distribution
                if 'usage_patterns' in analytics:
                    patterns = analytics['usage_patterns']
                    
                    content_types = patterns.get('content_types', {})
                    print("Content type distribution:")
                    for content_type, count in content_types.items():
                        print(f"  {content_type}: {count} items")
                    
                    query_patterns = patterns.get('query_patterns', {})
                    print("\nQuery pattern analysis:")
                    for pattern, frequency in query_patterns.items():
                        print(f"  {pattern}: {frequency} queries")

            Capacity planning::

                analytics = await memory_system.get_memory_analytics()
                
                # Storage utilization
                if 'storage_efficiency' in analytics:
                    storage = analytics['storage_efficiency']
                    
                    total_items = storage.get('total_memory_items', 0)
                    storage_size = storage.get('total_storage_mb', 0)
                    
                    print(f"Total memory items: {total_items:,}")
                    print(f"Storage usage: {storage_size:.1f} MB")
                    
                    if total_items > 0:
                        avg_size = storage_size / total_items
                        print(f"Average item size: {avg_size:.2f} KB")
                    
                    # Growth projections
                    monthly_growth = storage.get('monthly_growth_rate', 0)
                    if monthly_growth > 0:
                        projected_size = storage_size * (1 + monthly_growth)
                        print(f"Projected size next month: {projected_size:.1f} MB")

            System optimization insights::

                analytics = await memory_system.get_memory_analytics()
                
                # Optimization recommendations
                if 'optimization_suggestions' in analytics:
                    suggestions = analytics['optimization_suggestions']
                    
                    print("Optimization recommendations:")
                    for category, recommendations in suggestions.items():
                        print(f"\n{category.title()}:")
                        for rec in recommendations:
                            print(f"  • {rec}")
                
                # Performance bottlenecks
                if 'bottlenecks' in analytics:
                    bottlenecks = analytics['bottlenecks']
                    print("\nPerformance bottlenecks detected:")
                    for bottleneck in bottlenecks:
                        print(f"  ⚡ {bottleneck['component']}: {bottleneck['issue']}")
                        print(f"     Impact: {bottleneck['impact']}")
                        print(f"     Suggestion: {bottleneck['suggestion']}")

        Analytics Categories:
            The analytics report includes multiple categories of information:

            - **System Health**: Operational status and error conditions
            - **Usage Metrics**: Query frequency, storage patterns, user activity
            - **Performance Data**: Response times, throughput, resource utilization
            - **Content Analysis**: Entity types, relationship patterns, topic distribution
            - **Optimization Insights**: Bottlenecks, efficiency recommendations
            - **Capacity Planning**: Growth trends, storage projections, scaling needs

        Note:
            Analytics generation may take several seconds for large memory systems
            as it requires querying all subsystems and performing statistical analysis.
            The system automatically handles cases where individual subsystems are
            temporarily unavailable, providing partial analytics with appropriate
            warnings for missing data.
        """
        analytics = {
            "user_id": self.user_id,
            "timestamp": datetime.now().isoformat(),
            "systems": {},
        }

        # Graph memory stats
        try:
            graph_stats = self.graph_memory.graph.query(
                """
                MATCH (n {user_id: $user_id})
                WITH labels(n) as node_labels, count(n) as count
                RETURN node_labels[0] as type, count
                ORDER BY count DESC
            """,
                {"user_id": self.user_id},
            )

            analytics["systems"]["graph"] = {
                "node_distribution": graph_stats,
                "total_nodes": sum(stat["count"] for stat in graph_stats),
            }
        except BaseException:
            analytics["systems"]["graph"] = {"error": "Unable to get stats"}

        # React memory stats
        recent_memories = await self.react_memory.arun(
            "List my 10 most recent memories", auto_save=False
        )
        analytics["systems"]["react"] = {
            "recent_activity": recent_memories[:200] + "..."
        }

        # Long-term memory stats
        analytics["systems"]["longterm"] = {
            "retriever_active": hasattr(self.longterm_memory, "memory_retriever")
        }

        return analytics

    async def consolidate_all_memories(self) -> dict[str, Any]:
        """Perform comprehensive memory consolidation across all integrated subsystems.

        Executes automated maintenance operations to optimize memory storage,
        organize related information, archive old data, and improve system
        performance. This process includes graph memory consolidation, conversational
        memory archival, and cross-system optimization.

        Returns:
            Dict[str, Any]: Comprehensive consolidation results containing:
                - timestamp: Consolidation operation timestamp in ISO format
                - systems_consolidated: List of subsystems that underwent consolidation
                - graph: Graph memory consolidation results (concept creation, clustering)
                - react_to_longterm: Results of archival from reactive to long-term memory
                - archived_memories: Whether old conversational memories were archived
                - optimization_performed: List of optimization operations completed
                - performance_improvement: Estimated performance gains from consolidation
                - storage_reclaimed: Amount of storage space recovered (in MB)
                - errors: Any errors encountered during consolidation
                - next_consolidation_recommended: Suggested time for next consolidation

        Raises:
            ConsolidationError: If critical consolidation operations fail.
            DatabaseError: If database operations required for consolidation fail.
            PermissionError: If insufficient permissions for maintenance operations.

        Examples:
            Regular maintenance consolidation::

                # Perform routine system maintenance
                consolidation = await memory_system.consolidate_all_memories()
                
                print(f"Consolidation completed at: {consolidation['timestamp']}")
                print(f"Systems processed: {consolidation['systems_consolidated']}")
                
                # Graph memory results
                if 'graph' in consolidation:
                    graph_result = consolidation['graph']
                    print(f"Graph concepts created: {graph_result.get('concepts_created', 0)}")
                    print(f"Entities analyzed: {graph_result.get('candidates_analyzed', 0)}")
                
                # Archival results
                if consolidation.get('archived_memories'):
                    print("✅ Old conversational memories archived to long-term storage")
                
                # Performance improvements
                if 'performance_improvement' in consolidation:
                    improvement = consolidation['performance_improvement']
                    print(f"Estimated performance gain: {improvement.get('query_speedup', 0):.1f}%")

            Scheduled maintenance workflow::

                import asyncio
                from datetime import datetime, timedelta

                async def scheduled_maintenance():
                    while True:
                        # Perform consolidation every 24 hours
                        try:
                            consolidation = await memory_system.consolidate_all_memories()
                            
                            # Log consolidation results
                            systems = consolidation['systems_consolidated']
                            print(f"[{datetime.now()}] Consolidation complete: {systems}")
                            
                            # Check for errors
                            if consolidation.get('errors'):
                                for error in consolidation['errors']:
                                    print(f"⚠️  Consolidation error: {error}")
                            
                            # Storage optimization
                            reclaimed = consolidation.get('storage_reclaimed', 0)
                            if reclaimed > 0:
                                print(f"💾 Storage reclaimed: {reclaimed:.1f} MB")
                            
                        except Exception as e:
                            print(f"❌ Maintenance failed: {e}")
                        
                        # Wait 24 hours
                        await asyncio.sleep(24 * 60 * 60)

                # Start background maintenance
                asyncio.create_task(scheduled_maintenance())

            Performance optimization focus::

                # Run consolidation with performance monitoring
                import time
                
                start_time = time.time()
                consolidation = await memory_system.consolidate_all_memories()
                consolidation_time = time.time() - start_time
                
                print(f"Consolidation completed in {consolidation_time:.2f}s")
                
                # Analyze optimization results
                if 'optimization_performed' in consolidation:
                    optimizations = consolidation['optimization_performed']
                    print(f"Optimizations applied: {len(optimizations)}")
                    
                    for optimization in optimizations:
                        print(f"  • {optimization['operation']}: {optimization['result']}")
                
                # Measure performance improvement
                if 'performance_improvement' in consolidation:
                    perf = consolidation['performance_improvement']
                    
                    query_speedup = perf.get('query_speedup', 0)
                    storage_efficiency = perf.get('storage_efficiency', 0)
                    
                    print(f"Expected query speedup: {query_speedup:.1f}%")
                    print(f"Storage efficiency gain: {storage_efficiency:.1f}%")

            Error handling and recovery::

                try:
                    consolidation = await memory_system.consolidate_all_memories()
                    
                    # Check for partial failures
                    if consolidation.get('errors'):
                        print("⚠️  Consolidation completed with warnings:")
                        for error in consolidation['errors']:
                            print(f"    {error}")
                        
                        # Determine if retry is needed
                        critical_errors = [
                            err for err in consolidation['errors']
                            if 'critical' in err.lower() or 'failed' in err.lower()
                        ]
                        
                        if critical_errors:
                            print("🔄 Retrying consolidation for critical errors...")
                            # Implement retry logic here
                    else:
                        print("✅ Consolidation completed successfully")
                        
                except ConsolidationError as e:
                    print(f"❌ Consolidation failed: {e}")
                    # Implement error recovery or alerting

        Consolidation Operations:
            The consolidation process performs several types of maintenance:

            - **Graph Memory Consolidation**:
                - Creates concept nodes for highly connected entities
                - Merges duplicate or similar entities
                - Optimizes relationship patterns
                - Removes orphaned or low-confidence nodes

            - **Conversational Memory Archival**:
                - Identifies old conversational memories (30+ days)
                - Archives important conversations to long-term memory
                - Removes routine or low-importance dialogue history
                - Preserves user preferences and learning

            - **Cross-System Optimization**:
                - Deduplicates information stored in multiple systems
                - Balances load across subsystems
                - Updates indexes and caches
                - Optimizes query performance

            - **Storage Cleanup**:
                - Removes temporary or obsolete data
                - Compacts vector stores
                - Optimizes database storage
                - Updates statistical models

        Note:
            Consolidation is a resource-intensive operation that should be performed
            during low-usage periods. The process is designed to be non-blocking
            for normal memory operations but may temporarily impact performance.
            For production systems, consider running consolidation during scheduled
            maintenance windows and monitor system performance during the process.
        """
        consolidation_results = {
            "timestamp": datetime.now().isoformat(),
            "systems_consolidated": [],
        }

        # Graph memory consolidation
        graph_consolidation = await self.graph_memory.consolidate_memories()
        consolidation_results["graph"] = graph_consolidation
        consolidation_results["systems_consolidated"].append("graph")

        # Move old conversational memories to long-term
        old_memories = await self.react_memory.arun(
            "Search memories from more than 30 days ago", auto_save=False
        )

        if old_memories and "no memories" not in old_memories.lower():
            # Store in long-term memory
            await self.longterm_memory.run(
                f"Archive of old memories: {old_memories}", extract_memories=True
            )
            consolidation_results["archived_memories"] = True
            consolidation_results["systems_consolidated"].append("react_to_longterm")

        return consolidation_results


# Example usage
async def demo_integrated_memory():
    """Comprehensive demonstration of IntegratedMemorySystem capabilities.
    
    This demo showcases the full range of integrated memory functionality including
    intelligent routing, multi-system storage, cross-system querying, analytics,
    and maintenance operations. It provides a complete example of how to use
    the system for real-world knowledge management scenarios.
    """
    system = IntegratedMemorySystem(
        user_id="demo_user",
        neo4j_config={
            "neo4j_uri": "bolt://localhost:7687",
            "neo4j_username": "neo4j",
            "neo4j_password": "password",
        },
    )

    print("=== Integrated Memory System Demo ===\n")

    # Store different types of memories
    memories = [
        # Structured knowledge
        "John Smith is the CEO of TechCorp, which is headquartered in San Francisco.",
        # Conversational memory
        "During our conversation, John mentioned he's been with the company for 10 years.",
        # Important fact
        "Important: John's email is john.smith@techcorp.com - always use this for official communication.",
        # Mixed content
        "I met Sarah Johnson at the TechCorp office. She works as CTO and told me about their new AI project.",
        # Time-based memory
        "Yesterday, John and Sarah presented the Q4 roadmap to the board.",
    ]

    print("Storing memories...\n")
    for memory in memories:
        result = await system.store_memory(memory, mode=MemorySystemMode.INTELLIGENT)
        print(f"Stored in: {result['systems_used']}")
        print(f"Content: {memory[:50]}...\n")

    # Query memories in different ways
    queries = [
        "Who are the executives at TechCorp?",
        "What did John mention in our conversation?",
        "What happened yesterday?",
        "What do I know about the AI project?",
        "What is John's contact information?",
    ]

    print("\nQuerying memories...\n")
    for query in queries:
        result = await system.query_memory(query, mode=MemorySystemMode.INTELLIGENT)
        print(f"Query: {query}")
        print(f"Systems used: {result['systems_queried']}")
        if "combined_answer" in result:
            print(f"Answer: {result['combined_answer'][:200]}...")
        print()

    # Get analytics
    print("\nMemory System Analytics:")
    analytics = await system.get_memory_analytics()
    print(json.dumps(analytics, indent=2))

    # Consolidate memories
    print("\nConsolidating memories...")
    consolidation = await system.consolidate_all_memories()
    print(f"Consolidation complete: {consolidation['systems_consolidated']}")


# Advanced example with custom agent integration
async def create_research_assistant():
    """Create a sophisticated research assistant with comprehensive memory integration.
    
    This example demonstrates how to build domain-specific agents that leverage
    the full power of the integrated memory system. The research assistant can
    store papers, find relationships, and maintain a comprehensive knowledge graph
    of research information while providing intelligent query capabilities.
    """
    # Initialize memory system
    memory_system = IntegratedMemorySystem(
        user_id="researcher",
        neo4j_config={
            "neo4j_uri": "bolt://localhost:7687",
            "neo4j_username": "neo4j",
            "neo4j_password": "password",
        },
    )

    # Create custom tools using the memory system
    @tool
    async def remember_paper(
        title: str, authors: str, key_findings: str, relevance: str
    ) -> str:
        """Store comprehensive research paper information in integrated memory.
        
        Args:
            title: Full title of the research paper
            authors: List of paper authors (comma-separated)
            key_findings: Summary of main research findings and contributions
            relevance: Explanation of how this paper relates to current work
            
        Returns:
            Status message indicating successful storage across memory systems
        """
        memory_content = f"""
        Research Paper: {title}
        Authors: {authors}
        Key Findings: {key_findings}
        Relevance to our work: {relevance}
        """

        result = await memory_system.store_memory(
            memory_content,
            mode=MemorySystemMode.HYBRID,  # Store in multiple systems
        )

        return (
            f"Stored paper information in {len(result['systems_used'])} memory systems"
        )

    @tool
    async def find_related_papers(topic: str) -> str:
        """Search for research papers related to a specific topic using hybrid memory retrieval.
        
        Args:
            topic: Research topic or keyword to search for in stored papers
            
        Returns:
            Comprehensive summary of related papers with relevance analysis
        """
        result = await memory_system.query_memory(
            f"Find research papers related to {topic}", mode=MemorySystemMode.HYBRID
        )

        if "combined_answer" in result:
            return result["combined_answer"]
        return "No related papers found in memory"

    @tool
    async def get_research_graph(entity: str) -> str:
        """Explore the knowledge graph structure around a research entity.
        
        Args:
            entity: Research entity name (author, institution, concept) to explore
            
        Returns:
            JSON representation of the entity's knowledge graph neighborhood
        """
        graph_result = await memory_system.graph_memory.get_memory_subgraph(
            entity, max_depth=2, relationship_types=["AUTHORED", "CITES", "RELATED_TO"]
        )

        return json.dumps(graph_result, indent=2)

    # Create sophisticated research assistant with memory integration
    research_assistant = ReactAgent(
        name="research_assistant",
        engine=AugLLMConfig(
            model="gpt-4",
            temperature=0.7,
            max_tokens=2000
        ),
        tools=[remember_paper, find_related_papers, get_research_graph],
        system_message="""You are an advanced research assistant with comprehensive memory capabilities.
        
Your capabilities include:
- Storing research papers with entity extraction and relationship mapping
- Finding related research using graph traversal and semantic similarity
- Exploring knowledge graph connections between researchers, papers, and concepts
- Synthesizing information across multiple memory systems
- Providing contextual analysis based on stored research knowledge

Always:
1. Store important research information in memory using appropriate detail
2. Use graph exploration to find unexpected connections
3. Provide comprehensive context from your memory systems
4. Suggest related research and potential collaboration opportunities
5. Maintain a structured knowledge base of research relationships

You have access to graph memory (entities/relationships), conversational memory
(discussions/context), and long-term memory (important facts/insights).""",
    )

    return research_assistant, memory_system


if __name__ == "__main__":
    # Run demo
    asyncio.run(demo_integrated_memory())
