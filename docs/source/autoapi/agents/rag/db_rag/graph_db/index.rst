agents.rag.db_rag.graph_db
==========================

.. py:module:: agents.rag.db_rag.graph_db

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: agents.rag.db_rag.graph_db
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/rag/db_rag/graph_db/agent/index
   /autoapi/agents/rag/db_rag/graph_db/branches/index
   /autoapi/agents/rag/db_rag/graph_db/config/index
   /autoapi/agents/rag/db_rag/graph_db/engines/index
   /autoapi/agents/rag/db_rag/graph_db/example/index
   /autoapi/agents/rag/db_rag/graph_db/models/index
   /autoapi/agents/rag/db_rag/graph_db/scratch/index
   /autoapi/agents/rag/db_rag/graph_db/state/index


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.graph_db.Config
   agents.rag.db_rag.graph_db.CypherQueryOutput
   agents.rag.db_rag.graph_db.ExampleConfig
   agents.rag.db_rag.graph_db.GraphDBConfig
   agents.rag.db_rag.graph_db.GraphDBRAGAgent
   agents.rag.db_rag.graph_db.GraphDBRAGConfig
   agents.rag.db_rag.graph_db.GuardrailsOutput
   agents.rag.db_rag.graph_db.InputState
   agents.rag.db_rag.graph_db.OutputState
   agents.rag.db_rag.graph_db.OverallState
   agents.rag.db_rag.graph_db.PropertyFilter
   agents.rag.db_rag.graph_db.ValidateCypherOutput


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.basic_example
   agents.rag.db_rag.graph_db.batch_processing_example
   agents.rag.db_rag.graph_db.check_domain_relevance
   agents.rag.db_rag.graph_db.correct_query
   agents.rag.db_rag.graph_db.custom_domain_example
   agents.rag.db_rag.graph_db.domain_router
   agents.rag.db_rag.graph_db.error_handling_example
   agents.rag.db_rag.graph_db.execute_query
   agents.rag.db_rag.graph_db.generate_answer
   agents.rag.db_rag.graph_db.generate_query
   agents.rag.db_rag.graph_db.get_graph_db
   agents.rag.db_rag.graph_db.get_graph_db_schema
   agents.rag.db_rag.graph_db.main
   agents.rag.db_rag.graph_db.performance_monitoring_example
   agents.rag.db_rag.graph_db.run_all_examples
   agents.rag.db_rag.graph_db.setup_workflow
   agents.rag.db_rag.graph_db.streaming_example
   agents.rag.db_rag.graph_db.validate_cypher_syntax
   agents.rag.db_rag.graph_db.validate_decision
   agents.rag.db_rag.graph_db.validate_engines
   agents.rag.db_rag.graph_db.validate_filter_type
   agents.rag.db_rag.graph_db.validate_query
   agents.rag.db_rag.graph_db.validation_router


Package Contents
----------------

