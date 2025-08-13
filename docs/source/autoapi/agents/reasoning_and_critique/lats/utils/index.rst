
:py:mod:`agents.reasoning_and_critique.lats.utils`
==================================================

.. py:module:: agents.reasoning_and_critique.lats.utils



Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.lats.utils.create_lats_agent
   agents.reasoning_and_critique.lats.utils.create_reflection_chain
   agents.reasoning_and_critique.lats.utils.format_messages_for_chain

.. py:function:: create_lats_agent(system_prompt: str = 'You are a helpful assistant that can answer questions and help with tasks.', tools: list[langchain_core.tools.BaseTool] | None = None, max_depth: int = 3, max_iterations: int = 3, n_candidates: int = 3, exploration_weight: float = 1.0, name: str = 'lats_agent', model: str = 'gpt-4o') -> Any

   Create a LATS agent with the specified configuration.

   :param system_prompt: System prompt for the agent
   :param tools: Optional list of tools for the agent to use
   :param max_depth: Maximum depth of the search tree
   :param max_iterations: Maximum number of iterations for the search
   :param n_candidates: Number of candidates to generate at each expansion
   :param exploration_weight: Weight for exploration in UCB calculation
   :param name: Name for the agent
   :param model: Model name to use

   :returns: A configured LATS agent


   .. autolink-examples:: create_lats_agent
      :collapse:

.. py:function:: create_reflection_chain() -> Any

   Create a chain for generating reflections on responses.


   .. autolink-examples:: create_reflection_chain
      :collapse:

.. py:function:: format_messages_for_chain(messages: list[Any]) -> str

   Format a list of messages as a string for input to a chain.


   .. autolink-examples:: format_messages_for_chain
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.lats.utils
   :collapse:
   
.. autolink-skip:: next
