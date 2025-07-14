# tests/agents/react/test_react_agent.py


# rom haive.agents.react.config import ReactAgentConfig
from haive.core.config.runnable import RunnableConfigManager
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.react.agent import ReactAgent


# Define tool functions (outside of test class to avoid fixture errors)
@tool
def calc_add(a: int, b: int) -> str:
    """Add two numbers."""
    return str(a + b)


def echo_message(message: str) -> str:
    """Echo back the input message."""
    return f"Echo: {message}"


react_agent = ReactAgent(
    name="ReactAgent",
    description="A React agent that can use tools to interact with the world.",
    engine=AugLLMConfig(
        # model="gpt-4o-mini",
        tools=[calc_add],
    ),
)
response = react_agent.run("What is 2 + 2?", debug=True)
print(response)
#
