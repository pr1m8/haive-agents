agents.multi.enhanced_sequential_agent
======================================

.. py:module:: agents.multi.enhanced_sequential_agent

.. autoapi-nested-parse::

   Enhanced SequentialAgent implementation using Agent[AugLLMConfig].

   SequentialAgent = Agent[AugLLMConfig] + sequential execution of agents.


   .. autolink-examples:: agents.multi.enhanced_sequential_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.enhanced_sequential_agent.logger


Classes
-------

.. autoapisummary::

   agents.multi.enhanced_sequential_agent.MockAgent
   agents.multi.enhanced_sequential_agent.SequentialAgent


Module Contents
---------------

.. py:class:: MockAgent(name: str, transform: str)

   .. py:method:: arun(input_data: str) -> str
      :async:



   .. py:attribute:: engine


   .. py:attribute:: name


   .. py:attribute:: transform


.. py:class:: SequentialAgent

   Bases: :py:obj:`haive.agents.simple.enhanced_simple_real.EnhancedAgentBase`


   Enhanced SequentialAgent that executes agents in sequence.

   SequentialAgent = Agent[AugLLMConfig] + sequential pipeline execution.

   Each agent's output becomes the next agent's input, creating a pipeline.
   The coordinator (this agent) can optionally process results between steps.

   .. attribute:: agents

      List of agents to execute in order

   .. attribute:: process_between_steps

      Whether to process between agent calls

   .. attribute:: continue_on_error

      Whether to continue if an agent fails

   .. attribute:: return_all_outputs

      Return all intermediate outputs vs just final

   .. rubric:: Examples

   Simple pipeline::

       # Create pipeline: Researcher -> Analyst -> Writer
       pipeline = SequentialAgent(
           name="report_pipeline",
           agents=[
               ResearchAgent(name="researcher"),
               AnalystAgent(name="analyst"),
               WriterAgent(name="writer")
           ]
       )

       result = pipeline.run("Create report on AI trends")
       # Researcher finds data -> Analyst processes -> Writer creates report

   With intermediate processing::

       pipeline = SequentialAgent(
           name="enhanced_pipeline",
           agents=[research_agent, analysis_agent],
           process_between_steps=True,
           system_message="Enhance and clarify outputs between steps"
       )

       # Coordinator enhances outputs between each step


   .. autolink-examples:: SequentialAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation with pipeline info.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _get_coordinator_prompt() -> str

      Get coordinator prompt for processing between steps.


      .. autolink-examples:: _get_coordinator_prompt
         :collapse:


   .. py:method:: add_agent(agent: haive.agents.simple.enhanced_simple_real.EnhancedAgentBase) -> None

      Add an agent to the end of the sequence.

      :param agent: Agent to add to pipeline


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build sequential execution graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: execute_sequence(input_data: Any) -> Any | list[Any]
      :async:


      Execute agents in sequence.

      :param input_data: Initial input for the pipeline

      :returns: Final output or list of all outputs


      .. autolink-examples:: execute_sequence
         :collapse:


   .. py:method:: get_pipeline_description() -> str

      Get human-readable pipeline description.


      .. autolink-examples:: get_pipeline_description
         :collapse:


   .. py:method:: insert_agent(index: int, agent: haive.agents.simple.enhanced_simple_real.EnhancedAgentBase) -> None

      Insert an agent at specific position.

      :param index: Position to insert at
      :param agent: Agent to insert


      .. autolink-examples:: insert_agent
         :collapse:


   .. py:method:: remove_agent(index: int) -> haive.agents.simple.enhanced_simple_real.EnhancedAgentBase | None

      Remove agent at index.

      :param index: Position to remove from

      :returns: Removed agent or None


      .. autolink-examples:: remove_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup sequential coordinator.


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



   .. py:attribute:: continue_on_error
      :type:  bool
      :value: None



   .. py:attribute:: max_retries_per_step
      :type:  int
      :value: None



   .. py:attribute:: process_between_steps
      :type:  bool
      :value: None



   .. py:attribute:: return_all_outputs
      :type:  bool
      :value: None



   .. py:attribute:: step_timeout
      :type:  float | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



.. py:data:: logger

