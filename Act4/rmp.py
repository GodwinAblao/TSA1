import csv

# Global variables
records = []
filename = "students.csv"  # Default filename

# Load records from CSV file
def open_file():
    global records
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            records = [
                {
                    "id": row[0],
                    "name": (row[1], row[2]),
                    "class_standing": float(row[3]),
                    "major_exam": float(row[4]),
                }
                for row in reader
            ]
        print(f"File '{filename}' opened successfully.")
    except FileNotFoundError:
        print("No existing file found. Starting with an empty record list.")

# Save records to CSV file
def save_file():
    global filename
    if not records:
        print("No records to save!")
        return

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
        for record in records:
            writer.writerow([record["id"], record["name"][0], record["name"][1], record["class_standing"], record["major_exam"]])

    print(f"File '{filename}' saved successfully.")

# Save As function to save records to a new file
def save_as_file(new_filename):
    global filename
    filename = new_filename
    save_file()

# Show all student records
def show_all_records():
    if not records:
        print("No records available.")
        return
    for record in records:
        print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Class Standing: {record['class_standing']}, Major Exam: {record['major_exam']}")

# Order by last name
def order_by_last_name():
    sorted_records = sorted(records, key=lambda x: x["name"][1])
    for record in sorted_records:
        print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}")

# Order by grade (60% Class Standing + 40% Major Exam)
def order_by_grade():
    sorted_records = sorted(records, key=lambda x: (x["class_standing"] * 0.6 + x["major_exam"] * 0.4), reverse=True)
    for record in sorted_records:
        final_grade = (record["class_standing"] * 0.6 + record["major_exam"] * 0.4)
        print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Final Grade: {final_grade:.2f}")

# Show student record by ID
def show_student_record():
    student_id = input("Enter Student ID: ")
    for record in records:
        if record["id"] == student_id:
            print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Class Standing: {record['class_standing']}, Major Exam: {record['major_exam']}")
            return
    print("Student record not found.")

# Add a student record
def add_record():
    student_id = input("Enter Student ID (6 digits): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))

    record = {
        "id": student_id,
        "name": (first_name, last_name),
        "class_standing": class_standing,
        "major_exam": major_exam
    }

    records.append(record)
    print("Record added successfully!")

# Edit a student record
def edit_record():
    student_id = input("Enter Student ID to edit: ")
    for record in records:
        if record["id"] == student_id:
            print("Editing record:", record)
            record["name"] = (input("Enter New First Name: "), input("Enter New Last Name: "))
            record["class_standing"] = float(input("Enter New Class Standing: "))
            record["major_exam"] = float(input("Enter New Major Exam Grade: "))
            print("Record updated successfully!")
            return
    print("Student record not found.")

# Delete a student record
def delete_record():
    student_id = input("Enter Student ID to delete: ")
    global records
    records = [record for record in records if record["id"] != student_id]
    print("Record deleted successfully!")


# Main Menu
def main_menu():
    while True:
        print("\nSTUDENT RECORD MANAGEMENT SYSTEM")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Student Records")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            new_filename = input("Enter new filename: ")
            save_as_file(new_filename)
        elif choice == "4":
            show_all_records()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            show_student_record()
        elif choice == "8":
            add_record()
        elif choice == "9":
            edit_record()
        elif choice == "10":
            delete_record()
        elif choice == "11":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
