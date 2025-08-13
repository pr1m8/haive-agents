
:py:mod:`agents.reasoning_and_critique.tot.tree_of_thoughts_agent`
==================================================================

.. py:module:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent

Tree of Thoughts Multi-Agent Implementation.

This implements the complete Tree of Thoughts algorithm using MultiAgent
with proper LangGraph routing, conditional edges, and send-based branching.


.. autolink-examples:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TOTCommand
   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TOTIteration
   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TreeOfThoughtsAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TOTCommand:

   .. graphviz::
      :align: center

      digraph inheritance_TOTCommand {
        node [shape=record];
        "TOTCommand" [label="TOTCommand"];
        "pydantic.BaseModel" -> "TOTCommand";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TOTCommand
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TOTIteration:

   .. graphviz::
      :align: center

      digraph inheritance_TOTIteration {
        node [shape=record];
        "TOTIteration" [label="TOTIteration"];
        "pydantic.BaseModel" -> "TOTIteration";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TOTIteration
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TreeOfThoughtsAgent:

   .. graphviz::
      :align: center

      digraph inheritance_TreeOfThoughtsAgent {
        node [shape=record];
        "TreeOfThoughtsAgent" [label="TreeOfThoughtsAgent"];
      }

.. autoclass:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent.TreeOfThoughtsAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.tree_of_thoughts_agent.create_tree_of_thoughts_agent

.. py:function:: create_tree_of_thoughts_agent(beam_size: int = 3, max_iterations: int = 3, generation_temperature: float = 0.7, scoring_temperature: float = 0.3) -> TreeOfThoughtsAgent

   Create a Tree of Thoughts agent with default settings.

   :param beam_size: Number of top solutions to keep in beam search
   :param max_iterations: Maximum TOT iterations
   :param generation_temperature: Temperature for candidate generation
   :param scoring_temperature: Temperature for solution scoring

   :returns: Configured TreeOfThoughtsAgent


   .. autolink-examples:: create_tree_of_thoughts_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.tree_of_thoughts_agent
   :collapse:
   
.. autolink-skip:: next
