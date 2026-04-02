"""LangGraph Platform graph entry points for haive-agents.

This module exposes all workable agent graphs as callable factories for
LangGraph Platform (langgraph.json). Each function returns a compiled
LangGraph StateGraph served via ``langgraph dev`` or LangGraph Cloud.
"""

import logging

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _aug(temperature=0.7, system_message="You are a helpful AI assistant."):
    from haive.core.engine.aug_llm import AugLLMConfig
    return AugLLMConfig(temperature=temperature, system_message=system_message)


# ---------------------------------------------------------------------------
# Foundation Agents
# ---------------------------------------------------------------------------

def simple_agent():
    """Basic conversational agent with hooks and structured output."""
    from haive.agents.simple.agent import SimpleAgent
    return SimpleAgent(name="simple_agent", engine=_aug()).compile()


def react_agent():
    """ReAct agent with reasoning + acting loop and tool-use."""
    from haive.agents.react.agent import ReactAgent
    return ReactAgent(
        name="react_agent",
        engine=_aug(0.3, "You are a helpful assistant that can use tools."),
    ).compile()


# ---------------------------------------------------------------------------
# Multi-Agent Orchestration
# ---------------------------------------------------------------------------

def multi_agent_sequential():
    """Sequential multi-agent pipeline (agent A -> B -> C)."""
    from haive.agents.simple.agent import SimpleAgent
    from haive.agents.multi.agent import MultiAgent

    agents = [
        SimpleAgent(name="planner", engine=_aug(0.3, "You create concise plans.")),
        SimpleAgent(name="executor", engine=_aug(0.5, "You execute plans step by step.")),
        SimpleAgent(name="reviewer", engine=_aug(0.3, "You review work for quality.")),
    ]
    return MultiAgent(name="sequential_pipeline", agents=agents, execution_mode="sequential").compile()


# ---------------------------------------------------------------------------
# Supervision
# ---------------------------------------------------------------------------

def supervisor():
    """Dynamic supervisor that routes tasks to sub-agents."""
    from haive.agents.dynamic_supervisor.agent import DynamicSupervisorAgent
    return DynamicSupervisorAgent(
        name="supervisor",
        engine=_aug(0.3, "You are a supervisor that routes tasks to appropriate agents."),
    ).compile()


# ---------------------------------------------------------------------------
# RAG Agents
# ---------------------------------------------------------------------------

def rag_agent():
    """Base retrieval-augmented generation agent (HuggingFace embeddings)."""
    from haive.agents.rag.base.agent import BaseRAGAgent
    return BaseRAGAgent(name="rag_agent").compile()


def simple_rag():
    """Simple RAG = retriever + answer agent in sequence."""
    from haive.agents.rag.simple.agent import SimpleRAGAgent
    return SimpleRAGAgent(name="simple_rag").compile()


def dynamic_rag():
    """Dynamic RAG with multiple retrieval sources."""
    from haive.agents.rag.dynamic.agent import DynamicRAGAgent
    return DynamicRAGAgent(name="dynamic_rag").compile()


def llm_rag():
    """LLM-based RAG agent."""
    from haive.agents.rag.llm_rag.agent import LLMRAGAgent
    return LLMRAGAgent(name="llm_rag").compile()


# ---------------------------------------------------------------------------
# Planning & Execution
# ---------------------------------------------------------------------------

def plan_and_execute():
    """Plan-and-execute agent: creates a plan then executes each step."""
    from haive.agents.planning.plan_and_execute.v2.agent import PlanAndExecuteAgent
    from haive.agents.simple.agent import SimpleAgent

    planner = SimpleAgent(name="planner", engine=_aug(0.3, "You create detailed step-by-step plans."))
    executor = SimpleAgent(name="executor", engine=_aug(0.5, "You execute plan steps carefully."))
    return PlanAndExecuteAgent(
        name="plan_and_execute", agents=[planner, executor], execution_mode="sequential"
    ).compile()


def llm_compiler():
    """LLM Compiler: parallel tool-call planning and execution."""
    from haive.agents.planning.llm_compiler.agent import LLMCompilerAgent
    from haive.agents.planning.llm_compiler.config import LLMCompilerAgentConfig
    config = LLMCompilerAgentConfig(name="llm_compiler")
    return LLMCompilerAgent(config).app


# ---------------------------------------------------------------------------
# Reasoning & Critique
# ---------------------------------------------------------------------------

def reflection_agent():
    """Self-reflection agent that generates then improves its answer."""
    from haive.agents.reasoning_and_critique.reflection.agent import ReflectionAgent
    return ReflectionAgent(
        name="reflection_agent",
        engine=_aug(0.5, "You are a thoughtful assistant that reflects on your answers."),
    ).compile()


