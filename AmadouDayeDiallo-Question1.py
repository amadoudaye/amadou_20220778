num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
    #Basically the program Takes an input from the user, then checks divisibility using 
    # the modulo operator% then finally prints the appropriate message based on the conditions.