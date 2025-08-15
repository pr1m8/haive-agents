agents.reasoning_and_critique.lats.v2.agents
============================================

.. py:module:: agents.reasoning_and_critique.lats.v2.agents


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.lats.v2.agents.expansion_agent
   agents.reasoning_and_critique.lats.v2.agents.expansion_engine
   agents.reasoning_and_critique.lats.v2.agents.initial_agent
   agents.reasoning_and_critique.lats.v2.agents.initial_engine
   agents.reasoning_and_critique.lats.v2.agents.logger
   agents.reasoning_and_critique.lats.v2.agents.reflection_agent
   agents.reasoning_and_critique.lats.v2.agents.reflection_engine
   agents.reasoning_and_critique.lats.v2.agents.selection_agent
   agents.reasoning_and_critique.lats.v2.agents.selection_engine
   agents.reasoning_and_critique.lats.v2.agents.tool_node


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.lats.v2.agents.backpropagate
   agents.reasoning_and_critique.lats.v2.agents.create_lats
   agents.reasoning_and_critique.lats.v2.agents.evaluate_candidates
   agents.reasoning_and_critique.lats.v2.agents.execute_tool_calls
   agents.reasoning_and_critique.lats.v2.agents.process_expansion
   agents.reasoning_and_critique.lats.v2.agents.process_initial_response
   agents.reasoning_and_critique.lats.v2.agents.process_reflection
   agents.reasoning_and_critique.lats.v2.agents.should_continue_search
   agents.reasoning_and_critique.lats.v2.agents.should_execute_tools


Module Contents
---------------

.. py:function:: backpropagate(nodes: dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode], node_id: str, reward: float) -> dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode]

   Backpropagate reward up the tree.


   .. autolink-examples:: backpropagate
      :collapse:

.. py:function:: create_lats(tools: list[Any], max_depth: int = 5, max_rollouts: int = 10, n_candidates: int = 5, **kwargs) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create a Language Agent Tree Search system.


   .. autolink-examples:: create_lats
      :collapse:

.. py:function:: evaluate_candidates(state: haive.agents.reasoning_and_critique.lats.v2.state.LATSState) -> list[langgraph.types.Send]

   Send candidates for reflection.


   .. autolink-examples:: evaluate_candidates
      :collapse:

.. py:function:: execute_tool_calls(state: haive.agents.reasoning_and_critique.lats.v2.state.LATSState) -> dict[str, Any] | list[langgraph.types.Send]

   Execute tool calls for nodes that need them.


   .. autolink-examples:: execute_tool_calls
      :collapse:

.. py:function:: process_expansion(state: haive.agents.reasoning_and_critique.lats.v2.state.LATSState) -> dict[str, Any]

   Process expansion results into new nodes.


   .. autolink-examples:: process_expansion
      :collapse:

.. py:function:: process_initial_response(state: haive.agents.reasoning_and_critique.lats.v2.state.LATSState) -> dict[str, Any]

   Process initial response and create root node.


   .. autolink-examples:: process_initial_response
      :collapse:

.. py:function:: process_reflection(state: haive.agents.reasoning_and_critique.lats.v2.state.LATSState) -> dict[str, Any]

   Process reflection results and update node scores.


   .. autolink-examples:: process_reflection
      :collapse:

.. py:function:: should_continue_search(state: haive.agents.reasoning_and_critique.lats.v2.state.LATSState) -> str

   Decide whether to continue search or terminate.


   .. autolink-examples:: should_continue_search
      :collapse:

.. py:function:: should_execute_tools(state: haive.agents.reasoning_and_critique.lats.v2.state.LATSState) -> str

   Check if any nodes need tool execution.


   .. autolink-examples:: should_execute_tools
      :collapse:

.. py:data:: expansion_agent

.. py:data:: expansion_engine

.. py:data:: initial_agent

.. py:data:: initial_engine

.. py:data:: logger

.. py:data:: reflection_agent

.. py:data:: reflection_engine

.. py:data:: selection_agent

.. py:data:: selection_engine

.. py:data:: tool_node

