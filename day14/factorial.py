def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: calculate factorial of n by multiplying n with factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Test the factorial function with a number
number = 5
result = factorial(number)
print("Factorial of", number, "is:", result)

