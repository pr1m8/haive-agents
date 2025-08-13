
:py:mod:`agents.react_class.react_agent2.agent3`
================================================

.. py:module:: agents.react_class.react_agent2.agent3


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.agent3.ReactAgent
   agents.react_class.react_agent2.agent3.ReactAgentConfig
   agents.react_class.react_agent2.agent3.ReactAgentState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "haive.core.engine.agent.agent.Agent[ReactAgentConfig]" -> "ReactAgent";
      }

.. autoclass:: agents.react_class.react_agent2.agent3.ReactAgent
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
        "haive.core.engine.agent.agent.AgentConfig" -> "ReactAgentConfig";
      }

.. autoclass:: agents.react_class.react_agent2.agent3.ReactAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgentState {
        node [shape=record];
        "ReactAgentState" [label="ReactAgentState"];
        "pydantic.BaseModel" -> "ReactAgentState";
      }

.. autopydantic_model:: agents.react_class.react_agent2.agent3.ReactAgentState
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



Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.agent3.create_react_agent
   agents.react_class.react_agent2.agent3.from_tools
   agents.react_class.react_agent2.agent3.run
   agents.react_class.react_agent2.agent3.search
   agents.react_class.react_agent2.agent3.search
   agents.react_class.react_agent2.agent3.setup_workflow
   agents.react_class.react_agent2.agent3.structured_output_node

.. py:function:: create_react_agent(tools: list[langchain_core.tools.BaseTool], system_prompt: str = 'You are a helpful assistant with access to tools.', max_iterations: int = 5, model: str = 'gpt-4o', temperature: float = 0.7, parallel_tool_execution: bool = True, tool_routing: dict[str, str] | None = None, structured_output_model: type[pydantic.BaseModel] | None = None, name: str | None = None) -> ReactAgent

   Create a ReAct agent with the specified configuration.


   .. autolink-examples:: create_react_agent
      :collapse:

.. py:function:: from_tools(tools, **kwargs)

   Module-level from_tools function.


   .. autolink-examples:: from_tools
      :collapse:

.. py:function:: run(agent, input_data)

   Module-level run function.


   .. autolink-examples:: run
      :collapse:

.. py:function:: search(query: str) -> str

   Search for information about a topic.


   .. autolink-examples:: search
      :collapse:

.. py:function:: search(query)

   Module-level search function.


   .. autolink-examples:: search
      :collapse:

.. py:function:: setup_workflow()

   Module-level setup_workflow function.


   .. autolink-examples:: setup_workflow
      :collapse:

.. py:function:: structured_output_node(state)

   Module-level structured_output_node function.


   .. autolink-examples:: structured_output_node
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.agent3
   :collapse:
   
.. autolink-skip:: next