def reasoning_system():
    """Logic-based reasoning system with multiple engines."""
    from haive.agents.reasoning_and_critique.logic.agent import ReasoningSystem
    return ReasoningSystem(name="reasoning_system").compile()


def self_discover_selector():
    """Self-Discover selector: picks relevant reasoning modules."""
    from haive.agents.reasoning_and_critique.self_discover.selector.agent import SelectorAgent
    return SelectorAgent(name="selector").compile()


def self_discover_adapter():
    """Self-Discover adapter: adapts modules to the task."""
    from haive.agents.reasoning_and_critique.self_discover.adapter.agent import AdapterAgent
    return AdapterAgent(name="adapter").compile()


def self_discover_structurer():
    """Self-Discover structurer: structures the reasoning plan."""
    from haive.agents.reasoning_and_critique.self_discover.structurer.agent import StructurerAgent
    return StructurerAgent(name="structurer").compile()


def self_discover_executor():
    """Self-Discover executor: executes the structured reasoning plan."""
    from haive.agents.reasoning_and_critique.self_discover.executor.agent import ExecutorAgent
    return ExecutorAgent(name="executor").compile()


# ---------------------------------------------------------------------------
# Conversation
# ---------------------------------------------------------------------------

def collaborative_conversation():
    """Collaborative multi-agent conversation."""
    from haive.agents.conversation.collaberative.agent import CollaborativeConversation
    from haive.agents.simple.agent import SimpleAgent

    participants = {
        "expert": SimpleAgent(name="expert", engine=_aug(0.3, "You are a domain expert.")),
        "critic": SimpleAgent(name="critic", engine=_aug(0.5, "You critically evaluate ideas.")),
    }
    return CollaborativeConversation(name="collab", participant_agents=participants).compile()


def debate_conversation():
    """Structured debate between agents."""
    from haive.agents.conversation.debate.agent import DebateConversation
    from haive.agents.simple.agent import SimpleAgent

    participants = {
        "pro": SimpleAgent(name="pro", engine=_aug(0.7, "You argue in favor of the proposition.")),
        "con": SimpleAgent(name="con", engine=_aug(0.7, "You argue against the proposition.")),
    }
    return DebateConversation(name="debate", participant_agents=participants).compile()


# ---------------------------------------------------------------------------
# Memory
# ---------------------------------------------------------------------------

def memory_agent():
    """Memory-enhanced agent with vector store + knowledge graph."""
    from haive.agents.memory.agent import MemoryAgent
    from haive.agents.memory.memory_utils import create_memory_vectorstore
    vector_store = create_memory_vectorstore()
    return MemoryAgent(
        name="memory_agent",
        engine=_aug(0.5, "You are a helpful assistant with long-term memory. Use save_memory to remember facts and recall_memories to retrieve them."),
        vector_store=vector_store,
    ).compile()


# ---------------------------------------------------------------------------
# Task Analysis
# ---------------------------------------------------------------------------

def task_analysis():
    """Task analysis and decomposition agent."""
    from haive.agents.task_analysis.agent import TaskAnalysisAgent
    return TaskAnalysisAgent(name="task_analysis").compile()


# ---------------------------------------------------------------------------
# RAG Variants (Advanced)
# ---------------------------------------------------------------------------

def step_back_rag():
    """Step-Back RAG: generates abstracted queries for better retrieval."""
    from haive.agents.rag.step_back.agent import StepBackRAGAgent
    return StepBackRAGAgent(name="step_back_rag").compile()


def flare_rag():
    """FLARE RAG: forward-looking active retrieval."""
    from haive.agents.rag.flare.agent import FLARERAGAgent
    return FLARERAGAgent(name="flare_rag").compile()


def multi_query_rag():
    """Multi-Query RAG: generates multiple query variants for retrieval."""
    from haive.agents.rag.multi_query.agent import MultiQueryRAGAgent
    return MultiQueryRAGAgent(name="multi_query_rag").compile()


def fusion_rag():
    """RAG Fusion: reciprocal rank fusion across multiple retrievals."""
    from haive.agents.rag.fusion.agent import RAGFusionAgent
    return RAGFusionAgent(name="fusion_rag").compile()


def speculative_rag():
    """Speculative RAG: hypothesis generation + parallel verification."""
    from haive.agents.rag.speculative.agent import SpeculativeRAGAgent
    return SpeculativeRAGAgent(name="speculative_rag").compile()


def document_grading_rag():
    """Document Grading RAG: grades retrieved documents for relevance."""
    from haive.agents.rag.document_grading.agent import DocumentGradingRAGAgent
    return DocumentGradingRAGAgent(name="document_grading_rag").compile()


def self_route_rag():
    """Self-Route RAG: analyzes query to choose optimal retrieval strategy."""
    from haive.agents.rag.self_route.agent import SelfRouteRAGAgent
    return SelfRouteRAGAgent(name="self_route_rag").compile()
