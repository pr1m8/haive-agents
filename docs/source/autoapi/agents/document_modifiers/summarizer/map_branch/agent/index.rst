agents.document_modifiers.summarizer.map_branch.agent
=====================================================

.. py:module:: agents.document_modifiers.summarizer.map_branch.agent

.. autoapi-nested-parse::

   Map-Reduce Summarizer Agent for document summarization.

   This module provides the SummarizerAgent class which implements a map-reduce
   approach to document summarization. It can handle large documents by splitting
   them into manageable chunks, summarizing each chunk, and then combining the
   summaries into a final coherent summary.

   The agent handles token limit constraints and provides automatic fallback
   mechanisms for oversized documents.

   Classes:
       SummarizerAgent: Main agent for map-reduce document summarization

   .. rubric:: Examples

   Basic usage::

       from haive.agents.document_modifiers.summarizer.map_branch import SummarizerAgent
       from haive.agents.document_modifiers.summarizer.map_branch.config import SummarizerAgentConfig

       config = SummarizerAgentConfig(
           token_max=1000,
           name="document_summarizer"
       )
       agent = SummarizerAgent(config)

       documents = ["Long document text 1...", "Long document text 2..."]
       result = agent.run({"contents": documents})
       summary = result["final_summary"]

   With custom token limits::

       config = SummarizerAgentConfig(
           token_max=2000,  # Allow longer intermediate summaries
           engines={
               "map_chain": custom_map_config,
               "reduce_chain": custom_reduce_config
           }
       )
       agent = SummarizerAgent(config)

   .. seealso::

      - :class:`~haive.agents.document_modifiers.summarizer.map_branch.config.SummarizerAgentConfig`: Configuration class
      - :class:`~haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState`: State management


   .. autolink-examples:: agents.document_modifiers.summarizer.map_branch.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.agent.logger


Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.agent.SummarizerAgent


Functions
---------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.agent.build_agent


Module Contents
---------------

