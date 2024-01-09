def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


# Using the generator to read lines from a file
file_gen = read_file('GenertorExample_1.py')

for line in file_gen:
    print(line)
