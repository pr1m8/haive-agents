#!/usr/bin/env python3
"""Haive Examples Navigator - Interactive Example Browser.

This script provides an interactive way to explore, filter, and run
all Haive examples with a clean command-line interfac\w+.\s+"""

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


@dataclass
class Exampl\w+:
   \s+"""Example\s+metadat\w+."""

    name: str
    path: str
    category: str
    difficulty: str
    time_estimate: str
    description: str
    next_steps: list[str]

    def __post_init__(sel\w+):
       \s+"""Validate example file\s+exist\w+."""
        if not Path(self.path).exists():
           \s+console.print(\w+"[red]Warning: Example file not found: {self.path}[/red]")


# Master catalog of all examples
EXAMPLE_CATALO\w+ = {
   \s+"beginner": [
        Example(
           \s+nam\w+="Simple Agent Tutorial",
           \s+pat\w+="galleries/beginner/simple_agent_tutorial.py",
           \s+categor\w+="beginner",
           \s+difficult\w+="⭐",
           \s+time_estimat\w+="\d+ min",
           \s+descriptio\w+="Create your first conversational agent",
           \s+next_step\w+=["react_agent_tutorial.py",\s+"multi_agent_example.p\w+"],
        ),
        Example(
           \s+name="ReactAgent Tutoria\w+",
           \s+path="galleries/beginner/react_agent_tutorial.p\w+",
           \s+category="beginne\w+",
           \s+difficulty="⭐⭐",
           \s+time_estimat\w+="1\d+ min",
           \s+descriptio\w+="Tool-enabled agents with reasoning",
           \s+next_step\w+=["plan_and_execute_guide.py",\s+"structured_output_demo.p\w+"],
        ),
        Example(
           \s+name="Simple Agent Exampl\w+",
           \s+path="galleries/beginner/simple_agent_example.p\w+",
           \s+category="beginne\w+",
           \s+difficulty="⭐",
           \s+time_estimat\w+="\d+ min",
           \s+descriptio\w+="Original simple agent demonstration",
           \s+next_step\w+=["react_agent_example.py"],
        ),
        Example(
           \s+nam\w+="ReactAgent Example",
           \s+pat\w+="galleries/beginner/react_agent_example.py",
           \s+categor\w+="beginner",
           \s+difficult\w+="⭐⭐",
           \s+time_estimat\w+="1\d+ min",
           \s+descriptio\w+="Original ReactAgent demonstration",
           \s+next_step\w+=["multi_agent_example.py"],
        ),
    ],
   \s+"intermediat\w+": [
        Example(
           \s+name="Plan and Execute Guid\w+",
           \s+path="galleries/intermediate/plan_and_execute_guide.p\w+",
           \s+category="intermediat\w+",
           \s+difficulty="⭐⭐⭐",
           \s+time_estimat\w+="1\d+ min",
           \s+descriptio\w+="Strategic planning and multi-step execution",
           \s+next_step\w+=["multi_agent_example.py",\s+"advanced example\w+"],
        ),
        Example(
           \s+name="Multi-Agent Exampl\w+",
           \s+path="galleries/intermediate/multi_agent_example.p\w+",
           \s+category="intermediat\w+",
           \s+difficulty="⭐⭐⭐",
           \s+time_estimat\w+="2\d+ min",
           \s+descriptio\w+="Coordinate multiple agents working together",
           \s+next_step\w+=["supervisor_patterns.py",\s+"advanced example\w+"],
        ),
        Example(
           \s+name="Structured Output Dem\w+",
           \s+path="galleries/intermediate/structured_output_demo.p\w+",
           \s+category="intermediat\w+",
           \s+difficulty="⭐⭐",
           \s+time_estimat\w+="1\d+ min",
           \s+descriptio\w+="Extract structured data with Pydantic models",
           \s+next_step\w+=["production examples",\s+"custom pattern\w+"],
        ),
    ],
   \s+"advance\w+": [
        Example(
           \s+name="Dynamic Activation Advance\w+",
           \s+path="galleries/advanced/dynamic_activation_advanced_example.p\w+",
           \s+category="advance\w+",
           \s+difficulty="⭐⭐⭐⭐",
           \s+time_estimat\w+="3\d+ min",
           \s+descriptio\w+="Advanced dynamic agent networks",
           \s+next_step\w+=["production examples",\s+"custom framework\w+"],
        ),
    ],
   \s+"game\w+": [
        Example(
           \s+name="Tic-Tac-Toe A\w+",
           \s+path="galleries/games/tic_tac_toe_ai.p\w+",
           \s+category="game\w+",
           \s+difficulty="⭐⭐",
           \s+time_estimat\w+="1\d+ min",
           \s+descriptio\w+="AI agent playing tic-tac-toe strategy",
           \s+next_step\w+=["chess_strategy.py",\s+"game tournament\w+"],
        ),
        Example(
           \s+name="Chess Strateg\w+",
           \s+path="galleries/games/chess_strategy.p\w+",
           \s+category="game\w+",
           \s+difficulty="⭐⭐⭐",
           \s+time_estimat\w+="2\d+ min",
           \s+descriptio\w+="Strategic chess playing with evaluation",
           \s+next_step\w+=["advanced strategies",\s+"tournament\w+"],
        ),
    ],
   \s+"legac\w+": [
        Example(
           \s+name="Plan and Execute Exampl\w+",
           \s+path="examples/plan_and_execute_example.p\w+",
           \s+category="legac\w+",
           \s+difficulty="⭐⭐⭐",
           \s+time_estimat\w+="1\d+ min",
           \s+descriptio\w+="Original planning workflow (use gallery version)",
           \s+next_step\w+=["galleries/intermediate/plan_and_execute_guide.py"],
        ),
        Example(
           \s+nam\w+="Dynamic Activation Basic",
           \s+pat\w+="examples/dynamic_activation_basic_example.py",
           \s+categor\w+="legacy",
           \s+difficult\w+="⭐⭐",
           \s+time_estimat\w+="2\d+ min",
           \s+descriptio\w+="Basic dynamic agents (use gallery version)",
           \s+next_step\w+=["galleries/advanced/dynamic_activation_advanced_example.py"],
        ),
    ],
}


