#!/usr/bin/env python3
"""SimpleAgent v3 Structured Output Documentation and Examples.

This module provides comprehensive documentation and examples for using structured
output functionality with SimpleAgent v3, including Pydantic model integration,
tool-based structured responses, and real LLM execution patterns.

The structured output system in SimpleAgent v3 uses a tool-based approach where
Pydantic models are converted to LangChain tools, allowing the LLM to generate
properly formatted and validated responses.

Examples:
    Basic structured output::

        from haive.agents.simple.agent_v3 import SimpleAgentV3
        from haive.core.engine.aug_llm import AugLLMConfig
        from pydantic import BaseModel, Field

        class TaskAnalysis(BaseModel):
            task_type: str = Field(description="Type of task")
            complexity: int = Field(ge=1, le=10, description="Complexity 1-10")

        agent = SimpleAgentV3(
            name="analyzer",
            engine=AugLLMConfig(
                structured_output_model=TaskAnalysis,
                temperature=0.2
            )
        )

        result = agent.run("Analyze building a web app")
        # Returns structured TaskAnalysis response

    Multiple structured output models::

        class QuestionAnswer(BaseModel):
            question: str = Field(description="Original question")
            answer: str = Field(description="Direct answer")
            reasoning: str = Field(description="Reasoning")

        agent = SimpleAgentV3(
            name="qa_agent",
            engine=AugLLMConfig(structured_output_model=QuestionAnswer)
        )

See Also:
    haive.agents.simple.agent_v3.SimpleAgentV3: Main agent implementation
    haive.core.engine.aug_llm.AugLLMConfig: Engine configuration
    haive.core.schema.prebuilt.llm_state.LLMState: State management
"""

import logging
from typing import Any, Dict, List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from pydantic import BaseModel, Field, field_validator

from haive.agents.simple.agent_v3 import SimpleAgentV3

logger = logging.getLogger(__name__)


# ============================================================================
# STRUCTURED OUTPUT MODEL EXAMPLES
# ============================================================================


class TaskAnalysis(BaseModel):
    """Comprehensive task analysis model for project planning.

    This model provides structured analysis of tasks including complexity
    assessment, step breakdown, time estimation, and confidence levels.
    Designed for use with SimpleAgentV3 structured output functionality.

    Attributes:
        task_type: The category of task (e.g., 'development', 'analysis', 'research').
        complexity: Task complexity rating on a scale of 1-10 where 1 is trivial
            and 10 is extremely complex requiring significant expertise.
        steps_required: Ordered list of specific steps needed to complete the task.
            Each step should be actionable and clearly defined.
        estimated_time: Time estimate in minutes for task completion by a competent
            individual with appropriate resources.
        confidence: Confidence level in the analysis accuracy, ranging from 0.0
            (completely uncertain) to 1.0 (completely certain).

    Examples:
        Creating a task analysis::

            analysis = TaskAnalysis(
                task_type="development",
                complexity=7,
                steps_required=[
                    "Define requirements and scope",
                    "Design system architecture",
                    "Implement core functionality",
                    "Write tests and documentation",
                    "Deploy and monitor"
                ],
                estimated_time=1200,  # 20 hours
                confidence=0.85
            )

    Note:
        This model is automatically converted to a LangChain tool when used
        with SimpleAgentV3's structured_output_model parameter. The LLM
        will generate responses that conform to this schema.
    """

    task_type: str = Field(
        description="Type of task (e.g., 'development', 'analysis', 'research')",
        examples=["development", "analysis", "research", "planning", "optimization"],
    )

    complexity: int = Field(
        ge=1,
        le=10,
        description="Task complexity on scale of 1-10 (1=trivial, 10=extremely complex)",
        examples=[3, 7, 9],
    )

    steps_required: List[str] = Field(
        description="Ordered list of specific actionable steps needed",
        min_items=1,
        max_items=15,
        examples=[
            ["Research requirements", "Create design", "Implement solution"],
            ["Gather data", "Analyze patterns", "Generate report"],
        ],
    )

    estimated_time: int = Field(
        ge=1,
        description="Estimated completion time in minutes",
        examples=[30, 240, 1440],  # 30 min, 4 hours, 24 hours
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence in analysis accuracy (0.0=uncertain, 1.0=certain)",
        examples=[0.6, 0.8, 0.95],
    )

    @field_validator("task_type")
    @classmethod
    def validate_task_type(cls, v: str) -> str:
        """Validate task type is non-empty and reasonable length.

        Args:
            v: Task type string to validate

        Returns:
            Validated task type string

        Raises:
            ValueError: If task type is empty or too long
        """
        if not v or not v.strip():
            raise TypeError("Task type cannot be empty")
        if len(v.strip()) > 50:
            raise TypeError("Task type must be 50 characters or less")
        return v.strip().lower()

    @field_validator("steps_required")
    @classmethod
    def validate_steps(cls, v: List[str]) -> List[str]:
        """Validate steps are non-empty and reasonable.

        Args:
            v: List of step strings to validate

        Returns:
            Validated list of steps

        Raises:
            ValueError: If any step is empty or list is invalid
        """
        if not v:
            raise ValueError("At least one step is required")

        cleaned_steps = []
        for i, step in enumerate(v):
            if not step or not step.strip():
                raise ValueError(f"Step {i+1} cannot be empty")
            if len(step.strip()) > 200:
                raise ValueError(f"Step {i+1} must be 200 characters or less")
            cleaned_steps.append(step.strip())

        return cleaned_steps


