import os

def find_and_dump_txt_files(directory, output_file):
    with open(output_file, 'w') as output:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.txt'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            output.write(content)
                        print(f"Appended content from {file_path}")
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")

    print(f"All text file content has been appended to {output_file}.")

directory = r'C:\Users\Ande Rakesh\Personal'  # Change to the directory you want to search
output_file = r'C:\Users\Ande Rakesh\Personal\output_text_file.txt'  # Name of the file to dump content into

find_and_dump_txt_files(directory, output_file)
