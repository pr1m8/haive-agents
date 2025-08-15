agents.multi.simple
===================

.. py:module:: agents.multi.simple

.. autoapi-nested-parse::

   Simple multi-agent module.


   .. autolink-examples:: agents.multi.simple
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/multi/simple/agent/index


Classes
-------

.. autoapisummary::

   agents.multi.simple.SimpleMultiAgent


Package Contents
----------------

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



