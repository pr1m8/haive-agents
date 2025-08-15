agents.base.mixins.persistence_mixin
====================================

.. py:module:: agents.base.mixins.persistence_mixin

.. autoapi-nested-parse::

   Persistence Mixin for Agent classes.

   This mixin provides persistence functionality including checkpointer setup,
   store management, and configuration handling. It separates persistence
   concerns from the main Agent class while ensuring proper serialization.


   .. autolink-examples:: agents.base.mixins.persistence_mixin
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.mixins.persistence_mixin.logger


Classes
-------

.. autoapisummary::

   agents.base.mixins.persistence_mixin.PersistenceMixin


Module Contents
---------------

.. py:class:: PersistenceMixin

   Mixin for agent persistence functionality.

   Provides methods for setting up checkpointers, stores, and managing
   persistence configuration in a serializable way.


   .. autolink-examples:: PersistenceMixin
      :collapse:

   .. py:method:: _asetup_persistence_from_fields() -> None
      :async:


      Set up async persistence using the persistence field.


      .. autolink-examples:: _asetup_persistence_from_fields
         :collapse:


   .. py:method:: _generate_default_thread_id() -> str

      Generate a unique thread_id for each agent instance.

      This method now generates truly unique thread IDs using UUIDs to prevent
      collisions when multiple instances of the same agent run concurrently.

      For cases where you need consistent thread IDs (e.g., resuming conversations),
      explicitly pass a thread_id to the run() method.


      .. autolink-examples:: _generate_default_thread_id
         :collapse:


   .. py:method:: _setup_async_checkpointer_from_fields() -> None

      Set up async checkpointer using the persistence field.


      .. autolink-examples:: _setup_async_checkpointer_from_fields
         :collapse:


   .. py:method:: _setup_checkpointer_from_fields() -> None

      Set up checkpointer using the persistence field.


      .. autolink-examples:: _setup_checkpointer_from_fields
         :collapse:


   .. py:method:: _setup_default_persistence() -> None

      Set up default persistence configuration.

      Creates default PostgreSQL persistence with recursion limit 100,
      using Supabase connection string from environment if available,
      falling back to memory persistence if PostgreSQL unavailable.


      .. autolink-examples:: _setup_default_persistence
         :collapse:


   .. py:method:: _setup_persistence_from_config() -> None

      Set up persistence using the agent's serializable fields.

      This method sets up checkpointer and store based on the Agent's
      serializable persistence fields.

      Persistence behavior:
      - persistence=False: Persistence is explicitly disabled
      - persistence=None: Use memory persistence (safe default for testing)
      - persistence=True: Use default persistence (PostgreSQL if available)
      - persistence=<config>: Use specific configuration


      .. autolink-examples:: _setup_persistence_from_config
         :collapse:


   .. py:method:: _setup_store_from_fields() -> None

      Set up store using the add_store field.


      .. autolink-examples:: _setup_store_from_fields
         :collapse:


   .. py:method:: _sync_persistence_fields_from_config() -> None

      Sync serializable persistence fields from config.


      .. autolink-examples:: _sync_persistence_fields_from_config
         :collapse:


   .. py:method:: get_effective_runnable_config(**overrides) -> langchain_core.runnables.RunnableConfig

      Get the effective runnable config with defaults and overrides.


      .. autolink-examples:: get_effective_runnable_config
         :collapse:


   .. py:method:: get_persistence_config() -> dict[str, Any]

      Get the current persistence configuration as a serializable dict.


      .. autolink-examples:: get_persistence_config
         :collapse:


   .. py:method:: update_persistence_config(**config_updates) -> None

      Update persistence configuration and re-setup if needed.


      .. autolink-examples:: update_persistence_config
         :collapse:


.. py:data:: logger

