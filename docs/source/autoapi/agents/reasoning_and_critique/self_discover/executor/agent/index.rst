agents.reasoning_and_critique.self_discover.executor.agent
==========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.executor.agent

.. autoapi-nested-parse::

   Self-Discover Executor Agent implementation.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.executor.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.executor.agent.ExecutorAgent


Module Contents
---------------

.. py:class:: ExecutorAgent(name: str = 'executor', engine: haive.core.engine.aug_llm.AugLLMConfig = None, **kwargs)

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   Agent that executes structured reasoning plans to solve tasks.

   The Executor Agent is the fourth and final stage in the Self-Discover workflow.
   It takes the structured reasoning plan and systematically executes it to
   arrive at a comprehensive solution for the original task.

   .. attribute:: name

      Agent identifier (default: "executor")

   .. attribute:: engine

      LLM configuration for the agent

   .. rubric:: Example

   >>> from haive.core.engine.aug_llm import AugLLMConfig
   >>>
   >>> config = AugLLMConfig(temperature=0.5)
   >>> executor = ExecutorAgent(engine=config)
   >>>
   >>> result = await executor.arun({
   ...     "reasoning_structure": "Step 1: Analyze requirements...",
   ...     "task_description": "Design a recommendation system"
   ... })

   Initialize the Executor Agent.

   :param name: Name for the agent
   :param engine: LLM configuration (if not provided, creates default)
   :param \*\*kwargs: Additional arguments passed to SimpleAgent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutorAgent
      :collapse:

