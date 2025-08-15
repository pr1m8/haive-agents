agents.base.agent_structured_output_mixin
=========================================

.. py:module:: agents.base.agent_structured_output_mixin

.. autoapi-nested-parse::

   Mixin for adding structured output capabilities to agents.

   This mixin provides class methods for creating agents with structured output,
   enabling any agent to be composed with a StructuredOutputAgent for type-safe
   output conversion.


   .. autolink-examples:: agents.base.agent_structured_output_mixin
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.agent_structured_output_mixin.T
   agents.base.agent_structured_output_mixin.TAgent


Classes
-------

.. autoapisummary::

   agents.base.agent_structured_output_mixin.StructuredOutputMixin


Module Contents
---------------

.. py:class:: StructuredOutputMixin

   Mixin that adds structured output capabilities to any agent.


   .. autolink-examples:: StructuredOutputMixin
      :collapse:

   .. py:method:: as_structured_tool(output_model: type[T], name: str | None = None, description: str | None = None, **agent_kwargs) -> Any
      :classmethod:


      Convert agent to a tool that returns structured output.

      This creates a tool that:
      1. Runs the agent
      2. Converts output to structured format
      3. Returns the Pydantic model instance

      :param output_model: The Pydantic model for output
      :param name: Optional tool name
      :param description: Optional tool description
      :param \*\*agent_kwargs: Arguments for agent construction

      :returns: LangChain tool that returns structured output

      .. rubric:: Examples

      Create structured tool::

          research_tool = ResearchAgent.as_structured_tool(
              output_model=ResearchResult,
              name="research_tool",
              description="Research topics and return structured results"
          )

          # Use in another agent
          coordinator = ReactAgent(
              name="coordinator",
              tools=[research_tool]
          )


      .. autolink-examples:: as_structured_tool
         :collapse:


   .. py:method:: ensure_structured_output(output: Any, output_model: type[T], handle_errors: bool = True) -> T | None

      Ensure agent output conforms to a structured model.

      This instance method can be used to validate/convert output
      after execution, handling various output formats gracefully.

      :param output: The output to structure (str, BaseMessage, dict, etc.)
      :param output_model: The Pydantic model to convert to
      :param handle_errors: Whether to return None on errors (vs raising)

      :returns: Structured output instance or None if error and handle_errors=True

      .. rubric:: Examples

      In agent implementation::

          def run(self, input_text: str) -> Any:
              # Get raw output
              raw_output = self.engine.invoke(input_text)

              # Ensure it's structured
              return self.ensure_structured_output(
                  raw_output,
                  self.output_schema
              )


      .. autolink-examples:: ensure_structured_output
         :collapse:


   .. py:method:: with_structured_output(output_model: type[T], name: str | None = None, custom_context: str | None = None, custom_prompt: langchain_core.prompts.ChatPromptTemplate | None = None, **agent_kwargs) -> tuple[TAgent, haive.agents.base.agent.Agent]
      :classmethod:


      Create an agent paired with a StructuredOutputAgent for structured output.

      This method creates a two-agent workflow where:
      1. The original agent produces unstructured output
      2. A StructuredOutputAgent converts it to the specified model

      The agents are designed to work in sequence in a multi-agent workflow,
      with the structured output agent reading from messages state.

      :param output_model: The Pydantic model to structure output into
      :param name: Optional name for the agent (defaults to class name)
      :param custom_context: Optional context for extraction
      :param custom_prompt: Optional custom prompt template
      :param \*\*agent_kwargs: Arguments passed to the original agent constructor

      :returns: Tuple of (original_agent, structured_output_agent)

      .. rubric:: Examples

      Basic usage::

          # Create ReactAgent with structured output
          planner, structurer = ReactAgent.with_structured_output(
              output_model=PlanOutput,
              name="planner"
          )

          # Use in multi-agent workflow
          agents = [planner, structurer]

      Custom extraction::

          analyzer, structurer = SimpleAgent.with_structured_output(
              output_model=AnalysisResult,
              custom_context="Focus on quantitative metrics",
              temperature=0.7
          )

      In state definition::

          class WorkflowState(MultiAgentState):
              # AnalysisResult fields will be populated
              summary: str = ""
              metrics: Dict[str, float] = Field(default_factory=dict)
              confidence: float = 0.0


      .. autolink-examples:: with_structured_output
         :collapse:


.. py:data:: T

.. py:data:: TAgent

