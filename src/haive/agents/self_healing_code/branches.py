from langgraph.graph import END

from .state import SelfHealingCodeState


def error_router(state: SelfHealingCodeState):
    """Error Router.

    Args:
        state: [TODO: Add description]
    """
    if state.error:
        return "bug_report_node"
    return END


def memory_filter_router(state: SelfHealingCodeState):
    """Memory Filter Router.

    Args:
        state: [TODO: Add description]
    """
    if state.memory_search_results:
        return "memory_filter_node"
    return "memory_generation_node"


def memory_generation_router(state: SelfHealingCodeState):
    """Memory Generation Router.

    Args:
        state: [TODO: Add description]
    """
    if state.memory_ids_to_update:
        return "memory_modification_node"
    return "memory_generation_node"


def memory_update_router(state: SelfHealingCodeState):
    """Memory Update Router.

    Args:
        state: [TODO: Add description]
    """
    if state.memory_ids_to_update:
        return "memory_modification_node"
    return "code_update_node"
