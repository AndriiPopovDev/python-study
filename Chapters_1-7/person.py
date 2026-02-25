person = {
    'first_name': 'alina',
    'last_name': 'chernish',
    'age': 24,
    'city': 'kyiv',
}

print(
    f"I have a girlfrien, her name is {person['first_name'].title()} {person['last_name'].title()},"
     f" she's {person['age']}, living with me in {person['city'].title()}."
    )


numbers = {
    'alina': 13,
    'anna': 24,
    'vlad': 3,
    'nika': 5,
    'kate': 12
}

for name, num in numbers.items():
    print(f"{name.title()}'s favorite number is {num}.")

"""
glossary = {
    'dictionary': "Dictionary like list with key to value",
    'list': "List is mutable structure",
    'tupe': "Like list but immutable",
    'int': "Opposit to float",
    'float': "Opposit to int",
}

print(f"\n{glossary['list']}")
"""


rivers = {
    'nile': 'africa',
    'dnipro': 'ukraine',
    'amozon': 'south america', 
    'misisipi': 'usa',
    'yangtze': 'china',
}

print("\n")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")