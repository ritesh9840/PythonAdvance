class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.value = value

    @staticmethod
    def static_method():
        print("This is a static method.")

    def instance_method(self):
        print(f"This is an instance method with value: {self.value}")


# Accessing a static method
MyClass.static_method()

# Creating an instance of the class
obj = MyClass("example")

# Accessing an instance method
obj.instance_method()
