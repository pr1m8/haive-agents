
:py:mod:`agents.reasoning_and_critique.tot.modular.state`
=========================================================

.. py:module:: agents.reasoning_and_critique.tot.modular.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.state.ToTState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToTState:

   .. graphviz::
      :align: center

      digraph inheritance_ToTState {
        node [shape=record];
        "ToTState" [label="ToTState"];
        "pydantic.BaseModel" -> "ToTState";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.modular.state.ToTState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.state.update_candidates

.. py:function:: update_candidates(existing: list[haive.agents.tot.modular.models.Candidate] | None = None, updates: list[haive.agents.tot.modular.models.Candidate] | str | list[dict[str, Any]] | None = None) -> list[haive.agents.tot.modular.models.Candidate]

   Update candidate list, handling special cases like clearing.

   :param existing: Current list of candidates
   :param updates: New candidates to add, or "clear" to empty the list

   :returns: Updated list of candidates


   .. autolink-examples:: update_candidates
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.modular.state
   :collapse:
   
.. autolink-skip:: next
