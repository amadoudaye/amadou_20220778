numbers = []
for i in range(5):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

print("\nOriginal list of numbers:", numbers)

sorted_numbers = sorted(numbers)
print("Sorted list (ascending):", sorted_numbers)

largest = max(sorted_numbers)
sorted_numbers.remove(largest)
print(f"Largest number ({largest}) removed.")

print("Updated list:", sorted_numbers)

if sorted_numbers:
    average = sum(sorted_numbers) / len(sorted_numbers)
    print(f"Average of remaining numbers: {average:.2f}")