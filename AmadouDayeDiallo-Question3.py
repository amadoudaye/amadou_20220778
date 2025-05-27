students = [("Alice", 85), ("Bob", 78), ("Charlie", 92)]

# Convert to dictionary
student_dict = dict(students)

# Filter students with score > 80 using dictionary comprehension
filtered_dict = {name: score for name, score in student_dict.items() if score > 80}

# Extract just the names using list comprehension
names_above_80 = [name for name in filtered_dict]

print("Filtered dictionary:", filtered_dict)
print("Names of students who scored above 80:", names_above_80)
#this program converts the list of tuples to a dictionary with dict().
#then the program filters students with scores above 80 using dictionary comprehension.
#and finally it extracts the names using list comprehension.