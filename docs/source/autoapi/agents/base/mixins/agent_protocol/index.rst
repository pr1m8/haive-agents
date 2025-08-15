agents.base.mixins.agent_protocol
=================================

.. py:module:: agents.base.mixins.agent_protocol


Classes
-------

.. autoapisummary::

   agents.base.mixins.agent_protocol.AgentProtocol


Module Contents
---------------

.. py:class:: AgentProtocol

   Bases: :py:obj:`Protocol`


   Protocol defining the interface an Agent class must provide for mixins.


   .. autolink-examples:: AgentProtocol
      :collapse:

   .. py:method:: _prepare_input(input_data: Any) -> Any


   .. py:method:: _prepare_runnable_config(thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None, **kwargs) -> langchain_core.runnables.RunnableConfig


   .. py:method:: _process_output(output_data: Any) -> Any


   .. py:method:: _process_stream_chunk(chunk: Any, stream_mode: str) -> dict[str, Any]


   .. py:method:: arun(input_data: Any, thread_id: str | None = None, config: langchain_core.runnables.RunnableConfig | None = None, debug: bool | None = None, **kwargs) -> Any
      :async:



   .. py:method:: astream(input_data: Any, thread_id: str | None = None, stream_mode: str = 'values', config: langchain_core.runnables.RunnableConfig | None = None, debug: bool | None = None, **kwargs) -> collections.abc.AsyncGenerator[dict[str, Any], None]
      :async:



   .. py:method:: compile(**kwargs) -> langgraph.graph.graph.CompiledGraph


   .. py:method:: run(input_data: Any, thread_id: str | None = None, debug: bool | None = None, config: langchain_core.runnables.RunnableConfig | None = None, **kwargs) -> Any


   .. py:method:: save_state_history(config: langchain_core.runnables.RunnableConfig) -> None


   .. py:method:: stream(input_data: Any, thread_id: str | None = None, stream_mode: str = 'values', config: langchain_core.runnables.RunnableConfig | None = None, debug: bool | None = None, **kwargs) -> collections.abc.Generator[dict[str, Any], None, None]


   .. py:attribute:: _app
      :type:  Optional[langgraph.graph.graph.CompiledGraph]


   .. py:attribute:: _async_checkpointer
      :type:  Any | None


   .. py:attribute:: _checkpoint_mode
      :type:  Literal['sync', 'async']


   .. py:attribute:: _disable_checkpointing
      :type:  bool


   .. py:attribute:: checkpointer
      :type:  Any | None


   .. py:attribute:: config
      :type:  Any | None


   .. py:attribute:: engine
      :type:  Optional[haive.core.engine.base.Engine]


   .. py:attribute:: graph
      :type:  Optional[haive.core.graph.state_graph.base_graph2.BaseGraph]


   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel] | None


   .. py:attribute:: name
      :type:  str


   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel] | None


   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig | None


   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.state_schema.StateSchema] | None


   .. py:attribute:: store
      :type:  Any | None


   .. py:attribute:: verbose
      :type:  bool


