agents.simple.factory
=====================

.. py:module:: agents.simple.factory

.. autoapi-nested-parse::

   Utility functions for creating and using SimpleAgent.

   This module provides helper functions for easily creating SimpleAgent instances
   with various configurations.


   .. autolink-examples:: agents.simple.factory
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/simple/factory/v2/index


Functions
---------

.. autoapisummary::

   agents.simple.factory.create_simple_agent


Module Contents
---------------

.. py:function:: create_simple_agent(name: str = 'simple_agent', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, state_schema: type[pydantic.BaseModel] = SimpleAgentState, system_prompt: str = 'You are a helpful assistant.', prompt_template: str | langchain_core.prompts.ChatPromptTemplate | None = None, input_mapping: dict[str, str] | None = None, output_mapping: dict[str, str] | None = None, model: str = 'gpt-4o', debug: bool = False, preserve_model: bool = True) -> haive.agents.simple.agent.SimpleAgent

   Create a SimpleAgent with the specified configuration.

   :param name: Name of the agent
   :param engine: LLM engine to use (created if not provided)
   :param state_schema: Schema for agent state (default: SimpleAgentState)
   :param system_prompt: System prompt for the LLM
   :param prompt_template: Custom prompt template (string or ChatPromptTemplate)
   :param input_mapping: Mapping from state to engine inputs
   :param output_mapping: Mapping from engine outputs to state
   :param model: Model to use if creating engine
   :param debug: Enable debug mode
   :param preserve_model: Whether to preserve BaseModel instances

   :returns: Configured SimpleAgent instance


   .. autolink-examples:: create_simple_agent
      :collapse:

