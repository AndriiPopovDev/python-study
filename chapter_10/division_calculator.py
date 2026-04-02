print("Give me two numbers, and I'll divided them")
print("Enter 'q' to quit")

while True:
    first_number = int(input("\nFirst number: "))
    if first_number == 'q':
        break

    second_number = int(input("\nSecond number: "))
    if second_number == 'q':
        break

    try:
        answer = first_number / second_number
    except ZeroDivisionError:
        print("You can't divided by 0")
    else:
        print(answer)
