
:py:mod:`agents.react_class.react_agent2.dynamic_agent`
=======================================================

.. py:module:: agents.react_class.react_agent2.dynamic_agent

Dynamic React Agent - an extension of React agent with tool selection capabilities.


.. autolink-examples:: agents.react_class.react_agent2.dynamic_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.dynamic_agent.DynamicReactAgent
   agents.react_class.react_agent2.dynamic_agent.DynamicReactAgentConfig
   agents.react_class.react_agent2.dynamic_agent.DynamicReactAgentState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicReactAgent {
        node [shape=record];
        "DynamicReactAgent" [label="DynamicReactAgent"];
        "haive.agents.react_class.react_agent2.agent2.ReactAgent" -> "DynamicReactAgent";
      }

.. autoclass:: agents.react_class.react_agent2.dynamic_agent.DynamicReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicReactAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicReactAgentConfig {
        node [shape=record];
        "DynamicReactAgentConfig" [label="DynamicReactAgentConfig"];
        "haive.agents.react_class.react_agent2.config2.ReactAgentConfig" -> "DynamicReactAgentConfig";
      }

.. autoclass:: agents.react_class.react_agent2.dynamic_agent.DynamicReactAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicReactAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicReactAgentState {
        node [shape=record];
        "DynamicReactAgentState" [label="DynamicReactAgentState"];
        "haive.agents.react_class.react_agent2.state2.ReactAgentState" -> "DynamicReactAgentState";
      }

.. autoclass:: agents.react_class.react_agent2.dynamic_agent.DynamicReactAgentState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.dynamic_agent.create_dynamic_react_agent

.. py:function:: create_dynamic_react_agent(tools: list[langchain_core.tools.BaseTool], system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, name: str | None = None, max_tools_per_turn: int = 5, max_iterations: int = 10, response_format: type[pydantic.BaseModel] | dict[str, Any] | None = None, use_memory: bool = True, visualize: bool = True, repeat_selection: bool = True, vector_store_config: haive.core.models.vectorstore.base.VectorStoreConfig | None = None, tool_documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> DynamicReactAgent

   Create a dynamic react agent with minimal configuration.

   :param tools: List of tools the agent can use
   :param system_prompt: Optional system prompt
   :param model: Model name to use
   :param temperature: Temperature for generation
   :param name: Optional agent name
   :param max_tools_per_turn: Maximum number of tools to select per turn
   :param max_iterations: Maximum iterations for React agent
   :param response_format: Optional structured output model
   :param use_memory: Whether to use memory
   :param visualize: Whether to visualize the graph
   :param repeat_selection: Whether to repeat tool selection after each tool invocation
   :param vector_store_config: Optional vector store configuration
   :param tool_documents: Optional pre-created tool documents
   :param \*\*kwargs: Additional configuration parameters

   :returns: DynamicReactAgent instance


   .. autolink-examples:: create_dynamic_react_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.dynamic_agent
   :collapse:
   
.. autolink-skip:: next
