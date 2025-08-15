agents.reasoning_and_critique.tot.modular.factory
=================================================

.. py:module:: agents.reasoning_and_critique.tot.modular.factory


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.factory.create_game24_tot_agent
   agents.reasoning_and_critique.tot.modular.factory.create_math_tot_agent
   agents.reasoning_and_critique.tot.modular.factory.create_tot_agent


Module Contents
---------------

.. py:function:: create_game24_tot_agent(model: str = 'gpt-4o', temperature: float = 0.7, name: str | None = None, **kwargs) -> haive.agents.reasoning_and_critique.tot.modular.agent.ToTAgent

   Create a Tree of Thoughts agent specifically for "Game of 24" problems.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param name: Optional agent name
   :param \*\*kwargs: Additional configuration parameters

   :returns: ToTAgent configured for the Game of 24


   .. autolink-examples:: create_game24_tot_agent
      :collapse:

.. py:function:: create_math_tot_agent(model: str = 'gpt-4o', temperature: float = 0.7, name: str | None = None, **kwargs) -> haive.agents.reasoning_and_critique.tot.modular.agent.ToTAgent

   Create a Tree of Thoughts agent specifically for math problems.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param name: Optional agent name
   :param \*\*kwargs: Additional configuration parameters

   :returns: ToTAgent configured for math problems


   .. autolink-examples:: create_math_tot_agent
      :collapse:

.. py:function:: create_tot_agent(model: str = 'gpt-4o', temperature: float = 0.7, max_depth: int = 5, threshold: float = 0.9, beam_size: int = 3, candidates_per_expansion: int = 3, name: str | None = None, system_prompt: str = 'You are an expert problem solver using a step-by-step approach.', expand_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, score_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, score_function: collections.abc.Callable | None = None, visualize: bool = True, **kwargs) -> haive.agents.reasoning_and_critique.tot.modular.agent.ToTAgent

   Create a Tree of Thoughts agent with customizable parameters.

   :param model: Model name to use
   :param temperature: Temperature for generation
   :param max_depth: Maximum depth for the search
   :param threshold: Score threshold for success
   :param beam_size: Number of candidates to keep after pruning
   :param candidates_per_expansion: Number of candidates to generate in each expansion
   :param name: Optional name for the agent
   :param system_prompt: System prompt for the agent
   :param expand_prompt: Custom prompt for expansion (string or ChatPromptTemplate)
   :param score_prompt: Custom prompt for scoring (string or ChatPromptTemplate)
   :param score_function: Optional function to score candidates instead of using LLM
   :param visualize: Whether to visualize the ToT graph
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured ToTAgent instance


   .. autolink-examples:: create_tot_agent
      :collapse:

