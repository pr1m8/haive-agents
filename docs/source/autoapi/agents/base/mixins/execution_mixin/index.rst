agents.base.mixins.execution_mixin
==================================

.. py:module:: agents.base.mixins.execution_mixin


Attributes
----------

.. autoapisummary::

   agents.base.mixins.execution_mixin.logger


Classes
-------

.. autoapisummary::

   agents.base.mixins.execution_mixin.ExecutionMixin


Module Contents
---------------

.. py:class:: ExecutionMixin

   Mixin for agent execution functionality including run, stream, and state management.


   .. autolink-examples:: ExecutionMixin
      :collapse:

   .. py:method:: _format_structured_output(output_data: Any) -> Any

      Format structured output for cleaner display without changing the type.

      :param output_data: Raw output data that may contain structured outputs

      :returns: The original output data unchanged (type preservation)


      .. autolink-examples:: _format_structured_output
         :collapse:


   .. py:method:: _prepare_input(input_data: Any) -> Any

      Prepare input for the agent based on the input schema.

      :param input_data: Input in various formats

      :returns: Processed input compatible with the graph


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _prepare_runnable_config(thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None, **kwargs) -> langchain_core.runnables.RunnableConfig

      Prepare a runnable config with thread ID and other parameters.

      :param thread_id: Optional thread ID for persistence
      :param config: Optional runtime configuration
      :param \*\*kwargs: Additional configuration parameters

      :returns: Prepared runnable configuration


      .. autolink-examples:: _prepare_runnable_config
         :collapse:


   .. py:method:: _process_output(output_data: Any) -> Any

      Process and validate output data.

      :param output_data: Raw output data from the graph

      :returns: Processed output data


      .. autolink-examples:: _process_output
         :collapse:


   .. py:method:: _process_stream_chunk(chunk: Any, stream_mode: str) -> dict[str, Any]

      Process a stream chunk based on stream mode.

      :param chunk: The raw stream chunk
      :param stream_mode: Stream mode (values, updates, debug, etc.)

      :returns: Processed stream chunk


      .. autolink-examples:: _process_stream_chunk
         :collapse:


   .. py:method:: arun(input_data: Any, thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None, debug: bool | None = None, **kwargs) -> Any
      :async:


      Asynchronously run the agent with input data.

      :param input_data: Input data for the agent
      :param thread_id: Optional thread ID for persistence
      :param config: Optional runtime configuration
      :param debug: Whether to enable debug mode
      :param \*\*kwargs: Additional runtime configuration

      :returns: Output from the agent


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: astream(input_data: Any, thread_id: str | None = None, stream_mode: str = 'values', config: langchain_core.runnables.RunnableConfig | None = None, debug: bool | None = None, **kwargs) -> collections.abc.AsyncGenerator[dict[str, Any], None]
      :async:


      Asynchronously stream agent execution with input data.

      This implementation wraps the synchronous generator in an async one
      by running the sync generator's iteration in a separate thread to avoid
      blocking the event loop.


      .. autolink-examples:: astream
         :collapse:


   .. py:method:: run(input_data: Any, thread_id: str | None = None, debug: bool | None = None, config: langchain_core.runnables.RunnableConfig | None = None, **kwargs) -> Any

      Synchronously run the agent with input data.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: save_state_history(config: langchain_core.runnables.RunnableConfig)

      Optionally save state history to a file.


      .. autolink-examples:: save_state_history
         :collapse:


   .. py:method:: stream(input_data: Any, thread_id: str | None = None, stream_mode: str = 'values', config: langchain_core.runnables.RunnableConfig | None = None, debug: bool | None = None, **kwargs) -> collections.abc.Generator[dict[str, Any], None, None]

      Stream agent execution with input data.

      :param input_data: Input data for the agent
      :param thread_id: Optional thread ID for persistence
      :param stream_mode: Stream mode (values, updates, debug, etc.)
      :param config: Optional runtime configuration
      :param debug: Whether to enable debug mode
      :param \*\*kwargs: Additional runtime configuration

      :Yields: State updates during execution


      .. autolink-examples:: stream
         :collapse:


.. py:data:: logger

