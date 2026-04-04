print("Give me two numbers, and I'll divided them")
print("Enter 'q' to quit")

while True:
    try:
        x = int(input("\nFirst number: "))
        if x == 'q':
            break

        y = int(input("\nSecond number: "))
        if y == 'q':
            break
    except ValueError:
        print("I need number for dividing")

        try:
            division = x / y
        except ZeroDivisionError:
            print("You can't divided by 0")
        else:
            print(division)
