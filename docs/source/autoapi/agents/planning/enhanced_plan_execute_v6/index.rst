
:py:mod:`agents.planning.enhanced_plan_execute_v6`
==================================================

.. py:module:: agents.planning.enhanced_plan_execute_v6

Enhanced Plan & Execute V6 - Using MultiAgent with Universal Structured Output.

This module provides the next-generation Plan & Execute implementation using:
- MultiAgent for multi-agent orchestration
- Universal structured output pattern (Agent.with_structured_output)
- BasePlannerAgent and BaseExecutorAgent from base planning components
- Modern Haive architecture with hooks, recompilation, and state management

## Key Features

- **Universal Structured Output**: Any agent can have structured output via mixins
- **MultiAgent**: Modern multi-agent coordination with conditional routing
- **Base Planning Components**: Uses BasePlannerAgent and BaseExecutorAgent
- **Real Component Testing**: No mocks, actual LLM execution and tool usage
- **Modern Architecture**: Hooks, recompilation, state management, type safety

## Architecture

```
BasePlannerAgent.with_structured_output(BasePlan)
    ↓ (structured BasePlan output)
BaseExecutorAgent.with_structured_output(ExecutionResult)
    ↓ (structured ExecutionResult output)
Conditional Routing (should_continue)
    ↓
MultiAgent orchestration
```

## Usage

### Basic Usage
```python
from haive.agents.planning.enhanced_plan_execute_v6 import create_enhanced_plan_execute_v6

# Create with default configuration
agent = create_enhanced_plan_execute_v6()
result = await agent.arun("Calculate compound interest on $1000 at 5% for 10 years")

# Create with custom tools
from haive.tools.tools.search_tools import tavily_search_tool
agent = create_enhanced_plan_execute_v6(
    name="research_planner",
    executor_tools=[tavily_search_tool]
)
result = await agent.arun("Research Tesla stock performance and calculate ROI")
```

### Advanced Configuration
```python
agent = create_enhanced_plan_execute_v6(
    name="advanced_planner",
    planner_config=AugLLMConfig(
        model="gpt-4",
        temperature=0.2,
        system_message="You are an expert strategic planner."
    ),
    executor_config=AugLLMConfig(
        model="gpt-4-turbo",
        temperature=0.1
    ),
    executor_tools=[tavily_search_tool, calculator_tool],
    max_iterations=15,
    enable_hooks=True
)

# Add custom hooks
@agent.before_run
def track_execution(context):
    print(f"Starting planning workflow: {context.agent_name}")

result = await agent.arun("Complex multi-step research task")
```

## Status: Production Ready

This implementation showcases the full power of modern Haive architecture:
- MultiAgent coordination
- Universal structured output patterns
- Base planning components
- Real component integration


.. autolink-examples:: agents.planning.enhanced_plan_execute_v6
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v6.ExecutionResult
   agents.planning.enhanced_plan_execute_v6.PlanExecuteState
   agents.planning.enhanced_plan_execute_v6.PlanningDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionResult {
        node [shape=record];
        "ExecutionResult" [label="ExecutionResult"];
        "pydantic.BaseModel" -> "ExecutionResult";
      }

.. autopydantic_model:: agents.planning.enhanced_plan_execute_v6.ExecutionResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanExecuteState:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteState {
        node [shape=record];
        "PlanExecuteState" [label="PlanExecuteState"];
        "haive.core.schema.prebuilt.multi_agent_state.MultiAgentState" -> "PlanExecuteState";
      }

.. autoclass:: agents.planning.enhanced_plan_execute_v6.PlanExecuteState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanningDecision:

   .. graphviz::
      :align: center

      digraph inheritance_PlanningDecision {
        node [shape=record];
        "PlanningDecision" [label="PlanningDecision"];
        "pydantic.BaseModel" -> "PlanningDecision";
      }

