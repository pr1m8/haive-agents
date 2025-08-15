agents.memory_reorganized.models.meta
=====================================

.. py:module:: agents.memory_reorganized.models.meta

.. autoapi-nested-parse::

   Meta model module.

   This module provides meta functionality for the Haive framework.

   Classes:
       MemoryValidationMeta: MemoryValidationMeta implementation.
       for: for implementation.
       in: in implementation.

   Functions:


   .. autolink-examples:: agents.memory_reorganized.models.meta
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.models.meta.MemoryValidationMeta


Module Contents
---------------

.. py:class:: MemoryValidationMeta

   Bases: :py:obj:`abc.ABCMeta`


   Advanced metaclass for memory models with automatic validation registration and.
   cross-model consistency checking.


   .. autolink-examples:: MemoryValidationMeta
      :collapse:

   .. py:method:: _apply_global_validations(namespace: dict, level: str) -> dict
      :classmethod:


      Apply validation rules based on validation level.


      .. autolink-examples:: _apply_global_validations
         :collapse:


   .. py:method:: _integrity_validator(obj) -> bool
      :staticmethod:


      Data integrity validation.


      .. autolink-examples:: _integrity_validator
         :collapse:


   .. py:method:: _security_validator(obj) -> bool
      :staticmethod:


      Enterprise security validation.


      .. autolink-examples:: _security_validator
         :collapse:


   .. py:attribute:: _lock


   .. py:attribute:: _memory_registry
      :type:  dict[str, type]


   .. py:attribute:: _validation_rules
      :type:  dict[str, list[callable]]


