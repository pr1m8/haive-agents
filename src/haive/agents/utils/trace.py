"""Agent trace pretty-printer using Rich.

Provides clean, readable output for any haive agent run, filtering out
the noisy LangGraph checkpoint dumps and showing only meaningful content:
messages, tool calls, tool results, and KG extractions.

Usage:
    from haive.agents.utils.trace import run_traced, TracePrinter

    # Run any agent with pretty trace
    result = run_traced(agent, "What is 15 * 23?")

    # Save trace to file
    result = run_traced(agent, "Hello", save_to="traces/")
"""

import json
import os
import time
from datetime import datetime
from typing import Any

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.tree import Tree
    from rich import box
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

if HAS_RICH:
    console = Console()
else:
    console = None


class TracePrinter:
    """Pretty-prints agent execution traces."""

    def __init__(self, show_tokens: bool = True, max_content_len: int = 500,
                 show_tool_args: bool = True):
        self.show_tokens = show_tokens
        self.max_content_len = max_content_len
        self.show_tool_args = show_tool_args

    def print_result(self, result: Any, title: str = "Agent Trace") -> None:
        """Print a formatted trace from an agent result."""
        messages = self._extract_messages(result)
        if not messages:
            self._print("[dim]No messages in result[/dim]")
            return

        if HAS_RICH:
            self._print_rich(messages, title)
        else:
            self._print_plain(messages, title)

    def _print_rich(self, messages: list, title: str) -> None:
        tree = Tree(f"[bold cyan]{title}[/bold cyan]")
        total_in = total_out = 0

        for msg in messages:
            msg_type = type(msg).__name__
            content = getattr(msg, "content", "")
            tool_calls = getattr(msg, "tool_calls", None)
            usage = (getattr(msg, "response_metadata", {}) or {}).get("token_usage", {})

            if usage:
                total_in += usage.get("prompt_tokens", 0) or usage.get("input_tokens", 0)
                total_out += usage.get("completion_tokens", 0) or usage.get("output_tokens", 0)

            if msg_type == "HumanMessage":
                tree.add(f"[bold green]User:[/bold green] {self._trunc(content)}")
            elif msg_type == "AIMessage":
                if tool_calls:
                    calls = ", ".join(
                        f"[yellow]{c['name']}[/yellow]({self._fmt_args(c.get('args', {}))})"
                        for c in tool_calls
                    )
                    tree.add(f"[bold blue]AI → Tools:[/bold blue] {calls}")
                elif content:
                    tree.add(f"[bold blue]AI:[/bold blue] {self._trunc(content)}")
            elif msg_type == "ToolMessage":
                name = getattr(msg, "name", "tool")
                style = "red" if "error" in content.lower() else "magenta"
                tree.add(f"[{style}]Tool ({name}):[/{style}] {self._trunc(content)}")

        console.print(tree)
        if self.show_tokens and (total_in or total_out):
            console.print(f"  [dim]Tokens: {total_in} in / {total_out} out[/dim]")

    def _print_plain(self, messages: list, title: str) -> None:
        print(f"=== {title} ===")
        for msg in messages:
            msg_type = type(msg).__name__
            content = getattr(msg, "content", "")
            tool_calls = getattr(msg, "tool_calls", None)
            if msg_type == "HumanMessage":
                print(f"  [User]: {self._trunc(content)}")
            elif msg_type == "AIMessage":
                if tool_calls:
                    calls = ", ".join(f"{c['name']}()" for c in tool_calls)
                    print(f"  [AI → Tools]: {calls}")
                elif content:
                    print(f"  [AI]: {self._trunc(content)}")
            elif msg_type == "ToolMessage":
                name = getattr(msg, "name", "tool")
                print(f"  [Tool ({name})]: {self._trunc(content)}")

    def print_store_summary(self, store: Any, user_id: str = "default") -> None:
        """Print store contents summary."""
        if HAS_RICH:
            table = Table(title="Store Contents", box=box.SIMPLE)
            table.add_column("Namespace", style="cyan")
            table.add_column("Count", justify="right", style="green")
            table.add_column("Sample", style="white")
        else:
            print("--- Store ---")

        for ns_name, ns_tuple in [("Memories", ("user", user_id)),
                                   ("KG Triples", ("kg", user_id)),
                                   ("Summaries", ("summary", user_id))]:
            try:
                items = store.search(ns_tuple, limit=50)
                count = len(items)
                sample = ""
                if items:
                    val = items[0].value if hasattr(items[0], "value") else items[0]
                    if isinstance(val, dict):
                        if val.get("type") == "kg_triple":
                            sample = f"{val['subject']} {val['predicate']} {val['object']}"
                        else:
                            sample = val.get("content", str(val))[:60]
                if HAS_RICH:
                    table.add_row(ns_name, str(count), sample)
                else:
                    print(f"  {ns_name}: {count} — {sample}")
            except Exception:
                if HAS_RICH:
                    table.add_row(ns_name, "?", "[dim]error[/dim]")
                else:
                    print(f"  {ns_name}: error")

        if HAS_RICH:
            console.print(table)

    def print_kg_triples(self, store: Any, user_id: str = "default") -> None:
        """Print KG triples from store."""
        try:
            items = store.search(("kg", user_id), limit=50)
            triples = [
                i.value if hasattr(i, "value") else i
                for i in items
                if (i.value if hasattr(i, "value") else i).get("type") == "kg_triple"
            ]
            if not triples:
                self._print("[dim]No KG triples[/dim]")
                return

            if HAS_RICH:
                table = Table(title="Knowledge Graph", box=box.ROUNDED)
                table.add_column("Subject", style="cyan")
                table.add_column("Predicate", style="yellow")
                table.add_column("Object", style="green")
                for t in triples:
                    table.add_row(t["subject"], t["predicate"], t["object"])
                console.print(table)
            else:
                print("--- KG Triples ---")
                for t in triples:
                    print(f"  {t['subject']} --{t['predicate']}--> {t['object']}")
        except Exception as e:
            self._print(f"[red]Error: {e}[/red]")

    def _extract_messages(self, result: Any) -> list:
        if hasattr(result, "messages") and result.messages:
            return result.messages
        if isinstance(result, dict) and "messages" in result:
            return result["messages"]
        return []

    def _trunc(self, text: str, max_len: int | None = None) -> str:
        max_len = max_len or self.max_content_len
        return text[:max_len] + "..." if len(text) > max_len else text

    def _fmt_args(self, args: dict) -> str:
        if not self.show_tool_args or not args:
            return ""
        parts = []
        for k, v in args.items():
            v_str = str(v)[:50]
            parts.append(f"{k}={v_str}")
        return ", ".join(parts)

    def _print(self, text: str) -> None:
        if HAS_RICH:
            console.print(text)
        else:
            print(text)


