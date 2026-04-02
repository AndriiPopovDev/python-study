from pathlib import Path

path = Path('guest.txt')

flag = True
content = ""
print("U can stop programm typing 'n'")
while flag:
    answer = input("Hello, what's your name?: ")
    if answer != 'n':
        content += answer
    elif answer == 'n':
        path.write_text(content)
        break

    while True:
        answer = input("Do u have friends? His name is: ") 
        if answer != 'n':
            content += '\n'
            content += answer
        elif answer == 'n':
            flag = False
            path.write_text(content)
            break