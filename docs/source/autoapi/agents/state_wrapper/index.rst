agents.state_wrapper
====================

.. py:module:: agents.state_wrapper


Attributes
----------

.. autoapisummary::

   agents.state_wrapper.logger
   agents.state_wrapper.state_wrapper


Classes
-------

.. autoapisummary::

   agents.state_wrapper.StateWrapper


Module Contents
---------------

.. py:class:: StateWrapper

   A wrapper for state dictionaries that stores Page objects separately.
   This avoids serialization issues by keeping non-serializable objects
   outside the state dictionary.


   .. autolink-examples:: StateWrapper
      :collapse:

   .. py:method:: get_object(key: str) -> Any

      Retrieve a stored non-serializable object.


      .. autolink-examples:: get_object
         :collapse:


   .. py:method:: get_page() -> playwright.async_api.Page | None

      Retrieve the stored Page object.


      .. autolink-examples:: get_page
         :collapse:


   .. py:method:: inject_page(state: dict[str, Any]) -> dict[str, Any]

      Re-inject the Page object into a state dict.

      :param state: The state dictionary to update

      :returns: Updated state with Page object added


      .. autolink-examples:: inject_page
         :collapse:


   .. py:method:: prepare_input(state: dict[str, Any]) -> dict[str, Any]

      Prepare state for LangGraph by removing any Page objects.

      :param state: The input state dictionary

      :returns: A new state dict with Page objects removed


      .. autolink-examples:: prepare_input
         :collapse:


   .. py:method:: set_page(page: playwright.async_api.Page) -> None

      Store the Page object.


      .. autolink-examples:: set_page
         :collapse:


   .. py:method:: store_object(key: str, obj: Any) -> None

      Store any other non-serializable object.


      .. autolink-examples:: store_object
         :collapse:


   .. py:attribute:: _other_objects
      :type:  dict[str, Any]


   .. py:attribute:: _page_instance
      :type:  playwright.async_api.Page | None
      :value: None



.. py:data:: logger

.. py:data:: state_wrapper

