agents.rag.db_rag.graph_db.agent
================================

.. py:module:: agents.rag.db_rag.graph_db.agent

.. autoapi-nested-parse::

   Graph Database RAG Agent implementation.

   This module implements the main Graph Database RAG Agent that provides natural
   language querying capabilities for Neo4j databases. The agent uses a multi-step
   workflow to convert questions to Cypher queries, validate them, execute them,
   and generate natural language responses.

   The agent workflow consists of the following steps:
       1. **Domain Relevance Check**: Validates if the query is within the configured domain
       2. **Query Generation**: Converts natural language to Cypher using few-shot learning
       3. **Query Validation**: Checks the Cypher query against the database schema
       4. **Query Correction**: Fixes any errors found during validation
       5. **Query Execution**: Runs the validated query against Neo4j
       6. **Answer Generation**: Converts database results to natural language

   .. rubric:: Example

   Basic usage of the Graph DB RAG Agent::

       >>> from haive.agents.rag.db_rag.graph_db import GraphDBRAGAgent, GraphDBRAGConfig
       >>>
       >>> # Configure the agent for a movie domain
       >>> config = GraphDBRAGConfig(
       ...     domain_name="movies",
       ...     domain_categories=["movie", "actor", "director"],
       ...     graph_db_config=GraphDBConfig(
       ...         graph_db_uri="bolt://localhost:7687",
       ...         graph_db_user="neo4j",
       ...         graph_db_password="password"
       ...     )
       ... )
       >>>
       >>> # Create and use the agent
       >>> agent = GraphDBRAGAgent(config)
       >>> result = agent.invoke({"question": "Who directed The Matrix?"})
       >>> print(result["answer"])
       The Wachowskis directed The Matrix.

   Using the agent with streaming::

       >>> # Stream the workflow execution
       >>> for chunk in agent.stream({"question": "What are the top 5 rated movies?"}):
       ...     if "answer" in chunk:
       ...         print(chunk["answer"])

   .. note::

      The agent requires a connection to a Neo4j database and uses environment
      variables for configuration if not explicitly provided.

   .. seealso::

      - :class:`GraphDBRAGConfig`: Configuration options for the agent
      - :class:`OverallState`: State management during workflow execution
      - :mod:`haive.agents.rag.db_rag.graph_db.engines`: LLM engines used by the agent


   .. autolink-examples:: agents.rag.db_rag.graph_db.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.graph_db.agent.GraphDBRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.agent.check_domain_relevance
   agents.rag.db_rag.graph_db.agent.correct_query
   agents.rag.db_rag.graph_db.agent.domain_router
   agents.rag.db_rag.graph_db.agent.execute_query
   agents.rag.db_rag.graph_db.agent.generate_answer
   agents.rag.db_rag.graph_db.agent.generate_query
   agents.rag.db_rag.graph_db.agent.setup_workflow
   agents.rag.db_rag.graph_db.agent.validate_query
   agents.rag.db_rag.graph_db.agent.validation_router


Module Contents
---------------

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

.. py:function:: domain_router(query: str, domain_categories: list = None) -> str

   Route queries based on domain relevance.


   .. autolink-examples:: domain_router
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

.. py:function:: setup_workflow()

   Set up the graph DB RAG workflow.


   .. autolink-examples:: setup_workflow
      :collapse:

.. py:function:: validate_query(query: str, schema: dict = None) -> dict

   Validate a Cypher query against database schema.


   .. autolink-examples:: validate_query
      :collapse:

.. py:function:: validation_router(validation_result: dict) -> str

   Route based on validation results.


   .. autolink-examples:: validation_router
      :collapse:

