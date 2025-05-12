try:
    days = float(input("Enter the number of days: "))

    minutes = days * 24 * 60
    seconds = days * 24 * 60 * 60

    print(f"{days} days is equal to:")
    print(f"{minutes} minutes")
    print(f"{seconds} seconds")

except ValueError:
    print("Invalid input. Please enter a numeric value.")