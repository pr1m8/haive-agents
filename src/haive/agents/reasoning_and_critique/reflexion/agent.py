from collections.abc import Callable

from haive.agents.reflexion.config import ReflexionConfig
from haive.agents.reflexion.responder_with_retries import ResponderWithRetries
from haive.agents.reflexion.utils import _get_num_iterations
from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.branches import Branch
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import BaseTool, StructuredTool
from langgraph.graph import END, START
from langgraph.prebuilt import ToolNode
from langgraph.types import Command

# from haive_agents.reflexion.aug_llms import initial_answer_chain,revision_chain


@register_agent(ReflexionConfig)
class ReflexionAgent(Agent[ReflexionConfig]):
    """Agent that uses Reflexion to answer questions."""

    config: ReflexionConfig

    def __init__(self, config: ReflexionConfig = ReflexionConfig()):
        self.config = config
        self.responder = ResponderWithRetries(
            config.engines["responder"], config.attempts, name="responder"
        )
        self.revisor = ResponderWithRetries(
            config.engines["revisor"], config.attempts, name="revisor"
        )
        self.answer_writer = AugLLMConfig(model="gpt-4o", name="answer_writer")
        self.tool_node = self.create_tool_node(config.tools)
        self.event_loop_branch = Branch(
            function=lambda state: _get_num_iterations(state) > self.config.max_iterations,
            destinations={True: "end", False: "execute_tools"},
        )
        super().__init__(config)

    def create_tool_node(self, tools: list[BaseTool | Callable]) -> ToolNode:
        """Create a tool node from a list of tools.

        Args:
            tools: list of tools to create a tool node from
        Returns:
           ToolNode: a tool node from the list of tools
        """
        tool_node_tools = []
        for tool in self.config.tools:
            for model in self.config.models:
                tool_node_tools.append(StructuredTool.from_function(tool, name=model.__name__))
        return ToolNode(tools=tool_node_tools)

    def final_answer(self, state: dict):
        """Final answer tool."""
        prompt = PromptTemplate.from_template(
            """Given the folllowing converstaion, and user request, write out the final response.
            Conversation:
            {conversation}
            """
        )
        self.answer_writer.prompt_template = prompt
        aug_llm = self.answer_writer.create_runnable()
        # Handle both dict and model cases
        if hasattr(state, "model_dump") and callable(getattr(state, "model_dump")):
            conversation_data = state.model_dump()  # type: ignore
        elif isinstance(state, dict):
            conversation_data = state
        else:
            conversation_data = dict(state) if hasattr(state, "__dict__") else {}
        response = aug_llm.invoke(input={"conversation": conversation_data})

        return Command(update={"answer": response})

    def setup_workflow(self) -> None:
        """Setup the reflexion workflow graph."""
        if not hasattr(self, "graph") or self.graph is None:
            # Initialize graph if not already done
            from langgraph.graph import StateGraph

            self.graph = StateGraph(dict)  # Use dict for now

        self.graph.add_node("draft", self.responder.respond)
        self.graph.add_edge(START, "draft")
        self.graph.add_node("tools", self.tool_node)
        self.graph.add_edge("draft", "tools")
        self.graph.add_node("revision", self.revisor.respond)
        self.graph.add_node("final_answer", self.final_answer)
        self.graph.add_edge("tools", "revision")
        self.graph.add_edge("final_answer", END)

        # Create a simple condition function for LangGraph
        def should_continue(state):
            iterations = _get_num_iterations(state)
            return "end" if iterations > self.config.max_iterations else "execute_tools"

        self.graph.add_conditional_edges(
            "revision", should_continue, {"execute_tools": "tools", "end": "final_answer"}
        )
