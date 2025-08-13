
:py:mod:`agents.simple.agent_v3_minimal`
========================================

.. py:module:: agents.simple.agent_v3_minimal

SimpleAgent v3 implementation with minimal import overhead.

This implementation provides the same SimpleAgentV3 functionality but with
lazy loading of all heavy dependencies to achieve sub-5 second import times.

Usage:
    # Fast import - no heavy dependencies loaded
    from haive.agents.simple.agent_v3_minimal import SimpleAgentV3Minimal as SimpleAgentV3

    # Full functionality available when actually used
    agent = SimpleAgent(name="test")
    result = await agent.arun("Hello")


.. autolink-examples:: agents.simple.agent_v3_minimal
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.agent_v3_minimal.SimpleAgentV3Minimal


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgentV3Minimal:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgentV3Minimal {
        node [shape=record];
        "SimpleAgentV3Minimal" [label="SimpleAgentV3Minimal"];
      }

.. autoclass:: agents.simple.agent_v3_minimal.SimpleAgentV3Minimal
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.agent_v3_minimal
   :collapse:
   
.. autolink-skip:: next
