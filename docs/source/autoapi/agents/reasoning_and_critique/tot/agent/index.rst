agents.reasoning_and_critique.tot.agent
=======================================

.. py:module:: agents.reasoning_and_critique.tot.agent

.. autoapi-nested-parse::

   Tree of Thoughts (ToT) agent implementation.

   This module implements the Tree of Thoughts algorithm as a Haive agent.


   .. autolink-examples:: agents.reasoning_and_critique.tot.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agent.T
   agents.reasoning_and_critique.tot.agent.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agent.ToTAgent


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agent.compose_evaluator_runnable
   agents.reasoning_and_critique.tot.agent.compose_generator_runnable
   agents.reasoning_and_critique.tot.agent.create_evaluator_engine
   agents.reasoning_and_critique.tot.agent.create_generator_engine


Module Contents
---------------

.. py:class:: ToTAgent(config: haive.agents.reasoning_and_critique.tot.config.TOTAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.reasoning_and_critique.tot.config.TOTAgentConfig`\ ], :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Tree of Thoughts agent implementation.

   This agent implements the Tree of Thoughts search algorithm, which:
   1. Generates candidate solutions
   2. Scores the candidates
   3. Selects the best candidates for further exploration
   4. Repeats until a satisfactory solution is found or max depth reached

   The implementation supports parallel processing of candidates through beam search.

   Initialize the ToT agent.

   :param config: Configuration for the ToT agent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToTAgent
      :collapse:

   .. py:method:: _collect_evaluations(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> langgraph.types.Command

      Collect all the evaluated candidates.

      :param state: Current state with individual evaluations

      :returns: Command with collected scored candidates


      .. autolink-examples:: _collect_evaluations
         :collapse:


   .. py:method:: _evaluate_candidate(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> langgraph.types.Command
      :async:


      Evaluate a single candidate solution.

      :param state: State containing a single candidate to evaluate

      :returns: Command with evaluation results


      .. autolink-examples:: _evaluate_candidate
         :collapse:


   .. py:method:: _generate_candidates(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> langgraph.types.Command
      :async:


      Generate candidate solutions for the problem.

      :param state: Current search state

      :returns: Command with candidate updates


      .. autolink-examples:: _generate_candidates
         :collapse:


   .. py:method:: _map_beam_expansion(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> Literal['__end__'] | list[langgraph.types.Send]

      Map beam candidates to parallel expansion nodes.

      :param state: Current search state

      :returns: List of Send commands for parallel expansion or END


      .. autolink-examples:: _map_beam_expansion
         :collapse:


   .. py:method:: _map_candidates_to_evaluation(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> list[langgraph.types.Send]

      Map candidates to parallel evaluation nodes.

      :param state: Current search state

      :returns: List of Send commands for parallel evaluation


      .. autolink-examples:: _map_candidates_to_evaluation
         :collapse:


   .. py:method:: _score_candidates(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> langgraph.types.Command
      :async:


      Score all candidates sequentially.

      :param state: Current search state

      :returns: Command with scored candidate updates


      .. autolink-examples:: _score_candidates
         :collapse:


   .. py:method:: _select_best(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> langgraph.types.Command

      Select the best candidates for the next iteration.

      :param state: Current search state

      :returns: Command with best candidate updates


      .. autolink-examples:: _select_best
         :collapse:


   .. py:method:: _setup_runnables()

      Set up the generator and evaluator runnables.


      .. autolink-examples:: _setup_runnables
         :collapse:


   .. py:method:: _should_continue_search(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> str

      Decide whether to continue the search.

      :param state: Current search state

      :returns: Route key for next step


      .. autolink-examples:: _should_continue_search
         :collapse:


   .. py:method:: _should_expand_or_finish(state: haive.agents.reasoning_and_critique.tot.state.TOTState) -> str

      Decide whether to expand candidates or finish.

      :param state: Current search state

      :returns: Route key for next step


      .. autolink-examples:: _should_expand_or_finish
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the Tree of Thoughts workflow using the DynamicGraph builder.

      This creates a graph with nodes for:
      1. Generating candidate solutions
      2. Scoring candidates
      3. Selecting the best candidates for beam search
      4. Expanding new generations from those candidates


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: beam_width


   .. py:attribute:: evaluator_output_model


   .. py:attribute:: expansion_count


   .. py:attribute:: generator_output_model


   .. py:attribute:: max_depth


   .. py:attribute:: parallel_evaluation


   .. py:attribute:: parallel_expansion


   .. py:attribute:: threshold


   .. py:attribute:: use_structured_output


.. py:function:: compose_evaluator_runnable(engine, use_structured_output=False)

   Create evaluator runnable.


   .. autolink-examples:: compose_evaluator_runnable
      :collapse:

.. py:function:: compose_generator_runnable(engine, use_structured_output=False)

   Create generator runnable.


   .. autolink-examples:: compose_generator_runnable
      :collapse:

.. py:function:: create_evaluator_engine(engine, use_structured_output=False, output_model=None)

   Create evaluator engine configuration.


   .. autolink-examples:: create_evaluator_engine
      :collapse:

.. py:function:: create_generator_engine(engine, use_structured_output=False, output_model=None)

   Create generator engine configuration.


   .. autolink-examples:: create_generator_engine
      :collapse:

.. py:data:: T

.. py:data:: logger

