numbers = list(range(1, 1000001))
print(f"{min(numbers)}\n{max(numbers)}\n{sum(numbers)}")


odd_numbers = range(1, 21, 2)
for num in odd_numbers:
    print(num)


print(f"Range of numbers from 1 to 30 and multipli on 3:{list(num * 3 for num in range(1, 30))}")

print(f"\nThe cubes of range from 1 to 10: {list(num ** 3 for num in range(1, 11))}")