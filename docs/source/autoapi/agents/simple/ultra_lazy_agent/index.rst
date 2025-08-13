
:py:mod:`agents.simple.ultra_lazy_agent`
========================================

.. py:module:: agents.simple.ultra_lazy_agent

Ultra-aggressive lazy loading implementation that defers ALL dependencies.
until the moment of first actual use. Target: <3 second import time.

This uses the most minimal possible imports and defers everything else.


.. autolink-examples:: agents.simple.ultra_lazy_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.ultra_lazy_agent.UltraLazyAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for UltraLazyAgent:

   .. graphviz::
      :align: center

      digraph inheritance_UltraLazyAgent {
        node [shape=record];
        "UltraLazyAgent" [label="UltraLazyAgent"];
      }

.. autoclass:: agents.simple.ultra_lazy_agent.UltraLazyAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.ultra_lazy_agent
   :collapse:
   
.. autolink-skip:: next
