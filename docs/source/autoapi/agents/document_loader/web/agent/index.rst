agents.document_loader.web.agent
================================

.. py:module:: agents.document_loader.web.agent

.. autoapi-nested-parse::

   Web-specific Document Loader Agent.

   This module provides a specialized document loader agent for loading
   documents from web URLs.


   .. autolink-examples:: agents.document_loader.web.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_loader.web.agent.WebLoaderAgent


Module Contents
---------------

.. py:class:: WebLoaderAgent

   Bases: :py:obj:`haive.agents.document_loader.base.agent.DocumentLoaderAgent`


   Specialized document loader agent for loading documents from web URLs.

   This agent is pre-configured for loading from web sources and provides
   additional web-specific options.

   .. attribute:: name

      Name of the agent

   .. attribute:: url

      URL to load

   .. attribute:: dynamic_loading

      Whether to use a dynamic loading strategy (e.g., Playwright)

   .. attribute:: recursive

      Whether to recursively crawl links

   .. attribute:: max_depth

      Maximum depth for recursive crawling

   .. attribute:: headers

      Custom headers to use for requests


   .. autolink-examples:: WebLoaderAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Set up the agent with a web loader engine.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: dynamic_loading
      :type:  bool
      :value: None



   .. py:attribute:: headers
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Web Loader Agent'



   .. py:attribute:: recursive
      :type:  bool
      :value: None



   .. py:attribute:: url
      :type:  str | None
      :value: None



