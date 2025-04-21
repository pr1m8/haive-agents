# src/haive/agents/selfdiscover/agent.py

import json
import logging
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END
from langgraph.types import Command
from pydantic import BaseModel

from haive.agents.self_discover.config import SelfDiscoverAgentConfig
from haive.agents.self_discover.models import (
    ModuleAdaptationResult,
    ModuleSelectionResult,
    ReasoningOutput,
    ReasoningStructure,
)
from haive.agents.self_discover.state import SelfDiscoverState
from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph

# Set up logging
logger = logging.getLogger(__name__)

@register_agent(SelfDiscoverAgentConfig)
class SelfDiscoverAgent(Agent[SelfDiscoverAgentConfig]):
    """An agent that implements the SelfDiscover methodology with structured output models.
    
    This agent follows a four-stage approach:
    1. Select appropriate reasoning modules for the task
    2. Adapt the modules to better fit the task
    3. Structure the reasoning into a step-by-step plan
    4. Execute the plan to solve the task
    
    Each stage uses a dedicated LLM with structured output models to ensure
    consistent, high-quality reasoning.
    """
    def setup_workflow(self) -> None:
        """Set up the workflow graph for the SelfDiscover agent."""
        # Create a builder with our schema
        gb = DynamicGraph(state_schema=self.state_schema)

        # Define node functions for each stage
        def select_modules(state: SelfDiscoverState) -> Command:
            """Select appropriate reasoning modules for the task."""
            try:
                # Prepare inputs
                inputs = {
                    "reasoning_modules": state.reasoning_modules,
                    "task_description": state.task_description
                }

                # Create runnable from AugLLMConfig and invoke it
                select_runnable = self.config.select_engine.create_runnable()
                result = select_runnable.invoke(inputs)

                # The result should be a ModuleSelectionResult object
                if isinstance(result, ModuleSelectionResult):
                    # Format the result for the next stage
                    formatted_result = result.format_for_next_stage()

                    # Store both the structured object and formatted string
                    metadata = state.metadata.copy()
                    metadata["selection_result"] = result.model_dump()

                    # Return command with updated state
                    return Command(
                        update={
                            "selected_modules": formatted_result,
                            "metadata": metadata
                        },
                        goto="adapt"
                    )
                # Fall back to string representation
                selected_modules = self._extract_string_result(result)
                return Command(
                    update={"selected_modules": selected_modules},
                    goto="adapt"
                )

            except Exception as e:
                logger.error(f"Error in select_modules: {e!s}")
                return Command(
                    update={"error": f"Error in module selection: {e!s}"},
                    goto=END
                )

        def adapt_modules(state: SelfDiscoverState) -> Command:
            """Adapt the selected modules for the specific task."""
            try:
                # Check if we have selected modules
                if not state.selected_modules:
                    return Command(
                        update={"error": "No modules selected for adaptation"},
                        goto=END
                    )

                # Prepare inputs
                inputs = {
                    "selected_modules": state.selected_modules,
                    "task_description": state.task_description
                }

                # Create runnable from AugLLMConfig and invoke it
                adapt_runnable = self.config.adapt_engine.create_runnable()
                result = adapt_runnable.invoke(inputs)

                # The result should be a ModuleAdaptationResult object
                if isinstance(result, ModuleAdaptationResult):
                    # Format the result for the next stage
                    formatted_result = result.format_for_next_stage()

                    # Store both the structured object and formatted string
                    metadata = state.metadata.copy()
                    metadata["adaptation_result"] = result.model_dump()

                    # Return command with updated state
                    return Command(
                        update={
                            "adapted_modules": formatted_result,
                            "metadata": metadata
                        },
                        goto="structure"
                    )
                # Fall back to string representation
                adapted_modules = self._extract_string_result(result)
                return Command(
                    update={"adapted_modules": adapted_modules},
                    goto="structure"
                )

            except Exception as e:
                logger.error(f"Error in adapt_modules: {e!s}")
                return Command(
                    update={"error": f"Error in module adaptation: {e!s}"},
                    goto=END
                )

        def create_structure(state: SelfDiscoverState) -> Command:
            """Create a structured reasoning plan."""
            try:
                # Check if we have adapted modules
                if not state.adapted_modules:
                    return Command(
                        update={"error": "No adapted modules for structure creation"},
                        goto=END
                    )

                # Prepare inputs
                inputs = {
                    "adapted_modules": state.adapted_modules,
                    "task_description": state.task_description
                }

                # Create runnable from AugLLMConfig and invoke it
                structure_runnable = self.config.structure_engine.create_runnable()
                result = structure_runnable.invoke(inputs)

                # The result should be a ReasoningStructure object
                if isinstance(result, ReasoningStructure):
                    # Format the result for the next stage
                    formatted_result = result.format_for_next_stage()

                    # Store both the structured object and formatted string
                    metadata = state.metadata.copy()
                    metadata["structure_result"] = result.model_dump()

                    # Return command with updated state
                    return Command(
                        update={
                            "reasoning_structure": formatted_result,
                            "metadata": metadata
                        },
                        goto="reason"
                    )
                # Fall back to string representation
                reasoning_structure = self._extract_string_result(result)
                return Command(
                    update={"reasoning_structure": reasoning_structure},
                    goto="reason"
                )

            except Exception as e:
                logger.error(f"Error in create_structure: {e!s}")
                return Command(
                    update={"error": f"Error in structure creation: {e!s}"},
                    goto=END
                )

        def execute_reasoning(state: SelfDiscoverState) -> Command:
            """Execute the reasoning plan to solve the task."""
            try:
                # Check if we have a reasoning structure
                if not state.reasoning_structure:
                    return Command(
                        update={"error": "No reasoning structure for execution"},
                        goto=END
                    )

                # Prepare inputs
                inputs = {
                    "reasoning_structure": state.reasoning_structure,
                    "task_description": state.task_description
                }

                # Create runnable from AugLLMConfig and invoke it
                reasoning_runnable = self.config.reasoning_engine.create_runnable()
                result = reasoning_runnable.invoke(inputs)

                # The result should be a ReasoningOutput object
                if isinstance(result, ReasoningOutput):
                    # Format the result for the final answer
                    formatted_result = result.format_complete_reasoning()

                    # Store both the structured object and formatted string
                    metadata = state.metadata.copy()
                    metadata["reasoning_result"] = result.model_dump()

                    # Prepare update with answer and metadata
                    update = {
                        "answer": result.final_answer,
                        "metadata": metadata
                    }

                    # Also add as message if we have messages
                    if hasattr(state, "messages") and state.messages is not None:
                        messages = list(state.messages)
                        messages.append(AIMessage(content=formatted_result))
                        update["messages"] = messages

                    # Return command with updated state
                    return Command(update=update, goto=END)
                # Fall back to string representation
                answer = self._extract_string_result(result)

                # Prepare update with answer
                update = {"answer": answer}

                # Also add as message if we have messages
                if hasattr(state, "messages") and state.messages is not None:
                    messages = list(state.messages)
                    messages.append(AIMessage(content=answer))
                    update["messages"] = messages

                # Return command with updated state
                return Command(update=update, goto=END)

            except Exception as e:
                logger.error(f"Error in execute_reasoning: {e!s}")
                error_msg = f"Error in reasoning execution: {e!s}"

                # Prepare update with error
                update = {"error": error_msg}

                # Also add error as message if we have messages
                if hasattr(state, "messages") and state.messages is not None:
                    messages = list(state.messages)
                    messages.append(AIMessage(content=f"Error: {error_msg}"))
                    update["messages"] = messages

                # Return command with updated state
                return Command(update=update, goto=END)

        # Add nodes to the graph
        gb.add_node("select", select_modules)
        gb.add_node("adapt", adapt_modules)
        gb.add_node("structure", create_structure)
        gb.add_node("reason", execute_reasoning)

        # Set entry point and build graph
        gb.set_entry_point("select")
        self.graph = gb.build()

        # Compile the graph
        self.app = self.graph.compile(checkpointer=self.memory)

        logger.info(f"Set up SelfDiscover workflow for {self.config.name}")

    def _extract_string_result(self, result: Any) -> str:
        """Extract a string result from the engine output regardless of type."""
        if isinstance(result, str):
            return result
        if hasattr(result, "content"):
            return result.content
        if hasattr(result, "final_answer"):
            return result.final_answer
        if isinstance(result, dict):
            if "text" in result:
                return result["text"]
            if "output" in result:
                return result["output"]
            if "content" in result:
                return result["content"]
            if "final_answer" in result:
                return result["final_answer"]
            # Try to serialize the whole dict as a fallback
            try:
                return json.dumps(result)
            except:
                return str(result)
        else:
            return str(result)

    def _prepare_input(self, input_data: str | list[str] | dict[str, Any] | BaseModel) -> Any:
        """Prepare input for the SelfDiscover agent.
        Overrides the base method to handle SelfDiscover-specific input preparation.
        """
        # Store reasoning modules as a formatted string
        reasoning_modules_str = "\n".join(self.config.reasoning_modules)

        if isinstance(input_data, str):
            # Single string to task description
            return self.state_schema(
                messages=[HumanMessage(content=input_data)],
                task_description=input_data,
                reasoning_modules=reasoning_modules_str
            )
        if isinstance(input_data, list) and all(isinstance(item, str) for item in input_data):
            # List of strings - join for task description
            combined_text = "\n".join(input_data)
            return self.state_schema(
                messages=[HumanMessage(content=item) for item in input_data],
                task_description=combined_text,
                reasoning_modules=reasoning_modules_str
            )
        if isinstance(input_data, dict):
            # Dictionary input - ensure required fields
            input_dict = dict(input_data)

            # Set reasoning modules if not provided
            if "reasoning_modules" not in input_dict:
                input_dict["reasoning_modules"] = reasoning_modules_str

            # Convert input or text to task_description if needed
            if "task_description" not in input_dict:
                if "input" in input_dict:
                    input_dict["task_description"] = input_dict["input"]
                elif "text" in input_dict:
                    input_dict["task_description"] = input_dict["text"]
                elif input_dict.get("messages"):
                    # Extract text from messages
                    messages = input_dict["messages"]
                    input_dict["task_description"] = "\n".join([
                        m.content if hasattr(m, "content") else str(m)
                        for m in messages
                    ])

            # Ensure messages exist
            if "messages" not in input_dict:
                input_dict["messages"] = [HumanMessage(content=input_dict.get("task_description", ""))]

            return self.state_schema(**input_dict)
        if isinstance(input_data, BaseModel):
            # Convert BaseModel to dict and process
            data = input_data.model_dump() if hasattr(input_data, "model_dump") else input_data.dict()
            return self._prepare_input(data)
        raise ValueError(f"Invalid input type: {type(input_data)}")

    def run(self, input_data: str | list[str] | dict[str, Any] | BaseModel, **kwargs) -> dict[str, Any]:
        """Run the SelfDiscover agent with the given input."""
        # Use parent implementation
        result = super().run(input_data, **kwargs)

        # Log key outputs for debugging
        if self.config.debug:
            if "selected_modules" in result:
                logger.debug(f"Selected modules: {result['selected_modules'][:200]}...")
            if "adapted_modules" in result:
                logger.debug(f"Adapted modules: {result['adapted_modules'][:200]}...")
            if "reasoning_structure" in result:
                logger.debug(f"Reasoning structure: {result['reasoning_structure'][:200]}...")
            if "answer" in result:
                logger.debug(f"Answer: {result['answer'][:200]}...")
            if "metadata" in result:
                logger.debug(f"Metadata keys: {list(result['metadata'].keys())}")

        return result


