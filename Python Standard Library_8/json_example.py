import json

# Reading from a JSON file
with open("example.json", "r") as json_file:
    data = json.load(json_file)

# Print the loaded JSON data
print("Loaded JSON Data:")
print(data)

# Modify the data (for example, add a new student)
new_student = {"name": "David", "age": 28, "score": 88}
data["students"].append(new_student)

# Writing to a JSON file with updated data
with open("example_updated.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

print("Data written to 'example_updated.json' successfully.")
