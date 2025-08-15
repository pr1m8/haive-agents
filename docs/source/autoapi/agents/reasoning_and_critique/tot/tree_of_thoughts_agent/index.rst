agents.reasoning_and_critique.tot.tree_of_thoughts_agent
========================================================

.. py:module:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent

.. autoapi-nested-parse::

   Tree of Thoughts Multi-Agent Implementation.

   This implements the complete Tree of Thoughts algorithm using MultiAgent
   with proper LangGraph routing, conditional edges, and send-based branching.


   .. autolink-examples:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TOTCommand
   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TOTIteration
   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TreeOfThoughtsAgent


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.create_tree_of_thoughts_agent


Module Contents
---------------

.. py:class:: TOTCommand(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Commands for Tree of Thoughts routing.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TOTCommand
      :collapse:

   .. py:attribute:: action
      :type:  Literal['generate', 'score', 'expand', 'select_best', 'finish']
      :value: None



   .. py:attribute:: beam_size
      :type:  int
      :value: None



   .. py:attribute:: data
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: target_node
      :type:  str | None
      :value: None



.. py:class:: TOTIteration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for a single TOT iteration.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TOTIteration
      :collapse:

   .. py:attribute:: beam_size
      :type:  int
      :value: None



   .. py:attribute:: best_candidates
      :type:  list[str]
      :value: None



   .. py:attribute:: candidates
      :type:  list[str]
      :value: None



   .. py:attribute:: iteration_number
      :type:  int
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: problem
      :type:  str
      :value: None



   .. py:attribute:: scores
      :type:  list[float]
      :value: None



.. py:class:: TreeOfThoughtsAgent(name: str = 'tree_of_thoughts', beam_size: int = 3, max_iterations: int = 3, generation_temperature: float = 0.7, scoring_temperature: float = 0.3, engine: haive.core.engine.aug_llm.AugLLMConfig | None = None)

   Tree of Thoughts agent using multi-agent coordination with conditional routing.

   Initialize Tree of Thoughts agent.

   :param name: Agent name
   :param beam_size: Number of top solutions to keep in beam search
   :param max_iterations: Maximum TOT iterations
   :param generation_temperature: Temperature for candidate generation
   :param scoring_temperature: Temperature for solution scoring
   :param engine: Optional engine configuration


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TreeOfThoughtsAgent
      :collapse:

   .. py:method:: build_graph_config() -> dict[str, Any]

      Build the graph configuration with conditional edges and routing.


      .. autolink-examples:: build_graph_config
         :collapse:


   .. py:method:: expand_candidates_node(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]
      :async:


      Expand candidates from a seed solution.


      .. autolink-examples:: expand_candidates_node
         :collapse:


   .. py:method:: finalize_result_node(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]
      :async:


      Finalize the TOT result with the best solution.


      .. autolink-examples:: finalize_result_node
         :collapse:


   .. py:method:: generate_candidates_node(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]
      :async:


      Generate initial candidate solutions.


      .. autolink-examples:: generate_candidates_node
         :collapse:


   .. py:method:: route_tot_action(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> list[langgraph.constants.Send]

      Route TOT actions using Send for parallel processing.


      .. autolink-examples:: route_tot_action
         :collapse:


   .. py:method:: score_solutions_node(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]
      :async:


      Score all candidate solutions.


      .. autolink-examples:: score_solutions_node
         :collapse:


   .. py:method:: should_continue(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> str

      Determine if TOT should continue or finish.

      :returns: "continue" to keep iterating, "finish" to end


      .. autolink-examples:: should_continue
         :collapse:


   .. py:method:: solve_problem(problem: str) -> dict[str, Any]
      :async:


      Solve a problem using Tree of Thoughts algorithm.

      :param problem: Problem statement to solve

      :returns: Dictionary with the best solution and metadata


      .. autolink-examples:: solve_problem
         :collapse:


   .. py:method:: start_node(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]
      :async:


      Initialize TOT state.


      .. autolink-examples:: start_node
         :collapse:


   .. py:method:: update_iteration_node(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]
      :async:


      Update iteration state and prepare for next iteration.


      .. autolink-examples:: update_iteration_node
         :collapse:


   .. py:attribute:: beam_size
      :value: 3



   .. py:attribute:: candidate_generator


   .. py:attribute:: engine


   .. py:attribute:: max_iterations
      :value: 3



   .. py:attribute:: name
      :value: 'tree_of_thoughts'



   .. py:attribute:: solution_scorer


.. py:function:: create_tree_of_thoughts_agent(beam_size: int = 3, max_iterations: int = 3, generation_temperature: float = 0.7, scoring_temperature: float = 0.3) -> TreeOfThoughtsAgent

   Create a Tree of Thoughts agent with default settings.

   :param beam_size: Number of top solutions to keep in beam search
   :param max_iterations: Maximum TOT iterations
   :param generation_temperature: Temperature for candidate generation
   :param scoring_temperature: Temperature for solution scoring

   :returns: Configured TreeOfThoughtsAgent


   .. autolink-examples:: create_tree_of_thoughts_agent
      :collapse:

