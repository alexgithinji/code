def register_student():
    student = {}  # Create an empty dictionary to store student information

    print("Student Registration")
    student["name"] = input("Enter student's full name: ")
    student["age"] = int(input("Enter student's age: "))
    student["grade"] = int(input("Enter student's grade: "))
    student["contact"] = input("Enter student's contact information: ")

    return student


def main():
    students = []  # Create a list to store registered students

    while True:
        print("\nOptions:")
        print("1. Register a new student")
        print("2. Display registered students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_student = register_student()
            students.append(new_student)
            print("Student registered successfully!")

        elif choice == "2":
            print("\nRegistered Students:")
            for idx, student in enumerate(students, start=1):
                print(f"\nStudent {idx}:")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Grade: {student['grade']}")
                print(f"Contact: {student['contact']}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
