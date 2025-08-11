#!/usr/bin/env python3
"""Debug script to trace structured output tool usage in planning_v2."""

import asyncio
import logging
import json
from typing import Any, Dict
from pprint import pprint

from haive.agents.simple import SimpleAgent
from haive.agents.planning_v2.base.models import Status, Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.core.engine.aug_llm import AugLLMConfig

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Enable debug logging for key modules
for module in ['haive.core.engine', 'haive.core.graph', 'haive.agents.base']:
    logging.getLogger(module).setLevel(logging.DEBUG)


async def debug_structured_output():
    """Debug why LLM isn't using structured output tool."""
    
    print("\n" + "="*80)
    print("STRUCTURED OUTPUT DEBUGGING")
    print("="*80)
    
    # Create engine with structured output
    print("\n1. Creating AugLLMConfig with structured output...")
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
        force_tool_use=True  # Force tool use
    )
    
    # Debug engine configuration
    print("\n2. Engine Configuration:")
    print(f"   - Type: {type(engine)}")
    print(f"   - Temperature: {getattr(engine, 'temperature', 'NOT SET')}")
    print(f"   - Force Tool Use: {getattr(engine, 'force_tool_use', 'NOT SET')}")
    print(f"   - Structured Output Model: {getattr(engine, 'structured_output_model', 'NOT SET')}")
    print(f"   - Tools: {getattr(engine, 'tools', 'NOT SET')}")
    print(f"   - Tool Routes: {getattr(engine, 'tool_routes', 'NOT SET')}")
    print(f"   - Tool Names: {getattr(engine, 'tool_names', 'NOT SET')}")
    
    # Check tool configuration
    print("\n3. Tool Analysis:")
    tools = getattr(engine, 'tools', None)
    if tools:
        for i, tool in enumerate(tools):
            print(f"\n   Tool {i+1}:")
            print(f"   - Type: {type(tool)}")
            print(f"   - Name: {getattr(tool, 'name', 'NO NAME')}")
            
            # Check if it's a BaseModel
            from pydantic import BaseModel
            if isinstance(tool, type) and issubclass(tool, BaseModel):
                print(f"   - Is BaseModel: Yes")
                print(f"   - Has __call__: {hasattr(tool, '__call__') and callable(getattr(tool, '__call__'))}")
            
            # Check tool schema if available
            if hasattr(tool, 'args_schema'):
                print(f"   - Args Schema: {tool.args_schema}")
            if hasattr(tool, 'schema'):
                print(f"   - Schema: {tool.schema()}")
    else:
        print("   NO TOOLS CONFIGURED!")
    
    # Create agent
    print("\n4. Creating SimpleAgent...")
    agent = SimpleAgent(
        name="debug_planner",
        engine=engine
    )
    
    # Check agent configuration
    print("\n5. Agent Configuration:")
    print(f"   - Name: {agent.name}")
    print(f"   - Engine: {type(agent.engine)}")
    print(f"   - Structured Output Model: {getattr(agent, 'structured_output_model', 'NOT SET')}")
    
    # Check if agent has graph
    if hasattr(agent, '_graph'):
        print("\n6. Graph Configuration:")
        print(f"   - Graph exists: Yes")
        print(f"   - Nodes: {list(agent._graph.nodes)}")
        print(f"   - Edges: {list(agent._graph.edges)}")
    else:
        print("\n6. Graph Configuration: NO GRAPH FOUND")
    
    # Trace the execution
    print("\n7. Running agent with tracing...")
    
    # Set up tracing
    import sys
    import types
    
    def trace_calls(frame, event, arg):
        """Trace function calls to understand flow."""
        if event == 'call':
            # Get function/method name
            func_name = frame.f_code.co_name
            
            # Filter for relevant calls
            relevant_modules = ['haive.core.engine', 'haive.core.graph', 'haive.agents']
            module = frame.f_globals.get('__name__', '')
            
            if any(module.startswith(m) for m in relevant_modules):
                # Check for tool-related calls
                if any(keyword in func_name.lower() for keyword in ['tool', 'structured', 'output', 'invoke', 'call']):
                    print(f"\n>>> TRACE: {module}.{func_name}")
                    
                    # Print local variables for tool-related calls
                    if 'tool' in func_name.lower():
                        locals_dict = frame.f_locals
                        for key, value in locals_dict.items():
                            if key in ['self', 'tool', 'tools', 'tool_name', 'tool_route', 'structured_output_model']:
                                print(f"    {key}: {type(value)} = {repr(value)[:100]}")
        
        return trace_calls
    
    # Enable tracing
    sys.settrace(trace_calls)
    
    try:
        # Run the agent
        input_data = {"objective": "Build a simple REST API for a todo list"}
        
        print(f"\n8. Invoking agent with: {input_data}")
        result = await agent.arun(input_data)
        
        print("\n9. Execution Result:")
        print(f"   - Type: {type(result)}")
        print(f"   - Is Plan: {isinstance(result, Plan)}")
        
        if hasattr(result, 'model_dump'):
            print(f"   - Content: {json.dumps(result.model_dump(), indent=2)}")
        else:
            print(f"   - Content: {result}")
        
        # Check for messages in result
        if hasattr(result, 'messages'):
            print(f"\n10. Messages in result: {len(result.messages)}")
            for i, msg in enumerate(result.messages):
                print(f"\n   Message {i+1}:")
                print(f"   - Type: {type(msg)}")
                print(f"   - Content: {msg}")
                
                # Check for tool calls
                if hasattr(msg, 'tool_calls'):
                    print(f"   - Tool Calls: {msg.tool_calls}")
        
    finally:
        # Disable tracing
        sys.settrace(None)
    
    print("\n" + "="*80)
    print("DEBUGGING COMPLETE")
    print("="*80)


