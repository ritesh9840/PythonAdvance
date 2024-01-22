def outer_function(x):
    # This inner function is a closure
    def inner_function(y):
        return x + y
    return inner_function


# Creating closures
closure1 = outer_function(10)
closure2 = outer_function(20)

# Using closures
result1 = closure1(5)  # Result: 10 + 5 = 15
result2 = closure2(5)  # Result: 20 + 5 = 25

print(result1)
print(result2)
