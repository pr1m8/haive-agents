agents.memory.models_dir.procedural.models
==========================================

.. py:module:: agents.memory.models_dir.procedural.models


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.procedural.models.InstructionComponent
   agents.memory.models_dir.procedural.models.ProceduralMemory
   agents.memory.models_dir.procedural.models.ReflectionCycle


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


Module Contents
---------------

.. py:class:: InstructionComponent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual instruction component with metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: InstructionComponent
      :collapse:

   .. py:method:: validate_instruction_clarity(v: str) -> str
      :classmethod:


      Validate instruction clarity and format.


      .. autolink-examples:: validate_instruction_clarity
         :collapse:


   .. py:attribute:: component_id
      :type:  uuid.UUID
      :value: None



   .. py:attribute:: effectiveness_score
      :type:  float
      :value: None



   .. py:attribute:: instruction_text
      :type:  str
      :value: None



   .. py:attribute:: last_modified
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: usage_count
      :type:  int
      :value: None



.. py:class:: ProceduralMemory

   Bases: :py:obj:`haive.agents.memory.models_dir.base.BaseMemoryModel`, :py:obj:`haive.agents.memory.models_dir.semantic.mixins.TemporalMixin`


   Advanced procedural memory with self-modification capabilities.


   .. autolink-examples:: ProceduralMemory
      :collapse:

   .. py:method:: _add_reflection_trigger(trigger: str) -> None

      Add a reflection trigger event.


      .. autolink-examples:: _add_reflection_trigger
         :collapse:


   .. py:method:: adapt_from_reflection(reflection: ReflectionCycle) -> None

      Adapt instructions based on reflection cycle.


      .. autolink-examples:: adapt_from_reflection
         :collapse:


   .. py:method:: generate_instruction_text() -> str

      Generate formatted instruction text for agent use.


      .. autolink-examples:: generate_instruction_text
         :collapse:


   .. py:method:: should_trigger_reflection() -> bool

      Determine if reflection cycle should be triggered.


      .. autolink-examples:: should_trigger_reflection
         :collapse:


   .. py:method:: validate_instruction_set(v: list[InstructionComponent]) -> list[InstructionComponent]
      :classmethod:


      Validate instruction set consistency.


      .. autolink-examples:: validate_instruction_set
         :collapse:


   .. py:method:: validate_procedural_integrity() -> ProceduralMemory

      Validate overall procedural memory integrity.


      .. autolink-examples:: validate_procedural_integrity
         :collapse:


   .. py:attribute:: __memory_type__
      :value: 'procedural'



   .. py:attribute:: __validation_level__
      :value: 'enterprise'



   .. py:attribute:: adaptation_threshold
      :type:  float
      :value: None



   .. py:attribute:: agent_id
      :type:  str
      :value: None



   .. py:attribute:: change_log
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: contextual_modifiers
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: core_instructions
      :type:  list[InstructionComponent]
      :value: None



   .. py:attribute:: instruction_set_name
      :type:  str
      :value: None



   .. py:attribute:: last_reflection
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: overall_effectiveness
      :type:  float
      :value: None



   .. py:attribute:: performance_trends
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: reflection_cycles
      :type:  list[ReflectionCycle]
      :value: None



   .. py:attribute:: usage_statistics
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: version
      :type:  int
      :value: None



.. py:class:: ReflectionCycle(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Reflection cycle for continuous improvement.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionCycle
      :collapse:

   .. py:method:: validate_reflection_logic() -> ReflectionCycle

      Validate reflection cycle logic.


      .. autolink-examples:: validate_reflection_logic
         :collapse:


   .. py:attribute:: change_rationale
      :type:  str
      :value: None



   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: current_performance
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: cycle_id
      :type:  uuid.UUID
      :value: None



   .. py:attribute:: identified_issues
      :type:  list[str]
      :value: None



   .. py:attribute:: proposed_changes
      :type:  list[str]
      :value: None



   .. py:attribute:: trigger_event
      :type:  str
      :value: None



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

