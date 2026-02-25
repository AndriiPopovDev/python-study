from formatted_name import formatted_name

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")

greet_user('alina')


while True:
    print(f"\nPlase tell me your name")
    print(f"(enter 'q' at any time to quit)")    

    f_name = input(f"\nYour first name: ")
    if f_name == 'q':
        break

    l_name = input(f"\nThe last name please: ")
    if l_name == 'q':
        break

    f_name = formatted_name(f_name, l_name)
    print(f"Hello, {f_name}!")