agents.document_modifiers.complex_extraction.agent
==================================================

.. py:module:: agents.document_modifiers.complex_extraction.agent

.. autoapi-nested-parse::

   Complex Extraction Agent for structured data extraction from text.

   This module provides the ComplexExtractionAgent class which implements sophisticated
   structured data extraction using validation with retries and optional JSONPatch-based
   error correction to reliably extract data according to specified schemas.

   The agent supports multiple retry strategies and can handle complex validation
   scenarios where initial extraction attempts may fail.

   Classes:
       ComplexExtractionAgent: Main agent for complex structured data extraction

   .. rubric:: Examples

   Basic usage::

       from haive.agents.document_modifiers.complex_extraction import ComplexExtractionAgent
       from haive.agents.document_modifiers.complex_extraction.config import ComplexExtractionAgentConfig
       from pydantic import BaseModel

       class PersonInfo(BaseModel):
           name: str
           age: int
           occupation: str

       config = ComplexExtractionAgentConfig(
           extraction_model=PersonInfo,
           max_retries=3
       )
       agent = ComplexExtractionAgent(config)

       text = "John Smith is a 35-year-old software engineer."
       result = agent.run(text)
       person_data = result["extracted_data"]

   With JSONPatch error correction::

       config = ComplexExtractionAgentConfig(
           extraction_model=PersonInfo,
           use_jsonpatch=True,
           max_retries=5
       )
       agent = ComplexExtractionAgent(config)
       result = agent.run(complex_text)

   .. seealso::

      - :class:`~haive.agents.document_modifiers.complex_extraction.config.ComplexExtractionAgentConfig`: Configuration class
      - :class:`~haive.agents.document_modifiers.complex_extraction.models.RetryStrategy`: Retry strategy configuration


   .. autolink-examples:: agents.document_modifiers.complex_extraction.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.agent.logger


Classes
-------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.agent.ComplexExtractionAgent


Module Contents
---------------