class QuestionAnswer(BaseModel):
    """Structured question-answer response model.

    This model provides a standardized format for answering questions with
    explicit reasoning and certainty assessment. Ideal for Q&A systems,
    educational applications, and knowledge retrieval scenarios.

    Attributes:
        question: The original question being answered, restated for clarity.
        answer: Direct, concise answer to the question without unnecessary elaboration.
        reasoning: Brief explanation of the logic, evidence, or methodology used
            to arrive at the answer.
        certainty: Level of confidence in the answer accuracy using standardized
            categories ('high', 'medium', 'low').

    Examples:
        Creating a Q&A response::

            qa = QuestionAnswer(
                question="What is the capital of France?",
                answer="Paris",
                reasoning="Paris has been the capital of France since 987 AD and serves as the political, economic, and cultural center.",
                certainty="high"
            )

        With uncertainty::

            qa = QuestionAnswer(
                question="Will it rain tomorrow?",
                answer="Likely, with 70% probability",
                reasoning="Weather models show approaching low-pressure system with high humidity",
                certainty="medium"
            )
    """

    question: str = Field(
        description="The original question being answered, restated clearly",
        min_length=5,
        max_length=500,
        examples=[
            "What is the capital of France?",
            "How does photosynthesis work?",
            "What are the benefits of exercise?",
        ],
    )

    answer: str = Field(
        description="Direct, concise answer to the question",
        min_length=1,
        max_length=1000,
        examples=[
            "Paris",
            "Photosynthesis converts sunlight, CO2, and water into glucose and oxygen",
            "Exercise improves cardiovascular health, strength, and mental well-being",
        ],
    )

    reasoning: str = Field(
        description="Brief explanation of logic or evidence supporting the answer",
        min_length=10,
        max_length=2000,
        examples=[
            "Paris has been France's capital since 987 AD and serves as the political center",
            "This process occurs in chloroplasts using chlorophyll to capture light energy",
            "Scientific studies consistently show these benefits across age groups",
        ],
    )

    certainty: str = Field(
        description="Level of certainty in the answer: 'high', 'medium', or 'low'",
        pattern="^(high|medium|low)$",
        examples=["high", "medium", "low"],
    )

    @field_validator("certainty")
    @classmethod
    def validate_certainty(cls, v: str) -> str:
        """Validate certainty level is one of the allowed values.

        Args:
            v: Certainty level string

        Returns:
            Validated certainty level

        Raises:
            ValueError: If certainty level is not valid
        """
        allowed = {"high", "medium", "low"}
        v_lower = v.lower().strip()
        if v_lower not in allowed:
            raise ValueError(f"Certainty must be one of: {', '.join(allowed)}")
        return v_lower


