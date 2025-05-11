import uuid

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.schema_composer import SchemaComposer
from haive.core.utils.pydantic_utils import (
    compare_models,
    display_code,
    display_model,
    pretty_print,
)
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.agents.simple.config import SimpleAgentConfig


class Plan(BaseModel):
    Steps: list[str] = Field(description="A list of steps to complete the task")


aug_llm = AugLLMConfig(
    model="gpt-4o",
    temperature=0.0,
    system_prompt="You are a helpful assistant that can help me plan my day.",
    structured_output_model=Plan,
    prompt_template=ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that can help me plan my day."),
            # ("placeholder", "{messages}")
        ]
    ),
)

print(aug_llm.prompt_template)
# breakpoint()
schema = SchemaComposer.from_components([aug_llm])

# Display the schema
print(schema)
print(schema.to_python_code())

# Generate input/output schemas
input_schema = schema.create_input_schema()
output_schema = schema.create_output_schema()

# Use the utility functions with the derived schemas
print("Input Schema Structure:")
display_model(input_schema, "Input Schema")

print("Output Schema Structure:")
display_model(output_schema, "Output Schema")
display_model(schema, "Schema")
# Run the agent

config = SimpleAgentConfig(engine=aug_llm)
agent = SimpleAgent(config)
result = agent.run(
    {"messages": [HumanMessage(content="Write a plan for building a website")]},
    debug=True,
    runnable_config={"configurable": {"thread_id": uuid.uuid4()}},
)

# Display the result if it's a Pydantic model
if hasattr(result, "model_dump"):
    pretty_print(result, "Planning Result")
else:
    print(result)

# Display the Plan model code
display_code(Plan, "Plan Model Definition")

# Compare the Plan model with another model
# class EnhancedPlan(BaseModel):
# Steps: list[str] = Field(description="A list of steps to complete the task")
# Timeline: list[str] = Field(description="Estimated timeline for each step")

# compare_models(Plan, EnhancedPlan, "Basic Plan", "Enhanced Plan")
# agent.run({'messages':[{'role': 'user', 'content': "Write a plan for building a website"}]},debug=True)
