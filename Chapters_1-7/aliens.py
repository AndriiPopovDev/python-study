alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = []

for alien_number in range(30):
    new_alien = alien_0.copy()
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")

#print(f"\nTotal number of aliens: {len(aliens)}.")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

print("\n")
for alien in aliens[:5]:
    print(f"{alien}")
print("...")