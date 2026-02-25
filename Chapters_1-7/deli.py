sandwich_orders = ['hamburger', 'pastrami', 'sand wich', 'pastrami', 'kfcwich', 'pastrami'] 
finished_sandwiches = []


print("\nDeli has ran out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Ready sandwiches ---")
for sandwich in finished_sandwiches:
    print(sandwich.title())
