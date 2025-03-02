# 1. How does the format() function help in combining variables with text in Python? 
#    Can you provide a simple example?
#
#    The format() function in Python allows you to insert variables into a string in a structured way. 
#    It replaces placeholders `{}` with values passed as arguments, making string formatting more readable and dynamic.
#
#    Example:

def format_example():
    name = "Alice"
    age = 25
    message = "My name is {} and I am {} years old.".format(name, age)
    return message

# 2. Explain the basic difference between opening a file in 'read' mode ('r') and 'write' mode ('w') in Python.
#    When would you use each?
#
#    In Python, 'r' mode (read mode) is used to open a file for reading. If the file does not exist, 
#    an error (FileNotFoundError) is raised. This mode is useful when you need to retrieve information from a file 
#    without modifying its contents.
#
#    'w' mode (write mode) is used to create or overwrite a file. If the file exists, all its content is erased before writing new data. 
#    This mode is useful when you need to save or update data but do not need to keep the previous content.

def file_modes():
    return ("'r' mode is used to read a file. It raises an error if the file does not exist.\n"
            "'w' mode is used to write to a file. If the file exists, it will be overwritten.")

# 3. Describe what string slicing is in Python. Provide a basic example of extracting a substring from a larger string.
#
#    String slicing in Python is a way to extract specific parts of a string using index positions.
#    The syntax follows the format `string[start:stop:step]`, where:
#      - `start` is the beginning index (inclusive).
#      - `stop` is the ending index (exclusive).
#      - `step` is the interval between characters (optional).
#
#    Example:

def string_slicing():
    text = "Hello, World!"
    substring = text[0:5]  # Extracts 'Hello'
    return substring

# 4. When saving information to a file in Python, what is the purpose of using the 'a' mode instead of the 'w' mode?
#    Provide a straightforward example.
#
#    The 'a' (append) mode in Python allows data to be added to an existing file without deleting its contents.
#    Unlike 'w' mode, which overwrites the file, 'a' mode preserves the original content and places new data at the end.
#
#    This is useful for logging or keeping historical data.
#
#    Example:

def append_example():
    with open("example.txt", "a") as file:
        file.write("This is new data.\n")
    return "Data appended to file."

# 5. Write a simple Python code snippet to open and read a file named "data.txt."
#    How would you handle the case where the file might not exist?
#
#    When reading a file, there's a chance it might not exist. To avoid program crashes, we can use a try-except block to catch the error.
#    If the file exists, it will read and display its contents. If not, a friendly message will be shown instead of an error.
#
#    Example:

def read_file():
    try:
        with open("data.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "The file 'data.txt' does not exist."

# Example calls to functions
if __name__ == "__main__":
    print(format_example())
    print(file_modes())
    print(string_slicing())
    print(append_example())
    print(read_file())
