
:py:mod:`agents.react`
======================

.. py:module:: agents.react

React - ReAct agent implementation with enhanced v3 capabilities.

ReAct (Reasoning and Acting) agents that can use tools, reason about actions,
and provide structured output with comprehensive debugging and observability.

Available Implementations:
    - ReactAgent: Original implementation extending SimpleAgent
    - ReactAgent: Enhanced implementation with structured output, hooks, and advanced features

.. rubric:: Examples

Basic ReactAgent usage::

    from haive.agents.react import ReactAgent
    from haive.core.engine.aug_llm import AugLLMConfig

    agent = ReactAgent(name="react_agent", engine=AugLLMConfig())

Enhanced ReactAgent with structured output::

    from haive.agents.react import ReactAgent, create_react_agent
    from langchain_core.tools import tool
    from pydantic import BaseModel, Field

    @tool
    def calculator(expr: str) -> str:
        return str(eval(expr))

    class Analysis(BaseModel):
        reasoning: str = Field(description="Step-by-step reasoning")
        result: str = Field(description="Final answer")

    # Factory function approach
    agent = create_react_agent(
        name="enhanced_react",
        tools=[calculator],
        structured_output_model=Analysis,
        max_iterations=8,
        debug=True
    )

    # Direct instantiation approach
    agent = ReactAgent(
        name="direct_react",
        engine=AugLLMConfig(
            tools=[calculator],
            structured_output_model=Analysis
        ),
        max_iterations=6
    )

.. seealso::

   haive.agents.simple: SimpleAgent and SimpleAgentV3 implementations
   haive.core.engine.aug_llm: AugLLMConfig for engine configuration


.. autolink-examples:: agents.react
   :collapse:




