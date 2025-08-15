agents.rag.self_corr.agent
==========================

.. py:module:: agents.rag.self_corr.agent


Attributes
----------

.. autoapisummary::

   agents.rag.self_corr.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.self_corr.agent.SelfCorrectiveRAGAgent


Module Contents
---------------

.. py:class:: SelfCorrectiveRAGAgent(config: haive.agents.rag.self_corr.config.SelfCorrectiveRAGConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.rag.self_corr.config.SelfCorrectiveRAGConfig`\ ]


   RAG agent with self-correction capabilities.

   This agent implements a workflow that:
   1. Retrieves relevant documents for a query
   2. Filters documents based on relevance
   3. Generates an initial answer
   4. Evaluates the answer quality and checks for hallucinations
   5. Corrects the answer if issues are found
   6. Iterates until quality threshold is met or max iterations reached

   Initialize the agent with self-correction capabilities.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelfCorrectiveRAGAgent
      :collapse:

   .. py:method:: _initialize_components(config)

      Initialize all components for the agent.


      .. autolink-examples:: _initialize_components
         :collapse:


   .. py:method:: correct_answer(state: haive.agents.rag.self_corr.state.SelfCorrectiveRAGState) -> langgraph.types.Command

      Correct the answer based on evaluation feedback.

      :param state: Current state with query, answer, evaluation, and documents

      :returns: Command with corrected answer


      .. autolink-examples:: correct_answer
         :collapse:


   .. py:method:: correction_router(state: haive.agents.rag.self_corr.state.SelfCorrectiveRAGState) -> str

      Route based on evaluation results.


      .. autolink-examples:: correction_router
         :collapse:


   .. py:method:: evaluate_answer(state: haive.agents.rag.self_corr.state.SelfCorrectiveRAGState) -> langgraph.types.Command

      Evaluate the quality of the generated answer and check for hallucinations.

      :param state: Current state with query, answer, and documents

      :returns: Command with evaluation results


      .. autolink-examples:: evaluate_answer
         :collapse:


   .. py:method:: filter_documents(state: haive.agents.rag.self_corr.state.SelfCorrectiveRAGState) -> langgraph.types.Command

      Filter documents based on relevance to the query.

      :param state: Current state with query and retrieved documents

      :returns: Command with filtered documents


      .. autolink-examples:: filter_documents
         :collapse:


   .. py:method:: finalize_answer(state: haive.agents.rag.self_corr.state.SelfCorrectiveRAGState) -> langgraph.types.Command

      Prepare the final answer, possibly adding citations or formatting.

      :param state: Current state with final answer

      :returns: Command with finalized answer


      .. autolink-examples:: finalize_answer
         :collapse:


   .. py:method:: generate_answer(state: haive.agents.rag.self_corr.state.SelfCorrectiveRAGState) -> langgraph.types.Command

      Generate an initial answer based on filtered documents.

      :param state: Current state with query and filtered documents

      :returns: Command with generated answer


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: retrieve_documents(state: haive.agents.rag.self_corr.state.SelfCorrectiveRAGState) -> langgraph.types.Command

      Retrieve documents based on the query.

      :param state: Current state with query

      :returns: Command with retrieved documents


      .. autolink-examples:: retrieve_documents
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the self-corrective RAG workflow.

      Workflow:
      START → retrieve_documents → filter_documents → generate_answer → evaluate_answer
           → [correct_answer → evaluate_answer] (loop) → finalize_answer → END


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:property:: retriever
      :type: Any


      Lazy-loaded retriever property.

      .. autolink-examples:: retriever
         :collapse:


.. py:data:: logger

