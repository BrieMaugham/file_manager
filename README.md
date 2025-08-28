📂 File Manager – Python File Read & Write with Error Handling

I built this File Manager program to practice Python file handling and exception management. It reads the content of a file, modifies it, and writes the updated version into a new file. I also added robust error handling so the program gracefully responds if a file doesn’t exist or can’t be read.

🚀 Features

✅ Read content from an existing file
✅ Modify the content (uppercase transformation as an example)
✅ Write the modified content into a new file
✅ Handle missing files and invalid inputs with try-except blocks
✅ Give clear feedback to the user at every step

🛠️ How It Works

The program asks the user for a filename to read.

If the file exists, it reads the content.

The program transforms the text (uppercase in this case).

It writes the new content to a new file called modified_<filename>.

If the file doesn’t exist, it shows a friendly error message.

💻 Example Usage
# Run the program
python file_manager.py

# Example Output:
Enter the filename you want to read: example.txt
✅ Successfully read the file!
✅ Modified content has been saved to modified_example.txt


If the file doesn’t exist:

Enter the filename you want to read: notfound.txt
❌ Error: File notfound.txt was not found. Please check the filename and try again.

🧩 Code Structure
file_manager.py
def read_and_modify_file(filename):
    """Read a file, modify its content, and write to a new file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("✅ Successfully read the file!")

        # Modify content: convert to uppercase (can be customized)
        modified_content = content.upper()

        # Write to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"✅ Modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print(f"❌ Error: File {filename} was not found. Please check the filename and try again.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


# Main program
if __name__ == "__main__":
    filename = input("Enter the filename you want to read: ")
    read_and_modify_file(filename)

📦 Requirements

Python 3.x

A text file in the same directory to test with

🔥 Key Learning Outcomes

I practiced reading and writing files in Python.

I improved my skills in error handling with try-except.

I built a reusable function to process files dynamically.

I learned to give users clear feedback during execution.

📝 Future Improvements

🔹 Add more text processing options (lowercase, word count, etc.)
🔹 Allow users to choose where to save the modified file
🔹 Build a simple GUI for drag-and-drop file processing
