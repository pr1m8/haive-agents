agents.multi.simple.agent
=========================

.. py:module:: agents.multi.simple.agent

.. autoapi-nested-parse::

   Simple Multi-Agent implementation for basic multi-agent coordination.

   This module provides a simplified multi-agent system that focuses on ease of use
   and straightforward coordination patterns without complex orchestration.


   .. autolink-examples:: agents.multi.simple.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.multi.simple.agent.SimpleMultiAgent


Functions
---------

.. autoapisummary::

   agents.multi.simple.agent.create_simple_conditional
   agents.multi.simple.agent.create_simple_parallel
   agents.multi.simple.agent.create_simple_sequential


Module Contents
---------------

.. py:class:: SimpleMultiAgent

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Simplified multi-agent system using MultiAgent.

   This class provides a simplified interface to MultiAgent with
   common defaults and simplified configuration. Perfect for simple workflows
   and quick prototyping using the enhanced base agent pattern.

   .. rubric:: Examples

   Basic sequential execution::

       from haive.agents.simple.agent import SimpleAgent
       from haive.agents.react.agent import ReactAgent

       agents = [
           ReactAgent(name="analyzer", tools=[...]),
           SimpleAgent(name="formatter")
       ]

       simple_multi = SimpleMultiAgent(
           name="simple_workflow",
           agents=agents,
           execution_mode="sequential"
       )

       result = await simple_multi.arun("Process this input")

   Parallel execution::

       simple_multi = SimpleMultiAgent(
           name="parallel_workflow",
           agents=agents,
           execution_mode="parallel"
       )


   .. autolink-examples:: SimpleMultiAgent
      :collapse:

   .. py:method:: model_post_init(__context: Any) -> None

      Initialize with simplified defaults.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:method:: setup_simple_workflow() -> None

      Set up the simple multi-agent workflow with enhanced features.


      .. autolink-examples:: setup_simple_workflow
         :collapse:


   .. py:attribute:: build_mode
      :type:  str
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



.. py:function:: create_simple_conditional(*agents: haive.core.engine.agent.Agent, name: str = 'simple_conditional') -> SimpleMultiAgent

   Create a simple conditional multi-agent using enhanced pattern.


   .. autolink-examples:: create_simple_conditional
      :collapse:

.. py:function:: create_simple_parallel(*agents: haive.core.engine.agent.Agent, name: str = 'simple_parallel') -> SimpleMultiAgent

   Create a simple parallel multi-agent using enhanced pattern.


   .. autolink-examples:: create_simple_parallel
      :collapse:

.. py:function:: create_simple_sequential(*agents: haive.core.engine.agent.Agent, name: str = 'simple_sequential') -> SimpleMultiAgent

   Create a simple sequential multi-agent using enhanced pattern.


   .. autolink-examples:: create_simple_sequential
      :collapse:

