agents.state
============

.. py:module:: agents.state


Classes
-------

.. autoapisummary::

   agents.state.WebNavState


Functions
---------

.. autoapisummary::

   agents.state.debug_print


Module Contents
---------------

.. py:class:: WebNavState(**kwargs)

   Bases: :py:obj:`pydantic.BaseModel`


   Web Navigation State Model with Playwright Support & Serialization.

   This model holds the state for a web navigation agent:
     - 'page': the live Playwright page (excluded from serialization)
     - 'page_url': the page URL (used for persistence)
     - Other fields (input, img, bboxes, prediction, scratchpad, observation)

   Extract page object and initialize the model.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WebNavState
      :collapse:

   .. py:method:: dict(**kwargs) -> dict[str, Any]

      For compatibility with older Pydantic versions.


      .. autolink-examples:: dict
         :collapse:


   .. py:method:: ensure_prediction(v) -> Any
      :classmethod:


      Ensures prediction is either None or a valid object.


      .. autolink-examples:: ensure_prediction
         :collapse:


   .. py:method:: from_page(page: playwright.async_api.Page, **kwargs) -> WebNavState
      :classmethod:

      :async:


      Create a WebNavState from a live Playwright page.
      Both the live 'page' and its URL are set.


      .. autolink-examples:: from_page
         :collapse:


   .. py:method:: model_dump(**kwargs) -> dict[str, Any]

      Override model_dump to exclude _page attribute.


      .. autolink-examples:: model_dump
         :collapse:


   .. py:method:: to_page(browser) -> playwright.async_api.Page
      :async:


      Recreate a live Playwright page from the stored URL.


      .. autolink-examples:: to_page
         :collapse:


   .. py:attribute:: _page
      :type:  playwright.async_api.Page | None
      :value: None



   .. py:attribute:: bboxes
      :type:  list[haive.agents.web_nav.models.BBox]
      :value: None



   .. py:attribute:: img
      :type:  str | None
      :value: None



   .. py:attribute:: input
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: observation
      :type:  str | None
      :value: None



   .. py:property:: page
      :type: playwright.async_api.Page | None


      Getter for page property.

      .. autolink-examples:: page
         :collapse:


   .. py:attribute:: page_url
      :type:  str | None
      :value: None



   .. py:attribute:: prediction
      :type:  haive.agents.web_nav.models.Prediction | None
      :value: None



   .. py:attribute:: scratchpad
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



.. py:function:: debug_print(message: str)

   Helper function to print and log debug messages.


   .. autolink-examples:: debug_print
      :collapse:

