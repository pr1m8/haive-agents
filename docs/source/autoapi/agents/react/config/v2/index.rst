agents.react.config.v2
======================

.. py:module:: agents.react.config.v2

.. autoapi-nested-parse::

   Config configuration module.

   This module provides config functionality for the Haive framework.

   Classes:
       ReactAgentConfig: ReactAgentConfig implementation.


   .. autolink-examples:: agents.react.config.v2
      :collapse:


Classes
-------

.. autoapisummary::

   agents.react.config.v2.ReactAgentConfig


Module Contents
---------------

.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`


   Configuration for the React Agent.


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:attribute:: continuation_branch
      :type:  haive.core.graph.branches.branch.Branch
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: retry_policy
      :type:  langgraph.types.RetryPolicy
      :value: None



   .. py:attribute:: tools
      :type:  list[haive.core.types.Tool_Type]
      :value: None



