"""
ReWOO Agent Implementation

This file contains the implementation of the Reasoning Without Observation agent.
"""

# Import directly from base, not from plan_and_execute to avoid circular imports
from haive.core.engine.agent.agent import AgentArchitecture
haive.core.engine.aug_llm import compose_runnable
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command

import json
import traceback
from typing import Dict, Any, Optional, List, Union


from agents.rewoo.state import ReWOOState
from agents.rewoo.models import RewooPlan, RewooStep, ToolCall
"""
Configuration for the ReWOO agent.
"""

import uuid
from typing import List, Type
from pydantic import BaseModel, Field, model_validator
from langchain_core.tools import BaseTool
from langchain_core.runnables import RunnableConfig

from haive.core.engine.agent.agent import AgentArchitectureConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.utils.tool_utils import _format_tool_descriptions
from haive.core.tools.search_tools import tavily_search_tool, tavily_search_context, tavily_qna, tavily_extract

from agents.rewoo.state import ReWOOState
from agents.rewoo.models import ToolCall
from agents.rewoo.aug_llms import rewoo_aug_llm_config, solve_aug_llm_config

class RewooAgentConfig(AgentArchitectureConfig):
    """
    Configuration for the ReWOO Agent with automatic prompt formatting.
    
    This configuration extends the base AgentArchitectureConfig by adding:
    - Separate planner and solver LLM configurations
    - Tool registration for validation
    - Automatic prompt formatting with tool descriptions
    """
    planner: AugLLMConfig = Field(
        default=rewoo_aug_llm_config, 
        description="The configuration for the planner LLM"
    )
    solver: AugLLMConfig = Field(
        default=solve_aug_llm_config, 
        description="The configuration for the solver LLM"
    )
    # Store tools directly in the config, not in AugLLMConfig
    tools: List[BaseTool] = Field(
        default_factory=lambda: [tavily_search_tool, tavily_search_context, tavily_qna, tavily_extract],
        description="The tools available for the agent"
    )
    state_schema: Type[BaseModel] = Field(
        default=ReWOOState, 
        description="The state schema for the agent"
    )
    runnable_config: RunnableConfig = Field(
        default={"configurable": {"thread_id": str(uuid.uuid4())}},
        description="The runnable config for the agent"
    )
    should_visualize_graph: bool = Field(
        default=True, 
        description="Enable graph visualization"
    )
    visualize_graph_output_name: str = Field(
        default="rewoo_graph.png", 
        description="Graph output file name"
    )
    
    @model_validator(mode="after")
    def validate_and_register_tools(cls, values):
        """
        Ensure tools are registered for validation.
        
        This validator:
        1. Checks that tools are provided
        2. Registers the tools with the ToolCall model for validation
        
        Args:
            values: Configuration values
            
        Returns:
            Validated configuration values
        """
        tools = values.tools
        
        if not tools:
            raise ValueError("No tools provided in the configuration!")
        
        # Register tools in ToolCall for validation
        ToolCall.set_available_tools(tools)
        
        print(f"Registered Tools for Validation: {list(ToolCall.available_tools.keys())}")
        return values
    
    @model_validator(mode="after")
    def format_planning_prompt_with_tools(self):
        """
        Format the planning prompt with available tools.
        
        This ensures the planner has access to the correct tool descriptions.
        
        Returns:
            Self with updated prompt template
        """
        # Format tools for inclusion in the prompt
        formatted_tools = _format_tool_descriptions(self.tools)
        print(f"Formatted Tools: {formatted_tools}")
        
        # Update the planner prompt template with tools
        if not hasattr(self.planner, "prompt_template"):
            raise ValueError("Planner does not have a prompt_template attribute!")
        
        self.planner.prompt_template = self.planner.prompt_template.partial(
            tools=formatted_tools
        )
        
        print(f"Updated Planner Prompt Template with formatted tools")
        return self


