agents.wiki_writer.interview.agent
==================================

.. py:module:: agents.wiki_writer.interview.agent


Classes
-------

.. autoapisummary::

   agents.wiki_writer.interview.agent.InterviewAgent
   agents.wiki_writer.interview.agent.InterviewAgentConfig


Module Contents
---------------

.. py:class:: InterviewAgent(config: InterviewAgentConfig = InterviewAgentConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentArchitecture`


   An agent that conducts an interview with a Subject Matter Expert.


   .. autolink-examples:: InterviewAgent
      :collapse:

   .. py:method:: setup_workflow() -> None

      Setup the workflow for the agent.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:class:: InterviewAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentArchitectureConfig`


   Configuration for the Interview Agent.


   .. autolink-examples:: InterviewAgentConfig
      :collapse:

   .. py:attribute:: aug_llm_configs
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: state_schema
      :type:  haive.agents.wiki_writer.interview.state.InterviewState
      :value: None



