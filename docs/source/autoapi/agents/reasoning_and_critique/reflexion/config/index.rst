agents.reasoning_and_critique.reflexion.config
==============================================

.. py:module:: agents.reasoning_and_critique.reflexion.config


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflexion.config.ReflexionConfig


Module Contents
---------------

.. py:class:: ReflexionConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Reflexion agent.


   .. autolink-examples:: ReflexionConfig
      :collapse:

   .. py:method:: create_agent() -> Any
      :classmethod:



   .. py:attribute:: attempts
      :type:  int
      :value: 3



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]


   .. py:attribute:: max_iterations
      :type:  int
      :value: 5



   .. py:attribute:: models
      :type:  list[pydantic.BaseModel]


   .. py:attribute:: state_schema
      :type:  pydantic.BaseModel


   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool | collections.abc.Callable]


