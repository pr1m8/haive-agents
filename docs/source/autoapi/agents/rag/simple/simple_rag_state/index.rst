agents.rag.simple.simple_rag_state
==================================

.. py:module:: agents.rag.simple.simple_rag_state

.. autoapi-nested-parse::

   SimpleRAG - Proper MultiAgentState Implementation.

   This is the CORRECT SimpleRAG implementation following the working pattern from the guides:
   - Use MultiAgentState (not MultiAgent class inheritance)
   - Use create_agent_node_v3() for execution
   - Direct field updates through structured outputs
   - Sequential execution: retriever → generator

   Architecture:
       SimpleRAGState extends MultiAgentState
       agents = [BaseRAGAgent, SimpleAgent]
       Sequential execution via nodes: retriever_node → generator_node
       Direct field access: state.documents, state.answer

   .. rubric:: Examples

   Basic usage::

       from haive.agents.rag.simple.simple_rag_state import SimpleRAGState, create_simple_rag_workflow

       # Create the complete workflow
       state = create_simple_rag_workflow(
           query="What is machine learning?",
           vector_store=your_vector_store,
           top_k=5
       )

       # Execute sequential workflow
       result = await execute_simple_rag(state)

       # Access results directly
       print(f"Answer: {result.answer}")
       print(f"Sources: {result.sources}")


   .. autolink-examples:: agents.rag.simple.simple_rag_state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.simple.simple_rag_state.AnswerGeneration
   agents.rag.simple.simple_rag_state.DocumentRetrieval
   agents.rag.simple.simple_rag_state.SimpleRAGState


Functions
---------

.. autoapisummary::

   agents.rag.simple.simple_rag_state.create_rag_agents
   agents.rag.simple.simple_rag_state.create_simple_rag_workflow
   agents.rag.simple.simple_rag_state.display_rag_results
   agents.rag.simple.simple_rag_state.execute_simple_rag
   agents.rag.simple.simple_rag_state.get_rag_summary
   agents.rag.simple.simple_rag_state.run_simple_rag


Module Contents
---------------

.. py:class:: AnswerGeneration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from the answer generation agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnswerGeneration
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



.. py:class:: DocumentRetrieval(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from the document retrieval agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentRetrieval
      :collapse:

   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: query_processed
      :type:  str
      :value: None



   .. py:attribute:: retrieved_count
      :type:  int
      :value: None



.. py:class:: SimpleRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`


   State schema for SimpleRAG workflow using MultiAgentState pattern.

   This follows the working pattern from the guides:
   - Extends MultiAgentState for proper agent management
   - Contains all input and output fields as direct attributes
   - Agents update fields directly through structured outputs
   - No complex nested structures - just clean, direct field access

   Flow:
       1. Input: query, configuration
       2. Retriever updates: documents, retrieved_count, query_processed
       3. Generator updates: answer, sources, confidence
       4. Direct access: state.answer, state.sources, etc.


   .. autolink-examples:: SimpleRAGState
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: query_processed
      :type:  str
      :value: None



   .. py:attribute:: rag_workflow_id
      :type:  str
      :value: None



   .. py:attribute:: retrieved_count
      :type:  int
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



   .. py:attribute:: top_k
      :type:  int
      :value: None



.. py:function:: create_rag_agents(vector_store_config: haive.core.engine.vectorstore.VectorStoreConfig, llm_config: haive.core.engine.aug_llm.AugLLMConfig, structured_output_model: type[pydantic.BaseModel] | None = None) -> tuple[haive.agents.rag.base.agent.BaseRAGAgent, haive.agents.simple.agent.SimpleAgent]

   Create the retriever and generator agents for SimpleRAG.

   :param vector_store_config: Configuration for the vector store
   :param llm_config: Configuration for the LLM
   :param structured_output_model: Optional custom output model for generator

   :returns: Tuple of (retriever_agent, generator_agent)


   .. autolink-examples:: create_rag_agents
      :collapse:

.. py:function:: create_simple_rag_workflow(query: str, vector_store_config: haive.core.engine.vectorstore.VectorStoreConfig, llm_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, top_k: int = 5, structured_output_model: type[pydantic.BaseModel] | None = None, workflow_id: str = '') -> SimpleRAGState

   Create a complete SimpleRAG workflow state.

   :param query: The query to process
   :param vector_store_config: Vector store configuration
   :param llm_config: LLM configuration (uses default if None)
   :param top_k: Number of documents to retrieve
   :param structured_output_model: Optional custom output model
   :param workflow_id: Unique workflow identifier

   :returns: Initialized SimpleRAGState ready for execution


   .. autolink-examples:: create_simple_rag_workflow
      :collapse:

.. py:function:: display_rag_results(state: SimpleRAGState) -> None

   Display SimpleRAG results in a formatted way.

   :param state: Completed SimpleRAGState with results


   .. autolink-examples:: display_rag_results
      :collapse:

.. py:function:: execute_simple_rag(state: SimpleRAGState, debug: bool = False) -> SimpleRAGState
   :async:


   Execute the complete SimpleRAG workflow.

   This follows the working pattern from the guides:
   - Sequential execution using create_agent_node_v3()
   - Direct field updates through structured outputs
   - Clean, simple execution flow

   :param state: The SimpleRAGState to execute
   :param debug: Enable debug logging

   :returns: Updated state with all results populated


   .. autolink-examples:: execute_simple_rag
      :collapse:

.. py:function:: get_rag_summary(state: SimpleRAGState) -> dict[str, Any]

   Get a summary of the RAG execution.

   :param state: Completed SimpleRAGState

   :returns: Dictionary with execution summary


   .. autolink-examples:: get_rag_summary
      :collapse:

.. py:function:: run_simple_rag(query: str, vector_store_config: haive.core.engine.vectorstore.VectorStoreConfig, llm_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, top_k: int = 5, debug: bool = False) -> SimpleRAGState

   Synchronous wrapper for SimpleRAG execution.

   :param query: The query to process
   :param vector_store_config: Vector store configuration
   :param llm_config: LLM configuration
   :param top_k: Number of documents to retrieve
   :param debug: Enable debug logging

   :returns: Completed SimpleRAGState with results


   .. autolink-examples:: run_simple_rag
      :collapse:

