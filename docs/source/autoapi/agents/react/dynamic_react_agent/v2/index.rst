agents.react.dynamic_react_agent.v2
===================================

.. py:module:: agents.react.dynamic_react_agent.v2

.. autoapi-nested-parse::

   Dynamic React Agent with Tool Loading Capabilities.

   This module provides DynamicReactAgent, an enhanced ReactAgent that can
   dynamically discover, load, and activate tools based on task requirements
   using the Dynamic Activation Pattern.

   Based on:
   - @project_docs/active/patterns/dynamic_activation_pattern.md
   - @notebooks/tool_loader.ipynb pattern for tool loading
   - @packages/haive-agents/examples/supervisor/advanced/dynamic_activation_example.py


   .. autolink-examples:: agents.react.dynamic_react_agent.v2
      :collapse:


Classes
-------

.. autoapisummary::

   agents.react.dynamic_react_agent.v2.DynamicReactAgent
   agents.react.dynamic_react_agent.v2.DynamicToolState


Module Contents
---------------

.. py:class:: DynamicReactAgent

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   ReactAgent with dynamic tool loading capabilities.

   This agent extends ReactAgent with the ability to dynamically discover,
   load, and activate tools based on task requirements. It uses the Dynamic
   Activation Pattern with MetaStateSchema for component tracking.

   Key Features:
       - Dynamic tool discovery using ComponentDiscoveryAgent
       - Automatic tool loading from documentation
       - Tool activation and deactivation management
       - Usage tracking and statistics
       - Recompilation support for new tools
       - MetaStateSchema integration for tracking

   :param name: Agent name
   :param engine: AugLLMConfig for the agent
   :param state_schema: DynamicToolState (set automatically)

   Private Attributes:
       _discovery_agent: ComponentDiscoveryAgent for finding tools
       _meta_self: MetaStateSchema wrapper for self-tracking
       _tool_loader: Tool loader for actual tool instantiation

   .. rubric:: Examples

   Basic dynamic tool loading::

       from haive.agents.react.dynamic_react_agent import DynamicReactAgent
       from haive.core.engine.aug_llm import AugLLMConfig

       # Create agent with discovery
       agent = DynamicReactAgent.create_with_discovery(
           name="dynamic_react",
           document_path="@haive-tools",
           engine=AugLLMConfig()
       )

       # Task that needs specific tools
       result = await agent.arun("Calculate compound interest and create a chart")

       # Agent automatically discovers and loads needed tools
       active_tools = agent.get_active_tool_names()
       print(f"Tools used: {', '.join(active_tools)}")

   Manual tool discovery::

       # Discover tools for specific task
       tools = await agent.discover_and_load_tools("data visualization")
       print(f"Loaded {len(tools)} tools for visualization")

       # Use agent with newly loaded tools
       result = await agent.arun("Create a bar chart from this data")

   Tool management::

       # Get tool usage statistics
       stats = agent.get_tool_usage_stats()
       print(f"Most used tool: {max(stats, key=stats.get)}")

       # Categorize tools
       agent.categorize_tool("calculator", "math")
       agent.categorize_tool("chart_maker", "visualization")


   .. autolink-examples:: DynamicReactAgent
      :collapse:

   .. py:method:: _add_dynamic_tool_discovery_tool() -> None

      Add the dynamic tool discovery tool to the agent.

      This tool allows the agent to search for and request new tools
      dynamically based on task requirements.


      .. autolink-examples:: _add_dynamic_tool_discovery_tool
         :collapse:


   .. py:method:: _extract_tool_name(line: str) -> str

      Extract tool name from a line of text.

      :param line: Line of text containing tool information

      :returns: Extracted tool name or empty string


      .. autolink-examples:: _extract_tool_name
         :collapse:


   .. py:method:: _infer_tool_category(task: str, tool_doc: dict[str, Any]) -> str | None

      Infer tool category based on task and tool documentation.

      :param task: Task description
      :param tool_doc: Tool document

      :returns: Inferred category or None


      .. autolink-examples:: _infer_tool_category
         :collapse:


   .. py:method:: _load_tool_from_document(tool_doc: dict[str, Any]) -> langchain_core.tools.BaseTool | None
      :async:


      Load actual tool instance from tool document.

      :param tool_doc: Tool document from discovery

      :returns: Loaded BaseTool instance or None


      .. autolink-examples:: _load_tool_from_document
         :collapse:


   .. py:method:: _load_tool_from_suggestion(suggestion: dict[str, Any]) -> langchain_core.tools.BaseTool | None
      :async:


      Load a tool from a RAG suggestion.

      :param suggestion: Tool suggestion from RAG parsing

      :returns: Loaded tool instance or None


      .. autolink-examples:: _load_tool_from_suggestion
         :collapse:


   .. py:method:: _parse_rag_tool_suggestions(rag_result: str, task: str) -> list[dict[str, Any]]

      Parse RAG result to extract tool suggestions.

      :param rag_result: Result from RAG agent
      :param task: Original task description

      :returns: List of tool suggestions with metadata


      .. autolink-examples:: _parse_rag_tool_suggestions
         :collapse:


   .. py:method:: _recompile_with_new_tools(new_tools: list[langchain_core.tools.BaseTool]) -> None
      :async:


      Recompile agent graph with new tools.

      :param new_tools: List of new tools to add


      .. autolink-examples:: _recompile_with_new_tools
         :collapse:


   .. py:method:: _register_initial_tools(tools: list[dict[str, Any]]) -> None

      Register initial tools during agent setup.

      This method registers tools that were provided during agent creation
      through the factory method. It's called during setup_agent() after
      the agent's state schema is properly initialized.

      :param tools: List of tool dictionaries to register


      .. autolink-examples:: _register_initial_tools
         :collapse:


   .. py:method:: _setup_rag_tool_agent() -> None

      Setup RAG-based tool discovery agent.

      This creates a BaseRAGAgent that can search through tool documentation
      to find and suggest appropriate tools for tasks.


      .. autolink-examples:: _setup_rag_tool_agent
         :collapse:


   .. py:method:: _setup_tool_loader() -> None

      Setup tool loader for dynamic tool instantiation.

      This sets up the tool loading mechanism based on the pattern
      from @notebooks/tool_loader.ipynb.


      .. autolink-examples:: _setup_tool_loader
         :collapse:


   .. py:method:: activate_tool_by_name(tool_name: str) -> bool
      :async:


      Activate a tool by name.

      :param tool_name: Name of tool to activate

      :returns: True if activation succeeded

      .. rubric:: Examples

      Activate specific tool::

          success = await agent.activate_tool_by_name("calculator")
          if success:
              print("Calculator activated successfully")


      .. autolink-examples:: activate_tool_by_name
         :collapse:


   .. py:method:: categorize_tool(tool_name: str, category: str) -> None

      Categorize a tool by type.

      :param tool_name: Name of the tool
      :param category: Category to assign the tool to

      .. rubric:: Examples

      Categorize tools::

          agent.categorize_tool("calculator", "math")
          agent.categorize_tool("web_search", "web")


      .. autolink-examples:: categorize_tool
         :collapse:


   .. py:method:: create_with_discovery(name: str, document_path: str, engine: haive.core.engine.aug_llm.AugLLMConfig, use_mcp: bool = False, **kwargs) -> DynamicReactAgent
      :classmethod:


      Factory method to create agent with discovery capabilities.

      :param name: Agent name
      :param document_path: Path to documentation for tool discovery
      :param engine: AugLLMConfig for the agent
      :param use_mcp: Whether to use MCP (Model Context Protocol) for tools
      :param \*\*kwargs: Additional arguments for agent

      :returns: DynamicReactAgent with discovery capabilities

      .. rubric:: Examples

      Create with Haive tools::

          agent = DynamicReactAgent.create_with_discovery(
              name="haive_react",
              document_path="@haive-tools",
              engine=AugLLMConfig()
          )

      Create with custom tools and MCP::

          agent = DynamicReactAgent.create_with_discovery(
              name="custom_react",
              document_path="/path/to/custom/tools",
              engine=AugLLMConfig(temperature=0.3),
              use_mcp=True
          )


      .. autolink-examples:: create_with_discovery
         :collapse:


   .. py:method:: create_with_rag_tooling(name: str, engine: haive.core.engine.aug_llm.AugLLMConfig, rag_documents: list[str], tool_documents: list[str] | None = None, use_mcp: bool = False, **kwargs) -> DynamicReactAgent
      :classmethod:


      Factory method to create agent with RAG-based tool discovery.

      This creates a DynamicReactAgent that can request tools from a RAG agent
      based on document content. The agent will have both reasoning capabilities
      and the ability to discover and use tools dynamically.

      :param name: Agent name
      :param engine: AugLLMConfig for the agent
      :param rag_documents: List of documents for RAG knowledge base
      :param tool_documents: Optional separate documents for tool discovery
      :param use_mcp: Whether to use MCP (Model Context Protocol) for tools
      :param \*\*kwargs: Additional arguments for agent

      :returns: DynamicReactAgent with RAG-based tool discovery

      .. rubric:: Examples

      Create with RAG knowledge and tool discovery::

          documents = [
              "Python programming guide with examples",
              "Data analysis techniques and tools",
              "Machine learning algorithms overview"
          ]

          agent = DynamicReactAgent.create_with_rag_tooling(
              name="rag_react",
              engine=AugLLMConfig(),
              rag_documents=documents
          )

      Create with separate tool discovery documents::

          knowledge_docs = ["Domain knowledge documents..."]
          tool_docs = ["Tool documentation and examples..."]

          agent = DynamicReactAgent.create_with_rag_tooling(
              name="specialized_react",
              engine=AugLLMConfig(),
              rag_documents=knowledge_docs,
              tool_documents=tool_docs,
              use_mcp=True
          )


      .. autolink-examples:: create_with_rag_tooling
         :collapse:


   .. py:method:: create_with_tools(name: str, tools: list[dict[str, Any]], engine: haive.core.engine.aug_llm.AugLLMConfig, **kwargs) -> DynamicReactAgent
      :classmethod:


      Factory method to create agent with pre-registered tools.

      :param name: Agent name
      :param tools: List of tool dictionaries to register
      :param engine: AugLLMConfig for the agent
      :param \*\*kwargs: Additional arguments for agent

      :returns: DynamicReactAgent with pre-registered tools

      .. rubric:: Examples

      Create with specific tools::

          from langchain_core.tools import tool

          @tool
          def calculator(expression: str) -> float:
              '''Calculate mathematical expression.'''
              return eval(expression)

          tools = [
              {
                  "id": "calc",
                  "name": "Calculator",
                  "description": "Mathematical calculations",
                  "component": calculator,
                  "category": "math"
              }
          ]

          agent = DynamicReactAgent.create_with_tools(
              name="tool_react",
              tools=tools,
              engine=AugLLMConfig()
          )


      .. autolink-examples:: create_with_tools
         :collapse:


   .. py:method:: deactivate_tool_by_name(tool_name: str) -> bool

      Deactivate a tool by name.

      :param tool_name: Name of tool to deactivate

      :returns: True if deactivation succeeded

      .. rubric:: Examples

      Deactivate specific tool::

          success = agent.deactivate_tool_by_name("calculator")
          if success:
              print("Calculator deactivated successfully")


      .. autolink-examples:: deactivate_tool_by_name
         :collapse:


   .. py:method:: discover_and_load_tools(task: str) -> list[langchain_core.tools.BaseTool]
      :async:


      Discover and load tools for a specific task.

      :param task: Task description to find tools for

      :returns: List of loaded BaseTool instances

      .. rubric:: Examples

      Discover tools for calculation::

          tools = await agent.discover_and_load_tools("mathematical calculations")
          print(f"Loaded {len(tools)} math tools")

      Discover tools for data processing::

          tools = await agent.discover_and_load_tools("data analysis and visualization")
          for tool in tools:
              print(f"Loaded tool: {tool.name}")


      .. autolink-examples:: discover_and_load_tools
         :collapse:


   .. py:method:: discover_and_load_tools_legacy(task: str) -> list[langchain_core.tools.BaseTool]
      :async:


      Legacy version of discover_and_load_tools for backward compatibility.


      .. autolink-examples:: discover_and_load_tools_legacy
         :collapse:


   .. py:method:: get_active_tool_names() -> list[str]

      Get names of all active tools.

      :returns: List of active tool names

      .. rubric:: Examples

      List active tools::

          tool_names = agent.get_active_tool_names()
          print(f"Active tools: {', '.join(tool_names)}")


      .. autolink-examples:: get_active_tool_names
         :collapse:


   .. py:method:: get_registry_stats() -> dict[str, Any]

      Get statistics about the tool registry.

      :returns: Dictionary with registry statistics

      .. rubric:: Examples

      Show registry status::

          stats = agent.get_registry_stats()
          print(f"Total tools: {stats['total_components']}")
          print(f"Active tools: {stats['active_components']}")
          print(f"Most used: {stats['most_used_component']}")


      .. autolink-examples:: get_registry_stats
         :collapse:


   .. py:method:: get_tool_usage_stats() -> dict[str, int]

      Get tool usage statistics.

      :returns: Dictionary of tool name to usage count

      .. rubric:: Examples

      Get usage statistics::

          stats = agent.get_tool_usage_stats()
          most_used = max(stats.items(), key=lambda x: x[1])
          print(f"Most used tool: {most_used[0]} ({most_used[1]} times)")


      .. autolink-examples:: get_tool_usage_stats
         :collapse:


   .. py:method:: get_tools_by_category(category: str) -> list[str]

      Get tools in a specific category.

      :param category: Category to get tools for

      :returns: List of tool names in the category

      .. rubric:: Examples

      Get math tools::

          math_tools = agent.get_tools_by_category("math")
          print(f"Math tools: {', '.join(math_tools)}")


      .. autolink-examples:: get_tools_by_category
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the dynamic React agent.

      This method is called during agent initialization to set up
      the agent's internal state and discovery capabilities.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _meta_self
      :type:  haive.core.schema.prebuilt.meta_state.MetaStateSchema | None
      :value: None



   .. py:attribute:: _tool_loader
      :type:  Any | None
      :value: None



   .. py:attribute:: discovery_agent
      :type:  haive.agents.discovery.component_discovery_agent.ComponentDiscoveryAgent | None
      :value: None



   .. py:attribute:: rag_tool_agent
      :type:  Any | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[DynamicToolState]


   .. py:attribute:: tools_to_register
      :type:  list[dict[str, Any]] | None
      :value: None



