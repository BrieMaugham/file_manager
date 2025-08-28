# file_manager.py
# Author: Bridie Maugham Dibora
# Description: This program reads a file, handles errors if the file is missing, 
# and writes a modified version of the content to a new file.

def read_file(filename):
    """
    Reads and returns the content of the given file.
    If the file doesn't exist, raises a FileNotFoundError.
    """
    with open(filename, 'r') as file:
        content = file.read()
    return content


def modify_content(content):
    """
    Takes file content, modifies it (example: makes it uppercase), 
    and returns the modified version.
    """
    return content.upper()


def write_file(new_filename, content):
    """
    Writes the modified content to a new file.
    """
    with open(new_filename, 'w') as file:
        file.write(content)
    print(f"✅ Successfully wrote modified content to '{new_filename}'.")


def main():
    """
    Main function to run the program:
    1. Ask for a filename.
    2. Attempt to read it (with error handling).
    3. Modify the content.
    4. Write it to a new file.
    """
    print("📂 Welcome to Bridie's File Manager!")
    filename = input("Enter the filename you want to read: ")

    try:
        # Try to read the content of the file
        content = read_file(filename)
        print(f"📖 Successfully read '{filename}'.")

        # Modify content
        modified = modify_content(content)

        # Create a new filename
        new_filename = "modified_" + filename

        # Write modified content to a new file
        write_file(new_filename, modified)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
