agents.multi.base.agent
=======================

.. py:module:: agents.multi.base.agent

.. autoapi-nested-parse::

   Base MultiAgent implementation.

   This module provides the base multi-agent class that other multi-agent
   implementations can inherit from or use directly.


   .. autolink-examples:: agents.multi.base.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.multi.base.agent.SequentialAgent
   agents.multi.base.agent.SequentialAgentConfig


Module Contents
---------------

.. py:class:: SequentialAgent(config: SequentialAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.Agent`


   Agent that executes multiple agents in sequence.

   This agent runs a list of agents one after another, optionally
   passing the output of one agent as input to the next.


   .. autolink-examples:: SequentialAgent
      :collapse:

   .. py:method:: run(input_data: Any, **kwargs) -> Any

      Run all agents in sequence.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: agents


   .. py:attribute:: pass_results


.. py:class:: SequentialAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.AgentConfig`


   Configuration for sequential multi-agent execution.


   .. autolink-examples:: SequentialAgentConfig
      :collapse:

   .. py:attribute:: agents
      :type:  list[Any]
      :value: None



   .. py:attribute:: pass_results
      :type:  bool
      :value: None



