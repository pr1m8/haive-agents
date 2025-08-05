#!/usr/bin/env python
"""Debug the msgpack serialization issue systematically."""

import contextlib
import json
import pickle

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.base import SequentialAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


# Define tools/schemas
@tool
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b


class Plan(BaseModel):
    steps: list[str] = Field(description="list of steps")


# Create engines
add_aug = AugLLMConfig(tools=[add])
plan_aug = AugLLMConfig(structured_output_model=Plan, structured_output_version="v2")


# Test if engine can be dumped
with contextlib.suppress(Exception):
    dumped = add_aug.model_dump()

# Test pickle on engine directly
with contextlib.suppress(Exception):
    pickle.dumps(add_aug)

# Test json on dumped engine
try:
    dumped = add_aug.model_dump()
    json.dumps(dumped)
except Exception:
    # Find problematic fields
    for key, value in dumped.items():
        with contextlib.suppress(Exception):
            json.dumps({key: value})


# Test ReactAgent alone
react = ReactAgent(engine=add_aug)
react.compile()
with contextlib.suppress(Exception):
    result = react.run({"messages": [HumanMessage(content="Test")]})

# Test SimpleAgent alone
simple = SimpleAgent(engine=plan_aug)
simple.compile()
with contextlib.suppress(Exception):
    result = simple.run({"messages": [HumanMessage(content="Test")]})

multi = SequentialAgent(agents=[react, simple])
multi.compile()

# Get prepared input
prepared = multi._prepare_input({"messages": [HumanMessage(content="Test")]})

state_dict = prepared.model_dump() if hasattr(prepared, "model_dump") else prepared

if "engines" in state_dict:
    for _name, _engine in state_dict["engines"].items():
        pass

if "engines" in state_dict:
    for _eng_name, eng_data in state_dict["engines"].items():
        if hasattr(eng_data, "model_fields") or isinstance(eng_data, dict):
            pass
        else:
            pass

# The real test - run the multi-agent
try:
    result = multi.run({"messages": [HumanMessage(content="Calculate 5 + 3")]})
except Exception as e:
    if "msgpack" in str(e):
        pass

# Create agents without tools/schemas
simple_react = ReactAgent(name="Simple React")
simple_simple = SimpleAgent(name="Simple Simple")
simple_multi = SequentialAgent(agents=[simple_react, simple_simple])
simple_multi.compile()

with contextlib.suppress(Exception):
    result = simple_multi.run({"messages": [HumanMessage(content="Test")]})
