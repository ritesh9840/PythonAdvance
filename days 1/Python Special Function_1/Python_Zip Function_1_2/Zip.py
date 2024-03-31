list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
# Convert to list
result_list = list(zipped)
print(result_list)
# Iterate through the zipped result
for item in result_list:
    print(item)
# Output:
# (1, 'a')
# (2, 'b')
# (3, 'c')
