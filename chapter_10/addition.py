while True:
    try:
        x = int(input("Please enter first number: "))
        y = int(input("Please enter second number: "))
    except ValueError:
        print("You can't adding non digit")
    else:
        print(f"The result is: {x+y}")
        answer = input("Do u want to continue?(y/n): ")
        if answer == 'n':
            break

