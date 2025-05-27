def calculate_area(length, width):
    return length * width

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = calculate_area(length, width)
print("Area of the rectangle:", area)
#The Function calculate area multiplies length and width. i used input to take user input
#and float for decimal numbers. then the program print out the result.