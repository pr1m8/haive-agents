agents.document_loader.file.agent
=================================

.. py:module:: agents.document_loader.file.agent

.. autoapi-nested-parse::

   File-specific Document Loader Agent.

   This module provides a specialized document loader agent for loading
   documents from local files.


   .. autolink-examples:: agents.document_loader.file.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_loader.file.agent.FileLoaderAgent


Module Contents
---------------

.. py:class:: FileLoaderAgent

   Bases: :py:obj:`haive.agents.document_loader.base.agent.DocumentLoaderAgent`


   Specialized document loader agent for loading documents from files.

   This agent is pre-configured for loading from local files and provides
   additional file-specific options.

   .. attribute:: name

      Name of the agent

   .. attribute:: file_path

      Path to the file to load

   .. attribute:: file_extension

      File extension to use for loader selection

   .. attribute:: loader_name

      Explicit loader name to use


   .. autolink-examples:: FileLoaderAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Set up the agent with a file loader engine.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: file_extension
      :type:  str | None
      :value: None



   .. py:attribute:: file_path
      :type:  str | pathlib.Path | None
      :value: None



   .. py:attribute:: loader_name
      :type:  str | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'File Loader Agent'



