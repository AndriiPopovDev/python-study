def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inches pizza with the following topings:")

    for topping in toppings:
        print(f"- {topping}")
    

make_pizza(20, 'chilli')
make_pizza(15, 'pepperoni', 'mushrooms', 'bell papper')
