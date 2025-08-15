agents.patterns.react_structured_agent_variants
===============================================

.. py:module:: agents.patterns.react_structured_agent_variants

.. autoapi-nested-parse::

   React Structured Agent Variants - Building on base Agent patterns.

   This module creates various ReactAgent → SimpleAgent patterns using the base
   agent.py architecture, as requested. Shows different ways to combine agents
   for structured workflows with reasoning and output formatting.

   Variants include:
   1. Basic React → Simple structured flow
   2. Multi-stage reasoning with structured outputs
   3. Tool-enhanced React → Simple patterns
   4. Reflection-enabled variants


   .. autolink-examples:: agents.patterns.react_structured_agent_variants
      :collapse:


Classes
-------

.. autoapisummary::

   agents.patterns.react_structured_agent_variants.AnalysisResult
   agents.patterns.react_structured_agent_variants.MultiStageReasoningAgent
   agents.patterns.react_structured_agent_variants.ReactToStructuredAgent
   agents.patterns.react_structured_agent_variants.ReflectiveStructuredAgent
   agents.patterns.react_structured_agent_variants.StructuredSolution
   agents.patterns.react_structured_agent_variants.ToolEnhancedStructuredAgent


Functions
---------

.. autoapisummary::

   agents.patterns.react_structured_agent_variants.create_multi_stage_reasoning_agent
   agents.patterns.react_structured_agent_variants.create_react_structured_agent
   agents.patterns.react_structured_agent_variants.create_reflective_structured_agent
   agents.patterns.react_structured_agent_variants.create_tool_enhanced_agent
   agents.patterns.react_structured_agent_variants.example_basic_react_structured
   agents.patterns.react_structured_agent_variants.example_multi_stage
   agents.patterns.react_structured_agent_variants.example_reflective


Module Contents
---------------

.. py:class:: AnalysisResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured analysis from reasoning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnalysisResult
      :collapse:

   .. py:attribute:: analysis_approach
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: findings
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: key_factors
      :type:  list[str]
      :value: None



   .. py:attribute:: problem_statement
      :type:  str
      :value: None



.. py:class:: MultiStageReasoningAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Multi-stage reasoning with structured outputs at each stage.

   This pattern chains multiple reasoning stages, each producing
   structured outputs that feed into the next stage.


   .. autolink-examples:: MultiStageReasoningAgent
      :collapse:

   .. py:method:: _create_validator_tool()

      Create validation tool.


      .. autolink-examples:: _create_validator_tool
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build multi-stage graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup multi-stage reasoning pipeline.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: stages
      :type:  list[dict[str, Any]]
      :value: None



.. py:class:: ReactToStructuredAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   React → Structured output agent pattern.

   This agent combines ReactAgent for reasoning with SimpleAgentV3 for
   structured output generation, following the base Agent pattern.

   .. rubric:: Example

   >>> agent = ReactToStructuredAgent(
   ...     name="analyzer",
   ...     tools=[calculator, search_tool],
   ...     output_model=AnalysisResult,
   ...     debug=True
   ... )
   >>> result = await agent.arun("Analyze market trends")


   .. autolink-examples:: ReactToStructuredAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build React → Structured graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup React and Simple agents.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: output_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: react_agent
      :type:  haive.agents.react.agent.ReactAgent
      :value: None



   .. py:attribute:: reasoning_temperature
      :type:  float
      :value: None



   .. py:attribute:: structure_agent
      :type:  SimpleAgentV3
      :value: None



   .. py:attribute:: structuring_temperature
      :type:  float
      :value: None



   .. py:attribute:: tools
      :type:  list[Any]
      :value: None



.. py:class:: ReflectiveStructuredAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   React → Structured → Reflection pattern.

   This adds a reflection stage that reviews and improves the
   structured output before final delivery.


   .. autolink-examples:: ReflectiveStructuredAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph with optional reflection.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup reasoning, structuring, and reflection agents.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: include_reflection
      :type:  bool
      :value: None



   .. py:attribute:: output_model
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: StructuredSolution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured solution output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructuredSolution
      :collapse:

   .. py:attribute:: implementation_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: requirements
      :type:  list[str]
      :value: None



   .. py:attribute:: risks
      :type:  list[str]
      :value: None



   .. py:attribute:: solution_summary
      :type:  str
      :value: None



   .. py:attribute:: success_metrics
      :type:  list[str]
      :value: None



.. py:class:: ToolEnhancedStructuredAgent

   Bases: :py:obj:`ReactToStructuredAgent`


   Enhanced React → Structured agent with specialized tools.

   This variant adds domain-specific tools for enhanced reasoning.


   .. autolink-examples:: ToolEnhancedStructuredAgent
      :collapse:

   .. py:method:: setup_agent() -> None

      Setup with enhanced tools.


      .. autolink-examples:: setup_agent
         :collapse:


.. py:function:: create_multi_stage_reasoning_agent(name: str = 'multi_stage', stages: list[dict[str, Any]] | None = None, debug: bool = True) -> MultiStageReasoningAgent

   Create a multi-stage reasoning agent.


   .. autolink-examples:: create_multi_stage_reasoning_agent
      :collapse:

.. py:function:: create_react_structured_agent(name: str = 'react_structured', tools: list[Any] | None = None, output_model: type[pydantic.BaseModel] = StructuredSolution, debug: bool = True) -> ReactToStructuredAgent

   Create a React → Structured agent.


   .. autolink-examples:: create_react_structured_agent
      :collapse:

.. py:function:: create_reflective_structured_agent(name: str = 'reflective', include_reflection: bool = True, output_model: type[pydantic.BaseModel] = StructuredSolution, debug: bool = True) -> ReflectiveStructuredAgent

   Create a reflective structured agent.


   .. autolink-examples:: create_reflective_structured_agent
      :collapse:

.. py:function:: create_tool_enhanced_agent(name: str = 'tool_enhanced', output_model: type[pydantic.BaseModel] = AnalysisResult, debug: bool = True) -> ToolEnhancedStructuredAgent

   Create a tool-enhanced structured agent.


   .. autolink-examples:: create_tool_enhanced_agent
      :collapse:

.. py:function:: example_basic_react_structured()
   :async:


   Example of basic React → Structured flow.


   .. autolink-examples:: example_basic_react_structured
      :collapse:

.. py:function:: example_multi_stage()
   :async:


   Example of multi-stage reasoning.


   .. autolink-examples:: example_multi_stage
      :collapse:

.. py:function:: example_reflective()
   :async:


   Example of reflective structured output.


   .. autolink-examples:: example_reflective
      :collapse:

