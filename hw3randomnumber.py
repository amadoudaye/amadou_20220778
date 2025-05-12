try:
    days = float(input("Enter the number of days: "))

    minutes = days * 24 * 60
    seconds = days * 24 * 60 * 60

    print(f"{days} days is equal to:")
    print(f"{seconds} seconds")
    print(f"{minutes} minutes")

except ValueError:
    print("Invalid input. Please enter a numeric value.")