class ProgrammingAdvice(BaseModel):
    """Structured programming advice and guidance model.

    This model provides comprehensive programming guidance including language-specific
    information, conceptual explanations, practical examples, and best practices.
    Designed for educational content, code reviews, and technical documentation.

    Attributes:
        language: Programming language being discussed (e.g., 'Python', 'JavaScript').
        topic: Specific programming concept or topic being addressed.
        explanation: Clear, educational explanation of the concept suitable for
            the target audience level.
        example_code: Practical, executable code example demonstrating the concept.
            Should be complete and runnable when possible.
        best_practices: List of actionable best practices and recommendations
            related to the topic.

    Examples:
        Python concept explanation::

            advice = ProgrammingAdvice(
                language="Python",
                topic="List Comprehensions",
                explanation="List comprehensions provide a concise way to create lists based on existing iterables with optional filtering and transformation.",
                example_code="squares = [x**2 for x in range(10) if x % 2 == 0]",
                best_practices=[
                    "Use list comprehensions for simple transformations",
                    "Avoid complex nested comprehensions",
                    "Consider generator expressions for large datasets"
                ]
            )
    """

    language: str = Field(
        description="Programming language name (e.g., 'Python', 'JavaScript', 'Java')",
        min_length=1,
        max_length=50,
        examples=["Python", "JavaScript", "Java", "C++", "Go", "Rust"],
    )

    topic: str = Field(
        description="Specific programming concept or topic being addressed",
        min_length=3,
        max_length=100,
        examples=[
            "List Comprehensions",
            "Async/Await Patterns",
            "Memory Management",
            "Error Handling",
            "Design Patterns",
        ],
    )

    explanation: str = Field(
        description="Clear, educational explanation of the concept",
        min_length=50,
        max_length=2000,
        examples=[
            "List comprehensions provide a concise way to create lists with optional filtering",
            "Async/await enables non-blocking operations for better performance",
            "Proper memory management prevents leaks and improves application stability",
        ],
    )

    example_code: str = Field(
        description="Practical, executable code example demonstrating the concept",
        min_length=10,
        max_length=1500,
        examples=[
            "squares = [x**2 for x in range(10)]",
            "async def fetch_data(): return await api_call()",
            "with open('file.txt', 'r') as f: content = f.read()",
        ],
    )

    best_practices: List[str] = Field(
        description="List of actionable best practices and recommendations",
        min_items=1,
        max_items=10,
        examples=[
            [
                "Use meaningful variable names",
                "Write docstrings",
                "Handle exceptions properly",
            ],
            ["Validate input parameters", "Use type hints", "Follow PEP 8 style guide"],
            [
                "Write unit tests",
                "Use version control",
                "Keep functions small and focused",
            ],
        ],
    )

    @field_validator("language")
    @classmethod
    def validate_language(cls, v: str) -> str:
        """Validate and normalize programming language name.

        Args:
            v: Programming language name

        Returns:
            Normalized language name with proper capitalization
        """
        v = v.strip()
        if not v:
            raise ValueError("Programming language cannot be empty")

        # Common language name normalizations
        language_map = {
            "python": "Python",
            "javascript": "JavaScript",
            "js": "JavaScript",
            "java": "Java",
            "c++": "C++",
            "cpp": "C++",
            "csharp": "C#",
            "c#": "C#",
            "golang": "Go",
            "go": "Go",
            "rust": "Rust",
            "typescript": "TypeScript",
            "ts": "TypeScript",
        }

        return language_map.get(v.lower(), v.title())

    @field_validator("best_practices")
    @classmethod
    def validate_best_practices(cls, v: List[str]) -> List[str]:
        """Validate best practices list contains meaningful content.

        Args:
            v: List of best practice strings

        Returns:
            Validated list of best practices

        Raises:
            ValueError: If practices are empty or invalid
        """
        if not v:
            raise ValueError("At least one best practice is required")

        cleaned_practices = []
        for i, practice in enumerate(v):
            if not practice or not practice.strip():
                raise ValueError(f"Best practice {i+1} cannot be empty")
            if len(practice.strip()) < 10:
                raise ValueError(f"Best practice {i+1} must be at least 10 characters")
            if len(practice.strip()) > 200:
                raise ValueError(f"Best practice {i+1} must be 200 characters or less")
            cleaned_practices.append(practice.strip())

        return cleaned_practices


