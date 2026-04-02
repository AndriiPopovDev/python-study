from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nHi, what's your name?"
prompt += "\nEnter 'quit' if u're the last person: "

guest_book = []
while True:
    name = input(prompt)
    if name == 'quit':
        break
    
    print(f"Thanks {name.title()}, we'll add you to the guest book")
    guest_book.append(name)

file_string = ''
for name in guest_book:
    file_string += f"{name.title()}\n"

path.write_text(file_string)