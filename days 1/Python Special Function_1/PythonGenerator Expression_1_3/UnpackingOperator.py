def square_numbers(n):
    for i in range(n):
        yield i ** 2

# Using the generator in a loop
for square in square_numbers(5):
    print(square)

gen = square_numbers(3)
print(next(gen))  # prints 0
print(next(gen))  # prints 1
print(next(gen))  # prints 4
