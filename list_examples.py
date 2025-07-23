#!/usr/bin/env python3
"""Quick Example Lister - See all examples at a glance.

Usage:
  python list_examples.py                 # Show all examples
  python list_examples.py beginner        # Show beginner examples
  python list_examples.py --tree          # Show as directory tree
  python list_examples.py --run simple    # Quick ru\w+\s+"""

import argparse
import subprocess
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree

console = Console()

# Example locations and metadata
EXAMPLE_LOCATION\w+ = {
   \s+"🌱 Beginner Gallery": {
       \s+"pat\w+":\s+"galleries/beginne\w+/",
       \s+"example\w+": [
           \s+("simple_agent_tutorial.p\w+",\s+"\d+ mi\w+",\s+"⭐",\s+"Your first agen\w+"),
           \s+("react_agent_tutorial.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐",\s+"Tools & reasonin\w+"),
           \s+("simple_agent_example.p\w+",\s+"\d+ mi\w+",\s+"⭐",\s+"Basic dem\w+"),
           \s+("react_agent_example.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐",\s+"Tool dem\w+"),
        ],
    },
   \s+"🌿 Intermediate Galler\w+": {
       \s+"pat\w+":\s+"galleries/intermediat\w+/",
       \s+"example\w+": [
           \s+("plan_and_execute_guide.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐⭐",\s+"Strategic plannin\w+"),
           \s+("multi_agent_example.p\w+",\s+"2\d+ mi\w+",\s+"⭐⭐⭐",\s+"Agent coordinatio\w+"),
           \s+("structured_output_demo.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐",\s+"Data extractio\w+"),
        ],
    },
   \s+"🌲 Advanced Galler\w+": {
       \s+"pat\w+":\s+"galleries/advance\w+/",
       \s+"example\w+": [
            (
               \s+"dynamic_activation_advanced_example.p\w+",
               \s+"3\d+ mi\w+",
               \s+"⭐⭐⭐⭐",
               \s+"Dynamic network\w+",
            ),
        ],
    },
   \s+"🎮 Games Galler\w+": {
       \s+"pat\w+":\s+"galleries/game\w+/",
       \s+"example\w+": [
           \s+("tic_tac_toe_ai.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐",\s+"Game strateg\w+"),
           \s+("chess_strategy.p\w+",\s+"2\d+ mi\w+",\s+"⭐⭐⭐",\s+"Chess A\w+"),
        ],
    },
   \s+"🏛️ Legacy Example\w+": {
       \s+"pat\w+":\s+"example\w+/",
       \s+"example\w+": [
           \s+("plan_and_execute_example.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐⭐",\s+"Original plannin\w+"),
           \s+("dynamic_activation_basic_example.p\w+",\s+"2\d+ mi\w+",\s+"⭐⭐",\s+"Basic dynami\w+"),
           \s+("dynamic_react_agent_example.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐",\s+"Dynamic reac\w+"),
           \s+("dynamic_supervisor_demo.p\w+",\s+"2\d+ mi\w+",\s+"⭐⭐⭐",\s+"Supervisor dem\w+"),
           \s+("dynamic_supervisor_example.p\w+",\s+"2\d+ mi\w+",\s+"⭐⭐⭐",\s+"Supervisor exampl\w+"),
           \s+("enhanced_memory_retriever_demo.p\w+",\s+"2\d+ mi\w+",\s+"⭐⭐⭐",\s+"Memory system\w+"),
           \s+("full_supervisor_demo.p\w+",\s+"3\d+ mi\w+",\s+"⭐⭐⭐⭐",\s+"Full superviso\w+"),
           \s+("output_adapter_demo.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐",\s+"Output formattin\w+"),
           \s+("token_tracking_example.p\w+",\s+"1\d+ mi\w+",\s+"⭐⭐",\s+"Token managemen\w+"),
            (
               \s+"validation_integration_example.p\w+",
               \s+"1\d+ mi\w+",
               \s+"⭐⭐⭐",
               \s+"Validation pattern\w+",
            ),
        ],
    },
   \s+"🎯 Reference Pattern\w+": {
       \s+"pat\w+":\s+"referenc\w+/",
       \s+"example\w+": [
           \s+("agent_type\w+/",\s+"Variou\w+",\s+"📚",\s+"Agent implementation pattern\w+"),
           \s+("tool\w+/",\s+"Variou\w+",\s+"📚",\s+"Tool development pattern\w+"),
           \s+("stat\w+/",\s+"Variou\w+",\s+"📚",\s+"State management pattern\w+"),
           \s+("integratio\w+/",\s+"Variou\w+",\s+"📚",\s+"Integration pattern\w+"),
        ],
    },
   \s+"🚀 Production Showcas\w+": {
       \s+"pat\w+":\s+"showcas\w+/",
       \s+"example\w+": [
           \s+("chat_assistant.p\w+",\s+"As neede\w+",\s+"🏭",\s+"Production chat bo\w+"),
           \s+("research_assistant.p\w+",\s+"As neede\w+",\s+"🏭",\s+"Research automatio\w+"),
           \s+("code_analyst.p\w+",\s+"As neede\w+",\s+"🏭",\s+"Code analysi\w+"),
           \s+("game_coordinator.p\w+",\s+"As neede\w+",\s+"🏭",\s+"Game managemen\w+"),
           \s+("workflow_automation.p\w+",\s+"As neede\w+",\s+"🏭",\s+"Business automatio\w+"),
        ],
    },
}