.. autopydantic_model:: agents.planning.enhanced_plan_execute_v6.PlanningDecision
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v6._add_monitoring_hooks_v6
   agents.planning.enhanced_plan_execute_v6.create_enhanced_plan_execute_v6
   agents.planning.enhanced_plan_execute_v6.create_research_plan_execute_v6
   agents.planning.enhanced_plan_execute_v6.create_simple_plan_execute_v6
   agents.planning.enhanced_plan_execute_v6.get_next_step_v6
   agents.planning.enhanced_plan_execute_v6.process_executor_output_v6
   agents.planning.enhanced_plan_execute_v6.process_planner_output_v6
   agents.planning.enhanced_plan_execute_v6.should_continue_v6
   agents.planning.enhanced_plan_execute_v6.test_enhanced_plan_execute_v6

.. py:function:: _add_monitoring_hooks_v6(workflow: haive.agents.multi.agent.MultiAgent) -> None

   Add comprehensive monitoring hooks to the V6 workflow.


   .. autolink-examples:: _add_monitoring_hooks_v6
      :collapse:

.. py:function:: create_enhanced_plan_execute_v6(name: str = 'EnhancedPlanExecuteV6', planner_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, executor_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, executor_tools: list | None = None, max_iterations: int = 20, enable_hooks: bool = True) -> haive.agents.multi.agent.MultiAgent

   Create enhanced Plan & Execute V6 using modern Haive patterns.

   :param name: Name for the multi-agent system
   :param planner_config: Configuration for the planning agent
   :param executor_config: Configuration for the execution agent
   :param executor_tools: Tools available to the executor
   :param max_iterations: Maximum planning iterations
   :param enable_hooks: Whether to enable the hooks system

   :returns: Complete planning workflow system
   :rtype: MultiAgent

   .. rubric:: Examples

   Basic usage::

       agent = create_enhanced_plan_execute_v6()
       result = await agent.arun("Calculate compound interest")

   With custom configuration::

       agent = create_enhanced_plan_execute_v6(
           name="research_planner",
           planner_config=AugLLMConfig(model="gpt-4", temperature=0.2),
           executor_tools=[tavily_search_tool],
           max_iterations=15
       )
       result = await agent.arun("Research and analyze market trends")


   .. autolink-examples:: create_enhanced_plan_execute_v6
      :collapse:

.. py:function:: create_research_plan_execute_v6(executor_tools: list | None = None) -> haive.agents.multi.agent.MultiAgent

   Create a plan and execute agent optimized for research tasks.


   .. autolink-examples:: create_research_plan_execute_v6
      :collapse:

.. py:function:: create_simple_plan_execute_v6(executor_tools: list | None = None) -> haive.agents.multi.agent.MultiAgent

   Create a simple plan and execute agent with default settings.


   .. autolink-examples:: create_simple_plan_execute_v6
      :collapse:

.. py:function:: get_next_step_v6(plan: haive.agents.planning.base.models.BasePlan[haive.agents.planning.base.models.PlanContent], completed_steps: list[str]) -> str | None

   Get the next step ID to execute based on plan and completed steps.


   .. autolink-examples:: get_next_step_v6
      :collapse:

.. py:function:: process_executor_output_v6(state: PlanExecuteState, executor_result: ExecutionResult) -> dict

   Process executor output and update state.


   .. autolink-examples:: process_executor_output_v6
      :collapse:

.. py:function:: process_planner_output_v6(state: PlanExecuteState, planner_result: haive.agents.planning.base.models.BasePlan[haive.agents.planning.base.models.PlanContent]) -> dict

   Process planner output and update state.


   .. autolink-examples:: process_planner_output_v6
      :collapse:

.. py:function:: should_continue_v6(state: PlanExecuteState) -> str

   Enhanced routing logic for V6 workflow.


   .. autolink-examples:: should_continue_v6
      :collapse:

.. py:function:: test_enhanced_plan_execute_v6()
   :async:


   Test the enhanced plan and execute V6 system.


   .. autolink-examples:: test_enhanced_plan_execute_v6
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.enhanced_plan_execute_v6
   :collapse:
   
.. autolink-skip:: next
