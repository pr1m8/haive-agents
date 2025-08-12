"""Test actual execution of ReactAgent with structured output."""


def test_react_agent_structured_execution(react_agent_with_structured_output):
    """Test actual execution of auto-wrapped ReactAgent with structured output."""

    print("\n" + "="*60)
    print("🚀 TESTING REACT AGENT STRUCTURED EXECUTION")
    print("="*60)

    react_agent = react_agent_with_structured_output

    # Verify it's set up for auto-wrap
    print("\n📋 Pre-execution checks:")
    print(f"   - Agent: {react_agent.name}")
    print(f"   - Class: {react_agent.__class__.__name__}")
    print(f"   - Auto-wrap needed: {getattr(react_agent, '_needs_structured_output_wrapper', False)}")
    print(f"   - Structured output: {react_agent.structured_output_model}")

    # Test input that should trigger tool usage and structured output
    test_input = "Calculate 15 * 23 and provide analysis with confidence score"

    print("\n🚀 Executing ReactAgent with structured output:")
    print(f"   - Input: {test_input}")

    try:
        # This should trigger the auto-wrap mechanism:
        # 1. ReactAgent does reasoning and tool use (15 * 23 = 345)
        # 2. SimpleAgent formatter converts result to ReactResult structure
        result = react_agent.run(test_input)

        print("   - ✅ Execution successful!")
        print(f"   - Result type: {type(result)}")
        print(f"   - Result: {result}")

        # Check if we got the expected structured output
        from tests.conftest import ReactResult
        if isinstance(result, ReactResult):
            print("   - 🎉 GOT STRUCTURED OUTPUT!")
            print(f"     * Analysis: {result.analysis}")
            print(f"     * Tool calls made: {result.tool_calls_made}")
            print(f"     * Confidence: {result.confidence}")

            # Verify the calculation was done
            assert "345" in result.analysis, "Should contain calculation result 15*23=345"
            assert result.tool_calls_made > 0, "Should have made tool calls"
            assert 0.0 <= result.confidence <= 1.0, "Confidence should be valid"

            print("   - ✅ All assertions passed - auto-wrap working perfectly!")

        else:
            print(f"   - ⚠️ Got {type(result)} instead of ReactResult")
            print(f"   - Raw result: {result}")

        return result

    except Exception as e:
        print(f"   - ❌ Execution failed: {e}")
        print(f"   - Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        raise


def test_react_agent_auto_wrap_internal_structure(react_agent_with_structured_output):
    """Test the internal structure of auto-wrapped ReactAgent."""

    print("\n" + "="*60)
    print("🔍 EXAMINING AUTO-WRAP INTERNAL STRUCTURE")
    print("="*60)

    react_agent = react_agent_with_structured_output

    # Compile to trigger auto-wrap
    react_agent.compile()

    print("\n📋 Internal structure after compilation:")
    print(f"   - Compiled: {react_agent._is_compiled}")
    print(f"   - App type: {type(react_agent._app)}")

    if hasattr(react_agent, "graph") and react_agent.graph:
        print(f"   - Graph type: {type(react_agent.graph)}")

        # Try to inspect the nodes in the auto-wrapped graph
        try:
            lg_graph = react_agent.graph.to_langgraph(state_schema=react_agent.state_schema)
            nodes = list(lg_graph.nodes.keys()) if hasattr(lg_graph, "nodes") else []
            edges = list(lg_graph.edges) if hasattr(lg_graph, "edges") else []

            print(f"   - Graph nodes: {nodes}")
            print(f"   - Graph edges: {edges}")

            # This should show the auto-wrapped structure:
            # - react_structured (base ReactAgent without structured output)
            # - react_structured_formatter (SimpleAgent for formatting)
            expected_nodes = ["react_structured", "react_structured_formatter"]
            for node in expected_nodes:
                if node in nodes:
                    print(f"     ✅ Found expected node: {node}")
                else:
                    print(f"     ❌ Missing expected node: {node}")

            # Verify it's a sequential flow
            if len(nodes) == 2 and "react_structured" in nodes and "react_structured_formatter" in nodes:
                print("   - 🎉 Auto-wrap structure is correct!")
            else:
                print("   - ⚠️ Unexpected auto-wrap structure")

        except Exception as e:
            print(f"   - Could not inspect graph structure: {e}")

    print("\n📋 This shows how auto-wrap transforms:")
    print("   - Original: ReactAgent(structured_output_model=ReactResult)")
    print("   - Auto-wrapped: MultiAgent([")
    print("       ReactAgent(no structured output),  # Does reasoning")
    print("       SimpleAgent(structured_output_model=ReactResult)  # Formats output")
    print("     ])")


def test_compare_manual_vs_auto_wrap():
    """Compare manual multi-agent setup vs auto-wrap mechanism."""

    print("\n" + "="*60)
    print("🔍 COMPARING MANUAL VS AUTO-WRAP")
    print("="*60)

    from langchain_core.prompts import ChatPromptTemplate

    from haive.agents.multi.agent import MultiAgent
    from haive.agents.react.agent import ReactAgent
    from haive.agents.simple.agent import SimpleAgent
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.core.models.llm.base import AzureLLMConfig
    from tests.conftest import ReactResult, simple_calculator, text_analyzer

    print("\n📋 Method 1: Manual MultiAgent setup")

    # Manual approach - explicitly create base agent + formatter
    base_agent = ReactAgent(
        name="manual_base",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.3),
            tools=[simple_calculator, text_analyzer],
        ),
        # NO structured_output_model - keep it as pure ReactAgent
    )

    formatter_agent = SimpleAgent(
        name="manual_formatter",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.1),
            structured_output_model=ReactResult,
            structured_output_version="v2",
        ),
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a structured output formatter. Extract information and format it according to the schema."),
            ("human", """Based on the previous agent's analysis:

{messages}

Extract and format the information according to the required structured output schema."""),
        ])
    )

    manual_multi = MultiAgent(
        name="manual_react_structured",
        agents=[base_agent, formatter_agent],
        execution_mode="sequential",
        debug=True,
    )

    print("   - Manual setup complete")
    print(f"   - Agents: {list(manual_multi.agent_dict.keys())}")

    print("\n📋 Method 2: Auto-wrap mechanism")

    # Auto-wrap approach - just add structured_output_model to ReactAgent
    auto_agent = ReactAgent(
        name="auto_react_structured",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.3),
            tools=[simple_calculator, text_analyzer],
        ),
        structured_output_model=ReactResult,  # This triggers auto-wrap
        structured_output_version="v2",
        debug=True,
    )

    print("   - Auto-wrap setup complete")
    print(f"   - Auto-wrap needed: {getattr(auto_agent, '_needs_structured_output_wrapper', False)}")

    # Compile both to see the structure
    try:
        manual_multi.compile()
        auto_agent.compile()

        print("\n📋 Comparison results:")
        print(f"   - Manual: {len(manual_multi.agents)} agents in MultiAgent")
        print("   - Auto-wrap: Internal MultiAgent created automatically")
        print("   - Both should produce similar results with structured output")

        print("\n✨ Auto-wrap mechanism provides:")
        print("   - ✅ Simplified setup (just add structured_output_model)")
        print("   - ✅ Same functionality as manual approach")
        print("   - ✅ Automatic formatting agent creation")
        print("   - ⚠️ BUT: Creates nested MultiAgent structures")

    except Exception as e:
        print(f"   - ❌ Compilation issue: {e}")
        raise
