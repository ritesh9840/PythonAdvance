class CustomContainer:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            print(f"{element} not found in the container.")

    def contains_element(self, element):
        return element in self.elements

    def get_elements(self):
        return self.elements


# Example usage:
custom_container = CustomContainer()

# Adding elements to the container
custom_container.add_element(10)
custom_container.add_element(20)
custom_container.add_element(30)

# Displaying the elements in the container
print("Elements in the container:", custom_container.get_elements())

# Checking if an element is present
print("Is 20 present in the container?", custom_container.contains_element(20))
print("Is 40 present in the container?", custom_container.contains_element(40))

# Removing an element from the container
custom_container.remove_element(20)

# Displaying the updated elements in the container
print("Elements in the container after removal:",
      custom_container.get_elements())
