
:py:mod:`agents.document_modifiers.kg.kg_iterative_refinement.agent`
====================================================================

.. py:module:: agents.document_modifiers.kg.kg_iterative_refinement.agent

Iterative Knowledge Graph Transformer Agent.

This module provides the IterativeGraphTransformer class which builds knowledge
graphs iteratively from a sequence of documents. It processes documents one by one,
starting with an initial graph and refining it with each subsequent document.

The agent is particularly useful for building comprehensive knowledge graphs from
multiple related documents where later documents may add detail or context to
earlier information.

Classes:
    IterativeGraphTransformer: Main agent for iterative knowledge graph construction

.. rubric:: Examples

Basic usage::

    from haive.agents.document_modifiers.kg.kg_iterative_refinement import IterativeGraphTransformer
    from haive.agents.document_modifiers.kg.kg_iterative_refinement.config import IterativeGraphTransformerConfig

    config = IterativeGraphTransformerConfig()
    agent = IterativeGraphTransformer(config)

    documents = [
        "Marie Curie was a physicist born in Poland.",
        "She won two Nobel Prizes in different fields.",
        "Her daughter Irène also won a Nobel Prize."
    ]
    result = agent.run({"contents": documents})
    graph = result["graph_doc"]

With custom configuration::

    config = IterativeGraphTransformerConfig(
        name="research_graph_builder",
        engines={"transformer": custom_llm_config}
    )
    agent = IterativeGraphTransformer(config)

.. seealso::

   - :class:`~haive.agents.document_modifiers.kg.kg_iterative_refinement.config.IterativeGraphTransformerConfig`: Configuration class
   - :class:`~haive.agents.document_modifiers.kg.kg_iterative_refinement.state.IterativeGraphTransformerState`: State management


.. autolink-examples:: agents.document_modifiers.kg.kg_iterative_refinement.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_iterative_refinement.agent.IterativeGraphTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeGraphTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeGraphTransformer {
        node [shape=record];
        "IterativeGraphTransformer" [label="IterativeGraphTransformer"];
        "haive.core.engine.agent.agent.Agent[haive.agents.document_modifiers.kg.kg_iterative_refinement.config.IterativeGraphTransformerConfig]" -> "IterativeGraphTransformer";
      }

.. autoclass:: agents.document_modifiers.kg.kg_iterative_refinement.agent.IterativeGraphTransformer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.kg.kg_iterative_refinement.agent.build_agent

.. py:function:: build_agent() -> IterativeGraphTransformer

   Create a default IterativeGraphTransformer instance.

   :returns: IterativeGraphTransformer with default configuration.


   .. autolink-examples:: build_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.kg.kg_iterative_refinement.agent
   :collapse:
   
.. autolink-skip:: next
