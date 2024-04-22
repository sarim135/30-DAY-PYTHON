# - Writing a Python program that calculates the area of a rectangle using variables to store the width and height, provided by user input.
# Get input from the user for width and height
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

# Calculate the area of the rectangle
area = width * height

# Print the result
print("The area of the rectangle is:", area)




# Creating a Python script to convert temperature from Fahrenheit to Celsius using a constant conversion factor.
# Constant conversion factor
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

# Get input from the user for temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Print the result
print("The temperature in Celsius is:", celsius)
