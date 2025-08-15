agents.agent
============

.. py:module:: agents.agent


Attributes
----------

.. autoapisummary::

   agents.agent.logger


Classes
-------

.. autoapisummary::

   agents.agent.BBox
   agents.agent.Prediction
   agents.agent.WebNavAgent
   agents.agent.WebNavAgentConfig
   agents.agent.WebNavState


Functions
---------

.. autoapisummary::

   agents.agent.debug_print
   agents.agent.run_web_navigator


Module Contents
---------------

.. py:class:: BBox(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Bounding box for web elements.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BBox
      :collapse:

   .. py:attribute:: ariaLabel
      :type:  str | None
      :value: None



   .. py:attribute:: height
      :type:  float


   .. py:attribute:: text
      :type:  str | None
      :value: None



   .. py:attribute:: type
      :type:  str


   .. py:attribute:: width
      :type:  float


   .. py:attribute:: x
      :type:  float


   .. py:attribute:: y
      :type:  float


.. py:class:: Prediction(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Agent prediction model.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Prediction
      :collapse:

   .. py:method:: ensure_args(v) -> Any
      :classmethod:


      Ensures args is a list.


      .. autolink-examples:: ensure_args
         :collapse:


   .. py:attribute:: action
      :type:  str


   .. py:attribute:: args
      :type:  list[str] | None
      :value: None



   .. py:attribute:: thought
      :type:  str


.. py:class:: WebNavAgent(config: WebNavAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`WebNavAgentConfig`\ ]


   An interactive web navigation agent using Playwright & LangGraph with integrated tools.


   .. autolink-examples:: WebNavAgent
      :collapse:

   .. py:method:: annotate_page(state: dict[str, Any]) -> dict[str, Any]
      :async:


      Annotates the page with bounding boxes.


      .. autolink-examples:: annotate_page
         :collapse:


   .. py:method:: capture_screenshot() -> str
      :async:


      Captures a screenshot and returns a base64 string.


      .. autolink-examples:: capture_screenshot
         :collapse:


   .. py:method:: close()
      :async:


      Clean up resources.


      .. autolink-examples:: close
         :collapse:


   .. py:method:: format_descriptions(state: dict[str, Any]) -> str

      Formats bounding boxes into readable descriptions.


      .. autolink-examples:: format_descriptions
         :collapse:


   .. py:method:: parse_prediction(text: str) -> dict[str, Any]

      Parses LLM output into a structured prediction.


      .. autolink-examples:: parse_prediction
         :collapse:


   .. py:method:: run(question: str, show_images: bool = False) -> str | None
      :async:


      Run the agent on a given question and return the final answer.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: select_tool(state: dict[str, Any]) -> str

      Routes the agent's prediction to the correct tool.


      .. autolink-examples:: select_tool
         :collapse:


   .. py:method:: setup_workflow() -> None

      Sets up the workflow graph for the agent.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: start_browser()
      :async:


      Launch the browser and navigate to Google.


      .. autolink-examples:: start_browser
         :collapse:


   .. py:method:: stop_browser()
      :async:


      Closes the browser instance.


      .. autolink-examples:: stop_browser
         :collapse:


   .. py:method:: tool_answer(state: dict[str, Any]) -> str
      :async:


      Returns final answer to user query.


      .. autolink-examples:: tool_answer
         :collapse:


   .. py:method:: tool_click(state: dict[str, Any]) -> str
      :async:


      Clicks on an element identified by its bounding box index.


      .. autolink-examples:: tool_click
         :collapse:


   .. py:method:: tool_go_back(state: dict[str, Any]) -> str
      :async:


      Navigates back in browser history.


      .. autolink-examples:: tool_go_back
         :collapse:


   .. py:method:: tool_scroll(state: dict[str, Any]) -> str
      :async:


      Scrolls either the window or a specific element.


      .. autolink-examples:: tool_scroll
         :collapse:


   .. py:method:: tool_to_google(state: dict[str, Any]) -> str
      :async:


      Navigates to Google homepage.


      .. autolink-examples:: tool_to_google
         :collapse:


   .. py:method:: tool_type(state: dict[str, Any]) -> str
      :async:


      Types text into an identified bounding box.


      .. autolink-examples:: tool_type
         :collapse:


   .. py:method:: tool_wait(state: dict[str, Any]) -> str
      :async:


      Waits for a fixed period (3s).


      .. autolink-examples:: tool_wait
         :collapse:


   .. py:method:: update_scratchpad(state: dict[str, Any])

      Updates the scratchpad with the latest observation and agent's reasoning.


      .. autolink-examples:: update_scratchpad
         :collapse:


   .. py:attribute:: agent


   .. py:attribute:: browser
      :type:  playwright.async_api.Browser | None
      :value: None



   .. py:attribute:: config


   .. py:attribute:: headless


   .. py:attribute:: llm


   .. py:attribute:: max_steps


   .. py:attribute:: page
      :type:  playwright.async_api.Page | None
      :value: None



   .. py:attribute:: screenshots
      :value: []



   .. py:attribute:: state
      :type:  WebNavState | None
      :value: None



.. py:class:: WebNavAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Web Navigator Agent.


   .. autolink-examples:: WebNavAgentConfig
      :collapse:

   .. py:attribute:: aug_llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: headless
      :type:  bool
      :value: None



   .. py:attribute:: max_steps
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: WebNavState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Web Navigation State Model with Playwright Support.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WebNavState
      :collapse:

   .. py:method:: ensure_prediction(v) -> Any
      :classmethod:


      Ensures prediction is either None or a valid object.


      .. autolink-examples:: ensure_prediction
         :collapse:


   .. py:attribute:: bbox_descriptions
      :type:  str | None
      :value: None



   .. py:attribute:: bboxes
      :type:  list[BBox]
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
      :type:  str
      :value: None



   .. py:attribute:: page_url
      :type:  str | None
      :value: None



   .. py:attribute:: prediction
      :type:  Prediction | None
      :value: None



   .. py:attribute:: scratchpad
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



.. py:function:: debug_print(message: str)

   Helper function to print and log debug messages.


   .. autolink-examples:: debug_print
      :collapse:

.. py:function:: run_web_navigator()
   :async:


.. py:data:: logger

