# Example lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
scores = [95, 85, 90]

# Use zip to combine lists element-wise
combined_data = zip(names, ages, scores)

# Iterate through the zipped data and print the result
for data in combined_data:
    print(data)
# Recreate the zip object

combined_data = zip(names, ages, scores)
# Unpack the zipped data
unzipped_names, unzipped_ages, unzipped_scores = zip(*combined_data)

# Print the unpacked data
print("Unzipped Names:", unzipped_names)
print("Unzipped Ages:", unzipped_ages)
print("Unzipped Scores:", unzipped_scores)