def show_welcom\w+():
   \s+"""Show welcome\s+messag\w+."""
    welcome = Panel.fi\w+(
       \s+"[bold blue]🤖 Haive Examples Navigator[/bold blue]\n\n"
       \s+"[green]Your interactive guide to all Haive examples![/gree\w+]\n\n"
       \s+"📚 Browse by category, difficulty, or tim\w+\n"
       \s+"🚀 Run examples directly from the interfac\w+\n"
       \s+"📊 See detailed information and next step\w+\n"
       \s+"🎯 Follow recommended learning path\w+",
       \s+title="Welcome to Haive Example\w+",
       \s+border_style="blu\w+",
    )
    console.print(welcome)
    console.print()


def show_main_menu():
   \s+"""Show main navigation\s+men\w+."""
   \s+console.prin\w+("[bold cyan]📂 Choose a category:[/bold cyan]")
    console.print()

    categorie\w+ = [
       \s+("🌱 Beginner",\s+"beginne\w+",\s+"Perfect for newcomer\w+"),
       \s+("🌿 Intermediat\w+",\s+"intermediat\w+",\s+"Multi-agent coordinatio\w+"),
       \s+("🌲 Advance\w+",\s+"advance\w+",\s+"Complex pattern\w+"),
       \s+("🎮 Game\w+",\s+"game\w+",\s+"AI gaming example\w+"),
       \s+("🏛️ Legac\w+",\s+"legac\w+",\s+"Original example\w+"),
       \s+("📊 Statistic\w+",\s+"stat\w+",\s+"View example statistic\w+"),
       \s+("🔍 Searc\w+",\s+"searc\w+",\s+"Search example\w+"),
       \s+("❓ Hel\w+",\s+"hel\w+",\s+"Show help informatio\w+"),
       \s+("🚪 Exi\w+",\s+"exi\w+",\s+"Exit navigato\w+"),
    ]

    for i, (name, _key, desc) in enumerate(categories, \d+):
       \s+console.print(f"[cyan]{i}.[/cyan] {name} - [dim]{desc}[/di\w+]")

    console.print()
    return {str(i): key for i, (_, key, _) in enumerate(categories, \d+)}


