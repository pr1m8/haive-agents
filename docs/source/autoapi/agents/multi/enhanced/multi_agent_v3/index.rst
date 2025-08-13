
:py:mod:`agents.multi.enhanced.multi_agent_v3`
==============================================

.. py:module:: agents.multi.enhanced.multi_agent_v3

Enhanced MultiAgent V3 - Full feature implementation with generic typing support.

This version provides advanced multi-agent orchestration with generic typing support,
performance tracking, and enhanced debugging capabilities. It follows the V3 pattern
established by SimpleAgentV3 and ReactAgent.

**Current Status**: This is the **V3 enhanced implementation** with advanced features.
Use this when you need generic typing support, performance tracking, or complex routing
patterns. For simpler use cases, use the default MultiAgent. For the latest features,
use MultiAgent.

Key Features:
- **Generic typing**: MultiAgent[AgentsT] for type-safe agent collections
- **Performance tracking**: Adaptive routing based on agent performance metrics
- **Rich debugging**: Comprehensive observability and capabilities display
- **Multi-engine coordination**: Support for multiple LLM engines
- **Advanced routing**: Conditional, branching, and adaptive patterns
- **V3 consistency**: Follows patterns from SimpleAgentV3 and ReactAgent

This version combines the best features from clean.py and enhanced_multi_agent_standalone.py:
- Production-ready coordination from clean.py
- Generic typing and performance features from standalone
- Full integration with enhanced base Agent class
- V3 pattern consistency with SimpleAgent V3 and ReactAgent V3

.. rubric:: Examples

With generic typing for type safety::

    from typing import Dict, Any
    from haive.agents.multi.enhanced_multi_agent_v3 import EnhancedMultiAgent

    # Type-safe agent dictionary
    agents: Dict[str, SimpleAgent] = {
        "analyzer": SimpleAgent(name="analyzer"),
        "processor": SimpleAgent(name="processor")
    }

    # Generic typing ensures type safety
    multi: EnhancedMultiAgent[Dict[str, SimpleAgent]] = EnhancedMultiAgent(
        name="typed_workflow",
        agents=agents,
        performance_mode=True
    )

With performance tracking::

    # Enable adaptive routing based on performance
    multi = EnhancedMultiAgent(
        name="adaptive_workflow",
        agents={"fast": fast_agent, "accurate": accurate_agent},
        execution_mode="branch",
        performance_mode=True,
        adaptation_rate=0.2
    )

    # System learns which agent performs best for different tasks
    result = await multi.arun("Process this data")

.. seealso::

   - :class:`haive.agents.multi.enhanced_multi_agent_v4.MultiAgent`: Latest V4
   - :class:`haive.agents.multi.clean.MultiAgent`: Current default
   - :class:`haive.agents.simple.agent_v3.SimpleAgentV3`: V3 pattern reference


.. autolink-examples:: agents.multi.enhanced.multi_agent_v3
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.enhanced.multi_agent_v3.EnhancedMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMultiAgent {
        node [shape=record];
        "EnhancedMultiAgent" [label="EnhancedMultiAgent"];
        "haive.agents.base.agent.Agent" -> "EnhancedMultiAgent";
        "Generic[AgentsT]" -> "EnhancedMultiAgent";
      }

.. autoclass:: agents.multi.enhanced.multi_agent_v3.EnhancedMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.enhanced.multi_agent_v3
   :collapse:
   
.. autolink-skip:: next
