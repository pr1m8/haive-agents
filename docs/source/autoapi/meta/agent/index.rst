
:py:mod:`meta.agent`
====================

.. py:module:: meta.agent

Generic MetaAgent class for agent composition and recompilation management.


.. autolink-examples:: meta.agent
   :collapse:

Classes
-------

.. autoapisummary::

   meta.agent.MetaAgent
   meta.agent.MetaAgentState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MetaAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MetaAgent {
        node [shape=record];
        "MetaAgent" [label="MetaAgent"];
        "haive.agents.base.agent.Agent" -> "MetaAgent";
        "Generic[TAgent]" -> "MetaAgent";
      }

.. autoclass:: meta.agent.MetaAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MetaAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_MetaAgentState {
        node [shape=record];
        "MetaAgentState" [label="MetaAgentState"];
        "haive.core.schema.StateSchema" -> "MetaAgentState";
      }

.. autoclass:: meta.agent.MetaAgentState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   meta.agent.get_summary
   meta.agent.meta_execute
   meta.agent.needs_recompilation
   meta.agent.recompile
   meta.agent.run
   meta.agent.setup_agent
   meta.agent.update_wrapped_agent
   meta.agent.wrap
   meta.agent.wrapped_agent

.. py:function:: get_summary(meta_agent: MetaAgent) -> dict[str, Any]

   Get summary of meta agent execution and recompilation.


   .. autolink-examples:: get_summary
      :collapse:

.. py:function:: meta_execute(meta_agent: MetaAgent, *args, **kwargs) -> Any
   :async:


   Execute a meta agent asynchronously.


   .. autolink-examples:: meta_execute
      :collapse:

.. py:function:: needs_recompilation(meta_agent: MetaAgent) -> bool

   Check if meta agent needs recompilation.


   .. autolink-examples:: needs_recompilation
      :collapse:

.. py:function:: recompile(meta_agent: MetaAgent, reason: str = 'Manual recompilation') -> dict[str, Any]

   Recompile a meta agent.


   .. autolink-examples:: recompile
      :collapse:

.. py:function:: run(meta_agent: MetaAgent, *args, **kwargs) -> Any

   Run a meta agent.


   .. autolink-examples:: run
      :collapse:

.. py:function:: setup_agent(meta_agent: MetaAgent) -> None

   Setup a meta agent.


   .. autolink-examples:: setup_agent
      :collapse:

.. py:function:: update_wrapped_agent(meta_agent: MetaAgent, new_agent: TAgent) -> None

   Update the wrapped agent in a meta agent.


   .. autolink-examples:: update_wrapped_agent
      :collapse:

.. py:function:: wrap(agent: TAgent, **kwargs) -> MetaAgent[TAgent]

   Convenience function to wrap an agent with meta capabilities.


   .. autolink-examples:: wrap
      :collapse:

.. py:function:: wrapped_agent(meta_agent: MetaAgent) -> Any

   Get the wrapped agent from a meta agent.


   .. autolink-examples:: wrapped_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: meta.agent
   :collapse:
   
.. autolink-skip:: next
