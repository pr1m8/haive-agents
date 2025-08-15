agents.reasoning_and_critique.self_discover.selector.agent
==========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.selector.agent

.. autoapi-nested-parse::

   Self-Discover Selector Agent implementation.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.selector.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.selector.agent.SelectorAgent


Module Contents
---------------

.. py:class:: SelectorAgent(name: str = 'selector', engine: haive.core.engine.aug_llm.AugLLMConfig = None, **kwargs)

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   Agent that selects relevant reasoning modules for a given task.

   The Selector Agent is the first stage in the Self-Discover workflow.
   It analyzes the task and selects 3-5 reasoning modules from the available
   options that would be most effective for solving the problem.

   .. attribute:: name

      Agent identifier (default: "selector")

   .. attribute:: engine

      LLM configuration for the agent

   .. rubric:: Example

   >>> from haive.core.engine.aug_llm import AugLLMConfig
   >>>
   >>> config = AugLLMConfig(temperature=0.3)
   >>> selector = SelectorAgent(engine=config)
   >>>
   >>> result = await selector.arun({
   ...     "available_modules": "1. Critical thinking\\n2. Pattern recognition...",
   ...     "task_description": "Design a recommendation system"
   ... })

   Initialize the Selector Agent.

   :param name: Name for the agent
   :param engine: LLM configuration (if not provided, creates default)
   :param \*\*kwargs: Additional arguments passed to SimpleAgent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectorAgent
      :collapse:

