"""Tests for the PlannerAgent."""

import pytest
from haive.agents.simple import SimpleAgent
from haive.agents.planning_v2.base.models import Status, Plan, Task
from haive.agents.planning_v2.base.planner.models import TaskPlan
from haive.agents.planning_v2.base.planner.prompts import planner_prompt, create_planner_prompt
from haive.core.engine.aug_llm import AugLLMConfig


@pytest.mark.asyncio
async def test_planner_basic():
    """Test basic planner functionality without context."""
    # Create engine with structured output AND prompt template
    # Use concrete TaskPlan instead of generic Plan[Task]
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=TaskPlan,  # Use concrete class
        prompt_template=planner_prompt  # Pass prompt to engine, not agent
    )
    
    # Create planner using SimpleAgent directly
    planner = SimpleAgent(
        name="test_planner",
        engine=engine
        # Remove prompt_template from here
    )
    
    # Run planner
    result = await planner.arun({
        "objective": "Build a simple REST API for a todo list"
    })
    
    # Debug output
    print(f"\nResult type: {type(result)}")
    print(f"Result objective: {getattr(result, 'objective', 'NO OBJECTIVE')}")
    print(f"Result status: {getattr(result, 'status', 'NO STATUS')}")
    print(f"Result steps: {getattr(result, 'steps', 'NO STEPS')}")
    print(f"Result as dict: {result.model_dump() if hasattr(result, 'model_dump') else 'NO MODEL_DUMP'}")
    
    # Assertions
    assert isinstance(result, (Plan, TaskPlan))  # Accept either since TaskPlan inherits from Plan
    assert result.objective == "Build a simple REST API for a todo list"
    assert result.status == Status.PENDING
    assert len(result.steps) > 0
    
    # Check steps
    for step in result.steps:
        assert isinstance(step, Task)
        assert step.objective  # Task uses 'objective' not 'description'
        assert step.status == Status.PENDING
    
    # Print output for visual verification
    print(f"\nGenerated {len(result.steps)} steps:")
    for i, step in enumerate(result.steps, 1):
        print(f"{i}. {step.objective}")


@pytest.mark.asyncio
async def test_planner_with_context():
    """Test planner with additional context."""
    context = """Technical requirements:
    - Use FastAPI framework
    - PostgreSQL database
    - Include JWT authentication
    - Docker deployment
    """
    
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=create_planner_prompt(context)  # Pass prompt to engine
    )
    
    planner = SimpleAgent(
        name="contextual_planner",
        engine=engine
    )
    
    result = await planner.arun({
        "objective": "Build a simple REST API for a todo list"
    })
    
    # Assertions
    assert isinstance(result, Plan)
    assert len(result.steps) > 0
    
    # Check that context influenced the plan
    # Convert all steps to lowercase for checking
    all_steps_text = " ".join(step.description.lower() for step in result.steps)
    
    # Should mention some of our context items
    context_keywords = ["fastapi", "postgresql", "jwt", "docker", "authentication"]
    found_keywords = [kw for kw in context_keywords if kw in all_steps_text]
    
    print(f"\nContext keywords found in plan: {found_keywords}")
    assert len(found_keywords) > 0, "Plan should incorporate context requirements"
    
    # Print first few steps
    print(f"\nFirst 5 steps with context:")
    for i, step in enumerate(result.steps[:5], 1):
        print(f"{i}. {step.description}")


@pytest.mark.asyncio
async def test_planner_complex_objective():
    """Test planner with a more complex objective."""
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt  # Pass prompt to engine
    )
    
    planner = SimpleAgent(
        name="complex_planner",
        engine=engine
    )
    
    result = await planner.arun({
        "objective": "Migrate a monolithic Django application to microservices architecture"
    })
    
    # This should generate more steps
    assert len(result.steps) >= 5
    assert result.objective == "Migrate a monolithic Django application to microservices architecture"
    
    # Check for logical progression
    print(f"\nComplex plan with {len(result.steps)} steps:")
    for i, step in enumerate(result.steps[:10], 1):  # Show first 10
        print(f"{i}. {step.description}")
    
    if len(result.steps) > 10:
        print(f"... and {len(result.steps) - 10} more steps")


@pytest.mark.asyncio
async def test_planner_partial_context():
    """Test using partial directly for context."""
    # Use partial to add context
    context_prompt = planner_prompt.partial(
        context_section="\nContext: This is for a startup MVP, prioritize speed over perfection.\n"
    )
    
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=context_prompt  # Pass prompt to engine
    )
    
    planner = SimpleAgent(
        name="mvp_planner",
        engine=engine
    )
    
    result = await planner.arun({
        "objective": "Create a landing page with email signup"
    })
    
    assert isinstance(result, Plan)
    assert len(result.steps) > 0
    
    print(f"\nMVP-focused plan:")
    for i, step in enumerate(result.steps, 1):
        print(f"{i}. {step.description}")


@pytest.mark.asyncio
async def test_planner_computed_properties():
    """Test the computed properties of the Plan model."""
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt  # Pass prompt to engine
    )
    
    planner = SimpleAgent(
        name="test_planner",
        engine=engine
    )
    
    result = await planner.arun({
        "objective": "Set up CI/CD pipeline"
    })
    
    # Test computed properties
    assert result.current_step == 0  # All pending, so first step
    assert result.completed_steps == 0
    assert result.total_steps == len(result.steps)
    assert result.progress_percentage == 0.0
    
    # Manually complete some steps to test progress
    if len(result.steps) >= 2:
        result.steps[0].status = Status.COMPLETED
        assert result.completed_steps == 1
        assert result.current_step == 1  # Should move to next
        
        result.steps[1].status = Status.IN_PROGRESS
        assert result.current_step == 1  # Still on step 1 (in progress)
        
        result.steps[1].status = Status.COMPLETED
        assert result.completed_steps == 2
        assert result.progress_percentage == (2 / len(result.steps)) * 100