
:py:mod:`agents.rag.modular_chain`
==================================

.. py:module:: agents.rag.modular_chain

Modular RAG using ChainAgent.

Build configurable RAG pipelines with modular components.


.. autolink-examples:: agents.rag.modular_chain
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.modular_chain.ModularConfig
   agents.rag.modular_chain.RAGModule


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ModularConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ModularConfig {
        node [shape=record];
        "ModularConfig" [label="ModularConfig"];
        "pydantic.BaseModel" -> "ModularConfig";
      }

.. autopydantic_model:: agents.rag.modular_chain.ModularConfig
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

   Inheritance diagram for RAGModule:

   .. graphviz::
      :align: center

      digraph inheritance_RAGModule {
        node [shape=record];
        "RAGModule" [label="RAGModule"];
        "str" -> "RAGModule";
        "enum.Enum" -> "RAGModule";
      }

.. autoclass:: agents.rag.modular_chain.RAGModule
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGModule** is an Enum defined in ``agents.rag.modular_chain``.



Functions
---------

.. autoapisummary::

   agents.rag.modular_chain.create_comprehensive_modular_rag
   agents.rag.modular_chain.create_custom_modular_rag
   agents.rag.modular_chain.create_modular_rag
   agents.rag.modular_chain.create_simple_modular_rag

.. py:function:: create_comprehensive_modular_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a comprehensive modular RAG with all modules.


   .. autolink-examples:: create_comprehensive_modular_rag
      :collapse:

.. py:function:: create_custom_modular_rag(documents: list[langchain_core.documents.Document], modules: list[str], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a custom modular RAG with specified modules.


   .. autolink-examples:: create_custom_modular_rag
      :collapse:

.. py:function:: create_modular_rag(documents: list[langchain_core.documents.Document], config: ModularConfig, llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Modular RAG') -> haive.agents.chain.ChainAgent

   Create a modular RAG system with configurable components.


   .. autolink-examples:: create_modular_rag
      :collapse:

.. py:function:: create_simple_modular_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a simple modular RAG with basic modules.


   .. autolink-examples:: create_simple_modular_rag
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.modular_chain
   :collapse:
   
.. autolink-skip:: next
