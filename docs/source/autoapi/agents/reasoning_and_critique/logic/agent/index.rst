agents.reasoning_and_critique.logic.agent
=========================================

.. py:module:: agents.reasoning_and_critique.logic.agent


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.logic.agent.ReasoningSystem
   agents.reasoning_and_critique.logic.agent.ReasoningSystemState


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.logic.agent.create_bias_detector
   agents.reasoning_and_critique.logic.agent.create_logical_reasoner
   agents.reasoning_and_critique.logic.agent.create_premise_extractor
   agents.reasoning_and_critique.logic.agent.create_synthesis_agent
   agents.reasoning_and_critique.logic.agent.create_uncertainty_analyzer


Module Contents
---------------

.. py:class:: ReasoningSystem

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Orchestrator agent for comprehensive reasoning analysis.


   .. autolink-examples:: ReasoningSystem
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the reasoning analysis workflow graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Sync engines to the engines dict.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: bias_detector
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: logical_reasoner
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: premise_extractor
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: state_schema
      :type:  Any
      :value: None



   .. py:attribute:: synthesizer
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: uncertainty_analyzer
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



.. py:class:: ReasoningSystemState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   State for the reasoning system.


   .. autolink-examples:: ReasoningSystemState
      :collapse:

   .. py:attribute:: alternative_reasoning
      :type:  list[haive.agents.reasoning_and_critique.logic.models.ReasoningChain] | None
      :value: None



   .. py:attribute:: bias_analysis
      :type:  haive.agents.reasoning_and_critique.logic.models.ReasoningAnalysis | None
      :value: None



   .. py:attribute:: constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: evidence
      :type:  list[haive.agents.reasoning_and_critique.logic.models.Evidence]
      :value: None



   .. py:attribute:: explore_alternatives
      :type:  bool
      :value: None



   .. py:attribute:: final_report
      :type:  haive.agents.reasoning_and_critique.logic.models.ReasoningReport | None
      :value: None



   .. py:attribute:: initial_premises
      :type:  haive.agents.reasoning_and_critique.logic.models.ReasoningChain | None
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: primary_reasoning
      :type:  haive.agents.reasoning_and_critique.logic.models.ReasoningChain | None
      :value: None



   .. py:attribute:: question
      :type:  str
      :value: None



   .. py:attribute:: reasoning_depth
      :type:  int
      :value: None



   .. py:attribute:: uncertainty_analysis
      :type:  Any | None
      :value: None



.. py:function:: create_bias_detector() -> haive.core.engine.aug_llm.AugLLMConfig

   Create bias detector configuration.


   .. autolink-examples:: create_bias_detector
      :collapse:

.. py:function:: create_logical_reasoner() -> haive.core.engine.aug_llm.AugLLMConfig

   Create logical reasoner configuration.


   .. autolink-examples:: create_logical_reasoner
      :collapse:

.. py:function:: create_premise_extractor() -> haive.core.engine.aug_llm.AugLLMConfig

   Create premise extractor configuration.


   .. autolink-examples:: create_premise_extractor
      :collapse:

.. py:function:: create_synthesis_agent() -> haive.core.engine.aug_llm.AugLLMConfig

   Create synthesis agent configuration.


   .. autolink-examples:: create_synthesis_agent
      :collapse:

.. py:function:: create_uncertainty_analyzer() -> haive.core.engine.aug_llm.AugLLMConfig

   Create uncertainty analyzer configuration.


   .. autolink-examples:: create_uncertainty_analyzer
      :collapse:

