
:py:mod:`agents.rag.agentic.document_grader`
============================================

.. py:module:: agents.rag.agentic.document_grader

Document Grading Agent for Agentic RAG.

This agent evaluates retrieved documents for relevance using existing models from common.


.. autolink-examples:: agents.rag.agentic.document_grader
   :collapse:


Functions
---------

.. autoapisummary::

   agents.rag.agentic.document_grader.create_document_grader_agent
   agents.rag.agentic.document_grader.grade_documents

.. py:function:: create_document_grader_agent(name: str = 'document_grader', temperature: float = 0.0, **kwargs) -> haive.agents.simple.SimpleAgent

   Create a document grader agent using direct SimpleAgent instantiation.

   :param name: Agent name (default: "document_grader")
   :param temperature: LLM temperature (default: 0.0 for consistency)
   :param \*\*kwargs: Additional configuration options

   :returns: SimpleAgent configured for document grading

   .. rubric:: Example

   .. code-block:: python

       # Create grader agent
       grader = create_document_grader_agent(
       name="doc_grader",
       temperature=0.0
       )

       # Grade documents
       result = await grader.arun({
       "query": "What is quantum computing?",
       "documents": [
       {"content": "Quantum computing uses quantum mechanics...", "id": "doc1"},
       {"content": "Classical computing uses binary digits...", "id": "doc2"}
       ]
       })

       # Access results
       for decision in result.document_decisions:
       print(f"Document {decision.document_id}: {decision.decision}")
       print(f"Reason: {decision.justification}")


   .. autolink-examples:: create_document_grader_agent
      :collapse:

.. py:function:: grade_documents(agent: haive.agents.simple.SimpleAgent, query: str, documents: list[dict[str, Any]]) -> haive.agents.rag.common.document_graders.models.DocumentBinaryResponse
   :async:


   Grade documents for relevance to a query.

   :param agent: The document grader agent
   :param query: The user query
   :param documents: List of documents with 'content' and 'id' fields

   :returns: DocumentBinaryResponse with grading results


   .. autolink-examples:: grade_documents
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic.document_grader
   :collapse:
   
.. autolink-skip:: next
