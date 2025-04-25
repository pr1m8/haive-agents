from agents.document_agents.kg.kg_iterative_refinement.config import IterativeGraphTransformerConfig      
from agents.document_agents.kg.kg_iterative_refinement.state import IterativeGraphTransformerState
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command
from langchain_community.graphs.graph_document import GraphDocument
from haive.core.engine.agent.agent import Agent, register_agent
from agents.document_agents.kg.kg_iterative_refinement.utils import replace_empty_placeholders
from src.haive.flstaesr_backup.transform.graph_transform.base import GraphTransformer
from langgraph.graph import START,END
@register_agent(IterativeGraphTransformerConfig)
class IterativeGraphTransformer(Agent[IterativeGraphTransformerConfig]):
    """
    An agent that transforms a graph document iteratively.
    """
    def __init__(self, config: IterativeGraphTransformerConfig=IterativeGraphTransformerConfig()):
        #self.graph_transformer = GraphTransformer()
        self.llm_graph_transformer = GraphTransformer()
        
        super().__init__(config)
    

    # We define functions for each node, including a node that generates
    # the initial summary:
    def generate_initial_summary(self, state: IterativeGraphTransformerState, config: RunnableConfig):
        doc = state.contents[0]
        if isinstance(doc, str):
            doc = Document(page_content=doc)
        elif isinstance(doc, dict) and "page_content" in doc:
            doc = Document(**doc)

        print(f"Generating initial summary for document: {doc.page_content}")
        graph_doc = self.llm_graph_transformer.transform_documents(
            documents=[doc],
            strict_mode=True,
            ignore_tool_usage=True,
        )
        return Command(update={"graph_doc": graph_doc[0], "index": 1})


    # And a node that refines the summary based on the next document
        
    def refine_summary(self, state: IterativeGraphTransformerState, config: RunnableConfig):
        content = state.contents[state.index]

        # --- Normalize to Document ---
        if isinstance(content, str):
            content = Document(page_content=content)
        elif isinstance(content, dict) and "page_content" in content:
            content = Document(**content)
        elif not isinstance(content, Document):
            raise TypeError(f"Invalid content type: {type(content)}")

        print(f"DEBUG: content TYPE -> {type(content)}")
        print(f"DEBUG: content -> {content.page_content[:100]}")

        from langchain_core.prompts import PromptTemplate

        refine_template = PromptTemplate.from_template("""\
        Produce a final graph.

        Existing graph up to this point:
        {existing_answer}

        New context:
        ------------
        {context}
        ------------

        Given the new context, refine the original graph.
        """).format(existing_answer=str(state.graph_doc), context=content.page_content)

        refine_template = replace_empty_placeholders(refine_template)

        graph_doc = self.llm_graph_transformer.transform_documents(
            documents=[content],
            strict_mode=True,
            ignore_tool_usage=True,
            additional_instructions=refine_template,
        )

        return Command(update={"graph_doc": graph_doc[0], "index": state.index + 1})


    def setup_workflow(self):
        self.graph.add_node("generate_initial_summary", self.generate_initial_summary)
        self.graph.add_node("refine_summary", self.refine_summary)

        self.graph.add_edge(START, "generate_initial_summary")
        self.graph.add_conditional_edges("generate_initial_summary", self.state_schema.should_refine)
        self.graph.add_conditional_edges("refine_summary", self.state_schema.should_refine)

from langchain_core.documents import Document
test_docs = ["Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.",
        "Marie Curie was the first woman to win a Nobel Prize. Her husband, Pierre Curie, was a co-winner of her first Nobel Prize.",
        "Poland is a country in Europe. Poland was first established as a unified state in 966, and its capital is Warsaw.",
        "Warsaw is the capital and largest city of Poland. It is located on the Vistula River.",
        "Marie Curie discovered the elements polonium and radium. She named polonium after her native country Poland.",
        "Pierre Curie was a French physicist who made pioneering contributions to crystallography, magnetism, and radioactivity."]

config = IterativeGraphTransformerConfig(
    contents=test_docs,
    #aug_llm_configs=aug_llm_configs
)

agent = IterativeGraphTransformer(config)
def main():   
    result = agent.app.invoke({"contents": test_docs},config=agent.config.runnable_config)
    print(result)

main()