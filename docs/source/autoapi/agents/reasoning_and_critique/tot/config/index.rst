agents.reasoning_and_critique.tot.config
========================================

.. py:module:: agents.reasoning_and_critique.tot.config

.. autoapi-nested-parse::

   Configuration for the Tree of Thoughts agent.

   This module defines the configuration schema for the ToT agent,
   including engine configurations, algorithm parameters, and state schema.


   .. autolink-examples:: agents.reasoning_and_critique.tot.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.tot.config.T


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.config.TOTAgentConfig


Module Contents
---------------

.. py:class:: TOTAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Tree of Thoughts agent.

   This configuration specifies the LLM engines used for generation and scoring,
   as well as the parameters for the search algorithm.


   .. autolink-examples:: TOTAgentConfig
      :collapse:

   .. py:method:: create_for_problem_type(content_type: str = 'string', **kwargs) -> TOTAgentConfig
      :classmethod:


      Create a TOT agent configuration specialized for a specific problem type.

      :param content_type: Type of content ('string', 'equation', etc.)
      :param \*\*kwargs: Additional configuration parameters

      :returns: Configured TOTAgentConfig


      .. autolink-examples:: create_for_problem_type
         :collapse:


   .. py:method:: get_engine(engine_key: str) -> haive.core.engine.aug_llm.AugLLMConfig

      Get an engine by key from the engines dictionary.

      :param engine_key: Key of the engine to retrieve

      :returns: The requested engine configuration

      :raises KeyError: If the engine key is not found


      .. autolink-examples:: get_engine
         :collapse:


   .. py:attribute:: beam_width
      :type:  int
      :value: None



   .. py:attribute:: content_type_name
      :type:  str
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: evaluator_node
      :type:  str
      :value: None



   .. py:attribute:: evaluator_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: expansion_count
      :type:  int
      :value: None



   .. py:attribute:: generator_node
      :type:  str
      :value: None



   .. py:attribute:: generator_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: input_schema
      :type:  type[haive.agents.reasoning_and_critique.tot.state.TOTInput]
      :value: None



   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: output_schema
      :type:  type[haive.agents.reasoning_and_critique.tot.state.TOTOutput]
      :value: None



   .. py:attribute:: parallel_evaluation
      :type:  bool
      :value: None



   .. py:attribute:: parallel_expansion
      :type:  bool
      :value: None



   .. py:attribute:: selector_node
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.agents.reasoning_and_critique.tot.state.TOTState]
      :value: None



   .. py:attribute:: threshold
      :type:  float
      :value: None



   .. py:attribute:: use_structured_output
      :type:  bool
      :value: None



.. py:data:: T

