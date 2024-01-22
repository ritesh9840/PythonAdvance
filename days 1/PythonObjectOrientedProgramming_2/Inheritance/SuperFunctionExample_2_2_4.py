class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"


class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the superclass using super()
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"


# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", breed="Labrador")

print(my_dog.name)    # Outputs: "Buddy"
print(my_dog.breed)   # Outputs: "Labrador"
print(my_dog.speak())  # Outputs: "Woof!"
