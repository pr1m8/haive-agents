agents.memory.models_dir.meta
=============================

.. py:module:: agents.memory.models_dir.meta


Classes
-------

.. autoapisummary::

   agents.memory.models_dir.meta.MemoryValidationMeta


Module Contents
---------------

.. py:class:: MemoryValidationMeta

   Bases: :py:obj:`pydantic._internal._model_construction.ModelMetaclass`


   Advanced metaclass for memory models with automatic validation registration.
   and cross-model consistency checking.

   Metaclass for creating Pydantic models.

   :param cls_name: The name of the class to be created.
   :param bases: The base classes of the class to be created.
   :param namespace: The attribute dictionary of the class to be created.
   :param __pydantic_generic_metadata__: Metadata for generic models.
   :param __pydantic_reset_parent_namespace__: Reset parent namespace.
   :param _create_model_module: The module of the class to be created, if created by `create_model`.
   :param \*\*kwargs: Catch-all for any other keyword arguments.

   :returns: The new class created by the metaclass.


   .. autolink-examples:: __new__
      :collapse:


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


