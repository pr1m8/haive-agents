agent.v2
========

.. py:module:: agent.v2

.. autoapi-nested-parse::

   Agent core module.

   This module provides agent functionality for the Haive framework.

   Classes:
       ReactAgent: ReactAgent implementation.

   Functions:
       build_graph: Build Graph functionality.


   .. autolink-examples:: agent.v2
      :collapse:


Classes
-------

.. autoapisummary::

   agent.v2.ReactAgent


Module Contents
---------------

.. py:class:: ReactAgent

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   ReAct agent with looping behavior.


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build ReAct graph with proper looping.


      .. autolink-examples:: build_graph
         :collapse:


