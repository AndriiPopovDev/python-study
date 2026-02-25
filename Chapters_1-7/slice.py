players = ['ronaldu', 'messi', 'mbape', 'shevchenco', 'neymar']

for player in players[-3:]:
    print(player.title())

my_food = ['pizza', 'pasta', 'ravioli']
friends_food = my_food[:]
my_food.append('ice_cream')
friends_food.append('loly_popos')
print(f"\nMy favorite food:{my_food}\nFriend's favorite food:{friends_food}")

print(f"\nThe first 3 items in this list is: {players[:3]}")
print(f"\nThree items from the middle of the list: {players[1:4]}")
print(f"\nThe last three items in the list are: {players[-3:]}")


pizzas = ['margaritta', 'pepperoni', 'franchesko', 'barbecu']
friend_pizza = pizzas[:]

pizzas.append('carbonara')
friend_pizza.append('borsch')
print("\nMy favorite pizza are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizza are:")
for pizza in friend_pizza:
    print(pizza)