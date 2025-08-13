
:py:mod:`agents.planning.enhanced_plan_execute_v5`
==================================================

.. py:module:: agents.planning.enhanced_plan_execute_v5

Enhanced Plan & Execute V5 - Modern Haive Implementation with Custom Models and Agents.

This module provides a completely redesigned Plan & Execute implementation using the latest
Haive architecture patterns, enhanced agents, and modern multi-agent orchestration.

## Key Features

- **MultiAgent**: Latest multi-agent orchestration with state management
- **SimpleAgentV3**: Enhanced planning and replanning with hooks system
- **ReactAgent**: Advanced tool-based execution with real-time feedback
- **Custom Pydantic Models**: Structured output designed for planning workflows
- **Modern Prompt Engineering**: Context-aware prompts with structured templates
- **Comprehensive Monitoring**: Full hooks system for execution tracking
- **Dynamic Recompilation**: Real-time agent updates and tool management

## Architecture

```
PlannerAgentV3 (SimpleAgentV3)
    ↓ (structured Plan model)
ExecutorAgentV3 (ReactAgent) ←─┐
    ↓ (execution results)       │
Routing Logic ──→ Continue ────┘
    ↓
ReplannerAgentV3 (SimpleAgentV3)
    ↓ (structured Decision model)
Final Response or Loop Back
```

## Usage

### Basic Usage
```python
from haive.agents.planning.enhanced_plan_execute_v5 import create_enhanced_plan_execute_v5

# Create with default tools
agent = create_enhanced_plan_execute_v5()
result = await agent.arun("Calculate compound interest on $1000 at 5% for 10 years")

# Create with custom tools
from haive.tools import web_search_tool, calculator_tool
agent = create_enhanced_plan_execute_v5(
    name="research_planner",
    tools=[web_search_tool, calculator_tool]
)
result = await agent.arun("Research Tesla stock performance and calculate ROI")
```

### Advanced Configuration
```python
agent = create_enhanced_plan_execute_v5(
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
    tools=[custom_tool1, custom_tool2],
    max_iterations=10,
    enable_hooks=True
)

# Add custom hooks
@agent.before_run
def track_execution(context):
    print(f"Starting planning workflow: {context.agent_name}")

result = await agent.arun("Complex multi-step research task")
```

## Custom Models

The implementation uses custom Pydantic models designed specifically for planning:

- **TaskPlan**: Structured plan with steps, priorities, and dependencies
- **ExecutionStatus**: Rich execution tracking with success/failure states
- **PlanningDecision**: Intelligent routing decisions with reasoning
- **PlanExecuteState**: Enhanced state management for multi-agent coordination

## When to Use

✅ **Use this implementation when**:
- You need modern Haive architecture patterns
- Enhanced monitoring and debugging is important
- You want structured output and type safety
- Dynamic agent recompilation is needed
- Production-ready error handling is required

❌ **Consider alternatives when**:
- Simple tasks that don't need planning (use ReactAgent directly)
- Legacy compatibility is required (use clean_plan_execute)
- Minimal complexity is preferred (use SimpleAgent)

## Status: Next-Generation Planning

This is the future of planning agents in Haive, showcasing the full power
of the enhanced base agent pattern and modern multi-agent orchestration.


.. autolink-examples:: agents.planning.enhanced_plan_execute_v5
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v5.EnhancedPlanExecuteState
   agents.planning.enhanced_plan_execute_v5.ExecutionResult
   agents.planning.enhanced_plan_execute_v5.PlanningDecision
   agents.planning.enhanced_plan_execute_v5.TaskPlan
   agents.planning.enhanced_plan_execute_v5.TaskStep


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedPlanExecuteState:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedPlanExecuteState {
        node [shape=record];
        "EnhancedPlanExecuteState" [label="EnhancedPlanExecuteState"];
        "haive.core.schema.prebuilt.multi_agent_state.MultiAgentState" -> "EnhancedPlanExecuteState";
      }

.. autoclass:: agents.planning.enhanced_plan_execute_v5.EnhancedPlanExecuteState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionResult {
        node [shape=record];
        "ExecutionResult" [label="ExecutionResult"];
        "pydantic.BaseModel" -> "ExecutionResult";
      }

.. autopydantic_model:: agents.planning.enhanced_plan_execute_v5.ExecutionResult
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

   Inheritance diagram for PlanningDecision:

   .. graphviz::
      :align: center

      digraph inheritance_PlanningDecision {
        node [shape=record];
        "PlanningDecision" [label="PlanningDecision"];
        "pydantic.BaseModel" -> "PlanningDecision";
      }

