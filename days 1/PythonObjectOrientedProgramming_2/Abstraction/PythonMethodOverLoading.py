class OverloadingExample:

    def __init__(self, *args):
        if len(args) == 0:
            self.default_constructor()
        elif len(args) == 1:
            self.constructor_with_one_arg(args[0])
        elif len(args) == 2:
            self.constructor_with_two_args(args[0], args[1])
        else:
            print("Invalid number of arguments for the constructor.")

    def default_constructor(self):
        print("Default constructor called.")

    def constructor_with_one_arg(self, arg1):
        print("Constructor with one argument called. Argument:", arg1)

    def constructor_with_two_args(self, arg1, arg2):
        print("Constructor with two arguments called. Arguments:", arg1, arg2)

    def method_overloading(self, *args):
        if len(args) == 1:
            self.method_with_one_arg(args[0])
        elif len(args) == 2:
            self.method_with_two_args(args[0], args[1])
        else:
            print("Invalid number of arguments for the method.")

    def method_with_one_arg(self, arg1):
        print("Method with one argument called. Argument:", arg1)

    def method_with_two_args(self, arg1, arg2):
        print("Method with two arguments called. Arguments:", arg1, arg2)


# Create instances using different constructors
example1 = OverloadingExample()
example2 = OverloadingExample(42)
example3 = OverloadingExample("hello", 3.14)
example4 = OverloadingExample("too", "many", "arguments")

# Call methods with different numbers of arguments
example1.method_overloading(10)
example1.method_overloading(10, 20)
example1.method_overloading(10, 20, 30)
