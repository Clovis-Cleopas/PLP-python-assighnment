# QTN2: Prompt for filename and handle file errors
filename = input("Enter filename (e.g., input.txt): ").strip()

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File read successfully:")
        print(content)
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
except (PermissionError, IOError) as e:
    print(f"Error: Cannot read '{filename}' - {e}")