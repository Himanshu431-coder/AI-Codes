import csv

student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'

def display_menu():
    print("\n------------------------------------")
    print(" Welcome to Student Information System")
    print("------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

def add_student():
    print("\n--- Add Student Information ---")
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(student_data)

    print("Data saved successfully!\n")
    input("Press Enter to continue...")

def view_students():
    print("\n--- Student Records ---")
    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            print("\t".join(student_fields))
            print("-" * 50)
            for row in reader:
                if row:
                    print("\t".join(row))
    except FileNotFoundError:
        print("No records found.")
    input("\nPress Enter to continue...")

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    found = False
    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == roll:
                    print("\n--- Student Found ---")
                    for i in range(len(student_fields)):
                        print(f"{student_fields[i].capitalize()}: {row[i]}")
                    found = True
                    break
    except FileNotFoundError:
        pass

    if not found:
        print("Roll No. not found in our database")
    input("Press Enter to continue...")

def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    updated_data = []
    found = False

    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == roll:
                    print("Student Found. Enter new data:")
                    updated_row = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        updated_row.append(value)
                    updated_data.append(updated_row)
                    found = True
                else:
                    updated_data.append(row)

        if found:
            with open(student_database, "w", encoding="utf-8", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Student record updated successfully!")
        else:
            print("Roll No. not found in our database")
    except FileNotFoundError:
        print("No records found to update.")

    input("Press Enter to continue...")

def delete_student():
    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []

    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] != roll:
                    updated_data.append(row)
                elif row and row[0] == roll:
                    student_found = True

        if student_found:
            with open(student_database, "w", encoding="utf-8", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Roll no.", roll, "deleted successfully")
        else:
            print("Roll No. not found in our database")
    except FileNotFoundError:
        print("No records found to delete.")

    input("Press Enter to continue...")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("\nThank you for using our system!")
        break
    else:
        print("Invalid choice. Please try again.")
