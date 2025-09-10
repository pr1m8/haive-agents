"""ReactAgent V4 - Simple loop pattern with proper inheritance.

Minimal ReactAgent that:
1. Inherits properly from SimpleAgentV3
2. Implements tool_node back to agent_node loop
3. No fancy features, just the core pattern
"""

import contextlib
import logging
from typing import TYPE_CHECKING

from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langgraph.graph import END

from haive.agents.simple.agent_v3 import SimpleAgentV3

if TYPE_CHECKING:
    pass


logger = logging.getLogger(__name__)


class ReactAgentV4(SimpleAgentV3):
    """ReactAgent with simple looping behavior.

    Inherits all SimpleAgentV3 features and modifies graph to loop:
    - tool_node goes back to agent_node (not END)
    - parse_output goes back to agent_node (not END)
    """

    def build_graph(self) -> BaseGraph:
        """Build graph with ReAct looping pattern."""
        # Get the base graph from SimpleAgentV3
        graph = super().build_graph()

        # Check if we have an engine
        main_engine = self.engine
        if not main_engine:
            return graph

        # Modify edges for looping
        if "tool_node" in graph.nodes:
            with contextlib.suppress(Exception):
                graph.remove_edge("tool_node", END)
            graph.add_edge("tool_node", "agent_node")
            if self.debug:
                logger.debug("Added tool_node to agent_node loop")

        if "parse_output" in graph.nodes:
            with contextlib.suppress(Exception):
                graph.remove_edge("parse_output", END)
            graph.add_edge("parse_output", "agent_node")
            if self.debug:
                logger.debug("Added parse_output to agent_node loop")

        return graph


# Import Agent for model_rebuild
from haive.agents.base.enhanced_agent import Agent

# Rebuild model to resolve forward references
ReactAgentV4.model_rebuild()
