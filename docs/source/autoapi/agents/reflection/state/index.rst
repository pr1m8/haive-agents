agents.reflection.state
=======================

.. py:module:: agents.reflection.state

.. autoapi-nested-parse::

   State schema for Reflection Agent.


   .. autolink-examples:: agents.reflection.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reflection.state.ReflectionState


Functions
---------

.. autoapisummary::

   agents.reflection.state.add_improvement
   agents.reflection.state.finalize
   agents.reflection.state.should_continue


Module Contents
---------------

.. py:class:: ReflectionState

   Bases: :py:obj:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`


   State for Reflection Agent.


   .. autolink-examples:: ReflectionState
      :collapse:

   .. py:method:: add_improvement(improvement: haive.agents.reflection.models.Improvement) -> None

      Add improvement and update current content.


      .. autolink-examples:: add_improvement
         :collapse:


   .. py:method:: finalize() -> str

      Finalize the reflection process.


      .. autolink-examples:: finalize
         :collapse:


   .. py:method:: should_continue() -> bool

      Check if reflection should continue.


      .. autolink-examples:: should_continue
         :collapse:


   .. py:attribute:: critique
      :type:  haive.agents.reflection.models.Critique | None
      :value: None



   .. py:attribute:: current_content
      :type:  str
      :value: None



   .. py:attribute:: final_content
      :type:  str | None
      :value: None



   .. py:attribute:: improvements
      :type:  list[haive.agents.reflection.models.Improvement]
      :value: None



   .. py:attribute:: input
      :type:  str
      :value: None



   .. py:attribute:: iteration_count
      :type:  int
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: quality_threshold
      :type:  float
      :value: None



.. py:function:: add_improvement(state: ReflectionState, improvement: haive.agents.reflection.models.Improvement) -> None

   Add improvement to reflection state (module-level function).


   .. autolink-examples:: add_improvement
      :collapse:

.. py:function:: finalize(state: ReflectionState) -> str

   Finalize the reflection process (module-level function).


   .. autolink-examples:: finalize
      :collapse:

.. py:function:: should_continue(state: ReflectionState) -> bool

   Check if reflection should continue (module-level function).


   .. autolink-examples:: should_continue
      :collapse:

