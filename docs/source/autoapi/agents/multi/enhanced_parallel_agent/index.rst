agents.multi.enhanced_parallel_agent
====================================

.. py:module:: agents.multi.enhanced_parallel_agent

.. autoapi-nested-parse::

   Enhanced ParallelAgent implementation using Agent[AugLLMConfig].

   ParallelAgent = Agent[AugLLMConfig] + parallel execution of agents.


   .. autolink-examples:: agents.multi.enhanced_parallel_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.enhanced_parallel_agent.logger


Classes
-------

.. autoapisummary::

   agents.multi.enhanced_parallel_agent.MockExpert
   agents.multi.enhanced_parallel_agent.ParallelAgent


Module Contents
---------------

.. py:class:: MockExpert(name: str, specialty: str)

   .. py:method:: arun(input_data: str) -> str
      :async:



   .. py:attribute:: engine


   .. py:attribute:: name


   .. py:attribute:: specialty


.. py:class:: ParallelAgent

   Bases: :py:obj:`haive.agents.simple.enhanced_simple_real.EnhancedAgentBase`


   Enhanced ParallelAgent that executes agents concurrently.

   ParallelAgent = Agent[AugLLMConfig] + parallel execution + result aggregation.

   All agents receive the same input and execute concurrently. Results can be
   aggregated using various strategies (all, first, best, majority).

   .. attribute:: agents

      List of agents to execute in parallel

   .. attribute:: aggregation_strategy

      How to combine results

   .. attribute:: timeout_per_agent

      Timeout for each agent

   .. attribute:: min_agents_for_consensus

      Minimum agents for consensus strategies

   .. rubric:: Examples

   Parallel analysis with multiple experts::

       experts = ParallelAgent(
           name="expert_panel",
           agents=[
               FinanceExpert(),
               TechExpert(),
               MarketExpert()
           ],
           aggregation_strategy="all"
       )

       # All experts analyze simultaneously
       results = experts.run("Analyze startup investment opportunity")

   Consensus-based decision making::

       validators = ParallelAgent(
           name="validation_ensemble",
           agents=[Validator1(), Validator2(), Validator3()],
           aggregation_strategy="majority",
           min_agents_for_consensus=2
       )

       # Returns majority consensus
       decision = validators.run("Is this transaction valid?")


   .. autolink-examples:: ParallelAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation with parallel info.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _aggregate_results(results: list[tuple[int, Any]], original_input: Any) -> list[Any] | Any
      :async:


      Aggregate results based on strategy.

      :param results: List of (agent_index, result) tuples
      :param original_input: Original input for context

      :returns: Aggregated result


      .. autolink-examples:: _aggregate_results
         :collapse:


   .. py:method:: _get_merge_prompt() -> str

      Get prompt for merging results.


      .. autolink-examples:: _get_merge_prompt
         :collapse:


   .. py:method:: add_agent(agent: haive.agents.simple.enhanced_simple_real.EnhancedAgentBase) -> None

      Add an agent to the parallel group.

      :param agent: Agent to add


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build parallel execution graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: execute_parallel(input_data: Any) -> list[Any] | Any
      :async:


      Execute all agents in parallel.

      :param input_data: Input for all agents

      :returns: Aggregated results based on strategy


      .. autolink-examples:: execute_parallel
         :collapse:


   .. py:method:: remove_agent(agent: haive.agents.simple.enhanced_simple_real.EnhancedAgentBase) -> bool

      Remove an agent from the parallel group.

      :param agent: Agent to remove

      :returns: True if removed, False if not found


      .. autolink-examples:: remove_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup parallel coordinator.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: validate_agents(v: list[haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]) -> list[haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]
      :classmethod:


      Validate agent list.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:attribute:: agents
      :type:  list[haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]
      :value: None



   .. py:attribute:: aggregation_strategy
      :type:  Literal['all', 'first', 'best', 'majority', 'merge']
      :value: None



   .. py:attribute:: continue_on_timeout
      :type:  bool
      :value: None



   .. py:attribute:: merge_with_llm
      :type:  bool
      :value: None



   .. py:attribute:: min_agents_for_consensus
      :type:  int
      :value: None



   .. py:attribute:: quality_scorer
      :type:  Any | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



   .. py:attribute:: timeout_per_agent
      :type:  float | None
      :value: None



.. py:data:: logger

