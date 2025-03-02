import csv

filename = "students.csv"
records = []

def load_records():
    """Load student records from a CSV file."""
    global records
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            records = [(row[0], (row[1], row[2]), float(row[3]), float(row[4])) for row in reader]
        print("Records loaded successfully.")
    except FileNotFoundError:
        print("No existing file found. Starting fresh.")
    except Exception as e:
        print(f"Error loading file: {e}")

def save_file():
    """Save student records to a CSV file and a text file."""
    if not records:
        print("No records to save!")
        return

    # Save to CSV
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
        for record in records:
            writer.writerow([record[0], record[1][0], record[1][1], record[2], record[3]])

    # Save to TXT
    with open("student.txt", "w") as file:
        for record in records:
            file.write(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, "
                       f"Class Standing: {record[2]}, Major Exam: {record[3]}\n")

    print("Student details saved to 'student.txt' and 'students.csv'.")

def save_as(new_filename):
    """Save the records to a new file."""
    with open(new_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
        for record in records:
            writer.writerow([record[0], record[1][0], record[1][1], record[2], record[3]])
    print(f"Records saved as '{new_filename}'.")

def show_all():
    """Display all student records."""
    if not records:
        print("No records found!")
        return
    print("\nStudent Records:")
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, "
              f"Class Standing: {record[2]}, Major Exam: {record[3]}")

def order_by_last_name():
    """Sort records by last name."""
    sorted_records = sorted(records, key=lambda x: x[1][1])
    for record in sorted_records:
        print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, "
              f"Class Standing: {record[2]}, Major Exam: {record[3]}")

def order_by_grade():
    """Sort records by weighted grade (60% Class Standing + 40% Major Exam)."""
    sorted_records = sorted(records, key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)
    for record in sorted_records:
        weighted_grade = (record[2] * 0.6 + record[3] * 0.4)
        print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Weighted Grade: {weighted_grade:.2f}")

def show_student(student_id):
    """Display a specific student's record."""
    for record in records:
        if record[0] == student_id:
            print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, "
                  f"Class Standing: {record[2]}, Major Exam: {record[3]}")
            return
    print("Student not found.")

def add_record():
    """Add a new student record."""
    student_id = input("Enter Student ID (6 digits): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))

    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record():
    """Edit an existing student record."""
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input(f"Enter New First Name ({record[1][0]}): ") or record[1][0]
            last_name = input(f"Enter New Last Name ({record[1][1]}): ") or record[1][1]
            class_standing = input(f"Enter New Class Standing ({record[2]}): ")
            major_exam = input(f"Enter New Major Exam ({record[3]}): ")

            class_standing = float(class_standing) if class_standing else record[2]
            major_exam = float(major_exam) if major_exam else record[3]

            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record():
    """Delete a student record."""
    student_id = input("Enter Student ID to delete: ")
    global records
    new_records = [record for record in records if record[0] != student_id]

    if len(new_records) == len(records):
        print("Student not found.")
    else:
        records = new_records
        print("Record deleted successfully.")

def menu():
    """Display the menu and handle user choices."""
    load_records()
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            load_records()
        elif choice == "2":
            save_file()
        elif choice == "3":
            new_filename = input("Enter new filename: ")
            save_as(new_filename)
        elif choice == "4":
            show_all()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            show_student(student_id)
        elif choice == "8":
            add_record()
        elif choice == "9":
            edit_record()
        elif choice == "10":
            delete_record()
        elif choice == "11":
            save_file()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
