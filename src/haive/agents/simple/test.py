from haive.agents.simple.config import SimpleAgentConfig
from haive.agents.simple.agent import SimpleAgent
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.schema_composer import SchemaComposer
from haive.core.utils.pydantic_utils import display_model, display_code, pretty_print, compare_models

class Plan(BaseModel):
    Steps: list[str] = Field(description="A list of steps to complete the task")
    
aug_llm = AugLLMConfig(model="gpt-4o", temperature=0.0, system_prompt="You are a helpful assistant that can help me plan my day.", structured_output_model=Plan)
config = SimpleAgentConfig(engine=aug_llm)
agent = SimpleAgent(config)
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

# Run the agent
result = agent.run("Write a plan for building a website")

# Display the result if it's a Pydantic model
if hasattr(result, "model_dump"):
    pretty_print(result, "Planning Result")
else:
    print(result)

# Display the Plan model code
display_code(Plan, "Plan Model Definition")

# Compare the Plan model with another model
class EnhancedPlan(BaseModel):
    Steps: list[str] = Field(description="A list of steps to complete the task")
    Timeline: list[str] = Field(description="Estimated timeline for each step")

compare_models(Plan, EnhancedPlan, "Basic Plan", "Enhanced Plan")