class ExecutionSummary(BaseModel):
    """Summary of structured output execution and results.

    This model captures metadata about structured output execution including
    performance metrics, validation results, and execution context. Useful
    for monitoring, debugging, and optimization of structured output systems.

    Attributes:
        model_name: Name of the Pydantic model used for structured output.
        execution_time_ms: Total execution time in milliseconds from request
            to structured response generation.
        token_usage: Dictionary containing token consumption metrics including
            input tokens, output tokens, and total tokens used.
        validation_passed: Boolean indicating whether the generated output
            passed Pydantic model validation without errors.
        llm_provider: Name of the LLM provider used (e.g., 'deepseek', 'openai').
        temperature: Temperature setting used for generation (0.0-2.0).
        error_details: Optional dictionary containing error information if
            execution failed or validation errors occurred.
    """

    model_name: str = Field(
        description="Name of the Pydantic model used for structured output",
        examples=["TaskAnalysis", "QuestionAnswer", "ProgrammingAdvice"],
    )

    execution_time_ms: int = Field(
        ge=0,
        description="Total execution time in milliseconds",
        examples=[1250, 2100, 850],
    )

    token_usage: Dict[str, int] = Field(
        description="Token consumption metrics",
        examples=[
            {"input_tokens": 150, "output_tokens": 85, "total_tokens": 235},
            {"input_tokens": 300, "output_tokens": 120, "total_tokens": 420},
        ],
    )

    validation_passed: bool = Field(
        description="Whether generated output passed Pydantic validation",
        examples=[True, False],
    )

    llm_provider: str = Field(
        description="LLM provider used for generation",
        examples=["deepseek", "openai", "anthropic", "azure"],
    )

    temperature: float = Field(
        ge=0.0,
        le=2.0,
        description="Temperature setting used for generation",
        examples=[0.1, 0.7, 1.0],
    )

    error_details: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Error information if execution failed",
        examples=[
            None,
            {
                "error_type": "ValidationError",
                "message": "Field 'complexity' must be between 1 and 10",
            },
        ],
    )


# ============================================================================
# STRUCTURED OUTPUT UTILITY FUNCTIONS
# ============================================================================


def create_structured_output_agent(
    name: str,
    structured_output_model: type[BaseModel],
    temperature: float = 0.2,
    max_tokens: int = 500,
    llm_provider: str = "deepseek",
    debug: bool = False,
    **engine_kwargs,
) -> SimpleAgentV3:
    """Create a SimpleAgentV3 configured for structured output.

    This utility function simplifies the creation of SimpleAgentV3 instances
    optimized for structured output generation. It handles engine configuration,
    temperature settings, and debug options automatically.

    Args:
        name: Unique identifier for the agent instance.
        structured_output_model: Pydantic model class to use for output structure.
        temperature: LLM temperature setting (0.0=deterministic, 2.0=creative).
            Lower values (0.1-0.3) recommended for structured output consistency.
        max_tokens: Maximum tokens for response generation. Should be sized
            appropriately for the expected output model complexity.
        llm_provider: LLM provider to use ('deepseek', 'openai', 'azure').
        debug: Enable debug logging and detailed execution traces.
        **engine_kwargs: Additional arguments passed to AugLLMConfig.

    Returns:
        SimpleAgentV3: Configured agent ready for structured output generation.

    Raises:
        ValueError: If structured_output_model is not a valid Pydantic model.
        ImportError: If specified LLM provider is not available.

    Examples:
        Create task analysis agent::

            agent = create_structured_output_agent(
                name="task_analyzer",
                structured_output_model=TaskAnalysis,
                temperature=0.1,
                max_tokens=400
            )

            result = agent.run("Analyze building a mobile app")
            # Returns TaskAnalysis instance

        Create Q&A agent with debug::

            qa_agent = create_structured_output_agent(
                name="qa_bot",
                structured_output_model=QuestionAnswer,
                temperature=0.2,
                debug=True
            )

            answer = qa_agent.run("What is machine learning?")
            # Returns QuestionAnswer with detailed debug logs

    Note:
        The created agent uses LLMState for token tracking and state management.
        Structured output models are automatically converted to LangChain tools
        and bound to the LLM for consistent schema enforcement.
    """
    # Validate structured output model
    if not (
        isinstance(structured_output_model, type)
        and issubclass(structured_output_model, BaseModel)
    ):
        raise ValueError(
            f"structured_output_model must be a Pydantic BaseModel class, "
            f"got {type(structured_output_model)}"
        )

    # Configure LLM provider
    llm_configs = {
        "deepseek": DeepSeekLLMConfig,
        # Add other providers as needed
    }

    if llm_provider not in llm_configs:
        raise ValueError(f"Unsupported LLM provider: {llm_provider}")

    llm_config_class = llm_configs[llm_provider]

    # Create engine configuration
    engine_config = AugLLMConfig(
        structured_output_model=structured_output_model,
        temperature=temperature,
        max_tokens=max_tokens,
        llm_config=llm_config_class(),
        **engine_kwargs,
    )

    # Create and return agent
    agent = SimpleAgentV3(name=name, engine=engine_config, debug=debug)

    if debug:
        logger.info(
            f"Created structured output agent '{name}' with model "
            f"{structured_output_model.__name__} (temp={temperature}, "
            f"max_tokens={max_tokens}, provider={llm_provider})"
        )

    return agent


