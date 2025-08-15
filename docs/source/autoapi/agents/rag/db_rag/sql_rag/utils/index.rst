agents.rag.db_rag.sql_rag.utils
===============================

.. py:module:: agents.rag.db_rag.sql_rag.utils

.. autoapi-nested-parse::

   Utility functions for SQL RAG Agent.

   This module provides helper functions for database operations, toolkit creation,
   error handling, and schema exploration. These utilities support the main agent
   workflow with reusable functionality.

   .. rubric:: Example

   Creating SQL toolkit::

       >>> from haive.agents.rag.db_rag.sql_rag.utils import create_sql_toolkit
       >>> from haive.agents.rag.db_rag.sql_rag.config import SQLDatabaseConfig
       >>>
       >>> db_config = SQLDatabaseConfig(db_uri="sqlite:///example.db")
       >>> toolkit = create_sql_toolkit(db_config)
       >>> tools = toolkit.get_tools()
       >>> print(f"Available tools: {[tool.name for tool in tools]}")
       Available tools: ['sql_db_query', 'sql_db_schema', 'sql_db_list_tables', ...]


   .. autolink-examples:: agents.rag.db_rag.sql_rag.utils
      :collapse:


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.utils.create_sql_toolkit
   agents.rag.db_rag.sql_rag.utils.create_tool_node_with_fallback
   agents.rag.db_rag.sql_rag.utils.explore_database_schema
   agents.rag.db_rag.sql_rag.utils.get_all_toolkit_tools
   agents.rag.db_rag.sql_rag.utils.handle_tool_error


Module Contents
---------------

.. py:function:: create_sql_toolkit(db_config: haive.agents.rag.db_rag.sql_rag.config.SQLDatabaseConfig, llm_config: haive.core.engine.aug_llm.AugLLMConfig | haive.core.models.llm.base.LLMConfig | None = None) -> langchain_community.agent_toolkits.SQLDatabaseToolkit

   Create a SQL Database Toolkit using the provided configuration.

   This function creates a LangChain SQLDatabaseToolkit that provides
   various tools for interacting with SQL databases including query
   execution, schema inspection, and table listing.

   :param db_config: Configuration for the SQL database connection.
   :type db_config: SQLDatabaseConfig
   :param llm_config: Configuration for the LLM to use
                      with the toolkit. If None, defaults to OpenAI GPT-4.
   :type llm_config: Optional[AugLLMConfig]

   :returns: Configured toolkit instance with database tools.
   :rtype: SQLDatabaseToolkit

   :raises ValueError: If database connection fails or is invalid.

   .. rubric:: Example

   Creating toolkit with custom LLM::

       >>> from haive.core.engine.aug_llm import AugLLMConfig
       >>>
       >>> llm_config = AugLLMConfig(
       ...     model="gpt-4",
       ...     temperature=0.1  # Low temperature for SQL generation
       ... )
       >>>
       >>> toolkit = create_sql_toolkit(db_config, llm_config)
       >>>
       >>> # Use toolkit to query schema
       >>> schema_tool = next(t for t in toolkit.get_tools() if t.name == "sql_db_schema")
       >>> schema = schema_tool.invoke({"table_names": "customers"})


   .. autolink-examples:: create_sql_toolkit
      :collapse:

.. py:function:: create_tool_node_with_fallback(tools: langchain_core.tools.BaseTool | list[langchain_core.tools.BaseTool]) -> langchain_core.runnables.RunnableWithFallbacks

   Create a ToolNode with a fallback to handle errors gracefully.

   This function wraps tools in a ToolNode with error handling that
   surfaces errors back to the agent for correction rather than failing.

   :param tools: Tool or list of tools
                 to create a node for.
   :type tools: Union[BaseTool, List[BaseTool]]

   :returns: ToolNode wrapped with fallback error handling.
   :rtype: RunnableWithFallbacks

   .. rubric:: Example

   >>> query_tool = toolkit.get_tool("sql_db_query")
   >>> safe_tool_node = create_tool_node_with_fallback(query_tool)
   >>>
   >>> # If query fails, error is captured and returned
   >>> result = safe_tool_node.invoke({
   ...     "messages": [AIMessage(tool_calls=[{"name": "sql_db_query", "args": {"query": "INVALID SQL"}}])]
   ... })


   .. autolink-examples:: create_tool_node_with_fallback
      :collapse:

.. py:function:: explore_database_schema(db: langchain_community.utilities.SQLDatabase) -> dict[str, Any]

   Explore the database schema thoroughly to get comprehensive information.

   This function performs a deep exploration of the database schema,
   including tables, columns, sample data, and potential relationships.
   It's used to provide context for SQL generation.

   :param db: SQLDatabase instance to explore.
   :type db: SQLDatabase

   :returns:

             Detailed schema information including:
                 - tables: List of table names
                 - table_info: Detailed schema for each table
                 - table_samples: Sample rows from each table
                 - relationships: Detected foreign key relationships
                 - dialect: SQL dialect being used
   :rtype: Dict[str, Any]

   .. rubric:: Example

   >>> db = SQLDatabase.from_uri("sqlite:///northwind.db")
   >>> schema_info = explore_database_schema(db)
   >>>
   >>> print(f"Found {len(schema_info['tables'])} tables")
   Found 8 tables
   >>>
   >>> print(f"Dialect: {schema_info['dialect']}")
   Dialect: sqlite
   >>>
   >>> # Show detected relationships
   >>> for rel in schema_info['relationships']:
   ...     print(f"{rel['from_table']}.{rel['column']} -> {rel['to_table']}")
   orders.customer_id -> customers
   order_details.product_id -> products

   .. note::

      Relationship detection uses heuristics based on naming conventions
      and may not catch all foreign keys. For production use, consider
      querying database metadata directly.


   .. autolink-examples:: explore_database_schema
      :collapse:

.. py:function:: get_all_toolkit_tools(toolkit: langchain_community.agent_toolkits.SQLDatabaseToolkit) -> list[langchain_core.tools.BaseTool]

   Get all tools from a SQLDatabaseToolkit.

   :param toolkit: The toolkit instance to extract tools from.
   :type toolkit: SQLDatabaseToolkit

   :returns: List of all available tools in the toolkit.
   :rtype: List[BaseTool]

   .. rubric:: Example

   >>> toolkit = create_sql_toolkit(db_config)
   >>> tools = get_all_toolkit_tools(toolkit)
   >>> for tool in tools:
   ...     print(f"Tool: {tool.name} - {tool.description}")
   Tool: sql_db_query - Execute a SQL query against the database
   Tool: sql_db_schema - Get the schema of specific tables
   Tool: sql_db_list_tables - List all tables in the database


   .. autolink-examples:: get_all_toolkit_tools
      :collapse:

.. py:function:: handle_tool_error(state: dict[str, Any]) -> dict[str, Any]

   Handle tool execution errors by surfacing them to the agent.

   This function processes tool execution errors and formats them
   for the agent to understand and potentially correct.

   :param state: Current state with error information.
   :type state: Dict[str, Any]

   :returns: Modified state with formatted error messages.
   :rtype: Dict[str, Any]

   .. rubric:: Example

   >>> state = {
   ...     "error": ValueError("Table 'users' does not exist"),
   ...     "messages": [AIMessage(tool_calls=[{"id": "123", "name": "sql_db_query"}])]
   ... }
   >>> result = handle_tool_error(state)
   >>> print(result["messages"][0].content)
   'Error: ValueError("Table \'users\' does not exist")\\nPlease fix your mistakes.'


   .. autolink-examples:: handle_tool_error
      :collapse:

