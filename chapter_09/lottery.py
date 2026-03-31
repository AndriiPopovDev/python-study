from random import choice

random_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    'a', 'b', 'c', 'd', 'e',
]

winning_ticket = []
while len(winning_ticket) < 4:
    pulled_item = choice(random_list)

    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print(f"\nThe winning ticket is: {winning_ticket}")