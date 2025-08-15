agents.reasoning_and_critique.self_discover.agent2
==================================================

.. py:module:: agents.reasoning_and_critique.self_discover.agent2


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.agent2.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.agent2.SelfDiscoverAgent


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.agent2.create_self_discover_agent


Module Contents
---------------

.. py:class:: SelfDiscoverAgent

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.reasoning_and_critique.self_discover.config.SelfDiscoverAgentConfig`\ ]


   An agent that implements the SelfDiscover methodology with structured output models.

   This agent follows a four-stage approach:
   1. Select appropriate reasoning modules for the task
   2. Adapt the modules to better fit the task
   3. Structure the reasoning into a step-by-step plan
   4. Execute the plan to solve the task

   Each stage uses a dedicated LLM with structured output models to ensure
   consistent, high-quality reasoning.


   .. autolink-examples:: SelfDiscoverAgent
      :collapse:

   .. py:method:: setup_workflow() -> None

      Set up the workflow graph for the SelfDiscover agent.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:function:: create_self_discover_agent(model: str = 'gpt-4o', temperature: float = 0.0, name: str | None = None, reasoning_modules: list[str] | None = None, select_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, adapt_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, structure_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, reasoning_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, visualize: bool = True, **kwargs) -> SelfDiscoverAgent

   Create a SelfDiscover agent with customizable parameters.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param name: Optional name for the agent
   :param reasoning_modules: List of reasoning modules to use
   :param select_prompt: Custom prompt for the selection stage
   :param adapt_prompt: Custom prompt for the adaptation stage
   :param structure_prompt: Custom prompt for the structure stage
   :param reasoning_prompt: Custom prompt for the reasoning stage
   :param visualize: Whether to visualize the graph
   :param \*\*kwargs: Additional configuration parameters

   :returns: SelfDiscoverAgent instance


   .. autolink-examples:: create_self_discover_agent
      :collapse:

.. py:data:: logger

