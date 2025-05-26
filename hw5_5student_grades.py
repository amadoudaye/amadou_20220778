students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 75],
    "Charlie": [79, 85, 82]
}

def add_student(name, grades):
    """Adds a new student to the dictionary."""
    if name in students:
        print(f"{name} already exists.")
    else:
        students[name] = grades
        print(f"Added {name} with grades {grades}.")

def update_grades(name, new_grades):
    """Updates grades for an existing student."""
    if name in students:
        students[name] = new_grades
        print(f"Updated grades for {name} to {new_grades}.")
    else:
        print(f"Student {name} not found.")

def print_average_grades():
    """Calculates and prints average grade for each student."""
    print("\nAverage Grades:")
    for name, grades in students.items():
        if grades:
            average = sum(grades) / len(grades)
            print(f"{name}: {average:.2f}")
        else:
            print(f"{name}: No grades available.")

add_student("Diana", [91, 89, 95])
update_grades("Alice", [88, 90, 93])
print_average_grades()