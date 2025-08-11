#!/usr/bin/env python3
"""
Debug what format instructions are actually being sent to the LLM in the prompt.
"""

from typing import List
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)


def debug_actual_format_instructions_in_prompt():
    """Debug if format instructions are actually included in the prompt sent to LLM."""
    print("🔍 DEBUGGING ACTUAL FORMAT INSTRUCTIONS IN PROMPT")
    print("=" * 70)
    
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2",
        temperature=0.1
    )
    
    print(f"1. Configuration:")
    print(f"   structured_output_version: {config.structured_output_version}")
    print(f"   include_format_instructions: {config.include_format_instructions}")
    print(f"   use_tool_for_format_instructions: {config.use_tool_for_format_instructions}")
    print(f"   force_tool_use: {config.force_tool_use}")
    
    # Check internal format instructions
    has_internal = hasattr(config, '_format_instructions_text') and config._format_instructions_text
    print(f"   _format_instructions_text exists: {has_internal}")
    if has_internal:
        print(f"   Internal instructions length: {len(config._format_instructions_text)} chars")
    
    # Check prompt template partial variables
    partials = config.prompt_template.partial_variables
    print(f"   Prompt template partials: {list(partials.keys())}")
    has_format_instructions = "format_instructions" in partials
    print(f"   format_instructions in partials: {has_format_instructions}")
    
    if has_format_instructions:
        instructions = partials["format_instructions"]
        print(f"   Partial format_instructions length: {len(instructions)} chars")
    
    print(f"\n2. PROMPT TEMPLATE ANALYSIS:")
    print(f"   Template type: {type(config.prompt_template)}")
    print(f"   Input variables: {config.prompt_template.input_variables}")
    print(f"   Optional variables: {getattr(config.prompt_template, 'optional_variables', 'None')}")
    
    # Get the actual messages in the template
    if hasattr(config.prompt_template, 'messages'):
        print(f"   Messages count: {len(config.prompt_template.messages)}")
        for i, msg_template in enumerate(config.prompt_template.messages):
            print(f"   Message {i} type: {type(msg_template)}")
            if hasattr(msg_template, 'prompt'):
                template_text = msg_template.prompt.template if hasattr(msg_template.prompt, 'template') else str(msg_template.prompt)
                print(f"   Message {i} template: {template_text[:200]}...")
                
                # Check if format_instructions is in the template
                if "format_instructions" in template_text:
                    print(f"     ✅ format_instructions found in message {i}")
                else:
                    print(f"     ❌ format_instructions NOT found in message {i}")
    
    print(f"\n3. ACTUAL PROMPT FORMATTING TEST:")
    # Test what actually gets sent to the LLM
    input_data = {
        "messages": [{
            "role": "user", 
            "content": "Create a simple plan with 2 tasks"
        }]
    }
    
    try:
        # Format the prompt to see what gets sent
        formatted = config.prompt_template.format_prompt(**input_data)
        print(f"   Formatted messages count: {len(formatted.messages)}")
        
        for i, msg in enumerate(formatted.messages):
            print(f"   Message {i} ({msg.type}):")
            content = msg.content[:500] if len(msg.content) > 500 else msg.content
            print(f"     Content: {content}")
            
            # Check if format instructions are in the actual content
            if "format_instructions" in msg.content:
                print(f"     ✅ format_instructions variable found in content")
            elif "JSON schema" in msg.content:
                print(f"     ✅ JSON schema found in content")
            elif "output should be formatted" in msg.content.lower():
                print(f"     ✅ Format guidance found in content")
            else:
                print(f"     ❌ No format instructions found in content")
                
    except Exception as e:
        print(f"   ❌ Failed to format prompt: {e}")
        import traceback
        traceback.print_exc()


def debug_v1_vs_v2_format_instructions():
    """Compare format instructions usage between v1 and v2 modes."""
    print(f"\n" + "=" * 70)
    print("🔄 COMPARING V1 VS V2 FORMAT INSTRUCTIONS")
    print("=" * 70)
    
    # V1 Configuration
    config_v1 = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v1",
        temperature=0.1
    )
    
    # V2 Configuration  
    config_v2 = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2",
        temperature=0.1
    )
    
    configs = [("V1", config_v1), ("V2", config_v2)]
    
    for version, config in configs:
        print(f"\n{version} Configuration:")
        print(f"   force_tool_use: {config.force_tool_use}")
        print(f"   include_format_instructions: {config.include_format_instructions}")
        print(f"   use_tool_for_format_instructions: {config.use_tool_for_format_instructions}")
        
        # Check internal and partial format instructions
        has_internal = hasattr(config, '_format_instructions_text') and config._format_instructions_text
        has_partial = "format_instructions" in config.prompt_template.partial_variables
        
        print(f"   Internal format instructions: {has_internal}")
        print(f"   Partial format instructions: {has_partial}")
        
        if has_internal:
            print(f"   Internal length: {len(config._format_instructions_text)} chars")
        if has_partial:
            instructions = config.prompt_template.partial_variables["format_instructions"]
            print(f"   Partial length: {len(instructions)} chars")
        
        # Test actual prompt formatting
        input_data = {"messages": [{"role": "user", "content": "Test"}]}
        try:
            formatted = config.prompt_template.format_prompt(**input_data)
            has_format_guidance = any(
                "schema" in msg.content.lower() or 
                "json" in msg.content.lower() or 
                "format" in msg.content.lower()
                for msg in formatted.messages
            )
            print(f"   Format guidance in prompt: {has_format_guidance}")
            
        except Exception as e:
            print(f"   ❌ Failed to format: {e}")


if __name__ == "__main__":
    debug_actual_format_instructions_in_prompt()
    debug_v1_vs_v2_format_instructions()
    
    print(f"\n" + "=" * 70)
    print("🏁 KEY QUESTIONS TO ANSWER:")
    print("=" * 70)
    print("1. Are format instructions actually in the prompt sent to LLM in v2 mode?")
    print("2. If not, why does v2 mode ignore format instructions?") 
    print("3. Should v2 mode rely only on tool schema without format instructions?")
    print("4. Is the tool schema sufficient for nested object structures?")