def run_traced(agent: Any, input_data: str | dict, title: str | None = None,
               save_to: str | None = None, **kwargs) -> Any:
    """Run any haive agent with pretty-printed trace output.

    Works with SimpleAgent, ReactAgent, MemoryAgent, MultiAgent, etc.

    Args:
        agent: Any haive agent
        input_data: Input string or dict
        title: Optional title
        save_to: Optional directory to save trace JSON
        **kwargs: Passed to agent.run()
    """
    agent_name = getattr(agent, "name", type(agent).__name__)
    trace_title = title or agent_name
    printer = TracePrinter()

    input_str = input_data if isinstance(input_data, str) else str(input_data)[:100]
    if HAS_RICH:
        console.print(Panel(
            f"[bold]{trace_title}[/bold]\n[dim]Input: {input_str}[/dim]",
            border_style="cyan", expand=False,
        ))
    else:
        print(f"\n=== {trace_title} ===\nInput: {input_str}")

    start = time.time()
    result = agent.run(input_data, **kwargs)
    elapsed = time.time() - start

    printer.print_result(result, title=trace_title)
    if HAS_RICH:
        console.print(f"  [dim]Time: {elapsed:.2f}s[/dim]")
    else:
        print(f"  Time: {elapsed:.2f}s")

    if hasattr(agent, "get_store") and agent.get_store():
        user_id = getattr(agent, "user_id", "default")
        printer.print_store_summary(agent.get_store(), user_id)

    if save_to:
        _save_trace(result, agent_name, input_data, elapsed, save_to)

    return result


def _save_trace(result: Any, agent_name: str, input_data: Any,
                elapsed: float, save_dir: str) -> None:
    """Save trace to JSON file."""
    os.makedirs(save_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(save_dir, f"{agent_name}_{ts}.json")

    messages = []
    raw = result.messages if hasattr(result, "messages") else []
    for msg in raw:
        entry = {"type": type(msg).__name__, "content": getattr(msg, "content", "")}
        tc = getattr(msg, "tool_calls", None)
        if tc:
            entry["tool_calls"] = [{"name": c["name"], "args": c.get("args", {})} for c in tc]
        usage = (getattr(msg, "response_metadata", {}) or {}).get("token_usage")
        if usage:
            entry["token_usage"] = usage
        messages.append(entry)

    trace = {
        "agent": agent_name, "input": str(input_data),
        "timestamp": datetime.now().isoformat(),
        "elapsed_seconds": round(elapsed, 3),
        "messages": messages,
    }
    with open(filepath, "w") as f:
        json.dump(trace, f, indent=2, default=str)

    if HAS_RICH:
        console.print(f"  [dim]Saved: {filepath}[/dim]")
    else:
        print(f"  Saved: {filepath}")
