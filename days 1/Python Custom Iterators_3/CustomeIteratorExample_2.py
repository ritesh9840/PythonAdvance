# Let's create another example of a custom iterator. 
# In this case, we'll implement an iterator for a range of numbers 
# with a specified step

class CustomRangeIterator:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current < self.end) or (self.step < 0 and self.current > self.end):
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration


class CustomRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return CustomRangeIterator(self.start, self.end, self.step)


# Example usage:
custom_range = CustomRange(1, 10, 2)

# Using the custom iterator in a for loop
for value in custom_range:
    print(value)

# Manually using the iterator
iterator = iter(custom_range)
try:
    while True:
        value = next(iterator)
        print(value)
except StopIteration:
    pass
