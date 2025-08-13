#!/usr/bin/env python3
"""Debug why streaming values are empty."""

from src.haive.agents.conversation.collaberative.agent import CollaborativeConversation


def debug_streaming_values():
    """Debug what's actually in the streaming chunks."""
    # Create simple agent
    agent = CollaborativeConversation.create_brainstorming_session(
        topic="Test", participants=["Alice"], max_rounds=2
    )

    try:
        config = {"configurable": {"recursion_limit": 10}}

        for i, chunk in enumerate(agent.stream({}, config=config)):
            if hasattr(chunk, "__dict__"):
                pass

            if isinstance(chunk, dict):
                for key, value in chunk.items():
                    if isinstance(value, dict):
                        # Show first few key-value pairs
                        for _k, v in list(value.items())[:3]:
                            if isinstance(v, str) and len(v) > 100:
                                pass
                            else:
                                pass
                        if len(value) > 3:
                            pass
                    elif isinstance(value, list):
                        if value:
                            pass
                    else:
                        pass

            if i >= 5:  # Limit to avoid too much output
                break

    except Exception:
        import traceback

        traceback.print_exc()

    try:
        if hasattr(agent, "app"):
            # Test streaming directly on app
            for i, chunk in enumerate(agent.app.stream({}, config=config)):
                if isinstance(chunk, dict) and chunk:
                    # Show state values
                    for key, value in chunk.items():
                        if key in [
                            "current_speaker",
                            "turn_count",
                            "conversation_ended",
                        ] or (key == "messages" and isinstance(value, list)):
                            pass

                if i >= 5:
                    break
        else:
            pass

    except Exception:
        pass

    try:
        modes = ["values", "updates", "messages"]
        for mode in modes:
            config = {"configurable": {"recursion_limit": 10}, "stream_mode": mode}

            chunk_count = 0
            for chunk in agent.stream({}, config=config):
                chunk_count += 1
                if isinstance(chunk, dict) and chunk:
                    if mode == "values":
                        # For values mode, show actual state
                        for key in ["current_speaker", "turn_count", "messages"]:
                            if key in chunk:
                                if key == "messages":
                                    pass
                                else:
                                    pass
                elif chunk:
                    pass
                else:
                    pass

                if chunk_count >= 5:
                    break
    except Exception:
        pass

    try:
        # Check if agent is properly compiled

        # Try to get state schema
        if hasattr(agent, "state_schema") and hasattr(
            agent.state_schema, "model_fields"
        ):
            pass

        # Check if graph is built
        if hasattr(agent, "graph") and hasattr(agent.graph, "nodes"):
            pass

    except Exception:
        pass


if __name__ == "__main__":
    debug_streaming_values()
