class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Snake(Animal):
    pass  # Snake inherits the make_sound method from the Animal class


# Create instances of different classes
generic_animal = Animal()
dog = Dog()
cat = Cat()
snake = Snake()

# Call the make_sound method on each object
generic_animal.make_sound()  # Output: Generic animal sound
dog.make_sound()            # Output: Bark! Bark!
cat.make_sound()            # Output: Meow!
snake.make_sound()          # Output: Generic animal sound (inherited from Animal class)
