agents.reasoning_and_critique.self_discover.v2.state
====================================================

.. py:module:: agents.reasoning_and_critique.self_discover.v2.state

.. autoapi-nested-parse::

   State schema for Self-Discovery reasoning system.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.v2.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.v2.state.SelfDiscoveryState


Module Contents
---------------

.. py:class:: SelfDiscoveryState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages.messages_state.MessagesState`


   State for self-discovery reasoning workflow.


   .. autolink-examples:: SelfDiscoveryState
      :collapse:

   .. py:attribute:: __shared_fields__
      :value: ['messages', 'reasoning_modules', 'task_description', 'selected_modules', 'adapted_modules',...



   .. py:attribute:: adapted_modules
      :type:  str | None
      :value: None



   .. py:attribute:: answer
      :type:  str | None
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: reasoning_modules
      :type:  str
      :value: None



   .. py:attribute:: reasoning_structure
      :type:  str | None
      :value: None



   .. py:attribute:: selected_modules
      :type:  str | None
      :value: None



   .. py:attribute:: task_description
      :type:  str
      :value: None