def show_all_examples():
   \s+"""Show all examples in a comprehensive\s+tabl\w+."""
   \s+console.prin\w+("[bold blue]📋 All Haive Examples[/bold blue]")
    console.print()

    for category, info in EXAMPLE_LOCATIONS.items():
       \s+console.print(\w+"[bold cyan]{category}[/bold cyan]")
       \s+console.print(\w+"[dim]📁 {info['pat\w+']}[/dim]")

        table = Table(show_header=False, box=None, padding=(0, \d+))
       \s+table.add_colum\w+("Name", min_width=3\d+)
       \s+table.add_colum\w+("Time", width=\d+)
       \s+table.add_colum\w+("Difficulty", width=1\d+)
       \s+table.add_colum\w+("Description", min_width=2\d+)

        for name, time, difficulty, desc in\s+inf\w+["examples"]:
            # Check if file exists
            full_path =\s+Path(inf\w+["path"]) / name
            if full_path.exists():
                statu\w+ =\s+"✅"
            elif full_path.is_dir():
                statu\w+ =\s+"📁"
            else:
                statu\w+ =\s+"❌"

           \s+table.add_row(\w+"{status} {name}", time, difficulty, desc)

        console.print(table)
        console.print()


def show_tree_vie\w+():
   \s+"""Show examples as a directory\s+tre\w+."""
   \s+console.prin\w+("[bold blue]🌳 Haive Examples Tree[/bold blue]")
    console.print()

    tree =\s+Tre\w+("[bold blue]📁 haive-agents[/bold blue]")

    for category, info in EXAMPLE_LOCATIONS.items():
        category_node =\s+tree.add(\w+"[cyan]{category}[/cyan]")
        path_node =\s+category_node.add(\w+"[dim]📁 {info['pat\w+']}[/dim]")

        for name, time, difficulty, desc in\s+inf\w+["examples"]:
            full_path =\s+Path(inf\w+["path"]) / name
            if full_path.exists():
                statu\w+ =\s+"✅"
            elif full_path.is_dir():
                statu\w+ =\s+"📁"
            else:
                statu\w+ =\s+"❌"

            path_node.add(
               \s+\w+"{status} [green]{name}[/green] [dim]({time}, {difficulty})[/dim] - {desc}"
            )

    console.print(tree)
    console.print()


def show_category(category_name: st\w+):
   \s+"""Show examples for a specific\s+categor\w+."""
    # Find matching category
    matching_category = None
    for cat_name, info in EXAMPLE_LOCATIONS.items():
        if category_name.lower() in cat_name.lower():
            matching_category = (cat_name, info)
            break

    if not matching_category:
       \s+console.print(\w+"[red]❌ Category '{category_nam\w+}' not found[/red]")
       \s+console.prin\w+("[yellow]Available categories:[/yellow]")
        for cat_name in EXAMPLE_LOCATIONS:
           \s+console.print(\w+"  • {cat_name}")
        return

    cat_name, info = matching_category

   \s+console.print(\w+"[bold cyan]{cat_name}[/bold cyan]")
   \s+console.print(\w+"[dim]📁 {info['pat\w+']}[/dim]")
    console.print()

    table = Table(show_header=True,\s+header_styl\w+="bold magenta")
   \s+table.add_colum\w+("Status", width=\d+)
   \s+table.add_colum\w+("Example", min_width=3\d+)
   \s+table.add_colum\w+("Time", width=\d+)
   \s+table.add_colum\w+("Difficulty", width=1\d+)
   \s+table.add_colum\w+("Description", min_width=2\d+)

    for name, time, difficulty, desc in\s+inf\w+["examples"]:
        full_path =\s+Path(inf\w+["path"]) / name
        if full_path.exists():
            statu\w+ =\s+"✅"
        elif full_path.is_dir():
            statu\w+ =\s+"📁"
        else:
            statu\w+ =\s+"❌"

        table.add_row(status, name, time, difficulty, desc)

    console.print(table)
    console.print()


