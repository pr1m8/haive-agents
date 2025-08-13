#!/usr/bin/env python3
"""Plan-and-Execute Pattern Example

This example demonstrates how to create a planning agent that:
1. Breaks down complex tasks into actionable steps
2. Creates detailed execution plans with dependencies
3. Executes steps with feedback and adaptation
4. Provides progress tracking and error handling

The pattern separates planning from execution, allowing for more robust
and adaptable task completion."""

import asyncio
from datetime import datetime
from enum import Enum
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


class StepStatus(str, Enum):
    """Status of individual plan steps."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class PlanStep(BaseModel):
    """Individual step in an execution plan."""

    step_id: str = Field(description="Unique identifier for this step")
    title: str = Field(description="Brief title of the step")
    description: str = Field(description="Detailed description of what to do")
    prerequisites: list[str] = Field(
        default_factory=list, description="Step IDs that must complete first"
    )
    estimated_duration: str | None = Field(
        default=None, description="Estimated time to complete"
    )
    status: StepStatus = Field(default=StepStatus.PENDING, description="Current status")
    result: str | None = Field(
        default=None, description="Result or output from execution"
    )
    notes: list[str] = Field(
        default_factory=list, description="Execution notes and observations"
    )


class ExecutionPlan(BaseModel):
    """Complete execution plan with metadata."""

    plan_id: str = Field(description="Unique plan identifier")
    title: str = Field(description="Plan title")
    description: str = Field(description="Overall plan description")
    steps: list[PlanStep] = Field(description="Ordered list of execution steps")
    created_at: datetime = Field(default_factory=datetime.now)
    estimated_total_duration: str | None = Field(
        default=None, description="Total estimated time"
    )

    def get_next_steps(self) -> list[PlanStep]:
        """Get steps that are ready to execute (prerequisites met)."""
        completed_steps = {
            step.step_id for step in self.steps if step.status == StepStatus.COMPLETED
        }

        ready_steps = []
        for step in self.steps:
            if step.status == StepStatus.PENDING:
                # Check if all prerequisites are completed
                if all(prereq in completed_steps for prereq in step.prerequisites):
                    ready_steps.append(step)

        return ready_steps

    def get_step(self, step_id: str) -> PlanStep | None:
        """Get step by ID."""
        return next((step for step in self.steps if step.step_id == step_id), None)

    def update_step_status(
        self,
        step_id: str,
        status: StepStatus,
        result: str = None,
        notes: list[str] = None,
    ):
        """Update step status and add result/notes."""
        step = self.get_step(step_id)
        if step:
            step.status = status
            if result:
                step.result = result
            if notes:
                step.notes.extend(notes)


class PlannerAgent(SimpleAgentV3):
    """Agent specialized in breaking down complex tasks into actionable plans."""

    def __init__(self, name: str = "planner", **kwargs):
        super().__init__(
            name=name,
            engine=AugLLMConfig(
                temperature=0.3,  # More focused for planning
                structured_output_model=ExecutionPlan,
                system_message="""You are an expert project planner and task breakdown specialist.

Your role is to analyze complex tasks and create detailed, actionable execution plans.

Key principles:
- Break tasks into small, specific steps (15-30 minutes each)
- Identify dependencies and prerequisites clearly
- Consider potential risks and mitigation strategies
- Make steps actionable with clear success criteria
- Estimate realistic timeframes
- Order steps logically for efficient execution

For each step, provide:
- Clear, actionable description
- Specific deliverables or outcomes
- Prerequisites that must be completed first
- Realistic time estimates

Create plans that are thorough but practical, allowing for iterative execution and adaptation.""",
            ),
            **kwargs,
        )


class ExecutorAgent(ReactAgent):
    """Agent that executes individual plan steps with tools and feedback."""

    def __init__(self, name: str = "executor", tools: list = None, **kwargs):
        # Default tools for common execution tasks
        if tools is None:
            tools = []

        super().__init__(
            name=name,
            engine=AugLLMConfig(
                temperature=0.5,
                system_message="""You are a skilled task executor focused on completing specific plan steps.

Your role is to:
- Execute individual plan steps thoroughly and systematically
- Use available tools to accomplish objectives
- Provide detailed feedback on results and progress
- Identify issues and suggest solutions
- Document outcomes clearly for the next steps

When executing a step:
1. Understand the objective clearly
2. Use available tools effectively
3. Verify completion against success criteria
4. Document results and any issues encountered
5. Suggest improvements for future similar tasks

Be thorough, methodical, and provide actionable feedback.""",
            ),
            tools=tools,
            **kwargs,
        )


class PlanAndExecuteWorkflow(EnhancedMultiAgentV4):
    """Complete plan-and-execute workflow combining planning and execution agents."""

    def __init__(
        self,
        planner_name: str = "planner",
        executor_name: str = "executor",
        executor_tools: list = None,
        **kwargs,
    ):
        # Create specialized agents
        self.planner = PlannerAgent(name=planner_name)
        self.executor = ExecutorAgent(name=executor_name, tools=executor_tools or [])

        super().__init__(
            agents=[self.planner, self.executor],
            execution_mode="custom",  # We'll handle execution manually
            **kwargs,
        )

        self.current_plan: ExecutionPlan | None = None
        self.execution_log: list[dict[str, Any]] = []

    async def create_plan(
        self, task: str, context: dict[str, Any] = None
    ) -> ExecutionPlan:
        """Create an execution plan for the given task."""
        planning_prompt = f"""Please create a detailed execution plan for this task:.

