#Unpacking in Function Calls
def my_function(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)
values = [1, 2, 3,4,5]
my_function(*values)
