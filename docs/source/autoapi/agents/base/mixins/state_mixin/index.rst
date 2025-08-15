agents.base.mixins.state_mixin
==============================

.. py:module:: agents.base.mixins.state_mixin


Attributes
----------

.. autoapisummary::

   agents.base.mixins.state_mixin.logger


Classes
-------

.. autoapisummary::

   agents.base.mixins.state_mixin.StateMixin


Module Contents
---------------

.. py:class:: StateMixin

   Mixin for agent state management functionality.

   This mixin expects to be used with classes that have:
   - _app: Application/graph instance
   - name: Agent name
   - config: Agent configuration
   - _prepare_runnable_config: Method to prepare runnable config


   .. autolink-examples:: StateMixin
      :collapse:

   .. py:method:: get_state_filename() -> str | None

      Get the current state filename if one has been generated.


      .. autolink-examples:: get_state_filename
         :collapse:


   .. py:method:: inspect_state(thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None) -> None

      Inspect the current state of the agent.

      :param thread_id: Optional thread ID for persistence
      :param config: Optional runtime configuration


      .. autolink-examples:: inspect_state
         :collapse:


   .. py:method:: inspect_state_async(thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None) -> None
      :async:


      Asynchronously inspect the current state of the agent.

      :param thread_id: Optional thread ID for persistence
      :param config: Optional runtime configuration


      .. autolink-examples:: inspect_state_async
         :collapse:


   .. py:method:: load_from_state(state_data: dict[str, Any] | str, thread_id: str | None = None) -> bool

      Load agent state from a saved state file or dictionary.

      :param state_data: Dictionary or path to JSON file containing state data
      :param thread_id: Optional thread ID for persistence

      :returns: True if successful, False otherwise


      .. autolink-examples:: load_from_state
         :collapse:


   .. py:method:: load_from_state_async(state_data: dict[str, Any] | str, thread_id: str | None = None) -> bool
      :async:


      Asynchronously load agent state from a saved state file or dictionary.

      :param state_data: Dictionary or path to JSON file containing state data
      :param thread_id: Optional thread ID for persistence

      :returns: True if successful, False otherwise


      .. autolink-examples:: load_from_state_async
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize the mixin with state tracking attributes after Pydantic validation.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:method:: reset_state(thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None) -> bool

      Reset the agent's state for a thread.

      :param thread_id: Optional thread ID for persistence
      :param config: Optional runtime configuration

      :returns: True if successful, False otherwise


      .. autolink-examples:: reset_state
         :collapse:


   .. py:method:: reset_state_async(thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None) -> bool
      :async:


      Asynchronously reset the agent's state for a thread.

      :param thread_id: Optional thread ID for persistence
      :param config: Optional runtime configuration

      :returns: True if successful, False otherwise


      .. autolink-examples:: reset_state_async
         :collapse:


   .. py:method:: save_state_history(runnable_config: langchain_core.runnables.RunnableConfig | None = None) -> bool

      Save the current agent state to a JSON file.

      :param runnable_config: Optional runnable configuration

      :returns: True if successful, False otherwise


      .. autolink-examples:: save_state_history
         :collapse:


   .. py:method:: save_state_history_async(runnable_config: langchain_core.runnables.RunnableConfig | None = None) -> bool
      :async:


      Asynchronously save the current agent state to a JSON file.

      :param runnable_config: Optional runnable configuration

      :returns: True if successful, False otherwise


      .. autolink-examples:: save_state_history_async
         :collapse:


   .. py:method:: set_state_filename(filename: str) -> None

      Set a custom state filename.


      .. autolink-examples:: set_state_filename
         :collapse:


   .. py:attribute:: _app
      :type:  Any


.. py:data:: logger

