def formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formated"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = formatted_name('andrii', 'popov', 'oleksiyovich')
coder = formatted_name('alina', 'chernish')

print(f"{musician}, {coder}")