TASK: {task}

"""
        if context:
            planning_prompt += "CONTEXT:\n"
            for key, value in context.items():
                planning_prompt += f"- {key}: {value}\n"
            planning_prompt += "\n"

        planning_prompt += """Please break this down into specific, actionable steps with clear dependencies.
Each step should be:
- Small enough to complete in 15-30 minutes
- Have clear success criteria
- Include realistic time estimates
- Properly sequenced with dependencies

Focus on practical execution and deliverable outcomes."""

        print(f"🎯 Creating execution plan for: {task}")

        # Use planner agent to create structured plan
        plan = await self.planner.arun(planning_prompt)

        if isinstance(plan, ExecutionPlan):
            self.current_plan = plan
            print(f"📋 Plan created with {len(plan.steps)} steps")
            self._display_plan_summary()
            return plan
        raise ValueError(f"Planner returned unexpected type: {type(plan)}")

    async def execute_plan(
        self,
        plan: ExecutionPlan | None = None,
        max_parallel_steps: int = 1,
        interactive: bool = True,
    ) -> dict[str, Any]:
        """Execute the plan step by step with feedback and adaptation."""
        if plan is None:
            plan = self.current_plan

        if plan is None:
            raise ValueError("No plan provided and no current plan available")

        print(f"\n🚀 Starting execution of plan: {plan.title}")
        execution_start = datetime.now()

        completed_steps = 0
        failed_steps = 0

        while True:
            # Get next executable steps
            ready_steps = plan.get_next_steps()

            if not ready_steps:
                # Check if we're done or stuck
                pending_steps = [
                    s for s in plan.steps if s.status == StepStatus.PENDING
                ]
                if not pending_steps:
                    break  # All done!
                print(
                    "⚠️  No steps ready to execute. Remaining steps have unmet prerequisites."
                )
                break

            # Execute steps (limit parallel execution)
            steps_to_execute = ready_steps[:max_parallel_steps]

            for step in steps_to_execute:
                print(f"\n▶️  Executing Step {step.step_id}: {step.title}")

                if interactive:
                    proceed = (
                        input("Continue with this step? (y/n/s=skip): ").lower().strip()
                    )
                    if proceed == "n":
                        print("Execution stopped by user")
                        return self._create_execution_summary(
                            plan, execution_start, completed_steps, failed_steps
                        )
                    if proceed == "s":
                        step.status = StepStatus.SKIPPED
                        step.notes.append("Skipped by user request")
                        print(f"⏭️  Skipped step: {step.title}")
                        continue

                # Execute the step
                success = await self._execute_step(step, plan)

                if success:
                    completed_steps += 1
                    print(f"✅ Completed: {step.title}")
                else:
                    failed_steps += 1
                    print(f"❌ Failed: {step.title}")

                    if interactive:
                        retry = input("Step failed. Retry? (y/n): ").lower().strip()
                        if retry == "y":
                            # Reset step and retry
                            step.status = StepStatus.PENDING
                            step.result = None
                            continue

        return self._create_execution_summary(
            plan, execution_start, completed_steps, failed_steps
        )

    async def _execute_step(self, step: PlanStep, plan: ExecutionPlan) -> bool:
        """Execute a single step using the executor agent."""
        try:
            step.status = StepStatus.IN_PROGRESS

            # Prepare execution context
            execution_prompt = f"""Execute this plan step:.

STEP: {step.title}
DESCRIPTION: {step.description}

CONTEXT:
- Plan: {plan.title}
- Step ID: {step.step_id}
- Prerequisites completed: {', '.join(step.prerequisites) if step.prerequisites else 'None'}
- Estimated duration: {step.estimated_duration or 'Not specified'}

Please execute this step thoroughly and provide detailed feedback on:
1. What actions you took
2. What results were achieved
3. Any issues or obstacles encountered
4. Whether the step objective was fully met
5. Any recommendations for improvement

