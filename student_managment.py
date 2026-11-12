
students = []
names = []
marks = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    x = int(input("Enter choice: "))

    if x == 1:
        a = input("Enter student name: ")
        b = int(input("Enter student marks: "))

        students.append(a)
        names.append(a)
        marks.append(b)

        print("Student added successfully")
        print("Name:", a)
        print("Marks:", b)

    elif x == 2:
        print("\nStudent Records:")

        for i in range(len(names)):
            print("Student Name:", names[i])
            print("Student Marks:", marks[i])

        print("Total Students:", len(names))

    elif x == 3:
        c = input("Enter student name to search: ")

        for i in range(len(names)):
            if names[i] == c:
                print("Student Found!")
                print("Name:", names[i])
                print("Marks:", marks[i])

    elif x == 4:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")
