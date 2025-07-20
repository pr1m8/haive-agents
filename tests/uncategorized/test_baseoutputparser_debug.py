"""Debug BaseOutputParser and PydanticUndefined issues."""

import logging

from haive.core.engine.aug_llm.config import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v2 import SimpleAgentV2

# Set up logging to see details
logging.basicConfig(level=logging.DEBUG)


class SimpleResponse(BaseModel):
    """Simple response model."""

    answer: str = Field(description="The answer")


# Create a simple prompt
simple_prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("human", "{query}")]
)


def test_basic_case():
    """Test the most basic case."""
    try:
        # Create AugLLMConfig
        engine = AugLLMConfig(
            prompt_template=simple_prompt,
            structured_output_model=SimpleResponse,
            structured_output_version="v2",
        )

        # Check for PydanticUndefined
        from pydantic_core import PydanticUndefined

        for _field_name, field_info in engine.model_fields.items():
            if (
                hasattr(field_info, "default")
                and field_info.default is PydanticUndefined
            ) or hasattr(field_info, "default"):
                pass

        # Create agent
        agent = SimpleAgentV2(engine=engine)

        # Try to get state schema
        state_schema = agent.state_schema

        # Check state schema for PydanticUndefined
        if state_schema and hasattr(state_schema, "model_fields"):
            for _field_name, field_info in state_schema.model_fields.items():
                if (
                    hasattr(field_info, "default")
                    and field_info.default is PydanticUndefined
                ) or hasattr(field_info, "default"):
                    pass

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


def test_run_attempt():
    """Test actually running the agent."""
    try:
        engine = AugLLMConfig(
            prompt_template=simple_prompt,
            structured_output_model=SimpleResponse,
            structured_output_version="v2",
        )

        agent = SimpleAgentV2(engine=engine)

        # Try to run
        agent.run("What is 2+2?", debug=True)
        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":

    basic_ok = test_basic_case()
    if basic_ok:
        test_run_attempt()
    else:
        pass
