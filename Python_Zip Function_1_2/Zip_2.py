#You can also use zip with more than two iterables:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']

zipped = zip(list1, list2, list3)
result_list = list(zipped)
print(result_list)
# Output: [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]


