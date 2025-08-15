agents.rag.db_rag.graph_db.config
=================================

.. py:module:: agents.rag.db_rag.graph_db.config

.. autoapi-nested-parse::

   Configuration module for the Graph Database RAG Agent.

   This module provides configuration classes for connecting to Neo4j databases
   and configuring the Graph DB RAG Agent with appropriate engines, schemas,
   and domain-specific settings.

   .. rubric:: Example

   Basic configuration setup::

       >>> from haive.agents.rag.db_rag.graph_db.config import GraphDBRAGConfig
       >>>
       >>> # Create config with default settings
       >>> config = GraphDBRAGConfig(
       ...     domain_name="movies",
       ...     domain_categories=["movie", "actor", "director"]
       ... )
       >>>
       >>> # Create agent with config
       >>> agent = GraphDBRAGAgent(config)

   Environment Variables:
       The following environment variables are used for Neo4j connection:

       - NEO4J_URI: The URI of the Neo4j database (e.g., "bolt://localhost:7687")
       - NEO4J_USER: Username for Neo4j authentication
       - NEO4J_PASSWORD: Password for Neo4j authentication
       - NEO4J_DATABASE: Database name (optional, defaults to "neo4j")


   .. autolink-examples:: agents.rag.db_rag.graph_db.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.db_rag.graph_db.config.GraphDBAgentConfig


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.graph_db.config.ExampleConfig
   agents.rag.db_rag.graph_db.config.GraphDBConfig
   agents.rag.db_rag.graph_db.config.GraphDBRAGConfig


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.config.get_graph_db
   agents.rag.db_rag.graph_db.config.get_graph_db_schema
   agents.rag.db_rag.graph_db.config.validate_engines


Module Contents
---------------