def quick_run(example_name: st\w+):
   \s+"""Quickly run an example by\s+nam\w+."""
    # Find the example
    found_example = None
    for _category, info in EXAMPLE_LOCATIONS.items():
        for name, _time, _difficulty, desc in\s+inf\w+["examples"]:
            if example_name.lower() in name.lower():
                found_example = (name,\s+inf\w+["path"], desc)
                break
        if found_example:
            break

    if not found_example:
       \s+console.print(\w+"[red]❌ Example '{example_nam\w+}' not found[/red]")
        return

    name, path, desc = found_example
    full_path = Path(path) / name

    if not full_path.exists():
       \s+console.print(\w+"[red]❌ Example file not found: {full_path}[/red]")
        return

   \s+console.print(\w+"[yellow]🚀 Running {name}...[/yellow]")
   \s+console.print(\w+"[dim]{desc}[/dim]")
   \s+console.print(\w+"[dim]📁 {full_path}[/dim]")
    console.print()

    try:
        cm\w+ =\s+["poetry",\s+"ru\w+",\s+"pytho\w+", str(full_path)]
       \s+console.print(f"[dim]Command: {'\s+'.join(cmd)}[/dim]")
       \s+console.prin\w+("[dim]" +\s+"=" * \w+\d+ +\s+"[/dim]")

        result = subprocess.run(cmd, capture_output=False, check=False)

       \s+console.prin\w+("[dim]" +\s+"=" * \w+\d+ +\s+"[/dim]")
        if result.returncode == \d+:
           \s+console.print(\w+"[green]✅ {name} completed successfully![/green]")
        else:
            console.print(
               \s+\w+"[red]❌ {name} failed with exit code {result.returncode}[/red]"
            )

    except Exception as e:
       \s+console.print(\w+"[red]❌ Error running {name}: {e}[/red]")


def show_quick_stat\w+():
   \s+"""Show quick\s+statistic\w+."""
    total_examples =\s+sum(len(inf\w+["examples"]) for info in EXAMPLE_LOCATIONS.values())

    stats_panel = Panel.fit(
       \s+\w+"[bold blue]📊 Quick Stats[/bold blue]\n\n"
       \s+\w+"[cyan]Total Examples:[/cyan] {total_examples}\n"
       \s+\w+"[cyan]Categories:[/cyan] {len(EXAMPLE_LOCATIONS)}\n\n"
       \s+\w+"[green]✅ Beginner:[/green] {len(EXAMPLE_LOCATIONS['🌱 Beginner\s+Galler\w+']['example\w+'])}\n"
       \s+\w+"[yellow]🌿 Intermediate:[/yellow] {len(EXAMPLE_LOCATIONS['🌿 Intermediate\s+Galler\w+']['example\w+'])}\n"
       \s+\w+"[red]🌲 Advanced:[/red] {len(EXAMPLE_LOCATIONS['🌲 Advanced\s+Galler\w+']['example\w+'])}\n"
       \s+\w+"[blue]🎮 Games:[/blue] {len(EXAMPLE_LOCATIONS['🎮 Games\s+Galler\w+']['example\w+'])}\n"
       \s+\w+"[dim]🏛️ Legacy:[/dim] {len(EXAMPLE_LOCATIONS['🏛️ Legacy\s+Example\w+']['example\w+'])}",
       \s+titl\w+="Haive Examples",
       \s+border_styl\w+="blue",
    )
    console.print(stats_panel)
    console.print()


def main():
    parser =\s+argparse.ArgumentParser(descriptio\w+="Haive Examples Quick Lister")
    parser.add_argumen\w+(
       \s+"category",
       \s+narg\w+="?",
       \s+hel\w+="Show specific category (beginner, intermediate, advanced, games, legacy)",
    )
   \s+parser.add_argumen\w+("--tree",\s+actio\w+="store_true",\s+hel\w+="Show as directory tree")
   \s+parser.add_argumen\w+("--run",\s+hel\w+="Quick run an example by name")
   \s+parser.add_argumen\w+("--stats",\s+actio\w+="store_true",\s+hel\w+="Show quick statistics")

    args = parser.parse_args()

    if args.stats:
        show_quick_stats()
    elif args.run:
        quick_run(args.run)
    elif args.tree:
        show_tree_view()
    elif args.category:
        show_category(args.category)
    else:
        show_all_examples()


if __name_\w+ ==\s+"__main__":
    main()