guest_list = ['alina', 'vlad', 'max', 'kate']
invite_message = "I've glad to invate u to my diner."

guest_list.remove('max')
guest_list.append('mykita')

guest_list.insert(0, 'max')
guest_list.insert(2, 'anna')
guest_list.append('julia')

print("\nSorry guys, the table isn't enough big to invate u all")

sr_message = "Sorry for mistake"
popped_guest = guest_list.pop()
print(f"{popped_guest}, {sr_message}.")
popped_guest = guest_list.pop()
print(f"{popped_guest}, {sr_message}.")
popped_guest = guest_list.pop()
print(f"{popped_guest}, {sr_message}.")
popped_guest = guest_list.pop()
print(f"{popped_guest}, {sr_message}.")
popped_guest = guest_list.pop().title()
print(f"{popped_guest}, {sr_message}.")
print(guest_list)

for name in guest_list:
    print(f"{name.title()}, u are still invited!")

del guest_list


#for i in guest_list:
#    print(f"{i.title()}, {invite_message}")

