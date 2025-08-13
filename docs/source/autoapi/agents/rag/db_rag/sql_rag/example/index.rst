
:py:mod:`agents.rag.db_rag.sql_rag.example`
===========================================

.. py:module:: agents.rag.db_rag.sql_rag.example

Example usage of SQL RAG Agent.

from typing import Union
This module demonstrates various usage patterns for the SQL RAG Agent,
from basic queries to advanced configurations. It includes examples for
different database types, error handling, and customization options.

Running the Examples:
    Basic example::

        $ python example.py

    With specific database::

        $ SQL_DB_TYPE=mysql SQL_DB_NAME=mydb python example.py

    With custom query::

        $ python example.py --query "Show me top products by revenue"

Examples Included:
    1. Basic usage with default configuration
    2. PostgreSQL with specific tables
    3. SQLite with local file
    4. MySQL with authentication
    5. Complex queries with joins
    6. Error handling and validation
    7. Custom LLM engines
    8. Batch processing

.. note::

   Ensure you have proper database credentials configured either
   through environment variables or in the code before running.


.. autolink-examples:: agents.rag.db_rag.sql_rag.example
   :collapse:


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.sql_rag.example.basic_example
   agents.rag.db_rag.sql_rag.example.batch_processing_example
   agents.rag.db_rag.sql_rag.example.custom_llm_example
   agents.rag.db_rag.sql_rag.example.error_handling_example
   agents.rag.db_rag.sql_rag.example.interactive_mode
   agents.rag.db_rag.sql_rag.example.main
   agents.rag.db_rag.sql_rag.example.mysql_example
   agents.rag.db_rag.sql_rag.example.postgresql_example
   agents.rag.db_rag.sql_rag.example.sqlite_example

.. py:function:: basic_example() -> dict[str, Any]

   Run a basic example with default configuration.

   This example demonstrates the simplest usage of the SQL RAG Agent
   with minimal configuration, relying on environment variables.

   :returns: Query result including answer and SQL used.
   :rtype: Dict[str, Any]

   Example Output:
       >>> result = basic_example()
       ✅ Connected to postgresql database
       >>> print(result["answer"])
       'The database contains the following tables: customers, orders, products...'


   .. autolink-examples:: basic_example
      :collapse:

.. py:function:: batch_processing_example() -> list[dict[str, Any]]

   Example of processing multiple queries in batch.

   This example shows how to efficiently process multiple queries
   using the same agent instance, with performance timing.

   :returns: Results for all queries.
   :rtype: List[Dict[str, Any]]

   .. rubric:: Example

   >>> results = batch_processing_example()
   Processing 5 queries...
   Query 1: ✓ (1.2s)
   Query 2: ✓ (0.8s)
   ...
   Total time: 5.5s, Average: 1.1s per query


   .. autolink-examples:: batch_processing_example
      :collapse:

.. py:function:: custom_llm_example() -> dict[str, Any]

   Example with custom LLM configuration.

   This example demonstrates how to customize the LLM engines
   used for different steps in the workflow.

   :returns: Query result using custom LLM configuration.
   :rtype: Dict[str, Any]

   .. rubric:: Example

   >>> result = custom_llm_example()
   Using custom LLM configuration...
   >>> print(result["answer"])
   'Based on the analysis with custom temperature settings...'


   .. autolink-examples:: custom_llm_example
      :collapse:

.. py:function:: error_handling_example() -> None

   Demonstrate error handling and validation features.

   This example shows how the agent handles various error conditions
   including invalid queries, non-existent tables, and SQL errors.

   .. rubric:: Example

   >>> error_handling_example()
   Testing error handling...
   Query 1 - Invalid domain: This question is not about database...
   Query 2 - SQL error corrected successfully
   Query 3 - No results found: The database doesn't contain any orders...


   .. autolink-examples:: error_handling_example
      :collapse:

.. py:function:: interactive_mode() -> None

   Run the agent in interactive mode.

   This function starts an interactive session where users can
   continuously ask questions about the database.

   .. rubric:: Example

   >>> interactive_mode()
   SQL RAG Agent - Interactive Mode
   Type 'exit' to quit, 'help' for commands

   SQL> What tables do we have?
   Answer: The database contains tables: customers, orders, products...

   SQL> Show me total sales
   Answer: Total sales amount to $1,234,567...

   SQL> exit
   Goodbye!


   .. autolink-examples:: interactive_mode
      :collapse:

.. py:function:: main() -> int | float

   Main function to run examples.

   This function provides a command-line interface for running
   different examples or custom queries.

   Command-line Arguments:
       --example: Which example to run (basic, postgresql, sqlite, mysql, error, custom, batch, interactive)
       --query: Custom query to run
       --config: Path to JSON config file

   .. rubric:: Examples

   Run basic example::

       $ python example.py --example basic

   Run custom query::

       $ python example.py --query "Show me revenue by product category"

   Run interactive mode::

       $ python example.py --example interactive

   Use custom config::

       $ python example.py --config my_config.json --query "Top customers"


   .. autolink-examples:: main
      :collapse:

.. py:function:: mysql_example() -> dict[str, Any]

   Example with MySQL database and authentication.

   This example shows MySQL configuration with full authentication
   and custom few-shot examples for better SQL generation.

   :returns: Query result from MySQL database.
   :rtype: Dict[str, Any]

   .. rubric:: Example

   >>> result = mysql_example()
   Connecting to MySQL database...
   ✅ Connected to mysql database
   >>> print(result["answer"])
   'Product sales trend shows 15% growth...'


   .. autolink-examples:: mysql_example
      :collapse:

.. py:function:: postgresql_example() -> dict[str, Any]

   Example with PostgreSQL configuration and specific tables.

   This example shows how to configure the agent for a PostgreSQL
   database with specific table inclusion and custom domain settings.

   :returns: Query result from PostgreSQL database.
   :rtype: Dict[str, Any]

   .. rubric:: Example

   >>> result = postgresql_example()
   Configuring PostgreSQL connection...
   ✅ Connected to postgresql database
   >>> print(result["answer"])
   'Your top 5 customers by total order value are...'


   .. autolink-examples:: postgresql_example
      :collapse:

.. py:function:: sqlite_example() -> dict[str, Any]

   Example with SQLite database file.

   This example demonstrates using a local SQLite database file,
   which is useful for development and testing.

   :returns: Query result from SQLite database.
   :rtype: Dict[str, Any]

   .. rubric:: Example

   >>> result = sqlite_example()
   Using SQLite database: ./data/sample.db
   ✅ Connected to sqlite database
   >>> print(result["answer"])
   'The total number of active users is 1,234...'


   .. autolink-examples:: sqlite_example
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.sql_rag.example
   :collapse:
   
.. autolink-skip:: next
