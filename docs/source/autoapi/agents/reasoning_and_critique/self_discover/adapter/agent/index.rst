agents.reasoning_and_critique.self_discover.adapter.agent
=========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.adapter.agent

.. autoapi-nested-parse::

   Self-Discover Adapter Agent implementation.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.adapter.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.adapter.agent.AdapterAgent


Module Contents
---------------

.. py:class:: AdapterAgent(name: str = 'adapter', engine: haive.core.engine.aug_llm.AugLLMConfig = None, **kwargs)

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   Agent that adapts selected reasoning modules for specific tasks.

   The Adapter Agent is the second stage in the Self-Discover workflow.
   It takes the reasoning modules selected by the Selector Agent and adapts
   them to be concrete and actionable for the specific task at hand.

   .. attribute:: name

      Agent identifier (default: "adapter")

   .. attribute:: engine

      LLM configuration for the agent

   .. rubric:: Example

   >>> from haive.core.engine.aug_llm import AugLLMConfig
   >>>
   >>> config = AugLLMConfig(temperature=0.4)
   >>> adapter = AdapterAgent(engine=config)
   >>>
   >>> result = await adapter.arun({
   ...     "selected_modules": "1. Critical thinking: Analyze assumptions...",
   ...     "task_description": "Design a recommendation system"
   ... })

   Initialize the Adapter Agent.

   :param name: Name for the agent
   :param engine: LLM configuration (if not provided, creates default)
   :param \*\*kwargs: Additional arguments passed to SimpleAgent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdapterAgent
      :collapse:

