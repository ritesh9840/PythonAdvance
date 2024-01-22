# Using a list comprehension
list_comp = [x**2 for x in range(5)]

# Using a generator expression
gen_expr = (x**2 for x in range(5))

# Printing the results
print("List comprehension:", list_comp)
print("Generator expression:", gen_expr)

# Iterating over the generator expression
for value in gen_expr:
    print(value)
