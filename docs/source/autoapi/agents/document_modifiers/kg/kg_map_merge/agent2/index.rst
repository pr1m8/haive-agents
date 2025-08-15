agents.document_modifiers.kg.kg_map_merge.agent2
================================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.agent2


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.agent2.StructuredKGAgent


Module Contents
---------------

.. py:class:: StructuredKGAgent(config: haive.agents.document_modifiers.kg.kg_map_merge.config.ParallelKGAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.document_modifiers.kg.kg_map_merge.config.ParallelKGAgentConfig`\ ]


   An agent that builds a knowledge graph using structured output models.

   This agent:
   1. Extracts schema (node types, relationship types) from content
   2. Processes documents in parallel to extract graph fragments
   3. Merges the graph fragments into a unified knowledge graph

   Uses structured Pydantic models for all extraction and merging steps.

   Initialize the knowledge graph agent with structured output processing.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructuredKGAgent
      :collapse:

   .. py:method:: collect_merged(state: dict)

      Collect a merged graph result.
      Updates the main state with the latest merge result.


      .. autolink-examples:: collect_merged
         :collapse:


   .. py:method:: continue_merging(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Update merged results list with latest merge result.
      Decide whether to continue merging or finalize.


      .. autolink-examples:: continue_merging
         :collapse:


   .. py:method:: distribute_documents(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Set up the state for parallel document processing.


      .. autolink-examples:: distribute_documents
         :collapse:


   .. py:method:: distribute_graph_document_pairs(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Collect results from the parallel document processing.
      Updates the main state with the processed graph documents.


      .. autolink-examples:: distribute_graph_document_pairs
         :collapse:


   .. py:method:: extract_schema(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)
      :async:


      Extracts node and relationship types from the content using structured output.


      .. autolink-examples:: extract_schema
         :collapse:


   .. py:method:: finalize_graph(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Finalize the merged graph and extract valuable statistics.


      .. autolink-examples:: finalize_graph
         :collapse:


   .. py:method:: initialize_workflow(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Initial node that determines whether schema extraction is needed.
      Returns a Command directing to the appropriate next node.


      .. autolink-examples:: initialize_workflow
         :collapse:


   .. py:method:: map_documents(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Map function that creates Send commands for each document to be processed.
      Returns a list of Send objects - one for each document.


      .. autolink-examples:: map_documents
         :collapse:


   .. py:method:: map_merge_pairs(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Map function for merge pairs, creating Send commands for each pair.
      Returns a list of Send objects for parallel merging.


      .. autolink-examples:: map_merge_pairs
         :collapse:


   .. py:method:: merge_pair(state: dict)
      :async:


      Merge a pair of graph documents using structured output.


      .. autolink-examples:: merge_pair
         :collapse:


   .. py:method:: process_document(state: dict)
      :async:


      Process a single document to extract a knowledge graph fragment.
      Uses structured output model to directly get KGExtraction object.


      .. autolink-examples:: process_document
         :collapse:


   .. py:method:: route_after_collection(state: haive.agents.document_modifiers.kg.kg_map_merge.state.ParallelKGState)

      Determine next steps after document collection.
      Returns the appropriate node name for routing.


      .. autolink-examples:: route_after_collection
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow for the structured knowledge graph agent.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: graph_transformer


   .. py:attribute:: kg_extraction_chain


   .. py:attribute:: llm_graph_transformer


   .. py:attribute:: merge_analysis_chain


   .. py:attribute:: schema_extraction_chain


