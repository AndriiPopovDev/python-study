promt = "\n Pleas enter the name of a city you have visited"
promt += "\n (Enter 'quit' when u are finished.) "

while True:
    city = input(promt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")