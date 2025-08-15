agents.reasoning_and_critique.self_discover.structurer.agent
============================================================

.. py:module:: agents.reasoning_and_critique.self_discover.structurer.agent

.. autoapi-nested-parse::

   Self-Discover Structurer Agent implementation.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.structurer.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.structurer.agent.StructurerAgent


Module Contents
---------------

.. py:class:: StructurerAgent(name: str = 'structurer', engine: haive.core.engine.aug_llm.AugLLMConfig = None, **kwargs)

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   Agent that creates structured reasoning plans from adapted modules.

   The Structurer Agent is the third stage in the Self-Discover workflow.
   It takes the adapted reasoning modules and organizes them into a coherent,
   step-by-step plan for solving the specific task.

   .. attribute:: name

      Agent identifier (default: "structurer")

   .. attribute:: engine

      LLM configuration for the agent

   .. rubric:: Example

   >>> from haive.core.engine.aug_llm import AugLLMConfig
   >>>
   >>> config = AugLLMConfig(temperature=0.2)
   >>> structurer = StructurerAgent(engine=config)
   >>>
   >>> result = await structurer.arun({
   ...     "adapted_modules": "1. Critical analysis: Look for biases...",
   ...     "task_description": "Design a recommendation system"
   ... })

   Initialize the Structurer Agent.

   :param name: Name for the agent
   :param engine: LLM configuration (if not provided, creates default)
   :param \*\*kwargs: Additional arguments passed to SimpleAgent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructurerAgent
      :collapse:

