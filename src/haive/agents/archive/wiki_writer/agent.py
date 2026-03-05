import uuid

from haive.core.engine.agent.agent import Agent as AgentArchitecture
from haive.core.engine.agent.config import AgentConfig as AgentArchitectureConfig
from pydantic import Field


class WikiWriterAgentConfig(AgentArchitectureConfig):
    """Configuration for the Wiki Writer Agent."""

    aug_llm_config: AugLLMConfig = Field(
        default=wiki_writer_aug_llm, description="LLM config for Wiki Writer"
    )
    state_schema: WikiWriterState = Field(
        default=WikiWriterState, description="State schema for the agent"
    )
    runnable_config: RunnableConfig = Field(
        default={"configurable": {"thread_id": str(uuid.uuid4())}},
        description="Agent runnable config",
    )


class WikiWriterAgent(AgentArchitecture):
    """An agent that writes a wiki page."""

    def __init__(self, config: WikiWriterAgentConfig = WikiWriterAgentConfig()):
        """Init  .

        Args:
            config: [TODO: Add description]
        """
        super().__init__(config)

    async def call_agent(self, question: str) -> str | None:
        """Call Agent.

        Args:
            question: [TODO: Add description]

        Returns:
            [TODO: Add return description]
        """
        return await super().call_agent(question)