.. py:class:: Config(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Top-level configuration class for Graph DB RAG models.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Config
      :collapse:

   .. py:attribute:: allowed_categories
      :type:  list[str]
      :value: None



   .. py:attribute:: domain_name
      :type:  str
      :value: None



   .. py:attribute:: validation_enabled
      :type:  bool
      :value: None



.. py:class:: CypherQueryOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for Cypher query generation.

   This model ensures that generated Cypher queries are properly formatted
   and optionally include parameters for parameterized queries.

   .. attribute:: query

      The generated Cypher query string. Must start with a valid
      Cypher keyword (MATCH, CREATE, etc.).

   .. attribute:: parameters

      Optional dictionary of query parameters for parameterized
      queries. Keys are parameter names (without $), values are the
      parameter values.

   .. rubric:: Example

   >>> # Simple query without parameters
   >>> output = CypherQueryOutput(
   ...     query="MATCH (m:Movie) RETURN m.title LIMIT 10"
   ... )

   >>> # Parameterized query
   >>> output = CypherQueryOutput(
   ...     query="MATCH (m:Movie) WHERE m.year = $year RETURN m.title",
   ...     parameters={"year": 2023}
   ... )

   :raises ValueError: If the query doesn't start with a valid Cypher keyword.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CypherQueryOutput
      :collapse:

   .. py:method:: validate_cypher_syntax(query: str) -> str
      :classmethod:


      Validate that the query starts with a valid Cypher keyword.

      :param query: The Cypher query string to validate.

      :returns: The validated query string.
      :rtype: str

      :raises ValueError: If the query doesn't start with a valid keyword.


      .. autolink-examples:: validate_cypher_syntax
         :collapse:


   .. py:attribute:: parameters
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



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



.. py:class:: GraphDBRAGAgent(config: haive.agents.rag.db_rag.graph_db.config.GraphDBRAGConfig = GraphDBRAGConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.rag.db_rag.graph_db.config.GraphDBRAGConfig`\ ]


   Graph Database RAG Agent for natural language querying of Neo4j databases.

   This agent implements a sophisticated workflow for converting natural language
   questions into Cypher queries, executing them against a Neo4j database, and
   generating human-readable responses. It includes domain validation, query
   validation, error correction, and result formatting.

   The agent uses few-shot learning with domain-specific examples to improve
   query generation accuracy and includes robust error handling for common
   Cypher mistakes.

   .. attribute:: config

      Configuration object containing all settings.

      :type: GraphDBRAGConfig

   .. attribute:: graph_db

      Connected Neo4j database instance.

      :type: Neo4jGraph

   .. attribute:: graph_db_enhanced_schema

      Enhanced schema information from the database.

   .. attribute:: graph_db_structured_schema

      Structured schema for relationship validation.

   .. attribute:: corrector_schema

      Schema used for correcting relationship directions.

   .. attribute:: cypher_query_corrector

      Utility for fixing common Cypher errors.

   .. attribute:: example_selector

      Semantic similarity selector for few-shot examples.

   .. attribute:: no_results

      Default message when no results are found.

      :type: str

   .. rubric:: Example

   Creating and using the agent::

       >>> # Create agent with minimal config
       >>> agent = GraphDBRAGAgent()
       >>>
       >>> # Query the database
       >>> result = agent.invoke({
       ...     "question": "What movies has Tom Hanks acted in?"
       ... })
       >>> print(f"Answer: {result['answer']}")
       >>> print(f"Cypher used: {result['cypher_statement']}")

       >>> # Use with custom domain
       >>> config = GraphDBRAGConfig(
       ...     domain_name="healthcare",
       ...     domain_categories=["patient", "doctor", "medication"]
       ... )
       >>> healthcare_agent = GraphDBRAGAgent(config)

   .. note::

      The agent automatically sets up the workflow graph upon initialization.
      All node functions return Command objects for state updates and routing.

   Initialize the Graph DB RAG Agent.

   Sets up the Neo4j connection, schema information, example selector,
   and workflow graph. Handles initialization errors gracefully with
   appropriate logging.

   :param config: Configuration object. Defaults to GraphDBRAGConfig() which
                  uses environment variables for Neo4j connection.

   :raises ValueError: If Neo4j connection cannot be established.
   :raises Exception: For other initialization errors.

   .. rubric:: Example

   >>> # Using default config (from environment)
   >>> agent = GraphDBRAGAgent()

   >>> # Using custom config
   >>> custom_config = GraphDBRAGConfig(
   ...     domain_name="movies",
   ...     graph_db_config=GraphDBConfig(
   ...         graph_db_uri="bolt://localhost:7687"
   ...     )
   ... )
   >>> agent = GraphDBRAGAgent(custom_config)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphDBRAGAgent
      :collapse:

   .. py:method:: _get_default_examples(domain_name: str) -> list[dict[str, str]]

      Get default examples for the specified domain.

      Provides pre-defined examples for common domains to help with few-shot
      learning when custom examples are not provided.

      :param domain_name: The name of the domain (e.g., "movies", "healthcare").

      :returns:     - question: Natural language question
                    - query: Corresponding Cypher query
      :rtype: List of example dictionaries, each containing

      .. rubric:: Example

      >>> agent = GraphDBRAGAgent()
      >>> examples = agent._get_default_examples("movies")
      >>> print(examples[0])
      {
          "question": "Which movie has the highest rating?",
          "query": "MATCH (m:Movie) RETURN m.title, m.rating ORDER BY m.rating DESC LIMIT 1"
      }


      .. autolink-examples:: _get_default_examples
         :collapse:


   .. py:method:: _initialize_config(config: haive.agents.rag.db_rag.graph_db.config.GraphDBRAGConfig) -> None

      Initialize configuration and core components.

      Sets up the Neo4j connection, retrieves schema information, configures
      the Cypher query corrector, and initializes the example selector for
      few-shot learning.

      :param config: The configuration object containing all settings.

      :raises ValueError: If Neo4j connection fails.
      :raises Exception: For other initialization errors.

      .. note::

         This method is called automatically during __init__ and should not
         be called directly.


      .. autolink-examples:: _initialize_config
         :collapse:


   .. py:method:: _initialize_example_selector(config: haive.agents.rag.db_rag.graph_db.config.GraphDBRAGConfig) -> None

      Initialize the semantic example selector for few-shot learning.

      Creates an example selector that retrieves relevant query examples based
      on semantic similarity. Falls back to simpler selection methods if
      vector-based selection fails.

      :param config: Configuration containing example settings and domain info.

      .. note::

         The selector prioritizes examples in this order:
         1. Domain-specific examples from config
         2. Examples loaded from file (if specified)
         3. Default examples for the domain
         4. General fallback examples


      .. autolink-examples:: _initialize_example_selector
         :collapse:


   .. py:method:: check_domain_relevance(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> langgraph.types.Command

      Check if the user's question is relevant to the configured domain.

      This is the first step in the workflow. It uses the guardrails engine
      to determine if the question should be processed or rejected as
      out-of-domain.

      :param state: Current workflow state containing the user's question.

      :returns:     - next_action: "end" if out-of-domain, otherwise continue
                    - database_records: Error message if out-of-domain
                    - steps: Updated with "check_domain_relevance"
      :rtype: Command object with updates

      .. rubric:: Example

      >>> state = OverallState(question="What's the weather like?")
      >>> command = agent.check_domain_relevance(state)
      >>> # For a movie domain agent, this would return:
      >>> # Command(update={"next_action": "end", ...})

      .. note::

         This node acts as a guardrail to prevent processing of irrelevant
         queries, saving computational resources and improving accuracy.


      .. autolink-examples:: check_domain_relevance
         :collapse:


   .. py:method:: correct_query(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> langgraph.types.Command

      Correct errors in the Cypher query based on validation feedback.

      Uses the correct_cypher engine to fix identified errors and produce
      a valid query that matches the database schema.

      :param state: Current state containing the invalid query and errors.

      :returns:     - next_action: "validate_query" (to re-validate)
                    - cypher_statement: The corrected Cypher query
                    - steps: Updated with "correct_query"
      :rtype: Command object with updates

      .. rubric:: Example

      >>> state = OverallState(
      ...     cypher_statement="MATCH (p:Actor)-[:DIRECTED]->(m:Film) RETURN p.name",
      ...     cypher_errors=["Label 'Film' does not exist, use 'Movie'"]
      ... )
      >>> command = agent.correct_query(state)
      >>> print(command.update["cypher_statement"])
      MATCH (p:Person)-[:DIRECTED]->(m:Movie) RETURN p.name

      .. note::

         The corrected query is sent back to validation to ensure
         all errors are resolved.


      .. autolink-examples:: correct_query
         :collapse:


   .. py:method:: domain_router(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> str

      Route based on domain relevance check result.

      :param state: Current state with next_action field.

      :returns: Next node name - END if out-of-domain, "generate_query" otherwise.
      :rtype: str

      .. note:: This is used as a conditional edge function in the workflow graph.


      .. autolink-examples:: domain_router
         :collapse:


   .. py:method:: execute_query(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> langgraph.types.Command

      Execute the validated Cypher query against the Neo4j database.

      Runs the query and captures the results for answer generation.
      Handles empty results gracefully.

      :param state: Current state containing the validated Cypher statement.

      :returns:     - database_records: Query results or "No results found"
                    - next_action: "generate_answer"
                    - steps: Updated with "execute_query"
      :rtype: Command object with updates

      .. rubric:: Example

      >>> state = OverallState(
      ...     cypher_statement="MATCH (m:Movie) RETURN m.title LIMIT 3"
      ... )
      >>> command = agent.execute_query(state)
      >>> print(command.update["database_records"])
      [{"m.title": "The Matrix"}, {"m.title": "Inception"}, ...]

      .. note::

         The query is executed with proper sanitization and timeout
         settings configured in the Neo4j connection.


      .. autolink-examples:: execute_query
         :collapse:


   .. py:method:: generate_answer(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> langgraph.types.Command

      Generate a natural language answer from the query results.

      Uses the generate_final_answer engine to convert database records
      into a human-friendly response that directly answers the question.

      :param state: Current state containing question and database results.

      :returns:     - answer: The natural language response
                    - next_action: "end"
                    - steps: Updated with "generate_answer"
      :rtype: Command object with updates

      .. rubric:: Example

      >>> state = OverallState(
      ...     question="Who directed The Matrix?",
      ...     database_records=[{"p.name": "Lana Wachowski"}, {"p.name": "Lilly Wachowski"}]
      ... )
      >>> command = agent.generate_answer(state)
      >>> print(command.update["answer"])
      The Matrix was directed by Lana Wachowski and Lilly Wachowski.

      .. note::

         The engine is prompted to provide direct, conversational answers
         without mentioning the database or technical details.


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: generate_query(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> langgraph.types.Command

      Generate a Cypher query from the natural language question.

      Uses the text2cypher engine with few-shot examples to convert the
      user's question into a valid Cypher query for the database schema.

      :param state: Current state containing the user's question.

      :returns:     - cypher_statement: The generated Cypher query
                    - steps: Updated with "generate_query"
      :rtype: Command object with updates

      .. rubric:: Example

      >>> state = OverallState(question="Who directed Inception?")
      >>> command = agent.generate_query(state)
      >>> print(command.update["cypher_statement"])
      MATCH (p:Person)-[:DIRECTED]->(m:Movie {title: 'Inception'}) RETURN p.name

      .. note::

         The quality of generation depends heavily on the provided examples
         and their similarity to the user's question.


      .. autolink-examples:: generate_query
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the complete Graph DB RAG workflow.

      Configures the workflow graph with all nodes and edges, including
      conditional routing based on validation results. This method is
      called automatically during agent initialization.

      The workflow structure::

          START
            ↓
          check_domain_relevance
            ↓ (conditional)
          generate_query ← ─ ─ ─ ┐
            ↓                    │
          validate_query         │
            ↓ (conditional)     │
          correct_query ─ ─ ─ ─ ─┘
            ↓
          execute_query
            ↓
          generate_answer
            ↓
          END

      .. note::

         The workflow includes loops for query correction and multiple
         exit points for error handling.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: validate_query(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> langgraph.types.Command

      Validate the generated Cypher query against the database schema.

      Checks for syntax errors, schema mismatches, and logical issues in
      the generated query. Routes to correction if errors are found.

      :param state: Current state containing the Cypher statement to validate.

      :returns:     - next_action: "correct_cypher" if errors, "execute_query" if valid
                    - cypher_errors: List of validation errors (if any)
                    - steps: Updated with "validate_query"
      :rtype: Command object with updates

      .. rubric:: Example

      >>> state = OverallState(
      ...     cypher_statement="MATCH (p:Actor)-[:DIRECTED]->(m:Film) RETURN p.name"
      ... )
      >>> command = agent.validate_query(state)
      >>> # Would return errors about "Film" label and "Actor" directing

      .. note::

         Validation checks include label existence, property names,
         relationship types, and query completeness.


      .. autolink-examples:: validate_query
         :collapse:


   .. py:method:: validation_router(state: haive.agents.rag.db_rag.graph_db.state.OverallState) -> str

      Route based on query validation result.

      :param state: Current state with next_action field.

      :returns: Next node name - "correct_query", "execute_query", or END.
      :rtype: str

      .. note:: This is used as a conditional edge function in the workflow graph.


      .. autolink-examples:: validation_router
         :collapse:


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



.. py:class:: GuardrailsOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output for domain relevance checking.

   This model represents the decision on whether a query is relevant to
   the configured domain. It supports multiple categories within a domain.

   .. attribute:: decision

      The routing decision. Either "end" (not relevant) or one
      of the allowed categories (relevant to that category).

   .. attribute:: allowed_categories

      List of valid categories for the domain. The
      "end" option is always implicitly included.

   .. rubric:: Example

   >>> # Query about movies in a movie domain
   >>> output = GuardrailsOutput(
   ...     decision="movie",
   ...     allowed_categories=["movie", "actor", "director"]
   ... )

   >>> # Query not relevant to the domain
   >>> output = GuardrailsOutput(
   ...     decision="end",
   ...     allowed_categories=["movie", "actor", "director"]
   ... )

   .. note::

      The validate_decision method should be called after instantiation
      to ensure the decision is valid.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GuardrailsOutput
      :collapse:

   .. py:class:: Config

      Pydantic model configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:method:: validate_decision() -> None

      Validate that the decision is within allowed values.

      :raises ValueError: If the decision is not 'end' or in allowed_categories.

      .. rubric:: Example

      >>> output = GuardrailsOutput(decision="movie")
      >>> output.validate_decision()  # No error

      >>> output = GuardrailsOutput(decision="invalid")
      >>> output.validate_decision()  # Raises ValueError


      .. autolink-examples:: validate_decision
         :collapse:


   .. py:attribute:: allowed_categories
      :type:  list[str]
      :value: None



   .. py:attribute:: decision
      :type:  str
      :value: None



.. py:class:: InputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input state for the graph database agent.

   This class defines the initial input structure for queries to the
   Graph DB RAG agent. It contains only the user's natural language question.

   .. attribute:: question

      The user's natural language question to be converted to Cypher
      and executed against the Neo4j database.

   .. rubric:: Example

   >>> input_state = InputState(question="Who directed The Matrix?")
   >>> print(input_state.question)
   Who directed The Matrix?

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: InputState
      :collapse:

   .. py:attribute:: question
      :type:  str
      :value: None



.. py:class:: OutputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output state for the graph database agent.

   This class defines the final output structure returned by the Graph DB RAG
   agent after processing a query. It includes the answer, execution steps,
   and the generated Cypher statement.

   .. attribute:: answer

      The natural language answer generated from the query results.
      Defaults to empty string if no answer has been generated yet.

   .. attribute:: steps

      List of workflow steps executed during query processing.
      Useful for debugging and understanding the agent's reasoning.

   .. attribute:: cypher_statement

      The final Cypher query that was executed.
      Useful for learning and debugging purposes.

   .. rubric:: Example

   >>> output = OutputState(
   ...     answer="The Wachowskis directed The Matrix.",
   ...     steps=["check_domain", "generate_query", "execute_query"],
   ...     cypher_statement="MATCH (p:Person)-[:DIRECTED]->(m:Movie {title: 'The Matrix'}) RETURN p.name"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: OutputState
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: cypher_statement
      :type:  str
      :value: None



   .. py:attribute:: steps
      :type:  list[str]
      :value: None



.. py:class:: OverallState(/, **data: Any)

   Bases: :py:obj:`InputState`, :py:obj:`OutputState`


   Complete state for the graph database agent workflow.

   This class combines input and output states with additional fields needed
   for the internal workflow execution. It tracks the current state of query
   processing including errors, validation results, and database records.

   .. attribute:: next_action

      The next workflow step to execute. Used for routing
      decisions in the graph. Common values include:
      - "generate_query": Generate Cypher from natural language
      - "validate_query": Validate the generated Cypher
      - "correct_cypher": Fix errors in the Cypher statement
      - "execute_query": Run the query against Neo4j
      - "end": Terminate the workflow

   .. attribute:: cypher_errors

      List of validation errors found in the Cypher statement.
      Used by the correction step to fix issues.

   .. attribute:: database_records

      Records retrieved from the Neo4j database.
      Can be a list of dictionaries or a string message if no results.

   .. rubric:: Example

   >>> state = OverallState(
   ...     question="What are the top rated movies?",
   ...     next_action="generate_query",
   ...     cypher_statement="MATCH (m:Movie) RETURN m.title, m.rating ORDER BY m.rating DESC LIMIT 5",
   ...     database_records=[
   ...         {"m.title": "The Shawshank Redemption", "m.rating": 9.3},
   ...         {"m.title": "The Godfather", "m.rating": 9.2}
   ...     ]
   ... )

   .. note::

      This state is passed between all nodes in the workflow graph,
      accumulating information as the query is processed.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: OverallState
      :collapse:

   .. py:attribute:: cypher_errors
      :type:  list[str]
      :value: None



   .. py:attribute:: database_records
      :type:  list[dict]
      :value: None



   .. py:attribute:: next_action
      :type:  str
      :value: None



.. py:class:: PropertyFilter(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a filter condition on a node property in a Cypher query.

   This model captures property-based filtering conditions that appear in
   WHERE clauses or inline property matches in Cypher queries.

   .. attribute:: node_label

      The Neo4j label of the node being filtered (e.g., "Movie", "Person").

   .. attribute:: property_key

      The property name being filtered (e.g., "title", "year").

   .. attribute:: property_value

      The value to match against. Can be string, number, or boolean.

   .. attribute:: filter_type

      The comparison operator used. Defaults to equality.

   .. rubric:: Example

   >>> # Filter for movies released after 2020
   >>> filter = PropertyFilter(
   ...     node_label="Movie",
   ...     property_key="year",
   ...     property_value=2020,
   ...     filter_type=">"
   ... )

   >>> # Filter for person named "Keanu Reeves"
   >>> filter = PropertyFilter(
   ...     node_label="Person",
   ...     property_key="name",
   ...     property_value="Keanu Reeves"
   ... )

   :raises ValueError: If filter_type is not one of the valid operators.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyFilter
      :collapse:

   .. py:method:: validate_filter_type(v) -> Literal['=', '!=', '>', '<', '>=', '<='] | None
      :classmethod:


      Validate that the filter type is a supported operator.

      :param v: The filter type value to validate.

      :returns: The validated filter type.
      :rtype: str

      :raises ValueError: If the filter type is not supported.


      .. autolink-examples:: validate_filter_type
         :collapse:


   .. py:attribute:: filter_type
      :type:  Literal['=', '!=', '>', '<', '>=', '<='] | None
      :value: None



   .. py:attribute:: node_label
      :type:  str
      :value: None



   .. py:attribute:: property_key
      :type:  str
      :value: None



   .. py:attribute:: property_value
      :type:  Any | None
      :value: None



.. py:class:: ValidateCypherOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Validation result for a Cypher query.

   This model captures the results of validating a Cypher query against
   the database schema, including any errors found and filters detected.

   .. attribute:: is_valid

      Whether the Cypher query is valid and can be executed.

   .. attribute:: errors

      List of syntax or semantic errors found. Each error should
      explain what's wrong and potentially how to fix it.

   .. attribute:: filters

      List of property filters detected in the query. Useful for
      understanding what the query is filtering on.

   .. rubric:: Example

   >>> # Valid query result
   >>> result = ValidateCypherOutput(
   ...     is_valid=True,
   ...     errors=[],
   ...     filters=[PropertyFilter(
   ...         node_label="Movie",
   ...         property_key="year",
   ...         property_value=2023
   ...     )]
   ... )

   >>> # Invalid query result
   >>> result = ValidateCypherOutput(
   ...     is_valid=False,
   ...     errors=[
   ...         "Label 'Film' does not exist in schema. Did you mean 'Movie'?",
   ...         "Property 'release_date' does not exist for Movie. Use 'year' instead."
   ...     ]
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ValidateCypherOutput
      :collapse:

   .. py:attribute:: errors
      :type:  list[str] | None
      :value: None



   .. py:attribute:: filters
      :type:  list[PropertyFilter] | None
      :value: None



   .. py:attribute:: is_valid
      :type:  bool
      :value: None



.. py:function:: basic_example()

   Demonstrate basic usage of GraphDBRAGAgent.

   This example shows the simplest way to use the agent with default
   configuration. It relies on environment variables for Neo4j connection.

   Example Output:
       >>> basic_example()
       Basic GraphDB RAG Agent Example
       =====================================

       Question: What is the movie with the highest rating?

       Processing...
        Answer: The highest rated movie is "The Shawshank Redemption" with a rating of 9.3.

        Execution Details:
       - Cypher Query: MATCH (m:Movie) RETURN m.title, m.rating ORDER BY m.rating DESC LIMIT 1
       - Processing Time: 2.3 seconds
       - Steps: ['check_domain_relevance', 'generate_query', 'validate_query', 'execute_query', 'generate_answer']


   .. autolink-examples:: basic_example
      :collapse:

.. py:function:: batch_processing_example()

   Demonstrate batch processing of multiple queries.

   This example shows how to efficiently process multiple queries
   and collect statistics about the execution.

   Example Output:
       >>> batch_processing_example()
        Batch Processing Example
       =====================================

       Processing 5 queries...

       1. "What are the top 5 rated movies?"
           Success (2.1s)

       2. "Who acted in The Godfather?"
           Success (1.8s)

       3. "What's the weather?"
           Out of domain (0.5s)

        Batch Statistics:
       - Total Queries: 5
       - Successful: 4 (80%)
       - Failed: 1 (20%)
       - Average Time: 1.7s
       - Total Time: 8.5s


   .. autolink-examples:: batch_processing_example
      :collapse:

.. py:function:: check_domain_relevance(query: str, domain_categories: list = None) -> bool

   Check if a query is relevant to the specified domain.

   :param query: The query to check
   :param domain_categories: List of domain categories to check against

   :returns: True if the query is domain-relevant, False otherwise


   .. autolink-examples:: check_domain_relevance
      :collapse:

.. py:function:: correct_query(query: str, errors: list = None) -> str

   Correct a Cypher query based on provided errors.

   :param query: The original query
   :param errors: List of error messages

   :returns: Corrected query string


   .. autolink-examples:: correct_query
      :collapse:

.. py:function:: custom_domain_example()

   Demonstrate agent configuration for a custom domain.

   This example shows how to configure the agent for a specific domain
   with custom examples and categories.

   Example Output:
       >>> custom_domain_example()
        Custom Domain (Healthcare) Example
       =====================================

       Configuring agent for healthcare domain...

       Testing domain relevance:
       -  "Which patients have diabetes?" - Accepted
       -  "What's the weather today?" - Rejected (out of domain)

       Processing healthcare query...
       Answer: The following patients have been diagnosed with diabetes: John Smith, Mary Johnson, and Robert Williams.


   .. autolink-examples:: custom_domain_example
      :collapse:

.. py:function:: domain_router(query: str, domain_categories: list = None) -> str

   Route queries based on domain relevance.


   .. autolink-examples:: domain_router
      :collapse:

.. py:function:: error_handling_example()

   Demonstrate error handling and recovery strategies.

   This example shows how the agent handles various error conditions
   including invalid queries, connection issues, and schema mismatches.

   Example Output:
       >>> error_handling_example()
        Error Handling Example
       =====================================

       Testing various error scenarios...

       1. Invalid Cypher syntax:
          Initial query had errors: ['Syntax error at line 1']
           Successfully corrected and executed

       2. Non-existent labels:
            Handled gracefully: Label 'NonExistentNode' not in schema

       3. Complex nested query:
           Successfully validated and executed


   .. autolink-examples:: error_handling_example
      :collapse:

.. py:function:: execute_query(query: str, db_connection=None) -> dict

   Execute a Cypher query against the database.


   .. autolink-examples:: execute_query
      :collapse:

.. py:function:: generate_answer(query_results: dict, original_query: str = '') -> str

   Generate natural language answer from query results.


   .. autolink-examples:: generate_answer
      :collapse:

.. py:function:: generate_query(natural_language_query: str) -> str

   Generate Cypher query from natural language.


   .. autolink-examples:: generate_query
      :collapse:

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

.. py:function:: main()

   Run all examples with a menu interface.

   This function provides an interactive menu to run different examples
   demonstrating various features of the GraphDBRAGAgent.

   .. rubric:: Example

   Running the main function::

       $ python example.py

        GraphDB RAG Agent Examples
       =============================

       Select an example to run:
       1. Basic Usage
       2. Streaming Execution
       3. Custom Domain Configuration
       4. Batch Processing
       5. Error Handling
       6. Performance Monitoring
       7. Async Execution
       8. Run All Examples
       0. Exit

       Enter your choice (0-8):


   .. autolink-examples:: main
      :collapse:

.. py:function:: performance_monitoring_example()

   Demonstrate performance monitoring and optimization.

   This example shows how to monitor agent performance and identify
   bottlenecks in the workflow.

   Example Output:
       >>> performance_monitoring_example()
        Performance Monitoring Example
       =====================================

       Running performance analysis...

        Performance Metrics:

       Step                    | Time (s) | % of Total
       -------------------------|----------|------------
       check_domain_relevance   |   0.3    |   12%
       generate_query           |   1.2    |   48%
       validate_query           |   0.4    |   16%
       execute_query            |   0.3    |   12%
       generate_answer          |   0.3    |   12%
       -------------------------|----------|------------
       Total                    |   2.5    |   100%

        Optimization Suggestions:
       - Query generation is the bottleneck (48% of time)
       - Consider caching frequent queries
       - Use more specific examples for faster generation


   .. autolink-examples:: performance_monitoring_example
      :collapse:

.. py:function:: run_all_examples()

   Run all examples in sequence.

   This function executes all example functions to demonstrate
   the full capabilities of the GraphDBRAGAgent.


   .. autolink-examples:: run_all_examples
      :collapse:

.. py:function:: setup_workflow()

   Set up the graph DB RAG workflow.


   .. autolink-examples:: setup_workflow
      :collapse:

.. py:function:: streaming_example()

   Demonstrate streaming execution with progress tracking.

   This example shows how to use the streaming interface to monitor
   the agent's progress through each step of the workflow.

   Example Output:
       >>> streaming_example()
        Streaming GraphDB RAG Agent Example
       =====================================

       Question: Who directed The Matrix?

        Step: check_domain_relevance
           Domain check passed

        Step: generate_query
           Generated Cypher: MATCH (p:Person)-[:DIRECTED]->(m:Movie {title: 'The Matrix'}) RETURN p.name

        Step: validate_query
           Query validation passed

        Step: execute_query
           Query executed successfully
           Results: [{'p.name': 'Lana Wachowski'},
               {'p.name': 'Lilly Wachowski'}]

        Step: generate_answer
           Final answer generated

        Final Answer: The Matrix was directed by Lana Wachowski and Lilly Wachowski.


   .. autolink-examples:: streaming_example
      :collapse:

.. py:function:: validate_cypher_syntax(query: str) -> bool

   Validate Cypher query syntax.

   :param query: Cypher query string to validate

   :returns: True if syntax is valid, False otherwise


   .. autolink-examples:: validate_cypher_syntax
      :collapse:

.. py:function:: validate_decision(decision: str, allowed_values: list[str]) -> bool

   Validate decision against allowed values.

   :param decision: Decision value to validate
   :param allowed_values: List of allowed decision values

   :returns: True if decision is valid, False otherwise


   .. autolink-examples:: validate_decision
      :collapse:

.. py:function:: validate_engines(engines: dict) -> bool

   Validate that all required engines are properly configured.

   :param engines: Dictionary of engine configurations

   :returns: True if all engines are valid, False otherwise


   .. autolink-examples:: validate_engines
      :collapse:

.. py:function:: validate_filter_type(filter_type: str) -> bool

   Validate filter type for property filtering.

   :param filter_type: Filter type to validate

   :returns: True if filter type is valid, False otherwise


   .. autolink-examples:: validate_filter_type
      :collapse:

.. py:function:: validate_query(query: str, schema: dict = None) -> dict

   Validate a Cypher query against database schema.


   .. autolink-examples:: validate_query
      :collapse:

.. py:function:: validation_router(validation_result: dict) -> str

   Route based on validation results.


   .. autolink-examples:: validation_router
      :collapse:

