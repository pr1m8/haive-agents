meta.agent
==========

.. py:module:: meta.agent

.. autoapi-nested-parse::

   Generic MetaAgent class for agent composition and recompilation management.


   .. autolink-examples:: meta.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   meta.agent.TAgent


Classes
-------

.. autoapisummary::

   meta.agent.MetaAgent
   meta.agent.MetaAgentState


Functions
---------

.. autoapisummary::

   meta.agent.get_summary
   meta.agent.meta_execute
   meta.agent.needs_recompilation
   meta.agent.recompile
   meta.agent.run
   meta.agent.setup_agent
   meta.agent.update_wrapped_agent
   meta.agent.wrap
   meta.agent.wrapped_agent


Module Contents
---------------

.. py:class:: MetaAgent(wrapped_agent: TAgent, name: str | None = None, engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`, :py:obj:`Generic`\ [\ :py:obj:`TAgent`\ ]


   Generic meta agent that can wrap any agent type.

   This provides a generic wrapper around any agent, adding:
   - Recompilation tracking and management
   - Graph composition capabilities
   - Nested execution with state management
   - Dynamic agent modification

   Usage:
       .. code-block:: python

           # Wrap any agent type
           simple_agent = SimpleAgent(name="worker", engine=engine)
           meta_simple = MetaAgent[SimpleAgent](wrapped_agent=simple_agent)

           # Execute through meta layer
           result = await meta_simple.execute()

           # Check recompilation
           if meta_simple.needs_recompilation():
           meta_simple.recompile()


   Initialize meta agent with wrapped agent.

   :param wrapped_agent: The agent to wrap with meta capabilities
   :param name: Optional name (defaults to "meta_{wrapped_agent.name}")
   :param engine: Optional engine (uses wrapped agent's engine if not provided)
   :param \*\*kwargs: Additional arguments for Agent base class


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MetaAgent
      :collapse:

   .. py:method:: __repr__() -> str

      String representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: arun(*args, **kwargs) -> Any
      :async:


      Execute wrapped agent through meta layer.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: build_graph() -> Any

      Build graph for meta agent execution.

      The meta agent delegates to the wrapped agent's graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_summary() -> dict[str, Any]

      Get execution and recompilation summary.


      .. autolink-examples:: get_summary
         :collapse:


   .. py:method:: needs_recompilation() -> bool

      Check if wrapped agent needs recompilation.


      .. autolink-examples:: needs_recompilation
         :collapse:


   .. py:method:: recompile(reason: str = 'Manual recompilation') -> dict[str, Any]

      Recompile the wrapped agent if needed.


      .. autolink-examples:: recompile
         :collapse:


   .. py:method:: run(*args, **kwargs) -> Any

      Sync version of arun.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup meta agent with wrapped agent.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: update_wrapped_agent(new_agent: TAgent) -> None

      Update the wrapped agent dynamically.


      .. autolink-examples:: update_wrapped_agent
         :collapse:


   .. py:method:: wrap(agent: TAgent, **kwargs) -> MetaAgent[TAgent]
      :classmethod:


      Factory method to wrap any agent with meta capabilities.

      :param agent: The agent to wrap
      :param \*\*kwargs: Additional arguments for MetaAgent

      :returns: MetaAgent wrapping the provided agent


      .. autolink-examples:: wrap
         :collapse:


   .. py:property:: wrapped_agent
      :type: TAgent


      Get the wrapped agent.

      .. autolink-examples:: wrapped_agent
         :collapse:


.. py:class:: MetaAgentState

   Bases: :py:obj:`haive.core.schema.StateSchema`


   State for generic meta agents.


   .. autolink-examples:: MetaAgentState
      :collapse:

   .. py:attribute:: execution_count
      :type:  int
      :value: None



   .. py:attribute:: last_recompilation_reason
      :type:  str
      :value: None



   .. py:attribute:: last_result
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: meta_state
      :type:  haive.core.schema.prebuilt.meta_state.MetaStateSchema
      :value: None



   .. py:attribute:: recompilation_count
      :type:  int
      :value: None



   .. py:attribute:: wrapped_agent_ref
      :type:  Any | None
      :value: None



.. py:function:: get_summary(meta_agent: MetaAgent) -> dict[str, Any]

   Get summary of meta agent execution and recompilation.


   .. autolink-examples:: get_summary
      :collapse:

.. py:function:: meta_execute(meta_agent: MetaAgent, *args, **kwargs) -> Any
   :async:


   Execute a meta agent asynchronously.


   .. autolink-examples:: meta_execute
      :collapse:

.. py:function:: needs_recompilation(meta_agent: MetaAgent) -> bool

   Check if meta agent needs recompilation.


   .. autolink-examples:: needs_recompilation
      :collapse:

.. py:function:: recompile(meta_agent: MetaAgent, reason: str = 'Manual recompilation') -> dict[str, Any]

   Recompile a meta agent.


   .. autolink-examples:: recompile
      :collapse:

.. py:function:: run(meta_agent: MetaAgent, *args, **kwargs) -> Any

   Run a meta agent.


   .. autolink-examples:: run
      :collapse:

.. py:function:: setup_agent(meta_agent: MetaAgent) -> None

   Setup a meta agent.


   .. autolink-examples:: setup_agent
      :collapse:

.. py:function:: update_wrapped_agent(meta_agent: MetaAgent, new_agent: TAgent) -> None

   Update the wrapped agent in a meta agent.


   .. autolink-examples:: update_wrapped_agent
      :collapse:

.. py:function:: wrap(agent: TAgent, **kwargs) -> MetaAgent[TAgent]

   Convenience function to wrap an agent with meta capabilities.


   .. autolink-examples:: wrap
      :collapse:

.. py:function:: wrapped_agent(meta_agent: MetaAgent) -> Any

   Get the wrapped agent from a meta agent.


   .. autolink-examples:: wrapped_agent
      :collapse:

.. py:data:: TAgent

