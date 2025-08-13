
:py:mod:`agents.rag.factories.compatible_rag_factory_simple`
============================================================

.. py:module:: agents.rag.factories.compatible_rag_factory_simple

Simplified Compatible RAG Factory.

Simplified version without legacy functions that have import issues.


.. autolink-examples:: agents.rag.factories.compatible_rag_factory_simple
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory_simple.CompatibleRAGFactory
   agents.rag.factories.compatible_rag_factory_simple.RAGComponent
   agents.rag.factories.compatible_rag_factory_simple.WorkflowPattern


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompatibleRAGFactory:

   .. graphviz::
      :align: center

      digraph inheritance_CompatibleRAGFactory {
        node [shape=record];
        "CompatibleRAGFactory" [label="CompatibleRAGFactory"];
      }

.. autoclass:: agents.rag.factories.compatible_rag_factory_simple.CompatibleRAGFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGComponent:

   .. graphviz::
      :align: center

      digraph inheritance_RAGComponent {
        node [shape=record];
        "RAGComponent" [label="RAGComponent"];
        "enum.Enum" -> "RAGComponent";
      }

.. autoclass:: agents.rag.factories.compatible_rag_factory_simple.RAGComponent
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGComponent** is an Enum defined in ``agents.rag.factories.compatible_rag_factory_simple``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for WorkflowPattern:

   .. graphviz::
      :align: center

      digraph inheritance_WorkflowPattern {
        node [shape=record];
        "WorkflowPattern" [label="WorkflowPattern"];
        "enum.Enum" -> "WorkflowPattern";
      }

.. autoclass:: agents.rag.factories.compatible_rag_factory_simple.WorkflowPattern
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **WorkflowPattern** is an Enum defined in ``agents.rag.factories.compatible_rag_factory_simple``.



Functions
---------

.. autoapisummary::

   agents.rag.factories.compatible_rag_factory_simple.create_plug_and_play_component
   agents.rag.factories.compatible_rag_factory_simple.get_component_compatibility_info

.. py:function:: create_plug_and_play_component(component_type: RAGComponent, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.simple.agent.SimpleAgent | haive.agents.rag.base.agent.BaseRAGAgent

   Create any RAG component as a standalone agent.


   .. autolink-examples:: create_plug_and_play_component
      :collapse:

.. py:function:: get_component_compatibility_info(component_type: RAGComponent) -> dict[str, list[str]]

   Get I/O schema information for a component type.


   .. autolink-examples:: get_component_compatibility_info
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.factories.compatible_rag_factory_simple
   :collapse:
   
.. autolink-skip:: next
