agents.memory_reorganized.knowledge.kg_generator_agent
======================================================

.. py:module:: agents.memory_reorganized.knowledge.kg_generator_agent

.. autoapi-nested-parse::

   Knowledge Graph Generator Agent for Memory System.

   This agent specializes in extracting and maintaining knowledge graphs from memories,
   building entity relationships and semantic connections across the memory system.


   .. autolink-examples:: agents.memory_reorganized.knowledge.kg_generator_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.knowledge.kg_generator_agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.knowledge.kg_generator_agent.KGGeneratorAgent
   agents.memory_reorganized.knowledge.kg_generator_agent.KGGeneratorAgentConfig
   agents.memory_reorganized.knowledge.kg_generator_agent.KnowledgeGraphNode
   agents.memory_reorganized.knowledge.kg_generator_agent.KnowledgeGraphRelationship
   agents.memory_reorganized.knowledge.kg_generator_agent.MemoryKnowledgeGraph


Module Contents
---------------

.. py:class:: KGGeneratorAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent specializing in knowledge graph generation from memory system.

   The KGGeneratorAgent is a specialized memory agent that extracts entities and relationships
   from memory content to build comprehensive knowledge graphs. It uses LLM-powered extraction
   to identify semantic structures and connections across memories.

   This agent extends SimpleAgent with knowledge graph capabilities, providing methods for:
   - Entity extraction with confidence scoring
   - Relationship discovery between entities
   - Incremental graph building and updates
   - Entity neighborhood exploration
   - Graph-based memory analysis

   .. attribute:: memory_store

      Manager for memory storage and retrieval operations

   .. attribute:: classifier

      Classifier for analyzing memory content and types

   .. attribute:: knowledge_graph

      The maintained knowledge graph structure

   .. attribute:: graph_transformer

      Transformer for graph processing operations

   .. attribute:: extract_batch_size

      Number of memories to process in each batch

   .. attribute:: min_confidence_threshold

      Minimum confidence score for extracted entities/relationships

   .. attribute:: enable_iterative_refinement

      Whether to enable iterative graph refinement

   .. attribute:: entity_types

      List of entity types the agent should extract

   .. attribute:: relationship_types

      List of relationship types the agent should extract

   .. attribute:: entity_extraction_prompt

      Prompt template for entity extraction

   .. attribute:: relationship_extraction_prompt

      Prompt template for relationship extraction

   .. rubric:: Examples

   Basic usage::

       # Create configuration
       config = KGGeneratorAgentConfig(
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           engine=AugLLMConfig(temperature=0.1)
       )

       # Create agent
       kg_agent = KGGeneratorAgent(config)

       # Extract knowledge graph from memories
       graph = await kg_agent.extract_knowledge_graph_from_memories()
       print(
           f"Extracted {len(graph.nodes)} entities and {len(graph.relationships)} relationships")

   Entity extraction::

       # Extract entities with limit
       entities = await kg_agent.extract_entities_from_memories(limit=10)

       for entity in entities:
           print(
               f"Entity: {entity.name} ({entity.type}) - Confidence: {entity.confidence}")

   Relationship extraction::

       # Extract relationships
       relationships = await kg_agent.extract_relationships_from_memories(limit=10)

       for rel in relationships:
           print(f"Relationship: {rel.relationship_type} "
                 f"({rel.source_id} -> {rel.target_id})")

   Entity exploration::

       # Get entity context with neighborhood
       context = await kg_agent.get_entity_context("Python")

       if "entity" in context:
           entity = context["entity"]
           neighborhood = context["neighborhood"]
           print(f"Entity: {entity.name}")
           print(f"Connected nodes: {neighborhood['total_nodes']}")
           print(f"Relationships: {neighborhood['total_relationships']}")

   Agent execution::

       # Use agent for interactive queries
       response = await kg_agent.run("Extract knowledge graph from recent memories")
       print(response)

       # Get graph statistics
       stats = await kg_agent.run("Show me graph statistics")
       print(stats)


   .. autolink-examples:: KGGeneratorAgent
      :collapse:

   .. py:method:: _extract_entities_from_memory(memory: dict[str, Any]) -> None
      :async:


      Extract entities from a single memory.


      .. autolink-examples:: _extract_entities_from_memory
         :collapse:


   .. py:method:: _extract_relationships_from_memory(memory: dict[str, Any]) -> None
      :async:


      Extract relationships from a single memory.


      .. autolink-examples:: _extract_relationships_from_memory
         :collapse:


   .. py:method:: _find_entity_id(entity_name: str) -> str | None

      Find entity ID by name.


      .. autolink-examples:: _find_entity_id
         :collapse:


   .. py:method:: _generate_entity_id(name: str, entity_type: str) -> str

      Generate unique entity ID.


      .. autolink-examples:: _generate_entity_id
         :collapse:


   .. py:method:: _generate_relationship_id(source_id: str, target_id: str, rel_type: str) -> str

      Generate unique relationship ID.


      .. autolink-examples:: _generate_relationship_id
         :collapse:


   .. py:method:: _parse_json_response(response: str) -> dict[str, Any] | None

      Parse JSON response from LLM.


      .. autolink-examples:: _parse_json_response
         :collapse:


   .. py:method:: _process_memory_batch(memories: list[dict[str, Any]]) -> None
      :async:


      Process a batch of memories for entity and relationship extraction.


      .. autolink-examples:: _process_memory_batch
         :collapse:


   .. py:method:: _setup_prompts() -> None

      Setup prompts for entity and relationship extraction.


      .. autolink-examples:: _setup_prompts
         :collapse:


   .. py:method:: extract_entities_from_memories(limit: int | None = None, namespace: tuple[str, Ellipsis] | None = None) -> list[KnowledgeGraphNode]
      :async:


      Extract entities from memories and return them as a list.

      :param limit: Maximum number of memories to process
      :param namespace: Memory namespace to process

      :returns: List of extracted knowledge graph nodes (entities)


      .. autolink-examples:: extract_entities_from_memories
         :collapse:


   .. py:method:: extract_knowledge_graph_from_memories(memory_ids: list[str] | None = None, namespace: tuple[str, Ellipsis] | None = None, memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None) -> MemoryKnowledgeGraph
      :async:


      Extract knowledge graph from specified memories.

      Processes memories to extract entities and relationships, building a comprehensive
      knowledge graph. Uses LLM-powered extraction to identify semantic structures
      and connections across memory content.

      :param memory_ids: Specific memory IDs to process. If None, processes all memories
                         in the specified namespace and types.
      :param namespace: Memory namespace to process. If None, processes all namespaces.
      :param memory_types: Specific memory types to process. If None, processes all types.

      :returns: Updated MemoryKnowledgeGraph containing extracted entities and relationships
                with metadata about the extraction process.

      :raises ValueError: If no memories are found to process
      :raises RuntimeError: If extraction fails due to LLM or processing errors

      .. rubric:: Examples

      Extract from all memories::

          # Extract from all memories
          graph = await kg_agent.extract_knowledge_graph_from_memories()
          print(f"Extracted {len(graph.nodes)} entities")
          print(f"Extracted {len(graph.relationships)} relationships")

      Extract from specific memories::

          # Extract from specific memory IDs
          memory_ids = ["mem_123", "mem_456", "mem_789"]
          graph = await kg_agent.extract_knowledge_graph_from_memories(
              memory_ids=memory_ids
          )

      Extract from specific namespace::

          # Extract from user's personal memories
          graph = await kg_agent.extract_knowledge_graph_from_memories(
              namespace=("user", "personal")
          )

      Extract from specific memory types::

          # Extract only from semantic and episodic memories
          graph = await kg_agent.extract_knowledge_graph_from_memories(
              memory_types=[MemoryType.SEMANTIC, MemoryType.EPISODIC]
          )

      .. note::

         The extraction process runs in batches (controlled by extract_batch_size)
         to manage memory usage and API rate limits. Progress is logged during
         processing.


      .. autolink-examples:: extract_knowledge_graph_from_memories
         :collapse:


   .. py:method:: extract_relationships_from_memories(limit: int | None = None, namespace: tuple[str, Ellipsis] | None = None) -> list[KnowledgeGraphRelationship]
      :async:


      Extract relationships from memories and return them as a list.

      :param limit: Maximum number of memories to process
      :param namespace: Memory namespace to process

      :returns: List of extracted knowledge graph relationships


      .. autolink-examples:: extract_relationships_from_memories
         :collapse:


   .. py:method:: get_entity_context(entity_name: str) -> dict[str, Any]
      :async:


      Get context for an entity by name.

      :param entity_name: Name of the entity to get context for

      :returns: Dictionary containing entity context information


      .. autolink-examples:: get_entity_context
         :collapse:


   .. py:method:: get_entity_neighborhood(entity_id: str, depth: int = 1) -> dict[str, Any]
      :async:


      Get the neighborhood of an entity up to specified depth.

      :param entity_id: The entity to explore
      :param depth: Maximum depth to traverse

      :returns: Dictionary containing entity neighborhood information


      .. autolink-examples:: get_entity_neighborhood
         :collapse:


   .. py:method:: run(user_input: str) -> str
      :async:


      Main execution method for the KG Generator Agent.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup agent after initialization - Pydantic pattern.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: classifier
      :type:  haive.agents.memory.core.classifier.MemoryClassifier
      :value: None



   .. py:attribute:: enable_iterative_refinement
      :type:  bool
      :value: None



   .. py:attribute:: entity_extraction_prompt
      :type:  langchain_core.prompts.PromptTemplate
      :value: None



   .. py:attribute:: entity_types
      :type:  list[str]
      :value: None



   .. py:attribute:: extract_batch_size
      :type:  int
      :value: None



   .. py:attribute:: graph_transformer
      :type:  haive.agents.document_modifiers.kg.kg_base.models.GraphTransformer
      :value: None



   .. py:attribute:: knowledge_graph
      :type:  MemoryKnowledgeGraph
      :value: None



   .. py:attribute:: memory_store
      :type:  haive.agents.memory.core.stores.MemoryStoreManager
      :value: None



   .. py:attribute:: min_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: relationship_extraction_prompt
      :type:  langchain_core.prompts.PromptTemplate
      :value: None



   .. py:attribute:: relationship_types
      :type:  list[str]
      :value: None



.. py:class:: KGGeneratorAgentConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for Knowledge Graph Generator Agent.

   This configuration class defines all parameters needed to create and configure
   a KGGeneratorAgent, including LLM settings, extraction parameters, and entity/relationship
   type specifications.

   .. attribute:: name

      Unique identifier for the agent instance

   .. attribute:: memory_store_manager

      Manager for memory storage and retrieval operations

   .. attribute:: memory_classifier

      Classifier for analyzing memory content and types

   .. attribute:: engine

      LLM engine configuration for entity and relationship extraction

   .. attribute:: extract_batch_size

      Number of memories to process in each batch

   .. attribute:: min_confidence_threshold

      Minimum confidence score for extracted entities/relationships

   .. attribute:: enable_iterative_refinement

      Whether to enable iterative graph refinement

   .. attribute:: entity_types

      List of entity types the agent should extract

   .. attribute:: relationship_types

      List of relationship types the agent should extract

   .. rubric:: Examples

   Basic configuration::

       config = KGGeneratorAgentConfig(
           name="my_kg_generator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           engine=AugLLMConfig(temperature=0.1),
           extract_batch_size=20,
           min_confidence_threshold=0.7
       )

   Advanced configuration with custom types::

       config = KGGeneratorAgentConfig(
           name="custom_kg_generator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           engine=AugLLMConfig(
               model="gpt-4",
               temperature=0.1,
               max_tokens=2000
           ),
           extract_batch_size=15,
           min_confidence_threshold=0.8,
           entity_types=[
               "person", "organization", "technology", "concept",
               "project", "skill", "tool", "document"
           ],
           relationship_types=[
               "works_at", "knows", "uses", "creates", "manages",
               "collaborates_with", "depends_on", "teaches"
           ]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KGGeneratorAgentConfig
      :collapse:

   .. py:attribute:: enable_iterative_refinement
      :type:  bool
      :value: None



   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: entity_types
      :type:  list[str]
      :value: None



   .. py:attribute:: extract_batch_size
      :type:  int
      :value: None



   .. py:attribute:: memory_classifier
      :type:  haive.agents.memory.core.classifier.MemoryClassifier
      :value: None



   .. py:attribute:: memory_store_manager
      :type:  haive.agents.memory.core.stores.MemoryStoreManager
      :value: None



   .. py:attribute:: min_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: relationship_types
      :type:  list[str]
      :value: None



