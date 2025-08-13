
:py:mod:`agents.reasoning_and_critique.self_discover.engines`
=============================================================

.. py:module:: agents.reasoning_and_critique.self_discover.engines



Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.engines.create_adapt_engine
   agents.reasoning_and_critique.self_discover.engines.create_reasoning_engine
   agents.reasoning_and_critique.self_discover.engines.create_select_engine
   agents.reasoning_and_critique.self_discover.engines.create_selfdiscover_engines
   agents.reasoning_and_critique.self_discover.engines.create_structure_engine

.. py:function:: create_adapt_engine(model: str = 'gpt-4o', temperature: float = 0.0, custom_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, **kwargs) -> haive.core.engine.aug_llm.AugLLMConfig

   Create the engine for adapting selected reasoning modules with structured output.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param custom_prompt: Optional custom prompt
   :param \*\*kwargs: Additional parameters for AugLLMConfig

   :returns: AugLLMConfig for adaptation stage


   .. autolink-examples:: create_adapt_engine
      :collapse:

.. py:function:: create_reasoning_engine(model: str = 'gpt-4o', temperature: float = 0.0, custom_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, **kwargs) -> haive.core.engine.aug_llm.AugLLMConfig

   Create the engine for executing reasoning plans with structured output.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param custom_prompt: Optional custom prompt
   :param \*\*kwargs: Additional parameters for AugLLMConfig

   :returns: AugLLMConfig for reasoning stage


   .. autolink-examples:: create_reasoning_engine
      :collapse:

.. py:function:: create_select_engine(model: str = 'gpt-4o', temperature: float = 0.0, custom_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, **kwargs) -> haive.core.engine.aug_llm.AugLLMConfig

   Create the engine for selecting reasoning modules with structured output.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param custom_prompt: Optional custom prompt
   :param \*\*kwargs: Additional parameters for AugLLMConfig

   :returns: AugLLMConfig for selection stage


   .. autolink-examples:: create_select_engine
      :collapse:

.. py:function:: create_selfdiscover_engines(model: str = 'gpt-4o', temperature: float = 0.0, select_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, adapt_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, structure_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, reasoning_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create all engines for the SelfDiscover agent with structured output models.

   :param model: Model name to use for all engines
   :param temperature: Temperature for all engines
   :param select_prompt: Custom prompt for selection stage
   :param adapt_prompt: Custom prompt for adaptation stage
   :param structure_prompt: Custom prompt for structuring stage
   :param reasoning_prompt: Custom prompt for reasoning stage
   :param \*\*kwargs: Additional parameters for AugLLMConfigs

   :returns: Dictionary of AugLLMConfigs for each stage


   .. autolink-examples:: create_selfdiscover_engines
      :collapse:

.. py:function:: create_structure_engine(model: str = 'gpt-4o', temperature: float = 0.0, custom_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, **kwargs) -> haive.core.engine.aug_llm.AugLLMConfig

   Create the engine for creating structured reasoning plans with structured output.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param custom_prompt: Optional custom prompt
   :param \*\*kwargs: Additional parameters for AugLLMConfig

   :returns: AugLLMConfig for structuring stage


   .. autolink-examples:: create_structure_engine
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.engines
   :collapse:
   
.. autolink-skip:: next
