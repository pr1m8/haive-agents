#!/usr/bin/env python3
"""Trace where the Unknown tool warning comes from."""

import logging
import warnings
from typing import List
from pydantic import BaseModel, Field
from langchain_core.messages import AIMessage, HumanMessage
from haive.core.graph.node.validation_node_config_v2 import ValidationNodeConfigV2
from haive.core.engine.aug_llm import AugLLMConfig

# Capture warnings
warnings.filterwarnings("always")

# Enable all logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s:%(lineno)d - %(levelname)s - %(message)s'
)

class Task(BaseModel):
    description: str

class Plan[T](BaseModel):
    objective: str
    steps: List[T]

def test_warning_source():
    """Find where the warning comes from."""
    engine = AugLLMConfig(structured_output_model=Plan[Task])
    
    val_node = ValidationNodeConfigV2(
        name="test_validation",
        engine_name="test_engine"
    )
    
    messages = [
        HumanMessage(content="Test"),
        AIMessage(
            content="",
            tool_calls=[{
                "id": "call_123",
                "name": "plan_task_generic",
                "args": {"objective": "Test", "steps": []}
            }]
        )
    ]
    
    state = {
        "messages": messages,  
        "engines": {"test_engine": engine},
        "engine_name": "test_engine"
    }
    
    # Capture warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        
        result = val_node(state)
        
        print(f"\nWarnings captured: {len(w)}")
        for warning in w:
            print(f"Warning: {warning.message}")
            print(f"  Category: {warning.category}")
            print(f"  Module: {warning.filename}")
            print(f"  Line: {warning.lineno}")

if __name__ == "__main__":
    test_warning_source()