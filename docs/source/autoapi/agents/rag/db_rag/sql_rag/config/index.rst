agents.rag.db_rag.sql_rag.config
================================

.. py:module:: agents.rag.db_rag.sql_rag.config

.. autoapi-nested-parse::

   Configuration module for SQL RAG Agent.

   This module provides configuration classes for setting up SQL database connections
   and agent behavior. It supports multiple database types and includes extensive
   customization options for the agent workflow.

   .. rubric:: Example

   Basic PostgreSQL configuration::

       >>> from haive.agents.rag.db_rag.sql_rag.config import SQLRAGConfig, SQLDatabaseConfig
       >>>
       >>> # Configure database connection
       >>> db_config = SQLDatabaseConfig(
       ...     db_type="postgresql",
       ...     db_host="localhost",
       ...     db_name="sales_db",
       ...     db_user="admin",
       ...     db_password="secure_password",
       ...     include_tables=["orders", "customers", "products"]
       ... )
       >>>
       >>> # Configure agent
       >>> agent_config = SQLRAGConfig(
       ...     domain_name="sales",
       ...     db_config=db_config,
       ...     hallucination_check=True,
       ...     max_iterations=3
       ... )

   .. note::

      Database credentials can be provided through environment variables
      for security. See SQLDatabaseConfig for supported variables.


   .. autolink-examples:: agents.rag.db_rag.sql_rag.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.config.SQLAgentConfig


Classes
-------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.config.SQLDatabaseConfig
   agents.rag.db_rag.sql_rag.config.SQLRAGConfig


Module Contents
---------------

.. py:class:: SQLDatabaseConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for SQL database connections.

   This class handles connection details for various SQL database types
   including PostgreSQL, MySQL, SQLite, and MS SQL Server. Credentials
   can be provided directly or through environment variables.

   .. attribute:: db_type

      Database type - postgresql, mysql, sqlite, mssql.

      :type: str

   .. attribute:: db_uri

      Complete connection URI if provided directly.

      :type: Optional[str]

   .. attribute:: db_user

      Database username (env: SQL_DB_USER).

      :type: str

   .. attribute:: db_password

      Database password (env: SQL_DB_PASSWORD).

      :type: str

   .. attribute:: db_host

      Database host (env: SQL_DB_HOST).

      :type: str

   .. attribute:: db_port

      Database port (env: SQL_DB_PORT).

      :type: str

   .. attribute:: db_name

      Database name (env: SQL_DB_NAME).

      :type: str

   .. attribute:: include_tables

      Tables to include (None = all).

      :type: Optional[List[str]]

   .. attribute:: exclude_tables

      Tables to exclude from queries.

      :type: List[str]

   .. attribute:: sample_rows_in_table_info

      Sample rows to show in schema.

      :type: int

   .. attribute:: custom_query

      Custom query for schema retrieval.

      :type: Optional[str]

   .. rubric:: Example

   Using environment variables::

       >>> # Set environment variables:
       >>> # SQL_DB_TYPE=postgresql
       >>> # SQL_DB_HOST=localhost
       >>> # SQL_DB_NAME=mydb
       >>> # SQL_DB_USER=user
       >>> # SQL_DB_PASSWORD=pass
       >>>
       >>> config = SQLDatabaseConfig()
       >>> db = config.get_sql_db()
       ✅ Connected to postgresql database

   Direct configuration::

       >>> config = SQLDatabaseConfig(
       ...     db_type="mysql",
       ...     db_host="mysql.example.com",
       ...     db_port="3306",
       ...     db_name="analytics",
       ...     db_user="analyst",
       ...     db_password="secure_pass",
       ...     include_tables=["sales", "customers"]
       ... )

   Using connection URI::

       >>> config = SQLDatabaseConfig(
       ...     db_uri="sqlite:///path/to/database.db"
       ... )

   .. note::

      For SQLite databases, db_name should be the file path.
      For other databases, ensure the appropriate driver is installed:
      - PostgreSQL: psycopg2
      - MySQL: pymysql
      - MS SQL: pyodbc

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SQLDatabaseConfig
      :collapse:

   .. py:method:: get_connection_string() -> str

      Generate a connection string based on the database type.

      :returns: Properly formatted connection string for the database.
      :rtype: str

      :raises ValueError: If the database type is not supported.

      .. rubric:: Example

      >>> config = SQLDatabaseConfig(
      ...     db_type="postgresql",
      ...     db_user="user",
      ...     db_password="pass",
      ...     db_host="localhost",
      ...     db_port="5432",
      ...     db_name="mydb"
      ... )
      >>> print(config.get_connection_string())
      'postgresql+psycopg2://user:pass@localhost:5432/mydb'


      .. autolink-examples:: get_connection_string
         :collapse:


   .. py:method:: get_db_schema() -> dict[str, Any]

      Retrieve the schema and basic table info from the database.

      :returns:

                Dictionary containing:
                    - tables: List of table names
                    - dialect: SQL dialect being used
                    - table_info: Dictionary of table schemas
      :rtype: Dict[str, Any]

      .. rubric:: Example

      >>> config = SQLDatabaseConfig(db_uri="sqlite:///sales.db")
      >>> schema = config.get_db_schema()
      >>> print(f"Database dialect: {schema['dialect']}")
      Database dialect: sqlite
      >>> print(f"Tables: {', '.join(schema['tables'])}")
      Tables: customers, orders, products


      .. autolink-examples:: get_db_schema
         :collapse:


   .. py:method:: get_sql_db() -> langchain_community.utilities.SQLDatabase | None

      Create and return a SQLDatabase object for interacting with the database.

      :returns: Connected database object or None if connection fails.
      :rtype: Optional[SQLDatabase]

      .. rubric:: Example

      >>> config = SQLDatabaseConfig(db_uri="sqlite:///test.db")
      >>> db = config.get_sql_db()
      ✅ Connected to sqlite database at sqlite:///test.db
      >>> tables = db.get_usable_table_names()
      >>> print(f"Found {len(tables)} tables")
      Found 5 tables

      .. note::

         The method handles backward compatibility for different versions
         of langchain_community.utilities.SQLDatabase.


      .. autolink-examples:: get_sql_db
         :collapse:


   .. py:attribute:: custom_query
      :type:  str | None
      :value: None



   .. py:attribute:: db_host
      :type:  str
      :value: None



   .. py:attribute:: db_name
      :type:  str
      :value: None



   .. py:attribute:: db_password
      :type:  str
      :value: None



   .. py:attribute:: db_port
      :type:  str
      :value: None



   .. py:attribute:: db_type
      :type:  str
      :value: None



   .. py:attribute:: db_uri
      :type:  str | None
      :value: None



   .. py:attribute:: db_user
      :type:  str
      :value: None



   .. py:attribute:: exclude_tables
      :type:  list[str]
      :value: None



   .. py:attribute:: include_tables
      :type:  list[str] | None
      :value: None



   .. py:attribute:: sample_rows_in_table_info
      :type:  int
      :value: None



