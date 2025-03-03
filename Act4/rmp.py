import csv
import os

# Global variable for records
records = []
filename = "students.csv"

def load_records():
    """Load student records from a CSV file or create it if missing."""
    global records
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            records = [(row[0], (row[1], row[2]), float(row[3]), float(row[4])) for row in reader]
        print("Records loaded successfully.")
    except FileNotFoundError:
        print("No existing file found. Creating 'students.csv'...")
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
        records = []

def save_records():
    """Save records to the default CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
        for record in records:
            writer.writerow([record[0], record[1][0], record[1][1], record[2], record[3]])
    print("Records saved successfully.")

def save_as(new_filename):
    """Save records to a new file."""
    with open(new_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
        for record in records:
            writer.writerow([record[0], record[1][0], record[1][1], record[2], record[3]])
    print(f"Records saved as {new_filename} successfully.")

def show_records():
    """Display all student records."""
    print("\nAll Student Records:")
    print("ID       | Name               | Class Standing | Major Exam")
    print("---------------------------------------------------------")
    for record in records:
        print(f"{record[0]:<8} | {record[1][0]} {record[1][1]:<15} | {record[2]:<14} | {record[3]}")

def order_by_last_name():
    """Sort records by last name."""
    sorted_records = sorted(records, key=lambda x: x[1][1])
    for record in sorted_records:
        print(record)

def order_by_grade():
    """Sort records by weighted grade (60% class standing, 40% major exam)."""
    sorted_records = sorted(records, key=lambda x: 0.6 * x[2] + 0.4 * x[3], reverse=True)
    for record in sorted_records:
        print(record)

def show_student_record(student_id):
    """Find and display a student record by ID."""
    for record in records:
        if record[0] == student_id:
            print("\nStudent Found:")
            print(f"ID: {record[0]}\nName: {record[1][0]} {record[1][1]}\nClass Standing: {record[2]}\nMajor Exam: {record[3]}")
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
    print("Student record added successfully.")

def edit_record():
    """Edit an existing student record."""
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student ID not found.")

def delete_record():
    """Delete a student record by ID."""
    student_id = input("Enter Student ID to delete: ")
    global records
    records = [record for record in records if record[0] != student_id]
    print("Record deleted successfully.")

def menu():
    """Display menu and handle user choices."""
    load_records()
    while True:
        print("\nSTUDENT RECORD MANAGEMENT")
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
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            load_records()
        elif choice == "2":
            save_records()
        elif choice == "3":
            new_filename = input("Enter new filename: ")
            save_as(new_filename)
        elif choice == "4":
            show_records()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            show_student_record(student_id)
        elif choice == "8":
            add_record()
        elif choice == "9":
            edit_record()
        elif choice == "10":
            delete_record()
        elif choice == "0":
            print("Exiting...\n")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
menu()
