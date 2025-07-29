import asyncio
from typing import Any, Optional, Protocol


class AsyncAgent(Protocol):
    name: str

    async def arun(self, inputs: dict[str, Any],
                   debug: Optional[bool] = False) -> Any:
        """Standard LangChain-compatible async agent interface."""
        ...


class AgentTester:
    """
    A minimal, general-purpose tester for any agent that implements `.arun()`.

    Use this to quickly run agents in both synchronous and asynchronous contexts
    using a plain input dictionary.

    Attributes:
        agent (AsyncAgent): The agent to test.
        debug (bool): If True, prints input and output.

    Example:
        >>> from my_agent.agent import subquery_agent
        >>> from my_agent.models import Query
        >>> tester = AgentTester(subquery_agent, debug=True)
        >>> input_state = {"query": Query("How is AI used in medicine?")}
        >>> tester.run(input_state)
    """

    def __init__(self, agent: AsyncAgent, *, debug: bool = True):
        """
        Initialize the tester with an agent.

        Args:
            agent (AsyncAgent): The agent instance to run.
            debug (bool, optional): Print input/output. Defaults to True.
        """
        self.agent = agent
        self.debug = debug

    async def arun(self, input_state: dict[str, Any]) -> Any:
        """
        Run the agent asynchronously.

        Args:
            input_state (dict): The state dictionary passed to the agent.

        Returns:
            Any: The agent's structured response.
        """
        if self.debug:
            print(f"\n🚀 Running agent: {self.agent.name}")
            print(f"🟡 Input: {input_state}")

        result = await self.agent.arun(input_state, debug=self.debug)

        if self.debug:
            print(f"✅ Output from {self.agent.name}:
{result}\n")

        return result

    def run(self, input_state: dict[str, Any]) -> Any:
        """
        Run the agent synchronously (for CLI or scripts).

        Args:
            input_state (dict): The state dictionary passed to the agent.

        Returns:
            Any: The agent's output.
        """
        return asyncio.run(self.arun(input_state,debug=True))
