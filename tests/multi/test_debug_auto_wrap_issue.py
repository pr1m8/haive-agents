"""Debug test to understand the auto-wrap issue step by step.

This test will trace through exactly what happens when we create agents
and put them in MultiAgent to understand the infinite loop issue.
"""


def test_trace_auto_wrap_behavior(
    simple_agent_with_structured_output,
    simple_agent_without_structured_output,
    react_agent_with_tools
):
    """Trace what actually happens with auto-wrapping."""

    print("\n" + "="*60)
    print("🔍 TRACING AUTO-WRAP BEHAVIOR")
    print("="*60)

    # Check each agent type
    agents = [
        ("SimpleAgent WITH structured", simple_agent_with_structured_output),
        ("SimpleAgent WITHOUT structured", simple_agent_without_structured_output),
        ("ReactAgent with tools", react_agent_with_tools),
    ]

    for description, agent in agents:
        print(f"\n📋 {description}:")
        print(f"   - Name: {agent.name}")
        print(f"   - Class: {agent.__class__.__name__}")

        # Check if it has structured output
        has_structured = bool(getattr(agent, "structured_output_model", None))
        print(f"   - Has structured_output_model: {has_structured}")

        if has_structured:
            print(f"   - Structured model: {agent.structured_output_model}")

        # Check auto-wrap flag
        needs_wrap = bool(getattr(agent, "_needs_structured_output_wrapper", False))
        print(f"   - _needs_structured_output_wrapper: {needs_wrap}")

        # If it needs wrapping, what happens when we compile it?
        if needs_wrap:
            print("   - 🚨 THIS AGENT WILL BE AUTO-WRAPPED!")
            print("   - When compiled, it will become a nested MultiAgent internally")

            # Try to compile and see what happens
            try:
                print("   - Compiling agent to see what happens...")
                agent.compile()

                print("   - ✅ Agent compiled successfully")
                print(f"   - _app type: {type(agent._app)}")
                print(f"   - _is_compiled: {agent._is_compiled}")

                # Check if there's a wrapped graph
                if hasattr(agent, "_wrapped_graph"):
                    print(f"   - Has _wrapped_graph: {agent._wrapped_graph is not None}")

            except Exception as e:
                print(f"   - ❌ Compilation failed: {e}")


def test_what_happens_in_multi_agent(
    simple_agent_with_structured_output,
    simple_agent_without_structured_output,
    react_agent_with_tools
):
    """Test what happens when we put these agents in MultiAgent."""

    from haive.agents.multi.agent import MultiAgent

    print("\n" + "="*60)
    print("🔍 TESTING MULTI-AGENT BEHAVIOR")
    print("="*60)

    # Test 1: MultiAgent with non-auto-wrap agents
    print("\n📋 Test 1: MultiAgent with non-auto-wrap agents")
    try:
        multi1 = MultiAgent(
            name="test_no_autowrap",
            agents=[simple_agent_without_structured_output, react_agent_with_tools],
            execution_mode="sequential",
            debug=True,
        )

        print("   - ✅ MultiAgent created successfully")
        print(f"   - Agent count: {len(multi1.agents)}")
        print(f"   - Agent names: {list(multi1.agent_dict.keys())}")

        # Try to compile
        multi1.compile()
        print("   - ✅ MultiAgent compiled successfully")

    except Exception as e:
        print(f"   - ❌ Failed: {e}")

    # Test 2: MultiAgent with auto-wrap agent (THE PROBLEM)
    print("\n📋 Test 2: MultiAgent with auto-wrap agent (THE PROBLEM)")
    try:
        multi2 = MultiAgent(
            name="test_with_autowrap",
            agents=[react_agent_with_tools, simple_agent_with_structured_output],
            execution_mode="sequential",
            debug=True,
        )

        print("   - ✅ MultiAgent created successfully")
        print(f"   - Agent count: {len(multi2.agents)}")
        print(f"   - Agent names: {list(multi2.agent_dict.keys())}")

        # Check what's actually in the agent_dict
        for name, agent in multi2.agent_dict.items():
            print(f"   - Agent '{name}': {agent.__class__.__name__}")
            needs_wrap = bool(getattr(agent, "_needs_structured_output_wrapper", False))
            print(f"     * Auto-wrap needed: {needs_wrap}")

            if needs_wrap:
                print("     * 🚨 THIS CREATES THE NESTED MULTIAGENT ISSUE!")

        # Try to compile - this might cause issues
        print("   - Attempting to compile MultiAgent with auto-wrap agent...")
        multi2.compile()
        print("   - ✅ MultiAgent compiled successfully")

        # Try to run a simple test
        print("   - Attempting to run simple test...")
        result = multi2.run("Test input")
        print(f"   - ✅ Execution completed: {type(result)}")

    except Exception as e:
        print(f"   - ❌ Failed: {e}")
        print(f"   - Error type: {type(e)}")
        import traceback
        print("   - Stack trace:")
        traceback.print_exc()


def test_examine_auto_wrap_internals(simple_agent_with_structured_output):
    """Examine what happens internally during auto-wrap."""

    print("\n" + "="*60)
    print("🔍 EXAMINING AUTO-WRAP INTERNALS")
    print("="*60)

    agent = simple_agent_with_structured_output

    print(f"\n📋 Agent: {agent.name}")
    print(f"   - Class: {agent.__class__.__name__}")
    print(f"   - Needs wrap: {getattr(agent, '_needs_structured_output_wrapper', False)}")

    # Check if it has the auto-wrap detection method
    if hasattr(agent, "_check_and_wrap_structured_output"):
        print("   - Has _check_and_wrap_structured_output method: Yes")

    # Check if it has the wrap building method
    if hasattr(agent, "_build_wrapped_graph"):
        print("   - Has _build_wrapped_graph method: Yes")

        # Try to see what this method would create
        try:
            print("   - Calling _build_wrapped_graph to see what it creates...")
            wrapped_graph = agent._build_wrapped_graph()
            print(f"   - Wrapped graph type: {type(wrapped_graph)}")
            print("   - 🚨 THIS IS WHERE THE NESTED MULTIAGENT GETS CREATED!")

        except Exception as e:
            print(f"   - Error building wrapped graph: {e}")

    # Compile the agent to trigger auto-wrap
    print("\n   - Compiling agent to trigger auto-wrap...")
    try:
        agent.compile()
        print("   - ✅ Compilation successful")
        print(f"   - App type: {type(agent._app)}")

        # Check what the compiled app actually is
        if hasattr(agent._app, "nodes"):
            print(f"   - Graph nodes: {list(agent._app.nodes.keys())}")

    except Exception as e:
        print(f"   - ❌ Compilation failed: {e}")