async def inspect_tool_binding():
    """Inspect how tools are bound to the LLM."""
    print("\n" + "="*80)
    print("TOOL BINDING INSPECTION")
    print("="*80)
    
    # Create engine
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
        force_tool_use=True
    )
    
    # Get the actual LLM binding
    print("\n1. Getting LLM binding...")
    
    # Check if engine has get_runnable
    if hasattr(engine, 'get_runnable'):
        runnable = engine.get_runnable()
        print(f"   - Runnable type: {type(runnable)}")
        
        # Check if it's bound with tools
        if hasattr(runnable, 'kwargs'):
            print(f"   - Runnable kwargs: {list(runnable.kwargs.keys())}")
            if 'tools' in runnable.kwargs:
                print(f"   - Tools in kwargs: {runnable.kwargs['tools']}")
            if 'tool_choice' in runnable.kwargs:
                print(f"   - Tool choice: {runnable.kwargs['tool_choice']}")
    
    # Check the raw config
    print("\n2. Raw Engine State:")
    print(f"   - Tools list: {getattr(engine, 'tools', 'NOT SET')}")
    print(f"   - Tool names: {getattr(engine, 'tool_names', 'NOT SET')}")
    print(f"   - Force tool use: {getattr(engine, 'force_tool_use', 'NOT SET')}")
    
    # Check tool conversion
    print("\n3. Tool Conversion Check:")
    if engine.tools:
        from haive.core.tool import ToolEngine
        tool_engine = ToolEngine()
        
        for tool in engine.tools:
            print(f"\n   Original tool: {tool}")
            try:
                converted = tool_engine.convert_to_langchain_tool(tool)
                print(f"   Converted to: {type(converted)}")
                print(f"   Tool name: {getattr(converted, 'name', 'NO NAME')}")
                print(f"   Tool description: {getattr(converted, 'description', 'NO DESC')}")
            except Exception as e:
                print(f"   Conversion failed: {e}")


async def test_direct_llm_call():
    """Test calling LLM directly with tools."""
    print("\n" + "="*80)
    print("DIRECT LLM CALL TEST")
    print("="*80)
    
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI
    from langchain_core.tools import tool
    
    # Create a simple tool
    @tool
    def plan_task_generic(objective: str, status: str = "pending", steps: list = None) -> dict:
        """Create a plan with tasks for a given objective."""
        return {
            "objective": objective,
            "status": status,
            "steps": steps or []
        }
    
    # Create LLM with tool
    llm = ChatOpenAI(temperature=0.3)
    llm_with_tools = llm.bind_tools([plan_task_generic], tool_choice="required")
    
    # Test direct call
    print("\n1. Testing direct LLM call with tool...")
    messages = [HumanMessage(content="Create a plan to build a REST API")]
    
    response = await llm_with_tools.ainvoke(messages)
    
    print(f"\n2. Response type: {type(response)}")
    print(f"   - Content: {response.content}")
    print(f"   - Tool calls: {response.tool_calls}")
    
    if response.tool_calls:
        print("\n3. Tool call details:")
        for tc in response.tool_calls:
            print(f"   - Name: {tc['name']}")
            print(f"   - Args: {tc['args']}")


async def main():
    """Run all debugging functions."""
    # Run structured output debugging
    await debug_structured_output()
    
    # Inspect tool binding
    await inspect_tool_binding()
    
    # Test direct LLM call
    await test_direct_llm_call()


if __name__ == "__main__":
    asyncio.run(main())