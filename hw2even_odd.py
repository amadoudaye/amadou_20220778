user_input = input("Enter a number: ")

try:
    number = float(user_input)

    if number.is_integer():
        if int(number) % 2 == 0:
            print(f"{int(number)} is even.")
        else:
            print(f"{int(number)} is odd.")
    else:
        print(f"{number} is not an integer, so it cannot be classified as even or odd.")
except ValueError:
    print("Invalid input. Please enter a valid number.")