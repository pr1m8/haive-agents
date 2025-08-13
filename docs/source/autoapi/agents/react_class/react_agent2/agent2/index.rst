
:py:mod:`agents.react_class.react_agent2.agent2`
================================================

.. py:module:: agents.react_class.react_agent2.agent2


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.agent2.MessageNormalizingToolNode
   agents.react_class.react_agent2.agent2.ReactAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageNormalizingToolNode:

   .. graphviz::
      :align: center

      digraph inheritance_MessageNormalizingToolNode {
        node [shape=record];
        "MessageNormalizingToolNode" [label="MessageNormalizingToolNode"];
      }

.. autoclass:: agents.react_class.react_agent2.agent2.MessageNormalizingToolNode
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.react_class.react_agent2.config2.ReactAgentConfig]" -> "ReactAgent";
      }

.. autoclass:: agents.react_class.react_agent2.agent2.ReactAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.agent2.chat
   agents.react_class.react_agent2.agent2.create_react_agent
   agents.react_class.react_agent2.agent2.has_tool_calls
   agents.react_class.react_agent2.agent2.run
   agents.react_class.react_agent2.agent2.setup_workflow
   agents.react_class.react_agent2.agent2.should_use_tools
   agents.react_class.react_agent2.agent2.stream
   agents.react_class.react_agent2.agent2.structured_output_node

.. py:function:: chat() -> None

   Module-level chat function.


   .. autolink-examples:: chat
      :collapse:

.. py:function:: create_react_agent(tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | langchain_core.tools.Tool], model: str = 'gpt-4o', temperature: float = 0.7, system_prompt: str | None = None, name: str | None = None, max_iterations: int = 10, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, use_memory: bool = True, visualize: bool = True, debug: bool = False, structured_output_model: type[pydantic.BaseModel] | dict[str, Any] | None = None, additional_input_vars: list[str] | None = None, **kwargs) -> ReactAgent

   Create a React agent with the specified configuration.

   :param tools: List of tools for the agent
   :param model: Model name to use (default: "gpt-4o")
   :param temperature: Temperature for generation (default: 0.7)
   :param system_prompt: Optional system prompt
   :param name: Optional name for the agent
   :param max_iterations: Maximum number of iterations (default: 10)
   :param response_format: Optional schema for structured output
   :param use_memory: Whether to use memory (default: True)
   :param visualize: Whether to generate graph visualization (default: True)
   :param debug: Whether to enable debug mode (default: False)
   :param structured_output_model: Optional schema for structured output
   :param additional_input_vars: Additional input variables for prompt
   :param \*\*kwargs: Additional configuration parameters

   :returns: ReactAgent instance


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: has_tool_calls(state: dict[str, Any])

   Check if the last message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: run(agent, input_data)

   Module-level run function.


   .. autolink-examples:: run
      :collapse:

.. py:function:: setup_workflow()

   Module-level setup_workflow function.


   .. autolink-examples:: setup_workflow
      :collapse:

.. py:function:: should_use_tools(state)

   Module-level should_use_tools function.


   .. autolink-examples:: should_use_tools
      :collapse:

.. py:function:: stream(agent, input_data)

   Module-level stream function.


   .. autolink-examples:: stream
      :collapse:

.. py:function:: structured_output_node(state)

   Module-level structured_output_node function.


   .. autolink-examples:: structured_output_node
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.agent2
   :collapse:
   
.. autolink-skip:: next
