agents.reasoning_and_critique.tot.modular.branches
==================================================

.. py:module:: agents.reasoning_and_critique.tot.modular.branches


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.branches.ToTBranch


Module Contents
---------------

.. py:class:: ToTBranch(agent: Any)

   Bases: :py:obj:`haive.core.graph.branches.Branch`


   Branch class for Tree of Thoughts routing logic.

   Handles the logic of deciding whether to continue exploration or
   terminate the search and return the best solution found.

   Initialize with reference to parent agent for config access.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToTBranch
      :collapse:

   .. py:method:: evaluate(state: dict[str, Any]) -> str | tuple | list[langgraph.types.Send] | langgraph.types.Command

      Evaluate the current state and determine the next steps.


      .. autolink-examples:: evaluate
         :collapse:


   .. py:attribute:: agent


