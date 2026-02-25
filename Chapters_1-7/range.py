numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

for value in range(2, 11, 2):
    print(value)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)
print(f"\n{squares}")

triples = [] 
for value in range(1, 11):
    triples.append(value ** 3)

print(f"\n{triples}")

quadros = [value ** 4 for value in range(1, 11)]
print(f"\n{quadros}")
print(f"\n{list(value ** 4 for value in range(1, 11))}")