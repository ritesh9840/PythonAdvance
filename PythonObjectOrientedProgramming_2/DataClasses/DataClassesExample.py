from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    city: str


# Creating instances of the Person class
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "San Francisco")

# Accessing attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Printing the object representation
print(person1)  # Output: Person(name='Alice', age=25, city='New York')
print(person2)  # Output: Person(name='Bob', age=30, city='San Francisco')
