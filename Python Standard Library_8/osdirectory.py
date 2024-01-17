import os

# Create a new directory
new_directory = "example_directory"
os.makedirs(new_directory, exist_ok=True)
print(f"Directory '{new_directory}' created successfully.")

# Get the list of files and subdirectories in a directory
current_directory = os.getcwd()
contents = os.listdir(current_directory)
print(f"Contents of '{current_directory}': {contents}")

# Rename a directory
new_name = "renamed_directory"
os.rename(new_directory, new_name)
print(f"Directory '{new_directory}' renamed to '{new_name}'.")

# Check if a directory exists
directory_to_check = "nonexistent_directory"
exists = os.path.exists(directory_to_check)
print(f"Does the directory '{directory_to_check}' exist? {exists}")

# Remove a directory
directory_to_remove = "directory_to_remove"
os.makedirs(directory_to_remove, exist_ok=True)
os.rmdir(directory_to_remove)
print(f"Directory '{directory_to_remove}' removed successfully.")
