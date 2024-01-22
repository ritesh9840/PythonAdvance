import os
# Create a new file and write content to it
file_path = "example_file.txt"
with open(file_path, "w") as file:
    file.write("Hello, this is an example file.\n")
    file.write("Python is awesome!\n")

print(f"File '{file_path}' created and written to successfully.")

# Read content from the file
with open(file_path, "r") as file:
    content = file.read()
    print(f"Content of '{file_path}':\n{content}")

# Append additional content to the file
with open(file_path, "a") as file:
    file.write("Appending more text to the file.\n")

# Read the updated content from the file
with open(file_path, "r") as file:
    updated_content = file.read()
    print(f"Updated content of '{file_path}':\n{updated_content}")

# Get information about the file
file_info = os.stat(file_path)
print(f"File size: {file_info.st_size} bytes")
print(f"Last modified: {file_info.st_mtime}")

# Delete the file
os.remove(file_path)
print(f"File '{file_path}' deleted successfully.")
