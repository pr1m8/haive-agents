agents.simple.agent.v2
======================

.. py:module:: agents.simple.agent.v2

.. autoapi-nested-parse::

   Agent core module.

   This module provides agent functionality for the Haive framework.

   Classes:
       SimpleAgent: SimpleAgent implementation.
       Story: Story implementation.

   Functions:
       has_tool_calls: Has Tool Calls functionality.
       check_if_should_use_tool: Check If Should Use Tool functionality.
       placeholder_node: Placeholder Node functionality.


   .. autolink-examples:: agents.simple.agent.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.agent.v2.logger


Classes
-------

.. autoapisummary::

   agents.simple.agent.v2.SimpleAgent


Functions
---------

.. autoapisummary::

   agents.simple.agent.v2.check_if_should_use_tool
   agents.simple.agent.v2.has_tool_calls
   agents.simple.agent.v2.placeholder_node


Module Contents
---------------

.. py:class:: SimpleAgent

   Bases: :py:obj:`haive.agents.base.Agent`


   Simple agent that uses AugLLMConfig as its primary engine.

   This is the clean, minimal implementation that leverages the base Agent.
   All the complex logic is handled by the base Agent class - this just provides
   the SimpleAgent-specific convenience fields and graph building.

   The SimpleAgent is designed to be the most basic functional agent - essentially
   just Agent[AugLLMConfig] with convenience fields for common LLM parameters.

   .. attribute:: temperature

      Optional temperature for the LLM (0.0-2.0). Syncs to engine.

   .. attribute:: max_tokens

      Optional max tokens for responses. Syncs to engine.

   .. attribute:: model_name

      Optional model name override. Syncs to engine.model.

   .. attribute:: force_tool_use

      Optional flag to force tool usage. Syncs to engine.

   .. attribute:: structured_output_model

      Optional Pydantic model for structured output.

   .. attribute:: system_message

      Optional system message override. Syncs to engine.

   .. attribute:: llm_config

      Optional LLM configuration dict or object.

   .. attribute:: output_parser

      Optional parser for processing LLM output.

   .. attribute:: prompt_template

      Optional custom prompt template.

   .. rubric:: Examples

   Basic usage::

       from haive.agents.simple import SimpleAgent
       from haive.core.engine.aug_llm import AugLLMConfig

       # Create with defaults
       agent = SimpleAgent(name="assistant")
       result = agent.run("Hello, how are you?")

   With configuration::

       agent = SimpleAgent(
           name="creative_writer",
           temperature=0.9,
           max_tokens=1000,
           system_message="You are a creative writer."
       )

   With structured output::

       from pydantic import BaseModel, Field

       class Story(BaseModel):
           title: str = Field(description="Story title")
           content: str = Field(description="Story content")
           genre: str = Field(description="Story genre")

       agent = SimpleAgent(
           name="story_writer",
           structured_output_model=Story
       )
       story = agent.run("Write a short sci-fi story")
       # story will be a Story instance

   With tools::

       from langchain_core.tools import tool

       @tool
       def calculator(expression: str) -> str:
           '''Calculate mathematical expressions.'''
           return str(eval(expression))

       config = AugLLMConfig(tools=[calculator])
       agent = SimpleAgent(name="math_assistant", engine=config)
       result = agent.run("What is 15 * 23?")

   .. note::

      SimpleAgent always expects an AugLLMConfig engine. If none is provided,
      it creates one with default settings. The convenience fields (temperature,
      max_tokens, etc.) are synced to the engine during setup_agent().

   .. seealso::

      haive.agents.react.ReactAgent: For agents that need reasoning loops
      haive.agents.multi.MultiAgent: For coordinating multiple agents
      haive.core.engine.aug_llm.AugLLMConfig: The engine configuration


   .. autolink-examples:: SimpleAgent
      :collapse:

   .. py:method:: _always_needs_validation() -> bool

      Check if we always need validation (structured output or parser).


      .. autolink-examples:: _always_needs_validation
         :collapse:


   .. py:method:: _has_structured_output() -> bool

      Check if agent has structured output.


      .. autolink-examples:: _has_structured_output
         :collapse:


   .. py:method:: _has_tools() -> bool

      Check if agent has tools.


      .. autolink-examples:: _has_tools
         :collapse:


   .. py:method:: _sync_convenience_fields() -> None

      Sync convenience fields to engine.


      .. autolink-examples:: _sync_convenience_fields
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the simple agent graph.

      Creates a graph with the following structure based on agent configuration:

      1. Basic (no tools/parsing): START → agent_node → END
      2. With tools: START → agent_node → validation → tool_node → agent_node
      3. With parsing: START → agent_node → validation → parse_output → END
      4. With both: Combines tool and parsing flows

      The validation node routes between tools, parsing, or END based on
      the LLM output (tool calls, structured output needs, etc.).

      :returns: The compiled agent graph ready for execution.
      :rtype: BaseGraph

      .. note::

         This method is called automatically during agent initialization.
         The graph structure adapts based on the presence of tools,
         structured output models, or output parsers.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: ensure_aug_llm_config(v)
      :classmethod:


      Ensure engine is AugLLMConfig or create one.


      .. autolink-examples:: ensure_aug_llm_config
         :collapse:


   .. py:method:: setup_agent() -> None

      Sync convenience fields to engine and basic setup.

      This method is called during agent initialization to:
      1. Add the engine to the engines dict
      2. Sync all convenience fields to the engine
      3. Enable automatic schema generation

      The convenience fields (temperature, max_tokens, etc.) are copied
      to the engine configuration if they have non-None values.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: force_tool_use
      :type:  bool | None
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig | dict[str, Any] | None
      :value: None



   .. py:attribute:: max_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: model_name
      :type:  str | None
      :value: None



   .. py:attribute:: output_parser
      :type:  langchain_core.output_parsers.base.BaseOutputParser | None
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate | langchain_core.prompts.PromptTemplate | None
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



.. py:function:: check_if_should_use_tool(state: dict[str, Any]) -> bool

   Check if the last message has tool calls.


   .. autolink-examples:: check_if_should_use_tool
      :collapse:

.. py:function:: has_tool_calls(state: dict[str, Any]) -> Literal['true', 'false']

   Check if the last message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: placeholder_node(state: dict[str, Any])

   Placeholder node that does nothing.


   .. autolink-examples:: placeholder_node
      :collapse:

.. py:data:: logger

