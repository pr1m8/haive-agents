
:py:mod:`agents.rag.db_rag.graph_db`
====================================

.. py:module:: agents.rag.db_rag.graph_db

Module exports.


.. autolink-examples:: agents.rag.db_rag.graph_db
   :collapse:

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Config:

   .. graphviz::
      :align: center

      digraph inheritance_Config {
        node [shape=record];
        "Config" [label="Config"];
        "pydantic.BaseModel" -> "Config";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.Config
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CypherQueryOutput:

   .. graphviz::
      :align: center

      digraph inheritance_CypherQueryOutput {
        node [shape=record];
        "CypherQueryOutput" [label="CypherQueryOutput"];
        "pydantic.BaseModel" -> "CypherQueryOutput";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.CypherQueryOutput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExampleConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ExampleConfig {
        node [shape=record];
        "ExampleConfig" [label="ExampleConfig"];
        "pydantic.BaseModel" -> "ExampleConfig";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.ExampleConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphDBConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GraphDBConfig {
        node [shape=record];
        "GraphDBConfig" [label="GraphDBConfig"];
        "pydantic.BaseModel" -> "GraphDBConfig";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.GraphDBConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphDBRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GraphDBRAGAgent {
        node [shape=record];
        "GraphDBRAGAgent" [label="GraphDBRAGAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.rag.db_rag.graph_db.config.GraphDBRAGConfig]" -> "GraphDBRAGAgent";
      }

.. autoclass:: agents.rag.db_rag.graph_db.GraphDBRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphDBRAGConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GraphDBRAGConfig {
        node [shape=record];
        "GraphDBRAGConfig" [label="GraphDBRAGConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "GraphDBRAGConfig";
      }

.. autoclass:: agents.rag.db_rag.graph_db.GraphDBRAGConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GuardrailsOutput:

   .. graphviz::
      :align: center

      digraph inheritance_GuardrailsOutput {
        node [shape=record];
        "GuardrailsOutput" [label="GuardrailsOutput"];
        "pydantic.BaseModel" -> "GuardrailsOutput";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.GuardrailsOutput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for InputState:

   .. graphviz::
      :align: center

      digraph inheritance_InputState {
        node [shape=record];
        "InputState" [label="InputState"];
        "pydantic.BaseModel" -> "InputState";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.InputState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for OutputState:

   .. graphviz::
      :align: center

      digraph inheritance_OutputState {
        node [shape=record];
        "OutputState" [label="OutputState"];
        "pydantic.BaseModel" -> "OutputState";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.OutputState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for OverallState:

   .. graphviz::
      :align: center

      digraph inheritance_OverallState {
        node [shape=record];
        "OverallState" [label="OverallState"];
        "InputState" -> "OverallState";
        "OutputState" -> "OverallState";
      }

.. autoclass:: agents.rag.db_rag.graph_db.OverallState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PropertyFilter:

   .. graphviz::
      :align: center

      digraph inheritance_PropertyFilter {
        node [shape=record];
        "PropertyFilter" [label="PropertyFilter"];
        "pydantic.BaseModel" -> "PropertyFilter";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.PropertyFilter
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ValidateCypherOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ValidateCypherOutput {
        node [shape=record];
        "ValidateCypherOutput" [label="ValidateCypherOutput"];
        "pydantic.BaseModel" -> "ValidateCypherOutput";
      }

.. autopydantic_model:: agents.rag.db_rag.graph_db.ValidateCypherOutput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.graph_db
   :collapse:
   
.. autolink-skip:: next
