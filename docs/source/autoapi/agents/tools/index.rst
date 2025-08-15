agents.tools
============

.. py:module:: agents.tools


Attributes
----------

.. autoapisummary::

   agents.tools.logger


Functions
---------

.. autoapisummary::

   agents.tools.click
   agents.tools.go_back
   agents.tools.scroll
   agents.tools.to_google
   agents.tools.type_text
   agents.tools.wait


Module Contents
---------------

.. py:function:: click(state: dict[str, Any]) -> dict[str, Any]
   :async:


   Clicks on an element identified by its bounding box index.


   .. autolink-examples:: click
      :collapse:

.. py:function:: go_back(state: dict[str, Any]) -> dict[str, Any]
   :async:


   Navigates back in browser history.


   .. autolink-examples:: go_back
      :collapse:

.. py:function:: scroll(state: dict[str, Any]) -> dict[str, Any]
   :async:


   Scrolls either the window or a specific element.


   .. autolink-examples:: scroll
      :collapse:

.. py:function:: to_google(state: dict[str, Any]) -> dict[str, Any]
   :async:


   Navigates to Google homepage.


   .. autolink-examples:: to_google
      :collapse:

.. py:function:: type_text(state: dict[str, Any]) -> dict[str, Any]
   :async:


   Types text into an identified bounding box.


   .. autolink-examples:: type_text
      :collapse:

.. py:function:: wait(state: dict[str, Any]) -> dict[str, Any]
   :async:


   Waits for a fixed period (5s).


   .. autolink-examples:: wait
      :collapse:

.. py:data:: logger

