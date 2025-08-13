
:py:mod:`agents.rag.agentic.query_rewriter`
===========================================

.. py:module:: agents.rag.agentic.query_rewriter

Query Rewriting Agent for Agentic RAG.

This agent rewrites queries to improve retrieval using existing models from common.


.. autolink-examples:: agents.rag.agentic.query_rewriter
   :collapse:


Functions
---------

.. autoapisummary::

   agents.rag.agentic.query_rewriter.create_query_rewriter_agent
   agents.rag.agentic.query_rewriter.rewrite_query

.. py:function:: create_query_rewriter_agent(name: str = 'query_rewriter', temperature: float = 0.7, **kwargs) -> haive.agents.simple.SimpleAgent

   Create a query rewriter agent using direct SimpleAgent instantiation.

   :param name: Agent name (default: "query_rewriter")
   :param temperature: LLM temperature (default: 0.7 for creativity)
   :param \*\*kwargs: Additional configuration options

   :returns: SimpleAgent configured for query refinement

   .. rubric:: Example

   .. code-block:: python

       # Create query rewriter agent
       rewriter = create_query_rewriter_agent(
       name="query_rewriter",
       temperature=0.7
       )

       # Rewrite a query
       result = await rewriter.arun({
       "query": "quantum computing basics"
       })

       # Access results
       print(f"Original: {result.original_query}")
       print(f"Best rewrite: {result.best_refined_query}")
       for suggestion in result.refinement_suggestions:
       print(f"- {suggestion.refined_query} ({suggestion.improvement_type})")


   .. autolink-examples:: create_query_rewriter_agent
      :collapse:

.. py:function:: rewrite_query(agent: haive.agents.simple.SimpleAgent, query: str, context: str = '') -> haive.agents.rag.common.query_refinement.models.QueryRefinementResponse
   :async:


   Rewrite a query to improve retrieval.

   :param agent: The query rewriter agent
   :param query: The original query to rewrite
   :param context: Optional context to help with rewriting

   :returns: QueryRefinementResponse with refinement suggestions


   .. autolink-examples:: rewrite_query
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic.query_rewriter
   :collapse:
   
.. autolink-skip:: next
