"""Configuration for the LLMCompiler agent using AugLLMConfig system."""
import uuid
from typing import Any
from .models import JoinerOutput
from .state import CompilerState
from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from haive.tools.tools.dev_tools import python_repl_tool
from haive.tools.tools.search_tools import tavily_search_tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import BaseTool, StructuredTool
from pydantic import BaseModel, Field, model_validator
planner_prompt = ChatPromptTemplate.from_messages([('system', 'You are an AI assistant that creates detailed step-by-step plans to solve complex user queries.\n\nYour task is to create a plan that maximizes parallelizability - execute as many steps in parallel as possible.\n\nAvailable tools:\n{tool_descriptions}\n\nAlso available:\n{num_tools}. join(): Finalize the answer and respond to the user.\n\nYour plan must meet these requirements:\n1. Each step must use exactly one tool from the list above\n2. Each step must have a unique ID starting from 1\n3. Steps can depend on outputs from previous steps using ${{step_id}} syntax\n4. The final step must be join() to finalize the answer\n5. Organize steps to maximize parallel execution - don\'t make steps depend on others unless necessary\n\nFor each step, include:\n- A thought explaining your reasoning (optional)\n- The step ID and tool to call with proper arguments\n- Any dependencies on previous steps using ${{step_id}} in arguments\n\nExample plan format:\n```\n1. search(query="current GDP of Japan")\nThought: Now I need to find population data\n2. search(query="current population of Japan")\n3. math(problem="divide ${{1}} by ${{2}}")\n4. join()\n<END_OF_PLAN>\n```\n\nYour plan should accomplish the user\'s goal efficiently in as few steps as possible.\n'), ('user', '{query}')])
replanner_prompt = ChatPromptTemplate.from_messages([('system', 'You are an AI assistant that improves existing plans based on execution results.\n\nYour task is to create a new plan that builds on the previous execution results to solve the user\'s query.\n\nAvailable tools:\n{tool_descriptions}\n\nAlso available:\n{num_tools}. join(): Finalize the answer and respond to the user.\n\nReview the previous plan and its execution results carefully. Then create a new plan that:\n1. DOES NOT repeat steps that were already successfully executed\n2. Addresses any errors or issues from the previous execution\n3. Continues from where the previous plan left off\n4. Continues step numbering from {next_idx} (do not repeat previous step numbers)\n5. Maximizes parallel execution where possible\n6. Ends with a join() step to finalize the answer\n\nFor each new step, include:\n- A thought explaining your reasoning (optional)\n- The step ID (starting from {next_idx}) and tool to call with proper arguments\n- Any dependencies on previous steps using ${{step_id}} in arguments\n\nExample plan format:\n```\nThought: The previous plan found GDP and population data but failed to calculate the ratio correctly.\n\n{next_idx}. math(problem="properly format GDP from ${{1}} to a number")\n{next_idx_plus_one}. math(problem="properly format population from ${{2}} to a number")\n{next_idx_plus_two}. math(problem="divide ${{3}} by ${{4}}")\n{next_idx_plus_three}. join()\n<END_OF_PLAN>\n```\n\nYour plan should efficiently solve the remaining parts of the user\'s query.\n'), ('user', '{query}'), ('system', '{feedback}')])
joiner_prompt = ChatPromptTemplate.from_messages([('system', "You analyze execution results and decide whether to provide a final answer or request additional steps.\n\nYour task is to:\n1. Review the user's original query\n2. Examine the results of the executed steps\n3. Decide if you have enough information to provide a complete answer\n\nIf you have enough information, provide a comprehensive final response that directly answers the user's query.\n\nIf you DON'T have enough information:\n- Identify what information is missing\n- Explain why the current results are insufficient\n- Recommend specific additional steps needed to answer the query\n\nWhen providing a final answer:\n- Synthesize information from all relevant steps\n- Present the answer in a clear, concise format\n- Include specific data points that support your answer\n- Address all parts of the user's original query\n\nBe decisive - either provide a complete answer or explicitly request additional specific information.\n"), ('user', '\nOriginal Query: {query}\n\nExecuted Steps:\n{executed_tasks}\n\nResults:\n{results}\n\nBased on these results, can I provide a complete answer or do I need more information?\n')])
default_planner_config = AugLLMConfig(name='llm_compiler_planner', llm_config=AzureLLMConfig(model='gpt-4o', parameters={'temperature': 0.7, 'max_tokens': 4096}), prompt_template=planner_prompt, tools=None)
default_replanner_config = AugLLMConfig(name='llm_compiler_replanner', llm_config=AzureLLMConfig(model='gpt-4o', parameters={'temperature': 0.7, 'max_tokens': 4096}), prompt_template=replanner_prompt, tools=None)
default_joiner_config = AugLLMConfig(name='llm_compiler_joiner', llm_config=AzureLLMConfig(model='gpt-4o', parameters={'temperature': 0.7, 'max_tokens': 2048}), prompt_template=joiner_prompt, structured_output_model=JoinerOutput, structured_output_params={'method': 'function_calling'})

class LLMCompilerAgentConfig(AgentConfig):
    """Configuration for the LLM Compiler Agent using AugLLMConfig system.

    The LLM Compiler agent creates a directed acyclic graph (DAG) of tasks
    and executes them in parallel when dependencies are satisfied.
    """
    planner_config: AugLLMConfig = Field(default=default_planner_config, description='Configuration for the planner LLM')
    replanner_config: AugLLMConfig = Field(default=default_replanner_config, description='Configuration for the replanner LLM')
    joiner_config: AugLLMConfig = Field(default=default_joiner_config, description='Configuration for the joiner LLM')
    tool_instances: list[BaseTool | StructuredTool] = Field(default=[tavily_search_tool, python_repl_tool], description='Tool instances available to the agent')
    tool_configs: dict[str, dict[str, Any]] = Field(default_factory=dict, description='Configuration for tool instantiation')
    max_execution_time: float = Field(default=60.0, description='Maximum time to wait for task execution in seconds')
    max_replanning_attempts: int = Field(default=3, description='Maximum number of replanning attempts')
    should_visualize_graph: bool = Field(default=True, description='Whether to visualize the agent graph')
    visualize_graph_output_name: str = Field(default='llm_compiler_graph.png', description='Path to save graph visualization')
    state_schema: type[BaseModel] = Field(default=CompilerState, description='The state schema for the agent')
    runnable_config: RunnableConfig = Field(default={'configurable': {'thread_id': str(uuid.uuid4())}}, description='The runnable config for the agent')

    @model_validator(mode='after')
    def validate_configs(self, values) -> Any:
        """Ensure that the configurations are valid."""
        if not values.planner_config.prompt_template:
            values.planner_config.prompt_template = planner_prompt
        if not values.replanner_config.prompt_template:
            values.replanner_config.prompt_template = replanner_prompt
        if not values.joiner_config.prompt_template:
            values.joiner_config.prompt_template = joiner_prompt
        return values
DEFAULT_CONFIG = LLMCompilerAgentConfig()