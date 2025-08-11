#!/usr/bin/env python3
"""
Debug the AugLLMConfig initialization order to see when format instructions get lost.
"""

import os
from typing import List
from pydantic import BaseModel, Field


# Enable debug mode
os.environ['DEBUG_MODE'] = '1'


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)


def test_initialization_step_by_step():
    """Test AugLLMConfig initialization step by step."""
    print("🔍 DEBUGGING AUGLLMCONFIG INITIALIZATION ORDER")
    print("=" * 60)
    
    # Monkey patch to debug
    from haive.core.engine.aug_llm import AugLLMConfig
    
    # Store original methods
    original_setup_format_instructions = AugLLMConfig._setup_format_instructions
    original_update_chat_template = AugLLMConfig._update_chat_template_messages
    original_ensure_messages = AugLLMConfig._ensure_messages_placeholder_handling
    
    def debug_setup_format_instructions(self):
        """Debug wrapper for _setup_format_instructions."""
        print(f"\n🔧 _setup_format_instructions called")
        partials_before = dict(self.prompt_template.partial_variables)
        print(f"   Partials before: {list(partials_before.keys())}")
        
        result = original_setup_format_instructions(self)
        
        partials_after = dict(self.prompt_template.partial_variables)
        print(f"   Partials after: {list(partials_after.keys())}")
        
        has_instructions = "format_instructions" in partials_after
        print(f"   Format instructions added: {has_instructions}")
        if has_instructions:
            print(f"   Instructions length: {len(partials_after['format_instructions'])} chars")
        
        return result
    
    def debug_update_chat_template(self, messages):
        """Debug wrapper for _update_chat_template_messages."""
        print(f"\n🔄 _update_chat_template_messages called")
        partials_before = dict(self.prompt_template.partial_variables) if hasattr(self, 'prompt_template') and self.prompt_template else {}
        print(f"   Partials before: {list(partials_before.keys())}")
        has_instructions_before = "format_instructions" in partials_before
        print(f"   Format instructions before: {has_instructions_before}")
        
        result = original_update_chat_template(self, messages)
        
        partials_after = dict(self.prompt_template.partial_variables)
        print(f"   Partials after: {list(partials_after.keys())}")
        has_instructions_after = "format_instructions" in partials_after
        print(f"   Format instructions after: {has_instructions_after}")
        
        if has_instructions_before and not has_instructions_after:
            print(f"   ❌ FORMAT INSTRUCTIONS LOST HERE!")
        
        return result
    
    def debug_ensure_messages(self):
        """Debug wrapper for _ensure_messages_placeholder_handling."""
        print(f"\n📝 _ensure_messages_placeholder_handling called")
        partials_before = dict(self.prompt_template.partial_variables) if hasattr(self, 'prompt_template') and self.prompt_template else {}
        print(f"   Partials before: {list(partials_before.keys())}")
        
        result = original_ensure_messages(self)
        
        partials_after = dict(self.prompt_template.partial_variables)
        print(f"   Partials after: {list(partials_after.keys())}")
        
        return result
    
    # Patch methods
    AugLLMConfig._setup_format_instructions = debug_setup_format_instructions
    AugLLMConfig._update_chat_template_messages = debug_update_chat_template
    AugLLMConfig._ensure_messages_placeholder_handling = debug_ensure_messages
    
    try:
        print(f"Creating AugLLMConfig...")
        config = AugLLMConfig(
            structured_output_model=Plan[Task],
            structured_output_version="v2"
        )
        
        print(f"\n🏁 FINAL STATE:")
        final_partials = config.prompt_template.partial_variables
        print(f"   Final partials: {list(final_partials.keys())}")
        has_final_instructions = "format_instructions" in final_partials
        print(f"   Final format_instructions: {has_final_instructions}")
        
        # Also check internal state
        has_internal = hasattr(config, '_format_instructions_text') and config._format_instructions_text
        print(f"   Internal _format_instructions_text: {has_internal}")
        
    finally:
        # Restore original methods
        AugLLMConfig._setup_format_instructions = original_setup_format_instructions
        AugLLMConfig._update_chat_template_messages = original_update_chat_template
        AugLLMConfig._ensure_messages_placeholder_handling = original_ensure_messages
    
    return config


if __name__ == "__main__":
    config = test_initialization_step_by_step()