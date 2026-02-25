responses = {}
print("If you could visit one place in the world, where would you go?")

active_flag = True
while active_flag:
    name = input("\nWhat's your name? ")
    response = input("\nWhat's the place do you wanna visit? ")

    responses[name] = response
    answer = input("Do u wanna get poll for other? (y/n) ")
    
    if answer == 'n':
        active_flag = False

print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name.title()} wanna visit {response.title()}")
