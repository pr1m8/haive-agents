agents.document_loader.directory.agent
======================================

.. py:module:: agents.document_loader.directory.agent

.. autoapi-nested-parse::

   Directory-specific Document Loader Agent.

   This module provides a specialized document loader agent for loading
   documents from local directories.


   .. autolink-examples:: agents.document_loader.directory.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_loader.directory.agent.DirectoryLoaderAgent


Module Contents
---------------

.. py:class:: DirectoryLoaderAgent

   Bases: :py:obj:`haive.agents.document_loader.base.agent.DocumentLoaderAgent`


   Specialized document loader agent for loading documents from directories.

   This agent is pre-configured for loading from local directories and provides
   additional directory-specific options.

   .. attribute:: name

      Name of the agent

   .. attribute:: directory_path

      Path to the directory to load

   .. attribute:: recursive

      Whether to recursively load files

   .. attribute:: glob_pattern

      Glob pattern for filtering files

   .. attribute:: include_extensions

      List of file extensions to include

   .. attribute:: exclude_extensions

      List of file extensions to exclude


   .. autolink-examples:: DirectoryLoaderAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Set up the agent with a directory loader engine.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: directory_path
      :type:  str | pathlib.Path | None
      :value: None



   .. py:attribute:: exclude_extensions
      :type:  list[str] | None
      :value: None



   .. py:attribute:: glob_pattern
      :type:  str | None
      :value: None



   .. py:attribute:: include_extensions
      :type:  list[str] | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Directory Loader Agent'



   .. py:attribute:: recursive
      :type:  bool
      :value: None