.. autopydantic_model:: agents.planning.enhanced_plan_execute_v5.PlanningDecision
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

   Inheritance diagram for TaskPlan:

   .. graphviz::
      :align: center

      digraph inheritance_TaskPlan {
        node [shape=record];
        "TaskPlan" [label="TaskPlan"];
        "pydantic.BaseModel" -> "TaskPlan";
      }

.. autopydantic_model:: agents.planning.enhanced_plan_execute_v5.TaskPlan
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

   Inheritance diagram for TaskStep:

   .. graphviz::
      :align: center

      digraph inheritance_TaskStep {
        node [shape=record];
        "TaskStep" [label="TaskStep"];
        "pydantic.BaseModel" -> "TaskStep";
      }

.. autopydantic_model:: agents.planning.enhanced_plan_execute_v5.TaskStep
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

   agents.planning.enhanced_plan_execute_v5._add_monitoring_hooks
   agents.planning.enhanced_plan_execute_v5.create_enhanced_plan_execute_v5
   agents.planning.enhanced_plan_execute_v5.create_research_plan_execute
   agents.planning.enhanced_plan_execute_v5.create_simple_enhanced_plan_execute
   agents.planning.enhanced_plan_execute_v5.get_next_step_id
   agents.planning.enhanced_plan_execute_v5.should_continue_enhanced
   agents.planning.enhanced_plan_execute_v5.test_enhanced_plan_execute

.. py:function:: _add_monitoring_hooks(workflow: haive.agents.multi.enhanced.multi_agent_v4.MultiAgent) -> None

   Add comprehensive monitoring hooks to the workflow.


   .. autolink-examples:: _add_monitoring_hooks
      :collapse:

.. py:function:: create_enhanced_plan_execute_v5(name: str = 'EnhancedPlanExecuteV5', planner_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, executor_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, replanner_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, tools: list | None = None, max_iterations: int = 20, enable_hooks: bool = True) -> haive.agents.multi.enhanced.multi_agent_v4.MultiAgent

   Create enhanced Plan & Execute agent using modern Haive patterns.

   :param name: Name for the multi-agent system
   :param planner_config: Configuration for the planning agent
   :param executor_config: Configuration for the execution agent
   :param replanner_config: Configuration for the replanning agent
   :param tools: Tools available to the executor
   :param max_iterations: Maximum planning iterations
   :param enable_hooks: Whether to enable the hooks system

   :returns: Complete planning workflow system
   :rtype: MultiAgent

   .. rubric:: Examples

   Basic usage::

       agent = create_enhanced_plan_execute_v5()
       result = await agent.arun("Calculate compound interest")

   With custom configuration::

       agent = create_enhanced_plan_execute_v5(
           name="research_planner",
           planner_config=AugLLMConfig(model="gpt-4", temperature=0.2),
           tools=[web_search_tool, calculator_tool],
           max_iterations=15
       )
       result = await agent.arun("Research and analyze market trends")


   .. autolink-examples:: create_enhanced_plan_execute_v5
      :collapse:

.. py:function:: create_research_plan_execute(tools: list | None = None) -> haive.agents.multi.enhanced.multi_agent_v4.MultiAgent

   Create a plan and execute agent optimized for research tasks.


   .. autolink-examples:: create_research_plan_execute
      :collapse:

.. py:function:: create_simple_enhanced_plan_execute(tools: list | None = None) -> haive.agents.multi.enhanced.multi_agent_v4.MultiAgent

   Create a simple enhanced plan and execute agent with default settings.


   .. autolink-examples:: create_simple_enhanced_plan_execute
      :collapse:

.. py:function:: get_next_step_id(plan: TaskPlan, completed_steps: list[str]) -> str | None

   Get the next step ID to execute based on plan and completed steps.


   .. autolink-examples:: get_next_step_id
      :collapse:

.. py:function:: should_continue_enhanced(state: EnhancedPlanExecuteState) -> str

   Enhanced routing logic based on current state and decisions.


   .. autolink-examples:: should_continue_enhanced
      :collapse:

.. py:function:: test_enhanced_plan_execute()
   :async:


   Test the enhanced plan and execute system.


   .. autolink-examples:: test_enhanced_plan_execute
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.enhanced_plan_execute_v5
   :collapse:
   
.. autolink-skip:: next
