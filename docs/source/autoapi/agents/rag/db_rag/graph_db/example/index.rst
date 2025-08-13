
:py:mod:`agents.rag.db_rag.graph_db.example`
============================================

.. py:module:: agents.rag.db_rag.graph_db.example

Example usage of the Graph Database RAG Agent.

This module demonstrates various ways to use the GraphDBRAGAgent for querying
Neo4j databases with natural language. It includes basic usage, advanced
configurations, error handling, and different execution modes.

The examples cover:
    - Basic agent usage with default configuration
    - Custom domain configuration
    - Streaming execution with progress tracking
    - Batch query processing
    - Error handling and debugging
    - Performance monitoring

To run these examples:
    1. Ensure Neo4j is running and accessible
    2. Set environment variables for Neo4j connection
    3. Run: python example.py

.. rubric:: Example

Basic execution::

    $ export NEO4J_URI="bolt://localhost:7687"
    $ export NEO4J_USER="neo4j"
    $ export NEO4J_PASSWORD="your-password"
    $ python example.py

.. note::

   These examples assume you have a Neo4j database with movie data.
   Adjust the queries and domain configuration for your specific use case.


.. autolink-examples:: agents.rag.db_rag.graph_db.example
   :collapse:


Functions
---------

.. autoapisummary::

   agents.rag.db_rag.graph_db.example.async_example
   agents.rag.db_rag.graph_db.example.basic_example
   agents.rag.db_rag.graph_db.example.batch_processing_example
   agents.rag.db_rag.graph_db.example.custom_domain_example
   agents.rag.db_rag.graph_db.example.error_handling_example
   agents.rag.db_rag.graph_db.example.main
   agents.rag.db_rag.graph_db.example.performance_monitoring_example
   agents.rag.db_rag.graph_db.example.run_all_examples
   agents.rag.db_rag.graph_db.example.streaming_example

.. py:function:: async_example()
   :async:


   Demonstrate asynchronous execution of the agent.

   This example shows how to use the agent asynchronously for
   better performance in async applications.

   Example Output:
       >>> asyncio.run(async_example())
        Async Execution Example
       =====================================

       Processing 3 queries concurrently...

        Query 1 completed: "What are the top rated movies?"
        Query 2 completed: "Who directed The Godfather?"
        Query 3 completed: "Which actors have won an Oscar?"

       Total time: 2.8s (vs ~7s sequential)


   .. autolink-examples:: async_example
      :collapse:

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.db_rag.graph_db.example
   :collapse:
   
.. autolink-skip:: next