.. py:class:: DynamicToolState

   Bases: :py:obj:`haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState`


   Specialized state for dynamic tool management.

   Extends DynamicActivationState with tool-specific functionality
   for ReactAgent tool loading and management.

   :param tool_categories: Categorization of tools by type
   :param tool_usage_stats: Usage statistics for each tool
   :param last_tool_discovery: Timestamp of last tool discovery
   :param discovery_queries: History of discovery queries

   .. rubric:: Examples

   Basic tool state usage::

       state = DynamicToolState()

       # Track tool categories
       state.tool_categories = {
           "math": ["calculator", "statistics"],
           "web": ["search", "scraper"],
           "file": ["reader", "writef"]
       }

       # Track tool usage
       state.tool_usage_stats = {
           "calculator": 5,
           "search": 3,
           "reader": 2
       }

   Get active tools::

       active_tools = state.get_active_tools()
       for tool in active_tools:
           print(f"Active tool: {tool.name}")


   .. autolink-examples:: DynamicToolState
      :collapse:

   .. py:method:: categorize_tool(tool_name: str, category: str) -> None

      Categorize a tool by type.

      :param tool_name: Name of the tool
      :param category: Category to assign the tool to

      .. rubric:: Examples

      Categorize tools::

          state.categorize_tool("calculator", "math")
          state.categorize_tool("web_search", "web")
          state.categorize_tool("file_reader", "file")


      .. autolink-examples:: categorize_tool
         :collapse:


   .. py:method:: get_active_tools() -> list[langchain_core.tools.BaseTool]

      Get all active tools as LangChain tools.

      :returns: List of active BaseTool instances

      .. rubric:: Examples

      Get active tools for agent::

          tools = state.get_active_tools()
          agent_tools = [tool for tool in tools if isinstance(tool, BaseTool)]


      .. autolink-examples:: get_active_tools
         :collapse:


   .. py:method:: get_tool_usage_stats() -> dict[str, int]

      Get tool usage statistics.

      :returns: Dictionary of tool name to usage count

      .. rubric:: Examples

      Get usage statistics::

          stats = state.get_tool_usage_stats()
          most_used = max(stats.items(), key=lambda x: x[1])
          print(f"Most used tool: {most_used[0]} ({most_used[1]} times)")


      .. autolink-examples:: get_tool_usage_stats
         :collapse:


   .. py:method:: get_tools_by_category(category: str) -> list[str]

      Get tools in a specific category.

      :param category: Category to get tools for

      :returns: List of tool names in the category

      .. rubric:: Examples

      Get math tools::

          math_tools = state.get_tools_by_category("math")
          print(f"Math tools: {', '.join(math_tools)}")


      .. autolink-examples:: get_tools_by_category
         :collapse:


   .. py:method:: track_tool_usage(tool_name: str) -> None

      Track usage of a specific tool.

      :param tool_name: Name of the tool that was used

      .. rubric:: Examples

      Track tool usage::

          state.track_tool_usage("calculator")
          state.track_tool_usage("search")

          # Check usage stats
          print(f"Calculator used {state.tool_usage_stats['calculator']} times")


      .. autolink-examples:: track_tool_usage
         :collapse:


   .. py:attribute:: discovery_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: last_tool_discovery
      :type:  str | None
      :value: None



   .. py:attribute:: tool_categories
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: tool_usage_stats
      :type:  dict[str, int]
      :value: None



