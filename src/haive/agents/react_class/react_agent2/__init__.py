"""Module exports - Simplified to fix critical blocking error.

This module has been simplified to resolve the critical import error
that was blocking 62 modules. Complex import chains have been commented
out to focus on core functionality.
"""

from haive.agents.react_class.react_agent2.advanced_agent3 import (
    AdvancedReactAgent,
    AdvancedReactAgentConfig,
    add_tool,
)

from haive.agents.react_class.react_agent2.agent2 import (
    MessageNormalizingToolNode,
    ReactAgent,
    chat,
    create_react_agent,
    has_tool_calls,
    run,
    setup_workflow,
    should_use_tools,
    stream,
    structured_output_node
)

from haive.agents.react_class.react_agent2.agent3 import (
    ReactAgent as ReactAgent3,
    ReactAgentConfig,
    ReactAgentState,
    from_tools,
    search,
)

from haive.agents.react_class.react_agent2.config import (
    ReactAgentConfig as ReactAgentConfigV1,
    from_scratch
)

# Complex import chains commented out to resolve critical blocking error:
# - example2, example3, models, nodes, state2, config2, debug, dynamic_agent
# These can be uncommented and fixed individually as needed

__all__ = [
    "AdvancedReactAgent",
    "AdvancedReactAgentConfig", 
    "add_tool",
    "MessageNormalizingToolNode",
    "ReactAgent",
    "ReactAgent3",
    "ReactAgentConfig",
    "ReactAgentConfigV1",
    "ReactAgentState",
    "chat",
    "create_react_agent",
    "from_scratch",
    "from_tools",
    "has_tool_calls",
    "run",
    "search",
    "setup_workflow",
    "should_use_tools",
    "stream",
    "structured_output_node",
]