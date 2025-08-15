agents.reflection.simple_agent
==============================

.. py:module:: agents.reflection.simple_agent

.. autoapi-nested-parse::

   Simple Reflection Agent using clean MultiAgent pattern.


   .. autolink-examples:: agents.reflection.simple_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reflection.simple_agent.ReflectionAgent


Functions
---------

.. autoapisummary::

   agents.reflection.simple_agent.create
   agents.reflection.simple_agent.enhance_agent


Module Contents
---------------

.. py:class:: ReflectionAgent

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Simple reflection agent using clean MultiAgent pattern.


   .. autolink-examples:: ReflectionAgent
      :collapse:

   .. py:method:: _run_sequential(input_data, **kwargs)
      :async:


      Custom sequential execution with reflection loop.


      .. autolink-examples:: _run_sequential
         :collapse:


   .. py:method:: create(name: str = 'reflection_agent', max_iterations: int = 2, quality_threshold: float = 0.8, **kwargs) -> ReflectionAgent
      :classmethod:


      Create a simple reflection agent.


      .. autolink-examples:: create
         :collapse:


   .. py:method:: enhance_agent(base_agent: Any, name: str | None = None, **kwargs) -> ReflectionAgent
      :classmethod:


      Enhance any agent with reflection capability.


      .. autolink-examples:: enhance_agent
         :collapse:


.. py:function:: create(*args, **kwargs) -> ReflectionAgent

   Create a simple reflection agent.


   .. autolink-examples:: create
      :collapse:

.. py:function:: enhance_agent(base_agent: Any, **kwargs) -> ReflectionAgent

   Enhance any agent with reflection capability.


   .. autolink-examples:: enhance_agent
      :collapse:

