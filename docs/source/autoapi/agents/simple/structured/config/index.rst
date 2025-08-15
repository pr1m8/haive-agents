agents.simple.structured.config
===============================

.. py:module:: agents.simple.structured.config


Classes
-------

.. autoapisummary::

   agents.simple.structured.config.StructuredOutputAgentConfig


Module Contents
---------------

.. py:class:: StructuredOutputAgentConfig

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`


   Configuration for a structured output agent.

   Automatically sets up a single StructuredOutputTool for the provided model
   and configures the engine to always use this tool.


   .. autolink-examples:: StructuredOutputAgentConfig
      :collapse:

   .. py:method:: validate_and_setup() -> Any

      Set up the structured output tool and configure the engine.


      .. autolink-examples:: validate_and_setup
         :collapse:


   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: output_parser
      :type:  langchain_core.output_parsers.PydanticOutputParser
      :value: None



   .. py:attribute:: output_schema


   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel]


