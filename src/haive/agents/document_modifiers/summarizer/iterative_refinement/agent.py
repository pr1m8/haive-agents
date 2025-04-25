import operator
from typing import List, Literal, TypedDict,Union   

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig
from langgraph.constants import Send
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel,Field
from haive.core.engine.aug_llm import AugLLMConfig
#from haive.core.agent_architecture.base import AgentState
from langgraph.graph import START, END
from haive.core.engine.agent.agent import Agent,AgentConfig
from haive.core.engine.agent.agent import register_agent
#from haive.core.engine.agent.agent import AgentConfig
from typing import Dict
from agents.document_agents.summarizer.iterative_refinement.engines import initial_summary_aug_llm,refine_summary_aug_llm
from langgraph.types import Command
from langchain_core.messages import AnyMessage
import asyncio

from langchain_core.documents import Document
from agents.document_agents.summarizer.iterative_refinement.state import IterativeSummarizerState
# Initial summary
from agents.document_agents.summarizer.iterative_refinement.config import IterativeSummarizerConfig


@register_agent(IterativeSummarizerConfig)
class IterativeSummarizer(Agent[IterativeSummarizerConfig]):
    """
    An agent that summarizes a document iteratively.
    """
    def __init__(self, config: IterativeSummarizerConfig=IterativeSummarizerConfig()):
        super().__init__(config)
    

    # We define functions for each node, including a node that generates
    # the initial summary:
    async def generate_initial_summary(self,state: IterativeSummarizerState, config: RunnableConfig):
        summary = await self.engines['initial_summary'].ainvoke(
            state.contents[0],
            config,
        )
        return Command(update={"summary": summary, "index": 1})


    # And a node that refines the summary based on the next document
    async def refine_summary(self,state: IterativeSummarizerState, config: RunnableConfig):
        content = state.contents[state.index]
        summary = await self.engines['refine_summary'].ainvoke(
            {"existing_answer": state.summary, "context": content},
            config,
        )

        return Command(update={"summary": summary, "index": state.index + 1})   


    def setup_workflow(self):
        self.graph.add_node("generate_initial_summary", self.generate_initial_summary)
        self.graph.add_node("refine_summary", self.refine_summary)

        self.graph.add_edge(START, "generate_initial_summary")
        self.graph.add_conditional_edges("generate_initial_summary", self.state_schema.should_refine)
        self.graph.add_conditional_edges("refine_summary", self.state_schema.should_refine)

from langchain_core.documents import Document
test_docs = [
        Document(page_content="This is a test document about machine learning."),
        Document(page_content="This document expands on deep learning architectures."),
        Document(page_content="It also discusses how transformers are used in NLP."),
        Document(page_content="Finally, it provides an overview of applications of AI.")
    ]

config = IterativeSummarizerConfig(
    contents=test_docs,
    #aug_llm_configs=aug_llm_configs
)

agent = IterativeSummarizer(config)
async def main():   
    result = await agent.app.ainvoke({"contents": test_docs},config=agent.config.runnable_config)
    print(result)
if __name__ == "__main__":
    asyncio.run(main())