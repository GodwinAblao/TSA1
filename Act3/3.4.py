# Open the file in read mode
try:
    with open("student.txt", "r") as file:
        # Read the contents of the file
        content = file.read()

        # Check if the file is empty
        if content.strip():
            print("\nReading Student Information:\n")
            print(content)
        else:
            print("The file is empty. No student records found.")

except FileNotFoundError:
    print("Error: 'students.txt' not found. Please add student details first.")