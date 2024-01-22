class MyClass:
    def __init__(self, x):
        self.__x = x  # Private attribute

    def __private_method(self):
        return "This is a private method"

    def public_method(self):
        return f"Public method accessing private attribute: {self.__x}"


# Creating an instance of the class
obj = MyClass(x=42)

# Accessing public method
# Outputs: "Public method accessing private attribute: 42"
print(obj.public_method())

# Attempting to access private attribute directly (not recommended)
# Note: This is possible in Python, but it's against the convention.
print(obj._MyClass__x)  # Outputs: 42

# Attempting to call private method directly (not recommended)
# Note: This is possible, but it's against the convention.
print(obj._MyClass__private_method())  # Outputs: "This is a private method"