Be specific about outcomes and deliverables."""

            # Execute using executor agent
            result = await self.executor.arun(execution_prompt)

            # Update step with results
            step.status = StepStatus.COMPLETED
            step.result = str(result)
            step.notes.append(f"Executed at {datetime.now().strftime('%H:%M:%S')}")

            # Log execution
            self.execution_log.append(
                {
                    "step_id": step.step_id,
                    "timestamp": datetime.now().isoformat(),
                    "status": "completed",
                    "result": str(result),
                }
            )

            return True

        except Exception as e:
            step.status = StepStatus.FAILED
            step.result = f"ERROR: {e!s}"
            step.notes.append(f"Failed at {datetime.now().strftime('%H:%M:%S')}: {e!s}")

            self.execution_log.append(
                {
                    "step_id": step.step_id,
                    "timestamp": datetime.now().isoformat(),
                    "status": "failed",
                    "error": str(e),
                }
            )

            return False

    def _display_plan_summary(self):
        """Display a summary of the current plan."""
        if not self.current_plan:
            return

        plan = self.current_plan
        print(f"\n📋 Plan Summary: {plan.title}")
        print(f"Description: {plan.description}")
        print(f"Total Steps: {len(plan.steps)}")
        if plan.estimated_total_duration:
            print(f"Estimated Duration: {plan.estimated_total_duration}")

        print("\nSteps Overview:")
        for i, step in enumerate(plan.steps, 1):
            prereq_str = (
                f" (requires: {', '.join(step.prerequisites)})"
                if step.prerequisites
                else ""
            )
            duration_str = (
                f" [{step.estimated_duration}]" if step.estimated_duration else ""
            )
            print(f"  {i}. {step.title}{prereq_str}{duration_str}")

    def _create_execution_summary(
        self, plan: ExecutionPlan, start_time: datetime, completed: int, failed: int
    ) -> dict[str, Any]:
        """Create execution summary with results and metrics."""
        end_time = datetime.now()
        duration = end_time - start_time

        total_steps = len(plan.steps)
        skipped = len([s for s in plan.steps if s.status == StepStatus.SKIPPED])
        pending = len([s for s in plan.steps if s.status == StepStatus.PENDING])

        summary = {
            "plan_id": plan.plan_id,
            "plan_title": plan.title,
            "execution_duration": str(duration),
            "total_steps": total_steps,
            "completed_steps": completed,
            "failed_steps": failed,
            "skipped_steps": skipped,
            "pending_steps": pending,
            "success_rate": completed / max(total_steps - skipped, 1) * 100,
            "execution_log": self.execution_log,
            "final_status": "completed" if pending == 0 and failed == 0 else "partial",
        }

        print("\n📊 Execution Summary:")
        print(f"Duration: {duration}")
        print(
            f"Steps - Completed: {completed}, Failed: {failed}, Skipped: {skipped}, Pending: {pending}"
        )
        print(f"Success Rate: {summary['success_rate']:.1f}%")

        return summary


# Example usage and demonstration
async def main():
    """Demonstrate the plan-and-execute pattern with a practical example."""
    print("=== Plan-and-Execute Pattern Example ===\n")

    # Create the workflow
    workflow = PlanAndExecuteWorkflow(
        planner_name="project_planner", executor_name="task_executor"
    )

    # Example 1: Software Development Task
    print("Example 1: Creating a Python Package")

    task = """Create a new Python package called 'data-validator' that provides utilities for validating data structures. 

Requirements:
- Package should have proper structure (setup.py, src/, tests/, docs/)
- Include at least 3 validation functions (email, phone, date)
- Have comprehensive tests with >90% coverage
- Include documentation with examples
- Be publishable to PyPI

The package should be professional quality and follow Python best practices."""

    context = {
        "target_audience": "Data engineers and analysts",
        "python_version": "3.8+",
        "testing_framework": "pytest",
        "documentation": "Sphinx",
        "license": "MIT",
    }

    try:
        # Create execution plan
        plan = await workflow.create_plan(task, context)

        print(f"\n📋 Generated plan with {len(plan.steps)} steps")

        # Show detailed plan
        print("\nDetailed Plan:")
        for step in plan.steps:
            print(f"\n🔸 Step {step.step_id}: {step.title}")
            print(f"   Description: {step.description}")
            if step.prerequisites:
                print(f"   Prerequisites: {', '.join(step.prerequisites)}")
            if step.estimated_duration:
                print(f"   Estimated Time: {step.estimated_duration}")

        # Ask if user wants to execute
        if input("\nExecute this plan? (y/n): ").lower().strip() == "y":
            execution_summary = await workflow.execute_plan(
                plan=plan, interactive=True, max_parallel_steps=1
            )

            print("\n✅ Plan execution completed!")
            print(f"Final Status: {execution_summary['final_status']}")

    except Exception as e:
        print(f"❌ Error in plan-and-execute workflow: {e}")

    # Example 2: Research Project
    print("\n" + "=" * 50)
    print("Example 2: Market Research Project")

    research_task = """Conduct comprehensive market research for launching a new AI-powered productivity app.

Research should cover:
- Target market analysis and user personas
- Competitive landscape and feature comparison
- Pricing strategy recommendations
- Go-to-market strategy
- Risk assessment and mitigation strategies

Deliverable: Executive summary with actionable recommendations."""

    research_context = {
        "industry": "Productivity software",
        "target_market": "Knowledge workers and small teams",
        "budget": "$10,000",
        "timeline": "4 weeks",
        "team_size": "2 researchers",
    }

    try:
        research_plan = await workflow.create_plan(research_task, research_context)
        print(f"\n📋 Research plan created with {len(research_plan.steps)} steps")

        # Just show the plan, don't execute
        workflow._display_plan_summary()

    except Exception as e:
        print(f"❌ Error creating research plan: {e}")


if __name__ == "__main__":
    # Run the example
    asyncio.run(main())
