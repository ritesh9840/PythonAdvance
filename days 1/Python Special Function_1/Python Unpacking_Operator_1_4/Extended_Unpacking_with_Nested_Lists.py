#Extended Unpacking with Nested Lists:

nested_list = [1, [2, 3], 4]
a, (b, c), d = nested_list

print(a)  # 1
print(b)  # 2
print(c)  # 3
print(d)  # 4
