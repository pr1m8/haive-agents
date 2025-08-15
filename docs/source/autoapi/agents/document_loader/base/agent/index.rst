agents.document_loader.base.agent
=================================

.. py:module:: agents.document_loader.base.agent

.. autoapi-nested-parse::

   Document Loader Agent implementation.

   This module provides an agent implementation that uses the DocumentLoaderEngine
   to load documents from various sources and integrate with the Haive agent framework.

   The agent handles document loading from various sources, including:
   - Local files and directories
   - Web pages and URLs
   - Databases
   - Cloud storage
   - API services

   The agent can be integrated into more complex workflows and supports both
   synchronous and asynchronous operation modes.


   .. autolink-examples:: agents.document_loader.base.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_loader.base.agent.DocumentLoaderAgent


Module Contents
---------------

.. py:class:: DocumentLoaderAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Document Loader Agent that integrates the document loader engine with the agent framework.

   This agent provides a simple interface for loading documents from various sources
   through the agent framework. It can be used as a standalone agent or as part of
   a more complex agent workflow.

   The agent supports loading from:
   - Local files and directories
   - Web pages and URLs
   - Databases (with proper credentials)
   - Cloud storage (with proper credentials)

   .. attribute:: name

      Name of the agent

   .. attribute:: engine

      The document loader engine to use

   .. attribute:: config

      Configuration for the document loader engine

   .. attribute:: include_content

      Whether to include document content in the output

   .. attribute:: include_metadata

      Whether to include document metadata in the output

   .. attribute:: max_documents

      Maximum number of documents to load (None for unlimited)

   .. attribute:: use_async

      Whether to use async loading if available


   .. autolink-examples:: DocumentLoaderAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the document loader agent graph.

      Creates a simple linear graph that loads documents from the input source.

      :returns: A BaseGraph instance for document loading


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: process_output(output: haive.core.engine.document.DocumentOutput) -> dict[str, Any]

      Process the output from the document loader engine.

      This method filters and formats the output based on the agent's configuration.

      :param output: The raw output from the document loader engine

      :returns: A dictionary with processed document data


      .. autolink-examples:: process_output
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the agent by configuring the document loader engine.

      This method is called during agent initialization to set up the engine
      with the agent's configuration parameters.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: engine
      :type:  haive.core.engine.document.DocumentEngine
      :value: None



   .. py:attribute:: include_content
      :type:  bool
      :value: None



   .. py:attribute:: include_metadata
      :type:  bool
      :value: None



   .. py:attribute:: max_documents
      :type:  int | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Document Loader Agent'



   .. py:attribute:: use_async
      :type:  bool
      :value: None



