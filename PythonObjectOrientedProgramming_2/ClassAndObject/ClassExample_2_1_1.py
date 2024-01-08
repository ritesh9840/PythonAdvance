class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #In Python, you can convert an object to a string by implementing 
    # the __str__ method in the class . 
    # The __str__ method is called when the str() function
    # or the print() function is used with an object. Here's an example:
    
    def __str__(self):
        return f"Name: {self.name} \n and Age : {self.age}"


# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", age=3)
print(my_dog)