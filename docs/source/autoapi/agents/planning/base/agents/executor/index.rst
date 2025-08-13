
:py:mod:`agents.planning.base.agents.executor`
==============================================

.. py:module:: agents.planning.base.agents.executor

Base Executor Agent - Task execution agent with tavily search capabilities.

This module provides the foundational executor agent designed to carry out
specific steps from plans using available tools, particularly search capabilities.


.. autolink-examples:: agents.planning.base.agents.executor
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.base.agents.executor.BaseExecutorAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseExecutorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BaseExecutorAgent {
        node [shape=record];
        "BaseExecutorAgent" [label="BaseExecutorAgent"];
        "haive.agents.react.agent.ReactAgent" -> "BaseExecutorAgent";
      }

.. autoclass:: agents.planning.base.agents.executor.BaseExecutorAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.base.agents.executor.create_base_executor
   agents.planning.base.agents.executor.create_research_executor

.. py:function:: create_base_executor(name: str = 'base_executor', model: str = 'gpt-4o-mini', temperature: float = 0.1, additional_tools: list | None = None) -> BaseExecutorAgent

   Create a base executor agent with default configuration.

   :param name: Name for the executor agent
   :param model: LLM model to use for execution
   :param temperature: Sampling temperature (lower = more focused execution)
   :param additional_tools: Extra tools to add beyond default search tools

   :returns: Configured executor ready for task execution
   :rtype: BaseExecutorAgent

   .. rubric:: Examples

   Basic executor:

       executor = create_base_executor()

   Custom executor with additional tools:

       from haive.tools.tools import calculator_tool
       executor = create_base_executor(
           name="research_executor",
           model="gpt-4",
           temperature=0.05,
           additional_tools=[calculator_tool]
       )


   .. autolink-examples:: create_base_executor
      :collapse:

.. py:function:: create_research_executor(name: str = 'research_executor') -> BaseExecutorAgent

   Create a specialized executor optimized for research tasks.

   This creates an executor specifically tuned for research and information
   gathering tasks with enhanced search capabilities.

   :returns: Executor optimized for research execution
   :rtype: BaseExecutorAgent


   .. autolink-examples:: create_research_executor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.base.agents.executor
   :collapse:
   
.. autolink-skip:: next
