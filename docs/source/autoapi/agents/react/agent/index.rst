
:py:mod:`agents.react.agent`
============================

.. py:module:: agents.react.agent

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

Classes
-------

.. autoapisummary::

   agents.react.agent.ReactAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "ReactAgent";
      }

.. autoclass:: agents.react.agent.ReactAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.react.agent.create_react_agent
   agents.react.agent.create_research_agent
   agents.react.agent.example_calculator

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



.. rubric:: Related Links

.. autolink-examples:: agents.react.agent
   :collapse:
   
.. autolink-skip:: next
