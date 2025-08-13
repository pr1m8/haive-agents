
:py:mod:`agents.ltm.memory_schemas`
===================================

.. py:module:: agents.ltm.memory_schemas

Memory schemas for LTM agent using LangMem patterns.

These schemas define the structure of memories that will be extracted
and managed by the LTM agent.


.. autolink-examples:: agents.ltm.memory_schemas
   :collapse:

Classes
-------

.. autoapisummary::

   agents.ltm.memory_schemas.ConversationalMemory
   agents.ltm.memory_schemas.FactualMemory
   agents.ltm.memory_schemas.Memory
   agents.ltm.memory_schemas.PersonalContext
   agents.ltm.memory_schemas.UserPreference


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConversationalMemory:

   .. graphviz::
      :align: center

      digraph inheritance_ConversationalMemory {
        node [shape=record];
        "ConversationalMemory" [label="ConversationalMemory"];
        "pydantic.BaseModel" -> "ConversationalMemory";
      }

.. autopydantic_model:: agents.ltm.memory_schemas.ConversationalMemory
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

   Inheritance diagram for FactualMemory:

   .. graphviz::
      :align: center

      digraph inheritance_FactualMemory {
        node [shape=record];
        "FactualMemory" [label="FactualMemory"];
        "pydantic.BaseModel" -> "FactualMemory";
      }

.. autopydantic_model:: agents.ltm.memory_schemas.FactualMemory
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

   Inheritance diagram for Memory:

   .. graphviz::
      :align: center

      digraph inheritance_Memory {
        node [shape=record];
        "Memory" [label="Memory"];
        "pydantic.BaseModel" -> "Memory";
      }

.. autopydantic_model:: agents.ltm.memory_schemas.Memory
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

   Inheritance diagram for PersonalContext:

   .. graphviz::
      :align: center

      digraph inheritance_PersonalContext {
        node [shape=record];
        "PersonalContext" [label="PersonalContext"];
        "pydantic.BaseModel" -> "PersonalContext";
      }

.. autopydantic_model:: agents.ltm.memory_schemas.PersonalContext
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

   Inheritance diagram for UserPreference:

   .. graphviz::
      :align: center

      digraph inheritance_UserPreference {
        node [shape=record];
        "UserPreference" [label="UserPreference"];
        "pydantic.BaseModel" -> "UserPreference";
      }

.. autopydantic_model:: agents.ltm.memory_schemas.UserPreference
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

.. autolink-examples:: agents.ltm.memory_schemas
   :collapse:
   
.. autolink-skip:: next
