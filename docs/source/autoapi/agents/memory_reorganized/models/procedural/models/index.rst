agents.memory_reorganized.models.procedural.models
==================================================

.. py:module:: agents.memory_reorganized.models.procedural.models

.. autoapi-nested-parse::

   Models model module.

   This module provides models functionality for the Haive framework.

   Classes:
       InstructionComponent: InstructionComponent implementation.
       ReflectionCycle: ReflectionCycle implementation.
       ProceduralMemory: ProceduralMemory implementation.

   Functions:
       validate_instruction_clarity: Validate Instruction Clarity functionality.
       validate_reflection_logic: Validate Reflection Logic functionality.
       validate_instruction_set: Validate Instruction Set functionality.


   .. autolink-examples:: agents.memory_reorganized.models.procedural.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.models.procedural.models.InstructionComponent
   agents.memory_reorganized.models.procedural.models.ProceduralMemory
   agents.memory_reorganized.models.procedural.models.ReflectionCycle


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

   Bases: :py:obj:`BaseMemoryModel`, :py:obj:`TemporalMixin`


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


   .. py:method:: validate_instruction_set(v: List[InstructionComponent]) -> List[InstructionComponent]
      :classmethod:


      Validate instruction set consistency.


      .. autolink-examples:: validate_instruction_set
         :collapse:


   .. py:method:: validate_procedural_integrity() -> ProceduralMemory
      :classmethod:


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
      :type:  List[Dict[str, Any]]
      :value: None



   .. py:attribute:: contextual_modifiers
      :type:  Dict[str, List[str]]
      :value: None



   .. py:attribute:: core_instructions
      :type:  List[InstructionComponent]
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
      :type:  List[Dict[str, Any]]
      :value: None



   .. py:attribute:: reflection_cycles
      :type:  List[ReflectionCycle]
      :value: None



   .. py:attribute:: usage_statistics
      :type:  Dict[str, int]
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
      :classmethod:


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
      :type:  Dict[str, float]
      :value: None



   .. py:attribute:: cycle_id
      :type:  uuid.UUID
      :value: None



   .. py:attribute:: identified_issues
      :type:  List[str]
      :value: None



   .. py:attribute:: proposed_changes
      :type:  List[str]
      :value: None



   .. py:attribute:: trigger_event
      :type:  str
      :value: None