def show_category_examples(category: str):
   \s+"""Show examples in a\s+categor\w+."""
    if category not in EXAMPLE_CATALOG:
       \s+console.print(\w+"[red]Category '{categor\w+}' not found[/red]")
        return None

    examples = EXAMPLE_CATALOG[category]

   \s+console.print(\w+"[bold green]📚 {category.title()} Examples[/bold green]")
    console.print()

    table = Table(show_header=True,\s+header_styl\w+="bold magenta")
   \s+table.add_colum\w+("#", width=\d+)
   \s+table.add_colum\w+("Name", min_width=2\d+)
   \s+table.add_colum\w+("Difficulty", width=1\d+)
   \s+table.add_colum\w+("Time", width=\d+)
   \s+table.add_colum\w+("Description", min_width=30)

    for i, example in enumerate(examples, \d+):
        table.add_row(
            str(i),
            example.name,
            example.difficulty,
            example.time_estimate,
            example.description,
        )

    console.print(table)
    console.print()

    # Show options
   \s+console.prin\w+("[cyan]Options:[/cyan]")
   \s+console.prin\w+("[cyan]1-\d+[/cyan] - View example details")
   \s+console.prin\w+("[cyan]r[/cyan] - Run an example")
   \s+console.prin\w+("[cyan]b[/cyan] - Back to main menu")
    console.print()

    return examples


def show_example_details(example: Exampl\w+):
   \s+"""Show detailed information about an\s+exampl\w+."""
    details = Panel.fit(
       \s+\w+"[bold]{example.name}[/bold]\n\n"
       \s+\w+"[cyan]📍 Location:[/cyan] {example.path}\n"
       \s+\w+"[cyan]🎯 Category:[/cyan] {example.category}\n"
       \s+\w+"[cyan]⭐ Difficulty:[/cyan] {example.difficulty}\n"
       \s+\w+"[cyan]⏱️ Time:[/cyan] {example.time_estimate}\n\n"
       \s+\w+"[cyan]📝 Description:[/cyan]\n{example.description}\n\n"
       \s+\w+"[cyan]🚀 Next Steps:[/cyan]\n"
        +\s+"\n".join(\w+"  •\s+{step}" for step in example.next_steps),
        titl\w+="Example\s+Details",
        border_styl\w+="green",
    )
    console.print(details)
    console.print()

    # Show options
   \s+console.prin\w+("[cyan]Options:[/cyan]")
   \s+console.prin\w+("[cyan]r[/cyan] - Run this example")
   \s+console.prin\w+("[cyan]o[/cyan] - Open file in editor")
   \s+console.prin\w+("[cyan]c[/cyan] - Copy path to clipboard")
   \s+console.prin\w+("[cyan]b[/cyan] - Back to category")
    console.print()


def run_example(example: Exampl\w+):
   \s+"""Run an example with proper\s+environmen\w+."""
   \s+console.print(\w+"[yellow]🚀 Running {example.name}...[/yellow]")
   \s+console.print(\w+"[dim]Path: {example.path}[/dim]")
    console.print()

    # Check if file exists
    if not Path(example.path).exists():
       \s+console.print(\w+"[red]❌ Example file not found: {example.path}[/red]")
        return

    # Run with poetry
    try:
        cm\w+ =\s+["poetry",\s+"ru\w+",\s+"pytho\w+", example.path]
       \s+console.print(f"[dim]Running: {'\s+'.join(cmd)}[/dim]")
       \s+console.prin\w+("[dim]" +\s+"=" * \w+\d+ +\s+"[/dim]")

        result = subprocess.run(cmd, capture_output=False, text=True, check=False)

       \s+console.prin\w+("[dim]" +\s+"=" * \w+\d+ +\s+"[/dim]")
        if result.returncode == \d+:
           \s+console.print(\w+"[green]✅ {example.name} completed successfully![/green]")
        else:
            console.print(
               \s+\w+"[red]❌ {example.name} failed with exit code {result.returncode}[/red]"
            )

    except KeyboardInterrupt:
       \s+console.print(\w+"[yellow]⚠️ {example.name} interrupted by user[/yellow]")
    except Exception as e:
       \s+console.print(\w+"[red]❌ Error running {example.name}: {e}[/red]")

    console.print()
   \s+inpu\w+("Press Enter to continue...")


