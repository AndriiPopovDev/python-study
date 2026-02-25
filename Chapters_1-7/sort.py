cars = ['bmw', 'mersedes', 'honda', 'suzuki', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(f"\nHere is the original list: {cars},\n there is the sorted: {sorted(cars)},\n and back original {cars}")
cars.reverse()
print(f"\n{cars}")
print(len(cars))