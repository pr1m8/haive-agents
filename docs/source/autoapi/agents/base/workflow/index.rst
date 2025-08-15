agents.base.workflow
====================

.. py:module:: agents.base.workflow

.. autoapi-nested-parse::

   Workflow base class - Pure workflow orchestration without engine dependencies.

   This module provides the abstract Workflow class for building pure orchestration
   workflows that handle routing, transformation, and coordination without requiring
   language model engines.

   Classes:
       Workflow: Abstract base class for pure workflow orchestration.

   .. rubric:: Example

   Creating a simple data processing workflow::

       from haive.agents.base.workflow import Workflow

       class DataProcessor(Workflow):
           async def execute(self, data):
               # Pure processing logic, no LLM
               processed = transform_data(data)
               validated = validate_data(processed)
               return validated

       processor = DataProcessor(name="data_processor")
       result = await processor.execute(raw_data)

   .. seealso:: :class:`haive.agents.base.agent.Agent`: Full agent with engine support


   .. autolink-examples:: agents.base.workflow
      :collapse:


Classes
-------

.. autoapisummary::

   agents.base.workflow.Workflow


Module Contents
---------------

.. py:class:: Workflow(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


   Pure workflow orchestration without engine dependencies.

   Workflow handles pure orchestration - routing, transformation,
   coordination - without requiring engines. This is the foundation
   for building lightweight workflow components.

   .. attribute:: name

      Name of the workflow, auto-generated from class name if not provided.

   .. attribute:: verbose

      Enable verbose logging for detailed execution information.

   .. attribute:: debug

      Enable debug mode for additional diagnostics.

   .. rubric:: Examples

   Data processing workflow::

       class DataProcessor(Workflow):
           async def execute(self, data):
               # Pure processing, no LLM
               return processed_data

   Routing workflow::

       class Router(Workflow):
           async def execute(self, request):
               # Route to appropriate handler
               return route_decision

   .. note::

      This is an abstract base class. Subclasses must implement the
      execute() method to define the workflow logic.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Workflow
      :collapse:

   .. py:method:: __repr__() -> str

      String representation of the workflow.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: auto_generate_name(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Auto-generate workflow name from class name if not provided.

      Converts CamelCase class names to space-separated names for better
      readability in logs and debugging.

      :param values: Dictionary of field values before validation.

      :returns: Updated values dictionary with auto-generated name if needed.


      .. autolink-examples:: auto_generate_name
         :collapse:


   .. py:method:: execute(input_data: Any) -> Any
      :abstractmethod:

      :async:


      Execute the workflow logic.

      This method must be implemented by subclasses to define the
      specific workflow behavior.

      :param input_data: Input data for the workflow. Type depends on the
                         specific workflow implementation.

      :returns: Output data from the workflow. Type depends on the specific
                workflow implementation.

      :raises NotImplementedError: If not implemented by subclass.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: debug
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: verbose
      :type:  bool
      :value: None



