from InquirerPy import prompt, inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from rich.console import Console
from rich.progress import Progress 
import time

console = Console()

# Display a formatted welcome message with Rich
console.print(
    "[bold yellow]Hello, welcome to the Readme generator![/bold yellow]\n",
    "🤓 \n",
)

# Get user input with Inquirer
questions = [
    {"type": "input", "name": "project", "message": "What is your Project Name?"},
    {"type": "input", "name": "description", "message": "What is your Project about?"},
]
answers = prompt(questions)

def main():
    questions = [
        {
            "type": "list",
            "message": "Add a license for the repo?",
            "choices": ["Choose license", Choice(value=None, name="None")],
            "default": None,
        },
        {
            "type": "list",
            "message": "Select the license:",
            "choices": [
                Choice("licence-type", name="Apache License 2.0"),
                Choice("licence-type", name="GNU General Public License v3.0"),
                Choice("licence-type", name="MIT License"),
                Choice("licence-type", name="BSD 2-Clause 'Simplified' License"),
                Choice("licence-type", name="BSD 3-Clause 'New' or 'Revised' License"),
                Choice("licence-type", name="Boost Software License 1.0"),
                Choice("licence-type", name="Creative Commons Zero v1.0 Universal"),
                Choice("licence-type", name="Eclipse Public License 2.0"),
                Choice("licence-type", name="GNU Affero General Public License v3.0"),
                Choice("licence-type", name="GNU General Public License v2.0"),
                Choice("licence-type", name="GNU Lesser General Public License v2.1"),
                Choice("licence-type", name="Mozilla Public License 2.0"),
                Choice("licence-type", name="The Unilicense"),
            ],
            "multiselect": False,
            "transformer": lambda result: f"{len(result)} licence{'s' if len(result) > 1 else ''} selected",
            "when": lambda result: result[0] is not None,
        },
    ]

    result = prompt(questions=questions)


if __name__ == "__main__":
    main()

# Uses Rich to show a progress bar then a confirmation message
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for _ in range(10):
        time.sleep(0.1)
        progress.update(task, advance=10)

console.print("[bold green]Your Readme markdown file is ready![/bold green] ✅")