# - Writing a Python script that asks for an integer and prints whether it's a positive, negative, or zero.
# Ask the user for an integer input
num = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# - Writing a Python program that uses a loop to print out the first 10 square numbers (n^2)
# Loop to print the first 10 square numbers
for i in range(1, 11):
    square = i ** 2
    print(square)