# Helper Functions
def create_self_discover_agent(
    model: str = "gpt-4o",
    temperature: float = 0.0,
    name: str | None = None,
    reasoning_modules: list[str] | None = None,
    select_prompt: str | ChatPromptTemplate | None = None,
    adapt_prompt: str | ChatPromptTemplate | None = None,
    structure_prompt: str | ChatPromptTemplate | None = None,
    reasoning_prompt: str | ChatPromptTemplate | None = None,
    visualize: bool = True,
    **kwargs
) -> SelfDiscoverAgent:
    """Create a SelfDiscover agent with customizable parameters.
    
    Args:
        model: Model name to use
        temperature: Temperature for generation
        name: Optional name for the agent
        reasoning_modules: List of reasoning modules to use
        select_prompt: Custom prompt for the selection stage
        adapt_prompt: Custom prompt for the adaptation stage
        structure_prompt: Custom prompt for the structure stage
        reasoning_prompt: Custom prompt for the reasoning stage
        visualize: Whether to visualize the graph
        **kwargs: Additional configuration parameters
        
    Returns:
        SelfDiscoverAgent instance
    """
    # Create config with default settings
    config = SelfDiscoverAgentConfig.from_defaults(
        model=model,
        temperature=temperature,
        name=name,
        reasoning_modules=reasoning_modules,
        select_prompt=select_prompt,
        adapt_prompt=adapt_prompt,
        structure_prompt=structure_prompt,
        reasoning_prompt=reasoning_prompt,
        visualize=visualize,
        **kwargs
    )

    # Build and return the agent
    return config.build_agent()
