# Python Readme Maker

## Assignment
Create a tool using Python, to generate README markdown files for GitHub.

Python Libraries used:
- InquirerPy
- Rich
- Rich_gradient

With the python code examples from our class lessons, I was able to use these to form the basis of structuring the Python script. 
The tool asks the user a series of questions, collects the input from answers, and presents it in a visually appealing CLI using Rich and Rich Gradient. It then saves a markdown file ready to be used as a README for a GitHub repository. Please note that the tool outputs the filename as *README_output.md*. This was so that I could still distinguish between output generated from the tool, and this very README that I'm writing now.

I also used this tool for the intro to welcome the user in the CLI.<br>
[ASCII text art generator](https://patorjk.com/software/taag/#p=display&f=Terrace&t=Hello%21&x=none&v=4&h=4&w=80&we=false)
Though I have since learned that there is now a version of Figlet for Python, to allow text input to be automatically generated as ASCII word art. I may have to consider using that in future, as I found the Javascript equivalent quite handy.

## Future iterations
I would maybe consider breaking down the main.py file into separate modules in order to modularise the app, and make it easier to maintain and work with. At the moment, everything is all contained within one big main.py file.

There are also other functions available from InquirerPy that would allow more detailed user answers, and multiple choice questions to be entered. At the moment, it's quite constrained and only works well with short, one line answers. 
<br><br>

## Video walkthrough

https://github.com/user-attachments/assets/978bbfea-a302-441d-9d00-1a2cb82bfc61

<br>

*Example output below this line* 👇

___

<br>

# Project Title

## Description
Tool to help generate markdown files for github repository README

## Installation
To get a copy of this up and running, follow these instructions:
```
python3 main.py
```

## Usage
Answer the questions, and select a licence from the list to populate the markdown template

## Contact
- Jimmy
- github.com/jimmylee88

## License
This project is licensd under Creative Commons Zero v1.0 Universal.
    