def validate_structured_output(
    output: Any, expected_model: type[BaseModel], strict: bool = True
) -> tuple[bool, Optional[str], Optional[BaseModel]]:
    """Validate output against expected Pydantic model.

    This function validates that generated output conforms to the expected
    Pydantic model structure, providing detailed validation results and
    error information for debugging and quality assurance.

    Args:
        output: Output to validate (can be dict, JSON string, or model instance).
        expected_model: Expected Pydantic model class for validation.
        strict: If True, require exact model match. If False, allow
            compatible structures that can be converted to the model.

    Returns:
        tuple: Three-element tuple containing:
            - bool: Whether validation passed
            - Optional[str]: Error message if validation failed, None if passed
            - Optional[BaseModel]: Validated model instance if successful, None if failed

    Examples:
        Validate dictionary output::

            output_dict = {
                "task_type": "development",
                "complexity": 7,
                "steps_required": ["Plan", "Code", "Test"],
                "estimated_time": 480,
                "confidence": 0.8
            }

            is_valid, error, model = validate_structured_output(
                output_dict, TaskAnalysis
            )

            if is_valid:
                print(f"Valid TaskAnalysis: {model.task_type}")
            else:
                print(f"Validation error: {error}")

        Validate JSON string::

            json_output = '{"question": "What is AI?", "answer": "Artificial Intelligence", "reasoning": "...", "certainty": "high"}'

            is_valid, error, model = validate_structured_output(
                json_output, QuestionAnswer
            )
    """
    try:
        # Handle different input types
        if isinstance(output, str):
            # Try to parse as JSON
            import json

            try:
                output = json.loads(output)
            except json.JSONDecodeError as e:
                return False, f"Invalid JSON: {str(e)}", None

        elif isinstance(output, expected_model):
            # Already correct model type
            return True, None, output

        # Validate against model
        if isinstance(output, dict):
            try:
                validated_model = expected_model(**output)
                return True, None, validated_model
            except Exception as e:
                return False, f"Model validation failed: {str(e)}", None
        else:
            return False, f"Unsupported output type: {type(output)}", None

    except Exception as e:
        return False, f"Validation error: {str(e)}", None


