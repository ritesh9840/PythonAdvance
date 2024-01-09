gen_expr = (x**2 for x in range(5))
gen_list = list(gen_expr)

# Now you can iterate over the list multiple times
for value in gen_list:
    print(value)
