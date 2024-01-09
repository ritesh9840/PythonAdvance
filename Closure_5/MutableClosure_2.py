def outer_function():
    count = [0]

    def inner_function():
        count[0] += 1
        return count[0]
    return inner_function


counter = outer_function()
print(counter())  # Output: 1
print(counter())  # Output: 2

