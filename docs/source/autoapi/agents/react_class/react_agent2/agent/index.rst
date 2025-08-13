
:py:mod:`agents.react_class.react_agent2.agent`
===============================================

.. py:module:: agents.react_class.react_agent2.agent


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.agent.ReactAgent
   agents.react_class.react_agent2.agent.ReactAgentConfig
   agents.react_class.react_agent2.agent.ReactAgentSchema
   agents.react_class.react_agent2.agent.ReactAgentSchemaWithStructuredResponse


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "ReactAgent";
      }

.. autoclass:: agents.react_class.react_agent2.agent.ReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgentConfig {
        node [shape=record];
        "ReactAgentConfig" [label="ReactAgentConfig"];
        "pydantic.BaseModel" -> "ReactAgentConfig";
      }

.. autopydantic_model:: agents.react_class.react_agent2.agent.ReactAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgentSchema:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgentSchema {
        node [shape=record];
        "ReactAgentSchema" [label="ReactAgentSchema"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "ReactAgentSchema";
      }

.. autoclass:: agents.react_class.react_agent2.agent.ReactAgentSchema
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgentSchemaWithStructuredResponse:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgentSchemaWithStructuredResponse {
        node [shape=record];
        "ReactAgentSchemaWithStructuredResponse" [label="ReactAgentSchemaWithStructuredResponse"];
        "ReactAgentSchema" -> "ReactAgentSchemaWithStructuredResponse";
      }

.. autoclass:: agents.react_class.react_agent2.agent.ReactAgentSchemaWithStructuredResponse
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.agent.create_react_agent
   agents.react_class.react_agent2.agent.tools_condition

.. py:function:: create_react_agent(tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool | collections.abc.Callable], model: str = 'gpt-4o', temperature: float = 0.7, system_prompt: str | None = None, name: str | None = None, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, max_iterations: int = 10, checkpointer: langgraph.types.Checkpointer | None = None, store: langgraph.store.base.BaseStore | None = None, interrupt_before: list[str] | None = None, interrupt_after: list[str] | None = None, debug: bool = False, version: Literal['v1', 'v2'] = 'v1', visualize: bool = True, tool_routing: dict[str, str] | None = None, **kwargs) -> ReactAgent

   Create a React agent that follows the reasoning-action-observation pattern.

   :param tools: List of tools available to the agent
   :param model: LLM model name to use
   :param temperature: Temperature for generation
   :param system_prompt: System prompt text
   :param name: Optional name for the agent
   :param response_format: Schema for structured output
   :param max_iterations: Maximum number of reasoning steps
   :param checkpointer: Optional checkpointer for persistence
   :param store: Optional store for cross-thread data
   :param interrupt_before: List of node names to interrupt before
   :param interrupt_after: List of node names to interrupt after
   :param debug: Whether to enable debug mode
   :param version: Graph version (v1 or v2)
   :param \*\*kwargs: Additional configuration parameters

   :returns: ReactAgent instance


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: tools_condition(state: dict[str, Any], messages_key: str = 'messages') -> Literal['tools', '__end__']

   Determine if the state should route to tools or end based on the last message.

   :param state: State to check for tool calls
   :param messages_key: Key to find messages in state

   :returns: "tools" if tool calls present, "__end__" otherwise


   .. autolink-examples:: tools_condition
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.agent
   :collapse:
   
.. autolink-skip:: next
