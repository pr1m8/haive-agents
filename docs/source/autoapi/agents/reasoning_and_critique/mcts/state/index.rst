agents.reasoning_and_critique.mcts.state
========================================

.. py:module:: agents.reasoning_and_critique.mcts.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.mcts.state.TreeState


Module Contents
---------------

.. py:class:: TreeState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State schema for MCTS Agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TreeState
      :collapse:

   .. py:attribute:: input
      :type:  str
      :value: None



   .. py:attribute:: root
      :type:  haive.agents.reasoning_and_critique.mcts.models.TreeNode
      :value: None



