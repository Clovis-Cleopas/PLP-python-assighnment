# QTN1: Read a file, append content, write to new file

import os

filename = "newfile.txt"

# Ensure the file exists before reading
if not os.path.exists(filename):
    with open(filename, 'w') as file:
        file.write("This is the original content.")
# Read file
with open("newfile.txt", 'r') as file:
    content = file.read()
    print("Original content:")
    print(content)

# Modify by appending content
modified = content + "\nADDED NEW GREAT CONTENT"
print("\nModified content:")
print(modified)

# Write to new file
output = "newfile.txt".rsplit('.', 1)[0] + '_modified.txt'
with open(output, 'w') as file:
    file.write(modified)
    print(f"\nSuccess: Written to {output}")