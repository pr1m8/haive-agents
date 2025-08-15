agents.react.config
===================

.. py:module:: agents.react.config


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/react/config/v2/index


Classes
-------

.. autoapisummary::

   agents.react.config.ReactAgentConfig


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
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