def extract_structured_output_from_messages(
    messages: List[Any], expected_model: type[BaseModel]
) -> tuple[bool, Optional[BaseModel], Optional[str]]:
    """Extract and validate structured output from agent message history.

    This function searches through agent message history to find structured
    output content, typically from tool calls or direct model responses,
    and validates it against the expected Pydantic model.

    Args:
        messages: List of messages from agent execution (typically from state.messages).
        expected_model: Expected Pydantic model class for the structured output.

    Returns:
        tuple: Three-element tuple containing:
            - bool: Whether structured output was found and validated
            - Optional[BaseModel]: Validated model instance if found, None otherwise
            - Optional[str]: Error message if validation failed or output not found

    Examples:
        Extract from agent execution::

            agent = create_structured_output_agent("analyzer", TaskAnalysis)
            result = agent.run("Analyze building a website")

            found, model, error = extract_structured_output_from_messages(
                result.messages, TaskAnalysis
            )

            if found:
                print(f"Task complexity: {model.complexity}")
                print(f"Steps: {len(model.steps_required)}")
            else:
                print(f"Extraction failed: {error}")
    """
    try:
        # Look through messages for AI responses with tool calls
        for message in reversed(messages):  # Start from most recent
            if hasattr(message, "tool_calls") and message.tool_calls:
                for tool_call in message.tool_calls:
                    if hasattr(tool_call, "args") and tool_call.args:
                        # Try to validate tool call arguments
                        is_valid, error, model = validate_structured_output(
                            tool_call.args, expected_model
                        )
                        if is_valid:
                            return True, model, None

            # Also check message content for JSON
            if hasattr(message, "content") and message.content:
                content = message.content.strip()
                if content.startswith("{") and content.endswith("}"):
                    is_valid, error, model = validate_structured_output(
                        content, expected_model
                    )
                    if is_valid:
                        return True, model, None

        return (
            False,
            None,
            f"No structured output found matching {expected_model.__name__}",
        )

    except Exception as e:
        return False, None, f"Extraction error: {str(e)}"


# ============================================================================
# USAGE EXAMPLES AND DEMONSTRATIONS
# ============================================================================


def demonstrate_task_analysis():
    """Demonstrate TaskAnalysis structured output with real execution.

    This function shows how to use SimpleAgentV3 with the TaskAnalysis model
    for project planning and task breakdown scenarios.

    Returns:
        TaskAnalysis: Validated task analysis result

    Examples:
        Run task analysis demonstration::

            analysis = demonstrate_task_analysis()
            print(f"Task: {analysis.task_type}")
            print(f"Complexity: {analysis.complexity}/10")
            print(f"Time estimate: {analysis.estimated_time} minutes")
            for i, step in enumerate(analysis.steps_required, 1):
                print(f"{i}. {step}")
    """
    print("🔍 Demonstrating TaskAnalysis Structured Output")
    print("=" * 60)

    # Create agent with TaskAnalysis model
    agent = create_structured_output_agent(
        name="task_analyzer_demo",
        structured_output_model=TaskAnalysis,
        temperature=0.2,
        max_tokens=400,
    )

    # Example task to analyze
    task_query = """
    Analyze this task: Create a real-time chat application that supports 
    multiple rooms, user authentication, message history, and file sharing.
    The application should be web-based and handle up to 1000 concurrent users.
    """

    print(f"📝 Task Query: {task_query.strip()}")
    print("\n🤖 Generating structured analysis...")

    # Execute with structured output
    result = agent.run(task_query.strip())

    # Extract and validate structured output
    found, analysis, error = extract_structured_output_from_messages(
        result.messages, TaskAnalysis
    )

    if found and analysis:
        print("\n✅ TaskAnalysis Results:")
        print(f"   Task Type: {analysis.task_type}")
        print(f"   Complexity: {analysis.complexity}/10")
        print(
            f"   Estimated Time: {analysis.estimated_time} minutes ({analysis.estimated_time/60:.1f} hours)"
        )
        print(f"   Confidence: {analysis.confidence:.2f}")
        print(f"\n📋 Required Steps ({len(analysis.steps_required)}):")
        for i, step in enumerate(analysis.steps_required, 1):
            print(f"   {i}. {step}")

        return analysis
    else:
        print(f"\n❌ Failed to extract structured output: {error}")
        return None


def demonstrate_question_answer():
    """Demonstrate QuestionAnswer structured output with real execution.

    This function shows how to use SimpleAgentV3 with the QuestionAnswer model
    for Q&A systems and knowledge retrieval scenarios.

    Returns:
        QuestionAnswer: Validated question-answer result
    """
    print("\n❓ Demonstrating QuestionAnswer Structured Output")
    print("=" * 60)

    # Create Q&A agent
    agent = create_structured_output_agent(
        name="qa_demo_agent",
        structured_output_model=QuestionAnswer,
        temperature=0.3,
        max_tokens=300,
    )

    question = "What are the key benefits of using Pydantic for data validation in Python applications?"

    print(f"❓ Question: {question}")
    print("\n🤖 Generating structured answer...")

    # Execute Q&A
    result = agent.run(question)

    # Extract structured output
    found, qa_result, error = extract_structured_output_from_messages(
        result.messages, QuestionAnswer
    )

    if found and qa_result:
        print("\n✅ QuestionAnswer Results:")
        print(f"   Question: {qa_result.question}")
        print(f"   Answer: {qa_result.answer}")
        print(f"   Reasoning: {qa_result.reasoning}")
        print(f"   Certainty: {qa_result.certainty}")

        return qa_result
    else:
        print(f"\n❌ Failed to extract Q&A output: {error}")
        return None


