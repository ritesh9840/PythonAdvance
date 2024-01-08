class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

    def __repr__(self):
        return f"MyClass(value={self.value})"


my_instance = MyClass(value=42)

# Using str() function
print(str(my_instance))  # Outputs: "MyClass instance with value: 42"

# Using repr() function
print(repr(my_instance))  # Outputs: "MyClass(value=42)"


# It's worth noting that if __str__ is not defined in a class, 
# Python will use the __repr__ method as a fallback when str() is called. 
# However, it's good practice to provide both methods 
# for clarity and specificity in their intended use cases.
