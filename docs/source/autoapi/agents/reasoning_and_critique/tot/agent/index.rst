
:py:mod:`agents.reasoning_and_critique.tot.agent`
=================================================

.. py:module:: agents.reasoning_and_critique.tot.agent

Tree of Thoughts (ToT) agent implementation.

This module implements the Tree of Thoughts algorithm as a Haive agent.


.. autolink-examples:: agents.reasoning_and_critique.tot.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agent.ToTAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToTAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ToTAgent {
        node [shape=record];
        "ToTAgent" [label="ToTAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.reasoning_and_critique.tot.config.TOTAgentConfig]" -> "ToTAgent";
        "Generic[T]" -> "ToTAgent";
      }

.. autoclass:: agents.reasoning_and_critique.tot.agent.ToTAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agent.compose_evaluator_runnable
   agents.reasoning_and_critique.tot.agent.compose_generator_runnable
   agents.reasoning_and_critique.tot.agent.create_evaluator_engine
   agents.reasoning_and_critique.tot.agent.create_generator_engine

.. py:function:: compose_evaluator_runnable(engine, use_structured_output=False)

   Create evaluator runnable.


   .. autolink-examples:: compose_evaluator_runnable
      :collapse:

.. py:function:: compose_generator_runnable(engine, use_structured_output=False)

   Create generator runnable.


   .. autolink-examples:: compose_generator_runnable
      :collapse:

.. py:function:: create_evaluator_engine(engine, use_structured_output=False, output_model=None)

   Create evaluator engine configuration.


   .. autolink-examples:: create_evaluator_engine
      :collapse:

.. py:function:: create_generator_engine(engine, use_structured_output=False, output_model=None)

   Create generator engine configuration.


   .. autolink-examples:: create_generator_engine
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.agent
   :collapse:
   
.. autolink-skip:: next
