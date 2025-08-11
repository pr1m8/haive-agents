"""Simple test to verify TaskPlan works directly."""

from haive.agents.planning_v2.base.models import Plan, Status, Task
from haive.agents.planning_v2.base.planner.models import TaskPlan

# Test creating TaskPlan directly
plan = TaskPlan(
    objective="Test objective",
    steps=[Task(objective="Step 1"), Task(objective="Step 2")],
)

print(f"TaskPlan created: {plan}")
print(f"Objective: {plan.objective}")
print(f"Steps: {len(plan.steps)}")
print(f"Status: {plan.status}")

# Test model_dump
print(f"\nModel dump: {plan.model_dump()}")

# Check if TaskPlan is fully defined
print(f"\nTaskPlan.__name__: {TaskPlan.__name__}")
print(f"TaskPlan.__module__: {TaskPlan.__module__}")
print(f"TaskPlan model fields: {list(TaskPlan.model_fields.keys())}")

# Try model_rebuild
print("\nCalling model_rebuild...")
TaskPlan.model_rebuild()
print("Model rebuild successful!")
