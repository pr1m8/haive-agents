
:py:mod:`agents.rag.multi_query.agent`
======================================

.. py:module:: agents.rag.multi_query.agent

Multi-Query RAG Agent.

Improves recall through query diversification.
Generates multiple query variations and retrieves from all.


.. autolink-examples:: agents.rag.multi_query.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_query.agent.MultiQueryRAGAgent
   agents.rag.multi_query.agent.MultiRetrievalAgent
   agents.rag.multi_query.agent.QueryVariations


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiQueryRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiQueryRAGAgent {
        node [shape=record];
        "MultiQueryRAGAgent" [label="MultiQueryRAGAgent"];
        "haive.agents.multi.enhanced_sequential_agent.SequentialAgent" -> "MultiQueryRAGAgent";
      }

.. autoclass:: agents.rag.multi_query.agent.MultiQueryRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiRetrievalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiRetrievalAgent {
        node [shape=record];
        "MultiRetrievalAgent" [label="MultiRetrievalAgent"];
        "haive.agents.base.agent.Agent" -> "MultiRetrievalAgent";
      }

.. autoclass:: agents.rag.multi_query.agent.MultiRetrievalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryVariations:

   .. graphviz::
      :align: center

      digraph inheritance_QueryVariations {
        node [shape=record];
        "QueryVariations" [label="QueryVariations"];
        "pydantic.BaseModel" -> "QueryVariations";
      }

.. autopydantic_model:: agents.rag.multi_query.agent.QueryVariations
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





.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_query.agent
   :collapse:
   
.. autolink-skip:: next
