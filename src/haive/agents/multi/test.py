from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.base.agent import Agent
from haive.agents.rag.base.agent import SimpleRAGAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


@tool
def add(a: int, b: int) -> int:
    """returns the sum of two numbers"""
    return a + b


class Plan(BaseModel):
    steps: List[str] = Field(description="list of steps")


add_aug = AugLLMConfig(tools=[add])
plan_aug = AugLLMConfig(structured_output_model=Plan, structured_output_version="v2")
simple_agent = SimpleAgent(engine=plan_aug)
react_agent = ReactAgent(engine=add_aug)
# REPLACE WIOTH AGENTSCHEMACOMPOSER SO ITS AUTOMATIC.
# ss = SchemaComposer().from_components([react_agent,simple_agent])
from langchain_core.messages import HumanMessage

# SEQQUENTIAL AGENT IMPLEMENTAIOTN. Should share messages input for EXAMPLE, output schema defaults to last one, simple in this case.abs
from haive.agents.multi.base import ConditionalAgent, ParallelAgent, SequentialAgent

structured_react = SequentialAgent(agents=[react_agent, simple_agent])
# base_rag_agent.state_schema = agent_ss
# Test the sequential agent
print("Testing SequentialAgent...")
try:
    structured_react.compile()
    result = structured_react.run(
        {"messages": [HumanMessage(content="Calculate 5 + 3, then create a plan")]}
    )
    print("✅ Success!")
    print(f"Result: {result}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback

    traceback.print_exc()
