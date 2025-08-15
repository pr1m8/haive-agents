agents.reasoning_and_critique.lats.v2.models
============================================

.. py:module:: agents.reasoning_and_critique.lats.v2.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.v2.models.CandidateActions
   agents.reasoning_and_critique.lats.v2.models.Reflection
   agents.reasoning_and_critique.lats.v2.models.SelectionDecision
   agents.reasoning_and_critique.lats.v2.models.TreeNode


Module Contents
---------------

.. py:class:: CandidateActions(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from expansion agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateActions
      :collapse:

   .. py:attribute:: candidates
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: Reflection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from reflection agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Reflection
      :collapse:

   .. py:attribute:: found_solution
      :type:  bool
      :value: None



   .. py:property:: normalized_score
      :type: float



   .. py:attribute:: reflections
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



.. py:class:: SelectionDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from selection agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectionDecision
      :collapse:

   .. py:attribute:: selected_node_id
      :type:  str
      :value: None



   .. py:attribute:: should_terminate
      :type:  bool
      :value: None



   .. py:attribute:: termination_reason
      :type:  str | None
      :value: None



.. py:class:: TreeNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Non-recursive tree node for LATS.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TreeNode
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: uct_score(parent_visits: int, exploration_weight: float = 1.0) -> float

      Calculate Upper Confidence Bound for tree search.


      .. autolink-examples:: uct_score
         :collapse:


   .. py:attribute:: action
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: children_ids
      :type:  list[str]
      :value: None



   .. py:attribute:: depth
      :type:  int
      :value: 1



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: is_solved
      :type:  bool
      :value: False



   .. py:attribute:: is_terminal
      :type:  bool
      :value: False



   .. py:attribute:: messages
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: parent_id
      :type:  str | None
      :value: None



   .. py:attribute:: reflection_score
      :type:  float
      :value: 0.0



   .. py:attribute:: reflection_text
      :type:  str
      :value: ''



   .. py:attribute:: tool_response
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: value
      :type:  float
      :value: 0.0



   .. py:attribute:: visits
      :type:  int
      :value: 0



