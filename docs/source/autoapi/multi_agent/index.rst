multi_agent
===========

.. py:module:: multi_agent


Attributes
----------

.. autoapisummary::

   multi_agent.logger


Classes
-------

.. autoapisummary::

   multi_agent.MultiAgent


Module Contents
---------------

.. py:class:: MultiAgent

   Bases: :py:obj:`haive.agents.base.Agent`


   Multi-agent coordinator that manages multiple agents.

   This is a clean implementation that orchestrates multiple agents
   in sequence, parallel, or conditional execution patterns.

   The MultiAgent provides three execution modes:
   - sequence: Agents execute one after another
   - parallel: All agents execute simultaneously
   - conditional: A coordinator LLM routes to appropriate agents

   .. attribute:: agents

      Dictionary of agents to coordinate by name.

   .. attribute:: execution_mode

      How to execute agents (sequence/parallel/conditional).

   .. attribute:: coordinator_config

      Optional LLM config for conditional routing.

   .. rubric:: Examples

   Sequential execution::

       from haive.agents.multi import MultiAgent
       from haive.agents.simple import SimpleAgent

       writer = SimpleAgent(name="writer")
       editor = SimpleAgent(name="editor")

       pipeline = MultiAgent(
           name="content_pipeline",
           agents={"writer": writer, "editor": editor},
           execution_mode="sequence"
       )
       result = pipeline.run("Write and edit a blog post about AI")

   Parallel execution::

       analyzer1 = SimpleAgent(name="sentiment")
       analyzer2 = SimpleAgent(name="keywords")
       analyzer3 = SimpleAgent(name="summary")

       parallel = MultiAgent(
           name="text_analysis",
           agents={
               "sentiment": analyzer1,
               "keywords": analyzer2,
               "summary": analyzer3
           },
           execution_mode="parallel"
       )
       results = parallel.run("Analyze this text...")

   Conditional routing::

       from haive.core.engine.aug_llm import AugLLMConfig

       coder = SimpleAgent(name="coder")
       writer = SimpleAgent(name="writer")

       router = MultiAgent(
           name="smart_assistant",
           agents={"coder": coder, "writer": writer},
           execution_mode="conditional",
           coordinator_config=AugLLMConfig(temperature=0.1)
       )
       # Coordinator will route to appropriate agent
       result = router.run("Write a Python function to sort a list")

   .. note::

      In conditional mode, the coordinator LLM decides which agent to use
      based on the input. The routing is done by simple name matching in
      the coordinator's response.

   .. seealso::

      haive.agents.supervisor.SupervisorAgent: More advanced routing logic
      haive.agents.simple.SimpleAgent: Basic agent implementation


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: _build_conditional_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build conditional execution graph with coordinator.


      .. autolink-examples:: _build_conditional_graph
         :collapse:


   .. py:method:: _build_parallel_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build parallel execution graph.


      .. autolink-examples:: _build_parallel_graph
         :collapse:


   .. py:method:: _build_sequence_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build sequential execution graph.


      .. autolink-examples:: _build_sequence_graph
         :collapse:


   .. py:method:: add_agent(name: str, agent: haive.agents.base.Agent) -> None

      Add an agent to the multi-agent system.

      :param name: Unique name for the agent.
      :param agent: The agent instance to add.

      .. note::

         The graph is not automatically rebuilt after adding agents.
         You may need to rebuild the graph for changes to take effect.


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build multi-agent coordination graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_agent(name: str) -> haive.agents.base.Agent | None

      Get an agent by name.

      :param name: Name of the agent to retrieve.

      :returns: The agent instance or None if not found.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: remove_agent(name: str) -> None

      Remove an agent from the system.

      :param name: Name of the agent to remove.

      .. note::

         Does nothing if the agent doesn't exist.
         The graph is not automatically rebuilt.


      .. autolink-examples:: remove_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup multi-agent coordination.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: agents
      :type:  dict[str, haive.agents.base.Agent]
      :value: None



   .. py:attribute:: coordinator_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



.. py:data:: logger

