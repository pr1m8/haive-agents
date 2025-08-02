"""Module exports."""

from operator import add

from haive.agents.chain.chain_examples import (
    example_engines_as_nodes,
    example_incremental_building,
    example_mapped_flow,
    example_nested_chains,
    example_rag_router_simplified,
    example_sequential_mixed,
)
from haive.agents.chain.examples import (
    StrategyDecision,
    create_agentic_router_declarative,
    create_complex_flow_from_spec,
    create_plan,
    create_query_planning_declarative,
    create_rag_with_fallback,
    create_self_reflective_declarative,
    execute_sub_query,
    finalize_answer,
    improve_answer,
    reflect_and_critique,
    synthesize_results,
)
from haive.agents.chain.examples_simple import (
    example_basic,
    example_direct,
    example_incremental,
    example_mixed,
    example_rag_router,
    example_routing,
    formatter,
)
from haive.agents.chain.multi_integration import (
    ChainMultiAgent,
    ChainNodeWrapper,
    ExtendedExecutionMode,
    build_graph,
    chain_multi,
    chain_to_multi,
    conditional_multi,
    from_chain,
    from_nodes,
    multi_to_chain,
    sequential_multi,
)

# TEMPORARILY DISABLED - ignoring chain agent imports to focus on other issues
# from haive.agents.chain.chain_agent_simple import (
#     ChainAgent,
#     FlowBuilder,
#     flow,
#     flow_with_edges,
# )

# Create placeholder classes for missing exports
class ChainAgent:
    """Placeholder for ChainAgent - temporarily disabled."""
    pass

class FlowBuilder:
    """Placeholder for FlowBuilder - temporarily disabled."""
    pass

def flow(*args, **kwargs):
    """Placeholder for flow function - temporarily disabled."""
    pass

def flow_with_edges(*args, **kwargs):
    """Placeholder for flow_with_edges function - temporarily disabled."""
    pass

def branch(*args, **kwargs):
    """Placeholder for branch function - not implemented."""
    pass

def merge_to(*args, **kwargs):
    """Placeholder for merge_to function - not implemented."""
    pass

__all__ = [
    "ChainAgent",
    "ChainMultiAgent",
    "ChainNodeWrapper",
    "ExtendedExecutionMode",
    "FlowBuilder",
    "StrategyDecision",
    "add",
    "branch",
    "build_graph",
    "chain_multi",
    "chain_to_multi",
    "conditional_multi",
    "create_agentic_router_declarative",
    "create_complex_flow_from_spec",
    "create_plan",
    "create_query_planning_declarative",
    "create_rag_with_fallback",
    "create_self_reflective_declarative",
    "example_basic",
    "example_direct",
    "example_engines_as_nodes",
    "example_incremental",
    "example_incremental_building",
    "example_mapped_flow",
    "example_mixed",
    "example_nested_chains",
    "example_rag_router",
    "example_rag_router_simplified",
    "example_routing",
    "example_sequential_mixed",
    "execute_sub_query",
    "finalize_answer",
    "flow",
    "flow_with_edges",
    "formatter",
    "from_chain",
    "from_nodes",
    "improve_answer",
    "merge_to",
    "multi_to_chain",
    "reflect_and_critique",
    "sequential_multi",
    "synthesize_results",
]
