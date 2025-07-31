"""Minimal HyDE test runner."""

import os
import sys


# Set logging before imports
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["HAIVE_LOG_LEVEL"] = "ERROR"

import logging


logging.getLogger().setLevel(logging.ERROR)
for logger_name in ["haive", "langchain", "urllib3", "requests", "tensorflow"]:
    logging.getLogger(logger_name).setLevel(logging.ERROR)

# Now run the actual test
sys.path.insert(0, os.path.dirname(__file__))

from test_hyde_rag_demo import demonstrate_hyde_rag


if __name__ == "__main__":

    try:
        demonstrate_hyde_rag()
    except Exception:
        import traceback

        traceback.print_exc()
