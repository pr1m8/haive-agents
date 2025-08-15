agents.document_modifiers.tnt.agent
===================================

.. py:module:: agents.document_modifiers.tnt.agent

.. autoapi-nested-parse::

   Taxonomy generation agent implementation.

   from typing import Any, Dict, Optional
   This module implements an agent that generates taxonomies from conversation histories
   through an iterative process of document summarization, clustering, and refinement.
   It uses LLM-based processing at each step to generate high-quality taxonomies.

   The agent follows these main steps:
   1. Document summarization
   2. Minibatch creation
   3. Initial taxonomy generation
   4. Iterative taxonomy refinement
   5. Final taxonomy review

   .. rubric:: Example

   Basic usage of the taxonomy agent::

       config = TaxonomyAgentConfig(
           state_schema=TaxonomyGenerationState,
           visualize=True,
           name="TaxonomyAgent"
       )
       agent = TaxonomyAgent(config)
       result = agent.run(input_data={"documents": [...]})


   .. autolink-examples:: agents.document_modifiers.tnt.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_modifiers.tnt.agent.TaxonomyAgent
   agents.document_modifiers.tnt.agent.TaxonomyAgentConfig


Module Contents
---------------

.. py:class:: TaxonomyAgent(config: TaxonomyAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`TaxonomyAgentConfig`\ ]


   Agent that generates a taxonomy from a conversation history.

   Initialize the taxonomy agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaxonomyAgent
      :collapse:

   .. py:method:: _setup_map_reduce_chain()

      Sets up the map-reduce chain for summarization.


      .. autolink-examples:: _setup_map_reduce_chain
         :collapse:


   .. py:method:: generate_taxonomy(state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState, config: langchain_core.runnables.RunnableConfig) -> haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState

      Generates an initial taxonomy from the first document minibatch.

      :param state: The current state of the taxonomy process.
      :type state: TaxonomyGenerationState
      :param config: Configuration for the taxonomy generation.
      :type config: RunnableConfig

      :returns: Updated state with the initial taxonomy.
      :rtype: TaxonomyGenerationState


      .. autolink-examples:: generate_taxonomy
         :collapse:


   .. py:method:: get_content(state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState)

      Extracts document content for processing.


      .. autolink-examples:: get_content
         :collapse:


   .. py:method:: get_minibatches(state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState, config: langchain_core.runnables.RunnableConfig)

      Splits documents into minibatches for iterative taxonomy generation.

      :param state: The current state containing documents.
      :type state: TaxonomyGenerationState
      :param config: Configuration object specifying batch size.
      :type config: RunnableConfig

      :returns: Dictionary with a 'minibatches' key containing grouped document indices.
      :rtype: dict


      .. autolink-examples:: get_minibatches
         :collapse:


   .. py:method:: invoke_taxonomy_chain(chain_config: haive.core.engine.aug_llm.AugLLMConfig, state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState, config: langchain_core.runnables.RunnableConfig, mb_indices: list[int]) -> haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState

      Invokes the taxonomy LLM to generate or refine taxonomies.

      :param chain: LLM pipeline for taxonomy generation.
      :type chain: Runnable
      :param state: Current taxonomy state.
      :type state: TaxonomyGenerationState
      :param config: Configurable parameters.
      :type config: RunnableConfig
      :param mb_indices: Indices of documents to process in this iteration.
      :type mb_indices: List[int]

      :returns: Updated state with new taxonomy clusters.
      :rtype: TaxonomyGenerationState


      .. autolink-examples:: invoke_taxonomy_chain
         :collapse:


   .. py:method:: reduce_summaries(combined: dict) -> haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState

      Reduces summarized documents into a structured format.


      .. autolink-examples:: reduce_summaries
         :collapse:


   .. py:method:: review_taxonomy(state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState, config: langchain_core.runnables.RunnableConfig) -> haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState

      Evaluates the final taxonomy after all updates.

      :param state: The current state with completed taxonomies.
      :type state: TaxonomyGenerationState
      :param config: Configuration settings.
      :type config: RunnableConfig

      :returns: Updated state with reviewed taxonomy.
      :rtype: TaxonomyGenerationState


      .. autolink-examples:: review_taxonomy
         :collapse:


   .. py:method:: setup_workflow() -> None

      Sets up the taxonomy generation workflow in LangGraph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: update_taxonomy(state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState, config: langchain_core.runnables.RunnableConfig) -> haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState

      Iteratively refines the taxonomy using new minibatches of data.

      :param state: The current state containing previous taxonomies.
      :type state: TaxonomyGenerationState
      :param config: Configuration settings.
      :type config: RunnableConfig

      :returns: Updated state with revised taxonomy clusters.
      :rtype: TaxonomyGenerationState


      .. autolink-examples:: update_taxonomy
         :collapse:


.. py:class:: TaxonomyAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Agent configuration for generating a taxonomy from conversation history.


   .. autolink-examples:: TaxonomyAgentConfig
      :collapse:

   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: runtime_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: state_schema
      :type:  haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



