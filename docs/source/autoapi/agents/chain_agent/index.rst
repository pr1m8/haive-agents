agents.chain_agent
==================

.. py:module:: agents.chain_agent


Attributes
----------

.. autoapisummary::

   agents.chain_agent.logger
   agents.chain_agent.translator_prompt


Classes
-------

.. autoapisummary::

   agents.chain_agent.ChainAgent
   agents.chain_agent.ChainAgentConfig
   agents.chain_agent.ChainAgentSchema


Functions
---------

.. autoapisummary::

   agents.chain_agent.create_chain_agent


Module Contents
---------------

.. py:class:: ChainAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   An agent that chains multiple engines together, passing output from one to the next.
   Extends SimpleAgent to inherit its base functionality.


   .. autolink-examples:: ChainAgent
      :collapse:

   .. py:method:: _create_step_processor(step_idx, step_name, engine_config)

      Create a processor function for the given step.


      .. autolink-examples:: _create_step_processor
         :collapse:


   .. py:method:: _prepare_input(input_data: str | list[str] | dict[str, Any] | pydantic.BaseModel) -> Any

      Override the prepare_input method to handle chain-specific input preparation.


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up a chain workflow with multiple steps using DynamicGraph.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:class:: ChainAgentConfig

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`


   Configuration for a chain agent that processes input through multiple engines in sequence.
   Extends SimpleAgentConfig to inherit its capabilities.


   .. autolink-examples:: ChainAgentConfig
      :collapse:

   .. py:method:: from_engines(engines: list[haive.core.engine.aug_llm.AugLLMConfig], name: str | None = None, system_prompt: str | None = None, **kwargs) -> ChainAgentConfig
      :classmethod:


      Create a ChainAgentConfig from a list of AugLLMConfig engines.


      .. autolink-examples:: from_engines
         :collapse:


   .. py:attribute:: engines
      :type:  list[haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: step_names
      :type:  list[str] | None
      :value: None



.. py:class:: ChainAgentSchema

   Bases: :py:obj:`haive.agents.simple.state.SimpleAgentState`


   Schema for chain agents with intermediate results, extending SimpleAgentSchema.


   .. autolink-examples:: ChainAgentSchema
      :collapse:

   .. py:attribute:: chain_data
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: current_step
      :type:  int
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: intermediate_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: output
      :type:  str | None
      :value: None



.. py:function:: create_chain_agent(engines: list[haive.core.engine.aug_llm.AugLLMConfig], name: str | None = None, system_prompt: str | None = None, step_names: list[str] | None = None, visualize: bool = True, **kwargs) -> ChainAgent

   Create a chain agent from a list of engines.

   :param engines: List of AugLLMConfig engines to chain together
   :param name: Optional name for the agent
   :param system_prompt: Optional system prompt
   :param step_names: Optional names for each step
   :param visualize: Whether to generate a visualization
   :param \*\*kwargs: Additional configuration parameters

   :returns: ChainAgent instance


   .. autolink-examples:: create_chain_agent
      :collapse:

.. py:data:: logger

.. py:data:: translator_prompt

