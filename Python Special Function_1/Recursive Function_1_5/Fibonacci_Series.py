def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage:
n_terms = 10
fibonacci_series = fibonacci_iterative(n_terms)
print(f"Fibonacci series of {n_terms} terms:", fibonacci_series)
