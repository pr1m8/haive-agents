enhanced_agent_v3.v2
====================

.. py:module:: enhanced_agent_v3.v2

.. autoapi-nested-parse::

   Enhanced ReactAgent V3 - Full ReAct implementation with advanced features.

   This version combines the ReAct (Reasoning and Acting) pattern with all enhanced
   capabilities from the base Agent class and EnhancedSimpleAgent.

   Key Features:
   - Complete ReAct reasoning and action loop
   - Advanced tool integration and routing
   - Intelligent loop control and termination
   - Rich execution tracking and debugging
   - Performance optimizations for iterative workflows


   .. autolink-examples:: enhanced_agent_v3.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   enhanced_agent_v3.v2.logger


Classes
-------

.. autoapisummary::

   enhanced_agent_v3.v2.EnhancedReactAgent


Module Contents
---------------

.. py:class:: EnhancedReactAgent

   Bases: :py:obj:`haive.agents.simple.enhanced_agent_v3.EnhancedSimpleAgent`


   Enhanced ReactAgent V3 with complete ReAct pattern and advanced features.

   This agent implements the full Reasoning and Acting (ReAct) pattern with
   sophisticated enhancements:

   ReAct Pattern Features:
   - Reasoning: Agent thinks through problems step by step
   - Acting: Agent uses tools to gather information or take actions
   - Observing: Agent analyzes tool results and outcomes
   - Iterating: Agent continues until task completion or max iterations

   Enhanced Features (inherited from EnhancedSimpleAgent):
   - Dynamic schema generation and composition
   - Advanced engine management and routing
   - Rich execution capabilities with debugging
   - Sophisticated state management
   - Comprehensive persistence and serialization

   ReAct-Specific Enhancements:
   - Intelligent loop control and termination
   - Tool usage optimization and caching
   - Reasoning trace preservation and analysis
   - Advanced iteration management
   - Performance monitoring for iterative workflows

   .. attribute:: max_iterations

      Maximum reasoning iterations (default: 10)

   .. attribute:: reasoning_mode

      Reasoning strategy ('thorough', 'efficient', 'creative')

   .. attribute:: tool_selection_strategy

      How to choose tools ('auto', 'explicit', 'learned')

   .. attribute:: loop_detection

      Enable infinite loop detection and prevention

   .. attribute:: reasoning_trace

      Preserve detailed reasoning traces

   .. attribute:: performance_tracking

      Track performance metrics per iteration

   Advanced Configuration:
       iteration_timeout: Timeout per iteration in seconds
       tool_usage_optimization: Enable tool usage caching and optimization
       reasoning_quality_threshold: Minimum reasoning quality score
       early_termination_conditions: Custom termination conditions

   .. rubric:: Examples

   Basic ReAct usage::

       from langchain_core.tools import tool

       @tool
       def web_search(query: str) -> str:
           '''Search the web for information'''
           return search_results

       @tool
       def calculator(expression: str) -> str:
           '''Calculate mathematical expressions'''
           return str(eval(expression))

       agent = EnhancedReactAgent(
           name="research_agent",
           temperature=0.7,
           tools=[web_search, calculator],
           max_iterations=15
       )

       result = agent.run("Research the latest AI developments and calculate the growth rate")

   Advanced ReAct configuration::

       agent = EnhancedReactAgent(
           name="advanced_researcher",
           temperature=0.6,
           max_iterations=20,
           reasoning_mode="thorough",
           tool_selection_strategy="learned",
           loop_detection=True,
           reasoning_trace=True,
           performance_tracking=True,
           debug_mode=True,
           advanced_routing=True,
           iteration_timeout=30.0,
           tool_usage_optimization=True
       )

   With structured output::

       from pydantic import BaseModel, Field

       class ResearchReport(BaseModel):
           summary: str = Field(description="Research summary")
           key_findings: list[str] = Field(description="Key findings")
           sources: list[str] = Field(description="Information sources")
           confidence: float = Field(description="Confidence score")
           methodology: str = Field(description="Research methodology used")

       agent = EnhancedReactAgent(
           name="structured_researcher",
           tools=[web_search, calculator],
           structured_output_model=ResearchReport,
           reasoning_mode="thorough",
           performance_tracking=True
       )

       report = agent.run("Research renewable energy trends and market projections")


   .. autolink-examples:: EnhancedReactAgent
      :collapse:

   .. py:method:: __repr__() -> str

      Enhanced string representation for ReAct agent.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _add_iteration_control(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add iteration control and loop detection.


      .. autolink-examples:: _add_iteration_control
         :collapse:


   .. py:method:: _add_performance_monitoring(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add performance monitoring to the graph.


      .. autolink-examples:: _add_performance_monitoring
         :collapse:


   .. py:method:: _add_react_loop(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add ReAct looping logic to the graph.


      .. autolink-examples:: _add_react_loop
         :collapse:


   .. py:method:: _setup_iteration_management() -> None

      Setup iteration management and control.


      .. autolink-examples:: _setup_iteration_management
         :collapse:


   .. py:method:: _setup_performance_tracking() -> None

      Setup performance tracking for iterations.


      .. autolink-examples:: _setup_performance_tracking
         :collapse:


   .. py:method:: _setup_react_features() -> None

      Setup ReAct-specific capabilities.


      .. autolink-examples:: _setup_react_features
         :collapse:


   .. py:method:: _validate_react_configuration() -> None

      Validate ReAct-specific configuration.


      .. autolink-examples:: _validate_react_configuration
         :collapse:


   .. py:method:: analyze_tool_usage() -> dict[str, Any]

      Analyze tool usage patterns and efficiency.


      .. autolink-examples:: analyze_tool_usage
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build enhanced ReAct graph with intelligent looping.

      Creates a sophisticated ReAct graph that includes:
      - Intelligent reasoning loop control
      - Advanced tool routing and selection
      - Performance monitoring and optimization
      - Loop detection and prevention
      - Detailed execution tracing

      Graph Structure:
      1. START → agent_node (reasoning)
      2. agent_node → validation (check for tool calls/completion)
      3. validation → tool_node (if tools needed)
      4. tool_node → agent_node (continue reasoning - THE LOOP)
      5. validation → parse_output (if structured output)
      6. validation → END (if task complete)

      Enhanced Features:
      - Loop detection and prevention
      - Iteration counting and limits
      - Performance monitoring nodes
      - Quality assessment nodes

      :returns: Enhanced ReAct graph with loop control
      :rtype: BaseGraph


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: display_react_capabilities() -> None

      Display comprehensive ReAct capabilities.


      .. autolink-examples:: display_react_capabilities
         :collapse:


   .. py:method:: get_react_summary() -> dict[str, Any]

      Get comprehensive ReAct execution summary.


      .. autolink-examples:: get_react_summary
         :collapse:


   .. py:method:: get_reasoning_trace() -> list[dict[str, Any]]

      Get detailed reasoning trace if enabled.


      .. autolink-examples:: get_reasoning_trace
         :collapse:


   .. py:method:: optimize_performance() -> dict[str, Any]

      Run performance optimization analysis.


      .. autolink-examples:: optimize_performance
         :collapse:


   .. py:method:: setup_agent() -> None

      Enhanced setup for ReAct-specific features.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: early_termination_conditions
      :type:  list[str] | None
      :value: None



   .. py:attribute:: iteration_timeout
      :type:  float | None
      :value: None



   .. py:attribute:: loop_detection
      :type:  bool
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: performance_tracking
      :type:  bool
      :value: None



   .. py:attribute:: reasoning_mode
      :type:  str
      :value: None



   .. py:attribute:: reasoning_quality_threshold
      :type:  float | None
      :value: None



   .. py:attribute:: reasoning_trace
      :type:  bool
      :value: None



   .. py:attribute:: tool_selection_strategy
      :type:  str
      :value: None



   .. py:attribute:: tool_usage_optimization
      :type:  bool
      :value: None



.. py:data:: logger

