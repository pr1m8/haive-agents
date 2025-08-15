agents.rag.db_rag.sql_rag.agent
===============================

.. py:module:: agents.rag.db_rag.sql_rag.agent

.. autoapi-nested-parse::

   SQL RAG Agent for natural language database querying.

   This module implements a sophisticated SQL Retrieval-Augmented Generation (RAG) agent
   that enables natural language querying of SQL databases. The agent uses a multi-step
   workflow to analyze queries, generate SQL, validate results, and produce accurate answers.

   .. rubric:: Example

   Basic usage of the SQL RAG Agent::

       >>> from haive.agents.rag.db_rag.sql_rag import SQLRAGAgent, SQLRAGConfig
       >>>
       >>> # Create configuration
       >>> config = SQLRAGConfig(
       ...     domain_name="sales",
       ...     db_config=SQLDatabaseConfig(
       ...         db_type="postgresql",
       ...         db_name="sales_db"
       ...     )
       ... )
       >>>
       >>> # Initialize agent
       >>> agent = SQLRAGAgent(config)
       >>>
       >>> # Query the database
       >>> result = agent.invoke({
       ...     "question": "What were the total sales last quarter?"
       ... })
       >>> print(result["answer"])
       'Total sales last quarter were $1.2M across 450 transactions...'

   .. attribute:: logger

      Module-level logger for debugging and monitoring.

      :type: logging.Logger

   .. note::

      This agent requires proper database credentials and connection details
      to be configured either through environment variables or explicit configuration.


   .. autolink-examples:: agents.rag.db_rag.sql_rag.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.agent.SQLRAGAgent


Module Contents
---------------

