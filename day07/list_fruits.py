# Writing a Python program that creates a list of 5 fruits provided by the user and prints each fruit in a for loop.
# Create an empty list to store fruits
fruits = []

# Ask the user to enter 5 fruits
for i in range(5):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

# Print each fruit using a for loop
print("List of fruits:")
for fruit in fruits:
    print(fruit)
