prompt = "\n Greetings! Welcom to theater, how old are you?"
prompt += "\n (Type 'quit' to end the program): "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if int(age) <= 3:
        print("Your ticket are free! Have a good evening")
    elif int(age) >= 3 and int(age) <= 12:
        print("Ticket cost 10$")
    else:
        print("Your tecket cost 15$")