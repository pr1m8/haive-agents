from typing import Annotated, List, Literal, TypedDict,Dict
from haive.core.engine.agent.agent import AgentConfig,Agent,register_agent
from haive.core.engine.aug_llm import AugLLMConfig,compose_runnable
from pydantic import BaseModel,Field
from agents.document_agents.summarizer.map_branch.state import SummaryState
from agents.document_agents.summarizer.map_branch.engines import map_aug_llm_config,reduce_augllm_config
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain.chains.combine_documents.reduce import (
    acollapse_docs,
    split_list_of_docs,
)
from langgraph.constants import Send
from langgraph.graph import END, START, StateGraph
import operator
import openai
from agents.document_agents.summarizer.map_branch.config import SummarizerAgentConfig
from langgraph.types import Command,Send
from haive.core.utils.doc_utils import clean_and_format_text 
import asyncio
import re
"""
1638, in _request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': "Invalid 'messages[0].content': string too long. Expected a string with maximum length 1048576, but got a string with length 1123800 instead.", 'type': 'invalid_request_error', 'param': 'messages[0].content', 'code': 'string_above_max_length'}}
During task with name 'generate_summary' and id '45f607c2-df38-a452-2686-e432a7583e3f'
(.venv) will@Williams-Air-2 hive_v8 % xxxxxxxxxc
"""



