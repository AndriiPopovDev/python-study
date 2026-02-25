alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_incriment = 1
elif alien_0['speed'] == 'medium':
    x_incriment = 2
else:
    x_incriment = 3
alien_0['x_position'] = alien_0['x_position'] + x_incriment

print(f"New x-position {alien_0['x_position']}")