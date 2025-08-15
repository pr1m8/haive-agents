agents.react_class.react_agent2.config
======================================

.. py:module:: agents.react_class.react_agent2.config


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.config.ReactAgentConfig


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.config.from_scratch


Module Contents
---------------

.. py:class:: ReactAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a React agent that follows the ReAct pattern:.
   1. Think: Reason about the current state
   2. Act: Decide on an action and execute it
   3. Observe: See the result of the action
   4. Repeat until a final answer is reached.


   .. autolink-examples:: ReactAgentConfig
      :collapse:

   .. py:method:: from_scratch(tools: dict[str, Any] | list[Any], system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, max_iterations: int = 10, max_retry_attempts: int = 3, name: str | None = None, **kwargs) -> ReactAgentConfig
      :classmethod:


      Create a ReactAgentConfig from scratch.

      :param tools: Dictionary of tool name to tool function, or list of tools
      :param system_prompt: Optional system prompt override
      :param model: Model name
      :param temperature: Temperature for the thinking LLM
      :param max_iterations: Maximum number of thinking iterations
      :param max_retry_attempts: Maximum retry attempts per tool
      :param name: Optional agent name
      :param \*\*kwargs: Additional configuration

      :returns: ReactAgentConfig instance


      .. autolink-examples:: from_scratch
         :collapse:


   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: max_retry_attempts
      :type:  int
      :value: None



   .. py:attribute:: model
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.agents.react_class.react_agent2.models.ReactState]


   .. py:attribute:: system_prompt
      :type:  str
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



   .. py:attribute:: think_llm
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: tools
      :type:  dict[str, Any] | list[Any]
      :value: None



.. py:function:: from_scratch(**kwargs)

   Module-level from_scratch function.


   .. autolink-examples:: from_scratch
      :collapse:

