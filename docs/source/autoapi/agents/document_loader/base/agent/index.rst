
:py:mod:`agents.document_loader.base.agent`
===========================================

.. py:module:: agents.document_loader.base.agent

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




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentLoaderAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentLoaderAgent {
        node [shape=record];
        "DocumentLoaderAgent" [label="DocumentLoaderAgent"];
        "haive.agents.base.agent.Agent" -> "DocumentLoaderAgent";
      }

.. autoclass:: agents.document_loader.base.agent.DocumentLoaderAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_loader.base.agent
   :collapse:
   
.. autolink-skip:: next
