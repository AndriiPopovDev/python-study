from pathlib import Path

path = Path('programming.txt')

contents = "Hello world!\n" 
contents += "I like programming\n"
contents += "I like play video games\n"

path.write_text(contents)