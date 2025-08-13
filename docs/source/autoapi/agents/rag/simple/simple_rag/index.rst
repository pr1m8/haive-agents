
:py:mod:`agents.rag.simple.simple_rag`
======================================

.. py:module:: agents.rag.simple.simple_rag

SimpleRAG - Class inheriting from MultiAgent.


.. autolink-examples:: agents.rag.simple.simple_rag
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.simple.simple_rag.RAGAnswer
   agents.rag.simple.simple_rag.SimpleRAG


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGAnswer:

   .. graphviz::
      :align: center

      digraph inheritance_RAGAnswer {
        node [shape=record];
        "RAGAnswer" [label="RAGAnswer"];
        "pydantic.BaseModel" -> "RAGAnswer";
      }

.. autopydantic_model:: agents.rag.simple.simple_rag.RAGAnswer
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

   Inheritance diagram for SimpleRAG:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAG {
        node [shape=record];
        "SimpleRAG" [label="SimpleRAG"];
        "haive.agents.multi.agent.MultiAgent" -> "SimpleRAG";
      }

.. autoclass:: agents.rag.simple.simple_rag.SimpleRAG
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.simple.simple_rag
   :collapse:
   
.. autolink-skip:: next