.. py:class:: ComplexExtractionAgent(config: haive.agents.document_modifiers.complex_extraction.config.ComplexExtractionAgentConfig = ComplexExtractionAgentConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.document_modifiers.complex_extraction.config.ComplexExtractionAgentConfig`\ ]


   Agent that extracts complex structured information from text.

   This agent implements sophisticated structured data extraction using validation
   with retries and optional JSONPatch-based error correction to reliably extract
   data according to specified Pydantic schemas.

   The agent creates a validation workflow that can handle complex extraction
   scenarios where initial attempts may fail due to parsing errors, validation
   issues, or incomplete data. It supports multiple retry strategies and can
   automatically correct errors using JSONPatch operations.

   :param config: Configuration object containing extraction settings, model schema,
                  retry parameters, and LLM configuration.

   .. attribute:: extraction_model

      Pydantic model class defining the extraction schema

   .. attribute:: max_retries

      Maximum number of retry attempts for failed extractions

   .. attribute:: force_tool_choice

      Whether to force the LLM to use the extraction tool

   .. attribute:: use_jsonpatch

      Whether to enable JSONPatch-based error correction

   .. attribute:: extraction_tool

      Tool instance created from the extraction model

   .. attribute:: llm

      Language model instance for performing extractions

   .. rubric:: Examples

   Basic structured extraction::

       from pydantic import BaseModel

       class ProductInfo(BaseModel):
           name: str
           price: float
           category: str

       config = ComplexExtractionAgentConfig(
           extraction_model=ProductInfo,
           max_retries=3
       )
       agent = ComplexExtractionAgent(config)

       text = "The MacBook Pro costs $2499 and is a laptop computer."
       result = agent.run(text)
       product = result["extracted_data"]
       # product = {"name": "MacBook Pro", "price": 2499.0, "category": "laptop"}

   With advanced error correction::

       config = ComplexExtractionAgentConfig(
           extraction_model=ProductInfo,
           use_jsonpatch=True,
           max_retries=5,
           force_tool_choice=True
       )
       agent = ComplexExtractionAgent(config)

   Processing multiple documents::

       documents = ["Product A costs $100", "Product B is $200 software"]
       results = [agent.run(doc) for doc in documents]

   .. note::

      The agent requires a Pydantic model class to define the extraction schema.
      JSONPatch functionality requires the 'jsonpatch' library to be installed.

   :raises ImportError: If JSONPatch is enabled but the jsonpatch library is not installed
   :raises ValueError: If extraction fails after maximum retry attempts

   .. seealso::

      - :class:`ComplexExtractionAgentConfig`: Configuration options
      - :class:`RetryStrategy`: Retry strategy configuration
      - :class:`PatchFunctionParameters`: JSONPatch parameter schema

   Initialize the complex extraction agent.

   Sets up the extraction model, validation tools, and retry mechanisms
   based on the provided configuration.

   :param config: Configuration object containing extraction model, retry settings,
                  and LLM configuration. Defaults to a new instance with default values.

   :raises ImportError: If JSONPatch is enabled in config but jsonpatch library
       is not installed.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexExtractionAgent
      :collapse:

   .. py:method:: _bind_validator_with_retries(llm: langchain_core.runnables.Runnable[collections.abc.Sequence[langchain_core.messages.AnyMessage], langchain_core.messages.AIMessage] | langchain_core.runnables.Runnable[collections.abc.Sequence[langchain_core.messages.BaseMessage], langchain_core.messages.BaseMessage], *, validator: langgraph.prebuilt.ValidationNode, retry_strategy: haive.agents.document_modifiers.complex_extraction.models.RetryStrategy, tool_choice: str | None = None) -> langgraph.graph.StateGraph

      Bind a tool validator with retry logic and return the graph builder.

      Creates a StateGraph that implements validation with retry logic for
      tool calls. The graph includes nodes for message counting, LLM execution,
      validation, fallback handling, and result finalization.

      :param llm: The language model runnable to generate responses. Can be either
                  a message-to-AIMessage or message-to-BaseMessage runnable.
      :param validator: Validation node for checking tool call validity against
                        the expected schema.
      :param retry_strategy: Strategy configuration for handling retries, including
                             max attempts, fallback behavior, and message aggregation.
      :param tool_choice: Optional tool name to force the LLM to use. If specified,
                          the LLM will be required to call this specific tool.

      :returns: StateGraph builder instance (not compiled). The graph must be compiled
                before use.

      .. note::

         The returned graph includes the following nodes:
         - count_messages: Tracks initial message count
         - llm: Primary LLM execution
         - validator: Tool call validation
         - fallback: Fallback LLM for retry attempts
         - finalizer: Result aggregation and finalization


      .. autolink-examples:: _bind_validator_with_retries
         :collapse:


   .. py:method:: _prepare_extraction_messages(input_data: str | list[str] | dict[str, Any] | pydantic.BaseModel) -> list[langchain_core.messages.BaseMessage]

      Prepare messages for extraction.

      Converts various input formats into a standardized list of BaseMessage
      objects that can be processed by the extraction workflow.

      :param input_data: Input data in various formats:
                         - str: Single text to extract from
                         - List[str]: Multiple texts to combine
                         - Dict[str, Any]: Dictionary with text content
                         - BaseModel: Pydantic model with extractable content
                         - BaseMessage or List[BaseMessage]: Pre-formatted messages

      :returns: List of BaseMessage objects formatted for extraction. The messages
                include appropriate prompts that instruct the LLM to extract data
                according to the configured extraction model.

      .. note::

         This method handles various edge cases and fallback scenarios to
         ensure robust message preparation regardless of input format.


      .. autolink-examples:: _prepare_extraction_messages
         :collapse:


   .. py:method:: _setup_extraction_tool() -> None

      Set up the extraction tool based on the provided model.

      Creates a LangChain Tool instance from the Pydantic extraction model
      that can be used by the LLM for structured data extraction.

      The tool is configured with the model's schema as the args_schema,
      allowing the LLM to understand the expected output format.


      .. autolink-examples:: _setup_extraction_tool
         :collapse:


   .. py:method:: bind_validator_with_jsonpatch_retries(llm: langchain_core.language_models.BaseChatModel, *, tools: list[langchain_core.tools.Tool], tool_choice: str | None = None, max_attempts: int = 3) -> langgraph.graph.StateGraph

      Bind a validator with JSONPatch-based retries.

      Creates an advanced validation workflow that uses JSONPatch operations
      to automatically correct validation errors. When a tool call fails
      validation, the system generates patch instructions to fix the errors.

      :param llm: The base language model to use for extraction and error correction.
      :param tools: List of tools available for extraction. The validation will
                    ensure tool calls conform to these tool schemas.
      :param tool_choice: Optional specific tool name to force the LLM to use.
                          If specified, the LLM must use this tool.
      :param max_attempts: Maximum number of retry attempts before giving up.
                           Defaults to 3.

      :returns: StateGraph builder instance (not compiled). Must be compiled before use.

      :raises ImportError: If the jsonpatch library is not installed but JSONPatch
          functionality is requested.

      .. note::

         This method creates a sophisticated retry mechanism where:
         1. Initial extraction attempts use the primary LLM
         2. Validation errors trigger JSONPatch correction attempts
         3. Patch operations are applied to fix specific validation issues
         4. Multiple correction iterations are supported up to max_attempts


      .. autolink-examples:: bind_validator_with_jsonpatch_retries
         :collapse:


   .. py:method:: bind_validator_with_retries(llm: langchain_core.language_models.BaseChatModel, *, tools: list[langchain_core.tools.Tool], tool_choice: str | None = None, max_attempts: int = 3) -> langgraph.graph.StateGraph

      Bind a validator with standard retries (no JSONPatch).

      Creates a basic validation workflow with simple retry logic. When
      validation fails, the system will retry the extraction up to the
      maximum number of attempts without advanced error correction.

      :param llm: The base language model to use for extraction attempts.
      :param tools: List of tools available for extraction. Tool calls will be
                    validated against these tool schemas.
      :param tool_choice: Optional specific tool name to force the LLM to use.
                          If specified, the LLM must call this tool.
      :param max_attempts: Maximum number of retry attempts before failing.
                           Defaults to 3.

      :returns: StateGraph builder instance (not compiled). Must be compiled before use.

      .. note::

         This is the simpler alternative to JSONPatch-based retries. It will
         simply retry failed extractions without attempting to automatically
         correct validation errors.


      .. autolink-examples:: bind_validator_with_retries
         :collapse:


   .. py:method:: extract_node(state: Any) -> dict[str, Any]

      Main extraction node function.

      Processes the current state through the extraction pipeline, invoking
      the configured extraction tool and handling the results.

      :param state: Current workflow state containing messages and other context.
                    Can be either a dictionary with 'messages' key or an object
                    with messages attribute.

      :returns:

                - extracted_data: The structured data extracted by the tool
                - messages: Updated message list including extraction results
                - error: Error message if extraction failed
      :rtype: Updated state dictionary containing

      .. note::

         This method handles various state formats and gracefully manages
         errors during extraction. If no extraction runnable is available,
         the state is passed through unchanged.


      .. autolink-examples:: extract_node
         :collapse:


   .. py:method:: run(input_data: str | list[str] | dict[str, Any] | pydantic.BaseModel, **kwargs) -> dict[str, Any]

      Run the extraction agent on input data.

      Processes the input through the extraction pipeline, handling various
      input formats and returning structured extraction results.

      :param input_data: Input text or data to extract information from. Supports:
                         - str: Single text document
                         - List[str]: Multiple text documents to process together
                         - Dict[str, Any]: Dictionary with 'text', 'content', or 'messages' keys
                         - BaseModel: Pydantic model with text content
      :param \*\*kwargs: Additional runtime configuration options passed to the
                         underlying workflow execution.

      :returns:

                - extracted_data: Structured data conforming to the extraction model
                - messages: Full conversation history during extraction
                - Additional metadata from the extraction process
      :rtype: Dictionary containing extraction results

      .. rubric:: Example

      Basic text extraction::

          agent = ComplexExtractionAgent(config)
          result = agent.run("John Smith is 30 years old.")
          person_data = result["extracted_data"]

      Multiple documents::

          docs = ["Person A info", "Person B info"]
          result = agent.run(docs)

      .. note::

         If no extraction workflow has been set up, this method will
         automatically call setup_workflow() before processing.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the agent workflow.

      Initializes the extraction workflow graph based on the agent configuration.
      This method creates the appropriate validation and retry mechanism (either
      JSONPatch-based or standard retries) and configures the processing pipeline.

      The workflow includes encoding/decoding steps, validation nodes, and
      state management for tracking extraction progress.

      .. note::

         This method is called automatically when needed and does not need
         to be invoked manually. The workflow graph is not compiled here -
         compilation happens in the parent class.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: extraction_model


   .. py:attribute:: extraction_runnable
      :value: None



   .. py:attribute:: extraction_tool
      :value: None



   .. py:attribute:: force_tool_choice


   .. py:attribute:: llm


   .. py:attribute:: max_retries


   .. py:attribute:: use_jsonpatch


.. py:data:: logger

