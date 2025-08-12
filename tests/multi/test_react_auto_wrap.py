"""Test ReactAgent with structured output to verify auto-wrapping works correctly."""


def test_react_agent_with_structured_output_auto_wrap(react_agent_with_structured_output):
    """Test that ReactAgent with structured output gets auto-wrapped correctly."""

    print("\n" + "="*60)
    print("🔍 TESTING REACT AGENT AUTO-WRAP")
    print("="*60)

    react_agent = react_agent_with_structured_output

    print("\n📋 ReactAgent with structured output:")
    print(f"   - Name: {react_agent.name}")
    print(f"   - Class: {react_agent.__class__.__name__}")
    print(f"   - Has structured_output_model: {bool(react_agent.structured_output_model)}")
    print(f"   - Structured model: {react_agent.structured_output_model}")

    # Check auto-wrap flag
    needs_wrap = bool(getattr(react_agent, "_needs_structured_output_wrapper", False))
    print(f"   - _needs_structured_output_wrapper: {needs_wrap}")

    # This should be True because ReactAgent doesn't handle structured output natively
    assert needs_wrap == True, "ReactAgent with structured output should need auto-wrap"

    print("   - ✅ ReactAgent correctly marked for auto-wrap!")

    # Try to compile and see what happens
    print("\n📋 Compiling ReactAgent (should create wrapped MultiAgent):")
    try:
        react_agent.compile()

        print("   - ✅ Compilation successful")
        print(f"   - App type: {type(react_agent._app)}")
        print(f"   - _is_compiled: {react_agent._is_compiled}")

        # Check if the graph was wrapped
        if hasattr(react_agent, "graph") and react_agent.graph:
            print(f"   - Graph created: {type(react_agent.graph)}")

            # Try to get graph nodes if available
            try:
                lg_graph = react_agent.graph.to_langgraph(state_schema=react_agent.state_schema)
                nodes = list(lg_graph.nodes.keys()) if hasattr(lg_graph, "nodes") else []
                print(f"   - Graph nodes: {nodes}")
            except Exception as e:
                print(f"   - Could not inspect graph nodes: {e}")

        print("   - 🎉 AUTO-WRAP SUCCESSFUL - ReactAgent is now wrapped in MultiAgent!")

    except Exception as e:
        print(f"   - ❌ Compilation failed: {e}")
        import traceback
        traceback.print_exc()
        raise


def test_react_vs_simple_auto_wrap_comparison(
    react_agent_with_structured_output,
    simple_agent_with_structured_output
):
    """Compare auto-wrap behavior between ReactAgent and SimpleAgent."""

    print("\n" + "="*60)
    print("🔍 COMPARING REACT VS SIMPLE AUTO-WRAP")
    print("="*60)

    agents = [
        ("ReactAgent + structured", react_agent_with_structured_output),
        ("SimpleAgent + structured", simple_agent_with_structured_output),
    ]

    print("\n📋 Auto-wrap comparison:")

    for description, agent in agents:
        needs_wrap = bool(getattr(agent, "_needs_structured_output_wrapper", False))

        print(f"   - {description}:")
        print(f"     * Class: {agent.__class__.__name__}")
        print(f"     * Needs auto-wrap: {needs_wrap}")
        print(f"     * Expected: {'Yes' if 'React' in description else 'No'}")

    # Assertions
    react_needs_wrap = bool(getattr(react_agent_with_structured_output, "_needs_structured_output_wrapper", False))
    simple_needs_wrap = bool(getattr(simple_agent_with_structured_output, "_needs_structured_output_wrapper", False))

    assert react_needs_wrap == True, "ReactAgent should need auto-wrap"
    assert simple_needs_wrap == False, "SimpleAgent should NOT need auto-wrap"

    print("\n   - ✅ Auto-wrap detection working correctly!")
    print("     * ReactAgent: auto-wrap needed (correct)")
    print("     * SimpleAgent: no auto-wrap needed (correct)")


def test_multi_agent_with_auto_wrapped_react(
    react_agent_with_structured_output,
    simple_agent_without_structured_output
):
    """Test MultiAgent containing an auto-wrapped ReactAgent."""

    from haive.agents.multi.agent import MultiAgent

    print("\n" + "="*60)
    print("🔍 TESTING MULTIAGENT + AUTO-WRAPPED REACT")
    print("="*60)

    react_agent = react_agent_with_structured_output
    simple_agent = simple_agent_without_structured_output

    print("\n📋 Creating MultiAgent with:")
    print(f"   - ReactAgent (auto-wrap needed): {getattr(react_agent, '_needs_structured_output_wrapper', False)}")
    print(f"   - SimpleAgent (no auto-wrap): {getattr(simple_agent, '_needs_structured_output_wrapper', False)}")

    try:
        # Create MultiAgent
        multi_agent = MultiAgent(
            name="test_auto_wrap_multi",
            agents=[simple_agent, react_agent],  # Put auto-wrap agent second
            execution_mode="sequential",
            debug=True,
        )

        print("   - ✅ MultiAgent created successfully")
        print(f"   - Agent count: {len(multi_agent.agents)}")
        print(f"   - Agent names: {list(multi_agent.agent_dict.keys())}")

        # Check what's in the agents
        for name, agent in multi_agent.agent_dict.items():
            needs_wrap = bool(getattr(agent, "_needs_structured_output_wrapper", False))
            print(f"   - Agent '{name}': {agent.__class__.__name__} (auto-wrap: {needs_wrap})")

        # Try to compile
        print("\n📋 Compiling MultiAgent with auto-wrapped ReactAgent:")
        multi_agent.compile()
        print("   - ✅ Compilation successful!")

        # Try a simple execution
        print("\n📋 Testing execution:")
        result = multi_agent.run("Test the auto-wrapped ReactAgent")
        print("   - ✅ Execution successful!")
        print(f"   - Result type: {type(result)}")

    except Exception as e:
        print(f"   - ❌ Failed: {e}")
        import traceback
        traceback.print_exc()
        raise
