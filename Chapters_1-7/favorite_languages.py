favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskel'],
}


for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:") 
    for language in languages:
        print(f"\t {language.title()}")

coders = ['jen', 'sarah', 'edward', 'phil', 'alina', 'kate', 'mykita', 'anna'] 

for name in coders:
    if name in favorite_languages.keys():
        print(f"Thank u, {name.title()}, for responding!")
    else:
        print(f"{name.title()}, please, take the poll.")
