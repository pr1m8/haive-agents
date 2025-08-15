agents.reasoning_and_critique.tot.modular.state
===============================================

.. py:module:: agents.reasoning_and_critique.tot.modular.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.state.ToTState


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.state.update_candidates


Module Contents
---------------

.. py:class:: ToTState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The state schema for Tree of Thoughts agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToTState
      :collapse:

   .. py:attribute:: answer
      :type:  str | None
      :value: None



   .. py:attribute:: best_candidate
      :type:  haive.agents.tot.modular.models.Candidate | None
      :value: None



   .. py:attribute:: candidates
      :type:  Annotated[list[haive.agents.tot.modular.models.Candidate], update_candidates]
      :value: None



   .. py:attribute:: current_seed
      :type:  haive.agents.tot.modular.models.Candidate | None
      :value: None



   .. py:attribute:: depth
      :type:  int
      :value: None



   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: problem
      :type:  str
      :value: None



   .. py:attribute:: scored_candidates
      :type:  Annotated[list[haive.agents.tot.modular.models.Candidate], update_candidates]
      :value: None



.. py:function:: update_candidates(existing: list[haive.agents.tot.modular.models.Candidate] | None = None, updates: list[haive.agents.tot.modular.models.Candidate] | str | list[dict[str, Any]] | None = None) -> list[haive.agents.tot.modular.models.Candidate]

   Update candidate list, handling special cases like clearing.

   :param existing: Current list of candidates
   :param updates: New candidates to add, or "clear" to empty the list

   :returns: Updated list of candidates


   .. autolink-examples:: update_candidates
      :collapse:

