
:py:mod:`agents.memory_v2.long_term_memory_agent`
=================================================

.. py:module:: agents.memory_v2.long_term_memory_agent

Long-Term Memory Agent following LangChain patterns.

This implementation follows the LangChain long-term memory agent documentation:
https://python.langchain.com/docs/versions/migrating_memory/long_term_memory_agent/

Key features:
1. Load memories first approach
2. Semantic memory retrieval across conversations
3. Text and structured knowledge storage
4. Time-weighted retrieval
5. ReactAgent tool integration

Architecture:
- BaseRAGAgent for memory retrieval
- SimpleRAGAgent for memory-enhanced responses
- Memory extraction and storage pipeline
- Cross-conversation persistence


.. autolink-examples:: agents.memory_v2.long_term_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.long_term_memory_agent.KnowledgeTriple
   agents.memory_v2.long_term_memory_agent.LongTermMemoryAgent
   agents.memory_v2.long_term_memory_agent.LongTermMemoryStore
   agents.memory_v2.long_term_memory_agent.MemoryEntry


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KnowledgeTriple:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeTriple {
        node [shape=record];
        "KnowledgeTriple" [label="KnowledgeTriple"];
        "pydantic.BaseModel" -> "KnowledgeTriple";
      }

.. autopydantic_model:: agents.memory_v2.long_term_memory_agent.KnowledgeTriple
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

   Inheritance diagram for LongTermMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LongTermMemoryAgent {
        node [shape=record];
        "LongTermMemoryAgent" [label="LongTermMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.long_term_memory_agent.LongTermMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LongTermMemoryStore:

   .. graphviz::
      :align: center

      digraph inheritance_LongTermMemoryStore {
        node [shape=record];
        "LongTermMemoryStore" [label="LongTermMemoryStore"];
      }

.. autoclass:: agents.memory_v2.long_term_memory_agent.LongTermMemoryStore
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryEntry {
        node [shape=record];
        "MemoryEntry" [label="MemoryEntry"];
        "pydantic.BaseModel" -> "MemoryEntry";
      }

.. autopydantic_model:: agents.memory_v2.long_term_memory_agent.MemoryEntry
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



Functions
---------

.. autoapisummary::

   agents.memory_v2.long_term_memory_agent.create_long_term_memory_agent
   agents.memory_v2.long_term_memory_agent.demo_long_term_memory

.. py:function:: create_long_term_memory_agent(user_id: str, llm_config: haive.core.models.llm.base.LLMConfig | None = None, storage_path: str = './memory_store') -> LongTermMemoryAgent

   Factory function to create long-term memory agent.


   .. autolink-examples:: create_long_term_memory_agent
      :collapse:

.. py:function:: demo_long_term_memory()
   :async:


   Demo the long-term memory agent functionality.


   .. autolink-examples:: demo_long_term_memory
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.long_term_memory_agent
   :collapse:
   
.. autolink-skip:: next
