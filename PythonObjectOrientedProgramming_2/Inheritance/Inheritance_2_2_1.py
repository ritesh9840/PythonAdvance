class Animal:
    def speak(self):
        return "Generic animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


# Creating an instance of the Dog class
my_dog = Dog()
print(my_dog.speak())  # Outputs: "Woof!"
