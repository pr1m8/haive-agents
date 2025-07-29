"""Example core module.

This module provides example functionality for the Haive framework.

Functions:
    run_example: Run Example functionality.
"""

"""Quick example of using SequentialAgent with imported AugLLMConfig components.

from typing import Any
This demonstrates how to easily chain together pre-configured components
for a sequential reasoning workflow.
"""

from haive.core.utils.pydantic_utils import pretty_print

# Import the pre-configured AugLLMConfigs directly
from haive.agents.reasoning_and_critique.self_discover.engines import (
    create_adapt_engine,
    create_select_engine,
    create_structure_engine,
)
from haive.agents.sequential.config import SequentialAgentConfig

# Create engines for the workflow
select_engine = create_select_engine()
adapt_engine = create_adapt_engine()
structure_engine = create_structure_engine()

# Create the sequential agent with the imported components
agent = SequentialAgentConfig.from_components(
    components=[select_engine, adapt_engine, structure_engine],
    name="reasoning_workflow_agent",
    # Optionally provide custom step names
    step_names=["select_modules", "adapt_modules", "create_plan"],
).build_agent()

# Print the workflow


def run_example() -> Any:
    # Define a task
    task = "Design an algorithm to detect fraudulent credit card transactions"

    # Run the agent (automatically handles data passing between steps)
    result = agent.run({"task_description": task})

    # Display the final plan

    if "plan" in result:
        pretty_print(result["plan"], "Reasoning Plan")
    else:
        pretty_print(result, "Complete Result")

    return result


if __name__ == "__main__":
    run_example()