.. py:class:: ExampleConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for few-shot examples used in Cypher generation.

   This class manages example queries that help the LLM learn the mapping
   between natural language questions and Cypher queries for a specific domain.

   .. attribute:: examples_path

      Path to JSON file containing examples. The file should
      contain a list of dicts with "question" and "query" keys.

   .. attribute:: examples

      Direct list of examples if not using a file. Each example
      should have "question" (natural language) and "query" (Cypher) keys.

   .. attribute:: k

      Number of examples to retrieve for few-shot prompting. More examples
      can improve accuracy but increase prompt length.

   .. rubric:: Example

   >>> # Using a file
   >>> example_config = ExampleConfig(
   ...     examples_path="examples/movie_queries.json",
   ...     k=3
   ... )
   >>>
   >>> # Using direct examples
   >>> example_config = ExampleConfig(
   ...     examples=[
   ...         {
   ...             "question": "Who directed Inception?",
   ...             "query": "MATCH (p:Person)-[:DIRECTED]->(m:Movie {title: 'Inception'}) RETURN p.name"
   ...         },
   ...         {
   ...             "question": "What movies did Tom Hanks act in?",
   ...             "query": "MATCH (p:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN m.title"
   ...         }
   ...     ],
   ...     k=2
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExampleConfig
      :collapse:

   .. py:attribute:: examples
      :type:  list[dict[str, str]] | None
      :value: None



   .. py:attribute:: examples_path
      :type:  str | None
      :value: None



   .. py:attribute:: k
      :type:  int
      :value: None



.. py:class:: GraphDBConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for connecting to a Neo4j graph database.

   This class manages Neo4j connection parameters and provides methods
   for establishing connections and retrieving schema information.

   .. attribute:: graph_db_uri

      Neo4j connection URI. Defaults to NEO4J_URI env var.
      Format: "bolt://host:port" or "neo4j://host:port"

   .. attribute:: graph_db_user

      Username for authentication. Defaults to NEO4J_USER env var.

   .. attribute:: graph_db_password

      Password for authentication. Defaults to NEO4J_PASSWORD env var.

   .. attribute:: graph_db_database

      Database name. Defaults to NEO4J_DATABASE env var or "neo4j".

   .. attribute:: enhanced_schema

      Whether to use enhanced schema scanning for better
      property and relationship detection.

   .. rubric:: Example

   >>> # Using environment variables
   >>> db_config = GraphDBConfig()
   >>>
   >>> # Explicit configuration
   >>> db_config = GraphDBConfig(
   ...     graph_db_uri="bolt://localhost:7687",
   ...     graph_db_user="neo4j",
   ...     graph_db_password="password",
   ...     graph_db_database="movies"
   ... )
   >>>
   >>> # Connect to database
   >>> graph = db_config.get_graph_db()
   >>> if graph:
   ...     schema = db_config.get_graph_db_schema()

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphDBConfig
      :collapse:

   .. py:method:: get_graph_db() -> langchain_neo4j.Neo4jGraph | None

      Create and return a Neo4jGraph connection object.

      Establishes a secure connection to the Neo4j database with proper
      timeout, sanitization, and schema refresh settings.

      :returns: Connected graph object if successful.
                None: If connection fails.
      :rtype: Neo4jGraph

      .. rubric:: Example

      >>> config = GraphDBConfig()
      >>> graph = config.get_graph_db()
      >>> if graph:
      ...     print("✅ Connected to Neo4j")
      ... else:
      ...     print("❌ Connection failed")


      .. autolink-examples:: get_graph_db
         :collapse:


   .. py:method:: get_graph_db_schema() -> dict | None

      Retrieve the graph schema from the Neo4j database.

      Gets the complete schema including node labels, relationship types,
      and properties. Uses enhanced schema if enabled for more detailed
      information.

      :returns:

                Schema dictionary with structure:
                    {
                        "node_props": {label: [properties]},
                        "rel_props": {type: [properties]},
                        "relationships": [relationship_structures]
                    }
                None: If connection fails or schema cannot be retrieved.
      :rtype: dict

      .. rubric:: Example

      >>> config = GraphDBConfig(enhanced_schema=True)
      >>> schema = config.get_graph_db_schema()
      >>> if schema:
      ...     print(f"Node labels: {list(schema['node_props'].keys())}")
      ...     print(f"Relationship types: {list(schema['rel_props'].keys())}")


      .. autolink-examples:: get_graph_db_schema
         :collapse:


   .. py:attribute:: enhanced_schema
      :type:  bool
      :value: None



   .. py:attribute:: graph_db_database
      :type:  str
      :value: None



   .. py:attribute:: graph_db_password
      :type:  str
      :value: None



   .. py:attribute:: graph_db_uri
      :type:  str
      :value: None



   .. py:attribute:: graph_db_user
      :type:  str
      :value: None



.. py:class:: GraphDBRAGConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Main configuration for the Graph Database RAG Agent.

   This class provides comprehensive configuration for the Graph DB RAG Agent,
   including LLM engines, domain settings, database connection, and schemas.

   .. attribute:: engines

      Dictionary of AugLLMConfig engines for different workflow steps:
      - "guardrails": Checks domain relevance
      - "text2cypher": Converts natural language to Cypher
      - "validate_cypher": Validates generated Cypher
      - "correct_cypher": Fixes Cypher errors
      - "generate_final_answer": Creates natural language response

   .. attribute:: domain_name

      The domain this agent specializes in (e.g., "movies", "healthcare").
      Used for guardrails and example selection.

   .. attribute:: domain_categories

      Valid categories within the domain for fine-grained routing.

   .. attribute:: example_config

      Configuration for few-shot examples.

   .. attribute:: state_schema

      Pydantic model for workflow state management.

   .. attribute:: graph_db_config

      Neo4j connection configuration.

   .. attribute:: input_schema

      Schema for agent input validation.

   .. attribute:: output_schema

      Schema for agent output structure.

   .. attribute:: domain_examples

      Domain-specific examples for different categories.

   .. rubric:: Example

   >>> # Configure a movie domain agent
   >>> config = GraphDBRAGConfig(
   ...     domain_name="movies",
   ...     domain_categories=["movie", "actor", "director", "genre"],
   ...     example_config=ExampleConfig(
   ...         examples_path="examples/movie_queries.json",
   ...         k=3
   ...     ),
   ...     graph_db_config=GraphDBConfig(
   ...         graph_db_uri="bolt://localhost:7687",
   ...         graph_db_user="neo4j",
   ...         graph_db_password="password"
   ...     )
   ... )
   >>>
   >>> # Create agent
   >>> agent = GraphDBRAGAgent(config)

   .. note::

      All required engines must be present in the engines dictionary.
      The validator will check for their presence and raise an error
      if any are missing.


   .. autolink-examples:: GraphDBRAGConfig
      :collapse:

   .. py:method:: validate_engines(engines: dict[str, haive.core.engine.aug_llm.AugLLMConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :classmethod:


      Validate that all required engines are present.

      Checks for the presence of all required engine configurations and
      handles potential naming mismatches (e.g., "generate_cypher" vs "text2cypher").

      :param engines: Dictionary of engine configurations.

      :returns: Validated engines dictionary.
      :rtype: Dict[str, AugLLMConfig]

      :raises ValueError: If any required engine is missing.


      .. autolink-examples:: validate_engines
         :collapse:


   .. py:attribute:: domain_categories
      :type:  list[str]
      :value: None



   .. py:attribute:: domain_examples
      :type:  dict[str, list[dict[str, str]]]
      :value: None



   .. py:attribute:: domain_name
      :type:  str
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: example_config
      :type:  ExampleConfig | None
      :value: None



   .. py:attribute:: graph_db_config
      :type:  GraphDBConfig
      :value: None



   .. py:attribute:: input_schema
      :type:  Any
      :value: None



   .. py:attribute:: output_schema
      :type:  Any
      :value: None



   .. py:attribute:: state_schema
      :type:  Any
      :value: None



.. py:function:: get_graph_db(uri: str = None, user: str = None, password: str = None, database: str = 'neo4j')

   Get a Neo4j database connection.

   :param uri: Neo4j URI (defaults to NEO4J_URI env var)
   :param user: Username (defaults to NEO4J_USER env var)
   :param password: Password (defaults to NEO4J_PASSWORD env var)
   :param database: Database name (defaults to "neo4j")

   :returns: Mock database connection (placeholder implementation)


   .. autolink-examples:: get_graph_db
      :collapse:

.. py:function:: get_graph_db_schema(db_connection=None) -> dict

   Get the schema from a Neo4j database.

   :param db_connection: Database connection object

   :returns: Dictionary representing the database schema


   .. autolink-examples:: get_graph_db_schema
      :collapse:

.. py:function:: validate_engines(engines: dict) -> bool

   Validate that all required engines are properly configured.

   :param engines: Dictionary of engine configurations

   :returns: True if all engines are valid, False otherwise


   .. autolink-examples:: validate_engines
      :collapse:

.. py:data:: GraphDBAgentConfig

   Alias for backward compatibility with older code.

   .. autolink-examples:: GraphDBAgentConfig
      :collapse:

