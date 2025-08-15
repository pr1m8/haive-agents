agents.reasoning_and_critique.lats.v2.state
===========================================

.. py:module:: agents.reasoning_and_critique.lats.v2.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.v2.state.LATSState


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.lats.v2.state.update_nodes


Module Contents
---------------

.. py:class:: LATSState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State for Language Agent Tree Search.


   .. autolink-examples:: LATSState
      :collapse:

   .. py:method:: get_best_leaf_to_expand() -> str | None

      Find the best leaf node to expand using UCT.


      .. autolink-examples:: get_best_leaf_to_expand
         :collapse:


   .. py:method:: get_node(node_id: str) -> haive.agents.reasoning_and_critique.lats.v2.models.TreeNode | None

      Get a node by ID.


      .. autolink-examples:: get_node
         :collapse:


   .. py:attribute:: best_solution_id
      :type:  str | None
      :value: None



   .. py:attribute:: candidate_nodes
      :type:  list[haive.agents.reasoning_and_critique.lats.v2.models.TreeNode]
      :value: None



   .. py:attribute:: current_node_id
      :type:  str | None
      :value: None



   .. py:property:: current_trajectory
      :type: str


      Get trajectory to current node for prompts.

      .. autolink-examples:: current_trajectory
         :collapse:


   .. py:attribute:: exploration_weight
      :type:  float
      :value: None



   .. py:property:: input_query
      :type: str


      Extract query from first human message.

      .. autolink-examples:: input_query
         :collapse:


   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: max_rollouts
      :type:  int
      :value: None



   .. py:attribute:: n_candidates
      :type:  int
      :value: None



   .. py:attribute:: nodes
      :type:  Annotated[dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode], update_nodes]
      :value: None



   .. py:attribute:: rollouts_completed
      :type:  Annotated[int, operator.add]
      :value: None



   .. py:attribute:: root_id
      :type:  str | None
      :value: None



   .. py:property:: should_continue_search
      :type: bool


      Determine if search should continue.

      .. autolink-examples:: should_continue_search
         :collapse:


   .. py:attribute:: should_terminate
      :type:  bool
      :value: None



   .. py:attribute:: termination_reason
      :type:  str | None
      :value: None



   .. py:attribute:: tools
      :type:  list[dict[str, Any]]
      :value: None



   .. py:property:: tree_statistics
      :type: str


      Summary of tree search progress.

      .. autolink-examples:: tree_statistics
         :collapse:


.. py:function:: update_nodes(existing: dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode] | None = None, updates: dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode] | None = None) -> dict[str, haive.agents.reasoning_and_critique.lats.v2.models.TreeNode]

   Custom reducer for tree nodes.


   .. autolink-examples:: update_nodes
      :collapse:

