agents.memory_reorganized.models.base
=====================================

.. py:module:: agents.memory_reorganized.models.base

.. autoapi-nested-parse::

   Base model module.

   This module provides base functionality for the Haive framework.

   Classes:
       BaseMemoryModel: BaseMemoryModel implementation.
       Config: Config implementation.

   Functions:
       validate_tags: Validate Tags functionality.
       validate_priority: Validate Priority functionality.
       validate_lifecycle_consistency: Validate Lifecycle Consistency functionality.


   .. autolink-examples:: agents.memory_reorganized.models.base
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.models.base.BaseMemoryModel


Module Contents
---------------

.. py:class:: BaseMemoryModel(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Enhanced base memory model with sophisticated validation patterns and automatic.
   metadata management.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseMemoryModel
      :collapse:

   .. py:class:: Config

      Enhanced model configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True



      .. py:attribute:: json_encoders


      .. py:attribute:: validate_assignment
         :value: True




   .. py:method:: mark_accessed() -> None

      Mark memory as being accessed for validation.


      .. autolink-examples:: mark_accessed
         :collapse:


   .. py:method:: validate_lifecycle_consistency() -> BaseMemoryModel
      :classmethod:


      Cross-field lifecycle validation.


      .. autolink-examples:: validate_lifecycle_consistency
         :collapse:


   .. py:method:: validate_priority(v: int, info) -> int
      :classmethod:


      Dynamic priority validation based on memory type.


      .. autolink-examples:: validate_priority
         :collapse:


   .. py:method:: validate_tags(v: list[str]) -> list[str]
      :classmethod:


      Advanced tag validation with business rules.


      .. autolink-examples:: validate_tags
         :collapse:


   .. py:attribute:: access_count
      :type:  int
      :value: None



   .. py:attribute:: checksum
      :type:  str | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: expires_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: is_archived
      :type:  bool
      :value: None



   .. py:attribute:: last_accessed
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: memory_id
      :type:  uuid.UUID
      :value: None



   .. py:attribute:: priority_level
      :type:  int
      :value: None



   .. py:attribute:: relationships
      :type:  dict[str, list[uuid.UUID]]
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



   .. py:attribute:: validation_status
      :type:  Literal['pending', 'validated', 'invalid', 'expired']
      :value: None



