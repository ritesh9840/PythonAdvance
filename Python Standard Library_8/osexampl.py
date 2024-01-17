import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Join path components to create a complete path
path1 = "folder1"
path2 = "folder2"
complete_path = os.path.join(path1, path2, "file.txt")
print("Complete Path:", complete_path)

# Check if a path exists
path_to_check = "/path/to/some/file.txt"
exists = os.path.exists(path_to_check)
print(f"Does the path exist? {exists}")

# Check if a path is a file or a directory
is_file = os.path.isfile(path_to_check)
is_directory = os.path.isdir(path_to_check)
print(f"Is it a file? {is_file}")
print(f"Is it a directory? {is_directory}")

# Split a path into the directory and file components
directory, filename = os.path.split(path_to_check)
print("Directory:", directory)
print("Filename:", filename)
