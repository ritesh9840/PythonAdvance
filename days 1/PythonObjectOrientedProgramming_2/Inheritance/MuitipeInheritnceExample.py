class Animal:
    def speak(self):
        print("Generic animal sound")


class Mammal:
    def give_birth(self):
        print("Giving birth to live young")


class Dog(Animal, Mammal):
    def bark(self):
        print("Woof! Woof!")


class Bat(Animal, Mammal):
    def fly(self):
        print("I can fly!")


# Create instances of the classes
dog = Dog()
bat = Bat()

# Call methods from the multiple parent classes
dog.speak()         # Output: Generic animal sound
dog.give_birth()    # Output: Giving birth to live young
dog.bark()          # Output: Woof! Woof!

bat.speak()         # Output: Generic animal sound
bat.give_birth()    # Output: Giving birth to live young
bat.fly()           # Output: I can fly!

print(Dog.__mro__)
