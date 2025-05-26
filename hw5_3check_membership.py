# Define a set of prime numbers (you can expand this list as needed)
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is in the set of prime numbers
if num in prime_numbers:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not in the set of known prime numbers.")