.. py:class:: KnowledgeGraphNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a node (entity) in the knowledge graph.

   A knowledge graph node encapsulates an entity extracted from memory content,
   including its type, properties, and references to the memories that mention it.

   .. attribute:: id

      Unique identifier for the node, typically generated from name and type

   .. attribute:: type

      Entity type classification (person, organization, concept, etc.)

   .. attribute:: name

      Human-readable display name of the entity

   .. attribute:: properties

      Dictionary of additional properties and attributes

   .. attribute:: memory_references

      List of memory IDs that reference this entity

   .. attribute:: confidence

      Confidence score in entity existence and accuracy (0.0-1.0)

   .. attribute:: created_at

      UTC timestamp when the entity was first created

   .. attribute:: last_updated

      UTC timestamp of the last update to this entity

   .. rubric:: Examples

   Creating a person entity::

       person = KnowledgeGraphNode(
           id="person_alice_smith",
           type="person",
           name="Alice Smith",
           properties={"role": "engineer", "company": "TechCorp"},
           memory_references=["mem_123", "mem_456"],
           confidence=0.95
       )

   Creating a concept entity::

       concept = KnowledgeGraphNode(
           id="concept_machine_learning",
           type="concept",
           name="Machine Learning",
           properties={"category": "technology", "complexity": "high"},
           confidence=0.9
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeGraphNode
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: last_updated
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: memory_references
      :type:  list[str]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: type
      :type:  str
      :value: None



.. py:class:: KnowledgeGraphRelationship(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a relationship (edge) in the knowledge graph.

   A knowledge graph relationship connects two entities with a typed relationship,
   capturing semantic connections discovered from memory content.

   .. attribute:: id

      Unique identifier for the relationship, typically generated from source, target, and type

   .. attribute:: source_id

      ID of the source entity in the relationship

   .. attribute:: target_id

      ID of the target entity in the relationship

   .. attribute:: relationship_type

      Type of relationship (works_at, knows, uses, etc.)

   .. attribute:: properties

      Dictionary of additional relationship properties

   .. attribute:: memory_references

      List of memory IDs that reference this relationship

   .. attribute:: confidence

      Confidence score in relationship existence and accuracy (0.0-1.0)

   .. attribute:: created_at

      UTC timestamp when the relationship was first created

   .. attribute:: last_updated

      UTC timestamp of the last update to this relationship

   .. rubric:: Examples

   Creating a work relationship::

       work_rel = KnowledgeGraphRelationship(
           id="person_alice_smith_works_at_organization_techcorp",
           source_id="person_alice_smith",
           target_id="organization_techcorp",
           relationship_type="works_at",
           properties={

   "role": "senior_engineer",
    "start_date": "2020-01-15"},
               memory_references=["mem_123"],
               confidence=0.9
           )

       Creating a knowledge relationship::

           knows_rel = KnowledgeGraphRelationship(
               id="person_alice_smith_knows_concept_machine_learning",
               source_id="person_alice_smith",
               target_id="concept_machine_learning",
               relationship_type="knows",
               properties={"proficiency": "expert", "years_experience": 5},
               confidence=0.85
           )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeGraphRelationship
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: last_updated
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: memory_references
      :type:  list[str]
      :value: None



   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: relationship_type
      :type:  str
      :value: None



   .. py:attribute:: source_id
      :type:  str
      :value: None



   .. py:attribute:: target_id
      :type:  str
      :value: None



.. py:class:: MemoryKnowledgeGraph(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete knowledge graph structure extracted from memory system.

   The MemoryKnowledgeGraph represents a comprehensive knowledge graph built from
   memory content, containing entities (nodes) and their relationships (edges).
   It provides methods for managing the graph structure and querying entity neighborhoods.

   .. attribute:: nodes

      Dictionary mapping node IDs to KnowledgeGraphNode objects

   .. attribute:: relationships

      Dictionary mapping relationship IDs to KnowledgeGraphRelationship objects

   .. attribute:: metadata

      Dictionary containing graph-level metadata and statistics

   .. rubric:: Examples

   Creating and populating a knowledge graph::

       graph = MemoryKnowledgeGraph()

       # Add entities
       person = KnowledgeGraphNode(
           id="person_alice", type="person", name="Alice Smith"
       )
       company = KnowledgeGraphNode(
           id="org_techcorp", type="organization", name="TechCorp"
       )

       graph.add_node(person)
       graph.add_node(company)

       # Add relationship
       works_at = KnowledgeGraphRelationship(
           id="alice_works_at_techcorp",
           source_id="person_alice",
           target_id="org_techcorp",
           relationship_type="works_at"
       )

       graph.add_relationship(works_at)

   Querying the graph::

       # Get connected nodes
       connected = graph.get_connected_nodes("person_alice")

       # Get all relationships for a node
       relationships = graph.get_relationships_for_node("person_alice")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryKnowledgeGraph
      :collapse:

   .. py:method:: add_node(node: KnowledgeGraphNode) -> None

      Add or update a node in the graph.

      If the node already exists, its properties and memory references are merged
      with the existing node. Otherwise, a new node is added to the graph.

      :param node: The KnowledgeGraphNode to add or update

      .. rubric:: Examples

      Adding a new node::

          graph = MemoryKnowledgeGraph()
          node = KnowledgeGraphNode(
              id="person_alice", type="person", name="Alice Smith"
          )
          graph.add_node(node)

      Updating an existing node::

          # First addition
          node1 = KnowledgeGraphNode(
              id="person_alice", type="person", name="Alice Smith",
              properties={"role": "engineer"}
          )
          graph.add_node(node1)

          # Update with additional properties
          node2 = KnowledgeGraphNode(
              id="person_alice", type="person", name="Alice Smith",
              properties={"company": "TechCorp"}
          )
          graph.add_node(node2)
          # Result: node has both "role" and "company" properties


      .. autolink-examples:: add_node
         :collapse:


   .. py:method:: add_relationship(relationship: KnowledgeGraphRelationship) -> None

      Add or update a relationship in the graph.

      If the relationship already exists, its properties and memory references are merged
      with the existing relationship. Otherwise, a new relationship is added to the graph.

      :param relationship: The KnowledgeGraphRelationship to add or update

      .. rubric:: Examples

      Adding a new relationship::

          graph = MemoryKnowledgeGraph()
          rel = KnowledgeGraphRelationship(
              id="alice_works_at_techcorp",
              source_id="person_alice",
              target_id="org_techcorp",
              relationship_type="works_at"
          )
          graph.add_relationship(rel)

      Updating an existing relationship::

          # First addition
          rel1 = KnowledgeGraphRelationship(
              id="alice_works_at_techcorp",
              source_id="person_alice",
              target_id="org_techcorp",
              relationship_type="works_at",
              properties={"role": "engineer"}
          )
          graph.add_relationship(rel1)

          # Update with additional properties
          rel2 = KnowledgeGraphRelationship(
              id="alice_works_at_techcorp",
              source_id="person_alice",
              target_id="org_techcorp",
              relationship_type="works_at",
              properties={"start_date": "2020-01-15"}
          )
          graph.add_relationship(rel2)
          # Result: relationship has both "role" and "start_date"
          # properties


      .. autolink-examples:: add_relationship
         :collapse:


   .. py:method:: get_connected_nodes(node_id: str) -> list[KnowledgeGraphNode]

      Get all nodes connected to a given node.

      Traverses all relationships to find nodes that are directly connected
      to the specified node, regardless of relationship direction.

      :param node_id: The ID of the node to find connections for

      :returns: List of KnowledgeGraphNode objects connected to the specified node

      .. rubric:: Examples

      Finding connected nodes::

          graph = MemoryKnowledgeGraph()
          # Assume graph has been populated with nodes and relationships

          connected = graph.get_connected_nodes("person_alice")
          for node in connected:
              print(f"Connected to: {node.name} ({node.type})")


      .. autolink-examples:: get_connected_nodes
         :collapse:


   .. py:method:: get_relationships_for_node(node_id: str) -> list[KnowledgeGraphRelationship]

      Get all relationships involving a given node.

      Finds all relationships where the specified node is either the source
      or target of the relationship.

      :param node_id: The ID of the node to find relationships for

      :returns: List of KnowledgeGraphRelationship objects involving the specified node

      .. rubric:: Examples

      Finding node relationships::

          graph = MemoryKnowledgeGraph()
          # Assume graph has been populated

          relationships = graph.get_relationships_for_node(
              "person_alice")
          for rel in relationships:
              print(f"Relationship: {rel.relationship_type} "
                    f"({rel.source_id} -> {rel.target_id})")


      .. autolink-examples:: get_relationships_for_node
         :collapse:


   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: nodes
      :type:  dict[str, KnowledgeGraphNode]
      :value: None



   .. py:attribute:: relationships
      :type:  dict[str, KnowledgeGraphRelationship]
      :value: None



.. py:data:: logger

