from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce with lambda to calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

print(product)
