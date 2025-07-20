"""Enhanced ReactAgent implementation using Agent[AugLLMConfig].

ReactAgent = Agent[AugLLMConfig] + reasoning loop with tools.
"""

import logging
from typing import Any, Dict, List, Literal, Optional, Union

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage
from langchain_core.tools import BaseTool
from langgraph.graph import END, START
from pydantic import Field, model_validator

from haive.core.engine.aug_llm.config import AugLLMConfig
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.node.tool_node_config_v2 import ToolNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph

# Import base enhanced agent when available
# from haive.agents.base.enhanced_agent import Agent
# For now, using a minimal base
from haive.agents.simple.enhanced_simple_real import EnhancedAgentBase as Agent

logger = logging.getLogger(__name__)


class ReactAgent(Agent):  # Will be Agent[AugLLMConfig] when imports fixed
    """Enhanced ReactAgent with reasoning and action loop.
    
    ReactAgent = Agent[AugLLMConfig] + reasoning loop with tools.
    
    The ReAct pattern (Reasoning and Acting) allows the agent to:
    1. Reason about what action to take
    2. Take the action (use a tool)
    3. Observe the result
    4. Reason again based on the observation
    5. Continue until task is complete
    
    Attributes:
        max_iterations: Maximum reasoning iterations (default: 10)
        tools: List of tools available to the agent
        react_prompt: Optional custom prompt for ReAct pattern
        
    Examples:
        Basic usage::
        
            from langchain_core.tools import tool
            
            @tool
            def calculator(expression: str) -> str:
                '''Calculate mathematical expressions.'''
                return str(eval(expression))
            
            agent = ReactAgent(
                name="math_assistant",
                engine=AugLLMConfig(temperature=0.1),
                tools=[calculator],
                max_iterations=5
            )
            
            result = agent.run("What is 15 * 23 + 47?")
            # Agent will reason, use calculator, and provide answer
            
        With multiple tools::
        
            @tool
            def web_search(query: str) -> str:
                '''Search the web for information.'''
                return f"Results for {query}..."
                
            agent = ReactAgent(
                name="researcher",
                tools=[calculator, web_search]
            )
            
            result = agent.run("Find the population of Paris and calculate 10% of it")
    """
    
    # ReAct specific fields
    max_iterations: int = Field(
        default=10,
        ge=1,
        le=50,
        description="Maximum number of reasoning iterations"
    )
    
    tools: List[Union[BaseTool, Any]] = Field(
        default_factory=list,
        description="Tools available to the agent"
    )
    
    react_prompt: Optional[str] = Field(
        default=None,
        description="Custom ReAct prompt template"
    )
    
    # Convenience fields that sync to AugLLMConfig
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(default=None, ge=1)
    system_message: Optional[str] = Field(default=None)
    
    @model_validator(mode="before")
    @classmethod
    def ensure_aug_llm_config(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Ensure we have an AugLLMConfig engine with tools."""
        if not isinstance(values, dict):
            return values
        
        # Create engine if not provided
        if "engine" not in values or values["engine"] is None:
            values["engine"] = AugLLMConfig(
                temperature=values.get("temperature", 0.7),
                max_tokens=values.get("max_tokens"),
                system_message=values.get("system_message"),
                tools=values.get("tools", [])
            )
        elif not isinstance(values["engine"], AugLLMConfig):
            logger.warning("ReactAgent requires AugLLMConfig engine")
            values["engine"] = AugLLMConfig(tools=values.get("tools", []))
        
        return values
    
    def setup_agent(self) -> None:
        """Setup ReAct agent with reasoning prompt."""
        # Sync fields to engine
        if isinstance(self.engine, AugLLMConfig):
            self.engine.temperature = self.temperature
            if self.max_tokens:
                self.engine.max_tokens = self.max_tokens
            if self.tools:
                self.engine.tools = self.tools
                
            # Set ReAct system message if not custom
            if not self.system_message and not self.react_prompt:
                self.engine.system_message = self._get_default_react_prompt()
            elif self.react_prompt:
                self.engine.system_message = self.react_prompt
            elif self.system_message:
                self.engine.system_message = self.system_message
    
    def _get_default_react_prompt(self) -> str:
        """Get default ReAct prompt."""
        tool_descriptions = "\n".join([
            f"- {tool.name}: {tool.description}"
            for tool in self.tools
        ])
        
        return f"""You are a helpful assistant that uses the ReAct (Reasoning and Acting) pattern.

Available tools:
{tool_descriptions}

For each user request:
1. Reason about what needs to be done
2. Decide which tool to use (if any)
3. Use the tool and observe the result
4. Reason about the result
5. Continue until you can provide a final answer

Always think step by step and explain your reasoning."""
    
    def build_graph(self) -> BaseGraph:
        """Build ReAct pattern graph with reasoning loop."""
        graph = BaseGraph(name=f"{self.name}_react_graph")
        
        # Add engine node (reasoning)
        engine_node = EngineNodeConfig(
            name="reason",
            engine=self.engine
        )
        graph.add_node("reason", engine_node)
        
        # Add tool node if tools available
        if self.tools:
            tool_node = ToolNodeConfig(
                name="act",
                tools=self.tools
            )
            graph.add_node("act", tool_node)
            
            # Start -> Reason
            graph.add_edge(START, "reason")
            
            # Conditional routing from reason node
            def route_reasoning(state: Dict[str, Any]) -> Literal["act", "end"]:
                """Route based on reasoning output."""
                messages = state.get("messages", [])
                if not messages:
                    return "end"
                
                last_message = messages[-1]
                
                # Check iteration limit
                iterations = sum(1 for m in messages if isinstance(m, AIMessage))
                if iterations >= self.max_iterations:
                    logger.warning(f"Reached max iterations ({self.max_iterations})")
                    return "end"
                
                # Check if agent wants to use a tool
                if isinstance(last_message, AIMessage) and last_message.tool_calls:
                    return "act"
                
                return "end"
            
            graph.add_conditional_edges(
                "reason",
                route_reasoning,
                {
                    "act": "act",
                    "end": END
                }
            )
            
            # After acting, go back to reasoning
            graph.add_edge("act", "reason")
            
        else:
            # No tools, just reason once
            graph.add_edge(START, "reason")
            graph.add_edge("reason", END)
        
        return graph
    
    def __repr__(self) -> str:
        """String representation showing engine type and tools."""
        engine_type = type(self.engine).__name__ if self.engine else "None"
        tool_names = [t.name if hasattr(t, 'name') else str(t) for t in self.tools]
        return f"ReactAgent[{engine_type}](name='{self.name}', tools={tool_names})"


# Example usage
if __name__ == "__main__":
    from langchain_core.tools import tool
    
    @tool
    def calculator(expression: str) -> str:
        """Calculate mathematical expressions."""
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {e}"
    
    @tool 
    def word_counter(text: str) -> str:
        """Count words in text."""
        words = text.split()
        return f"The text contains {len(words)} words"
    
    # Create ReactAgent
    agent = ReactAgent(
        name="react_demo",
        temperature=0.1,  # Low temperature for reasoning
        tools=[calculator, word_counter],
        max_iterations=5
    )
    
    print(f"Created: {agent}")
    print(f"Engine type: {type(agent.engine).__name__}")
    print(f"Tools: {[t.name for t in agent.tools]}")
    
    # Example reasoning task
    print("\nExample: Complex calculation")
    print("Input: 'Calculate (15 * 23) + (47 / 2) and tell me how many words are in your explanation'")
    
    # In real usage:
    # result = agent.run("Calculate (15 * 23) + (47 / 2) and tell me how many words are in your explanation")
    # Agent would:
    # 1. Reason about the task
    # 2. Use calculator for (15 * 23) = 345
    # 3. Use calculator for (47 / 2) = 23.5
    # 4. Use calculator for 345 + 23.5 = 368.5
    # 5. Use word_counter on its explanation
    # 6. Provide final answer with both results