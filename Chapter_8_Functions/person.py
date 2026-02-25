def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'fist': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person 

musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('andrii', 'popov', '24') 
print(musician)