def demonstrate_programming_advice():
    """Demonstrate ProgrammingAdvice structured output with real execution.

    This function shows how to use SimpleAgentV3 with the ProgrammingAdvice model
    for educational content and technical guidance scenarios.

    Returns:
        ProgrammingAdvice: Validated programming advice result
    """
    print("\n💻 Demonstrating ProgrammingAdvice Structured Output")
    print("=" * 60)

    # Create programming advice agent
    agent = create_structured_output_agent(
        name="programming_tutor",
        structured_output_model=ProgrammingAdvice,
        temperature=0.4,
        max_tokens=500,
    )

    coding_question = (
        "Explain Python decorators with a practical example and best practices"
    )

    print(f"💡 Coding Question: {coding_question}")
    print("\n🤖 Generating structured programming advice...")

    # Execute programming guidance
    result = agent.run(coding_question)

    # Extract structured output
    found, advice, error = extract_structured_output_from_messages(
        result.messages, ProgrammingAdvice
    )

    if found and advice:
        print("\n✅ ProgrammingAdvice Results:")
        print(f"   Language: {advice.language}")
        print(f"   Topic: {advice.topic}")
        print(f"   Explanation: {advice.explanation}")
        print("\n📝 Example Code:"e:")
        print(f"   {advice.example_code}")
        print(f"\n⭐ Best Practices ({len(advice.best_practices)}):")
        for i, practice in enumerate(advice.best_practices, 1):
            print(f"   {i}. {practice}")

        return advice
    else:
        print(f"\n❌ Failed to extract programming advice: {error}")
        return None


def run_all_demonstrations():
    """Run all structured output demonstrations.

    This function executes all the demonstration functions to show the
    complete range of structured output capabilities with SimpleAgentV3.

    Examples:
        Run complete demonstration suite::

            results = run_all_demonstrations()

            # Access individual results
            task_analysis = results.get('task_analysis')
            qa_result = results.get('question_answer')
            programming_advice = results.get('programming_advice')

    Returns:
        dict: Dictionary containing all demonstration results with keys:
            'task_analysis', 'question_answer', 'programming_advice'
    """
    print("🎯 SIMPLEAGENT V3 STRUCTURED OUTPUT DEMONSTRATIONS")
    print("=" * 70)
    print("Running comprehensive structured output examples with real LLM execution")
    print("=" * 70)

    results = {}

    try:
        # Run TaskAnalysis demonstration
        results["task_analysis"] = demonstrate_task_analysis()

        # Run QuestionAnswer demonstration
        results["question_answer"] = demonstrate_question_answer()

        # Run ProgrammingAdvice demonstration
        results["programming_advice"] = demonstrate_programming_advice()

        # Summary
        successful_demos = sum(1 for result in results.values() if result is not None)
        total_demos = len(results)

        print("\n🎉 DEMONSTRATION SUMMARY"RY")
        print("=" * 40)
        print(f"Successful demonstrations: {successful_demos}/{total_demos}")

        if successful_demos == total_demos:
            print("✅ All structured output models working correctly!")
            print("\n🔧 Validated Features:")
            print("   • TaskAnalysis for project planning")
            print("   • QuestionAnswer for Q&A systems")
            print("   • ProgrammingAdvice for educational content")
            print("   • Real LLM execution with token tracking")
            print("   • Pydantic validation and error handling")
            print("   • Tool-based structured output generation")
        else:
            print("⚠️  Some demonstrations failed - check output above")

        return results

    except Exception as e:
        print(f"\n❌ Demonstration execution failed: {e}")
        logger.exception("Structured output demonstration error")
        return {}


if __name__ == "__main__":
    # Run demonstrations when executed directly
    demonstration_results = run_all_demonstrations()
