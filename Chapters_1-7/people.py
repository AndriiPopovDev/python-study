people = []

persons = {
    'user_0': {
        'first': 'alina',
        'last': 'chernish',
        'age': 24,
        'location': 'kyiv',
    },

    'user_1': {
        'first': 'vlad',
        'last': 'romanov',
        'age': 23,
        'location': 'kyiv oblast',
    },

    'user_2': {
        'first': 'kate',
        'last': 'kisiv',
        'age': 24,
        'location': 'poland',
    },

    }

people.append(persons)

for person, person_info in persons.items():
    full_name = f"{person_info['first']}  {person_info['last']}"
    age = person_info['age']
    location = person_info['location']

    print(f"{full_name.title()}, age is: {age}, location: {location.title()}")


pets = {
    'leonid': {
        'owner': 'sasha',
        'animal type': 'dog',
        'weight': 2,
        'eat': 'chips',
    },

    'dem': {
        'owner': 'sveta',
        'animal type': 'dog', 
        'weight': 5, 
        'eat': 'bubliki',
    },

    'ayko': {
        'owner': 'vlad',
        'animal type': 'parrot',
        'weight': 0.200,
        'eat': 'seeds',
    },
}

print("\n")
for name, info in pets.items():
    owner = info['owner'].title()
    animal_type = info['animal type']
    weight = info['weight']
    eat = info['eat']

    print(f"{name.title()} is {animal_type}, weight is: {weight}, like eat {eat}, owner is {owner}")
