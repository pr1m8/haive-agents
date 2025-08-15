agents.react.agent
==================

.. py:module:: agents.react.agent

.. autoapi-nested-parse::

   ReactAgent v3 - Enhanced ReAct Pattern with Structured Output Support.

   This module provides ReactAgent v3, an enhanced implementation of the ReAct (Reasoning and Acting)
   pattern that extends SimpleAgent with iterative reasoning loops, tool usage, and structured
   output capabilities.

   The ReactAgent v3 implements the ReAct paradigm where the agent alternates between:
   1. **Reasoning**: Thinking about the problem and planning next steps
   2. **Acting**: Using tools to gather information or perform actions
   3. **Observing**: Analyzing tool results and updating understanding
   4. **Iterating**: Continuing the cycle until the goal is achieved

   Key enhancements over the original ReactAgent:
   - Full structured output support with Pydantic models
   - Enhanced Agent base class with hooks system
   - Real-time recompilation when tools are added/removed
   - Comprehensive debug logging and observability
   - Token usage tracking and cost monitoring
   - Meta-agent embedding capabilities
   - Agent-as-tool pattern support

   .. rubric:: Examples

   Basic ReAct agent with tools::

       from haive.agents.react.agent_v3 import ReactAgent
       from haive.core.engine.aug_llm import AugLLMConfig
       from langchain_core.tools import tool

       @tool
       def calculator(expression: str) -> str:
           '''Calculate mathematical expressions.'''
           return str(eval(expression))

       @tool
       def web_search(query: str) -> str:
           '''Search the web for information.'''
           return f"Search results for: {query}"

       agent = ReactAgent(
           name="research_assistant",
           engine=AugLLMConfig(
               tools=[calculator, web_search],
               temperature=0.7,
               max_tokens=800
           ),
           debug=True
       )

       result = agent.run("Research the current population of Tokyo and calculate the population density")
       # Agent will iteratively use web_search and calculator tools

   With structured output for complex reasoning::

       from pydantic import BaseModel, Field
       from typing import List

       class ResearchAnalysis(BaseModel):
           research_question: str = Field(description="Original research question")
           reasoning_steps: List[str] = Field(description="Step-by-step reasoning process")
           tools_used: List[str] = Field(description="Tools utilized during research")
           key_findings: List[str] = Field(description="Important discoveries made")
           final_answer: str = Field(description="Comprehensive final answer")
           confidence: float = Field(ge=0.0, le=1.0, description="Confidence in answer")

       agent = ReactAgent(
           name="structured_researcher",
           engine=AugLLMConfig(
               tools=[calculator, web_search],
               structured_output_model=ResearchAnalysis,
               temperature=0.3,
               max_tokens=1000
           ),
           max_iterations=5,  # Limit reasoning loops
           debug=True
       )

       analysis = agent.run("Analyze the economic impact of renewable energy adoption")
       # Returns validated ResearchAnalysis with complete reasoning trace

   .. seealso::

      haive.agents.simple.agent_v3.SimpleAgent: Base agent class
      haive.agents.react.agent.ReactAgent: Original ReactAgent implementation
      haive.core.engine.aug_llm.AugLLMConfig: Engine configuration


   .. autolink-examples:: agents.react.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.react.agent.logger


Classes
-------

.. autoapisummary::

   agents.react.agent.ReactAgent


Functions
---------

.. autoapisummary::

   agents.react.agent.create_react_agent
   agents.react.agent.create_research_agent
   agents.react.agent.example_calculator


Module Contents
---------------