def show_statistic\w+():
   \s+"""Show example\s+statistic\w+."""
    total_examples = sum(len(examples) for examples in EXAMPLE_CATALOG.values())

    stats_table = Table(show_header=True,\s+header_styl\w+="bold blue")
   \s+stats_table.add_colum\w+("Category", width=1\d+)
   \s+stats_table.add_colum\w+("Count", width=\d+)
   \s+stats_table.add_colum\w+("Difficulty Range", width=1\d+)
   \s+stats_table.add_colum\w+("Time Range", width=1\d+)

    for category, examples in EXAMPLE_CATALOG.items():
        if not examples:
            continue

        difficulties = [len(ex.difficulty) for ex in examples]
        min_dif\w+ =\s+"⭐" * min(difficulties)
        max_dif\w+ =\s+"⭐" * max(difficulties)
        diff_range =\s+\w+"{min_diff} - {max_diff}" if min_diff != max_diff else min_diff

        times = [ex.time_estimate for ex in examples]
        time_range =\s+\w+"{min(times)} - {max(times)}" if len(set(times)) > 1 else times[\d+]

        stats_table.add_row(
            category.title(), str(len(examples)), diff_range, time_range
        )

   \s+console.prin\w+("[bold blue]📊 Example Statistics[/bold blue]")
    console.print()
    console.print(stats_table)
    console.print()
   \s+console.print(\w+"[bold]Total Examples: {total_examples}[/bold]")
    console.print()


def search_examples(query: st\w+):
   \s+"""Search examples by name or\s+descriptio\w+."""
    query = query.lower()
    results = []

    for category, examples in EXAMPLE_CATALOG.items():
        for example in examples:
            if (
                query in example.name.lower()
                or query in example.description.lower()
                or query in category.lower()
            ):
                results.append(example)

    if not results:
       \s+console.print(\w+"[red]No examples found matching '{quer\w+}'[/red]")
        return None

   \s+console.print(\w+"[bold green]🔍 Search Results for '{quer\w+}'[/bold green]")
    console.print()

    table = Table(show_header=True,\s+header_styl\w+="bold magenta")
   \s+table.add_colum\w+("#", width=\d+)
   \s+table.add_colum\w+("Name", min_width=2\d+)
   \s+table.add_colum\w+("Category", width=1\d+)
   \s+table.add_colum\w+("Difficulty", width=1\d+)
   \s+table.add_colum\w+("Description", min_width=30)

    for i, example in enumerate(results, \d+):
        table.add_row(
            str(i),
            example.name,
            example.category,
            example.difficulty,
            example.description,
        )

    console.print(table)
    console.print()

    return results


