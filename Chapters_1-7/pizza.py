available_toppings = ['mushrooms', 'olives', 'green papers', 'pepperoni', 'pineapple', 'extra cheese']

def make_pizza(requested_toppings):
    added_toppings = []
    unavailable_toppings = []

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            added_toppings.append(requested_topping)
            print(f"{requested_topping.title()} added to your pizza")
        else:
            unavailable_toppings.append(requested_topping)
            print(f"{requested_topping.title()} doesn't exist in our available topings")
    
    return added_toppings, unavailable_toppings

requested_toppings = ['mushrooms', 'extra cheese', 'sausages', 'green papers']
added, unavailable = make_pizza(requested_toppings)

print("\nYour pizza is ready!")
if added:
    print("\nToppings added:")
    for topping in added:
        print(f"- {topping.title()}")

if unavailable:
    print("\nUnavailable toppings:")
    for topping in unavailable:
        print(f"- {topping.title()}")


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"Your order a {pizza['crust']} - crust pizza, with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")


ingredient = ''
while ingredient != 'quit':

    ingredient = input("What the ingredient would u like to add?: ")
    if ingredient == 'quit':
       break 
    else:
       print(f"{ingredient.title()} added!")
