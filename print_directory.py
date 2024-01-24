import os

def print_directory_tree(path, indent=""):
    """Print the directory tree structure up to the second level."""
    if os.path.isdir(path):
        print(indent + f"{os.path.basename(path)}/")
        if indent.count("    ") < 2:  # Limit to 2 levels
            for item in sorted(os.listdir(path)):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    print_directory_tree(item_path, indent + "    ")

# Specify the root directory path
root_directory = "."  # You can replace this with the desired directory

# Print the directory tree up to the second level
print_directory_tree(root_directory)
