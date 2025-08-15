agents.simple.enhanced_agent_v3.v2
==================================

.. py:module:: agents.simple.enhanced_agent_v3.v2

.. autoapi-nested-parse::

   Enhanced SimpleAgent V3 - Full feature implementation using enhanced base Agent.

   This version leverages all advanced features from the enhanced base Agent class:
   - Dynamic schema generation and composition
   - Advanced engine management and routing
   - Rich execution capabilities with debugging
   - Sophisticated state management
   - Comprehensive persistence and serialization


   .. autolink-examples:: agents.simple.enhanced_agent_v3.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.enhanced_agent_v3.v2.logger


Classes
-------

.. autoapisummary::

   agents.simple.enhanced_agent_v3.v2.EnhancedSimpleAgent


Functions
---------

.. autoapisummary::

   agents.simple.enhanced_agent_v3.v2.has_tool_calls
   agents.simple.enhanced_agent_v3.v2.should_continue


Module Contents
---------------

.. py:class:: EnhancedSimpleAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Enhanced SimpleAgent V3 with full advanced features.

   This agent leverages all capabilities of the enhanced base Agent class:

   Core Features:
   - Dynamic schema generation from engines
   - Advanced engine management and routing
   - Rich execution capabilities with detailed debugging
   - Sophisticated state management with field visibility
   - Comprehensive persistence and checkpointing
   - Full serialization support

   SimpleAgent-Specific Features:
   - AugLLMConfig engine with validation and convenience fields
   - Automatic field syncing (temperature, max_tokens, etc.)
   - Adaptive graph building based on configuration
   - Support for tools, structured output, and custom parsing

   Enhanced Capabilities:
   - Multi-engine support for advanced workflows
   - Advanced tool routing and state management
   - Rich debugging and observability features
   - Dynamic schema evolution and composition
   - Performance optimization and caching

   .. attribute:: engine

      Primary AugLLMConfig engine (required)

   .. attribute:: temperature

      LLM temperature (syncs to engine)

   .. attribute:: max_tokens

      Maximum response tokens (syncs to engine)

   .. attribute:: model_name

      Model name override (syncs to engine.model)

   .. attribute:: force_tool_use

      Force tool usage flag (syncs to engine)

   .. attribute:: structured_output_model

      Pydantic model for structured output

   .. attribute:: system_message

      System message override (syncs to engine)

   .. attribute:: llm_config

      LLM configuration dict or object

   .. attribute:: output_parser

      Custom output parser

   .. attribute:: prompt_template

      Custom prompt template

   Enhanced Features:
       multi_engine_mode: Enable multiple engines per agent
       advanced_routing: Enable sophisticated tool/engine routing
       performance_mode: Enable caching and optimization
       debug_mode: Enable rich debugging and observability
       persistence_config: Advanced persistence configuration

   .. rubric:: Examples

   Basic usage (backwards compatible)::

       agent = EnhancedSimpleAgent(name="assistant")
       result = agent.run("Hello, how are you?")

   With enhanced features::

       agent = EnhancedSimpleAgent(
           name="advanced_agent",
           temperature=0.7,
           max_tokens=1000,
           system_message="You are an expert assistant",
           multi_engine_mode=True,
           debug_mode=True,
           persistence_config={"checkpoint_mode": "async"}
       )

   With structured output::

       class Analysis(BaseModel):
           summary: str = Field(description="Analysis summary")
           confidence: float = Field(description="Confidence score")
           recommendations: list[str] = Field(description="Recommendations")

       agent = EnhancedSimpleAgent(
           name="analyzer",
           structured_output_model=Analysis,
           performance_mode=True
       )
       analysis = agent.run("Analyze the current market trends")

   Multi-engine configuration::

       agent = EnhancedSimpleAgent(
           name="multi_engine_agent",
           engines={
               "primary": AugLLMConfig(model="gpt-4", temperature=0.3),
               "creative": AugLLMConfig(model="gpt-4", temperature=0.9),
               "fallback": AugLLMConfig(model="gpt-3.5-turbo")
           },
           advanced_routing=True
       )


   .. autolink-examples:: EnhancedSimpleAgent
      :collapse:

   .. py:method:: __repr__() -> str

      Enhanced string representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _always_needs_validation() -> bool

      Check if we always need validation routing.


      .. autolink-examples:: _always_needs_validation
         :collapse:


   .. py:method:: _has_structured_output() -> bool

      Check if agent has structured output configured.


      .. autolink-examples:: _has_structured_output
         :collapse:


   .. py:method:: _has_tools() -> bool

      Check if agent has tools available.


      .. autolink-examples:: _has_tools
         :collapse:


   .. py:method:: _setup_advanced_persistence() -> None

      Setup advanced persistence configuration.


      .. autolink-examples:: _setup_advanced_persistence
         :collapse:


   .. py:method:: _setup_advanced_routing() -> None

      Setup advanced tool and engine routing.


      .. autolink-examples:: _setup_advanced_routing
         :collapse:


   .. py:method:: _setup_debug_mode() -> None

      Setup rich debugging and observability.


      .. autolink-examples:: _setup_debug_mode
         :collapse:


   .. py:method:: _setup_multi_engine_mode() -> None

      Setup multi-engine capabilities.


      .. autolink-examples:: _setup_multi_engine_mode
         :collapse:


   .. py:method:: _setup_performance_mode() -> None

      Setup performance optimizations.


      .. autolink-examples:: _setup_performance_mode
         :collapse:


   .. py:method:: _sync_convenience_fields() -> None

      Sync convenience fields to engine with validation.


      .. autolink-examples:: _sync_convenience_fields
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build enhanced graph with adaptive features.

      Creates an intelligent graph structure that adapts based on:
      - Available tools and their routing requirements
      - Structured output models and parsing needs
      - Performance optimizations and caching
      - Debug mode and observability requirements

      Graph Structure:
      1. Basic: START → agent_node → END
      2. With tools: START → agent_node → validation → tool_node → agent_node
      3. With parsing: START → agent_node → validation → parse_output → END
      4. Enhanced: Includes performance optimizations and debug nodes

      :returns: The compiled agent graph with all enhancements
      :rtype: BaseGraph


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: display_capabilities() -> None

      Display comprehensive capabilities summary.


      .. autolink-examples:: display_capabilities
         :collapse:


   .. py:method:: ensure_aug_llm_config(v)
      :classmethod:


      Ensure engine is AugLLMConfig or create one.


      .. autolink-examples:: ensure_aug_llm_config
         :collapse:


   .. py:method:: get_capabilities_summary() -> dict[str, Any]

      Get comprehensive summary of agent capabilities.


      .. autolink-examples:: get_capabilities_summary
         :collapse:


   .. py:method:: setup_agent() -> None

      Enhanced setup with full feature integration.

      This setup method:
      1. Configures the primary engine and adds to engines dict
      2. Syncs all convenience fields to the engine
      3. Sets up multi-engine mode if enabled
      4. Configures advanced routing if enabled
      5. Sets up performance optimizations if enabled
      6. Configures debug mode if enabled
      7. Sets up advanced persistence if configured
      8. Enables automatic schema generation


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: validate_temperature(v)
      :classmethod:


      Validate temperature range.


      .. autolink-examples:: validate_temperature
         :collapse:


   .. py:attribute:: advanced_routing
      :type:  bool
      :value: None



   .. py:attribute:: debug_mode
      :type:  bool
      :value: None



   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



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



   .. py:attribute:: multi_engine_mode
      :type:  bool
      :value: None



   .. py:attribute:: output_parser
      :type:  langchain_core.output_parsers.base.BaseOutputParser | None
      :value: None



   .. py:attribute:: performance_mode
      :type:  bool
      :value: None



   .. py:attribute:: persistence_config
      :type:  dict[str, Any] | None
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



.. py:function:: has_tool_calls(state: dict[str, Any]) -> Literal['true', 'false']

   Check if the last message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: should_continue(state: dict[str, Any]) -> bool

   Enhanced routing logic for tool calls and structured output.


   .. autolink-examples:: should_continue
      :collapse:

.. py:data:: logger