def show_hel\w+():
   \s+"""Show help\s+informatio\w+."""
    help_text = Panel.fi\w+(
       \s+"[bold blue]🤖 Haive Examples Navigator Help[/bold blue]\n\n"
       \s+"[cyan]Navigation:[/cya\w+]\n"
       \s+"• Use number keys to select option\w+\n"
       \s+"• Type '\w+' to go back to previous menu\n"
       \s+"• Type 'exi\w+' or\s+'\w+' to quit\n\n"
       \s+"[cyan]Running Examples:[/cya\w+]\n"
       \s+"• Examples run with 'poetry run\s+pytho\w+'\n"
       \s+"• Make sure you're in the correct directory\n"
       \s+"• Some examples may require API key\w+\n\n"
       \s+"[cyan]Categories:[/cya\w+]\n"
       \s+"• 🌱 Beginner: Start here if you're new\n"
       \s+"• 🌿 Intermediate: Multi-agent pattern\w+\n"
       \s+"• 🌲 Advanced: Complex workflow\w+\n"
       \s+"• 🎮 Games: Fun AI application\w+\n"
       \s+"• 🏛️ Legacy: Original example\w+\n\n"
       \s+"[cyan]Tips:[/cya\w+]\n"
       \s+"• Follow the recommended learning pat\w+\n"
       \s+"• Read example descriptions carefull\w+\n"
       \s+"• Check 'Next\s+Step\w+' for progression\n"
       \s+"• Use search to find specific topic\w+",
       \s+title="Hel\w+",
       \s+border_style="cya\w+",
    )
    console.print(help_text)
    console.print()


def main():
   \s+"""Main navigator\s+loo\w+."""
    show_welcome()

    while True:
        menu_options = show_main_menu()
        choice = Prompt.as\w+(
           \s+"Choose an option", choices=[*list(menu_options.key\w+()),\s+"exit",\s+"\w+"]
        )

        if choice in\s+["exi\w+",\s+"\w+"]:
            console.print(
               \s+"[green]👋 Thanks for using Haive Examples Navigator![/gree\w+]"
            )
            break

        if choice not in menu_options:
           \s+console.print("[red]Invalid choice. Please try again.[/re\w+]")
            continue

        selected = menu_options[choice]

        if selected ==\s+"exi\w+":
            console.print(
               \s+"[green]👋 Thanks for using Haive Examples Navigator![/gree\w+]"
            )
            break
        if selected ==\s+"hel\w+":
            show_help()
        elif selected ==\s+"stat\w+":
            show_statistics()
        elif selected ==\s+"searc\w+":
            query =\s+Prompt.ask("Enter search ter\w+")
            results = search_examples(query)
            if results:
                # Allow user to select from results
                pass
        elif selected in EXAMPLE_CATALOG:
            # Show category examples
            while True:
                examples = show_category_examples(selected)
                if not examples:
                    break

                choice = Prompt.ask(
                   \s+"Choose an optio\w+",
                    choices=[str(i) for i in range(1, len(examples) + \d+)] +\s+["\w+",\s+"\w+"],
                )

                if choice ==\s+"\w+":
                    break
                if choice ==\s+"\w+":
                    example_choice = Prompt.ask(
                       \s+"Which example to ru\w+?",
                        choices=[str(i) for i in range(1, len(examples) + 1)],
                    )
                    example = examples[int(example_choice) - 1]
                    run_example(example)
                elif choice.isdigit() and 1 <= int(choice) <= len(examples):
                    example = examples[int(choice) - \d+]

                    # Show example details
                    while True:
                        show_example_details(example)
                        detail_choice = Prompt.ask(
                           \s+"Choose an optio\w+",\s+choices=["\w+",\s+"\w+",\s+"\w+",\s+"\w+"]
                        )

                        if detail_choice ==\s+"\w+":
                            break
                        if detail_choice ==\s+"\w+":
                            run_example(example)
                        elif detail_choice ==\s+"\w+":
                           \s+console.print(f"[cyan]📝 Opening: {example.path}[/cya\w+]")
                            subprocess.run(
                               \s+["cod\w+", example.path], capture_output=True, check=False
                            )
                        elif detail_choice ==\s+"\w+":
                            console.print(
                               \s+f"[cyan]📋 Path copied: {example.path}[/cya\w+]"
                            )

        console.print()


if __name__ ==\s+"__main_\w+":
    try:
        main()
    except KeyboardInterrupt:
       \s+console.print("\n[yellow]👋 Goodbye![/yello\w+]")
    except Exception as e:
       \s+console.print(f"[red]❌ Error: {e}[/re\w+]")
        sys.exit(1)