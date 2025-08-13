
:py:mod:`agents.react_class.react_agent2.advanced_agent3`
=========================================================

.. py:module:: agents.react_class.react_agent2.advanced_agent3


Classes
-------

.. autoapisummary::

   agents.react_class.react_agent2.advanced_agent3.AdvancedReactAgent
   agents.react_class.react_agent2.advanced_agent3.AdvancedReactAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdvancedReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdvancedReactAgent {
        node [shape=record];
        "AdvancedReactAgent" [label="AdvancedReactAgent"];
        "haive.core.engine.agent.agent.Agent[AdvancedReactAgentConfig]" -> "AdvancedReactAgent";
      }

.. autoclass:: agents.react_class.react_agent2.advanced_agent3.AdvancedReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdvancedReactAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_AdvancedReactAgentConfig {
        node [shape=record];
        "AdvancedReactAgentConfig" [label="AdvancedReactAgentConfig"];
        "haive.agents.react_class.react_agent2.config2.ReactAgentConfig" -> "AdvancedReactAgentConfig";
      }

.. autoclass:: agents.react_class.react_agent2.advanced_agent3.AdvancedReactAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.advanced_agent3.add_tool
   agents.react_class.react_agent2.advanced_agent3.create_advanced_react_agent

.. py:function:: add_tool(agent, tool)

   Module-level add_tool function.


   .. autolink-examples:: add_tool
      :collapse:

.. py:function:: create_advanced_react_agent(system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, tools: list[langchain_core.tools.BaseTool] | None = None, tool_routing: dict[str, str] | None = None, name: str | None = None, structured_output_model: type[pydantic.BaseModel] | None = None, **kwargs) -> AdvancedReactAgent

   Create an advanced React agent with tool-specific routing.

   :param system_prompt: Optional system prompt
   :param model: Model name to use
   :param temperature: Temperature for generation
   :param tools: List of tools to use
   :param tool_routing: Mapping from tool names to node names
   :param name: Optional name for the agent
   :param structured_output_model: Optional schema for structured output
   :param \*\*kwargs: Additional configuration parameters

   :returns: AdvancedReactAgent instance


   .. autolink-examples:: create_advanced_react_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.advanced_agent3
   :collapse:
   
.. autolink-skip:: next
