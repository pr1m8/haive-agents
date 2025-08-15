enhanced_supervisor_agent
=========================

.. py:module:: enhanced_supervisor_agent

.. autoapi-nested-parse::

   Enhanced SupervisorAgent implementation using Agent[AugLLMConfig].

   SupervisorAgent = Agent[AugLLMConfig] + worker management + delegation.


   .. autolink-examples:: enhanced_supervisor_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   enhanced_supervisor_agent.logger


Classes
-------

.. autoapisummary::

   enhanced_supervisor_agent.MockWorker
   enhanced_supervisor_agent.SupervisorAgent


Module Contents
---------------

.. py:class:: MockWorker(name: str, specialty: str)

   .. py:method:: arun(input_data: str) -> str
      :async:



   .. py:attribute:: engine


   .. py:attribute:: name


   .. py:attribute:: specialty


.. py:class:: SupervisorAgent

   Bases: :py:obj:`haive.agents.simple.enhanced_simple_real.EnhancedAgentBase`


   Enhanced SupervisorAgent that coordinates multiple worker agents.

   SupervisorAgent = Agent[AugLLMConfig] + worker management + delegation.

   The Supervisor pattern allows:
   1. Managing a team of worker agents
   2. Delegating tasks to appropriate workers
   3. Coordinating results from multiple workers
   4. Making decisions based on worker outputs

   .. attribute:: workers

      Dictionary of worker agents

   .. attribute:: max_delegation_rounds

      Maximum rounds of delegation

   .. attribute:: delegation_strategy

      How to choose workers (first, best, all)

   .. attribute:: supervisor_prompt

      Custom prompt for supervision

   .. rubric:: Examples

   Basic supervisor with workers::

       from haive.agents.simple import SimpleAgent
       from haive.agents.react import ReactAgent

       # Create workers
       analyst = SimpleAgent(name="analyst", engine=AugLLMConfig())
       researcher = ReactAgent(name="researcher", tools=[web_search])

       # Create supervisor
       supervisor = SupervisorAgent(
           name="project_manager",
           workers={
               "analyst": analyst,
               "researcher": researcher
           }
       )

       result = supervisor.run("Analyze market trends for electric vehicles")
       # Supervisor will delegate to researcher for data, then analyst for insights

   Dynamic worker addition::

       supervisor = SupervisorAgent(name="manager")
       supervisor.add_worker("coder", CodingAgent())
       supervisor.add_worker("tester", TestingAgent())

       result = supervisor.run("Implement and test a sorting algorithm")


   .. autolink-examples:: SupervisorAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation with worker info.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _get_default_supervisor_prompt() -> str

      Get default supervisor prompt.


      .. autolink-examples:: _get_default_supervisor_prompt
         :collapse:


   .. py:method:: add_worker(name: str, agent: haive.agents.simple.enhanced_simple_real.EnhancedAgentBase) -> None

      Add a worker agent.

      :param name: Unique name for the worker
      :param agent: Worker agent instance

      :raises ValueError: If worker name already exists


      .. autolink-examples:: add_worker
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor delegation graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: ensure_aug_llm_config(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Ensure supervisor has AugLLMConfig engine.


      .. autolink-examples:: ensure_aug_llm_config
         :collapse:


   .. py:method:: get_worker(name: str) -> haive.agents.simple.enhanced_simple_real.EnhancedAgentBase | None

      Get a specific worker by name.


      .. autolink-examples:: get_worker
         :collapse:


   .. py:method:: list_workers() -> list[str]

      List all worker names.


      .. autolink-examples:: list_workers
         :collapse:


   .. py:method:: remove_worker(name: str) -> haive.agents.simple.enhanced_simple_real.EnhancedAgentBase | None

      Remove a worker agent.

      :param name: Name of worker to remove

      :returns: Removed agent or None if not found


      .. autolink-examples:: remove_worker
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup supervisor with appropriate prompt.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: validate_workers(v: dict[str, haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]) -> dict[str, haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]
      :classmethod:


      Validate worker agents.


      .. autolink-examples:: validate_workers
         :collapse:


   .. py:attribute:: allow_direct_response
      :type:  bool
      :value: None



   .. py:attribute:: delegation_strategy
      :type:  Literal['first', 'best', 'all', 'round_robin']
      :value: None



   .. py:attribute:: max_delegation_rounds
      :type:  int
      :value: None



   .. py:attribute:: max_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: supervisor_prompt
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



   .. py:attribute:: workers
      :type:  dict[str, haive.agents.simple.enhanced_simple_real.EnhancedAgentBase]
      :value: None



.. py:data:: logger