@register_agent(SummarizerAgentConfig)
class SummarizerAgent(Agent[SummarizerAgentConfig]):
    """SummarizerAgent is a class that summarizes a list of documents."""
    def __init__(self, config: SummarizerAgentConfig=SummarizerAgentConfig()):
        
        """Initialize the SummarizerAgent with model and token constraints."""
        #self.llm = AzureChatOpenAI(model="gpt-4o")
        self.token_max = config.token_max  
        self.map_chain = compose_runnable(map_aug_llm_config)
        self.reduce_chain = compose_runnable(reduce_augllm_config)
        #self.graph = None

        # Initialize prompts and chains
        #self.initialize_prompts()
        #self.initialize_chains()
        #self.setup_workflow()
        super().__init__(config)
    

    

    def setup_workflow(self):
        """Construct the StateGraph for the summarizer workflow."""
        #graph = StateGraph(SummaryState)
        #self.graph = StateGraph(self.state_schema)
        self.graph.add_node("generate_summary", self.generate_summary)
        self.graph.add_node("collect_summaries", self.collect_summaries)
        self.graph.add_node("collapse_summaries", self.collapse_summaries)
        self.graph.add_node("generate_final_summary", self.generate_final_summary)
        
        self.graph.add_conditional_edges(START, self.map_summaries, ["generate_summary"])
        self.graph.add_edge("generate_summary", "collect_summaries")
        self.graph.add_conditional_edges("collect_summaries", self.should_collapse)
        self.graph.add_conditional_edges("collapse_summaries", self.should_collapse)
        self.graph.add_edge("generate_final_summary", END)

        #self.graph = graph

    async def generate_summary(self, state: SummaryState):
        """Generate a summary for a single document."""
        try:
            # Try the normal approach first
            response = await self.map_chain.ainvoke(state["content"])
            return {"summaries": [response]}
        except Exception as e:
            # If we get an error (like token limit), handle it by recursively splitting
            error_str = str(e)
            print(f"Error in generate_summary: {error_str}")
            
            # Check if this is a token limit error or similar content length issue - will fix eventually.
            if "string too long" in error_str or "token limit" in error_str or "maximum context length" in error_str:
                from langchain_text_splitters import RecursiveCharacterTextSplitter
                
                # Create a text splitter with reasonable chunk sizes
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=4000,  # Smaller chunks to ensure they fit within token limits
                    chunk_overlap=200,
                    length_function=lambda text: self.config.aug_llm_configs["map_chain"].llm_config.instantiate_llm().get_num_tokens(text)
                )
                
                # Split the content into manageable chunks
                if isinstance(state["content"], str):
                    chunks = text_splitter.split_text(state["content"])
                else:
                    # If it's a Document object
                    chunks = text_splitter.split_documents([state["content"]])
                    chunks = [doc.page_content for doc in chunks]
                
                print(f"Split content into {len(chunks)} chunks")
                
                # Process each chunk separately
                chunk_summaries = []
                for i, chunk in enumerate(chunks):
                    try:
                        print(f"Processing chunk {i+1}/{len(chunks)}")
                        chunk_summary = await self.map_chain.ainvoke(chunk)
                        chunk_summaries.append(chunk_summary)
                    except Exception as chunk_error:
                        print(f"Error processing chunk {i+1}: {str(chunk_error)}")
                        # For really problematic chunks, just make a short summary note
                        chunk_summaries.append(f"[Chunk {i+1} was too complex to summarize]")
                
                # If we have multiple chunk summaries, we need to combine them
                if len(chunk_summaries) > 1:
                    combined_summary = await self.reduce_chain.ainvoke("\n\n".join(chunk_summaries))
                    return {"summaries": [combined_summary]}
                elif len(chunk_summaries) == 1:
                    return {"summaries": [chunk_summaries[0]]}
                else:
                    return {"summaries": ["The document was too large to process and could not be summarized."]}
            else:
                # For other types of errors, just return an error message
                return Command(update={"summaries": [f"Error generating summary: {error_str}"]})

    def map_summaries(self, state: SummaryState):
        """Map out over documents to generate summaries."""
        return [
            Send("generate_summary", {"content": content})
            for content in state.contents
        ]

    def collect_summaries(self, state: SummaryState):
        """Collect summaries into a list of documents."""
        #print(state["summaries"])
        return Command(update={"collapsed_summaries": [
                Document(summary) for summary in state.summaries
            ]})

    async def collapse_summaries(self, state: SummaryState):
        """Collapse summaries if their total token count exceeds the limit."""
        doc_lists = split_list_of_docs(
            state["collapsed_summaries"], self.length_function, self.token_max
        )
        results = []
        for doc_list in doc_lists:
            results.append(await acollapse_docs(doc_list, self.reduce_chain.ainvoke))

        return Command(update={"collapsed_summaries": results})

    def should_collapse(self, state: SummaryState) -> Literal["collapse_summaries", "generate_final_summary"]:
        """Determine whether to collapse summaries further."""
        num_tokens = self.length_function(state.collapsed_summaries)
        if num_tokens > self.token_max:
            return "collapse_summaries"
        else:
            return "generate_final_summary"

    async def generate_final_summary(self, state: SummaryState):
        """Generate the final summary from collapsed summaries."""
        response = await self.reduce_chain.ainvoke(state.collapsed_summaries)
        return Command(update={"final_summary": response})

    def length_function(self, documents: List[Document]) -> int:
        """Calculate the total token count for a set of documents."""
        #llm = self.aug_llm_configs["reduce_chain"].llm_config.instantiate_llm()
        #print(llm)
        #print(documents)
        return sum(self.config.engines["reduce_chain"].llm_config.instantiate_llm(model="gpt-4o").get_num_tokens(doc.page_content) for doc in documents)

    async def arun(self, contents: List[str]) -> str:
            """Run the summarization workflow and return the final summary."""
            #app = self.graph.compile()
            async for output in self.app.astream({"contents": contents},config=self.runnable_config,debug=True):
                print(output)
            return self.app

def build_agent() -> SummarizerAgent:
    return SummarizerAgent(SummarizerAgentConfig())




async def main():
    summarizer = SummarizerAgent(SummarizerAgentConfig())
    #summarizer.setup_workflow()
    from langchain_community.document_loaders import WebBaseLoader
    documents = WebBaseLoader("https://en.wikipedia.org/wiki/Differential_geometry").load()
    
    print(summarizer.length_function(documents))
    documents = [Document(page_content=clean_and_format_text(d.page_content),metadata=d.metadata) for d in documents]
    await summarizer.arun(documents)
    #print(documents)
    #from langchain_community.document_transformers import Html2TextTransformer,MarkdownifyTransformer,BeautifulSoupTransformer,\
        #DoctranQATransformer,DoctranPropertyExtractor,OpenAIMetadataTagger,LongContextReorder,NucliaTextTransformer
    

if __name__ == "__main__":
    asyncio.run(main()) 

