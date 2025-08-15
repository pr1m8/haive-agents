agents.wiki_writer.agent
========================

.. py:module:: agents.wiki_writer.agent


Classes
-------

.. autoapisummary::

   agents.wiki_writer.agent.WikiWriterAgent
   agents.wiki_writer.agent.WikiWriterAgentConfig


Module Contents
---------------

.. py:class:: WikiWriterAgent(config: WikiWriterAgentConfig = WikiWriterAgentConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentArchitecture`


   An agent that writes a wiki page.


   .. autolink-examples:: WikiWriterAgent
      :collapse:

   .. py:method:: call_agent(question: str) -> str | None
      :async:



.. py:class:: WikiWriterAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentArchitectureConfig`


   Configuration for the Wiki Writer Agent.


   .. autolink-examples:: WikiWriterAgentConfig
      :collapse:

   .. py:attribute:: aug_llm_config
      :type:  AugLLMConfig
      :value: None



   .. py:attribute:: runnable_config
      :type:  RunnableConfig
      :value: None



   .. py:attribute:: state_schema
      :type:  WikiWriterState
      :value: None



