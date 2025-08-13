
:py:mod:`list_multi_agent`
==========================

.. py:module:: list_multi_agent

List-based multi-agent implementation.

from typing import Any
A clean, simple multi-agent that acts like a Python list of agents.
Focus on composition and orchestration, not complex state management.


.. autolink-examples:: list_multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   list_multi_agent.ListMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ListMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ListMultiAgent {
        node [shape=record];
        "ListMultiAgent" [label="ListMultiAgent"];
        "haive.agents.base.agent.Agent" -> "ListMultiAgent";
        "haive.core.common.mixins.recompile_mixin.RecompileMixin" -> "ListMultiAgent";
        "collections.abc.Sequence[haive.agents.base.agent.Agent]" -> "ListMultiAgent";
      }

.. autoclass:: list_multi_agent.ListMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   list_multi_agent.pipeline
   list_multi_agent.sequential

.. py:function:: pipeline(*agents: haive.agents.base.agent.Agent, name: str = 'pipeline') -> ListMultiAgent

   Create a pipeline of agents (alias for sequential).


   .. autolink-examples:: pipeline
      :collapse:

.. py:function:: sequential(*agents: haive.agents.base.agent.Agent, name: str = 'sequential_multi') -> ListMultiAgent

   Create a sequential multi-agent from agents.


   .. autolink-examples:: sequential
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: list_multi_agent
   :collapse:
   
.. autolink-skip:: next
