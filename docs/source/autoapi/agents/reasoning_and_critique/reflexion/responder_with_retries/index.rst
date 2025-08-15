agents.reasoning_and_critique.reflexion.responder_with_retries
==============================================================

.. py:module:: agents.reasoning_and_critique.reflexion.responder_with_retries


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflexion.responder_with_retries.ResponderWithRetries


Module Contents
---------------

.. py:class:: ResponderWithRetries(aug_llm_config: haive.core.engine.aug_llm.AugLLMConfig, num_retries: int = 3, name: str | None = None)

   A responder that retries a given runnable a number of times if it fails to validate.

   Args:
   aug_llm_config: The config for the LLM to use.
   num_retries: The number of times to retry the runnable.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResponderWithRetries
      :collapse:

   .. py:method:: respond(state: pydantic.BaseModel)

      Respond to the user's message.


      .. autolink-examples:: respond
         :collapse:


   .. py:attribute:: aug_llm_config


   .. py:attribute:: name
      :value: None



   .. py:attribute:: num_retries
      :value: 3



   .. py:attribute:: runnable


   .. py:attribute:: validator


