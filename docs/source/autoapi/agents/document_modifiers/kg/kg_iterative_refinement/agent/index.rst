agents.document_modifiers.kg.kg_iterative_refinement.agent
==========================================================

.. py:module:: agents.document_modifiers.kg.kg_iterative_refinement.agent

.. autoapi-nested-parse::

   Iterative Knowledge Graph Transformer Agent.

   This module provides the IterativeGraphTransformer class which builds knowledge
   graphs iteratively from a sequence of documents. It processes documents one by one,
   starting with an initial graph and refining it with each subsequent document.

   The agent is particularly useful for building comprehensive knowledge graphs from
   multiple related documents where later documents may add detail or context to
   earlier information.

   Classes:
       IterativeGraphTransformer: Main agent for iterative knowledge graph construction

   .. rubric:: Examples

   Basic usage::

       from haive.agents.document_modifiers.kg.kg_iterative_refinement import IterativeGraphTransformer
       from haive.agents.document_modifiers.kg.kg_iterative_refinement.config import IterativeGraphTransformerConfig

       config = IterativeGraphTransformerConfig()
       agent = IterativeGraphTransformer(config)

       documents = [
           "Marie Curie was a physicist born in Poland.",
           "She won two Nobel Prizes in different fields.",
           "Her daughter Irène also won a Nobel Prize."
       ]
       result = agent.run({"contents": documents})
       graph = result["graph_doc"]

   With custom configuration::

       config = IterativeGraphTransformerConfig(
           name="research_graph_builder",
           engines={"transformer": custom_llm_config}
       )
       agent = IterativeGraphTransformer(config)

   .. seealso::

      - :class:`~haive.agents.document_modifiers.kg.kg_iterative_refinement.config.IterativeGraphTransformerConfig`: Configuration class
      - :class:`~haive.agents.document_modifiers.kg.kg_iterative_refinement.state.IterativeGraphTransformerState`: State management


   .. autolink-examples:: agents.document_modifiers.kg.kg_iterative_refinement.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.kg.kg_iterative_refinement.agent.logger


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_iterative_refinement.agent.IterativeGraphTransformer


Functions
---------

.. autoapisummary::

   agents.document_modifiers.kg.kg_iterative_refinement.agent.build_agent


Module Contents
---------------

.. py:class:: IterativeGraphTransformer(config: haive.agents.document_modifiers.kg.kg_iterative_refinement.config.IterativeGraphTransformerConfig = IterativeGraphTransformerConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.document_modifiers.kg.kg_iterative_refinement.config.IterativeGraphTransformerConfig`\ ]


   Agent that builds knowledge graphs iteratively from documents.

   This agent processes a sequence of documents to build a comprehensive
   knowledge graph. It starts by creating an initial graph from the first
   document, then iteratively refines and expands the graph with information
   from subsequent documents.

   The iterative approach allows the agent to:
   1. Build context progressively
   2. Resolve entity references across documents
   3. Accumulate relationships and properties
   4. Maintain graph coherence throughout the process

   :param config: Configuration object containing agent settings and LLM
                  configuration for the graph transformer.

   .. attribute:: llm_graph_transformer

      The underlying GraphTransformer instance
      used to convert documents to graph representations.

   .. rubric:: Examples

   Processing a series of related documents::

       agent = IterativeGraphTransformer()
       docs = [
           "Einstein developed the theory of relativity.",
           "The theory of relativity revolutionized physics.",
           "Einstein received the Nobel Prize in 1921."
       ]
       result = agent.run({"contents": docs})

       # Access the final knowledge graph
       graph = result["graph_doc"]
       nodes = graph.nodes  # List of entities
       relationships = graph.relationships  # List of connections

   With strict mode for validation::

       config = IterativeGraphTransformerConfig(
           strict_mode=True,  # Enforce schema validation
           ignore_tool_usage=False  # Allow tool-based extraction
       )
       agent = IterativeGraphTransformer(config)

   .. note::

      The agent processes documents sequentially, so document order can
      affect the final graph structure. Consider ordering documents from
      general to specific for best results.

   :raises ValueError: If no documents are provided for processing
   :raises TypeError: If document content is not in a supported format

   .. seealso::

      - :class:`GraphTransformer`: The underlying graph transformation engine
      - :meth:`generate_initial_summary`: Initial graph creation
      - :meth:`refine_summary`: Graph refinement process

   Initialize the iterative graph transformer.

   Sets up the graph transformer instance that will be used to
   process documents into knowledge graph representations.

   :param config: Agent configuration with transformer settings.
                  Defaults to a new instance with default values.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeGraphTransformer
      :collapse:

   .. py:method:: generate_initial_summary(state: haive.agents.document_modifiers.kg.kg_iterative_refinement.state.IterativeGraphTransformerState, config: langchain_core.runnables.RunnableConfig) -> langgraph.types.Command

      Generate the initial knowledge graph from the first document.

      Creates the foundational graph structure from the first document
      in the sequence. This graph will be iteratively refined with
      subsequent documents.

      :param state: Current state containing the list of documents to process.
                    Must have at least one document in the 'contents' field.
      :param config: Runtime configuration for the operation.

      :returns: Command updating the state with the initial graph_doc and
                incrementing the index to 1.

      .. note::

         The state normalizes various input formats (str, dict, Document)
         to Document objects before processing.


      .. autolink-examples:: generate_initial_summary
         :collapse:


   .. py:method:: refine_summary(state: haive.agents.document_modifiers.kg.kg_iterative_refinement.state.IterativeGraphTransformerState, config: langchain_core.runnables.RunnableConfig) -> langgraph.types.Command

      Refine the knowledge graph with information from the next document.

      Takes the existing graph and integrates new information from the
      current document. The refinement process preserves existing knowledge
      while adding new entities, relationships, and properties.

      :param state: Current state containing the existing graph and remaining
                    documents. Must have a valid index pointing to the next document.
      :param config: Runtime configuration for the operation.

      :returns: Command updating the state with the refined graph_doc and
                incrementing the index.

      :raises IndexError: If the index is out of bounds for the contents list.
      :raises TypeError: If the content at the current index is not a valid type.


      .. autolink-examples:: refine_summary
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the iterative graph building workflow.

      Constructs a StateGraph that implements the following workflow:
      1. Generate initial graph from the first document
      2. Iteratively refine the graph with each subsequent document
      3. Continue until all documents have been processed

      The workflow uses conditional edges to determine when to stop
      refining based on the number of documents processed.

      .. note::

         This method is called automatically during agent initialization
         and does not need to be invoked manually.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: llm_graph_transformer


.. py:function:: build_agent() -> IterativeGraphTransformer

   Create a default IterativeGraphTransformer instance.

   :returns: IterativeGraphTransformer with default configuration.


   .. autolink-examples:: build_agent
      :collapse:

.. py:data:: logger

