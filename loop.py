# Function to calculate the factorial of a number
def factorial(n):
    result = 1  # Initialize the result to 1
    for i in range(1, n + 1):
        result *= i  # Multiply the result by the current value of i
    return result

# Prompt the user for input
num = int(input("Enter a number: "))

# Check if the input is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and print the factorial
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")
