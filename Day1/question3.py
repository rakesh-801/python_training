import os

def find_largest_file(directory):
    max_size = 0
    largest_file = ""

    # Walk through the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get the size of the file
                file_size = os.path.getsize(file_path)
                
                # Update if this file is larger
                if file_size > max_size:
                    max_size = file_size
                    largest_file = file_path
            except OSError as e:
                print(f"Error accessing file {file_path}: {e}")

    return largest_file, max_size

# Directory to check
directory = r'C:\Users\Ande Rakesh\Personal'

# Check if the directory is valid
if os.path.isdir(directory):
    print(f"{directory} is a valid directory.\n")
    
    # Find the largest file in the directory
    largest_file, size = find_largest_file(directory)
    
    if largest_file:
        print(f"The largest file is: {largest_file} with size {size} bytes")
    else:
        print("No files found in the directory.")
else:
    print(f"{directory} is not a valid directory.")
