agents.reasoning_and_critique.reflection.agent
==============================================

.. py:module:: agents.reasoning_and_critique.reflection.agent

.. autoapi-nested-parse::

   Reflection Agent Implementation.


   .. autolink-examples:: agents.reasoning_and_critique.reflection.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.reflection.agent.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflection.agent.ReflectionAgent


Module Contents
---------------

.. py:class:: ReflectionAgent(config: haive.agents.reasoning_and_critique.reflection.config.ReflectionAgentConfig)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   An agent with self-reflection capabilities that can improve its responses.

   This agent extends SimpleAgent by adding reflection and improvement steps
   to iteratively refine responses based on self-critique.

   Initialize the reflection agent with the provided configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionAgent
      :collapse:

   .. py:method:: _create_evaluation_function()

      Create a function to evaluate if the improved response is good enough.


      .. autolink-examples:: _create_evaluation_function
         :collapse:


   .. py:method:: _create_improvement_function()

      Create a function for the improvement node.


      .. autolink-examples:: _create_improvement_function
         :collapse:


   .. py:method:: _create_initial_response_function()

      Create a function for the initial response node.


      .. autolink-examples:: _create_initial_response_function
         :collapse:


   .. py:method:: _create_reflection_function()

      Create a function for the reflection node.


      .. autolink-examples:: _create_reflection_function
         :collapse:


   .. py:method:: _create_search_function()

      Create a function for the search node.


      .. autolink-examples:: _create_search_function
         :collapse:


   .. py:method:: _should_continue_improvement(state: haive.agents.reasoning_and_critique.reflection.state.ReflectionAgentState) -> str

      Determine if we should continue with another reflection round or end.


      .. autolink-examples:: _should_continue_improvement
         :collapse:


   .. py:method:: _should_continue_reflection(state: haive.agents.reasoning_and_critique.reflection.state.ReflectionAgentState) -> str

      Determine if we should continue to the search/improvement step or end.


      .. autolink-examples:: _should_continue_reflection
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up a workflow graph with reflection capabilities.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: config


.. py:data:: logger

