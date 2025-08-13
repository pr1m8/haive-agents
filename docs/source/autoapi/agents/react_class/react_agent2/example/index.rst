
:py:mod:`agents.react_class.react_agent2.example`
=================================================

.. py:module:: agents.react_class.react_agent2.example



Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.example.action_executor_processor
   agents.react_class.react_agent2.example.analyze_data
   agents.react_class.react_agent2.example.data_analyzer_processor
   agents.react_class.react_agent2.example.execute_action
   agents.react_class.react_agent2.example.run_custom_tool_routing_example
   agents.react_class.react_agent2.example.search_db
   agents.react_class.react_agent2.example.search_web

.. py:function:: action_executor_processor(state: dict[str, Any]) -> dict[str, Any]

   Custom processor for action execution requests.


   .. autolink-examples:: action_executor_processor
      :collapse:

.. py:function:: analyze_data(data_id: str, analysis_type: str = 'basic') -> str

   Analyze specified data with analysis type (basic, detailed, predictive).


   .. autolink-examples:: analyze_data
      :collapse:

.. py:function:: data_analyzer_processor(state: dict[str, Any]) -> dict[str, Any]

   Custom processor for data analysis requests.


   .. autolink-examples:: data_analyzer_processor
      :collapse:

.. py:function:: execute_action(action_type: str, target_id: str) -> str

   Execute a business action on the specified target.


   .. autolink-examples:: execute_action
      :collapse:

.. py:function:: run_custom_tool_routing_example()

   Example of React agent with custom tool routing.


   .. autolink-examples:: run_custom_tool_routing_example
      :collapse:

.. py:function:: search_db(query: str) -> str

   Search an internal database for information.


   .. autolink-examples:: search_db
      :collapse:

.. py:function:: search_web(query: str) -> str

   Search the web for public information.


   .. autolink-examples:: search_web
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.example
   :collapse:
   
.. autolink-skip:: next
