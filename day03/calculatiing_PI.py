# Creating a Python program that defines a constant for the value of PI and uses it to calculate thecircumference of a circle with a user-given radius.
import math

# Define a constant for the value of PI
PI = math.pi

# Function to calculate circumference
def calculate_circumference(radius):
    circumference = 2 * PI * radius
    return circumference

# Ask the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference using the user-given radius
circumference = calculate_circumference(radius)

# Print the result
print("The circumference of the circle with radius", radius, "is:", circumference)


# Writing a Python program that takes two numbers as input and calculates both their sum and difference.


# Function to calculate sum
def calculate_sum(num1, num2):
    return num1 + num2

# Function to calculate difference
def calculate_difference(num1, num2):
    return num1 - num2

# Ask the user for the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum and difference
sum_result = calculate_sum(num1, num2)
difference_result = calculate_difference(num1, num2)

# Print the results
print("The sum of", num1, "and", num2, "is:", sum_result)
print("The difference between", num1, "and", num2, "is:", difference_result)
