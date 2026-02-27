def greet_users(names):
    """Print simple greetings for each people"""
    for name in names:
        print(f"Hello {name.title()}!")


usernames = ['pudge', 'lina', 'ricki', 'axe']
greet_users(usernames)