.. py:class:: SummarizerAgent(config: haive.agents.document_modifiers.summarizer.map_branch.config.SummarizerAgentConfig = SummarizerAgentConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.document_modifiers.summarizer.map_branch.config.SummarizerAgentConfig`\ ]


   Agent that summarizes documents using a map-reduce approach.

   This agent implements a sophisticated document summarization workflow that
   can handle large documents and multiple documents simultaneously. It uses
   a map-reduce pattern where documents are first summarized individually
   (map phase), then combined and reduced to a final summary (reduce phase).

   The agent automatically handles token limit constraints by:
   1. Splitting oversized documents into manageable chunks
   2. Summarizing chunks individually
   3. Collapsing intermediate summaries when they exceed token limits
   4. Producing a coherent final summary

   :param config: Configuration object containing token limits, LLM settings,
                  and workflow parameters.

   .. attribute:: token_max

      Maximum token limit for intermediate summaries

   .. attribute:: map_chain

      Runnable for individual document summarization

   .. attribute:: reduce_chain

      Runnable for combining and reducing summaries

   .. attribute:: text_splitter

      Utility for splitting oversized documents

   .. rubric:: Examples

   Basic document summarization::

       config = SummarizerAgentConfig(token_max=1000)
       agent = SummarizerAgent(config)

       docs = ["First document content...", "Second document content..."]
       result = agent.run({"contents": docs})
       print(result["final_summary"])

   Handling large documents::

       # Agent automatically splits and processes large documents
       large_doc = "Very long document content..." * 1000
       result = agent.run({"contents": [large_doc]})
       # The agent will chunk, summarize, and combine automatically

   With custom configuration::

       config = SummarizerAgentConfig(
           token_max=2000,
           engines={
               "map_chain": custom_map_config,
               "reduce_chain": custom_reduce_config
           }
       )
       agent = SummarizerAgent(config)

   .. note::

      The agent uses recursive text splitting to handle documents that exceed
      token limits. Chunk summaries are automatically combined using the
      reduce chain to maintain coherence.

   :raises ValueError: If no documents are provided for summarization
   :raises RuntimeError: If summarization fails after all retry attempts

   .. seealso::

      - :class:`SummarizerAgentConfig`: Configuration options
      - :class:`SummaryState`: State management for the workflow
      - :meth:`setup_workflow`: Workflow construction details

   Initialize the SummarizerAgent with configuration.

   Sets up the map and reduce chains for document processing and
   initializes the text splitter for handling oversized documents.

   :param config: Agent configuration with token limits and LLM settings.
                  Defaults to a new instance with default values.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SummarizerAgent
      :collapse:

   .. py:method:: _get_token_count(text: str) -> int

      Get token count for a single text string.

      :param text: Text to count tokens for.

      :returns: Number of tokens in the text.


      .. autolink-examples:: _get_token_count
         :collapse:


   .. py:method:: _handle_oversized_document(content: str) -> dict
      :async:


      Handle document that exceeds token limits.

      Splits the document into chunks, summarizes each chunk, and
      combines the results.

      :param content: Document content that exceeds token limits.

      :returns: Dictionary with 'summaries' key containing the combined summary.


      .. autolink-examples:: _handle_oversized_document
         :collapse:


   .. py:method:: _is_token_limit_error(error_str: str) -> bool

      Check if error is related to token limits.

      :param error_str: Error message to check.

      :returns: True if error is token-related, False otherwise.


      .. autolink-examples:: _is_token_limit_error
         :collapse:


   .. py:method:: collapse_summaries(state: haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState) -> langgraph.types.Command
      :async:


      Collapse summaries that exceed token limits.

      When intermediate summaries collectively exceed the token limit,
      this method splits them into groups and reduces each group to
      a more concise summary.

      :param state: Current state containing Document objects to collapse.
                    Must have 'collapsed_summaries' key.

      :returns: Command updating the state with reduced summaries.


      .. autolink-examples:: collapse_summaries
         :collapse:


   .. py:method:: collect_summaries(state: haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState) -> langgraph.types.Command

      Collect individual summaries into document objects.

      Transforms the list of summary strings into Document objects
      for further processing in the collapse phase.

      :param state: Current state containing individual summaries.
                    Must have a 'summaries' key with a list of summary texts.

      :returns: Command updating the state with collapsed_summaries as
                Document objects.


      .. autolink-examples:: collect_summaries
         :collapse:


   .. py:method:: generate_final_summary(state: haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState) -> langgraph.types.Command
      :async:


      Generate the final consolidated summary.

      Processes all collapsed summaries through the reduce chain to
      create a single, coherent final summary.

      :param state: Current state with collapsed summaries ready for
                    final reduction.

      :returns: Command updating the state with the final summary text.


      .. autolink-examples:: generate_final_summary
         :collapse:


   .. py:method:: generate_summary(state: haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState) -> dict
      :async:


      Generate a summary for a single document.

      Processes a document through the map chain to create an individual
      summary. If the document exceeds token limits, it automatically
      splits the document into chunks and summarizes each chunk before
      combining them.

      :param state: Current state containing the document content to summarize.
                    Must have a 'content' key with the document text.

      :returns: Dictionary with 'summaries' key containing a list with the
                generated summary text.

      .. note::

         This method includes automatic error recovery for token limit
         issues by splitting oversized documents into manageable chunks.


      .. autolink-examples:: generate_summary
         :collapse:


   .. py:method:: length_function(documents: list[langchain_core.documents.Document]) -> int

      Calculate total token count for documents.

      Computes the sum of tokens across all provided documents using
      the reduce chain's tokenizer.

      :param documents: List of Document objects to count tokens for.

      :returns: Total number of tokens across all documents.


      .. autolink-examples:: length_function
         :collapse:


   .. py:method:: map_summaries(state: haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState) -> list[langgraph.types.Send]

      Map documents to summary generation tasks.

      Creates parallel summary generation tasks for each input document.
      Each document is sent to the generate_summary node for processing.

      :param state: Current state containing the list of documents to summarize.
                    Must have a 'contents' key with a list of document texts.

      :returns: List of Send commands, one for each document to summarize.


      .. autolink-examples:: map_summaries
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the map-reduce summarization workflow.

      Constructs a StateGraph that implements the following workflow:
      1. Map phase: Generate summaries for each input document
      2. Collect phase: Gather all individual summaries
      3. Collapse phase: Combine summaries if they exceed token limits
      4. Final phase: Generate the final consolidated summary

      The workflow includes conditional edges that determine whether
      intermediate summaries need to be collapsed based on token counts.

      .. note::

         This method is called automatically during agent initialization
         and does not need to be invoked manually.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_collapse(state: haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState) -> Literal['collapse_summaries', 'generate_final_summary']

      Determine if summaries need further collapsing.

      Checks if the total token count of collapsed summaries exceeds
      the configured limit. If so, directs to further collapsing;
      otherwise proceeds to final summary generation.

      :param state: Current state with collapsed summaries to evaluate.

      :returns: 'collapse_summaries' if over limit,
                'generate_final_summary' otherwise.
      :rtype: Next node name


      .. autolink-examples:: should_collapse
         :collapse:


   .. py:attribute:: map_chain


   .. py:attribute:: reduce_chain


   .. py:attribute:: text_splitter


   .. py:attribute:: token_max


.. py:function:: build_agent() -> SummarizerAgent

   Create a default SummarizerAgent instance.

   :returns: SummarizerAgent with default configuration.


   .. autolink-examples:: build_agent
      :collapse:

.. py:data:: logger

