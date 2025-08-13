
:py:mod:`agent_v3.v2`
=====================

.. py:module:: agent_v3.v2

Agent_V3 core module.
from langchain_core.messages import BaseMessage

This module provides agent v3 functionality for the Haive framework.

Classes:
    with: with implementation.
    ResearchAnalysis: ResearchAnalysis implementation.
    haive: haive implementation.

Functions:
    calculator: Calculator functionality.
    web_search: Web Search functionality.
    search_engine: Search Engine functionality.


.. autolink-examples:: agent_v3.v2
   :collapse:

Classes
-------

.. autoapisummary::

   agent_v3.v2.ReactAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "SimpleAgentV3" -> "ReactAgent";
      }

.. autoclass:: agent_v3.v2.ReactAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agent_v3.v2.create_react_agent
   agent_v3.v2.create_research_agent
   agent_v3.v2.example_calculator

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

.. autolink-examples:: agent_v3.v2
   :collapse:
   
.. autolink-skip:: next
