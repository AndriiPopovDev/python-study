prompt = "\nTell me something, and I'll repeat it back to you: "
prompt += "\nType 'quit' to end loop "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    
    else:
        print(message)