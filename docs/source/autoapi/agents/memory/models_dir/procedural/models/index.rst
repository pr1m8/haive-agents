
:py:mod:`agents.memory.models_dir.procedural.models`
====================================================

.. py:module:: agents.memory.models_dir.procedural.models


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.procedural.models.InstructionComponent
   agents.memory.models_dir.procedural.models.ProceduralMemory
   agents.memory.models_dir.procedural.models.ReflectionCycle


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for InstructionComponent:

   .. graphviz::
      :align: center

      digraph inheritance_InstructionComponent {
        node [shape=record];
        "InstructionComponent" [label="InstructionComponent"];
        "pydantic.BaseModel" -> "InstructionComponent";
      }

.. autopydantic_model:: agents.memory.models_dir.procedural.models.InstructionComponent
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

   Inheritance diagram for ProceduralMemory:

   .. graphviz::
      :align: center

      digraph inheritance_ProceduralMemory {
        node [shape=record];
        "ProceduralMemory" [label="ProceduralMemory"];
        "haive.agents.memory.models_dir.base.BaseMemoryModel" -> "ProceduralMemory";
        "haive.agents.memory.models_dir.semantic.mixins.TemporalMixin" -> "ProceduralMemory";
      }

.. autoclass:: agents.memory.models_dir.procedural.models.ProceduralMemory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionCycle:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionCycle {
        node [shape=record];
        "ReflectionCycle" [label="ReflectionCycle"];
        "pydantic.BaseModel" -> "ReflectionCycle";
      }

.. autopydantic_model:: agents.memory.models_dir.procedural.models.ReflectionCycle
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

   agents.memory.models_dir.procedural.models.adapt_from_reflection
   agents.memory.models_dir.procedural.models.generate_instruction_text
   agents.memory.models_dir.procedural.models.should_trigger_reflection
   agents.memory.models_dir.procedural.models.validate_instruction_clarity
   agents.memory.models_dir.procedural.models.validate_instruction_set
   agents.memory.models_dir.procedural.models.validate_procedural_integrity
   agents.memory.models_dir.procedural.models.validate_reflection_logic

.. py:function:: adapt_from_reflection(memory: ProceduralMemory, reflection: ReflectionCycle) -> None

   Adapt instructions based on reflection cycle.


   .. autolink-examples:: adapt_from_reflection
      :collapse:

.. py:function:: generate_instruction_text(memory: ProceduralMemory) -> str

   Generate formatted instruction text for agent use.


   .. autolink-examples:: generate_instruction_text
      :collapse:

.. py:function:: should_trigger_reflection(memory: ProceduralMemory) -> bool

   Determine if reflection cycle should be triggered.


   .. autolink-examples:: should_trigger_reflection
      :collapse:

.. py:function:: validate_instruction_clarity(instruction_text: str) -> str

   Validate instruction clarity and format.


   .. autolink-examples:: validate_instruction_clarity
      :collapse:

.. py:function:: validate_instruction_set(instructions: list[InstructionComponent]) -> list[InstructionComponent]

   Validate instruction set consistency.


   .. autolink-examples:: validate_instruction_set
      :collapse:

.. py:function:: validate_procedural_integrity(memory: ProceduralMemory) -> ProceduralMemory

   Validate overall procedural memory integrity.


   .. autolink-examples:: validate_procedural_integrity
      :collapse:

.. py:function:: validate_reflection_logic(reflection: ReflectionCycle) -> ReflectionCycle

   Validate reflection cycle logic.


   .. autolink-examples:: validate_reflection_logic
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory.models_dir.procedural.models
   :collapse:
   
.. autolink-skip:: next
