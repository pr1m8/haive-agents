
:py:mod:`agents.simple.lazy_simple_agent`
=========================================

.. py:module:: agents.simple.lazy_simple_agent

Ultra-optimized SimpleAgent implementation that achieves sub-3 second import times.
through comprehensive lazy loading and intelligent caching.

This approach uses proxy objects and deferred imports to avoid loading any heavy
dependencies (LangChain, NumPy, Pandas, etc.) until they're actually needed.

Usage:
    # Ultra-fast import - no heavy dependencies
    from haive.agents.simple.lazy_simple_agent import LazySimpleAgent as SimpleAgentV3

    # Heavy loading happens only when actually used
    agent = SimpleAgent(name="test")  # Still fast - creates proxy
    result = await agent.arun("Hello")  # Heavy loading happens here


.. autolink-examples:: agents.simple.lazy_simple_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.lazy_simple_agent.LazyAgent
   agents.simple.lazy_simple_agent.LazyAugLLMConfig
   agents.simple.lazy_simple_agent.LazySimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LazyAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LazyAgent {
        node [shape=record];
        "LazyAgent" [label="LazyAgent"];
      }

.. autoclass:: agents.simple.lazy_simple_agent.LazyAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LazyAugLLMConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LazyAugLLMConfig {
        node [shape=record];
        "LazyAugLLMConfig" [label="LazyAugLLMConfig"];
      }

.. autoclass:: agents.simple.lazy_simple_agent.LazyAugLLMConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LazySimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LazySimpleAgent {
        node [shape=record];
        "LazySimpleAgent" [label="LazySimpleAgent"];
      }

.. autoclass:: agents.simple.lazy_simple_agent.LazySimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.lazy_simple_agent.cached_import

.. py:function:: cached_import(module_path: str, class_name: str | None = None)

   Cached import with intelligent loading.


   .. autolink-examples:: cached_import
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.simple.lazy_simple_agent
   :collapse:
   
.. autolink-skip:: next