# Default configuration
DEFAULT_CONFIG = RewooAgentConfig()
class RewooAgent(AgentArchitecture):
    """
    ReWOO (Reasoning Without Observation) Agent implementation.
    
    This agent architecture follows these steps:
    1. Planning: Create steps with evidence references and tool calls
    2. Execution: Run tools and collect evidence for each step 
    3. Solving: Use collected evidence to solve the task
    
    The key feature is the use of evidence references that allow steps
    to reference outputs from previous steps.
    """
    
    def __init__(self, config: RewooAgentConfig = None):
        """
        Initialize the ReWOO agent with the given configuration.
        
        Args:
            config: Configuration for the agent
        """
        # Use default config if none provided
        if config is None:
            #from haive_agents.rewoo.config import DEFAULT_CONFIG
            config = RewooAgentConfig()
            
        # Call parent constructor
        super().__init__(config)
        
        # Store configuration and tools
        self.config = config
        self.tools = config.tools
        
        # Create model instances
        self.llm = config.planner.llm_config.instantiate()
        self.planner = compose_runnable(config.planner)
        self.solver = compose_runnable(config.solver)
        
        # Register tools in ToolCall for validation
        ToolCall.set_available_tools(self.tools)
    
    def plan(self, state: ReWOOState) -> Command:
        """
        Generate a plan with evidence references for the given task.
        
        Args:
            state: The current state
            
        Returns:
            Command to update the state
        """
        try:
            # Invoke the planner with the task
            planner_result = self.planner.invoke({"task": state.task})
            
            # Parse the result into a RewooPlan
            if isinstance(planner_result, dict) and "steps" in planner_result:
                # Extract steps directly from the result
                plan_data = planner_result
            elif isinstance(planner_result, str):
                # Try to extract JSON from string result
                try:
                    # Find JSON in the string
                    json_str = self._extract_json(planner_result)
                    plan_data = json.loads(json_str)
                except Exception as e:
                    print(f"Error parsing JSON from planner result: {e}")
                    # Create a fallback plan
                    plan_data = self._create_fallback_plan(state.task)
            else:
                # Create a fallback plan if result format is unexpected
                plan_data = self._create_fallback_plan(state.task)
            
            # Create the RewooPlan with RewooSteps
            plan = self._create_plan_from_data(plan_data)
            
            # Update state with the plan and set current step
            return Command(update={
                "plan": plan,
                "current_step_index": 0
            })
            
        except Exception as e:
            # Handle errors during planning
            print(f"Error during planning: {e}")
            traceback.print_exc()
            
            # Create a fallback plan
            plan_data = self._create_fallback_plan(state.task)
            plan = self._create_plan_from_data(plan_data)
            
            return Command(update={
                "plan": plan,
                "current_step_index": 0
            })
    
    def _extract_json(self, text: str) -> str:
        """
        Extract JSON from text.
        
        Args:
            text: The text to extract JSON from
            
        Returns:
            Extracted JSON string
        """
        # Find the first opening brace
        start = text.find("{")
        if start == -1:
            raise ValueError("No JSON found in text")
        
        # Find the matching closing brace
        brace_count = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                brace_count += 1
            elif text[i] == "}":
                brace_count -= 1
                if brace_count == 0:
                    return text[start:i+1]
        
        # If no matching closing brace, try a simple approach
        end = text.rfind("}")
        if end > start:
            return text[start:end+1]
        
        raise ValueError("No complete JSON found in text")
    
    def _create_fallback_plan(self, task: str) -> Dict[str, Any]:
        """
        Create a fallback plan when planning fails.
        
        Args:
            task: The task to create a plan for
            
        Returns:
            Fallback plan data
        """
        return {
            "steps": [
                {
                    "step_number": 1,
                    "description": f"Search for information about: {task}",
                    "evidence_ref": "#E1",
                    "tool_calls": [
                        {
                            "name": "tavily_search",
                            "input": {"query": task}
                        }
                    ]
                },
                {
                    "step_number": 2,
                    "description": f"Analyze search results and answer the question: {task}",
                    "evidence_ref": "#E2",
                    "tool_calls": [
                        {
                            "name": "LLM",
                            "input": f"Based on the search results in #E1, answer the question: {task}"
                        }
                    ]
                }
            ]
        }
    
    def _create_plan_from_data(self, plan_data: Dict[str, Any]) -> RewooPlan:
        """
        Create a RewooPlan from parsed data.
        
        Args:
            plan_data: The parsed plan data
            
        Returns:
            RewooPlan instance
        """
        steps = []
        
        # Process each step
        for step_data in plan_data.get("steps", []):
            # Process tool calls
            tool_calls = []
            for tool_call_data in step_data.get("tool_calls", []):
                # Correct common tool name mistakes
                tool_name = tool_call_data["name"]
                
                # Map common incorrect tool names to correct ones
                tool_name_mapping = {
                    "tavily_search": "tavily_search_tool",
                    "tavily": "tavily_search_tool",
                    "search": "tavily_search_tool",
                    "search_tool": "tavily_search_tool",
                    "context": "tavily_search_context",
                    "qna": "tavily_qna",
                    "extract": "tavily_extract"
                }
                
                if tool_name in tool_name_mapping:
                    corrected_name = tool_name_mapping[tool_name]
                    print(f"Correcting tool name from '{tool_name}' to '{corrected_name}'")
                    tool_name = corrected_name
                
                tool_call = ToolCall(
                    name=tool_name,
                    input=tool_call_data["input"]
                )
                tool_calls.append(tool_call)
            
            # Create the step
            step = RewooStep(
                step_number=step_data["step_number"],
                description=step_data["description"],
                evidence_ref=step_data.get("evidence_ref", f"#E{step_data['step_number']}"),
                tool_calls=tool_calls,
                # Added status field
                status="not_started"
            )
            steps.append(step)
        
        # Create and return the plan
        return RewooPlan(steps=steps)
    
    def execute_step(self, state: ReWOOState) -> Command:
        """
        Execute the current step in the plan.
        
        Args:
            state: The current state
            
        Returns:
            Command to update the state
        """
        # Get the current step
        current_step = state.get_current_step()
        if not current_step:
            return Command(update={})
        
        print(f"Executing step {current_step.step_number}: {current_step.description}")
        
        # Initialize results for this step
        step_results = {}
        
        # Execute each tool call
        for tool_call in current_step.tool_calls:
            try:
                if tool_call.name == "LLM":
                    # Handle LLM tool call
                    result = self._execute_llm_tool(tool_call, state)
                    step_results["LLM"] = result
                else:
                    # Handle regular tool call
                    result = self._execute_tool(tool_call, state)
                    step_results[tool_call.name] = result
            except Exception as e:
                # Handle errors during execution
                error_msg = f"Error executing tool {tool_call.name}: {str(e)}"
                print(error_msg)
                traceback.print_exc()
                step_results[tool_call.name] = error_msg
        
        # Update results and advance to next step
        results = state.results if hasattr(state, 'results') else {}
        results[current_step.evidence_ref] = step_results
        
        # Mark the current step as complete
        current_step.status = "complete"
        
        # Calculate next step index
        next_step_index = state.current_step_index + 1
        if next_step_index >= len(state.plan.steps):
            next_step_index = None  # All steps complete
        
        return Command(update={
            "results": results,
            "current_step_index": next_step_index
        })
    
    def _execute_llm_tool(self, tool_call: ToolCall, state: ReWOOState) -> str:
        """
        Execute an LLM tool call.
        
        Args:
            tool_call: The tool call to execute
            state: The current state
            
        Returns:
            The result of the LLM invocation
        """
        input_text = tool_call.input
        if isinstance(input_text, str):
            # Replace evidence references with actual evidence
            for ref, evidence in state.results.items():
                if f"{ref}" in input_text:
                    # Format evidence as a string
                    evidence_str = json.dumps(evidence, indent=2)
                    input_text = input_text.replace(f"{ref}", evidence_str)
        
        print(f"Invoking LLM with input: {input_text}")
        result = self.llm.invoke(input_text)
        
        return str(result)
    
    def _execute_tool(self, tool_call: ToolCall, state: ReWOOState) -> str:
        """
        Execute a regular tool call.
        
        Args:
            tool_call: The tool call to execute
            state: The current state
            
        Returns:
            The result of the tool invocation
        """
        # Find the tool
        tool = next((t for t in self.tools if t.name == tool_call.name), None)
        if not tool:
            raise ValueError(f"Unknown tool: {tool_call.name}")
        
        # Process the input
        processed_input = self._process_tool_input(tool_call.input, state.results)
        
        # Execute the tool
        print(f"Executing tool {tool_call.name} with input: {processed_input}")
        result = tool.invoke(processed_input)
        
        return str(result)
    
    def _process_tool_input(self, tool_input: Any, results: Dict[str, Dict[str, str]]) -> Any:
        """
        Process tool input to replace evidence references.
        
        Args:
            tool_input: The tool input to process
            results: The results dictionary
            
        Returns:
            Processed tool input
        """
        # Handle string inputs with evidence references
        if isinstance(tool_input, str) and tool_input.startswith("#E"):
            evidence_ref = tool_input
            if evidence_ref in results:
                # Join all results for this evidence reference
                evidence_values = list(results[evidence_ref].values())
                return " ".join(evidence_values)
            else:
                return f"No evidence found for {evidence_ref}"
        
        # Handle dictionary inputs
        if isinstance(tool_input, dict):
            processed_input = {}
            for key, value in tool_input.items():
                if isinstance(value, str) and value.startswith("#E"):
                    # Process evidence reference
                    evidence_ref = value
                    if evidence_ref in results:
                        # Get the first tool result for this evidence
                        evidence = results[evidence_ref]
                        first_result = next(iter(evidence.values())) if evidence else ""
                        processed_input[key] = first_result
                    else:
                        processed_input[key] = f"No evidence found for {evidence_ref}"
                else:
                    # Keep other values as is
                    processed_input[key] = value
            return processed_input
        
        # Return unmodified input for other types
        return tool_input
    
    def solve(self, state: ReWOOState) -> Command:
        """
        Generate the final solution using the collected evidence.
        
        Args:
            state: The current state
            
        Returns:
            Command to update the state with the final solution
        """
        task = state.task
        plan = state.plan
        results = state.results
        final_solution = []
        
        # Process each step
        for step in plan.steps:
            try:
                # Get evidence for this step
                evidence = results.get(step.evidence_ref, {})
                evidence_str = json.dumps(evidence, indent=2)
                
                # Create the solver prompt
                step_prompt = {
                    "task": task,
                    "step_number": step.step_number,
                    "step_description": step.description,
                    "evidence": evidence_str
                }
                
                # Invoke the solver
                print(f"Solving step {step.step_number}: {step.description}")
                step_result = self.solver.invoke(step_prompt)
                
                # Extract content from the result
                if hasattr(step_result, "content"):
                    result_content = step_result.content
                elif isinstance(step_result, str):
                    result_content = step_result
                else:
                    result_content = str(step_result)
                
                # Add to the final solution
                final_solution.append({
                    "step_number": step.step_number,
                    "description": step.description,
                    "result": result_content
                })
            except Exception as e:
                # Handle errors during solving
                error_msg = f"Error solving step {step.step_number}: {str(e)}"
                print(error_msg)
                traceback.print_exc()
                final_solution.append({
                    "step_number": step.step_number,
                    "description": step.description,
                    "result": error_msg
                })
        
        return Command(update={"final_solution": final_solution})
    
    def _route(self, state: ReWOOState) -> str:
        """
        Determine the next step in execution.
        
        Args:
            state: The current state
            
        Returns:
            The name of the next node to execute
        """
        if state.current_step_index is None:
            return "solving_phase"
        return "execute_step"
    
    def setup_workflow(self):
        """
        Set up the workflow graph for the agent.
        
        Creates the nodes and edges for the state graph.
        """
        # Create the state graph
        self.graph = StateGraph(self.config.state_schema)
        
        # Add nodes
        self.graph.add_node("planning_phase", self.plan)
        self.graph.add_node("execute_step", self.execute_step)
        self.graph.add_node("solving_phase", self.solve)
        
        # Add edges
        self.graph.add_edge("planning_phase", "execute_step")
        self.graph.add_edge("solving_phase", END)
        self.graph.add_conditional_edges("execute_step", self._route)
        self.graph.add_edge(START, "planning_phase")
        
        # Compile the graph if needed
        if self.config.should_compile_workflow:
            self.compile_graph(checkpointer=self.memory)
            
        # Visualize if needed
        if self.config.should_visualize_graph:
            self.visualize_graph(self.config.visualize_graph_output_name)
        
        return self.graph
    
    def run(self, task: str):
        """
        Run the agent on a task.
        
        Args:
            task: The task to solve
            
        Returns:
            The result of the execution
        """
        # Initialize if needed
        if not self.app:
            if not hasattr(self, "graph") or not self.graph:
                self.setup_workflow()
            self.compile_graph(checkpointer=self.memory)
        
        # Execute the workflow
        print(f"Running task: {task}")
        for step in self.app.stream({"task": task}, config=self.runnable_config, debug=True):
            print(step)
            print("---")
        
        # Return the final state
        return self.app.get_state(self.runnable_config)


# Example usage
if __name__ == "__main__":
    # Create the agent with default configuration
    agent = RewooAgent()
    
    # Set up the agent
    agent.setup_workflow()
    
    # Run the agent on a task
    result = agent.run("Find the sitemap for langgraph")
    
    # Print the final solution
    if "final_solution" in result:
        print("\nFinal Solution:")
        for step in result["final_solution"]:
            print(f"Step {step['step_number']}: {step['description']}")
            print(f"Result: {step['result']}")
            print()
    else:
        print("Execution incomplete or failed.")