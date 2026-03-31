from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides) 
        
    
"""6-sided die"""
d6 = Die()

results = []
for _ in range(10):
    results.append(d6.roll_die())
print("10 rolls of a 6-sided die:")
print(results)


"""10-sided die"""
print("\n")
d10 = Die(sides=10)

results = []
for _ in range(10):
    results.append(d10.roll_die())
print("10 rolls of a 10-sided die:")
print(results)


"""20-sided die"""
print("\n")
d20 = Die(sides=20)

results = []
for _ in range(10):
    results.append(d20.roll_die())
print("10 rolls of a 20-sided die:")
print(results)