.. py:class:: SQLRAGAgent(config: haive.agents.rag.db_rag.sql_rag.config.SQLRAGConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.rag.db_rag.sql_rag.config.SQLRAGConfig`\ ]


   SQL RAG Agent for querying SQL databases with natural language.

   This agent implements a sophisticated workflow for converting natural language
   questions into SQL queries, executing them safely, and generating accurate
   natural language responses. The workflow includes:

   1. **Domain Relevance Check**: Validates if the query is database-related
   2. **Schema Retrieval**: Gets relevant database schema information
   3. **Query Analysis**: Determines required tables, columns, and operations
   4. **SQL Generation**: Creates syntactically correct SQL from natural language
   5. **Validation & Correction**: Ensures SQL is safe and correct
   6. **Execution**: Runs the query safely with proper error handling
   7. **Answer Generation**: Produces natural language answers from results

   .. attribute:: sql_db

      Connected database instance

      :type: SQLDatabase

   .. attribute:: db_schema

      Complete database schema information

      :type: Dict[str, Any]

   .. attribute:: dialect

      SQL dialect being used (postgresql, mysql, etc.)

      :type: str

   .. attribute:: toolkit

      LangChain SQL toolkit instance

      :type: SQLDatabaseToolkit

   .. attribute:: tools

      Available database tools

      :type: List[BaseTool]

   .. attribute:: tool_nodes

      Tool nodes for workflow

      :type: Dict[str, ToolNode]

   .. attribute:: engines

      LLM engines for each step

      :type: Dict[str, AugLLMConfig]

   .. rubric:: Example

   Creating and using a SQL RAG Agent::

       >>> # Configure for a PostgreSQL database
       >>> config = SQLRAGConfig(
       ...     domain_name="e-commerce",
       ...     db_config=SQLDatabaseConfig(
       ...         db_type="postgresql",
       ...         db_host="localhost",
       ...         db_name="shop_db",
       ...         include_tables=["orders", "products", "customers"]
       ...     ),
       ...     hallucination_check=True,
       ...     max_iterations=3
       ... )
       >>>
       >>> # Create agent
       >>> agent = SQLRAGAgent(config)
       >>>
       >>> # Ask questions in natural language
       >>> response = agent.invoke({
       ...     "question": "Which products had the highest sales last month?"
       ... })
       >>>
       >>> # Access results
       >>> print(f"Answer: {response['answer']}")
       >>> print(f"SQL Used: {response['sql_statement']}")

   .. note::

      The agent includes safety features like SQL validation, hallucination
      detection, and query result verification to ensure accurate responses.

   Initialize the SQL RAG Agent with the given configuration.

   :param config: Configuration object containing database
                  connection details, LLM settings, and workflow parameters.
   :type config: SQLRAGConfig

   :raises ValueError: If database connection fails or required engines
       are missing from the configuration.

   .. rubric:: Example

   >>> config = SQLRAGConfig(
   ...     db_config=SQLDatabaseConfig(db_uri="sqlite:///sales.db")
   ... )
   >>> agent = SQLRAGAgent(config)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SQLRAGAgent
      :collapse:

   .. py:method:: _initialize_config(config: haive.agents.rag.db_rag.sql_rag.config.SQLRAGConfig) -> None

      Initialize the configuration and components.

      This method sets up the database connection, explores the schema,
      creates necessary tools, and configures all LLM engines.

      :param config: The configuration object to initialize from.
      :type config: SQLRAGConfig

      :raises ValueError: If database connection fails or is invalid.

      .. note::

         This method is called automatically during agent initialization
         and should not be called directly.


      .. autolink-examples:: _initialize_config
         :collapse:


   .. py:method:: analyze_query(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Analyze the query to determine relevant tables and fields.

      This method uses an LLM to understand the user's natural language
      question and identify which database tables, columns, joins, and
      aggregations will be needed to answer it.

      :param state: Current state containing the question
                    and schema information.
      :type state: OverallState

      :returns:

                Update command with query analysis including:
                    - relevant_tables: Tables needed for the query
                    - needed_columns: Specific columns to select
                    - constraints: WHERE clause conditions
                    - aggregations: GROUP BY/aggregate functions needed
                    - joins_needed: Required table joins
      :rtype: Command

      .. rubric:: Example

      Analyzing a complex query::

          >>> state = OverallState(
          ...     question="Show me top 5 customers by total order value"
          ... )
          >>> command = agent.analyze_query(state)
          >>> analysis = command.update["query_analysis"]
          >>> print(analysis.relevant_tables)
          ['customers', 'orders', 'order_items']
          >>> print(analysis.aggregations)
          ['SUM(order_items.price * order_items.quantity)']

      .. note::

         The analysis helps the SQL generation step create more accurate
         queries by understanding the semantic intent.


      .. autolink-examples:: analyze_query
         :collapse:


   .. py:method:: check_domain_relevance(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Determine if the query is relevant to databases.

      This method uses a guardrails LLM to check if the user's question
      is about querying the database or if it's an unrelated question
      that should be rejected.

      :param state: Current state containing the question.
      :type state: OverallState

      :returns:

                Update command with next_action set to either
                    'end' (if irrelevant) or continue to schema retrieval.
      :rtype: Command

      .. rubric:: Example

      >>> state = OverallState(question="What tables are in the database?")
      >>> command = agent.check_domain_relevance(state)
      >>> print(command.update["next_action"])
      'retrieve_schema'

      .. note::

         Questions like "What's the weather?" or "Tell me a joke" will
         be rejected with an appropriate message.


      .. autolink-examples:: check_domain_relevance
         :collapse:


   .. py:method:: correct_query(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Correct the SQL query based on validation errors.

      This method takes a query with validation errors and attempts to
      fix them, learning from the specific issues identified.

      :param state: Current state containing the invalid query
                    and the list of errors.
      :type state: OverallState

      :returns:

                Update command with corrected SQL query and instruction
                    to re-validate.
      :rtype: Command

      .. rubric:: Example

      Correcting a query with a missing GROUP BY::

          >>> state = OverallState(
          ...     sql_query="SELECT category, SUM(amount) FROM sales",
          ...     sql_errors=["Missing GROUP BY clause for 'category'"]
          ... )
          >>> command = agent.correct_query(state)
          >>> print(command.update["sql_query"])
          'SELECT category, SUM(amount) FROM sales GROUP BY category'

      .. note::

         The correction process may iterate multiple times based on the
         max_iterations configuration setting.


      .. autolink-examples:: correct_query
         :collapse:


   .. py:method:: domain_router(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> str

      Route based on domain relevance check.

      :param state: Current state with next_action field.
      :type state: OverallState

      :returns: Next node name - either END or "retrieve_schema".
      :rtype: str


      .. autolink-examples:: domain_router
         :collapse:


   .. py:method:: execute_query(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Execute the SQL query against the database.

      This method safely executes the validated SQL query and captures
      the results. It includes error handling and timeout protection.

      :param state: Current state containing the validated
                    SQL query to execute.
      :type state: OverallState

      :returns: Update command with query results or error message.
      :rtype: Command

      .. rubric:: Example

      Executing a query and handling results::

          >>> state = OverallState(
          ...     sql_query="SELECT COUNT(*) as total FROM orders"
          ... )
          >>> command = agent.execute_query(state)
          >>> print(command.update["query_result"])
          'total\n-----\n1234'

      .. warning::

         Only SELECT queries are executed. Any DML operations (INSERT,
         UPDATE, DELETE) are rejected during validation.


      .. autolink-examples:: execute_query
         :collapse:


   .. py:method:: generate_answer(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Generate the final answer based on the query results.

      This method converts the raw SQL query results into a natural
      language answer that directly addresses the user's question.
      It includes optional hallucination checking to ensure accuracy.

      :param state: Current state containing the question,
                    SQL query, and query results.
      :type state: OverallState

      :returns:

                Update command with the final answer and optional
                    hallucination check results.
      :rtype: Command

      .. rubric:: Example

      Generating an answer with hallucination checking::

          >>> state = OverallState(
          ...     question="Who is our top customer?",
          ...     query_result="customer_name | total_spent\\n-----------\\nAcme Corp | 50000"
          ... )
          >>> command = agent.generate_answer(state)
          >>> print(command.update["answer"])
          'Your top customer is Acme Corp with total spending of $50,000.'
          >>> print(command.update["hallucination_check"])
          'no'  # No hallucinations detected

      .. note::

         If hallucination checking is enabled and detects issues, a
         warning is appended to the answer.


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: generate_query(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Generate an SQL query from the natural language question.

      This method converts the user's natural language question into
      a syntactically correct SQL query, using the analysis results
      and database schema information.

      :param state: Current state containing question,
                    schema, and query analysis.
      :type state: OverallState

      :returns:

                Update command with the generated SQL query,
                    formatted for readability.
      :rtype: Command

      .. rubric:: Example

      SQL generation from natural language::

          >>> state = OverallState(
          ...     question="What were the total sales by category last month?"
          ... )
          >>> command = agent.generate_query(state)
          >>> print(command.update["sql_query"])
          '''
          SELECT
              c.category_name,
              SUM(oi.quantity * oi.price) as total_sales
          FROM categories c
          JOIN products p ON c.category_id = p.category_id
          JOIN order_items oi ON p.product_id = oi.product_id
          JOIN orders o ON oi.order_id = o.order_id
          WHERE o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)
          GROUP BY c.category_name
          ORDER BY total_sales DESC
          '''

      .. note::

         The method includes special handling for metadata queries like
         "what tables are in the database" that don't require complex SQL.


      .. autolink-examples:: generate_query
         :collapse:


   .. py:method:: retrieve_schema(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Retrieve database schema information for context.

      This method gathers detailed schema information about all relevant
      tables in the database, including column names, types, and relationships.

      :param state: Current state of the workflow.
      :type state: OverallState

      :returns:

                Update command with schema information and instruction
                    to proceed to query analysis.
      :rtype: Command

      .. rubric:: Example

      Schema retrieval for a sales database::

          >>> state = OverallState(question="Show me all orders")
          >>> command = agent.retrieve_schema(state)
          >>> schema_info = command.update["schema_info"]
          >>> print(f"Found {len(schema_info)} tables")
          Found 5 tables

      .. note::

         For large databases, this method limits schema retrieval to the
         first 10 tables to avoid overwhelming the LLM context.


      .. autolink-examples:: retrieve_schema
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the SQL RAG workflow graph.

      This method constructs the workflow graph with all necessary nodes
      and edges, including conditional routing based on validation results.

      The workflow follows this path:
      1. START -> check_domain_relevance
      2. Domain routing (end if irrelevant)
      3. retrieve_schema -> analyze_query -> generate_query
      4. validate_query with correction loop if needed
      5. execute_query -> generate_answer -> END

      .. note::

         This method is called automatically during agent initialization
         and should not be called directly.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: validate_query(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> langgraph.types.Command

      Validate the SQL query for syntax and schema correctness.

      This method performs comprehensive validation of the generated SQL
      including syntax checking, table/column name verification, join
      validation, and security checks.

      :param state: Current state containing the SQL query
                    to validate.
      :type state: OverallState

      :returns:

                Update command with either:
                    - next_action="execute_query" if valid
                    - next_action="correct_query" if errors found
                    - sql_errors list containing any validation errors
      :rtype: Command

      .. rubric:: Example

      Validating a query with an error::

          >>> state = OverallState(
          ...     sql_query="SELECT * FROM non_existent_table"
          ... )
          >>> command = agent.validate_query(state)
          >>> print(command.update["sql_errors"])
          ["Table 'non_existent_table' does not exist in the schema"]
          >>> print(command.update["next_action"])
          'correct_query'

      .. note::

         The validation prevents SQL injection and ensures only safe
         SELECT queries are executed.


      .. autolink-examples:: validate_query
         :collapse:


   .. py:method:: validation_router(state: haive.agents.rag.db_rag.sql_rag.state.OverallState) -> str

      Route based on query validation results.

      :param state: Current state with next_action field.
      :type state: OverallState

      :returns: Next node name - END, "correct_query", or "execute_query".
      :rtype: str


      .. autolink-examples:: validation_router
         :collapse:


.. py:data:: logger

