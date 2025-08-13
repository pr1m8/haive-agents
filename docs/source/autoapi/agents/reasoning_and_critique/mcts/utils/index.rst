
:py:mod:`agents.reasoning_and_critique.mcts.utils`
==================================================

.. py:module:: agents.reasoning_and_critique.mcts.utils



Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.mcts.utils.create_mcts_agent
   agents.reasoning_and_critique.mcts.utils.extract_best_solution
   agents.reasoning_and_critique.mcts.utils.print_tree_stats

.. py:function:: create_mcts_agent(tools: list[langchain_core.tools.BaseTool] | None = None, llm_config: haive.core.models.llm.base.LLMConfig | None = None, system_prompt: str | None = None, max_rollouts: int = 5, candidates_per_rollout: int = 5, exploration_weight: float = 1.0, name: str | None = None, **kwargs) -> haive.agents.reasoning_and_critique.mcts.agent.MCTSAgent

   Create a Monte Carlo Tree Search agent.

   :param tools: List of tools available to the agent
   :param llm_config: Configuration for the LLM
   :param system_prompt: System prompt for the agent
   :param max_rollouts: Maximum depth of rollouts
   :param candidates_per_rollout: Number of candidates to generate per rollout
   :param exploration_weight: Exploration weight for UCB calculation
   :param name: Name for the agent
   :param \*\*kwargs: Additional configuration parameters

   :returns: MCTSAgent instance


   .. autolink-examples:: create_mcts_agent
      :collapse:

.. py:function:: extract_best_solution(result: dict[str, Any]) -> dict[str, Any] | None

   Extract the best solution from an MCTS agent result.

   :param result: Result from an MCTS agent run

   :returns: Dictionary with best solution data, or None if no solution found


   .. autolink-examples:: extract_best_solution
      :collapse:

.. py:function:: print_tree_stats(result: dict[str, Any]) -> None

   Print statistics about the MCTS search tree.

   :param result: Result from an MCTS agent run


   .. autolink-examples:: print_tree_stats
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.mcts.utils
   :collapse:
   
.. autolink-skip:: next
