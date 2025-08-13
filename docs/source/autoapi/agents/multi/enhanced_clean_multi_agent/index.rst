
:py:mod:`agents.multi.enhanced_clean_multi_agent`
=================================================

.. py:module:: agents.multi.enhanced_clean_multi_agent

Enhanced Clean Multi-Agent Implementation using Agent[AugLLMConfig].

MultiAgent = Agent[AugLLMConfig] + agent coordination + state management.

This combines the enhanced agent pattern with the clean multi-agent approach:
- Uses Agent[AugLLMConfig] as the base
- Supports AgentNodeConfig for proper agent execution
- Maintains the engines dict pattern
- Provides multiple state management strategies


.. autolink-examples:: agents.multi.enhanced_clean_multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.enhanced_clean_multi_agent.ContainerMultiAgentState
   agents.multi.enhanced_clean_multi_agent.EnhancedMultiAgent
   agents.multi.enhanced_clean_multi_agent.MinimalMultiAgentState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContainerMultiAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_ContainerMultiAgentState {
        node [shape=record];
        "ContainerMultiAgentState" [label="ContainerMultiAgentState"];
        "haive.core.schema.state_schema.StateSchema" -> "ContainerMultiAgentState";
      }

.. autoclass:: agents.multi.enhanced_clean_multi_agent.ContainerMultiAgentState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMultiAgent {
        node [shape=record];
        "EnhancedMultiAgent" [label="EnhancedMultiAgent"];
        "haive.agents.simple.enhanced_simple_real.EnhancedAgentBase" -> "EnhancedMultiAgent";
      }

.. autoclass:: agents.multi.enhanced_clean_multi_agent.EnhancedMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MinimalMultiAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_MinimalMultiAgentState {
        node [shape=record];
        "MinimalMultiAgentState" [label="MinimalMultiAgentState"];
        "typing_extensions.TypedDict" -> "MinimalMultiAgentState";
      }

.. autoclass:: agents.multi.enhanced_clean_multi_agent.MinimalMultiAgentState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.enhanced_clean_multi_agent
   :collapse:
   
.. autolink-skip:: next
