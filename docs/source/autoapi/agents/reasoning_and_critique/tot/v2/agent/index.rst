agents.reasoning_and_critique.tot.v2.agent
==========================================

.. py:module:: agents.reasoning_and_critique.tot.v2.agent


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.agent.control_engine
   agents.reasoning_and_critique.tot.v2.agent.controller
   agents.reasoning_and_critique.tot.v2.agent.expander
   agents.reasoning_and_critique.tot.v2.agent.expansion_engine
   agents.reasoning_and_critique.tot.v2.agent.logger
   agents.reasoning_and_critique.tot.v2.agent.scorer
   agents.reasoning_and_critique.tot.v2.agent.scoring_engine


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.agent.control_workflow
   agents.reasoning_and_critique.tot.v2.agent.create_tree_of_thoughts
   agents.reasoning_and_critique.tot.v2.agent.expansion_workflow
   agents.reasoning_and_critique.tot.v2.agent.route_after_control_post
   agents.reasoning_and_critique.tot.v2.agent.route_after_expansion
   agents.reasoning_and_critique.tot.v2.agent.route_after_scoring
   agents.reasoning_and_critique.tot.v2.agent.route_after_scoring_prep
   agents.reasoning_and_critique.tot.v2.agent.scoring_workflow
   agents.reasoning_and_critique.tot.v2.agent.should_continue_search
   agents.reasoning_and_critique.tot.v2.agent.solve_with_tot


Module Contents
---------------

.. py:function:: control_workflow(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> dict[str, Any]

   Process control results and update state.


   .. autolink-examples:: control_workflow
      :collapse:

.. py:function:: create_tree_of_thoughts(name: str = 'TreeOfThoughts', max_depth: int = 10, beam_size: int = 3, expansion_factor: int = 5, threshold: float = 0.9, **kwargs) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create a Tree of Thoughts multi-agent system.


   .. autolink-examples:: create_tree_of_thoughts
      :collapse:

.. py:function:: expansion_workflow(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> dict[str, Any]

   Process expansion results and create candidates.


   .. autolink-examples:: expansion_workflow
      :collapse:

.. py:function:: route_after_control_post(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> str

   After control post-processing, go to controller.


   .. autolink-examples:: route_after_control_post
      :collapse:

.. py:function:: route_after_expansion(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> str

   After expansion, go to scoring workflow.


   .. autolink-examples:: route_after_expansion
      :collapse:

.. py:function:: route_after_scoring(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> str

   After scoring, go to control workflow.


   .. autolink-examples:: route_after_scoring
      :collapse:

.. py:function:: route_after_scoring_prep(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> str

   After scoring prep, go to scorer.


   .. autolink-examples:: route_after_scoring_prep
      :collapse:

.. py:function:: scoring_workflow(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> dict[str, Any]

   Process all candidates for scoring.


   .. autolink-examples:: scoring_workflow
      :collapse:

.. py:function:: should_continue_search(state: haive.agents.reasoning_and_critique.tot.v2.state.ToTState) -> str | list[langgraph.types.Send]

   After control, decide whether to continue search.


   .. autolink-examples:: should_continue_search
      :collapse:

.. py:function:: solve_with_tot(problem: str, problem_type: str | None = None, max_depth: int = 5, beam_size: int = 3, **kwargs) -> dict[str, Any]

   Solve a problem using Tree of Thoughts.


   .. autolink-examples:: solve_with_tot
      :collapse:

.. py:data:: control_engine

.. py:data:: controller

.. py:data:: expander

.. py:data:: expansion_engine

.. py:data:: logger

.. py:data:: scorer

.. py:data:: scoring_engine

