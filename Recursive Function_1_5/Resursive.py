#calculating the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print("Factorial of 5:", result)
