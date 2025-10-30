import time
from InquirerPy import prompt
from rich.console import Console
from rich.progress import Progress 
from rich_gradient.text import Text 

console = Console()

# Display a formatted welcome message with Rich and rich_gradient
console.print(Text(
        """ 
        \n
    ░██     ░██            ░██ ░██            ░██ 
    ░██     ░██            ░██ ░██            ░██ 
    ░██     ░██  ░███████  ░██ ░██  ░███████  ░██ 
    ░██████████ ░██    ░██ ░██ ░██ ░██    ░██ ░██ 
    ░██     ░██ ░█████████ ░██ ░██ ░██    ░██ ░██ 
    ░██     ░██ ░██        ░██ ░██ ░██    ░██     
    ░██     ░██  ░███████  ░██ ░██  ░███████  ░██ 
                                                                                        
        \n"""),
    Text("🤖 Welcome to Jimmy's Python Readme Maker! 🤖\n"),
    Text("Please enter details for your repository. \n"),
    )

# Get user input with Inquirer
licenses = [
    "Apache License 2.0",
    "GNU General Public License v3.0",
    "MIT License",
    "Creative Commons Zero v1.0 Universal",
    "GNU Lesser General Public License v3",
    "Mozilla Public License 2.0",
    "The Unilicense",
    "None"
]

questions = [
    {"type": "input", "name": "project", "message": "What is your Project Name?"},
    {"type": "input", "name": "description", "message": "What is your Project about?"},
    {"type": "input", "name": "installation", "message": "What are the installation instructions?"},
    {"type": "input", "name": "author", "message": "What is the author name?"},
    {"type": "input", "name": "usage", "message": "How do you want it to be used?"},
    {"type": "input", "name": "contact", "message": "Please provide contact"}, 
    {"type": "list", "name": "license", "message": "Choose a License:", "choices": licenses}  
 ]

answers = prompt(questions)

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
    
___

"""

# Outputs as README_output.md to distinguish from actual readme for repo and assignment submission
with open("README_output.md", 'w') as f:
            f.write(markdown_content)

# Uses Rich to show a progress bar then a confirmation message
if __name__ == "__main__":
    with Progress() as progress:
        console.print("")
        task = progress.add_task("Processing...", total=100)
        for _ in range(10):
            time.sleep(0.1)
            progress.update(task, advance=10)

console.print(Text("Your Readme markdown file is ready! ✅\n"))