.. py:class:: SQLRAGConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the SQL RAG Agent.

   This class configures the behavior of the SQL RAG agent including
   database connection, LLM engines, validation settings, and workflow
   parameters.

   .. attribute:: engines

      LLM engines for each workflow step.

      :type: Dict[str, AugLLMConfig]

   .. attribute:: llm_config

      Default LLM configuration.

      :type: LLMConfig

   .. attribute:: domain_name

      Domain specialization (e.g., "sales", "inventory").

      :type: str

   .. attribute:: domain_categories

      Valid categories for domain routing.

      :type: List[str]

   .. attribute:: state_schema

      State schema class for the agent.

      :type: Any

   .. attribute:: db_config

      Database connection configuration.

      :type: SQLDatabaseConfig

   .. attribute:: input_schema

      Input schema for agent invocation.

      :type: Any

   .. attribute:: output_schema

      Output schema for agent results.

      :type: Any

   .. attribute:: hallucination_check

      Enable hallucination detection.

      :type: bool

   .. attribute:: answer_grading

      Enable answer quality grading.

      :type: bool

   .. attribute:: examples_path

      Path to few-shot examples JSON.

      :type: Optional[str]

   .. attribute:: domain_examples

      Few-shot examples.

      :type: Dict[str, List[Dict[str, str]]]

   .. attribute:: max_iterations

      Maximum SQL correction attempts.

      :type: int

   .. rubric:: Example

   Complete configuration example::

       >>> config = SQLRAGConfig(
       ...     domain_name="e-commerce",
       ...     domain_categories=["sales", "inventory", "customers"],
       ...     db_config=SQLDatabaseConfig(
       ...         db_type="postgresql",
       ...         db_name="ecommerce_db",
       ...         include_tables=["orders", "products", "customers"]
       ...     ),
       ...     hallucination_check=True,
       ...     answer_grading=True,
       ...     max_iterations=3,
       ...     domain_examples={
       ...         "e-commerce": [
       ...             {
       ...                 "question": "Top selling products",
       ...                 "query": "SELECT p.name, SUM(oi.quantity) as sold FROM products p JOIN order_items oi ON p.id = oi.product_id GROUP BY p.id ORDER BY sold DESC LIMIT 10"
       ...             }
       ...         ]
       ...     }
       ... )

   Using custom engines::

       >>> from haive.core.engine.aug_llm import AugLLMConfig
       >>>
       >>> custom_engines = {
       ...     "generate_sql": AugLLMConfig(
       ...         name="custom_sql_generator",
       ...         temperature=0.1,  # Lower temperature for SQL
       ...         model="gpt-4"
       ...     ),
       ...     **default_sql_engines  # Keep other defaults
       >>> }
       >>>
       >>> config = SQLRAGConfig(
       ...     engines=custom_engines,
       ...     domain_name="analytics"
       ... )

   :raises ValueError: If required engines are missing from configuration.


   .. autolink-examples:: SQLRAGConfig
      :collapse:

   .. py:method:: check_required_engines(v: dict[str, haive.core.engine.aug_llm.AugLLMConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :classmethod:


      Validate that all required engines are present.

      :param v: Dictionary of engine configurations.

      :returns: Validated engine configurations.
      :rtype: Dict[str, AugLLMConfig]

      :raises ValueError: If any required engines are missing.


      .. autolink-examples:: check_required_engines
         :collapse:


   .. py:attribute:: answer_grading
      :type:  bool
      :value: None



   .. py:attribute:: db_config
      :type:  SQLDatabaseConfig
      :value: None



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



   .. py:attribute:: examples_path
      :type:  str | None
      :value: None



   .. py:attribute:: hallucination_check
      :type:  bool
      :value: None



   .. py:attribute:: input_schema
      :type:  Any
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: output_schema
      :type:  Any
      :value: None



   .. py:attribute:: state_schema
      :type:  Any
      :value: None



.. py:data:: SQLAgentConfig

