agents.reasoning_and_critique.mcts.agent
========================================

.. py:module:: agents.reasoning_and_critique.mcts.agent


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.mcts.agent.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.mcts.agent.MCTSAgent


Module Contents
---------------

.. py:class:: MCTSAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Monte Carlo Tree Search Agent implementation.

   This agent uses a Monte Carlo Tree Search approach to iteratively explore
   and find the best solution path.


   .. autolink-examples:: MCTSAgent
      :collapse:

   .. py:method:: _expand(state: haive.agents.reasoning_and_critique.mcts.state.TreeState, config: langchain_core.runnables.RunnableConfig) -> dict[str, Any]

      Expand the search tree by generating new candidates from the best node.


      .. autolink-examples:: _expand
         :collapse:


   .. py:method:: _generate_initial_response(state: haive.agents.reasoning_and_critique.mcts.state.TreeState) -> dict[str, Any]

      Generate the initial candidate response.


      .. autolink-examples:: _generate_initial_response
         :collapse:


   .. py:method:: _setup_chains()

      Set up the chains used by the agent.


      .. autolink-examples:: _setup_chains
         :collapse:


   .. py:method:: _should_continue(state: haive.agents.reasoning_and_critique.mcts.state.TreeState) -> str

      Determine whether to continue the tree search or exit.


      .. autolink-examples:: _should_continue
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow graph for the MCTS agent.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:data:: logger

