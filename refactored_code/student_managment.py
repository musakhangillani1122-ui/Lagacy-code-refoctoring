
students = []


def add_student():
    student_name = input("Enter student name: ")

    try:
        student_marks = int(input("Enter student marks: "))

        students.append({
            "name": student_name,
            "marks": student_marks
        })

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Marks must be a number.")


def show_students():
    print("\nStudent Records:")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("Student Name:", student["name"])
        print("Student Marks:", student["marks"])

    print("Total Students:", len(students))


def search_student():
    search_name = input("Enter student name to search: ")

    student_found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            student_found = True
            break

    if not student_found:
        print("Student not found.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                show_students()

            elif choice == 3:
                search_student()

            elif choice == 4:
                print("Program Closed")
                break

            else:
                print("Invalid choice! Select 1 to 4.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
