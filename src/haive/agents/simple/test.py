from haive.agents.simple.config import SimpleAgentConfig
from haive.agents.simple.agent import SimpleAgent
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm.base import AugLLMConfig
from haive.core.schema.schema_composer import SchemaComposer

class Plan(BaseModel):
    Steps: list[str] = Field(description="A list of steps to complete the task")
aug_llm = AugLLMConfig(model="gpt-4o", temperature=0.0, system_prompt="You are a helpful assistant that can help me plan my day.", structured_output_model=Plan)
config = SimpleAgentConfig(engine=aug_llm)
schema = SchemaComposer.from_components([aug_llm])
schema.pretty_print()
#a = agent.run("Write a plan for building a website")
#print(a)
