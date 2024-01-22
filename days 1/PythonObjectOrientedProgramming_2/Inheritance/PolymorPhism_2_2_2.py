class Animal:
    def speak(self):
        return "Generic animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


# Creating an instance of the Dog class
my_dog = Dog()
print(my_dog.speak())  # Outputs: "Woof!"


def animal_speak(animal):
    return animal.speak()


# Using polymorphism with different classes
my_animal = Animal()
my_dog = Dog()

print(animal_speak(my_animal))  # Outputs: "Generic animal sound"
print(animal_speak(my_dog))     # Outputs: "Woof!"
