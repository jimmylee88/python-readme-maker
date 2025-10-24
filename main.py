import os
import time
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from rich.console import Console
from rich.progress import Progress 

console = Console()

def collect_main_input():
    # Get user input with Inquirer
    questions = [
        {"type": "input", "name": "project", "message": "What is your Project Name?"},
        {"type": "input", "name": "description", "message": "What is your Project about?"},
        {"type": "input", "name": "installation", "message": "What are the installation instructions?"},
        {"type": "input", "name": "usage", "message": "How do you want it to be used?"},
        {"type": "input", "name": "author", "message": "What is the author name?"},
        {"type": "input", "name": "contact", "message": "Please provide contact"},   
    ]

    answers = prompt(questions)

    if answers is None or not answers:
        print("\nReadme generation cancelled")
        exit()

    return answers


def collect_license(current_answers):
    license_questions = [
        {
            "type": "list",
            "name": "add_license",
            "message": "Add a license for the repo?",
            "choices": ["Yes", Choice(value="No License Selected", name="No license")],
            "default": "Yes",
        },

        {
            "type": "list",
            "name": "license_type",
            "message": "Select a license:\n",
            "choices": [
                "Apache License 2.0",
                "GNU General Public License v3.0",
                "MIT License",
                "Creative Commons Zero v1.0 Universal",
                "GNU Lesser General Public License v3",
                "Mozilla Public License 2.0",
                "The Unilicense",
            ],
            "when": lambda answers: answers.get("add_license") == "Yes",
        },
    ]

    # prompt user for license details
    license_answers = prompt(license_questions)

    # merge license answers into main answers
    current_answers.update(license_answers)

    # ensure a license field exists
    if "license_type" not in current_answers:
        current_answers['license'] = "No license selected"
    else:
        current_answers['license'] = current_answers['license_type']

    return current_answers

def generate_markdown(answers):
    markdown_content = f"""# {answers['project']}

## Description
{answers['description']}

## Installation
To get a copy of this up and running, follow these instructions:
```
{answers['installation']}
```

## Usage
{answers['usage']}

## Contact
- {answers['author']}
- {answers['contact']}

## License
This project is licensd under {answers['license']}.
    
"""
    return markdown_content

def save_readme_file(markdown_text, filename="README_output.md"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
    except IOError as e:
        console.print(f"Could not write to file {filename}")
        console.prinit(f"Details: {e}")
        exit()

if __name__ == "__main__":

    # Display a formatted welcome message with Rich
    console.print(
        """
    ░██     ░██            ░██ ░██            ░██ 
    ░██     ░██            ░██ ░██            ░██ 
    ░██     ░██  ░███████  ░██ ░██  ░███████  ░██ 
    ░██████████ ░██    ░██ ░██ ░██ ░██    ░██ ░██ 
    ░██     ░██ ░█████████ ░██ ░██ ░██    ░██ ░██ 
    ░██     ░██ ░██        ░██ ░██ ░██    ░██     
    ░██     ░██  ░███████  ░██ ░██  ░███████  ░██ 
                                                                                        
        \n""",
    "[bold yellow]Welcome to the Readme generator![/bold yellow]\n",
    "Please enter details for your repository. \n",
    )

    # collect_main_input answers
    all_answers = collect_main_input()

    # merge answers from license to main_input
    all_answers = collect_license(all_answers)

    # Generate the markdown content
    readme_markdown = generate_markdown(all_answers)

    # Uses Rich to show a progress bar then a confirmation message
    with Progress() as progress:
        task = progress.add_task("Processing...", total=100)
        for _ in range(10):
            time.sleep(0.1)
            progress.update(task, advance=10)

    # Save the file
    save_readme_file(readme_markdown)

    console.print("[bold green]Your Readme markdown file is ready![/bold green] ✅")