.. py:class:: ReactAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   ReactAgent v3 with enhanced ReAct pattern, structured output, and hooks integration.

   This agent implements the ReAct (Reasoning and Acting) paradigm with significant
   enhancements over the original ReactAgent. It extends SimpleAgent to inherit
   all structured output capabilities, hooks system, recompilation features, and
   advanced observability while adding iterative reasoning loops.

   **ReAct Pattern Implementation:**
   The agent follows a continuous reasoning loop:

   1. **Think**: Analyze the current situation and plan next steps
   2. **Act**: Execute tools or gather information
   3. **Observe**: Process tool results and update understanding
   4. **Repeat**: Continue until goal is achieved or max iterations reached

   **Enhanced Features over ReactAgent:**
   - Full structured output support with automatic Pydantic model validation
   - Iterative reasoning with configurable maximum iteration limits
   - Enhanced debugging with step-by-step reasoning trace visibility
   - Real-time tool addition/removal with automatic graph recompilation
   - Comprehensive hooks system for monitoring and intervention
   - Token usage tracking and cost analysis throughout reasoning loops
   - Meta-agent embedding support for multi-agent coordination
   - Agent-as-tool conversion for hierarchical agent systems

   **Architecture Integration:**
   - Inherits from SimpleAgent for full enhanced Agent capabilities
   - Uses LLMState for comprehensive token and cost tracking
   - Integrates with RecompileMixin for dynamic tool management
   - Supports DynamicToolRouteMixin for flexible tool routing
   - Compatible with MetaStateSchema for embedding in larger systems

   .. attribute:: max_iterations

      Maximum number of reasoning iterations before stopping.
      Prevents infinite loops while allowing complex multi-step reasoning.

   .. attribute:: iteration_count

      Current iteration number during execution (read-only).

   .. attribute:: reasoning_trace

      List of reasoning steps taken during execution (read-only).

   .. attribute:: stop_on_first_tool_result

      Whether to stop after the first successful tool execution.
      Useful for simple lookup tasks vs. complex multi-step reasoning.

   .. attribute:: require_final_answer

      Whether to require a final non-tool response.
      Ensures the agent provides a summary or conclusion after tool usage.

   .. rubric:: Examples

   Basic ReAct agent for research tasks::

       from haive.agents.react.agent_v3 import ReactAgent
       from langchain_core.tools import tool

       @tool
       def search_engine(query: str) -> str:
           '''Search for information online.'''
           return f"Search results for: {query}"

       @tool
       def calculator(expression: str) -> str:
           '''Perform mathematical calculations.'''
           return str(eval(expression))

       agent = ReactAgent(
           name="research_agent",
           engine=AugLLMConfig(
               tools=[search_engine, calculator],
               temperature=0.7,
               max_tokens=1200
           ),
           max_iterations=8,
           debug=True
       )

       result = agent.run(
           "Find the current population of Japan and calculate how many Tokyo Domes "
           "would fit that many people (assuming 55,000 capacity each)"
       )
       # Agent iteratively searches for population data, then calculates the result

   Structured output for complex analysis::

       from pydantic import BaseModel, Field
       from typing import List

       class TechnicalAnalysis(BaseModel):
           problem_statement: str = Field(description="Clear problem definition")
           research_steps: List[str] = Field(description="Steps taken to research")
           calculations_performed: List[str] = Field(description="Mathematical operations")
           key_findings: List[str] = Field(description="Important discoveries")
           final_solution: str = Field(description="Complete solution with reasoning")
           confidence_level: float = Field(ge=0.0, le=1.0, description="Solution confidence")

       agent = ReactAgent(
           name="technical_analyst",
           engine=AugLLMConfig(
               tools=[search_engine, calculator],
               structured_output_model=TechnicalAnalysis,
               temperature=0.3
           ),
           max_iterations=6,
           require_final_answer=True
       )

       analysis = agent.run("Analyze the feasibility of a space elevator")
       # Returns TechnicalAnalysis with complete reasoning process
       assert isinstance(analysis, TechnicalAnalysis)
       print(f"Confidence: {analysis.confidence_level}")

   With hooks for monitoring reasoning process::

       @agent.before_iteration
       def log_iteration_start(context):
           logger.info(f"Starting iteration {context.iteration_count}")

       @agent.after_tool_execution
       def log_tool_usage(context):
           logger.info(f"Used tool: {context.tool_name} -> {context.tool_result[:100]}...")

       @agent.before_final_answer
       def validate_completeness(context):
           if len(context.reasoning_trace) < 3:
               logger.warning("Solution may be incomplete - consider more reasoning steps")

       result = agent.run("Complex multi-step problem")
       # Comprehensive monitoring throughout reasoning process

   Dynamic tool addition during reasoning::

       agent = ReactAgent(
           name="adaptive_agent",
           engine=AugLLMConfig(tools=[calculator]),
           auto_recompile=True,
           max_iterations=10
       )

       # Start reasoning
       result = agent.run("I need to research and calculate something complex")

       # Agent realizes it needs additional tools, add them dynamically
       @tool
       def database_lookup(query: str) -> str:
           '''Look up information in database.'''
           return f"Database result for: {query}"

       agent.add_tool(database_lookup)  # Triggers automatic recompilation

       # Continue reasoning with new tool available
       continued_result = agent.run("Now use the database to complete the analysis")

   Production configuration with limits::

       agent = ReactAgent(
           name="production_agent",
           engine=AugLLMConfig(
               tools=production_tools,
               temperature=0.2,
               max_tokens=800
           ),
           max_iterations=5,  # Limit for performance
           stop_on_first_tool_result=False,  # Allow multi-tool usage
           require_final_answer=True,  # Ensure conclusions
           debug=False  # Minimal logging for production
       )

   .. note::

      - ReAct agents are more computationally expensive than SimpleAgents due to iterative reasoning
      - Set appropriate max_iterations to balance thoroughness with performance
      - Structured output works seamlessly with the reasoning loop
      - Tool costs can accumulate across multiple iterations
      - Debug mode provides valuable insights into the reasoning process
      - The agent will automatically stop when it determines the task is complete

   .. seealso::

      SimpleAgent: Base class with structured output and enhanced features
      ReactAgent: Original ReactAgent implementation
      AugLLMConfig: Engine configuration for tools and structured output
      LLMState: State schema with token tracking across iterations
      RecompileMixin: Dynamic tool management capabilities


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _has_structured_output() -> bool

      Check if agent has structured output model configured.

      :returns: True if structured output model is configured
      :rtype: bool


      .. autolink-examples:: _has_structured_output
         :collapse:


   .. py:method:: _has_tools() -> bool

      Check if agent has tools configured for ReAct pattern execution.

      :returns: True if agent has tools available for acting phase
      :rtype: bool


      .. autolink-examples:: _has_tools
         :collapse:


   .. py:method:: _modify_graph_for_react_loops(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Modify graph connections to implement ReAct reasoning loops.

      Simple ReAct pattern like original ReactAgent:
      1. tool_node → agent_node (instead of END) for continued reasoning
      2. parse_output → agent_node (instead of END) for more reasoning

      This allows the agent to see tool results and continue reasoning.


      .. autolink-examples:: _modify_graph_for_react_loops
         :collapse:


   .. py:method:: _register_react_hooks() -> None

      Register ReAct-specific hook events for reasoning loop monitoring.

      Registers additional hook events specific to the ReAct pattern:
      - before_iteration: Called before each reasoning iteration
      - after_iteration: Called after each reasoning iteration
      - before_tool_execution: Called before any tool is executed
      - after_tool_execution: Called after tool execution completes
      - before_final_answer: Called before generating final response
      - reasoning_limit_reached: Called when max_iterations is hit


      .. autolink-examples:: _register_react_hooks
         :collapse:


   .. py:method:: add_reasoning_step(step: str) -> None

      Add a reasoning step to the trace for monitoring and debugging.

      :param step: Description of the reasoning step being performed


      .. autolink-examples:: add_reasoning_step
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build enhanced ReAct graph with iterative reasoning loops and structured output.

      Creates a graph that implements the ReAct pattern with reasoning loops
      instead of the linear execution flow of SimpleAgent. The graph structure
      enables the agent to iteratively reason, act with tools, and observe results
      until the problem is solved or max_iterations is reached.

      **Graph Structure:**

      .. code-block:: text

          START → agent_node → validation_node
                      ↑             ↓
                      ←─── tool_node (loops back for continued reasoning)
                      ↑             ↓
                      ←─── parse_output (for structured output, then loops back)
                                    ↓
                                 END (when reasoning complete or max iterations)

      **Key Differences from SimpleAgent:**

      - Tool executions loop back to agent_node for continued reasoning
      - Parser output loops back for additional reasoning iterations
      - Iteration counting and limiting built into the graph flow
      - Reasoning trace tracking throughout the execution

      :returns:

                Compiled graph ready for ReAct pattern execution with
                    reasoning loops, tool integration, and structured output support.
      :rtype: BaseGraph

      :raises GraphBuildError: If graph construction fails due to configuration issues.
      :raises ToolIntegrationError: If tool nodes cannot be properly integrated.

      .. rubric:: Examples

      Basic ReAct graph with tools::

          agent = ReactAgent(
              name="react_agent",
              engine=AugLLMConfig(tools=[calculator, search_tool])
          )

          graph = agent.build_graph()
          # Graph enables: reasoning → tool use → more reasoning → solution

      With structured output and reasoning limits::

          agent = ReactAgent(
              name="structured_react",
              engine=AugLLMConfig(
                  tools=[research_tools],
                  structured_output_model=AnalysisResult
              ),
              max_iterations=8
          )

          graph = agent.build_graph()
          # Graph supports structured output after reasoning completion

      .. note::

         - The graph automatically handles iteration counting and limits
         - Tool execution results always feed back into reasoning
         - Structured output is generated after reasoning completion
         - Graph compilation includes all SimpleAgent enhancements
         - Debug mode provides detailed graph traversal logging


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_reasoning_trace() -> list[str]

      Get the complete reasoning trace from the current or last execution.

      :returns: List of reasoning steps performed during execution
      :rtype: List[str]


      .. autolink-examples:: get_reasoning_trace
         :collapse:


   .. py:method:: get_tool_usage_history() -> list[dict[str, Any]]

      Get the complete tool usage history from the current or last execution.

      :returns: List of tool executions with results and metadata
      :rtype: List[Dict[str, Any]]


      .. autolink-examples:: get_tool_usage_history
         :collapse:


   .. py:method:: run(input_data: Any, debug: bool | None = None, **kwargs) -> Any

      Execute ReactAgent with iterative reasoning loops and structured output.

      Implements the full ReAct pattern with enhanced capabilities from SimpleAgent.
      The execution follows iterative reasoning cycles until the problem is solved
      or maximum iterations are reached.

      **ReAct Execution Flow:**
      1. **Initialize**: Set up reasoning state and iteration tracking
      2. **Think**: Analyze current situation and plan next steps
      3. **Act**: Execute tools or gather information if needed
      4. **Observe**: Process results and update reasoning state
      5. **Evaluate**: Determine if problem is solved or more reasoning needed
      6. **Iterate**: Return to step 2 if max_iterations not reached
      7. **Conclude**: Generate final answer (structured if configured)

      :param input_data: Input for the ReAct reasoning process. Supports all formats
                         from SimpleAgent (str, List[BaseMessage], Dict, BaseModel).
      :param debug: Override agent's debug setting for detailed reasoning trace.
                    When True, shows each reasoning iteration step-by-step.
      :param \*\*kwargs: Additional execution arguments:
                         - max_iterations_override: Temporarily override max_iterations
                         - stop_early: Stop after first successful tool result
                         - require_conclusion: Force final non-tool response

      :returns:

                Result format depends on configuration:
                    - With structured_output_model: Validated Pydantic model with reasoning
                    - Without structured output: Final reasoning conclusion as string
                    - Debug mode: Enhanced result with complete reasoning trace
      :rtype: Any

      :raises ReasoningLoopError: If reasoning loop fails to converge or encounters errors.
      :raises MaxIterationsExceeded: If max_iterations reached without solution.
      :raises ToolExecutionError: If critical tool execution fails during reasoning.
      :raises StructuredOutputError: If structured output validation fails after reasoning.

      .. rubric:: Examples

      Basic ReAct reasoning with tools::

          agent = ReactAgent(
              name="problem_solver",
              engine=AugLLMConfig(tools=[calculator, web_search]),
              max_iterations=6
          )

          result = agent.run(
              "What's the square root of the current population of Tokyo?",
              debug=True
          )
          # Shows: research Tokyo population → calculate square root → conclude

      Structured output with reasoning trace::

          class ProblemSolution(BaseModel):
              original_problem: str = Field(description="Problem statement")
              reasoning_steps: List[str] = Field(description="Thinking process")
              tools_used: List[str] = Field(description="Tools utilized")
              intermediate_results: List[str] = Field(description="Intermediate findings")
              final_answer: str = Field(description="Complete solution")
              confidence: float = Field(description="Solution confidence 0-1")

          agent = ReactAgent(
              name="structured_solver",
              engine=AugLLMConfig(
                  tools=[calculator, web_search],
                  structured_output_model=ProblemSolution
              ),
              max_iterations=8,
              require_final_answer=True
          )

          solution = agent.run("Complex multi-step research problem")
          # Returns ProblemSolution with complete reasoning documentation
          assert isinstance(solution, ProblemSolution)
          print(f"Reasoning steps: {len(solution.reasoning_steps)}")
          print(f"Confidence: {solution.confidence}")

      With iteration override and early stopping::

          result = agent.run(
              "Simple lookup question",
              max_iterations_override=3,  # Limit for simple task
              stop_early=True,  # Stop after first tool success
              debug=True
          )

      Production execution with monitoring::

          @agent.before_iteration
          def log_iteration(context):
              logger.info(f"Iteration {context.iteration_count}: {context.current_step}")

          @agent.after_tool_execution
          def log_tool_usage(context):
              logger.info(f"Tool {context.tool_name}: {context.success}")

          result = agent.run("Production reasoning task")
          # Comprehensive logging throughout reasoning process

      Performance Notes:
          - ReAct agents are 3-5x more expensive than SimpleAgents due to iteration
          - Each iteration involves a full LLM call and potential tool execution
          - Structured output adds validation overhead after reasoning completion
          - Debug mode significantly increases output and execution time
          - Tool costs accumulate across all reasoning iterations

      Reasoning Quality:
          - More iterations generally lead to better solutions but higher cost
          - Tools significantly improve reasoning quality for factual problems
          - Structured output ensures consistent result format and validation
          - Early stopping trades thoroughness for performance

      .. seealso::

         SimpleAgent.run: Base execution method with additional capabilities
         add_tool: Dynamic tool addition during reasoning
         set_max_iterations: Runtime iteration limit configuration
         get_reasoning_trace: Access complete reasoning history


      .. autolink-examples:: run
         :collapse:


   .. py:method:: set_max_iterations(max_iterations: int) -> None

      Set maximum reasoning iterations with validation.

      :param max_iterations: New maximum iteration limit (1-50)

      :raises ValueError: If max_iterations is outside valid range


      .. autolink-examples:: set_max_iterations
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup ReactAgent v3 with enhanced ReAct pattern and reasoning loop configuration.

      Extends SimpleAgent.setup_agent() with ReactAgent-specific initialization
      including reasoning loop configuration, iteration tracking setup, and
      ReAct-specific hooks registration.

      Additional setup includes:
      1. Reasoning iteration limits and tracking initialization
      2. Tool execution history and trace setup
      3. ReAct-specific hook events registration
      4. Graph modification for reasoning loops instead of linear execution
      5. Performance monitoring for iterative execution

      This method is called automatically during agent instantiation.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: validate_max_iterations(v: int) -> int
      :classmethod:


      Validate max_iterations is reasonable for performance.


      .. autolink-examples:: validate_max_iterations
         :collapse:


   .. py:attribute:: current_reasoning_step
      :type:  str | None
      :value: None



   .. py:attribute:: iteration_count
      :type:  int
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: reasoning_trace
      :type:  list[str]
      :value: None



   .. py:attribute:: require_final_answer
      :type:  bool
      :value: None



   .. py:attribute:: stop_on_first_tool_result
      :type:  bool
      :value: None



   .. py:attribute:: tool_results_history
      :type:  list[dict[str, Any]]
      :value: None



.. py:function:: create_react_agent(name: str, tools: list[langchain_core.tools.BaseTool], structured_output_model: type[pydantic.BaseModel] | None = None, max_iterations: int = 10, temperature: float = 0.7, max_tokens: int = 1200, debug: bool = False, **engine_kwargs) -> ReactAgent

   Create a ReactAgent with standard configuration for ReAct pattern execution.

   This factory function simplifies ReactAgent creation with sensible defaults
   for ReAct reasoning, tool usage, and optional structured output.

   :param name: Unique identifier for the agent instance.
   :param tools: List of LangChain tools for the acting phase of ReAct.
   :param structured_output_model: Optional Pydantic model for structured responses.
   :param max_iterations: Maximum reasoning iterations (recommended: 5-15).
   :param temperature: LLM temperature for reasoning (0.1=focused, 0.9=creative).
   :param max_tokens: Token limit per iteration (should account for tool results).
   :param debug: Enable detailed reasoning trace and execution logging.
   :param \*\*engine_kwargs: Additional AugLLMConfig parameters.

   :returns: Configured agent ready for ReAct pattern execution.
   :rtype: ReactAgent

   .. rubric:: Examples

   Research agent with web search and calculation::

       from langchain_core.tools import tool

       @tool
       def web_search(query: str) -> str:
           '''Search the web for current information.'''
           return search_api.search(query)

       @tool
       def calculator(expression: str) -> str:
           '''Perform mathematical calculations.'''
           return str(eval(expression))

       agent = create_react_agent(
           name="research_assistant",
           tools=[web_search, calculator],
           max_iterations=8,
           temperature=0.6,
           debug=True
       )

       result = agent.run("What's the GDP per capita of the top 5 economies?")

   With structured output for consistent results::

       class ResearchReport(BaseModel):
           query: str = Field(description="Original research question")
           methodology: List[str] = Field(description="Research steps taken")
           findings: List[str] = Field(description="Key discoveries")
           conclusion: str = Field(description="Final answer with reasoning")
           sources_used: List[str] = Field(description="Information sources")

       agent = create_react_agent(
           name="structured_researcher",
           tools=[web_search, calculator],
           structured_output_model=ResearchReport,
           max_iterations=12,
           temperature=0.4,
           max_tokens=1500
       )

       report = agent.run("Research renewable energy adoption trends")
       assert isinstance(report, ResearchReport)


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: create_research_agent(name: str, research_tools: list[langchain_core.tools.BaseTool], analysis_model: type[pydantic.BaseModel] | None = None, max_research_steps: int = 8, debug: bool = False) -> ReactAgent

   Create a ReactAgent optimized for research and analysis tasks.

   Pre-configured for research workflows with appropriate iteration limits,
   temperature settings, and token allowances for comprehensive investigation.

   :param name: Agent identifier for research tasks.
   :param research_tools: Tools for information gathering (search, databases, APIs).
   :param analysis_model: Optional structured output model for research results.
   :param max_research_steps: Maximum research iterations (recommended: 6-12).
   :param debug: Enable research process tracing.

   :returns: Research-optimized agent configuration.
   :rtype: ReactAgent


   .. autolink-examples:: create_research_agent
      :collapse:

.. py:function:: example_calculator(expression: str) -> str

   Calculate mathematical expressions.


   .. autolink-examples:: example_calculator
      :collapse:

.. py:data:: logger

