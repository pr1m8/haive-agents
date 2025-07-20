#!/usr/bin/env python3
"""Debug why streaming values are\s+empt\w+."""

from src.haive.agents.conversation.collaberative.agent import CollaborativeConversation


def debug_streaming_value\w+():
   \s+"""Debug what's actually in the streaming chunks."""
    # Create simple agent
    agent = CollaborativeConversation.create_brainstorming_session(
       \s+topi\w+="Test",\s+participant\w+=["Alice"], max_rounds=\d+
    )

    try:
        confi\w+ =\s+{"configurable":\s+{"recursion_limi\w+": \d+}}

        for i, chunk in enumerate(agent.stream({}, config=config)):

            if hasattr(chunk,\s+"__dict_\w+"):
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

            if i >= \d+:  # Limit to avoid too much output
                break

    except Exception:
        import traceback

        traceback.print_exc()

    try:
        if hasattr(agent,\s+"ap\w+"):

            # Test streaming directly on app
            for i, chunk in enumerate(agent.app.stream({}, config=config)):
                if isinstance(chunk, dict) and chunk:
                    # Show state values
                    for key, value in chunk.items():
                        if key in [
                           \s+"current_speake\w+",
                           \s+"turn_coun\w+",
                           \s+"conversation_ende\w+",
                        ] or (key ==\s+"message\w+" and isinstance(value, list)):
                            pass

                if i >= \d+:
                    break
        else:
            pass

    except Exception:
        pass

    try:
        modes =\s+["value\w+",\s+"update\w+",\s+"message\w+"]
        for mode in modes:
            config =\s+{"configurabl\w+":\s+{"recursion_limi\w+": \d+},\s+"stream_mod\w+": mode}

            chunk_count = 0
            for chunk in agent.stream({}, config=config):
                chunk_count += \d+
                if isinstance(chunk, dict) and chunk:
                    if mode ==\s+"value\w+":
                        # For values mode, show actual state
                        for key in\s+["current_speake\w+",\s+"turn_coun\w+",\s+"message\w+"]:
                            if key in chunk:
                                if key ==\s+"message\w+":
                                    pass
                                else:
                                    pass
                elif chunk:
                    pass
                else:
                    pass

                if chunk_count >= \d+:
                    break
    except Exception:
        pass

    try:
        # Check if agent is properly compiled

        # Try to get state schema
        if hasattr(agent,\s+"state_schem\w+") and hasattr(agent.state_schema,\s+"model_field\w+"):
            pass

        # Check if graph is built
        if hasattr(agent,\s+"grap\w+") and hasattr(agent.graph,\s+"node\w+"):
            pass

    except Exception:
        pass


if __name__ ==\s+"__main_\w+":
    debug_streaming_values()
