agents.planning.p_and_e.engines
===============================

.. py:module:: agents.planning.p_and_e.engines

.. autoapi-nested-parse::

   AugLLM configurations for Plan and Execute Agent System.

   This module defines the AugLLM configurations for planning, execution,
   and replanning agents.


   .. autolink-examples:: agents.planning.p_and_e.engines
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.p_and_e.engines.executor_aug_llm_config
   agents.planning.p_and_e.engines.planner_aug_llm_config
   agents.planning.p_and_e.engines.replan_aug_llm_config


Functions
---------

.. autoapisummary::

   agents.planning.p_and_e.engines.create_executor_aug_llm_config
   agents.planning.p_and_e.engines.create_planner_aug_llm_config
   agents.planning.p_and_e.engines.create_replan_aug_llm_config


Module Contents
---------------

.. py:function:: create_executor_aug_llm_config(model_name: str = 'gpt-4o', tools: list[langchain_core.tools.BaseTool] | None = None, force_tool_use: bool = False) -> haive.core.engine.aug_llm.AugLLMConfig

   Create AugLLM configuration for the execution agent.

   :param model_name: The LLM model to use
   :param temperature: Temperature for generation
   :param tools: List of tools available to the executor
   :param force_tool_use: Whether to force tool usage

   :returns: Configured AugLLMConfig for execution


   .. autolink-examples:: create_executor_aug_llm_config
      :collapse:

.. py:function:: create_planner_aug_llm_config(model_name: str = 'gpt-4o', temperature: float = 0.1, use_context: bool = True) -> haive.core.engine.aug_llm.AugLLMConfig

   Create AugLLM configuration for the planning agent.

   :param model_name: The LLM model to use
   :param temperature: Temperature for generation (lower = more focused)
   :param use_context: Whether to use the context-aware prompt template

   :returns: Configured AugLLMConfig for planning


   .. autolink-examples:: create_planner_aug_llm_config
      :collapse:

.. py:function:: create_replan_aug_llm_config(model_name: str = 'gpt-4o', temperature: float = 0.2, max_replan_attempts: int = 3) -> haive.core.engine.aug_llm.AugLLMConfig

   Create AugLLM configuration for the replanning agent.

   :param model_name: The LLM model to use
   :param temperature: Temperature for generation
   :param max_replan_attempts: Maximum number of replanning attempts

   :returns: Configured AugLLMConfig for replanning


   .. autolink-examples:: create_replan_aug_llm_config
      :collapse:

.. py:data:: executor_aug_llm_config

.. py:data:: planner_aug_llm_config

.. py:data:: replan_aug_llm_config

