import os

# Specify the directory you want to list (use '.' for the current directory)
directory_path = '.'  # or provide a specific path like 'C:/Users/YourUsername/Documents'

# List all files and folders in the directory
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)
